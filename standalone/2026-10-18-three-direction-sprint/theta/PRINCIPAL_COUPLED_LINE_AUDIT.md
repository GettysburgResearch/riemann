# Principal coupled-line audit and its paid physical operators

Status: **proposed exact component reductions and conditional exponent
budgets; no new zero-free region.** This is an independent audit developed
with the Eisenstein track after the sprint was redirected from finite
theta orders to a principal-only completion attempt. The local algebra is
native. The Hecke functional equation and the original physical probe are
imported with their stated normalization. Every use of a physical upper
bound below is explicitly conditional on that bound for the whole family
of dilated profiles.

## 1. Exact source and the issue being tested

Let F=Q(sqrt(-3)), Q=Np, and delete the fixed finite set S of primes as in
the source. The imported source is OpenAI's `original-quasi.tex`, resident
in the sibling Eisenstein directory as `_source-original-quasi.tex`,
actual-byte SHA256
`42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`.
The load-bearing passages are equations `local-parameters`, `5.13a`,
`local-H-definition`, `probe-high`, `probe-poisson-identity`, and `signal`.
The sibling track retains the source provenance and its full scope.

We specialize the target character eta to 1. The high-side row contains

    F_u(x,w,z)=zeta_F^S(6z) L^S(w,chi_u)
                    /L^S(x,bar chi_u) · H_u(x,w,z),       (1)

where chi_u means the original zero-extended character
`a -> chi_a(u)`. Its primitive inducing character may require a fixed
S-supported correction. Put

    s=x+w,        r=s-1.

The functional equation cancels the numerator and denominator on the
complex hypersurface r=0. Independent vertical x and w integrations do
not place the whole integral on this hypersurface. We test whether an
actual pole and an affordable physical operator can realize the
cancellation, rather than setting only the real parts to sum to one.

## 2. A universal coupling zeta factor

At p not dividing u set

    D=bar chi_p(u) Q^(-x),       W=chi_p(u) Q^(-w),
    V=Q^(-6z),                  R=a_p^2 Q^(4-6x-6z),
    E=P_p^*+D.

The source gives `H_p=P_p(1-V)(1-W)/(1-D)`. Its exact defect is

    H_p-1=[DW+(D-W)V-DVW+E(1-V)(1-W)]/(1-D).        (2)

Crucially `DW=Q^(-s)` with no row phase. Define

    J_{p,u}=(1-Q^(-s))H_p,       J_u=product_(p notin S) J_{p,u},

including the finitely many p dividing u in this definition. Then

    H_u=zeta_F^S(s) J_u,                            (3)

initially in absolute convergence and subsequently by continuation.
For p not dividing u, write

    B=(D-W)V-DVW+E(1-V)(1-W).

A direct multiplication of (2) gives

    J_{p,u}-1=
      [D^2 W(1-W)+(1-DW)B]/(1-D).                  (4)

There is no `1-W` denominator. The local factorization therefore exposes
an actual potential coupling pole at s=1; it is not merely a suggestive
comparison of two unrelated L-functions. For u=1 and sufficiently large
fixed S, J_1 is close to one on compact subregions of the domain below,
so this pole is nonzero there. Particular ramified rows can have a
vanishing residue; no nonvanishing claim for every u is needed.

For definiteness the following closed real-part region has strict local
margins:

    Re x>=51/100,  Re z>=17/50,  Re w>=-1/100,
    Re(x+w)>=99/100.                               (5)

All local denominators `1-D`, `1-R`, `1-V` stay away from zero uniformly.
Writing theta=max(-Re w,0), the source's j=0 formula gives

    |E| <= C[Q^(4-6Re x-6Re z+theta)
                    +Q^(1-Re s-6Re z)].

In (4) the first term has exponents at least
`Re x+Re s>=1.50` and `2Re s>=1.98`. The E term, after multiplication by
`1-W`, has exponent at least 1.08; all V terms have larger margins.
Consequently

    J_{p,u}=1+O(Q^(-27/25))             (p not dividing u), (6)

uniformly in all imaginary parts and unit phases. The ideal count
`#{a:Na<=T}=O(T)` proves normal convergence over these primes.

### The squarefree rows have a stronger uniform bound

Let j=v_p(u). The literal source j=1 formula, where D=W=0 but the local
`W_loc` has already been included in P_p, gives

    H_{p,j=1}=1+
      [R(1-Q^(-1))+Q^(-s)-Q^(1-s)V]/(1-R).          (7)

Hence

    J_{p,j=1}=1-Q^(-2s)
          +O(|R|(1+Q^(-Re s))+Q^(1-Re s)|V|),       (8)

and thus `J_{p,j=1}=1+O(Q^(-11/10))` throughout (5). In the formal
V=R=0 limit the factor is exactly `1-Q^(-2s)`, with no minus sign
depending on the number of prime factors of u.

Combining (6) and (8), **J_u is bounded independently of squarefree u**
throughout (5). This is stronger than the harmless `q_u^epsilon` bound.

For j>=2 the strict source term `(Q-1)Q^(-s)` is not multiplied by V.
The other terms have exponents bounded by

    j=2: -3/100;
    j=3: (1-Re s)-1/50 and -1/25;
    j=4: (1-Re s)-3/100;
    j=5: -3/50.

It follows, with `d=max(1-Re s,0)` and
`rad_2(u)=product_(v_p(u)>=2) Q`, that

    |J_u| <= C_epsilon q_u^epsilon rad_2(u)^d
          <= C_epsilon q_u^(d/2+epsilon).           (9)

To justify the constants, bound each exceptional factor by C Q^d,
then use `C^omega(u)<=C_epsilon q_u^epsilon`. The strict table term has
a V factor for j<=1: attributing a `Q^(1-Re s)` loss to j=1 would be
incorrect. Equation (9) is an upper bound, not an asserted lower bound
or inverse bound.

## 3. What the coupling residue actually contains

For a primitive finite-order Hecke character of conductor norm Q_u the
imported normalization is

    Lambda(s,chi)=(3Q_u)^(s/2)(2pi)^(-s) Gamma(s)L(s,chi),
    Lambda(s,chi)=epsilon_u Lambda(1-s,bar chi).

Thus, putting `C_u=3Q_u/(2pi)^2`, on w=1-x one obtains

    L(1-x,chi_u)/L(x,bar chi_u)
       =epsilon_u C_u^(x-1/2) Gamma(x)/Gamma(1-x).   (10)

The quotient is interpreted meromorphically first; (10) gives its
removable values at common zeros. Original zero extensions add their
literal finite deletion-factor quotient `E_S(x,u)`. In this family its
moving conductor is supported on rad(u), while the fixed S part is
bounded; the source gives `Q_u<<_S q_u`. Fixed S factors and gamma ratios
have at most the stated polynomial-height costs on fixed compact real
strips. They cannot simply be omitted from an exact phase formula.

If kappa_S is the residue of zeta_F^S at 1, the w-residue of the row's
new coupling factor is therefore

    kappa_S q_u^(-z) zeta_F^S(6z) J_u(x,1-x,z)
       ·epsilon_u C_u^(x-1/2) Gamma(x)/Gamma(1-x) E_S(x,u). (11)

The inverse L-function has disappeared from (11). In particular this
residue does **not** retain a pole at a hypothetical zero of the target
L-function. It is a nuisance term to bound or remove. The genuine target
detector remains the separate principal extraction w=1, z=1/6, u=1.

### The global Mobius sign must remain

For squarefree u the source's complete, CRT-normalized Gauss identity is

    gamma_1(u)gamma_2(u)=mu(u) alpha(u) G(u),
    gamma_1(u)=mu(u) alpha(u)G(u) conjugate(gamma_2(u)). (12)

The prime identity has a minus sign, but replacing it by one global minus
sign on a composite squarefree u loses mu(u).

Reciprocity presents `a -> chi_a(u)` as `chi_u(a)` times an S-supported
ray character from a fixed finite family. For coprime conductor factors,
the elementary CRT Gauss identity is

    tau(chi_1 chi_2)=chi_1(f_2)chi_2(f_1)tau(chi_1)tau(chi_2).

Accordingly a fixed S twist or a fixed different normalization contributes
only its displayed cross-evaluations and normalized S Gauss factor;
these are fixed-ray data as u varies. This mechanism does not supply an
extra mu(u). In particular, once the FE root is identified with gamma_1
up to those fixed-ray factors, (12) is a **Mobius-weighted** angular cubic
vector. The nonzero-angular, unweighted cubic-Gauss theorem cannot be
applied by silently dropping mu. Formula (8) shows that the leading
squarefree local correction does not supply the missing sign either.

A complete use of a specific cubic theorem still requires pinning every
different, finite-ray and primitive Gauss normalization; this audit does
not promote that comparison to a new mean estimate.

## 4. Two exact legal physical operations

The imported Mellin weight for the same physical probe is

    X^(1/2-z) Z^(x+z-1) Y^(w-1)
       Phi(x+z-1) M(z) W1hat(w).                    (13)

Common positive scaling `(X,Y,Z)->(tX,tY,tZ)` multiplies (13) by
`t^(x+w-3/2)=t^(r-1/2)`.

### 4.1. An absolutely weighted common inverse-zeta filter

Define, with the ideal Mobius function and the same S deletions,

    A(X,Y,Z)=sum_a mu_F(a) (Na)^(-3/2)
                         I(X/Na,Y/Na,Z/Na).         (14)

The coefficient mass `sum_a(Na)^(-3/2)` is finite. Moreover the annular
W1 cutoff makes this a finite sum at every fixed positive (X,Y,Z): if
`supp W1 subset [c_-,c_+]`, then `I(...,Y/Na,...)` vanishes when
`Na>c_+Y`, because every integral ideal has norm at least one.

On the initial absolute Mellin lines (14) multiplies the integrand by

    sum_a mu_F(a)(Na)^(-x-w)=1/zeta_F^S(x+w).         (15)

Equations (3), (6)--(9) supply the meromorphic continuation after that
exact cancellation. At the genuine principal extraction w=1,z=1/6 the
multiplier is `1/zeta_F^S(x+1)`. It is holomorphic and nowhere zero for
Re x>1/2, and consequently preserves every hypothetical target zero.

This is a legal arithmetic probe, but its small coefficient mass is not
by itself a proof that every native estimate survives: the new arguments
`X/Na,Y/Na,Z/Na` change the original scale geometry. A norm argument must
cover those trajectories, including their small scales.

### 4.2. A fixed derivative kills just the coupling pole

Write `D_X=X partial_X`, and similarly for Y,Z. The operator

    E=D_X+D_Y+D_Z+1/2                              (16)

multiplies (13) by r. Therefore r zeta_F^S(1+r) is holomorphic at r=0.
At the principal extraction the multiplier is x, which is nonzero on
Re x>1/2. Fixed profile logarithmic derivatives are legal in the native
smooth-profile calculus. Thus (16) is a possible way to remove the
coupling residue without a scale exponent cost, provided the native
bound is proved with those same fixed derivatives.

This opens the regular Euler product region (5); it does not bound the
remaining `L(w,chi_u)/L(x,bar chi_u)` away from r=0. In particular a
principal-only proof still needs a complete r-not-zero row estimate,
or a new correlated inverse/plain witness argument. Equations (9) and
(16) are explicit inputs for testing that remaining exponent budget.

## 5. A Cauchy projection pays for its width

For Re r>0 and R>0 the additional causal common-scale operation

    P_R A=integral_0^R t^(1/2) A(tX,tY,tZ) dt/t     (17)

has Mellin multiplier `R^r/r`. Moving the r contour through zero exposes
(11), multiplied by a residue independent of R, **and a remaining left
r-contour**. Dropping this remainder is not an identity.

There is a simple quantitative budget for this attempt. Suppose the
complete dilated family really satisfies the uniform native estimate

    |A(tX,tY,tZ)| <= C_epsilon
             [t max(X,Y)]^(1/2)(tZ)^epsilon,        (18)

on the full integration range, with its small-scale completion included.
Then direct integration proves

    |P_R A| <= C'_epsilon max(X,Y)^(1/2)
                                      R^(1+epsilon)Z^epsilon. (19)

Set X=Z^a,Y=Z^b. The genuine principal signal has exponent

    C(s)=s-5/6+a/3,

while the assumed native low exponent is `max(a,b)/2`. Write

    B(a,b)=5/6+max(a,b)/2-a/3.

For `R=Z^c`, c>0, (19) and the principal multiplier `R^s/s` give the
comparison boundary

    B_c=[B(a,b)+c]/(1+c).                           (20)

Whenever B(a,b)<1 this is strictly worse than B(a,b). A fixed power
suppression `R^(-delta)` of a left-r remainder cannot be purchased for
free by this direct broadening. A polylogarithmic R gives only a
polylogarithmic suppression, not the power saving required in the
continuation criterion.

For `R=Z^(-c)`, 0<=c<1, the comparison becomes `(B-c)/(1-c)`. If
`c<=min(a,b)`, this is exactly the old comparison written in the new
geometry

    Z'=Z^(1-c), a'=(a-c)/(1-c), b'=(b-c)/(1-c).

It is not an additional saving beyond that new scale choice. If c>b,
then every t<=R has `tY<=Z^(b-c)`, eventually below the smallest annular
scale; the original probe and (14) vanish identically there. Any formal
principal residue must then be canceled by the remaining high-side
terms. This gives a concrete check against discarding that remainder.

The full two-sided `t in (0,infinity)` projection is not rescued by an
improper integral: the genuine principal mode after the t^(1/2) weight
is t^s, and its infinity integral diverges when Re s>0. No full pure-line
projection has been proved by (17).

## 6. An absolute residue contour works only at an unhelpful budget

One may instead bound (11) absolutely over u. Using `Q_u<<q_u` and
`J_u<<q_u^epsilon` at r=0, a sufficient line is

    Re z>Re x+1/2+epsilon.

The complete sixth-free row sum converges there. At z=x+1/2+epsilon,
the physical factor (13), now with w=1-x, has exponent

    (2-a-b)Re x-1/2+O(epsilon).                     (21)

Compared with the principal exponent, the excess is

    -(a+b-1)Re x+(1-a)/3+O(epsilon).

If `a+b>1`, it is negative uniformly for Re x>1/2 provided

    5a+3b>5.                                      (22)

This is a valid sufficient coarse geometry, but with the same native
low cost it forces

    B(a,b)>15/16.

Indeed, for a>=b, (22) forces a>5/8 and B=5/6+a/6>15/16.
For b>=a, it forces b>(5-5a)/3, and minimizing
`5/6+b/2-a/3` over this half-plane gives the same balanced endpoint
a=b=5/8. Strict (22) makes the inequality strict.

In particular this bound cannot improve the working ordinary-zeta
benchmark near .874957. The conclusion is a paid contour estimate and
a failed optimization, not an improved zero-free region.

## 7. The remaining principal-specific question

The coupling pole is real, its residue has an exact FE cancellation,
and the derivative (16) can remove it while preserving the principal
detector. The refined normal-convergence estimate distinguishes the
squarefree sector from the squarefull part instead of charging every
row a conductor power. These are concrete reductions.

The missing analytic estimate is still for the **complete physical
derivative probe with r not identically zero**. In particular, the
phase in (12), or an operator that inserts its missing mu(u) without
destroying the native common-row estimate, cannot be assumed away.
No conclusion about RH or a stronger ordinary-zeta boundary follows
from the components proved here.

There is also a direct paid test of moving the reflected numerator
contour after (16). If its old line is `Re w=1-a_bin` and it is moved
left by d0>0, the FE conductor factor gains U^d0 on a row norm U, while
the physical factor gains Y^(-d0). Their net change is

    (U/Y)^d0,                                      (23)

before any squarefull correction cost. The relevant largest central
dyad has `U approximately Z^h`, where the source's geometry is
`h=1-l_x+ell` and `Y=Z^l_y`. Whenever l_y<=h, (23) is non-improving at
that dyad. This includes both the original and the compensated native
geometries. A benefit from this direct move requires
`l_x+l_y>1+ell`, the long-row regime where the low bound itself must
be re-proved at the required power. Thus (16) removes a genuine analytic
restriction but does not, by this direct conductor estimate, repair the
binding critical-dyad exponent.
