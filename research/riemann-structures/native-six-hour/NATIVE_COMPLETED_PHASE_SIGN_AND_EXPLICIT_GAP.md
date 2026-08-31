# A uniform phase sign and explicit primitive gap in the completed source

This proof concerns the literal half-source at a fixed nonempty finite prime
set P. It preserves the factor two, all source exponents and the original
observation measure. It is not a statement about the full retained-gamma
family, the all-prime limit, or the Riemann hypothesis.

The completion theorem at commit
822646ffea23d906c385f0273a8c45693e982c4d, file
FIXED_PRIME_INFINITE_HORIZON_COMPLETION.md, blob
851e4331c12d9f3f073ab73dca26baa33bd5e548, establishes the absolutely
convergent current and the admissible monotone path space used below.
The original primitive is L-102707 at
ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc, blob
6810bcece309b0c54ae6c8fc84b314990004549c.

## 1. A local phase derivative independent of the schedule coordinate

Put q_p=p^(-1/2), z_p=q_p exp(it log p), and use principal square roots.
For 0<=x<=1 write

    A_p = sqrt(1-z_p^2),
    C_p = sqrt(1-z_p),
    ell_p(x) = A_p + x(C_p-A_p),
    S(x,t) = product_p ell_p(x_p).

All radicands have positive real part. On |z|<1, analytic continuation
from z=0 gives the branch-compatible identity

    C_p/A_p = (1+z_p)^(-1/2).

Since |C_p-A_p|^2 is real, the local imaginary current is independent of x:

    Im(conj(ell_p(x)) (C_p-A_p))
      = Im(conj(A_p) C_p)
      = |1-z_p^2| Im((1+z_p)^(-1/2)) =: h_p(t).             (1)

The actual completed observation is F_gamma(t)=2 integral conj(S)dS.
The product rule and absolute convergence therefore give exactly

    Im F_gamma(t)
      = 2 sum_p h_p(t) integral_gamma product_(j!=p)|ell_j(x_j)|^2 dx_p.
                                                                    (2)

No source direction, cross term or ratio alias has been removed.

## 2. The sign is the same for every admissible path

Set p_max=max P. For 0<t<pi/log(p_max), each theta_p=t log p lies in
(0,pi). Thus Im(1+z_p)>0 and Im((1+z_p)^(-1/2))<0. Equation (1) gives
h_p(t)<0 for every p.

For any complex w with positive real part,

    Re sqrt(w) = sqrt((|w|+Re w)/2) >= sqrt(Re w).

Consequently, for every real t and x in [0,1],

    Re C_p >= sqrt(1-q_p),
    Re A_p >= sqrt(1-q_p^2) >= sqrt(1-q_p),
    |ell_p(x)|^2 >= 1-q_p.                                  (3)

Every admissible path has nonnegative dx_p and total increment one.
Equations (2) and (3) show, without any conditioning constant,

    Im F_gamma(t) < 0       for 0<t<pi/log(p_max).             (4)

This sign statement holds uniformly for all actual monotone schedules,
including schedules with pauses and simultaneous coordinate motion.
Real source coefficients imply F_gamma(-t)=conj(F_gamma(t)), so the
opposite sign holds on the reflected interval.

## 3. An explicit path-independent lower envelope

For w=a+ib=1+q exp(i theta), with 0<theta<pi,

    -Im(w^(-1/2)) = b / (|w| sqrt(2(|w|+a))).

Here |w|<=1+q and a<=1+q. Also |1-z^2|>=1-q^2. Hence

    -h_p(t) >= (1-q_p) q_p sin(theta_p)/(2 sqrt(1+q_p)).      (5)

In (2), all terms have the same sign. Multiplying (5) by the lower bound
in (3) for every other coordinate and using integral dx_p=1 yields

    -Im F_gamma(t) >= L_P(t),
    L_P(t) = product_p(1-q_p)
             * sum_p q_p sin(t log p)/sqrt(1+q_p),            (6)

throughout the interval in (4). The original factor two in the current
cancels the denominator two in (5).

In particular let

    T_P = pi/(2 log(p_max)),
    c_P = (2/pi) product_p(1-q_p)
                    * sum_p q_p log p/sqrt(1+q_p) > 0.

The elementary inequality sin(theta)>=2 theta/pi for 0<=theta<=pi/2
gives the simpler lower bound

    |Im F_gamma(t)| >= c_P |t|       for |t|<=T_P.            (7)

## 4. An explicit positive primitive contribution in the original norm

Use exactly dnu(t)=|kappa_hat(t)|^2 dt/(2pi) from the frozen primitive
observation. It is finite and even. The original compactly supported
nonzero kernel has a nonzero entire Fourier transform; its real zeros
are isolated. A zero at t=0 does not make the measure vanish on an
interval about zero.

The real part is the fixed endpoint function

    R_P(t) = product_p |1-z_p(t)| - product_p |1-z_p(t)^2|.

Therefore every admissible path satisfies

    ||F_gamma||_nu^2
      >= ||R_P||_nu^2 + Delta_P,
    Delta_P := c_P^2 integral_(-T_P)^(T_P) t^2 dnu(t) > 0.    (8)

One can instead integrate the larger envelope L_P(t)^2 over the full
sign interval for a sharper constant. Formula (8) is explicit in the
fixed primes and the original kernel; no smallest singular value,
finite-rank extrapolation or unproved positivity assumption is used.
The integral is finite since its domain is bounded and nu is finite.
Since the actual minimum exists by the completion theorem,

    m_infinity >= ||R_P||_nu^2 + Delta_P > ||R_P||_nu^2 > 0.   (9)

The last endpoint positivity follows also directly from
R_P(0)=product(1-q_p)-product(1-q_p^2)<0 and continuity.

## 5. An elementary closed lower bound for the specified kernel

The last integral can itself be bounded without numerical quadrature.
Set L=log 2 and s=sqrt 2. The three pieces of the exact kernel in
L-102880, at the same primitive commit, blob
d7330d114ebba1a7a16e22fa9ba6aa6b5eb7cdd6, give

    M_1 := integral u kappa(u) du = 8(s-1)L^2 > 0.          (10)

Indeed, the constant parts give
[4-12(1+s)+20s]L^2=8(s-1)L^2. For the exponential parts use the
primitive exp(u/2)(2u-4); their three endpoint contributions cancel
both the coefficient of L and the constant term. Thus (10) retains
the actual signed kernel, including its middle negative piece.

The same three pieces show |kappa(u)|<=8s on [0,3L], with zero outside.
Hence integral u^3|kappa(u)|du <= 2s(3L)^4. The elementary sine remainder
|sin v-v|<=|v|^3/6 then gives

    |Im kappa_hat(t) + M_1 t| <= s(3L)^4 |t|^3/3,           (11)

for the Fourier convention exp(-itu); the opposite convention reverses
both imaginary signs and gives the same absolute bound.
Define the explicit positive number

    tau_P = min(T_P, sqrt(3M_1/(2s(3L)^4))).

For |t|<=tau_P, equation (11) yields
|kappa_hat(t)|>=M_1|t|/2. Substitution into (8) proves the entirely
elementary estimate

    Delta_P >= c_P^2 M_1^2 tau_P^5/(20 pi) > 0.             (12)

The denominator 20 includes the original factor 1/(2pi) in dnu,
the Fourier lower bound factor 1/4, and
integral_(-tau)^tau t^4 dt=2tau^5/5. No zero-order assertion about the
Fourier transform is needed for (11): it uses its actual imaginary
part and the exact first moment.

## 6. What the bound does and does not decide

The theorem supplies a common phase sign and a source-exact obstruction
to removing the imaginary current by any admissible schedule. It is a
stronger effective version of a qualitative primitive-gap consequence
of infinite-source faithfulness. It does not identify the optimizer or
claim that the inequalities are sharp. It also does not claim a phase
sign for every finite product cutoff: finite truncation can interrupt
the completed product identity.

For a finite cutoff H and any compact interval [a,b] strictly inside
(0,pi/log(p_max)), a separate uniform completion bound epsilon_H does
imply the same negative sign whenever epsilon_H<min_[a,b] L_P.
This is a sufficient condition using the unchanged source tail, not an
assertion that a particular numerical cutoff has met it. No new numerical
acquisition was used in this proof.
