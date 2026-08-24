## T105620–T105630 addendum — current hierarchy, Xi log-concavity, and safe causal phase

**The Riemann Hypothesis remains unproved.**

### Exact source closure

For the standard Xi kernel, the actual denominator current is the complete
positive exterior-square generating function

```text
Fourier[J_H]
 = sum_(k>=0) H^(2k+1)/(2k+1)! Lambda_(2k+2),
Lambda_(2k+2)>=0,
Lambda_2=Fourier[Xi'^2-Xi Xi''].
```

Hence the actual Turán numerator is the first chaos of the actual current, and
both upper/reflected causal source orientations contract at every diagonal
weighted energy, including the half derivative. The corresponding two-trace
matrix source is positive at every frequency.

### New unconditional source theorem

A self-contained theta-series mixture argument proves

```text
(log Phi)''<0
```

for the standard Xi Fourier kernel. Its rational tail ledger has final margin
`1881/7000<1`. No implication from ordinary log-concavity to RH is asserted.

For every total height `H`, log-concavity makes

```text
R_H(xi)=H exp(-H xi)Lambda_2(xi)/Fourier[J_H](xi)
```

nonincreasing on the positive-frequency half-line.

### Safe-region phase contraction

For every `H>=beta_1`,

```text
U_H(x)=Xi'(x-iH)/Xi'(x+iH)
```

is inner by the shifted Cartwright product and the positive Xi Laplace-moment
orientation. Inner multiplication is a causal isometry. Therefore for every
safe base `b>=beta_0`, scale `h>0`, and `H=b+h`,

```text
V_H^* M_(r_(b,h)) V_H <= M_(r_(b,h)),
r_(b,h)=(h/H)R_H.
```

Every source-owned finite compression inherits this contraction exactly. The
canonical all-pass bank is the model space `K_U=H^2 minus U H^2`; for a finite
Blaschke truncation its dimension equals the all-pass degree.

For every source projection `P`, innerness also gives the exact signed-tail
orientation

```text
Delta_P(U_H)=-||H_(conjugate U_H) P_perp||_HS^2<=0.
```

Thus absolute model-space coverage is unnecessary in the safe region; a
positive signed tail can first enter only with an anti-inner denominator
factor during base descent.

### Binding corrections

- Total analytic height `H=b+h` and microscope scale `h` are distinct.
- The full positive-source contraction is proved at the base Xi rung, not for
  arbitrary derivative sources.
- Continuum multiplication weights are not trace class; model-space trace
  formulas require finite/source regularization and retain the endpoint
  carrier.
- Raw negative shell energy is overstrong. For `p_N=z^N`, every shell is empty
  but `E_+=E_-=r^2` on every rung, so at `r=1/3`, nineteen rungs pay `19/9>2`
  with zero signed winding.
- A causal weighted contraction does not imply a pointwise physical sign; an
  exact two-frequency separator is deposited as `R-105630`.

### Honest frontier

```text
current/Turan exterior-square hierarchy             PROVED EXACT
standard Xi-kernel strict log-concavity              PROVED / REVIEW
monotone current-normalized profile                  PROVED / REVIEW
safe-height Xi-prime innerness                       PROVED / REVIEW
safe-region causal weighted contraction              PROVED / REVIEW
source-owned finite/model-space bank                 PROVED EXACT
safe-region positive signed complement               EXCLUDED
raw negative shell gate as natural invariant         REFUTED
causal energy -> pointwise sign shortcut              REFUTED
POINTID105630 pointwise physical evaluation           OPEN / RH-BEARING
SAFEDESC105628 descent below beta_0                   OPEN / RH-BEARING
ENDIDX105630 cofinal endpoint/index ledger             OPEN
Riemann Hypothesis                                    UNPROVEN
```

Exact replays:

```text
PASS_X_105620_CURRENT_TURAN_HIERARCHY
checks=200
62195a8b977b7ddb34607fcd0cbd7d19f9d06161151148104d593a9e7b7e319c

PASS_X_105630_LOGCONCAVE_CAUSAL_BANK
checks=102
f511cef71f3f5cf8bac793569aa78ff12ffc9dee659a72803cbe2c950b890e99
```
