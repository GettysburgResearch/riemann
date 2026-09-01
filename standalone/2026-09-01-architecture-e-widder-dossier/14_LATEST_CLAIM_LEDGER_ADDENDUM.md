# Latest claim-ledger addendum: radial, heat, and theta–Darboux leverage

Status: **LOCAL REVIEW LEDGER ONLY.  THESE ARE NOT CANONICAL REPOSITORY CLAIM IDS.  RH REMAINS UNPROVED.**

This addendum extends
[`05_IMPORTED_VS_NEW_CLAIM_LEDGER.md`](05_IMPORTED_VS_NEW_CLAIM_LEDGER.md)
with the theorem packets added after the finite-height E–Widder pass.

`PROPOSED_NEW` means a proof is supplied in this standalone dossier and
requires independent review.  `OPEN_EQUIVALENT` means the statement remains
RH-equivalent and unproved.  `OPEN_BEARING` is a source theorem sufficient for
an RH-equivalent gate but not separately asserted equivalent in its strongest
local wording.

## 1. Invariant radial resolvent

| Local label | Statement | Status | Proof/source | Review sensitivity |
|---|---|---|---|---|
| `EW-RAD-001` | The normalized Widder atom is `lambda_u(a)=4ua/(u+a)^2=sech^2((log(u/|a|)-i arg a)/2)`. | `PROPOSED_NEW` | `09_INVARIANT_RESOLVENT_AND_HEAT_TRACE.md`, Section 1 | Branch and logarithm conventions. |
| `EW-RAD-002` | The complete order generator is the closed two-point resolvent `(2u/(zeta-zeta^-1))[zeta q(uzeta)-zeta^-1 q(u/zeta)]`. | `PROPOSED_NEW` | same, Section 2 | Partial fractions and factor two. |
| `EW-RAD-003` | On the real order ray the generator is a radial phase derivative of `mathfrak X`. | `PROPOSED_NEW` | same, Section 2 | Phase-current normalization. |
| `EW-RAD-004` | A nonreal invariant conjugate pair is positive for every scale exactly before `w=cos^2(arg(a)/2)`. | `PROPOSED_NEW` | same, Section 3 | Exact pair numerator. |
| `EW-RAD-005` | At the matching scale, an off-line orbit creates a noncancellable real pole of negative residue in `(1/2,1)`. | `PROPOSED_NEW` | same, Section 3 | Multiplicity and coincident-pole addition. |
| `EW-RAD-006` | RH is equivalent to unit-disc holomorphy, equivalently full real-ray positivity, of the radial order generator at every scale. | `PROPOSED_NEW` | same, Section 4 | Pole isolation and normal convergence. |
| `EW-RAD-007` | The radial generator is unconditionally positive on `0<=w<=1/2`, the sharp uniform direct-Euler ray. | `PROPOSED_NEW` | same, Sections 5–6 | Critical-strip angle and square-root branch. |
| `EW-RAD-008` | The imported height `H=3*10^12` confines every possible real-ray failure to an annulus of width below `2.78e-26`. | `PROPOSED_NEW` using `IMPORTED` height | same, Section 7 | Exact cutoff and no extrapolation. |
| `EW-RAD-OPEN` | The source radial current is nonnegative in the remaining terminal annulus for every scale. | `OPEN_EQUIVALENT` | same, Section 12 | Proving this proves RH. |

## 2. Fixed-centre heat trace

| Local label | Statement | Status | Proof/source | Review sensitivity |
|---|---|---|---|---|
| `EW-HEAT-001` | `K(t)=2 sum_a exp(-at)=exp(-t/4) sum_rho exp(-t gamma_rho^2)`. | `PROPOSED_NEW` | `09_INVARIANT_RESOLVENT_AND_HEAT_TRACE.md`, Section 8 | Orbit factor and centred-zero convention. |
| `EW-HEAT-002` | `q(u)` is the Laplace transform of `K(t)`. | `PROPOSED_NEW` | same, Section 8 | Tonelli/normal convergence. |
| `EW-HEAT-003` | RH is equivalent to complete monotonicity of the one fixed-centre heat trace `K`. | `PROPOSED_NEW` | same, Section 8 | Bernstein-to-Stieltjes converse. |
| `EW-HEAT-004` | Every Widder functional is a positive Laplace moment of `(-1)^k K^(k)`. | `PROPOSED_NEW` | same, Section 9 | Factorial and differentiation. |
| `EW-HEAT-005` | `K` has the explicit nonoscillatory Guinand--Weil gamma-plus-prime formula stated in the note. | `PROPOSED_NEW` | same, Section 10 | Fourier/Laplace normalization. |
| `EW-HEAT-OPEN` | The explicit source heat trace is completely monotone. | `OPEN_EQUIVALENT` | same, Sections 10–12 | Proving this proves RH. |

## 3. Theta–Darboux/Andreief factorization

| Local label | Statement | Status | Proof/source | Review sensitivity |
|---|---|---|---|---|
| `EW-TDA-001` | The invariant coefficient basis is `b_n(tau)=[u^n] cosh(tau sqrt(u+1/4))` and `c_n=2 int Phi b_n`. | `PROPOSED_NEW` | `13_THETA_DARBOUX_ANDREIEF_GATE.md`, Section 1 | Full-line/half-line normalization. |
| `EW-TDA-002` | The lowering operator `L=D_tau^2-1/4` satisfies `L b_n=b_(n-1)` and transports self-adjointly to the actual theta source. | `PROPOSED_NEW` | same, Section 2 | Boundary cancellation at zero and infinity. |
| `EW-TDA-003` | The kernel `(tau,n)->b_n(tau)` is strictly totally positive of infinite order. | `PROPOSED_NEW` | same, Section 3 | Infinite Cauchy--Binet and strictness. |
| `EW-TDA-004` | Every Toeplitz minor with nonnegative coefficient indices has the exact ordered Andreief factorization into a theta–Darboux determinant and a strictly positive coefficient determinant. | `PROPOSED_NEW` | same, Sections 4–5 | Index translation, determinant orientation and factor `2^r`. |
| `EW-TDA-005` | All arithmetic sign in the positive-index coefficient cone is isolated in one actual theta–Darboux exterior current. | `PROPOSED_NEW` | same, Section 4 | Structural consequence, not a sign theorem. |
| `EW-TDA-OPEN` | Every weighted theta–Darboux/Andreief exterior integral has nonnegative sign. | `OPEN_BEARING` | same, Section 6 | Source-local gate; pointwise positivity is not asserted. |
| `EW-OVT-OPEN` | The ordered theta–Darboux current obeys a variation theorem sufficient for all strictly TP coefficient tests. | `OPEN_BEARING` | `06_NEXT_ATTACK.md`, Section 4 | Principal next theorem. |

## 4. Quasi-free/count-law endpoint retained

| Local label | Statement | Status | Proof/source | Review sensitivity |
|---|---|---|---|---|
| `EW-QF-001` | The invariant coefficients are strictly positive and define one probability-generating function at every positive scale. | `PROPOSED_NEW` | `09_INVARIANT_ORDER_PRODUCT_AND_COUNT_LAW.md`, Sections 1–2 | Split theta integral. |
| `EW-QF-002` | RH is equivalent to the one-scale count law being `PF_infinity`, Poisson-binomial, or one positive trace-class Fredholm determinant. | `PROPOSED_NEW` using classical ASWE/Edrei | same, Section 2 | Entire-order converse. |
| `EW-QF-003` | The actual theta source gives an explicit vacuum-plus-continuous mixture of forced-one Bernoulli strings. | `PROPOSED_NEW` | `10_THETA_FOCK_MIXTURE_AND_QUASIFREE_GATE.md`, Sections 1–3 | Mixing normalization. |
| `EW-QF-OPEN` | The arithmetic theta mixture is the exterior character of one positive trace-class contraction. | `OPEN_EQUIVALENT` | same, Section 4 | The latent-selector/quasi-free gate. |

## 5. Exact current boundary

```text
radial resolvent and matching pole                    PROPOSED COMPLETE / REVIEW
resummed positive ray and terminal-annulus cutoff     PROPOSED COMPLETE / REVIEW
fixed-centre heat equivalence                         PROPOSED COMPLETE / REVIEW
strict TP coefficient propagator                      PROPOSED COMPLETE / REVIEW
theta–Darboux/Andreief source factorization           PROPOSED COMPLETE / REVIEW
weighted theta–Darboux variation theorem              OPEN / RH-BEARING
fixed-centre heat complete monotonicity                OPEN / RH-EQUIVALENT
one theta-built quasi-free determinant                OPEN / RH-EQUIVALENT
all-order E–Widder source inequality                  OPEN / RH-EQUIVALENT
Riemann Hypothesis                                    UNPROVED
```

## 6. Explicit nonclaims

This addendum does not claim:

- pointwise positivity of every theta–Darboux determinant;
- closure of `PF_infinity` under arbitrary positive mixtures;
- that a direct integral or averaged fibre operator solves the quasi-free
  gate;
- that bounded exact checkers establish an infinite determinant or heat sign;
- an all-order proof of the E–Widder inequality;
- RH or GRH.
