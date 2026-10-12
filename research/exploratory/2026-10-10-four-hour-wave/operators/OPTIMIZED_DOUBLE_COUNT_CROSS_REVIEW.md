# Independent optimized twice-integrated count review

Reviewer: operator_mechanisms, 2026-10-10. Verdict: **ACCEPT at the explicitly
imported complete-source scope**, including the classical global order
1,414,000 and the additional-strip global order 1,480,000. No original
height proof or producer was changed.

Frozen target:
`heights/final-review/OPTIMIZED_DOUBLE_COUNT.md`, SHA256
`4a760969f52d03199ce38fcd29ad787382d9c61e4009f6f3cd79dd7e19d9c5c9`;
checker `verify_optimized_double_count.py`, SHA256
`f6b681cbb261f34323e505acdc8611d3d40b253b6bccb8b8513eb10e234ed1f8`.
This review follows the separate full operator review of the frozen
DOUBLE_COUNT_PICK.md, including its exact gamma remainder, twice-integrated
count boundary terms, and fixed-denominator first and second derivatives.

## Analytic composition

The sharper primitive coefficient is correct uniformly in both variables.
Writing x=log T, v=log(t/T), L=28.729, c0=2.067/L, the exact reserve is

    c0*(x+v) - [2.067+v/141]
       = c0*(x-L)+(c0-1/141)*v > 0,

because x>L, v>=0, and c0>1/141. Thus
cA'=0.059+2067/28729=3762011/28729000 pays the complete accumulated theta
term. This also holds at t=T. It removes the formerly separately added
1/141 without dropping any actual error term. I independently derived
this same refinement before receiving the target manuscript.

Replacing only cA in the already reviewed second integration gives
J'=4*cA'*(C2+C1^2)=306538772327579/718225000000000. Both endpoint terms at
the good cutoff still vanish; the infinite endpoints retain proper-rational
decay. The complete source keeps its cutoff atom in the below-or-at part,
all multiplicities and the factor 2 in the positive-height count.

Retaining A in the original arbitrary-displacement amplification gives
exp[2*A*(d0+2/n)*q]. The fixed-denominator continuous and sampled derivative
bounds remain valid for A<=1/2. Discrete Minkowski still allows every
ordinate to have its own complex path. Conjugate cancellation removes the
first Taylor term, and the integral second remainder is paid by A^2/2.
Combining this with the product-rule factor 2 gives exactly

    A^2*(C2+C1^2)*kappa^2*q^2*(U*+J'*q^2),

with no missing conjugate, signed-pole, or multiplicity factor. Hence the
displayed G_A(q) is the full-source reserve. Its derivative is negative
for q>0, so exact endpoint positivity covers all smaller q.

The normal and optimized checker replays independently pass and are
byte-identical. I inspected every acceptance condition: frozen predecessor
proof binding; the all-variable reserve identity; complete positive
exponential Taylor tails; n>=850000 derivative constants; both exact
endpoint gaps; strict headline inequalities; maximum even orders; and the
published census extending past the whole common good-cutoff interval.
The maximal even orders at H0 are 1,414,566 and 1,480,878.

## Source limits

The classical A=1/2 case adds no quasi-RH assumption. The A=3/8 case
explicitly requires a uniform complete-source strip, rather than a finite
census or zero-density average. The imported September 30 theorem recorded
in literature/PRIMARY_SOURCES.md excludes all zeta zeros with Re(s)>7/8;
functional reflection supplies Re(s)>=1/8, and therefore |Re(s)-1/2|<=3/8.
This is the correct displacement substitution. Its analytic proof, formal
solution closure, published Turing estimate and high critical-line census
were not rebuilt or rerun by this review.

Both conclusions are finite global Pick orders. The selectable-cutoff
statements concern changing tail kernels. Neither supplies an all-order
global theorem or RH.

Independent replay receipts:
`optimized_double_count_independent_normal.json` and
`optimized_double_count_independent_optimized.json`.
