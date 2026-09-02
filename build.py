#!/usr/bin/env python3
"""
Builds index.html for Vantage Point from the SKILL.md (+ references/*.md)
files in ../claude-skills-library/skills/ (a sibling folder in the same
shelf, NOT part of this repo). Re-run this after editing any skill there
— it regenerates both the mindmap SVG and the category/skill content,
each between their own START/END markers in index.html, leaving
everything else (head, styles, script tag, flipchart modal) untouched.

Usage: python3 build.py
"""
import re
import html
import math
from pathlib import Path

ROOT = Path(__file__).parent
SKILLS_DIR = ROOT / ".." / "claude-skills-library" / "skills"

SITE_NAME = "Management Unconsulted"  # change here to rename the mindmap's center label

CATEGORIES = [
    ("Strategic analysis", [
        "mece-problem-structuring",
        "swot-strategic-review",
        "porters-five-forces",
        "business-model-canvas",
        "market-sizing-tam-sam-som",
        "competitive-landscape-mapper",
        "root-cause-five-whys",
        "plan-on-a-page",
    ]),
    ("Client & stakeholder deliverables", [
        "executive-summary-writer",
        "consulting-deck-storyliner",
        "board-investor-memo",
        "proposal-sow-drafter",
        "government-tender-response",
        "workshop-agenda-designer",
        "stakeholder-influence-map",
        "stakeholder-engagement-log",
    ]),
    ("Change & program management", [
        "change-impact-assessment",
        "change-management-roadmap",
        "change-readiness-assessment",
        "communication-engagement-plan",
        "raid-log-builder",
        "program-governance-structure",
        "project-retrospective",
        "rapid-decision-framework",
        "benefits-realization-review",
    ]),
    ("Project methodologies", [
        "project-methodology-selector",
        "prince2-project-structuring",
        "pmbok-project-planning",
        "agile-delivery-setup",
        "waterfall-project-plan",
        "babok-requirements-elicitation",
    ]),
    ("Research & intelligence", [
        "competitor-research-brief",
        "discovery-interview-kit",
        "benchmark-comparator",
        "vendor-evaluation-scorecard",
        "data-insights-summarizer",
    ]),
    ("Financial & operational", [
        "unit-economics-breakdown",
        "financial-ratio-reviewer",
        "risk-register-builder",
        "raci-matrix-generator",
        "process-map-simplifier",
        "cost-benefit-analysis",
    ]),
    ("Business-owner day-to-day", [
        "meeting-notes-to-actions",
        "weekly-ops-report",
        "pre-mortem-facilitator",
        "okr-drafter",
        "impact-effort-prioritizer",
        "positioning-pitch-crafter",
        "negotiation-prep",
        "capability-competency-matrix",
    ]),
]

# Short labels for the mindmap (full names are used in the list headers).
MINDMAP_LABELS = {
    "Strategic analysis": "Strategic Analysis",
    "Client & stakeholder deliverables": "Client Deliverables",
    "Change & program management": "Change & Program",
    "Project methodologies": "Project Methods",
    "Research & intelligence": "Research",
    "Financial & operational": "Financial & Ops",
    "Business-owner day-to-day": "Day-to-Day",
}

CATEGORY_COLORS = {
    "Strategic analysis": "#1f6f5c",
    "Client & stakeholder deliverables": "#3a5a78",
    "Change & program management": "#c1502e",
    "Project methodologies": "#a6790f",
    "Research & intelligence": "#6b4a8a",
    "Financial & operational": "#2c3e5c",
    "Business-owner day-to-day": "#8a5a2f",
}

# Inner SVG markup only (no <svg> wrapper), 20x20 viewBox, currentColor.
CATEGORY_ICONS = {
    "Strategic analysis": '<circle cx="10" cy="10" r="7"/><circle cx="10" cy="10" r="3.6"/><circle cx="10" cy="10" r="0.9" fill="currentColor" stroke="none"/>',
    "Client & stakeholder deliverables": '<rect x="3" y="7.5" width="14" height="9" rx="1.5"/><path d="M7.2 7.5V5.8a1.8 1.8 0 011.8-1.8h2a1.8 1.8 0 011.8 1.8v1.7"/>',
    "Change & program management": '<path d="M16 9.5A6 6 0 106 13.2"/><path d="M16 5.5v4h-4"/>',
    "Project methodologies": '<circle cx="4.5" cy="5" r="2"/><circle cx="15.5" cy="5" r="2"/><circle cx="10" cy="15.5" r="2"/><path d="M6.3 6.4l2.8 6.6M13.7 6.4l-2.8 6.6"/>',
    "Research & intelligence": '<circle cx="8.3" cy="8.3" r="5.3"/><path d="M16.2 16.2l-3.7-3.7"/>',
    "Financial & operational": '<path d="M4.5 16V9.5M10 16V4M15.5 16v-5" stroke-linecap="round"/>',
    "Business-owner day-to-day": '<rect x="3" y="3" width="14" height="14" rx="2.5"/><path d="M6.3 10.2l2.1 2.1 5-5" stroke-linecap="round" stroke-linejoin="round"/>',
}

LIST_MARKER = re.compile(r"^(-|\d+\.)\s+(.*)$")
CHECKLIST_MARKER = re.compile(r"^-\s+\[ \]\s+(.*)$")
HEADING_MARKER = re.compile(r"^(#{1,6})\s+(.*)$")
TABLE_ROW = re.compile(r"^\|.*\|$")


def inline(text):
    text = html.escape(text, quote=False)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"`([^`]+?)`", r"<code>\1</code>", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    return text


def render_table(lines):
    rows = [l.strip().strip("|").split("|") for l in lines]
    rows = [[c.strip() for c in r] for r in rows]
    header, _, *body = rows
    out = ["<div class=\"table-wrap\"><table><thead><tr>"]
    out += [f"<th>{inline(c)}</th>" for c in header]
    out.append("</tr></thead><tbody>")
    for r in body:
        out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
    out.append("</tbody></table></div>")
    return "".join(out)


def render_list_block(lines):
    items = []
    checklist = bool(CHECKLIST_MARKER.match(lines[0]))
    ordered = bool(re.match(r"^\d+\.", lines[0]))
    for line in lines:
        cl_m = CHECKLIST_MARKER.match(line)
        m = LIST_MARKER.match(line)
        if cl_m:
            items.append(cl_m.group(1))
        elif m:
            items.append(m.group(2))
        else:
            items[-1] += " " + line.strip()
    if checklist:
        lis = "".join(f'<li class="check"><span class="box" aria-hidden="true"></span>{inline(i)}</li>' for i in items)
        return f'<ul class="checklist">{lis}</ul>'
    tag = "ol" if ordered else "ul"
    lis = "".join(f"<li>{inline(i)}</li>" for i in items)
    return f"<{tag}>{lis}</{tag}>"


def convert(md_text, heading_shift=0):
    blocks = re.split(r"\n\s*\n", md_text.strip())
    out = []
    for block in blocks:
        lines = [l for l in block.split("\n") if l.strip() != ""]
        if not lines:
            continue
        first = lines[0]
        if first.startswith("```"):
            code = "\n".join(lines[1:-1]) if lines[-1].strip() == "```" else "\n".join(lines[1:])
            out.append(f"<pre><code>{html.escape(code)}</code></pre>")
            continue
        hm = HEADING_MARKER.match(first)
        if hm and len(lines) == 1:
            level = min(6, len(hm.group(1)) + heading_shift)
            out.append(f"<h{level}>{inline(hm.group(2))}</h{level}>")
            continue
        if all(TABLE_ROW.match(l) for l in lines) and len(lines) >= 2:
            out.append(render_table(lines))
            continue
        if LIST_MARKER.match(first):
            out.append(render_list_block(lines))
            continue
        out.append(f"<p>{inline(' '.join(l.strip() for l in lines))}</p>")
    return "\n".join(out)


def parse_frontmatter(text):
    parts = text.split("---", 2)
    fm, body = parts[1], parts[2]
    name = re.search(r"^name:\s*(.+)$", fm, re.M).group(1).strip()
    desc = re.search(r"^description:\s*(.+)$", fm, re.M).group(1).strip()
    return name, desc, body.strip()


def title_case(slug):
    caps = {"mece", "raci", "swot", "okr", "okrs", "tam", "sam", "som", "sow",
            "prince2", "pmbok", "babok", "raid", "rfq", "rft"}
    return " ".join(w.upper() if w in caps else w.capitalize() for w in slug.split("-"))


def build_skill(slug, color):
    folder = SKILLS_DIR / slug
    skill_md = (folder / "SKILL.md").read_text()
    name, desc, body = parse_frontmatter(skill_md)
    body_html = convert(body, heading_shift=0)

    refs_html = ""
    refs_dir = folder / "references"
    if refs_dir.is_dir():
        for ref_file in sorted(refs_dir.glob("*.md")):
            ref_text = ref_file.read_text().strip()
            ref_html = convert(ref_text, heading_shift=2)
            refs_html += f'<div class="reference">{ref_html}</div>'

    display_name = title_case(slug)
    search_blob = html.escape(f"{display_name} {desc}".lower(), quote=True)

    return f'''
      <div class="skill" id="{slug}" data-search="{search_blob}" data-skill-name="{html.escape(display_name)}" style="--cat-color:{color}">
        <div class="skill-summary">
          <span class="skill-name">{display_name}</span>
          <span class="skill-desc">{inline(desc)}</span>
          <a class="dl-link" href="dl/{slug}.zip" download title="Download this skill's folder as a .zip" onclick="event.stopPropagation()">&#8681; .zip</a>
        </div>
        <button type="button" class="read-more" data-skill="{slug}">Read more &rarr;</button>
        <div class="skill-body" hidden>
          {body_html}
          {f'<h3 class="ref-heading">Deeper methodology &amp; worked examples</h3>{refs_html}' if refs_html else ''}
        </div>
      </div>'''


def build_content():
    sections = []
    for cat_name, slugs in CATEGORIES:
        cat_id = re.sub(r"[^a-z0-9]+", "-", cat_name.lower()).strip("-")
        color = CATEGORY_COLORS[cat_name]
        icon = CATEGORY_ICONS[cat_name]
        skills_html = "\n".join(build_skill(s, color) for s in slugs)
        sections.append(f'''
    <details class="category" id="{cat_id}" style="--cat-color:{color}">
      <summary class="category-title">
        <svg class="cat-icon" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true">{icon}</svg>
        {cat_name}<span class="category-count">{len(slugs)}</span>
        <a class="dl-link dl-link-cat" href="dl/{cat_id}.zip" download title="Download all {len(slugs)} skills in this category as one .zip" onclick="event.stopPropagation()">&#8681; download {len(slugs)}</a>
      </summary>
      <div class="skill-list">{skills_html}
      </div>
    </details>''')
    return "\n".join(sections)


def build_zips():
    """Generates downloadable .zip files: one per skill, one per category
    (bundling that category's skill folders), and one with everything.
    Each zip preserves the real folder structure (skill-slug/SKILL.md,
    skill-slug/references/*.md) so extracting it and dropping the result
    into ~/.claude/skills/ works exactly like the source library does."""
    import zipfile

    dl_dir = ROOT / "dl"
    dl_dir.mkdir(exist_ok=True)
    for old in dl_dir.glob("*.zip"):
        old.unlink()

    def add_skill(zf, slug):
        folder = SKILLS_DIR / slug
        zf.write(folder / "SKILL.md", f"{slug}/SKILL.md")
        refs_dir = folder / "references"
        if refs_dir.is_dir():
            for ref_file in sorted(refs_dir.glob("*.md")):
                zf.write(ref_file, f"{slug}/references/{ref_file.name}")

    for cat_name, slugs in CATEGORIES:
        for slug in slugs:
            with zipfile.ZipFile(dl_dir / f"{slug}.zip", "w", zipfile.ZIP_DEFLATED) as zf:
                add_skill(zf, slug)

    for cat_name, slugs in CATEGORIES:
        cat_id = re.sub(r"[^a-z0-9]+", "-", cat_name.lower()).strip("-")
        with zipfile.ZipFile(dl_dir / f"{cat_id}.zip", "w", zipfile.ZIP_DEFLATED) as zf:
            for slug in slugs:
                add_skill(zf, slug)

    with zipfile.ZipFile(dl_dir / "all-skills.zip", "w", zipfile.ZIP_DEFLATED) as zf:
        for _, slugs in CATEGORIES:
            for slug in slugs:
                add_skill(zf, slug)

    n_zips = len(list(dl_dir.glob("*.zip")))
    print(f"Wrote {n_zips} zip files into {dl_dir}")


def jitter(seed, lo, hi):
    """Deterministic pseudo-random value in [lo, hi] from a string seed —
    stable across rebuilds (no randomness), used to break the mindmap out
    of a perfect circle: real mindmaps have branches of uneven length."""
    h = 0
    for c in seed:
        h = (h * 131 + ord(c)) % 2147483647
    return lo + (h % 10000) / 10000.0 * (hi - lo)


def text_width(s, font_size):
    """Rough average-character-width estimate for the body sans font,
    used only for collision math below — doesn't need to be exact, just
    a safe-sized upper bound."""
    return len(s) * font_size * 0.58


def wrap_label(name, font_size, max_width=150):
    """Greedy word-wrap onto as many lines as it takes to keep every
    line under `max_width` px at `font_size` — not just a single
    midpoint split. A single split can still leave one half wide (e.g.
    "Competitive" / "Landscape Mapper" — the second half is still 16
    characters), which was the actual biggest driver of mindmap
    crowding that ring/angle tuning alone couldn't fully absorb.
    Wrapping by real pixel width, recomputed whenever `font_size`
    changes, keeps box width bounded regardless of name length or font
    size instead of just pushing harder to route around it."""
    words = name.split(" ")
    lines, current = [], ""
    for w in words:
        candidate = f"{current} {w}".strip()
        if current and text_width(candidate, font_size) > max_width:
            lines.append(current)
            current = w
        else:
            current = candidate
    if current:
        lines.append(current)
    return lines


def build_mindmap():
    """Radial tree: center hub -> category nodes -> skill leaf nodes.
    Two things make this robust rather than hand-tuned:

    1. Leaf radius is jittered per node (deterministic per slug, not
       random) so lines read as hand-drawn — some longer, some shorter —
       rather than a perfect wheel.
    2. Leaf label positions go through an actual iterative collision
       pass: each label's bounding box is estimated, and any pair of
       leaves whose boxes overlap gets pushed further from the hub
       (both of them) and rechecked, repeated until nothing overlaps.
       This is what actually prevents label overlap — angle/radius
       constants below are just reasonable starting points, not a
       guarantee on their own. The final canvas size is computed FROM
       the resolved layout afterward, not guessed up front, so a future
       font-size or skill-count change can't silently leave content
       outside the viewBox.

    Branch/leaf lines start at the HUB'S EDGE (not its center point) and
    the hub is drawn last, painted on top — otherwise lines from
    roughly-opposite branches visibly cross through the hub circle.
    Everything sits inside a #mm-viewport <g> that app.js pans/zooms, and
    every element carries an animation-delay so the whole thing draws
    itself outward from the hub on load (see .mm-pop / .mm-line in
    style.css for the actual keyframes)."""
    r_center = 148  # wide enough for "Unconsulted" (the longest hub-text line) at HUB_FONT below
    r_cat_base, r_cat_jitter = 340, 20
    r_leaf_base, r_leaf_jitter = 640, 30
    RING_GAP, N_RINGS = 108, 4  # leaves cycle through 4 rings by index, see Phase 1
    LEAF_FONT, CAT_FONT = 28, 38
    n = len(CATEGORIES)
    total_skills = sum(len(s) for _, s in CATEGORIES)
    origin = 0.0  # positions computed relative to (0,0); recentered at the end

    # --- Phase 1: initial category + leaf positions (angle & radius) ---
    cats = []
    leaves = []
    for i, (cat_name, slugs) in enumerate(CATEGORIES):
        cat_id = re.sub(r"[^a-z0-9]+", "-", cat_name.lower()).strip("-")
        angle_deg = -90 + i * (360 / n) + jitter(cat_id, -4, 4)
        r_cat = r_cat_base + jitter(cat_id, -r_cat_jitter, r_cat_jitter)
        cats.append({"cat_name": cat_name, "cat_id": cat_id, "angle_deg": angle_deg, "r": r_cat, "index": i})

        n_leaves = len(slugs)
        arc = min(34, 5.4 * (n_leaves - 1)) if n_leaves > 1 else 0
        step = arc / (n_leaves - 1) if n_leaves > 1 else 0
        for j, slug in enumerate(slugs):
            leaf_angle_deg = angle_deg + (j - (n_leaves - 1) / 2) * step + jitter(slug + "a", -1.5, 1.5)
            # Alternate leaves onto two rings (near/far by index parity)
            # instead of relying purely on angle to keep neighbours apart.
            # Two adjacent leaves in the same category sit close in angle
            # by construction (the `step` above) — putting them on the
            # same ring made the collision pass do most of the work,
            # which is what produced a jagged, spiky outline (some leaves
            # pushed far out, most not) instead of a roughly circular
            # one. Staggering rings gives every leaf a same-size head
            # start on separation from its immediate neighbours, so the
            # collision pass below only has to clean up genuine
            # coincidences (e.g. two leaves from different categories
            # landing at a near-identical angle) rather than routine
            # adjacent-label crowding.
            r_leaf = r_leaf_base + (j % N_RINGS) * RING_GAP + jitter(slug, -r_leaf_jitter, r_leaf_jitter)
            name = title_case(slug)
            leaves.append({"slug": slug, "cat_id": cat_id, "cat_index": i, "angle_deg": leaf_angle_deg,
                            "r": r_leaf, "name": name, "lines": wrap_label(name, LEAF_FONT), "j": j})

    # --- Phase 2: iterative collision resolution on leaf label boxes ---
    def leaf_geom(leaf):
        angle = math.radians(leaf["angle_deg"])
        x, y = origin + leaf["r"] * math.cos(angle), origin + leaf["r"] * math.sin(angle)
        anchor = "start" if math.cos(angle) >= -0.05 else "end"
        dx = LEAF_FONT * 0.35 if anchor == "start" else -LEAF_FONT * 0.35
        w = max(text_width(line, LEAF_FONT) for line in leaf["lines"])
        h = LEAF_FONT * 1.3 * len(leaf["lines"])
        if anchor == "start":
            left, right = x + dx, x + dx + w
        else:
            left, right = x + dx - w, x + dx
        top, bottom = y - h / 2, y + h / 2
        return x, y, anchor, dx, (left, top, right, bottom)

    # Each leaf is pushed AT MOST ONCE PER PASS, even if it overlaps
    # several neighbours at once — without this throttle, a leaf sitting
    # in a crowded spot gets shoved by every one of its conflicts in the
    # same pass and the canvas balloons in a couple of iterations.
    # A leaf is also never pushed past MAX_R: a couple of stubborn pairs
    # (long label vs. long label, near a branch boundary) can otherwise
    # keep finding a *new* micro-overlap every single pass for hundreds
    # of passes, each one legitimate but each one making the whole
    # canvas bigger for all 50 leaves to chase a residual few pixels —
    # this is what made an earlier version compute a viewBox so large
    # the doubled font size actually rendered *smaller* on screen than
    # before. Capping growth trades "mathematically zero overlap in
    # every pathological case" for "bounded, predictable canvas size,"
    # which is the right tradeoff here — any leaf that hits the cap gets
    # reported so a real fix (e.g. shortening that skill's display name,
    # or nudging max_arc wider) can be made deliberately if it matters.
    # Only the closer-to-center leaf of an overlapping pair gets pushed
    # (by a bigger step), not both. Two leaves can land at nearly the
    # same angle by coincidence even though they're in different
    # categories entirely (observed: two real skills 0.25° apart) — on
    # a shared ray from the center, pushing BOTH outward by equal steps
    # never separates them, since their radius *gap* (what actually
    # determines their distance apart) never changes. Only moving one
    # of the two grows that gap every pass, which resolves same-ray
    # pairs efficiently instead of chasing them out to a huge radius
    # while never actually fixing anything.
    PAD, STEP, MAX_ITERS = 14, 16, 400
    MAX_R = r_leaf_base + (N_RINGS + 2) * RING_GAP  # safety net against a true pathological blowup, not a primary control
    capped = set()
    for _ in range(MAX_ITERS):
        moved_this_pass = set()
        any_overlap = False
        for i in range(len(leaves)):
            ai = leaf_geom(leaves[i])[4]
            for j in range(i + 1, len(leaves)):
                bj = leaf_geom(leaves[j])[4]
                if not (ai[2] + PAD < bj[0] or bj[2] + PAD < ai[0] or ai[3] + PAD < bj[1] or bj[3] + PAD < ai[1]):
                    any_overlap = True
                    closer, farther = (i, j) if leaves[i]["r"] <= leaves[j]["r"] else (j, i)
                    if closer not in moved_this_pass:
                        if leaves[closer]["r"] < MAX_R:
                            leaves[closer]["r"] = min(MAX_R, leaves[closer]["r"] + STEP * 2)
                            if closer == i:
                                ai = leaf_geom(leaves[i])[4]
                        else:
                            capped.add(leaves[closer]["slug"])
                        moved_this_pass.add(closer)
        if not any_overlap:
            break

    # Fallback: a radial push can't separate two leaves that are BOTH
    # pinned at MAX_R (their radius gap is then zero, however small
    # their angle gap is) — this is exactly what happened to two leaves
    # from different categories that coincidentally landed ~0.25° apart.
    # Once radius room is exhausted, nudge them apart in ANGLE instead,
    # a fraction of a degree at a time, capped at a couple of degrees so
    # it never visibly steals a leaf from its category's arc.
    ANGLE_STEP, MAX_ANGLE_NUDGE = 0.2, 11.0
    for _ in range(800):
        any_overlap = False
        for i in range(len(leaves)):
            ai = leaf_geom(leaves[i])[4]
            for j in range(i + 1, len(leaves)):
                bj = leaf_geom(leaves[j])[4]
                if not (ai[2] + PAD < bj[0] or bj[2] + PAD < ai[0] or ai[3] + PAD < bj[1] or bj[3] + PAD < ai[1]):
                    li, lj = leaves[i], leaves[j]
                    nudge_i = abs(li.get("_nudged", 0)) < MAX_ANGLE_NUDGE
                    nudge_j = abs(lj.get("_nudged", 0)) < MAX_ANGLE_NUDGE
                    if not (nudge_i or nudge_j):
                        continue
                    any_overlap = True
                    if nudge_i:
                        li["angle_deg"] -= ANGLE_STEP
                        li["_nudged"] = li.get("_nudged", 0) - ANGLE_STEP
                    if nudge_j:
                        lj["angle_deg"] += ANGLE_STEP
                        lj["_nudged"] = lj.get("_nudged", 0) + ANGLE_STEP
        if not any_overlap:
            break

    if capped:
        print(f"NOTE: {len(capped)} leaf(s) hit the mindmap radius cap (angle-nudge fallback ran to clean up any residual overlap): {sorted(capped)}")

    final_boxes = [leaf_geom(l)[4] for l in leaves]
    remaining = 0
    for i in range(len(leaves)):
        for j in range(i + 1, len(leaves)):
            a, bb = final_boxes[i], final_boxes[j]
            if not (a[2] < bb[0] or bb[2] < a[0] or a[3] < bb[1] or bb[3] < a[1]):
                remaining += 1
                print(f"WARNING: still overlapping: {leaves[i]['slug']} <-> {leaves[j]['slug']}")
    if not remaining:
        print("Mindmap collision resolution: 0 overlapping leaf labels")

    # --- Phase 3: compute final geometry + required canvas size ---
    max_extent = r_center
    for c in cats:
        angle = math.radians(c["angle_deg"])
        c["x"], c["y"] = origin + c["r"] * math.cos(angle), origin + c["r"] * math.sin(angle)
        c["anchor"] = "start" if math.cos(angle) >= -0.05 else "end"
        label = MINDMAP_LABELS[c["cat_name"]]
        reach = c["r"] + 16 + 8 + text_width(label, CAT_FONT)  # cat_r + dx gap + label width, see Phase 4
        max_extent = max(max_extent, reach)
    for leaf in leaves:
        x, y, anchor, dx, box = leaf_geom(leaf)
        leaf["x"], leaf["y"], leaf["anchor"], leaf["dx"] = x, y, anchor, dx
        max_extent = max(max_extent, abs(box[0]), abs(box[2]), abs(box[1]), abs(box[3]))

    margin = 70
    half = max_extent + margin
    cx = cy = half
    size = half * 2

    # Default view shows the WHOLE mindmap, edge to edge — every
    # category and every leaf visible without panning or zooming. The
    # viewBox was already sized to exactly bound the resolved layout
    # plus a margin (Phase 3 above), so "show everything" is just
    # scale 1 — no separate target-font-size calculation needed. (An
    # earlier version computed default zoom to hit a specific on-screen
    # font size instead; that's a different, reasonable goal, but it
    # directly conflicts with "see everything by default," which is
    # what was actually asked for — keeping the whole layout's *spatial
    # footprint* small, via the tighter MAX_R above, is what keeps this
    # readable instead.)
    default_scale = 1.0

    # --- Phase 4: emit SVG, offsetting every coordinate by (cx, cy) ---
    branch_parts = []
    for c in cats:
        color = CATEGORY_COLORS[c["cat_name"]]
        label = MINDMAP_LABELS[c["cat_name"]]
        angle = math.radians(c["angle_deg"])
        catx, caty = cx + c["x"], cy + c["y"]
        branch_delay = 200 + c["index"] * 70
        hub_edge_x, hub_edge_y = cx + r_center * math.cos(angle), cy + r_center * math.sin(angle)
        line_len = math.hypot(catx - hub_edge_x, caty - hub_edge_y)

        branch_parts.append(
            f'<line x1="{hub_edge_x:.1f}" y1="{hub_edge_y:.1f}" x2="{catx:.1f}" y2="{caty:.1f}" stroke="{color}" '
            f'stroke-width="3" opacity="0.6" class="mm-line" '
            f'style="--len:{line_len:.1f}px; animation-delay:{branch_delay}ms"/>'
        )

        cat_node_delay = branch_delay + 320
        cat_leaves = [l for l in leaves if l["cat_id"] == c["cat_id"]]
        for j, leaf in enumerate(cat_leaves):
            lx, ly = cx + leaf["x"], cy + leaf["y"]
            leaf_line_delay = cat_node_delay + 200 + j * 30
            leaf_node_delay = leaf_line_delay + 200
            leaf_line_len = math.hypot(lx - catx, ly - caty)
            branch_parts.append(
                f'<line x1="{catx:.1f}" y1="{caty:.1f}" x2="{lx:.1f}" y2="{ly:.1f}" stroke="{color}" '
                f'stroke-width="1.6" opacity="0.4" class="mm-line" '
                f'style="--len:{leaf_line_len:.1f}px; animation-delay:{leaf_line_delay}ms"/>'
            )
            branch_parts.append(f'<a href="#{leaf["slug"]}" class="mm-leaf" data-cat="{c["cat_id"]}">')
            branch_parts.append(f'<g class="mm-pop" style="transform-origin:{lx:.1f}px {ly:.1f}px; animation-delay:{leaf_node_delay}ms">')
            branch_parts.append(f'<circle cx="{lx:.1f}" cy="{ly:.1f}" r="4.5" fill="var(--paper)" stroke="{color}" stroke-width="2"/>')
            line_h = LEAF_FONT * 1.3
            n_lines = len(leaf["lines"])
            for li, line in enumerate(leaf["lines"]):
                text_y = ly + 6.5 - (n_lines - 1) * line_h / 2 + li * line_h
                branch_parts.append(f'<text x="{lx+leaf["dx"]:.1f}" y="{text_y:.1f}" text-anchor="{leaf["anchor"]}" font-size="{LEAF_FONT}" fill="var(--ink-soft)">{html.escape(line)}</text>')
            branch_parts.append('</g></a>')

        cat_r = 16
        cat_dx = cat_r + 8 if c["anchor"] == "start" else -(cat_r + 8)
        branch_parts.append(f'<a href="#{c["cat_id"]}" class="mm-node">')
        branch_parts.append(f'<g class="mm-pop" style="transform-origin:{catx:.1f}px {caty:.1f}px; animation-delay:{cat_node_delay}ms">')
        branch_parts.append(f'<circle cx="{catx:.1f}" cy="{caty:.1f}" r="{cat_r}" fill="{color}"/>')
        icon_size = cat_r * 1.3
        branch_parts.append(f'<svg x="{catx-icon_size/2:.1f}" y="{caty-icon_size/2:.1f}" width="{icon_size:.1f}" height="{icon_size:.1f}" viewBox="0 0 20 20" fill="none" stroke="var(--paper)" stroke-width="1.6">{CATEGORY_ICONS[c["cat_name"]]}</svg>')
        branch_parts.append(f'<text x="{catx+cat_dx:.1f}" y="{caty+CAT_FONT*0.32:.1f}" text-anchor="{c["anchor"]}" font-size="{CAT_FONT}" font-weight="700" fill="{color}">{html.escape(label)}</text>')
        branch_parts.append('</g></a>')

    # Hub is emitted LAST so it paints on top of every branch/leaf line —
    # combined with lines starting at its edge (not center) above, this
    # guarantees nothing is ever visible crossing through it. A slow,
    # subtle pulse ring keeps the finished mindmap from reading as inert
    # once the entrance animation settles.
    hub_parts = [f'<g class="mm-pop mm-hub" style="transform-origin:{cx}px {cy}px; animation-delay:0ms">']
    hub_parts.append(f'<circle class="mm-pulse-ring" cx="{cx}" cy="{cy}" r="{r_center}" fill="none" stroke="var(--ink)"/>')
    hub_parts.append(f'<circle cx="{cx}" cy="{cy}" r="{r_center}" fill="var(--paper)" stroke="var(--ink)" stroke-width="3"/>')
    HUB_FONT, HUB_SUB_FONT = 42, 17
    name_lines = SITE_NAME.split(" ")
    if len(name_lines) > 1:
        mid = len(name_lines) // 2 + len(name_lines) % 2
        line1, line2 = " ".join(name_lines[:mid]), " ".join(name_lines[mid:])
        hub_parts.append(f'<text x="{cx}" y="{cy-21}" text-anchor="middle" font-family="Source Serif 4, Georgia, serif" font-weight="600" font-size="{HUB_FONT}" fill="var(--ink)">{html.escape(line1)}</text>')
        hub_parts.append(f'<text x="{cx}" y="{cy+21}" text-anchor="middle" font-family="Source Serif 4, Georgia, serif" font-weight="600" font-size="{HUB_FONT}" fill="var(--ink)">{html.escape(line2)}</text>')
        sub_y = cy + 45
    else:
        hub_parts.append(f'<text x="{cx}" y="{cy-8}" text-anchor="middle" font-family="Source Serif 4, Georgia, serif" font-weight="600" font-size="{HUB_FONT+3}" fill="var(--ink)">{html.escape(SITE_NAME)}</text>')
        sub_y = cy + 26
    hub_parts.append(f'<text x="{cx}" y="{sub_y}" text-anchor="middle" font-family="ui-monospace, monospace" font-size="{HUB_SUB_FONT}" fill="var(--muted)">{total_skills} skills</text>')
    hub_parts.append('</g>')

    inner = "\n".join(['<g id="mm-viewport">'] + branch_parts + hub_parts + ['</g>'])
    return f'''<svg id="mm-svg" viewBox="0 0 {size:.0f} {size:.0f}" data-default-scale="{default_scale:.3f}" role="img" aria-label="Mindmap of {SITE_NAME}: {total_skills} skills across {n} categories, radiating from a central hub. Click any category or skill to jump to it below.">
{inner}
</svg>'''


def build():
    index_path = ROOT / "index.html"
    current = index_path.read_text()

    current = re.sub(
        r"(<!-- MINDMAP:START -->)(.*)(<!-- MINDMAP:END -->)",
        lambda m: m.group(1) + "\n" + build_mindmap() + "\n    " + m.group(3),
        current, flags=re.S,
    )
    current = re.sub(
        r"(<!-- CONTENT:START -->)(.*)(<!-- CONTENT:END -->)",
        lambda m: m.group(1) + build_content() + "\n    " + m.group(3),
        current, flags=re.S,
    )
    index_path.write_text(current)
    total = sum(len(s) for _, s in CATEGORIES)
    print(f"Wrote {total} skills across {len(CATEGORIES)} categories, plus the mindmap, into {index_path}")
    build_zips()


if __name__ == "__main__":
    build()
