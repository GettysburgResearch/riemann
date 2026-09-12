# Polynomial degree growth: a less restrictive full-RH target

**PROPOSED component theorems; independent mathematical review pending.**
**RH and the required subpower growth upper bound remain OPEN.**

This is a separate addition-only research packet. It reads the latest PR845
boundary construction and the latest PR848 collision-energy result, while
preserving the finite-stage corrections in the new theta/gamma programmes.
It changes no previous paper or canonical status.

## Main result

Retain AC28's exact odd-polynomial operators Q_p, Ap=tQ_p', and Ep. For
Pi_N=span{t,t^3,...,t^(2N-1)}, define

    Lambda_N = sup_(p!=0 in Pi_N) ||Ep||^2 / ||Ap||^2.

Every degree has a finite constant, but these constants necessarily diverge.
The full source has the exact source-preserving operator representation

    Ep=K(Ap),    (Kf)(t)=integral_0^1 m(t/u)f(u)du/u,
    m(x)=sum_(n<=x, odd)mu(n)/n,  1<t<3.

With normalized odd Legendre polynomials phi_j, define the positive scalar

    S_N=sum_(j<N)||Kphi_j||^2.

The manuscript proves

    RH iff S_N=N^o(1) iff Lambda_N=N^o(1)
       iff liminf log(1+S_N)/log N=0
       iff liminf log(1+Lambda_N)/log N=0.

Thus even an arbitrarily sparse UNBOUNDED sequence of certified subpower
upper bounds would suffice. The missing upper bound is not supplied here.
This is weaker than insisting on one uniformly bounded positive-eta constant
at every degree; necessity of that original condition is not asserted.

The key quantitative fact is not merely finite-dimensional compactness:
a hypothetical zero beta+i gamma with beta>1/2 forces

    Lambda_N >= c_(beta,gamma) N^((2beta-1)/10)

at EVERY sufficiently large degree. No such zero is asserted to exist.
A complete degree estimate for actual odd-polynomial approximants proves
this, so sparse upper bounds could not evade a hypothetical exceptional zero.

## Additional all-scale conclusions

- If Lambda_N=O(N^r), 0<=r<1, there are no zeta zeros with Re(s)>(1+r)/2.
- The unconditional ceiling is S_N<=800(2N-1); no fixed power saving is obtained.
- Under an explicitly stated harmonic-Mobius estimate |m(x)|<=M x^(beta-1),
  BOTH the operator norm and entire trace are O(N^(2beta-1)). The RH implication
  uses the classical RH-to-Mertens theorem only conditionally.
- An existing critical-line zero gives Lambda_N>=c log N eventually. The
  constants/threshold are not numerically evaluated. Uniform eta=0 cost is
  impossible; slow divergence is permitted by the new target.

All-degree statements above are written proofs, not inferred from the table.

## Finite arithmetic checks

The checker reconstructs the complete matrix using actual reciprocal even-zeta
values and every polynomial cross term. No zero locations are evaluated.
The table gives a certified Rayleigh LOWER bound for Lambda_N and a certified
trace UPPER bound; it is not a table of computed exact eigenvalues.

| N | degree cap | lower bound | upper bound |
|---:|---:|---:|---:|
| 1 | 1 | 2.386649 | 2.386650 |
| 2 | 3 | 3.125985 | 3.145814 |
| 4 | 7 | 3.531656 | 3.561926 |
| 8 | 15 | 3.735733 | 3.772366 |
| 16 | 31 | 3.840475 | 3.884869 |
| 32 | 63 | 3.893542 | 3.946811 |

Decimals are rounded outward from rational interval endpoints in results.json.
All six complete matrices also satisfy the all-vector upper bound Lambda_N<4.
Section 6 proves that this finite bound CANNOT hold at all degrees. A small
initial plateau is not evidence of a global bounded constant.

## Read and review

[PROOF.md](PROOF.md) contains DG26-1--6, including the exact end-to-end
conditional chain and its unproved upper estimate. [ATTEMPT.md](ATTEMPT.md)
explains what was tried and how the latest proposals affect the choice.
[LATEST_WORK.tsv](LATEST_WORK.tsv) pins 25 recent PR heads and separates
metadata reconnaissance from actual proof reading. [SOURCES.json](SOURCES.json)
credits both the classical ingredients and exact repository dependencies.
[VALIDATION.md](VALIDATION.md) states what was and was not run.

    python -B check.py --check results.json --self-test
    python -O -B check.py --check results.json --self-test
    python -OO -B check.py --check results.json --self-test

One same-author checker with different primitive calculations is not independent
mathematical review. No full checkout or repository-wide validator run is
claimed. Do not promote the OPEN estimate because its implication is proved.
