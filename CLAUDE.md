# CLAUDE.md — Management Unconsulted

## What this is

A read-only, browsable website version of `claude-skills-library/` (a
separate standalone project **elsewhere in the shelf**, its own local git
repo, not pushed to GitHub — see "Where this fits in the shelf" below for
the exact relationship now that this project has its own repo). That
project is the actual **functional** Claude Skills — installed to
`~/.claude/skills/` and used by Claude directly. This project exists
purely so Jozsua (or anyone else) can *view* that same content easily in
a browser.

Naming history: built as "The Playbook" (`the-playbook/`), renamed to
"Vantage Point" 2026-09-02, briefly renamed the same day to "The
Quagmire" (which turned out to collide with the shelf's hub page, also
called that — flagged at the time), reverted back to "Vantage Point"
shortly after on request ("this is called vantage point not the
quagmire"), then renamed again the same day to **"Management
Unconsulted"** once this project got pulled out into its own repo of
that name (see below) — matching the repo/product name rather than
having the repo and the live site disagree. **"Management Unconsulted"
is the current settled site name** — the site's `<title>`/`<h1>`/mindmap
hub text, the repo name, and the Quagmire hub tile's label are all meant
to say the same thing; don't let them drift apart, and don't rename any
one of them without updating the others. It started life as a subfolder
inside the `ai-slop/` repo (`ai-slop/vantage-point/`, published at
`jozsuaheng.github.io/Random-projects/vantage-point/`), then was pulled
out into its own standalone repo the same day — see below. To rename the
*site*: update `SITE_NAME` in `build.py` (mindmap center label, and
`r_center` alongside it if the new name is longer — `text_width()`'s
estimate for the widest hub-text line needs to fit inside `r_center`)
and `index.html`'s `<title>`/`<h1>`. The `localStorage` key for the
theme toggle (`management-unconsulted-theme`, in both `app.js` and the
inline anti-flash script in `index.html`'s `<head>`) was also renamed to
match — purely cosmetic (visitors never see the key name), but kept in
sync for the same reason as everything else above.

## Where this fits in the shelf

This is an **independent, standalone project** — its own local folder
(`management-unconsulted/`, a sibling of `ai-slop/` at the shelf root,
not nested inside it), its own git repo, pushed to its own GitHub repo:
**github.com/JozsuaHeng/Management-Unconsulted** (public), live at
**jozsuaheng.github.io/Management-Unconsulted/**. It is **not** part of
the `ai-slop/`/"Random projects" repo or its shared git history — it was
copied out (fresh files, not a history-preserving `git subtree`/
`filter-repo` split, since `ai-slop/`'s history is shared across many
unrelated projects and rewriting it wasn't warranted) and the original
`ai-slop/vantage-point/` folder was deleted from that repo once this one
was live.

The **Quagmire hub page** (`ai-slop/index.html`, the neal.fun-style tile
grid) has a tile for this project (`data-theme="playbook"`) — its label
and link were updated once the GitHub Pages URL above went live, so it
now reads "Management Unconsulted" and points at
`jozsuaheng.github.io/Management-Unconsulted/`, matching this site.

This project still depends on a **sibling folder**, `claude-skills-
library/` (one level up from this repo, at the shelf root — see
`build.py`'s `SKILLS_DIR`), for its actual skill content. That
dependency did *not* move — only the generated website did. If this
repo is ever cloned onto a machine that doesn't also have the shelf's
`claude-skills-library/` folder as a sibling, `build.py` won't run (the
already-built `index.html` + `dl/*.zip` still work fine as a static
site; only *rebuilding* needs that sibling folder present).

- `index.html` + `style.css` + `app.js`: the catalog page (client-side
  search filter only, no backend).
  - A large, animated, colour-coded radial **mindmap** is the primary
    visual overview — center hub, one branch per category, one leaf per
    skill. `LEAF_FONT`/`CAT_FONT` are 28px/32px (went 14→20→40→20→21→25→28
    across rounds of feedback; the geometry around them — `r_center`,
    leaf/category marker radii, `cat_dx`, hub text y-offsets — is scaled
    to match, so re-tune those together if the font value ever changes,
    not just the font).

    **Default view shows the whole mindmap, not a zoomed-in slice.**
    `default_scale` in `build_mindmap()` is fixed at `1.0`, and the
    `viewBox` is sized (Phase 3, below) to exactly bound the resolved
    layout — so scale 1 *is* "fit everything." An earlier pass computed
    default zoom to hit a specific on-screen font-size target instead;
    that's a reasonable goal in isolation, but it directly fights "see
    everything by default," which is what was actually asked for — don't
    reintroduce a target-px zoom calculation as the default. The lever
    that actually controls on-screen legibility now is the *canvas's
    spatial footprint* (how far out leaves get pushed) relative to
    `.mm-canvas`'s CSS height (`min(94vh, 1500px)` — deliberately large,
    since a taller container is the only real way to give a fixed-fit
    layout more pixels per label).

    Leaf label positions are resolved in three layers in
    `build_mindmap()`, each one a fallback for what the previous layer
    can't cheaply fix — plus a wrapping fix underneath all of them that
    turned out to matter more than any of the three:

    0. **Real word-wrap, not a single midpoint split.** `wrap_label(name,
       font_size, max_width=150)` greedily wraps a name onto as many
       lines as it takes to keep every line under `max_width` px at the
       actual `LEAF_FONT` — recomputed whenever the font size changes,
       instead of a fixed character-count threshold. The earlier version
       split a long name exactly once at its middle space, which still
       left one half wide for names like "Competitive Landscape Mapper"
       (the second half, "Landscape Mapper," was still 16 characters/
       ~230px at 25px font) — that leftover width, not point spacing, was
       the actual reason a handful of leaves in the densest categories
       could never be fully separated by ring/push/nudge tuning alone,
       however hard those were pushed. Fixing the wrap at the source
       resolved it outright.
    1. **Ring stagger (Phase 1).** Each leaf's base radius is
       `r_leaf_base + (index_within_category % N_RINGS) * RING_GAP +
       jitter(...)` — leaves cycle through 4 concentric rings (`N_RINGS`)
       by their position in the category's list, rather than all
       starting on one ring and relying entirely on a later push pass to
       sort them out. This is what actually keeps the shape roughly
       circular: most leaves now need little or no further correction,
       instead of a few getting pushed way out while most don't (which
       is what made the original one-ring version look spiky/uneven
       rather than round — same total leaf count, very different-looking
       outline). Each category's angular budget (`arc`) is deliberately
       tight — `min(34, 5.4×(n_leaves-1))` — with real buffer left to its
       neighbours in the 360°/7-category slice, because layer 3 below
       needs headroom to nudge into without leaking into the next
       category's arc.
    2. **Radial push (Phase 2a).** Any leaf pair whose boxes still
       overlap gets the closer-to-hub one pushed outward (by 2×`STEP`,
       asymmetric — not both), capped at `MAX_R` (`r_leaf_base +
       (N_RINGS+2)×RING_GAP`). Asymmetric matters for genuine same-ray
       coincidences: two real skills — `change-impact-assessment` and
       `stakeholder-engagement-log`, different categories — land ~0.25°
       apart by chance. On a shared ray, pushing *both* leaves out by
       equal steps barely changes their separation (their radius *gap*,
       the thing that actually determines distance apart, moves at
       roughly `(1 - cos Δθ)` per step — near zero for a tiny Δθ);
       pushing only the nearer one grows that gap every pass instead.
    3. **Angle nudge (Phase 2b), fallback of last resort.** If two
       leaves are *both* pinned at `MAX_R` when they collide, their
       radius gap is zero and no further radial push can separate them —
       this actually happened (both leaves of a pair independently
       walking out to the same ceiling), which is why this layer exists
       rather than just raising `MAX_R` again. For any pair still
       overlapping once Phase 2a is exhausted, this pass nudges each
       apart in **angle** instead, 0.2° at a time, up to a hard ±9° cap
       per leaf so a label can't drift into a neighbouring category's
       arc (see the tight `arc` budget in layer 1). Angle changes barely
       affect the canvas's required extent (unlike radius growth), which
       is why this is the safe place to spend the "last resort" budget.

    `build.py` prints the actual outcome of every rebuild — leaves that
    hit `MAX_R` (informational: Phase 2b exists precisely to clean up
    after them) and any label pair still overlapping after all layers
    (should be zero; treat a non-zero print as a real bug, not a
    tradeoff to accept — as of this pass it's genuinely 0). If a future
    font/count change needs revisiting this balance, try in order:
    `wrap_label`'s `max_width` first (the biggest lever, per layer 0
    above), then `RING_GAP`/`N_RINGS` (more rings or gap = less reliance
    on the push/nudge fallbacks and a rounder outline), then `.mm-canvas`
    CSS height, then `arc`'s per-category angular budget — but if `arc`
    grows, `MAX_ANGLE_NUDGE` in Phase 2b must shrink to compensate, or
    nudged leaves can cross into a neighbouring category's territory
    (this happened once mid-tuning: widening `arc` without re-checking
    the nudge cap produced cross-category collisions that hadn't existed
    before, on the *opposite* side of the mindmap from the pair the
    change was meant to fix).
    Canvas size (`viewBox`, `cx`/`cy`) is computed *from* the resolved
    layout's actual extent plus a margin, not guessed ahead of time —
    which is also why keeping the layout itself compact (ring stagger,
    the angle-nudge cap) is what keeps the whole mindmap large and
    legible on screen, not a separate lever.
    Branch/leaf lines start at the **hub's edge**, not its exact center
    point, and the hub `<g>` is emitted **last** so it paints on top of
    every line — both were needed together to stop lines from
    roughly-opposite branches visibly crossing through the hub circle's
    interior (a real bug from the first pass, caught from a screenshot —
    verify any future change to `r_center`/line logic by checking every
    branch line's start distance from center equals `r_center`, not 0).
    On load it draws itself outward (hub pops in, each branch's line
    draws, its category node bounces in, then its leaves cascade the
    same way — see `.mm-pop`/`.mm-line` keyframes in `style.css`; the
    pop keyframe deliberately overshoots twice, not once, for a visibly
    springier bounce). Once the entrance sequence settles (~2.6s), a
    slow, low-opacity **pulse ring** (`.mm-pulse-ring`, a second circle
    behind the hub) keeps expanding and fading on an infinite loop —
    added because the finished, static mindmap read as inert; kept
    deliberately subtle (long duration, low opacity peak) rather than
    distracting, and respects `prefers-reduced-motion`.
    It supports pan (click-drag or single-finger touch) and zoom
    (+/−/reset buttons only — mouse-wheel zoom was tried and removed,
    since it hijacked normal page-scroll whenever the cursor was over the
    mindmap), implemented by transforming the `#mm-viewport` `<g>` — see
    the pan/zoom block in `app.js`. Its `CX`/`CY`/`VB` constants are read
    from the SVG's actual `viewBox` attribute at runtime, not hardcoded —
    they'd otherwise drift out of sync every time `build_mindmap()`'s
    computed canvas size changes. Clicking a **leaf** opens that skill's
    popup directly (see below); clicking a **category node** zooms the
    mindmap in on that whole category's cluster (`zoomToCategory()` in
    `app.js`) — it also still flips that category's `<details>` open
    (unaffected below, categories still expand inline) but deliberately
    no longer `scrollIntoView`s there, since jumping the page away would
    immediately undo the zoom the click just performed. The zoom itself
    unions `getBBox()` over the category's node plus every one of its
    `.mm-leaf` elements — `getBBox()` returns each element's box in the
    *untransformed* viewBox coordinate system (the pan/zoom transform
    lives one level up, on `#mm-viewport`), which is exactly the same
    space `CX`/`CY`/`VB`/`tx`/`ty` already work in, so the same "map a
    target center to the viewBox center" math the +/−/reset buttons use
    (`scale = VB / max(width, height)`, clamped to `MIN_SCALE`/
    `MAX_SCALE`) applies directly with no separate pixel conversion. A
    temporary `.mm-anim` class (removed ~600ms later) adds a CSS
    transition for just this jump, since a permanent transition on
    `#mm-viewport` would fight drag-to-pan, which sets the transform on
    every `mousemove`; skipped under `prefers-reduced-motion`. Drag-
    then-release is distinguished from a real click via a movement
    threshold, so panning near a node doesn't accidentally trigger it.
    Category node circles/labels are deliberately bigger than leaf ones
    (`cat_r = 16` vs. a leaf's `4.5`, `CAT_FONT = 38` vs. `LEAF_FONT =
    28`) so the hub → 7-category structure reads at a glance before the
    reader looks at any individual leaf. The hub's own site-name text
    (`HUB_FONT = 42`) and `r_center` (`148` — sized for "Unconsulted,"
    the longer of the two current lines, per `text_width()`'s estimate;
    revisit this if `SITE_NAME` changes to something with a longer
    single word) went through the same size-up.
  - **Skill cards open in a centered popup, not inline.** A skill card
    shows only name/description/download-link; clicking the card (or its
    "Read more →" button, or its mindmap leaf) opens `#skill-modal` with
    that skill's full rendered content copied in via JS
    (`openSkillModal()` in `app.js`, reading the card's hidden
    `.skill-body` div). This replaced an earlier version where each
    skill was itself a `<details>` expanding inline — with 50 cards that
    made the page unwieldy to scan. **Categories are unaffected** and
    still expand inline as `<details>`/`<summary>` (collapsed by
    default) — only individual skills moved to the popup pattern.
    Expand-all/Collapse-all now only target `.category` elements
    accordingly.
  - **Downloads**: every skill has a small "⬇ .zip" link (in its
    summary, and again in the skill popup's header), every category has
    a "⬇ download N" link, and there's a "⬇ Download all 50" button
    right below the mindmap, right-aligned, above the first category
    (moved out of the hero's button row — with 4 buttons there it was
    overflowing the page's padding on narrower widths). All served from
    `dl/*.zip`, generated by `build_zips()` in `build.py` using Python's
    stdlib `zipfile` (no dependency) — each zip preserves the real
    `<slug>/SKILL.md` + `<slug>/references/*.md` structure, so extracting
    one straight into `~/.claude/skills/` (drag-and-drop in Finder, no
    Terminal required) works exactly like the source library. `dl/` is
    regenerated (old zips deleted first) on every `build.py` run and
    must be committed — GitHub Pages serves it as static files, there's
    no build step on the hosting side.
  - **"Copy" button in the skill popup header** (`#skill-modal-copy`,
    next to the `.zip` link) — copies that skill's plain-text content
    (title + description + body + any reference files) to the
    clipboard, so it can be pasted straight into a new chat with any AI,
    no upload/install step at all. Added because installing-as-a-Skill
    (claude.ai upload, or the Claude Code folder) turned out to be
    genuinely non-trivial for a first-time, non-technical user — several
    silent failure points (newly uploaded skills start switched off with
    no visible confirmation either way; unzip-then-upload has a "which
    folder do I actually select" ambiguity) — while copy-paste has none
    of that and works identically in Claude, ChatGPT, Gemini, or
    anything else that takes text input. The raw text lives in a hidden
    `.skill-raw` div per skill card (`build_skill()` in `build.py`,
    HTML-escaped so it round-trips cleanly through `.textContent` in
    `app.js` — deliberately a hidden element rather than a data
    attribute, since some skills' raw text runs to several KB). Falls
    back to `window.prompt()` with the text pre-selected if
    `navigator.clipboard` isn't available (no HTTPS, older browser).
    `.dl-link` (originally an `<a>`-only class) is now also used on this
    `<button>`, so it picked up `background: none; cursor: pointer;` to
    strip default button chrome — the font/color/border rules already
    applied identically either way.
  - **"Copy all 50" button** (`#copy-all`, next to "Download all 50"
    below the mindmap) — concatenates every `.skill-raw` div's text
    (separated by `\n\n---\n\n`) and copies the lot in one go. Shares
    the same clipboard/fallback logic as the per-skill Copy button via a
    `copyToClipboard(text, btn, label)` helper in `app.js` (both buttons
    call it — added when this button was added, to avoid duplicating the
    clipboard-write/prompt-fallback/"Copied!" logic a second time). This
    is **not** meant for pasting all 50 frameworks into one chat message
    — the button's `title` says so — it's for loading the *entire*
    library as permanent background knowledge into something like a
    ChatGPT Custom GPT, a Gemini Gem, or a Claude Project, where you want
    the whole library available rather than one skill at a time.
  - **"Quick start, by AI tool" section** (`.quickstart`, between the
    hero and the mindmap) — a categorized, always-visible companion to
    the "How to use this" modal, not a replacement for it: this is 4
    short card-per-tool at-a-glance boxes (Claude, ChatGPT, Gemini,
    Claude Code), the modal is the full walkthrough with troubleshooting
    for someone who's stuck. Added because "which AI am I even using,
    and does this work there" turned out to be a real, common first
    question that shouldn't require opening a modal to answer — putting
    it above the fold means a first-time visitor sees at a glance that
    this isn't Claude-only. Its "full step-by-step guide" link
    (`#quickstart-open-guide`) opens the same `#guide-modal` as the
    hero's own "How to use this" button — both wired to the same
    `openModal()` in `app.js`, so there's only one guide to keep in
    sync, just two doors into it.
  - The **"How to use this"** button opens an in-page flip-card modal
    (8 cards, prev/next/dots) written for a genuinely non-technical
    reader. **Restructured around copy-paste as the default path**
    (card 2), not the original design where installing-as-a-Skill was
    the main event — see the Copy button entry above for why: the
    install path has real friction and silent-failure points for a true
    beginner, while paste-it-in has none. Installing is now framed as an
    explicitly optional "upgrade" (card 4) for someone who's used the
    paste method a few times and wants Claude to reach for a skill
    automatically instead of re-pasting it — split into claude.ai/
    Desktop (card 5, still the friendlier of the two) and Claude Code
    (card 6, deliberately compressed from what used to be two cards'
    worth of detail, since Terminal is clearly not this guide's default
    reader). Card 7 answers "does this work with ChatGPT/Gemini?"
    directly: yes for copy-paste (it's just text), no for the
    auto-install upgrade (that's a Claude-specific feature — Custom GPTs
    / Gems are the rough equivalents there, not a drop-in). The last
    card's "next" button shows a checkmark (`✓`, styled
    `.flip-btn-done`) on the final card instead of the word "Done,"
    which didn't fit the circular button cleanly.
  - The hero has title+tagline stacked full-width, then a second row
    (`.hero-bottom`) putting the tagline and the search/button controls
    as top-aligned flex siblings — the controls sit literally in line
    with the tagline's top edge, not just "somewhere to the right."
    Stacks to one column under 900px. `.btn-row` wraps
    (`flex-wrap: wrap`) rather than forcing buttons to overflow past the
    column's edge on narrower widths. Below 420px, `.btn-row`'s buttons
    drop their `min-width` floor so three buttons can actually fit a
    phone-width screen without overflowing.
  - **Dark/light theme toggle** (`#theme-toggle`, top-right of a new
    `.top-bar` row alongside the back-link). The CSS already supported
    dark mode via `prefers-color-scheme` plus a `[data-theme]` override
    hook (unused until now) — the toggle just wires that hook up: click
    flips `<html data-theme="…">` between `"light"`/`"dark"` and persists
    the explicit choice to `localStorage` (`management-unconsulted-theme`); no
    stored value falls back to the OS setting via the existing media
    query, it's never forced to one theme for a first-time visitor. A
    small **inline, render-blocking script in `<head>`** (before
    `style.css` would otherwise paint) applies any stored choice
    immediately — without it, a visitor who chose dark would see a flash
    of the light theme every load until `app.js` (loaded at the end of
    `<body>`) caught up. The button swaps between inline sun/moon SVG
    icons (`.icon-sun`/`.icon-moon`, toggled via the same `[data-theme]`/
    media-query pairing used everywhere else) rather than text, to match
    the zoom-control buttons' icon-only style.
  - **Mobile/touch**: the mindmap's pan/zoom (`app.js`) now also handles
    genuine two-finger pinch-to-zoom (`touchstart`/`touchmove` branch on
    `e.touches.length === 2`, computing distance between the two touch
    points and calling the same `zoomAtPoint()` the +/− buttons use) —
    added because a phone screen makes the fit-everything default view's
    50 labels much smaller than on desktop, and until now touch users had
    no way to zoom in at all except the small fixed +/− buttons. Single-
    finger drag-to-pan on the canvas now also calls `e.preventDefault()`
    on `touchmove` (the listener switched from `passive: true` to
    `passive: false` to allow this) so the page itself doesn't scroll
    underneath a finger that's panning the mindmap — that fight didn't
    show up on desktop (mouse drag never scrolled the page) but was a
    real mobile bug. `.category-title` wraps onto two lines below 480px
    (icon/name/count-badge/download-link/collapse-arrow no longer forced
    onto one row that could overflow a narrow screen).
- All skills' full content (both `SKILL.md` and any `references/*.md`) is
  generated into `index.html` by `build.py`, between the
  `<!-- CONTENT:START -->` / `<!-- CONTENT:END -->` markers, and the
  mindmap between `<!-- MINDMAP:START -->` / `<!-- MINDMAP:END -->`. The
  category list (name + slugs, in order), `CATEGORY_COLORS`, and
  `CATEGORY_ICONS` are hardcoded in `build.py` — add a new skill to the
  right category's list there too when one is added to the source
  library; adding a whole new category needs an entry in all four dicts
  (`CATEGORIES`, `MINDMAP_LABELS`, `CATEGORY_COLORS`, `CATEGORY_ICONS`).

## Keeping it in sync

This site is a **generated copy**, not the source of truth. If a skill in
`claude-skills-library/skills/` (sibling folder, one level up — see
"Where this fits in the shelf" above) changes (content edited, a skill
added or removed), regenerate this page:

```bash
cd management-unconsulted
python3 build.py
```

This rewrites only the mindmap and category/skill content between their
markers — the hero, flipchart modal, zoom controls, styles, and script
are untouched. Commit the updated `index.html` (and the regenerated
`dl/*.zip` files) along with whatever changed on the source side, and
push — this repo has no separate build step on the GitHub Pages side.

## Design notes

- Palette/typography: warm paper + ink, Source Serif 4 for headings,
  Inter for body/UI — chosen for a more professional, less
  editorial/whimsical feel than an earlier Fraunces + Caveat pass. Font
  links live only in `index.html`'s `<head>`.
- Category colour-coding runs through the whole page (mindmap branch →
  category border/heading → each skill's left-border accent), so the
  same seven hues tie the overview and the detail view together.
- Supports both light and dark mode via `prefers-color-scheme` (and a
  `data-theme` override hook), since this is meant to be a genuinely
  readable reference page, not just a novelty tile destination.
- Mindmap entrance animation respects `prefers-reduced-motion` (skips
  straight to the final state).
- The Quagmire hub page's tile for this project lives entirely in the
  **other** repo now (`data-theme="playbook"` in `ai-slop/index.html` /
  `ai-slop/style.css` — internal CSS name kept as-is through the rename,
  only the visible label/link changed), not in this one — see "Where
  this fits in the shelf" above for why it's deliberately left pointing
  at the old URL for now. It's a light, gridded "whiteboard" card with a
  small hand-drawn strategy-diagram doodle and the name in a handwriting
  face (Caveat, kept only there) — the only light/gridded tile in the
  grid, on purpose, so it stands apart at a glance per the hub's own
  tile-design rule. The diagram was originally confined to the right
  ~42% of the card, leaving an empty-looking gap in the middle-left —
  widened to span most of the card (`top:24%; left:32%; width:64%;
  height:70%`, clear of the top-left title), plus a small second doodle
  (`.playbook-notes`, two sketched checklist marks) added in the
  remaining bottom-left corner so the composition doesn't have a dead
  zone.
