# Verified literature atlas for counterexample-oriented RH research

Agent: `gpt56-03`  
Issue: #3  
Snapshot: 2026-07-22  
Status: literature synthesis; theorem imports are `PROPOSED` until independently checked inside this repository.

## Reading discipline

This atlas records only references that were actually located during this
session.  The accompanying `source-ledger.md` says what was inspected: full
text, author manuscript, publisher abstract, or metadata only.  An exact
theorem statement is imported only when the statement itself was located in a
primary paper or in a later primary paper that explicitly restates it.  When
the original source was located only bibliographically, that limitation is
spelled out rather than hidden.

Publication is not repository verification.  A theorem card marked
`PROPOSED` means: a primary source supports the displayed statement, but no
independent agent has yet reconstructed the cited proof.  The cards are safe
interfaces for research planning, not a substitute for checking the source.

## Executive map

The most useful distinction for this project is not "analytic versus
arithmetic"; it is the logical shape of a possible disproof.

| Route | A single finite certified object can disprove RH? | Main certificate |
|---|---:|---|
| Robin | yes | integer factorization plus disjoint interval inequality |
| Lagarias | yes | integer factorization plus harmonic/exponential inequality |
| Nicolas primorial | yes | prime index, exact product, rigorous logarithms |
| Li coefficients | yes | one rigorously negative coefficient |
| Weil positivity | yes | one admissible function/vector with negative quadratic value |
| Deléglise--Nicolas `h(n)` | yes | optimal prime subset plus inverse-`li` inequality |
| Speiser | yes | one nonreal zero of `zeta'` left of `Re(s)=1/2` |
| de Bruijn--Newman | yes | one nonreal zero of `H_t` at an explicit `t>0` |
| direct zeta zero | yes | zero-count enclosure off the critical line |
| Pólya--Jensen | yes in principle | one nonhyperbolic Jensen polynomial |
| Nyman--Beurling/Báez-Duarte | not by one large finite residual | failure of a closure statement requires an analytic lower bound |
| Riesz-type asymptotic criteria | not by one large finite value | failure of a universal asymptotic bound |
| finite low-height zeta scan | no universal conclusion | only excludes the scanned region |

This classification prevents a recurrent logical error: a numerically large
residual in an asymptotic equivalent is not automatically a finite
counterexample witness.

## Highest-leverage connections to active work

### Issue #1: finite Weil positivity

Bombieri and Lagarias connect Li's coefficients to the Guinand--Weil explicit
formula.  Bombieri's later finite-matrix study treats finite restrictions of
Weil's quadratic functional.  The reusable project kernels are:

- `L-0310`: compact logarithmic support makes the prime-power sum finite;
- `L-0311`: a negative Hermitian direction admits a rational/dyadic witness;
- `M-0301`: every imported explicit formula must carry a normalization and
  source-provenance record.

These do not certify the recent cutoff-free dictionary used on agent #1's
branch.  The exact normalization audit requested by that branch's `Q-0004`
remains necessary.  Claim number `T-0305` is deliberately reserved for that
future independently reconstructed Weil theorem rather than filled with a
vague formula.

### Issue #2: Robin witness

Robin's theorem supplies the exact finite-witness implication.  Lagarias shows
how Robin's criterion yields an elementary harmonic-number equivalent and
records the reduction to colossally abundant integers if RH is false.
Choie--Lichiardopol--Moree--Solé give additional necessary structure for a
Robin counterexample.  The project kernels are:

- `L-0320`: exact product formulae for `sigma(n)/n` and `n/phi(n)`;
- `L-0321`: swapping inverted prime exponents strictly improves the Robin
  quotient (when both integers stay in the monotone `log log` domain);
- `T-0301` and `T-0302`: imported exact criteria.

The exponent-swap lemma is a safe pruning rule, not a proof that every search
may be restricted to one named family without further argument.

## Top five unclaimed directions

The research issues opened from this atlas are deliberately independent and
certificate-first.

1. **#14 — Li coefficients.** Dual evaluation from logarithmic derivatives and
   an arithmetic/explicit-formula representation.  One negative interval is a
   finite witness.
2. **#15 — Nicolas primorial inequality.** A one-dimensional prime-indexed
   search with exact product recurrence and ball logarithms.
3. **#16 — Deléglise--Nicolas bounded-prime-sum criterion.** A proof-producing
   prime-subset optimizer plus a rigorous inverse-`li` comparison.
4. **#17 — Speiser derivative-zero search.** Certified winding of `zeta'` in a
   rectangle strictly left of the critical line; coordinate with direct-zeta
   Issue #7.
5. **#18 — positive-time de Bruijn--Newman search.** Certified nonreal zero of
   `H_t` for rational `t>0`.

All five issues are unclaimed at creation and contain a starting lemma or
algorithmic recurrence.

## Important negative triage

### The low-height direct-zero region is closed

Platt and Trudgian rigorously proved with interval arithmetic that every zeta
zero with `0 < Im(rho) <= 3*10^12` lies on the critical line and is simple.
Thus a direct off-line rectangle search must begin above that height.  The
result is imported as `T-0310`; it is not recomputed here.

### Jensen brute force has an enormous certified exclusion range

For
\[
 \xi(1/2+z)=\sum_{j\ge0}\gamma(j)z^{2j}/j!,
 \qquad
 J^{d,n}(X)=\sum_{j=0}^d {d\choose j}\gamma(n+j)X^j,
\]
Griffin--Ono--Rolen--Thorner--Tripp--Wagner prove that verification of RH up to
height `T` forces all `J^{d,n}` to be hyperbolic for every `n>=0` and every
`d<=floor(T)^2`.  Combining this theorem with `T=3*10^12` gives an unconditional
exclusion through degree
\[
  (3\cdot10^{12})^2=9\cdot10^{24}.
\]
Therefore a raw search for a nonhyperbolic Jensen witness below that degree is
provably futile.  This does not refute the criterion; it demotes it as a
counterexample search route.

### Closure and asymptotic criteria need a separation theorem

The Báez-Duarte strengthening of Nyman--Beurling says that an indicator lies in
the closure of a specified span in `L^2`.  Computing a large but finite
least-squares residual neither proves nor disproves membership in the closure.
An actionable disproof would require a rigorous positive lower bound valid for
the whole infinite span, typically a separating functional.

The same warning applies to Riesz-style big-`O` equivalents: one finite
overshoot of a guessed numerical envelope does not contradict the asymptotic
statement unless the envelope is the exact quantified theorem.

## Literature groups

### Finite arithmetic witnesses

- G. Robin, *Grandes valeurs de la fonction somme des diviseurs et hypothèse de
  Riemann*, J. Math. Pures Appl. (9) 63 (1984), 187--213.
- J. C. Lagarias, *An Elementary Problem Equivalent to the Riemann
  Hypothesis*, Amer. Math. Monthly 109 (2002), 534--543.
- Y. Choie, N. Lichiardopol, P. Moree, P. Solé, *On Robin's criterion for the
  Riemann hypothesis*, J. Théor. Nombres Bordeaux 19 (2007), 357--372.
- J.-L. Nicolas, *Petites valeurs de la fonction d'Euler*, J. Number Theory 17
  (1983), 375--388.
- M. Deléglise, J.-L. Nicolas, *An arithmetic equivalence of the Riemann
  hypothesis*, J. Aust. Math. Soc. 106 (2019), 235--273.

### Positivity and explicit formulae

- X.-J. Li, *The Positivity of a Sequence of Numbers and the Riemann
  Hypothesis*, J. Number Theory 65 (1997), 325--333.
- E. Bombieri, J. C. Lagarias, *Complements to Li's Criterion for the Riemann
  Hypothesis*, J. Number Theory 77 (1999), 274--287.
- A. Weil, *Sur les "formules explicites" de la théorie des nombres premiers*,
  Colloque sur la théorie des nombres, Bruxelles, 1952, 252--265.
- E. Bombieri, *Remarks on Weil's quadratic functional in the theory of prime
  numbers, I*, Rend. Lincei Mat. Appl. 11 (2000), 183--233.

The original Weil paper was located bibliographically, but its full
normalization was not inspected in this session.  Do not quote an exact Weil
functional from this atlas; use the future `T-0305` audit.

### Analytic zero-location equivalents

- A. Speiser, *Geometrisches zur Riemannschen Zetafunktion*, Math. Ann. 110
  (1935), 514--521.
- L. Báez-Duarte, *A strengthening of the Nyman--Beurling criterion for the
  Riemann hypothesis*, Atti Accad. Naz. Lincei Rend. Lincei Mat. Appl. 14
  (2003), 5--11; arXiv:math/0202141.
- B. Rodgers, T. Tao, *The de Bruijn--Newman constant is non-negative*, Forum
  Math. Pi 8 (2020), e6.

### Polynomial equivalents and computational barriers

- M. Griffin, K. Ono, L. Rolen, D. Zagier, *Jensen polynomials for the Riemann
  zeta function and other sequences*, Proc. Natl. Acad. Sci. USA 116 (2019),
  11103--11110.
- M. Griffin, K. Ono, L. Rolen, J. Thorner, Z. Tripp, I. Wagner, *Jensen
  polynomials for the Riemann xi-function*, Adv. Math. 397 (2022), 108186.
- D. Platt, T. Trudgian, *The Riemann hypothesis is true up to
  `3*10^12`*, Bull. Lond. Math. Soc. 53 (2021), 792--797.

### Certified numerical infrastructure

- A. M. Turing, *Some calculations of the Riemann zeta-function*, Proc. London
  Math. Soc. (3) 3 (1953), 99--117.
- A. R. Booker, *Artin's conjecture, Turing's method, and the Riemann
  hypothesis*, Experiment. Math. 15 (2006), 385--407.
- F. Johansson, *Arb: efficient arbitrary-precision midpoint-radius interval
  arithmetic*, IEEE Trans. Comput. 66 (2017), 1281--1292.

Arb was merged into FLINT in 2023; new reproducibility records should pin a
FLINT/python-flint version rather than cite the old standalone documentation
as though it were current.

## Unverified or deliberately excluded items

- No recent preprint claiming to prove or disprove RH is treated as an
  established source in this atlas.
- The exact normalization of agent #1's recent finite Guinand--Weil dictionary
  is not verified here; it is explicitly delegated to its independent audit.
- The original proofs of Robin, Nicolas, Speiser, Weil, and Newman are not
  reproduced here.  Where full original text was not inspected, the theorem
  card identifies the later primary source used to verify the statement.
- Any bibliographic item lacking a confirmed title/venue/year/locator would be
  marked `UNVERIFIED`; none is silently completed from memory.
