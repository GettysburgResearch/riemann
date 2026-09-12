# A positive full-source energy and a cofinal descent target

**Proposed component proofs; independent review required. RH remains unproved.**

This continuation of #842 changes the all-order complete-monotonicity task into
a single positive sequence with a sharp alternative. Use the unchanged central
xi heat trace, with the FIXED shift h(t)=exp(-t)H(t), and define

    E_n=4^n/(2n+1)! integral_0^infinity t^(2n+1)|h^(n)(t)|^2 dt.

Every energy is positive and finite. For a zero rho=beta+i gamma, gamma>0, put

    D_*=sup [2 gamma(beta-1/2)/(1+gamma^2-(beta-1/2)^2)]^2.

The manuscript proves, without assuming any zero is off the line,

    lim E_(n+1)/E_n=1+D_*,
    lim log(1+E_n)/n=log(1+D_*).

Under RH, E_n strictly decreases to a positive limit. Otherwise the largest
angular rate is attained at finitely many distinct nodes; their diagonal
contributions dominate the complete double sum with a uniform exponential gap.
Thus E_n eventually increases geometrically. Analytic multiplicities are
retained, and no rightmost-beta or simple-zero assumption is made.

Consequently RH is equivalent to arbitrarily late downward steps, or to any
subexponential upper bound along an unbounded subsequence. NO such estimate
for the native sequence is supplied.

## A second exact form of the missing arithmetic estimate

For f_n(u)=exp((n+1)u)(-1)^n h^(n)(exp u), set V_n=||f_n'||_2^2/||f_n||_2^2.
The complete identity is

    E_(n+1)/E_n=[(n+1)^2+V_n]/[(n+1)(n+3/2)],
    lim V_n/(n+1)^2=D_*.

Infinitely many inequalities V_n<=(n+1)/2 suffice; even V_n=o(n^2) along an
unbounded sequence suffices. Integration by parts does not prove that upper
bound. Positivity/decrease of h alone cannot: the complete synthetic example
2exp(-t)+2exp(-2t)cos(t) has E_n asymptotic to (5/4)^n/8.

The source can be evaluated through the exact all-prime-power/archimedean
formula in PROOF Section6. Its summands are not separately positive. The shift
by one places every squared rate in the right half-plane using only the
classical critical strip, so this theorem does NOT depend on the preceding
finite low-zero census or new probability positivity claim.

## Reading and executable scope

Start with [PROOF.md](PROOF.md), particularly the pairwise equality conditions
and uniform infinite-pair gap in Section3. Then read [REVIEW.md](REVIEW.md),
[SOURCES.json](SOURCES.json) and [VALIDATION.md](VALIDATION.md).

    python -I -S -B check.py --check result.json
    python -I -S -B -O check.py --check result.json

The checker evaluates exact finite-exponential integrals, not native xi
energies. Six groups contain 1,109 finite panels, including 900 elementary
pair-geometry panels. Counts are not theorem counts. No finite decreasing run,
zero table, new theta quadrature or numerical limiting-rate estimate is used.
No all-order positivity, native descent, Ising realization or RH is claimed.
