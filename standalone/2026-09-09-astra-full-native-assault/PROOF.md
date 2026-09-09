# FNE26 — A direct full-residual Euler construction and its exact failure

Date: 2026-09-09. Author: Astra.
Status: complete proposed component proofs; independent mathematical review pending.
**No unconditional proof of RH was obtained. This is a failed candidate for the
original RH-facing residual, not a positive substitute for the missing bound.**

All primes and Mobius coefficients are ordinary arithmetic ones. The prime number
theorem is an explicitly imported UNCONDITIONAL input to the sharp asymptotic.
No hypothetical zero, independent-prime model, numerical zero table, or graph
spectrum is used to construct or evaluate the candidate.

## 1. The full problem being attacked

For a finite real Dirichlet polynomial p(s)=sum a_n n^(-s) satisfying p(1)=0, put

    A_p(x)=sum a_n floor(x/n),
    E(p)=integral_1^infinity |1-A_p(x)|^2 dx/x^2.

Balance gives A_p(x)=-sum a_n {x/n}, so E(p) is finite. The EXACT whole-frequency
identity is

    E(p)=(1/(2pi)) integral_R
             |1-zeta(1/2+it)p(1/2+it)|^2/(1/4+t^2) dt.       (1)

Indeed integrating first on Re s>1 yields the Mellin transform (1-zeta(s)p(s))/s.
The original bounded residual continues it to Re s>0; the pole at s=1 is
removable. Apply Fourier Plancherel to exp(-t/2)[1-A_p(exp t)] on t>=0.
This function is in L1 and L2. No meromorphic boundary norm is being mistaken
for a causal source: the source is constructed first.

Here is a complete sufficient ending, fixing the intended strength. Suppose
p_Y has a_n=mu(n) for EVERY n<=Y and is balanced. Mobius inversion gives
A_p(x)=1 on 1<=x<Y+1. For a hypothetical zeta zero rho=beta+i gamma with
beta>1/2, put delta=beta-1/2 and T=log(Y+1). The delayed residual's transform
at rho-1/2 is exactly 1/rho, with no cancellation by the finite polynomial.
Cauchy--Schwarz therefore gives

    E(p_Y) >= (2beta-1)(Y+1)^(2beta-1)/|rho|^2.             (2)

This uses the ENTIRE residual after T. No simplicity assumption is needed.
Consequently E(p_Y)=Y^(o(1)) along an unbounded sequence would exclude every
right-of-line zero; reflection by the functional equation would yield RH.
The same conclusion holds for independently chosen finite supports of any size.
**The required upper bound is not established below.**

## 2. A complete multiplicative candidate with the native normalizations

Fix an integer Y>=2 and set

    Q=Y+1, P_Y=product_(p<=Y) p,
    M_Y(s)=product_(p<=Y)(1-p^(-s)),
    m_Y=M_Y(1), c_Y=[m_Y^(-1)-log Q]/log 2,
    B_Y(s)=1-Q^(1-s)+c_Y[Q^(1-s)-(2Q)^(1-s)],
    p_Y(s)=M_Y(s) B_Y(s)-2Q^(-s)(1-2^(1-s))^2.            (3)

The product M_Y is expanded completely, not cut again at integer Y. Its
coefficient at d|P_Y is mu(d), and all of these squarefree divisors are retained.
The late corrections are ordinary finite Dirichlet polynomials. Coincident
indices are added, never treated as orthogonal observations.

**FNE26.T1.** For every integer Y>=2, the polynomial (3) satisfies

    p_Y[n]=mu(n) for n<=Y,
    p_Y(1)=0, p_Y'(1)=1, p_Y(0)=-2,
    support(p_Y) <= max(2Q P_Y,4Q).                       (4)

Moreover c_Y>0 and c_Y<=Y/log 2. These assertions are unconditional and do not
use PNT. The support is generally very large; it is NOT claimed to be O(Y),
and this candidate is not asserted to satisfy #803's fixed-ratio support or
coefficient-budget constraints.

Proof. The positive finite-prime Euler sum gives

    m_Y^(-1)=sum_(n Y-smooth) 1/n > H_Y > log(Y+1).

The last strict bound is the decreasing integral comparison. Including ALL
integers rather than only primes in the reciprocal product gives the upper bound

    m_Y^(-1) <= product_(n=2)^Y (1-1/n)^(-1)=Y.

Thus c_Y has the stated signs and size. At s=1,
B_Y(1)=0 and B_Y'(1)=log Q+c_Y log 2=1/m_Y. This proves balance and the derivative.
The last term of (3) has a double zero at s=1. Since M_Y(0)=0, its value -2 at
s=0 proves centering. No term of either late correction starts below Q. Every
n<=Y is either squarefree, with the correct coefficient in M_Y, or has mu(n)=0.
The support bound follows directly by multiplying the finite polynomials. QED.

The construction was intended to use the COMPLETE multiplicative relations,
not merely the positivity or gap of a graph built from them. Safe-axis jets
are imposed before the norm estimate, not retrofitted after a numerical solve.

## 3. The full norm nevertheless grows much too quickly

**FNE26.T2.** For the literal candidate (3), as Y tends to infinity through the
integers,

    lim [(log Y)/sqrt Y] log(1+E(p_Y)) = 4.               (5)

Equivalently E(p_Y)=exp[(4+o(1))sqrt Y/log Y]. This is a complete-norm asymptotic,
not a lower estimate on a point sample, not a finite-cutoff extrapolation, and
not a theorem about the optimized minimum. It holds without RH. In particular
this candidate fails even assuming RH. Its error is larger than every fixed
power of Y eventually, whereas (2) needs a subpower upper bound.

We prove both sides. Only the next elementary consequence of PNT is imported.

### 3.1 The low-frequency prime profile

Let S_Y=sum_(p<=Y)p^(-1/2) and a_Y=sqrt Y/log Y. Ordinary PNT, followed by partial
summation, gives

    S_Y ~ 2 a_Y.                                         (6)

For clarity, S_Y=pi(Y)/sqrt Y+(1/2)integral_2^Y pi(x)x^(-3/2)dx;
each leading contribution is asymptotic to a_Y. No RH-strength error is used.

For every fixed compact interval of real tau,

    (1/S_Y) sum_(p<=Y)p^(-1/2) exp[-i tau log p/log Y]
                         -> exp(-i tau)                  (7)

uniformly in tau. To see this, fix epsilon>0. The total mass of p<=Y^(1-epsilon)
is at most sum_(n<=Y^(1-epsilon))n^(-1/2)<=2Y^((1-epsilon)/2), which is o(S_Y).
On the remaining primes |log p/log Y-1|<=epsilon, so the phase difference is
at most |tau|epsilon. First let Y tend to infinity, then epsilon decrease to zero.
This proves uniformity on compact tau intervals; it is not a claim of random
or independent prime phases.

For 0<r<=1/sqrt2 the absolutely convergent local logarithm gives, uniformly in theta,

    |log|1-r exp(-i theta)|+r cos theta|
                              <=r^2/[2(1-r)].             (8)

The entire k>=2 series is in this remainder. Therefore

    log|M_Y(1/2+i tau/log Y)|
      =-Re sum_(p<=Y)p^(-1/2-i tau/log Y)+O(log Y),

since sum_(p<=Y)1/p<=H_Y. Because log Y=o(a_Y), (6)-(8) imply

    (1/a_Y)log|M_Y(1/2+i tau/log Y)| -> -2 cos tau          (9)

uniformly for bounded tau. This is an exact asymptotic of an ordinary-prime
finite product. Its maximum occurs near tau=pi, at a frequency tending to ZERO.

### 3.2 The required corrections do not cancel the growing band

Fix 0<epsilon<pi/2 and restrict tau to [pi-epsilon,pi+epsilon]. With
t=tau/log Y, (9) implies uniformly

    |M_Y(1/2+it)| >= exp[(2cos epsilon+o(1))a_Y].           (10)

Write the normalizing factor as

    B_Y(1/2+it)=1+sqrt Q exp(-it log Q)
                   {-1+c_Y[1-sqrt2 exp(-it log2)]}.

For all sufficiently large Y, cos(t log2)>=1/sqrt2 throughout this band.
As c_Y>=0, the real part of the braced expression is at most -1. Hence

    |B_Y(1/2+it)| >= sqrt Q-1.                            (11)

This estimate retains the phase of the late correction and its actual sign.
The centering term in (3) has uniform magnitude at most
2(1+sqrt2)^2/sqrt Q and is consequently negligible relative to (10)-(11).

No zero census is needed to control the remaining zeta factor. The alternating
eta series at 1/2 is strictly greater than 1-1/sqrt2, so
zeta(1/2)=eta(1/2)/(1-sqrt2)<0. By continuity there is a fixed neighborhood
of t=0 on which |zeta(1/2+it)| is bounded below by a positive constant.
Our entire shrinking band lies in that neighborhood eventually.

Thus the integrand in (1), on an interval of width 2epsilon/log Y, has a lower
bound of a positive polynomial factor times exp[(4cos epsilon+o(1))a_Y].
The target 1 is negligible there; no reverse triangle inequality is applied
without first obtaining this divergence. The denominator 1/4+t^2 is bounded
above and below. Consequently

    liminf (1/a_Y)log(1+E(p_Y)) >=4cos epsilon.

Let epsilon decrease to zero. This proves the lower half of (5). The interval,
not just its center, was used, and its shrinking width contributes only
O(log Y) to the logarithm of the lower bound.

### 3.3 All other frequencies are paid by an exact global zeta norm

We use a short global identity instead of truncating frequency or importing a
pointwise estimate whose constants might depend on the product length:

    Z0=(1/(2pi))integral_R |zeta(1/2+it)|^2/(1/4+t^2)dt
       =1+integral_1^infinity {x}^2 dx/x^2 <2.             (12)

Proof. Initially for Re s>1, the floor integral yields

    zeta(s)/s=1/(s-1)-integral_1^infinity {x}x^(-s-1)dx.

Both sides continue to Re s>0, s!=1. On s=1/2+it, the first term is the Fourier
transform of -exp(u/2)1_(u<0), while the second is the Fourier transform of
-exp(-u/2){exp u}1_(u>=0). These two functions are in L1 and L2 and have disjoint
supports. Plancherel gives (12), including its normalization. This does NOT say
zeta(s)/s is a causal Hardy function: its negative-time part was retained.

For all real t,

    |M_Y(1/2+it)| <= product_(p<=Y)(1+p^(-1/2)) <= exp(S_Y),
    |B_Y(1/2+it)| <= 1+sqrt Q[1+(1+sqrt2)c_Y]=O(Y^(3/2)).

Together with the centering term, sup_t |p_Y(1/2+it)|<=C Y^(3/2)exp(S_Y), with
an absolute C. Since the unit target has normalized norm squared 1, (1),(12)
and |a-b|^2<=2|a|^2+2|b|^2 give

    E(p_Y) <=2+4 sup_t |p_Y(1/2+it)|^2
             <=2+C'Y^3 exp(2S_Y).

Equation (6) now implies limsup in (5) is at most 4. This proves the theorem.
The upper bound includes the full infinite frequency line and therefore the
entire physical future. QED.

## 4. What this settles, and what it does not

The attempted proof was: retain complete finite Euler multiplicativity, impose
the native prefix and safe jets exactly, and pass to increasing preserved
horizons using a small complete norm. The small-norm assertion for (3) is FALSE;
(5) gives its exact leading growth scale. The construction is rejected.

This does not invalidate #803's much better fixed-ratio completions, its finite
minima, or its compression theorem. Their coefficients are different. Nor does
it refute #811/#818's continuum-corrected Euler sources. Those corrections were
introduced precisely because a raw finite Euler product cannot simply be used
in the critical strip. A fixed safe-point normalization is not that full causal
continuum correction.

No claim is made that every multiplicative method fails, that a modified
candidate cannot work, or that the optimized minimum is large. The upper bound
required in Section 1 is still OPEN. The conclusion is not a new zero-free
region, a reduction of the remaining gap, or an RH completion.

## 5. Classical inputs and review points

[E1] Euler products and Mobius Dirichlet series: NIST DLMF 27.4.3 and 27.4.5.
[E2] Ordinary prime number theorem: NIST DLMF 27.12.4 (only its leading term).
[E3] Fourier Plancherel, analytic uniqueness, and the functional equation of zeta
are standard analytic inputs; the exact source and normalization needed here
are explicitly derived in Sections 1 and 3.3.

Gonek, "Finite Euler products and the Riemann Hypothesis", arXiv:0704.3448,
is relevant prior context. Only its abstract was read in this pass; none of
its RH-conditional approximation theorems is an input above. No priority claim
is made for finite-Euler-product failure or the general approximation framework.

The principal review checks are (1), the exact three normalizations in (4),
the UNIFORM shrinking-band limit (9), the noncancellation estimate (11), the
negative-time term in (12), and the matching complete-norm upper bound.
The code checks finite coefficient algebra, not PNT or the analytic limit (5).
