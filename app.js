(function () {
  // --- Theme toggle: explicit light/dark choice persisted per-visitor.
  // The <head> inline script (see index.html) already applied any
  // stored choice before first paint; this just wires up the button and
  // keeps the icon + aria-label in sync with the current state.
  var themeBtn = document.getElementById("theme-toggle");
  function currentTheme() {
    var stored = document.documentElement.getAttribute("data-theme");
    if (stored === "light" || stored === "dark") return stored;
    return window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }
  function syncThemeButton() {
    var isDark = currentTheme() === "dark";
    themeBtn.setAttribute("aria-label", isDark ? "Switch to light theme" : "Switch to dark theme");
    themeBtn.title = isDark ? "Switch to light theme" : "Switch to dark theme";
  }
  themeBtn.addEventListener("click", function () {
    var next = currentTheme() === "dark" ? "light" : "dark";
    document.documentElement.setAttribute("data-theme", next);
    try { localStorage.setItem("vantage-point-theme", next); } catch (e) {}
    syncThemeButton();
  });
  syncThemeButton();

  var input = document.getElementById("search");
  var empty = document.getElementById("empty-state");
  var emptyQuery = document.getElementById("empty-query");
  var categories = Array.prototype.slice.call(document.querySelectorAll(".category"));

  function filter() {
    var q = input.value.trim().toLowerCase();
    var anyVisible = false;

    categories.forEach(function (cat) {
      var skills = cat.querySelectorAll(".skill");
      var catHasMatch = false;
      skills.forEach(function (skill) {
        var match = !q || skill.getAttribute("data-search").indexOf(q) !== -1;
        skill.hidden = !match;
        if (match) catHasMatch = true;
      });
      cat.hidden = !catHasMatch;
      if (catHasMatch) anyVisible = true;
      if (catHasMatch && q) cat.open = true;
    });

    empty.hidden = anyVisible || !q;
    if (!anyVisible && q) emptyQuery.textContent = input.value.trim();
  }

  input.addEventListener("input", filter);

  document.getElementById("expand-all").addEventListener("click", function () {
    document.querySelectorAll(".category").forEach(function (d) { d.open = true; });
  });
  document.getElementById("collapse-all").addEventListener("click", function () {
    document.querySelectorAll(".category").forEach(function (d) { d.open = false; });
  });

  // --- Skill modal: "Read more" (or clicking a skill card) opens the
  // full SKILL.md content in a centered popup instead of expanding
  // inline, since 50 cards expanding in place made the page unwieldy.
  var skillModal = document.getElementById("skill-modal");
  var skillModalTitle = document.getElementById("skill-modal-title");
  var skillModalBody = document.getElementById("skill-modal-body");
  var skillModalDl = document.getElementById("skill-modal-dl");

  function openSkillModal(slug) {
    var el = document.getElementById(slug);
    if (!el || !el.classList.contains("skill")) return;
    skillModalTitle.textContent = el.getAttribute("data-skill-name") || slug;
    skillModalBody.innerHTML = el.querySelector(".skill-body").innerHTML;
    skillModalDl.href = "dl/" + slug + ".zip";
    skillModal.hidden = false;
  }
  function closeSkillModal() { skillModal.hidden = true; }

  document.querySelectorAll(".skill").forEach(function (card) {
    var summary = card.querySelector(".skill-summary");
    var readMore = card.querySelector(".read-more");
    var slug = card.id;
    summary.addEventListener("click", function () { openSkillModal(slug); });
    readMore.addEventListener("click", function () { openSkillModal(slug); });
  });
  skillModal.querySelectorAll("[data-close]").forEach(function (el) {
    el.addEventListener("click", closeSkillModal);
  });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && !skillModal.hidden) closeSkillModal();
  });

  // --- Mindmap: pan + zoom ---
  var canvas = document.getElementById("mm-canvas");
  var svg = document.getElementById("mm-svg");
  var viewport = document.getElementById("mm-viewport");
  // Read the actual viewBox rather than hardcoding it — build.py now
  // computes canvas size dynamically from the resolved layout, so a
  // fixed constant here would drift out of sync with it.
  var vbParts = svg.getAttribute("viewBox").split(" ").map(Number);
  var CX = vbParts[2] / 2, CY = vbParts[3] / 2, VB = vbParts[2];
  // build.py computes this from the actual resolved canvas size, so
  // default zoom stays at a legible on-screen text size regardless of
  // how big/small the canvas ends up (a fixed multiplier here looked
  // right once and then silently went tiny the next time canvas size
  // changed for any reason).
  var DEFAULT_SCALE = parseFloat(svg.getAttribute("data-default-scale")) || 1.0;
  var scale = DEFAULT_SCALE, tx = CX * (1 - scale), ty = CY * (1 - scale);
  // Default (1.0) already shows the whole mindmap, so the useful zoom
  // range is entirely "zoom in further to read one area closely" —
  // little value in zooming out past the point everything's visible.
  var MIN_SCALE = 0.8, MAX_SCALE = 6;

  function applyTransform() {
    viewport.setAttribute("transform", "translate(" + tx.toFixed(1) + "," + ty.toFixed(1) + ") scale(" + scale.toFixed(3) + ")");
  }
  applyTransform();

  function zoomAtPoint(clientX, clientY, factor) {
    var newScale = Math.min(MAX_SCALE, Math.max(MIN_SCALE, scale * factor));
    if (newScale === scale) return;
    var pt = svg.createSVGPoint();
    pt.x = clientX; pt.y = clientY;
    var svgPt = pt.matrixTransform(svg.getScreenCTM().inverse());
    var contentX = (svgPt.x - tx) / scale;
    var contentY = (svgPt.y - ty) / scale;
    tx = svgPt.x - contentX * newScale;
    ty = svgPt.y - contentY * newScale;
    scale = newScale;
    applyTransform();
  }

  document.getElementById("mm-zoom-in").addEventListener("click", function () {
    var r = svg.getBoundingClientRect();
    zoomAtPoint(r.left + r.width / 2, r.top + r.height / 2, 1.25);
  });
  document.getElementById("mm-zoom-out").addEventListener("click", function () {
    var r = svg.getBoundingClientRect();
    zoomAtPoint(r.left + r.width / 2, r.top + r.height / 2, 1 / 1.25);
  });
  document.getElementById("mm-zoom-reset").addEventListener("click", function () {
    scale = DEFAULT_SCALE;
    tx = CX * (1 - scale);
    ty = CY * (1 - scale);
    applyTransform();
  });

  // Mouse-wheel zoom deliberately omitted: it fought with normal page
  // scrolling when the cursor happened to be over the mindmap. Zoom is
  // buttons + drag-to-pan only.

  // Drag to pan. Tracks whether a real drag happened so an accidental
  // click on a leaf/node right after dragging doesn't also navigate.
  var dragging = null;
  var didDrag = false;

  canvas.addEventListener("mousedown", function (e) {
    dragging = { x: e.clientX, y: e.clientY, tx: tx, ty: ty };
    didDrag = false;
    canvas.classList.add("dragging");
  });
  window.addEventListener("mousemove", function (e) {
    if (!dragging) return;
    var dx = e.clientX - dragging.x, dy = e.clientY - dragging.y;
    if (Math.abs(dx) > 3 || Math.abs(dy) > 3) didDrag = true;
    var rect = svg.getBoundingClientRect();
    tx = dragging.tx + dx * (VB / rect.width);
    ty = dragging.ty + dy * (VB / rect.height);
    applyTransform();
  });
  window.addEventListener("mouseup", function () {
    if (dragging) { dragging = null; canvas.classList.remove("dragging"); }
  });

  // Touch support: single-finger pan, two-finger pinch to zoom. The
  // fixed +/-/reset buttons are the only zoom controls on desktop (mouse
  // wheel was tried and removed, see above) but on a phone the mindmap
  // needs to fit 50 labels on a much smaller screen, so pinch is a real
  // gap rather than a nice-to-have there.
  var pinch = null;
  function touchDist(touches) {
    var dx = touches[0].clientX - touches[1].clientX, dy = touches[0].clientY - touches[1].clientY;
    return Math.hypot(dx, dy);
  }
  canvas.addEventListener("touchstart", function (e) {
    if (e.touches.length === 2) {
      dragging = null;
      pinch = { dist: touchDist(e.touches) };
      return;
    }
    if (e.touches.length !== 1) return;
    pinch = null;
    dragging = { x: e.touches[0].clientX, y: e.touches[0].clientY, tx: tx, ty: ty };
    didDrag = false;
  }, { passive: true });
  canvas.addEventListener("touchmove", function (e) {
    if (pinch && e.touches.length === 2) {
      e.preventDefault();
      var newDist = touchDist(e.touches);
      var midX = (e.touches[0].clientX + e.touches[1].clientX) / 2;
      var midY = (e.touches[0].clientY + e.touches[1].clientY) / 2;
      zoomAtPoint(midX, midY, newDist / pinch.dist);
      pinch.dist = newDist;
      return;
    }
    if (!dragging || e.touches.length !== 1) return;
    e.preventDefault(); // stop the page scrolling under a finger that's panning the mindmap
    var dx = e.touches[0].clientX - dragging.x, dy = e.touches[0].clientY - dragging.y;
    if (Math.abs(dx) > 3 || Math.abs(dy) > 3) didDrag = true;
    var rect = svg.getBoundingClientRect();
    tx = dragging.tx + dx * (VB / rect.width);
    ty = dragging.ty + dy * (VB / rect.height);
    applyTransform();
  }, { passive: false });
  canvas.addEventListener("touchend", function (e) {
    if (e.touches.length < 2) pinch = null;
    if (e.touches.length === 0) dragging = null;
  });

  // Zooms/pans the mindmap itself to frame one category's hub node plus
  // every one of its leaves, rather than leaving the whole map at its
  // current zoom. getBBox() on each element returns its box in the
  // *untransformed* viewBox coordinate system (the pan/zoom transform
  // lives on the #mm-viewport <g> that wraps all of this, so it isn't
  // included) — exactly the same space CX/CY/VB and tx/ty already work
  // in, so no separate pixel<->viewBox conversion is needed here.
  var reduceMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  function zoomToCategory(catId) {
    var els = svg.querySelectorAll('.mm-leaf[data-cat="' + catId + '"], .mm-node[href="#' + catId + '"]');
    if (!els.length) return;
    var minX = Infinity, minY = Infinity, maxX = -Infinity, maxY = -Infinity;
    els.forEach(function (el) {
      var b = el.getBBox();
      minX = Math.min(minX, b.x); minY = Math.min(minY, b.y);
      maxX = Math.max(maxX, b.x + b.width); maxY = Math.max(maxY, b.y + b.height);
    });
    var pad = 70;
    minX -= pad; minY -= pad; maxX += pad; maxY += pad;
    var newScale = Math.min(MAX_SCALE, Math.max(MIN_SCALE, VB / Math.max(maxX - minX, maxY - minY)));
    var ccx = (minX + maxX) / 2, ccy = (minY + maxY) / 2;
    if (!reduceMotion) viewport.classList.add("mm-anim");
    scale = newScale;
    tx = CX - ccx * scale;
    ty = CY - ccy * scale;
    applyTransform();
    window.setTimeout(function () { viewport.classList.remove("mm-anim"); }, 600);
  }

  // Mindmap: clicking a leaf opens that skill's popup directly (it's the
  // same "Read more" destination as clicking its card below). Clicking a
  // category node zooms the mindmap in on that category's whole cluster
  // of leaves instead — it also still expands that category's section
  // below (so it's ready when the reader scrolls down) but no longer
  // jumps the page there, since that would immediately scroll away from
  // the zoom this click just performed. Suppressed if the click was
  // actually the end of a pan drag.
  document.querySelectorAll(".mm-leaf").forEach(function (link) {
    link.addEventListener("click", function (e) {
      e.preventDefault();
      if (didDrag) return;
      openSkillModal(link.getAttribute("href").slice(1));
    });
  });
  document.querySelectorAll(".mm-node").forEach(function (link) {
    link.addEventListener("click", function (e) {
      e.preventDefault();
      if (didDrag) return;
      var catId = link.getAttribute("href").slice(1);
      var target = document.getElementById(catId);
      if (target) target.open = true;
      zoomToCategory(catId);
    });
  });

  // Flipchart guide modal
  var modal = document.getElementById("guide-modal");
  var cards = Array.prototype.slice.call(document.querySelectorAll(".flip-card"));
  var dots = Array.prototype.slice.call(document.querySelectorAll(".flip-dot"));
  var prevBtn = document.getElementById("flip-prev");
  var nextBtn = document.getElementById("flip-next");
  var current = 0;

  function showCard(i) {
    current = i;
    cards.forEach(function (c, idx) { c.hidden = idx !== i; });
    dots.forEach(function (d, idx) { d.classList.toggle("active", idx === i); });
    prevBtn.disabled = i === 0;
    nextBtn.textContent = i === cards.length - 1 ? "✓" : "→";
    nextBtn.classList.toggle("flip-btn-done", i === cards.length - 1);
    nextBtn.setAttribute("aria-label", i === cards.length - 1 ? "Done" : "Next");
  }

  function openModal() {
    showCard(0);
    modal.hidden = false;
  }
  function closeModal() {
    modal.hidden = true;
  }

  document.getElementById("open-guide").addEventListener("click", openModal);
  document.querySelectorAll("[data-close]").forEach(function (el) {
    el.addEventListener("click", closeModal);
  });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && !modal.hidden) closeModal();
  });

  prevBtn.addEventListener("click", function () {
    if (current > 0) showCard(current - 1);
  });
  nextBtn.addEventListener("click", function () {
    if (current < cards.length - 1) showCard(current + 1);
    else closeModal();
  });
  dots.forEach(function (dot, idx) {
    dot.addEventListener("click", function () { showCard(idx); });
  });
})();
