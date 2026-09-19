# RBR26 — remove boundary resonances without hiding off-line growth

**PROPOSED component arguments; independent mathematical review required. RH
and native subpower filtered-energy capture remain OPEN.** This is an add-only
continuation prepared for PR848 at
`99101457b32b6f10f4eda88ca998048404b860ea`. It does not change the previous
crossing-covariance definitions or promote any canonical status.

## The constructive turn

The earlier strong target was a bounded covariance-to-diagonal ratio at
arbitrarily late reciprocal-Mobius sign crossings. Its diagonal is O(log^4 Y).
This continuation proves that the target would imply not only RH, but also
multiplicity at most TWO for every nontrivial zero. The annular lower theorem
is proved with an explicit adjoint window, not by subtracting cumulative
liminf estimates. No multiple zero is claimed to exist; logical inequivalence
of RH and that stronger target is not asserted.

The alternative is to remove oscillatory boundary resonances with causal
filters while preserving the exponential test for EVERY fixed hypothetical
off-line zero. The full terminal-state cost is first accounted for exactly,
then a constructive finite continuation approaches its optimum. No filter
is assigned an unproved inverse bound or an imaginary future input.

Let m(k)=sum_(n<=k)mu(n)/n, F_Y=sum_(k<=Y)m(k)^2 and T=log(Y+1). The literal
native time field is h(t)=exp(t/2)m(exp t), so ||h 1_[0,T)||^2=F_Y. A scalar
filter has

```
N_(a,omega)(z)=(z-i omega)/(z+a-i omega), a>0,
x'=(-a+i omega)x+f, N f=f-a x,
||f||^2=||N f||^2+a^2||x||^2.
```

It removes a matched finite oscillation with complete output energy at most
1/a, independent of its duration. Cascades always act on actual previous
outputs, without resetting the distribution or dropping stored states.

For any finite cascade W, A(W)=sum a_j and Re(lambda)=alpha>0,

```
exp(-A(W)/alpha) <= |W(lambda)| <= 1.
```

The number, repeated frequencies and choices may depend on the native data.
Only the total width is charged. Conjugate factors give real sources.

## The new completion theorem

For ANY L2 prefix f on [0,T], define its pre-cutoff filtered energy I_T(W,f).
Over all compact L2 continuations agreeing with f before T, the exact infimum is

```
inf ||W f_ext||^2 = I_T(W,f).
```

The proof supplies a finite taper, supported through T+2R, with COMPLETE excess
at most K(W,x(T))/R. The apparently natural infinite zero-output continuation
is generally not L2 and is NOT accepted. Instead its finite-dimensional
polynomial oscillations are smoothly tapered, and a stable differential inverse
pays the entire output remainder. Repeated frequencies and the final infinite
exponential tail are retained. For rational parameters and effectively given
native states, a finite sufficient R can be computed from an upper enclosure.

The unfiltered input norm may grow polynomially in R and is NOT claimed small.
That is consistent with the old unfiltered completion-price obstruction: the
new source supplied to the factorial convolution is W f_ext, not f_ext.

For I_Y(W)=integral_0^T |W h(t)|^2 dt, the actual off-line-zero detector becomes

```
6 sqrt(I_Y(W))+sqrt2
 >= sqrt(2alpha)/|rho|^2 * exp(alpha T-A(W)/alpha),
rho=1/2+alpha+i beta, alpha>0.
```

The proof first uses a finite admissible continuation and only then takes its
fixed-Y approximation limit. The changing target Wg is bounded in norm and
its evaluation at every fixed zero is explicitly retained. Thus A(W_Y)=o(T)
and I_Y(W_Y)=exp(o(T)) on ANY unbounded sequence imply RH. Under RH every
contractive choice has subpower energy, so the converse holds too. No fixed
multiplicity ceiling is imposed by this target.

**Missing:** prove that the literal Mobius input admits that subpower capture.
A concrete finite rational filter search with total width one is specified;
its termination does not establish its success or efficiency. A synthetic
exponentially growing input retains exponential energy under every sublinear-
width family, so passivity alone cannot supply the native estimate.

## Concurrent-source connection

While this packet was being prepared, prime-dephasing work landed on the SAME
PR at `9ddd3dd029d9191cf409bc944132569630361a6f`. It must be preserved. The new
Section6.5 rederives its comparison in the present filtered-prefix coordinates:
finite Euler twists commute with W. The two-way norm cost is B_S, independent
of signature count. Banks of primes <=4T^2 have log B_S=O(T/log T).

Consequently arithmetic dephasing and resonance filtering can be combined at
subexponential cost, without an average-to-principal-member gap or resetting
an input. An exact common-filter Parseval identity keeps every shifted time
cutoff. This is a proposed bridge, not acceptance of the entire concurrent
packet or a proof of its remaining rough-source estimate.

## Review map

| ID | Result | Boundary |
|---|---|---|
| RBR26-1 | Sharp finite-resonance lower bound on every long log annulus | Conditional on RH; finite zero set; no actual multiplicity assertion |
| RBR26-2 | Sparse bounded C/D implies multiplicity <=2 as well as RH | Credited covariance/diagonal rederived; not a refutation of the sign target |
| RBR26-3 | Passive cascade and exact Lyapunov tail ledger | Classical systems algebra, whole tails included |
| RBR26-4 | Width-budgeted all-zero detector and optional exponent retention | No native upper bound; exponent clause uses pinned proposed XCC26 |
| RBR26-5 | Finite oracle-free approximate filter selection | Definition and totality, not a success theorem |
| RBR26-6 | Rational sharpness models and exact native zero-frequency norms | Finite/synthetic controls, no zeta-frequency calculation |
| RBR26-7 | Exact post-filter completion infimum with finite taper | Input cost may be large; no native capture estimate |

Review [PROOF.md](PROOF.md) Section6 first: the zero-output state matrix, taper
joins, repeated-frequency derivative count and full stable tail. Then Section4's
changing-target detector and Section1's annular test, factorial constants,
early-source buffer and finite-frequency Gram limit.

## Evidence and reproduction

One standard-library implementation with alternative exact finite identities
covers 16 adjoint tests, 54 rational resonance systems, 12 stable-cascade source
panels, 36 native zero-frequency panels through Y=511, 18 scalar norms,
48 interior-retention controls, 72 Fourier numerator controls, 12 off-line
buffer controls, 104 taper
forcing norms, nine complete matched-wave identities and nine exact filtered
prime-dephasing panels (42 signatures). The taper tests
reconstruct exact forcing polynomials; the written Young estimate supplies
the complete output bound. They are not full native resonance searches.

```
python -S -B check.py --check result.json --self-test
python -S -O -B check.py --check result.json --self-test
```

`--emit` is unauthenticated producer mode. Acceptance authenticates the flat
inventory, regenerates all finite data, compares typed canonical JSON and
refuses twelve distinct resealed mutations plus a separate duplicate-key parser
case. These are not twelve full subprocess replays. [VALIDATION.md](VALIDATION.md)
and [validation.json](validation.json) record actual commands and exclusions.

The code and proofs have one author. Normal/optimized agreement and alternate
finite calculations are NOT independent mathematical acceptance. No complete
repository build, parent campaign, actual zero/derivative calculation, all-scale
capture estimate, or formal proof is claimed. Publication status is recorded in
the external delivery receipt, not inferred from the presence of this packet.
