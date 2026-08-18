# Identifier migration

The author handoff used `T/L/R/X-97500` and `L/R-97501`. Those identifiers are
already occupied by live PRs #578 and #581. This recovery therefore maps them
mechanically to `T/L/R/X-97610` and `L/R-97611` and places the standalone paper
under a `-97610` directory.

The branch is stacked on PR #577 at exact head
`ae85922195c12a29944e624337bae2167091929b`. The scientific prose, formulas,
reviewed upstream heads and honest verdict are unchanged.

The included PDF is the exact 21-page author-rendered binary and therefore
displays the original `97500` identifiers. `main.tex` is the repository
`97610` edition. The three portable replays were rerun after migration; the
retained directed MPFR certificate remains byte-derived from the validated
author packet because the local Windows environment does not expose its
GNU/MPFR build chain.
