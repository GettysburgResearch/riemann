# Observatory contributor instructions

This directory is an additive software contribution to programme #897. The root AGENTS instructions still apply. It does not change the repository's mathematical acceptance status.

1. Read README, VALIDATION and ROADMAP. Start the app before extending it.
2. Run `python -m pytest observatory/tests -q`. For browser changes, run the native browser smoke test where available; name any harness substitutions. Never represent bridge mode as native-origin, Windows, or Safari testing.
3. Keep numerical providers pure and bounded. Validate through the per-provider schema (legacy desks retain Spec); never evaluate arbitrary browser-submitted Python or JS. A trusted source extension is code review, not a runtime upload feature.
4. Preserve exact anchors as strings. Do not send huge coordinates through float/Number and then subtract an anchor. Preserve pole/missing masks and independent event lists.
5. Keep ordinary precision distinct from certified enclosures. Show actual finite scope, normalization, omitted terms, domain limits and rounding class. Do not replace unavailable values with plausible pictures.
6. A plotted result is identified by its submitted request and hash, not by later control edits. Save/replay must retain provenance. Test cancellation and stale-result races after async changes.
7. For every provider addition: add definitions/capability limits, a known-value check, an adversarial test, a preset, and a boundary statement. Keep source code, not just images.
8. Do not expose this unauthenticated local server, weaken host/origin guards, or add paid infrastructure without a separate reviewed deployment design.
9. Keep changes inside observatory unless intentionally wiring a narrowly scoped CI task. Do not rewrite scientific canon, other research branches, or main's status pages.

Next work is the unchecked acceptance gates in ROADMAP. This is a broad v0.4 preview, not completion of every programme milestone. Separate numerical-contract work, view/state work, and storage work so contributors can test them independently.
