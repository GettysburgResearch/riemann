# Three-route continuation: theta, native Newton energy, and Lee--Yang

Status: **PROPOSED research components and compositions. RH remains unsolved.**
The packet contains complete written component proofs, exact finite checks,
two directed moment certificates, and scoped reviews. Publication and
same-session review do not make these integrated or externally accepted
mathematics. The all-field consequences retain the analytic dependencies
specified in the proofs.

Base: PR [#965](https://github.com/GettysburgResearch/riemann/pull/965),
commit `d58e3282a9379b6ae165681bc2e21e4f9fd18c26`.
This directory is new. Its claims have their own identities and do not
rewrite any inherited proof, review, or integrated status.

## Results at a glance

| Route | New proposed result | What is still needed for the full-proof route |
|---|---|---|
| Critical theta / principal source | Intermediate-line numerator means; proposed all-field boundary 49/54; larger exact correction domain; a first-transverse finite-part detector | A native signed estimate for the physical projection, with its weights and complete tails |
| Newton NRC32 | O_r(Y/log^r Y) exact coarse coordinates and complete discarded variance O_(r,B)(log^(-B)Y), for every fixed r and B | A saving from the quadratic exponent in the remaining native coarse energy |
| Theta-law Lee--Yang | A connected 281-spin ferromagnet exactly matching degrees through 16, with degree-18 discrepancy in (0.034,0.035); a certified negative compensated edge derivative | A target-reaching degree-18 extension and then realizations at unbounded orders with the all-order consumer's hypotheses |

Read the mathematical statements below, then the linked proofs. The status
of a finite certificate, a conditional implication from named analytic
inputs, and an open native estimate is kept explicit in each component.

## 1. Theta means and the critical principal source

### Numerator interpolation and the proposed global consequences

[INTERPOLATED_NUMERATOR.md](critical/INTERPOLATED_NUMERATOR.md) proves a
finite-vector interpolation theorem, then restores the exact primitive
conductor and imprimitive Euler factors. If E is any subset of U^nu actual
Poisson rows, the central second mean gives, for fixed 0<y<1/2,

    sum_E |L_u(y+it)| << U^(1/2+nu(1-y)+epsilon)(2+|t|)^C.

The subset may be selected by denominator zeros. No independence is
assumed. [THETA_COMPARISON.md](theta/THETA_COMPARISON.md) supplies every
contour and tail for the resulting proposed strict boundary
9081/10000=0.9081, using only the existing second mean and original
de Faveri density. It is independent of the later fourth-moment source.

Concurrent PR [#966](https://github.com/GettysburgResearch/riemann/pull/966)
supplied a fourth numerator mean with exponent 7/6. Its Theorem A is
credited and its complete sieve/AFE deduction is reproduced in
[FOURTH_MEAN_EXTENSION.md](theta/FOURTH_MEAN_EXTENSION.md). Interpolating
that mean gives the new subset exponent

    1/2+nu-y*(5/12+nu/2).

With the ORIGINAL density theorem, this proves the proposed composition

    zeta_K(s) != 0 for Re s>49/54, s!=1,

for every fixed number field K, and the corresponding finite-order Hecke
statement. Here 49/54 is approximately 0.9074074074. The scales are
X=Y=Z^(4/9), the physical exponent is 2/9, and the actual principal Mellin
shift is 37/54. A small-norm contour change to z=1/3 is necessary.

This improves #965's proposed 91/100 by 7/2700 and #966's proposed 109/120
by 1/1080. It does not improve the narrower reported 7/8 Riemann setting.
No boundary-line statement, uniformity in fields or conductors, or RH is
asserted. The separately reviewed fourth-mean composition does not use
#966's additional selected-character density theorem.

A final publication refresh also found concurrent
[#968](https://github.com/GettysburgResearch/riemann/pull/968), which gives
the same 7/6 fourth numerator exponent and a proposed 10/11 comparison.
The present 49/54 boundary is smaller by 1/594. That overlap is credited;
#968 is not an added dependency of this frozen proof. Its more general
fixed-order numerator formula is not used here.

### Exact local factors open a larger domain

[LOCAL_DOMAIN.md](critical/LOCAL_DOMAIN.md) evaluates every native exterior
valuation j=0,...,5. The original unit masks and angular phases survive.
Two sufficient restrictions, 3 Re(xi)>2 and
3 Re(xi)+Re(w)>5/2, are removed from the correction domain. At z=2/5 or
z=1/2 the resulting H_u domain is simply

    Re xi>1/2, Re w>0, Re(xi+w)>1.

The same calculation extracts a common factor for ALL rows:

    H_u(xi,w,z)=zeta_F^S(xi+w) K_u(xi,w,z),
    K_u << (Nu)^((1-Re xi-Re w)_+/2+epsilon)

on the explicitly stated larger domain. Only primes with valuation at
least two incur the crossing power. On the complex diagonal w=1-xi,
every fixed-order transverse derivative of K_u costs only (Nu)^epsilon.

This is a structural result for the actual correction. The 49/54 comparison
deliberately retains its inherited, narrower domain; its scale limit is
relative to that domain. No new global comparison using the enlarged
domain is silently appended. A subsequent comparison must account for
every changed contour and for the common diagonal pole.

### The diagonal residue loses the detector; the finite part restores it

[DIAGONAL_FINITE_PART.md](critical/DIAGONAL_FINITE_PART.md) treats the
principal row at z=1/2. Its extracted diagonal factor is nonzero for
1/2<Re xi<1. The normal residue is an explicit holomorphic function and
has canceled the target zeta zeros. The renormalized constant Laurent
coefficient instead equals exactly

    -(zeta_F^S)'(xi)/zeta_F^S(xi).

A hypothetical off-line zero of multiplicity m appears as a simple pole
of residue -m. The physical monomial contributes an explicit log(Y) term
to the finite part; it is retained and can be subtracted. Mellin test
factors and tails remain obligations of the physical projection.

This identifies the first transverse quantity that must survive a signed
estimate. The local K_u derivative bound does not estimate that full
renormalized physical quantity, which still contains the logarithmic
derivative being detected.

## 2. Native Newton compression

[newton/PROOF.md](newton/PROOF.md) uses the literal reciprocal energy

    m(k)=sum_(n<=k) mu(n)/n,  F_K=sum_(k<=K) m(k)^2,
    b=Y+1.

For every fixed integer r>=0 it constructs a deterministic partition of
EVERY cell Y<k<(Y+1)^2 into O_r(Y/log^r(2Y)) blocks. Each block mean is an
exact signed quadratic form in the old prefix mu(1),...,mu(Y). Its complete
orthogonal decomposition is

    F_(b^2-1)-F_Y=S_(Y,r)+D_(Y,r),
    0<=D_(Y,r)<<_(r,B) log^(-B)(2Y)

for every fixed B>0. The mesh is independent of B; r cannot grow with Y
under this theorem.

The added input is the ordinary Mobius, T=0 case of Matomaki--Radziwill--
Shao--Tao--Teravainen, arXiv:2411.05770v2, Theorem 3.1(i). The new variance
lemma sums maximal signed increments over EVERY integer starting point,
so the exceptional intervals are paid legitimately. Early annuli are
handled deterministically before applying the short-interval theorem.

The gain controls how many coordinates and how much complete remainder
are needed. It does not bound the magnitudes of the coarse coordinates.
The explicit delta-source control has zero detail and still has quadratic
coarse energy. The unresolved target remains a native estimate such as

    S_(Y,r)<=C log^A(2Y)(1+F_Y)^(2-delta), delta>0,

with sufficient saving along the native square ladder. No fake source,
completed source, or random model is substituted for the original prefix.

## 3. A connected Lee--Yang realization and a direction of improvement

[lee_yang/PROOF.md](lee_yang/PROOF.md) contains two proposed
computer-assisted finite theorems for the original normalized theta law.
The primitive density, normalization, variance, and all tails are replayed.

The first constructs a connected tree with 281 spins and 280 strictly
positive couplings, each between 1/200000 and 1/4. Every observed spin has
positive weight; one auxiliary hub has zero observable weight. Conditioning
on that hub gives a complete polynomial moment map for all configurations.
The finite weighted Lee--Yang theorem, with a separate Hurwitz argument
for the zero-weight hub, gives a characteristic function with only real zeros.

Its moments agree EXACTLY with the standardized theta moments through
degree 16. The unmatched raw standardized 18th moment is rigorously
between 0.034 and 0.035 above the target. The old D16 source discrepancy
is independently bounded between 0.169 and 0.170. A separate theorem at
that exact old source shows that an edge between two dimer roots has
compensated derivative between -0.785 and -0.784, after preserving all
lower prescribed moments.

The root certificates use exact rational inverses and outward integer
intervals on a radius-10^(-30) box. The source replay uses six explicit
theta indices, 98 cells, degree-120 Taylor polynomials and 320-bit directed
arithmetic, with every time and index tail paid. An independent seven-spin
enumeration checks the conditional polynomial model on all 128 states.

The new tree is not a degree-18 realization. The local negative derivative
does not supply a global interval reaching the next target. Unsuccessful
architectures and weight collisions are documented in
[EXPLORATION.md](lee_yang/EXPLORATION.md) as search outcomes, not obstructions.
The full-proof route still needs target-reaching realizations at unbounded
orders with the source and convergence hypotheses of its separate consumer.

## Reading and reproduction

Use [SOURCES.md](SOURCES.md) for exact imported commits and primary texts,
[REVIEW.md](REVIEW.md) for the review scope and dispositions, and
[VALIDATION.md](VALIDATION.md) for the exact computation contract.

From this directory, with standard Python 3:

```sh
python3 verify_packet.py
python3 verify_packet.py --replay
```

The first command verifies the complete file inventory and hashes. The
second also reruns the finite checkers and both full-source Lee--Yang
certificates. It does not claim to computationally prove the imported
analytic theorems. The manifest binds all files except itself, and no
external package, moment oracle, network access or solver is required
for these replays.
