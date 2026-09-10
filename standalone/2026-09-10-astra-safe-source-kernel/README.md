# Fixed-interval arithmetic prediction: an all-degree attack on RH

**PROPOSED component proofs; independent review pending. RH is NOT proved.**
This addition-only continuation of PR845 is based on
`e6dbb8ef4e458ea4c8d1b17ced77ec28905a7472`. Read [PROOF.md](PROOF.md).

## The target is one inequality, not a growing finite computation

For an arbitrary complex odd polynomial p, define actual positive-integer
arithmetic dilations

    Q_p(t)=sum_(n>=1, n odd) p(t/n)/n,
    E_p(t)=Q_p(1)-sum_(n>=3, n odd) p(t/n)/n.

Every series converges on compact intervals. The proposed closing theorem is:
for each eta>0 one finite constant C_eta works for EVERY degree and EVERY p:

    integral_1^3 |E_p(t)|^2 dt
      <=eta integral_0^1 |p(t)|^2 dt
          +4C_eta integral_0^1 t^2 |Q_p'(t)|^2 dt.       OPEN

The manuscript proves that this all-degree inequality would imply RH. The
intervals are fixed, the source is not replaced, and there is no unproved
continuum-to-lattice adapter in this implication. The inequality itself is
**not established**. Its necessity for RH is not asserted.

Writing p(t)=t P(t^2), the dilation is

    Q_p(t)=t integral P(t^2 u) dnu(u),
    nu=sum_(n odd) n^(-2) delta_(1/n^2),  nu total mass=pi^2/8.

Its polynomial multipliers are the classical explicit values
Z(2k)=(1-2^(-2k))zeta(2k). Positive measure and finite mass alone do not prove
the critical weighted inequality. The moment generating function is the
classical explicit expression pi*tan(pi*sqrt(z)/2)/(4*sqrt(z)); this does not
by itself settle the Mellin multiplier's zeros.

## Exact bridge to all complex zeros

Set ell=log3, a(z)=(z-1/2)Z(z+1/2), with a(1/2)=1/2. On the first logarithmic
interval the native inverse source is exactly exp(t/2). This yields entire
functions

    d_r(z)=integral_0^r exp(z(r-t))exp(t/2)dt,
    b_r(z)=exp(zr)-a(z)d_r(z), 0<=r<=ell,

and the complete Hermitian kernel

    K_(eta,C)(z,w)=[eta+4C a(z)conj(a(w))]/[z+conj(w)]
                    -integral_0^ell b_r(z)conj(b_r(w))dr.

There is no reciprocal zeta or unknown zero in its definition. Full Gram
positivity on ONE fixed safe real interval, such as (1,2), is equivalent to
positivity on Re z>0 and to the complete continuum prediction inequality.
The proof constructs a contraction between exact feature maps and continues
that bounded map, not scalar inequalities.

It is also equivalent to the all-odd-polynomial inequality above. The safe
nodes 2k-1/2 have no finite accumulation point: a proved bounded-analytic
uniqueness argument using their divergent Blaschke sum is essential.

If positive, the kernel forces EVERY zero alpha of a in Re z>0 to satisfy

    Re alpha <= log(1+eta)/(2log3).

Thus eta decreasing to zero rules out every off-critical zeta zero at every
height. This direct conditional conclusion needs no zero census or simplicity.

## What is proved unconditionally, and what fails

| Component | Result and exact boundary |
|---|---|
| AC28-1/2 | Complete numerator kernel and exact local/global/domain bridge. Neither side is assumed positive. |
| AC28-3 | Conditional global zero-free bound, critical-resonance cost, and impossibility at eta=0. No positive-eta upper estimate. |
| AC28-4 | The true kernel has positive diagonal at EVERY safe real point for eta=0,C=4. Full positivity nevertheless fails. |
| AC28-5 | Every finite odd-prime product fails some finite Gram test when eta<2, regardless of C. Its artificial zero replaces the true pole cancellation. |
| AC28-6 | Sharp full-input one-pole model and marginal sum of squares. Explicitly nonnative, not a decomposition of the Mobius source. |
| AC28-7 | Fixed-interval polynomial equivalence and positive dilation representation. Also ||Q_p'-p'||<=(4/5)||p'|| for EVERY degree. This uses the wrong, unweighted derivative norm for closure. |
| Q-AC28 | Uniform all-degree compensated estimate: OPEN. |

In particular finite-prime positivity cannot simply be passed to a limit.
The eta term must remain: critical zeros force C_eta to grow at least at the
specified inverse-power rate as eta decreases. The native diagonal theorem
does not authorize an all-order positive-kernel conclusion.

## Actual finite evidence

The checker supplies eight complete native Gram certificates at dimensions
2,4,6,8, eta=0 or 1/100, C=1. It uses two 256-bit outward interval paths:
Machin pi plus Bernoulli even-zeta values, and Euler--Maclaurin with its entire
remainder. Interval LDL and independently integrated polynomial/Bareiss
principal minors certify all vectors in each of these eight dimensions.
There are also 16 direct polynomial-isometry/derivative controls and exact
finite-Euler negative determinants. These are finite evidence, not the
all-degree premise. Both implementations have the same author.

See [VALIDATION.md](VALIDATION.md) for exact execution scope and
[SOURCES.json](SOURCES.json) for source pins and prior-art limits. The general
local-Gram/contractive-factorization mechanism is classical and already used
for a different xi kernel in PR398. No general novelty claim is made.

The next mathematical task is a source-faithful all-degree factorization or
weighted bound for the displayed polynomial inequality. A further collection
of successful finite matrices would not supply that theorem.
