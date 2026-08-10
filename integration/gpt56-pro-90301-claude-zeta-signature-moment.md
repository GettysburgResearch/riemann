# Integration handoff — Claude zeta-23 signature-moment import

Integration ID: `gpt56-pro-90301`  
Date: 2026-08-10  
Base commit: `527ee3cb985720195bd23012ad1ae321bd6f0774`  
Upstream formal source: `anthropics/zeta-23-lean@3635e74826a4c1fcece7d1cd2b6fa75e43a00510`  
Scope: source import, exact extension lemma, proposed analytic extension, diagnostic replay

## Files

### Source dossier

- `literature/anthropic-zeta-23/README.md`
- `literature/anthropic-zeta-23/SOURCES.lock.json`

### Mathematics

- `claims/lemmas/L-90301-co-lattice-multiwindow-collapse.md`
- `claims/theorems/T-90301-short-window-hybrid-conductor-signature-moment.md`

### Frontier and diagnostics

- `claims/observations/O-90301-bandwidth-one-frontier-after-claude.md`
- `claims/observations/O-90302-xiprime-scalar-window-is-numerically-saturated.md`
- `experiments/X-90301-claude-signature-moment/`

### Session report

- `reports/gpt56-pro/2026-08-10-claude-zeta-import-and-extension.md`

## Status ledger

| Object | Status | Strongest statement | Missing gate |
|---|---|---|---|
| external zeta-23 theorem | pinned/imported | 0.6725007 simple/on-line; 0.8362503 distinct | independent community review continues upstream |
| `L-90301` | proposed complete exact | all finite co-lattice windows collapse to one aggregate scalar profile | cold harmonic-analysis review |
| `T-90301` | proposed complete uniform | constants at \(\lambda\sim\log H/\log(qT)\) | line-by-line analytic review; Lean port |
| `O-90302` | empirical | scalar \(\xi'\) optimum appears within a few \(10^{-6}\) of upstream quartic | interval/Fredholm certificate if promoted |
| `X-90301` | replayed | constants and finite auxiliary checks pass | does not authenticate asymptotics |

## Replay

```bash
python3 experiments/X-90301-claude-signature-moment/verify.py
```

Expected terminal line:

```text
PASS_X_90301_CLAUDE_SIGNATURE_MOMENT
```

## Reviewer attack list

For `L-90301`:

1. Fourier-convention factor \(L\);
2. complex conjugation in the multiwindow kernel;
3. boundary dual modes for support length exactly \(L\);
4. whether every aggregate profile is realizable with one admissible tapered window.

For `T-90301`:

1. short-interval end effects;
2. uniform conductor zero count;
3. omitted Euler factors;
4. varying optimal profile;
5. endpoint \(X\asymp H\);
6. zeta pole term;
7. master error (T-90301.7).

## Integration recommendation

Do not merge `T-90301` into a `VERIFIED` packet until it receives an exact-SHA analytic review or a Lean formalization. The source dossier and `L-90301` may be reviewed independently. The observation and experiment should remain explicitly diagnostic.

RH remains unproved.
