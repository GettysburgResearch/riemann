# HBR29 — two separated scales in the native Brownian cutoff

Date: 2026-09-12. **PROPOSED component proofs, requiring independent mathematical review. RH is not proved.**

This continues HBR28, published as PR #872 at `45281093179434e08d28d8e589a8c70d70ead5b9`, without changing its source. It addresses the high-order Mellin-comparison problem left after HBR28 equations (25)–(26). A factorial-loss estimate is replaced by a complete O(1/m) normalized bound and a sharp relative asymptotic on growing complex-height windows. The same analysis disproves the attempted phase ending for every sufficiently high individual mode. A separate identity identifies the comparison's arithmetic-shift coefficient polynomials as a classical Meixner–Pollaczek family.

The mode index m is NOT branching depth, gamma truncation rank, the homotopy parameter in PR #876, or a count of zeta zeros. No numerical experiment is a premise. Classical probability, gamma, orthogonal-polynomial and complex-analysis tools are credited below; no external priority claim is made.

## 1. Exact sources and inherited identities

Let independent mean-one exponentials define

\[
X=\frac6{\pi^2}\sum_{j\ge1}\frac{E_j}{j^2},\qquad
L(t)=\mathbb E e^{-tX}=\frac{\sqrt{6t}}{\sinh\sqrt{6t}},\quad L(0)=1.
\tag{1}
\]

The positive series has mean one; the classical sinh product gives its transform. The Biane–Pitman–Yor identity in this normalization is

\[
\xi(2q)=\frac12(\pi/6)^q\mathbb E(X+X')^q.
\tag{2}
\]

This is an explicitly imported classical source identification, not an assumption about zero geometry. The two-scale estimates below require only (1); the neutral mode and Xi interpretation use (2).

For integer m>=1 put c=2m-1, epsilon=2^(-c), and

\[
a_m=\int_1^2u^{-2m}du=(1-\epsilon)/c.
\]

Let V_m have density u^(-2m)/a_m on [1,2]. Let Vtilde_m have Pareto density c u^(-c-1) on [1,infinity). With fresh independent variables at every position define

\[
W_m=\sum_{j\ge1}\Big(\prod_{i\le j}V_{m,i}^{-2}\Big)X_j,
\quad C_m=W_m+X_0,\quad P_m(t)=\mathbb E e^{-tW_m},\quad H_m=LP_m.
\tag{3}
\]

Tildes denote the corresponding Pareto objects. The mean scale factors are a_(m+1)/a_m<1 and c/(c+2)<1, so both positive series converge in L1 and almost surely. Apply the affine recursion first to finite sums and induct in moment order to obtain all positive moments. Since C_m,Ctilde_m>=X_0, (1) and the negative-moment Laplace integral give all inverse moments. Thus their Mellin transforms are entire. Real logarithms define positive-variable powers.

The entire companions are

\[
G_m(2q)=\frac12(\pi/6)^q(-1)^m q(q-1)\cdots(q-m+1)\mathbb E C_m^{q-m},
\tag{4}
\]

and similarly Gtilde. For Re q<m,

\[
G_m(2q)=\frac{(\pi/6)^q}{2\Gamma(-q)}
 \int_0^\infty t^{m-q-1}L(t)P_m(t)dt.
\tag{5}
\]

The identity follows from negative-moment inversion and Gamma(m-q)/Gamma(-q)=(-1)^m q(q-1)...(q-m+1). Equation (4) defines the removable values.

Writing r=sqrt(6t), the Pareto affine integral, followed by differentiation, gives 2t Ptilde'=c(L-1)Ptilde. Hence

\[
\widetilde P_m(t)=\left[\frac{2\tanh(r/2)}r\right]^c.
\tag{6}
\]

Direct differentiation verifies the ODE and value one at zero; the affine L1 contraction identifies the positive-law solution uniquely. The NATIVE affine integral retains both endpoints:

\[
2tP_m'(t)+cP_m(t)=a_m^{-1}[H_m(t)-\epsilon H_m(t/4)].
\tag{7}
\]

Comparing the two equations gives

\[
\frac d{dt}\frac{P_m(t)}{\widetilde P_m(t)}
 =\frac{\epsilon}{2a_mt\widetilde P_m(t)}[H_m(t)-H_m(t/4)]<0.
\tag{8}
\]

The ratio starts at one and tends to zero: W_m>=X_1/4 implies P_m(t)<=L(t/4), whereas (6) decays polynomially. Thus

\[
S_m(r)=P_m(r^2/6)/\widetilde P_m(r^2/6)=\mathbb P(Z_m>r)
\tag{9}
\]

is a survival function with positive density -S_m'. This is the square-root rescaling of HBR28's cutoff, Z_m=sqrt(6T_m). No complete monotonicity or zero-preserving property is assumed for it.

Quantile coupling gives V_m<=Vtilde_m, hence W_m>=Wtilde_m. The affine means give the exact distance

\[
\delta_c=\mathbb E(W_m-\widetilde W_m)
=\frac{3\epsilon c(c+2)}{16-(6c+16)\epsilon}.
\tag{10}
\]

In particular 0<=Ptilde_m(t)-P_m(t)<=t delta_c for real t>=0. Equations (6)–(10) are the inherited cutoff machinery, with its normalization and signs rederived here.

## 2. HBR29-1: an exact two-variable Mellin representation

Let R_c have distribution

\[
\mathbb P(R_c\le r)=\tanh(r/2)^c,\qquad
f_c(r)=\frac c2\tanh(r/2)^{c-1}\operatorname{sech}^2(r/2),\quad r>0.
\tag{11}
\]

For Re s<c+1 set

\[
\widetilde F_m(s)=\mathbb E R_c^{1-s},\qquad
F_m(s)=\mathbb E[R_c^{1-s}S_m(R_c)]
      =\mathbb E[R_c^{1-s}\mathbf1_{\{R_c<Z_m\}}],
\tag{12}
\]

where R_c and Z_m are independent in the last expression. Exactly,

\[
\boxed{G_m(s)=d_m\frac{\pi^{s/2}}{\Gamma(-s/2)}F_m(s),\quad
\widetilde G_m(s)=d_m\frac{\pi^{s/2}}{\Gamma(-s/2)}\widetilde F_m(s),
\quad d_m=\frac{(2/3)^m}{2c}.}
\tag{13}
\]

**Proof.** Substitute t=r^2/6 in (5). Use (6),(9) and tanh(r/2)^c/sinh r=f_c(r)/c. All constants simplify to (13). Near zero f_c=O(r^(c-1)); at infinity f_c<=2c exp(-r). They pay both ends for Re s<c+1, including logarithmic factors on compact substrips. This justifies absolute Fubini in (12) and holomorphy. The representation retains the whole native law. QED.

Below c>=3 is odd and ell=log(2c)>1.

## 3. HBR29-2: a global envelope for the literal cutoff

Put q=exp(-r/2) and b(r)=(1+q^2)/(1+q)^2. Changing variables in (8) gives the exact density

\[
\boxed{-S_m'(r)=\frac c{1-\epsilon}
\left[b(r)^c\frac q{1-q^2}S_m(r/2)-\frac\epsilon{\sinh r}S_m(r)\right].}
\tag{14}
\]

Both terms are present. Let E_c=c(c+2)(3/5)^c. Then for EVERY r>=0,

\[
\boxed{0\le1-S_m(r)\le
\min\{1,E_c+6\exp[-(c/2)e^{-r/2}]\}.}
\tag{15}
\]

**Proof.** For odd c>=3, (6c+16)2^-c decreases, and the denominator in (10) is at least eight. Thus delta_c<=(3/8)c(c+2)2^-c. At r_0=2log2, (6) gives Ptilde=(3/(5log2))^c. The W1 bound gives

\[
1-S_m(r_0)\le\tfrac14(\log2)^2c(c+2)(5\log2/6)^c
\le\tfrac{49}{400}c(c+2)(7/12)^c\le E_c,
\]

using log2<7/10. Monotonicity pays all r<=r_0. For r>=r_0, q<=1/2 and

\[
(b^c)'=c b^c\frac{q(1-q)}{(1+q)(1+q^2)}.
\]

The ratio of c b^c q/(1-q^2) to this derivative is (1+q^2)/(1-q)^2<=5. Drop the negative term in (14) ONLY for an upper bound, use S_m(r/2)<=1, and integrate. This gives

\[
1-S_m(r)\le E_c+\frac5{1-\epsilon}[b(r)^c-b(r_0)^c]\le E_c+6b(r)^c.
\]

Finally b=1-2q/(1+q)^2<=exp(-q/2). This proves the full envelope, not only a compact-r estimate. QED.

## 4. HBR29-3: complete normalized error, uniform at all imaginary heights

For s=sigma+i tau, 0<=sigma<=1 and EVERY real tau,

\[
\boxed{|\ell^{s-1}(\widetilde F_m(s)-F_m(s))|\le2E_c+192/c.}
\tag{16}
\]

This is a normalized ABSOLUTE bound, not a relative bound at zeros or small values of the comparison.

**Proof.** Put alpha=1-sigma in [0,1]. By (11), f_c(r)<=2c exp(-r), P(R_c>r)<=min(1,2c exp(-r)), and E R_c<=ell+1. Concavity gives E R_c^alpha<=(ell+1)^alpha. Equations (12),(15) bound the unnormalized error by

\[
E_c(\ell+1)^\alpha+12c\int_0^\infty r^\alpha e^{-r}
                                  e^{-(c/2)e^{-r/2}}dr.
\]

Set u=(c/2)e^(-r/2). The second term equals

\[
\frac{96}{c}\int_0^{c/2}[2\log(c/(2u))]^\alpha u e^{-u}du
\le\frac{96}{c}(2\log c+1/2)^\alpha.
\]

For the inequality extend the bracket by zero for u>c/2 and apply Jensen under the probability measure u exp(-u)du. Its mean bracket is bounded by 2log c+2 integral_0^1(-log u)u du=2log c+1/2. For alpha=0 bound the mass by one separately. Divide by ell^alpha. Since ell>1 and 2log c+1/2<2ell, both power ratios are at most two. This pays the entire r integration and proves (16). QED.

The improvement removes HBR28's factorial loss by exploiting the native survival structure, not by assuming that its old Wasserstein bound passes through a high-order Mellin transform.

## 5. HBR29-4: two different Gumbel scales

Let Y have standard Gumbel CDF exp(-exp(-x)). Then

\[
\boxed{R_c-\ell\Rightarrow Y,\qquad Z_m-2\ell\Rightarrow2Y.}
\tag{17}
\]

The second convergence holds in total variation (the densities converge in L1). No joint coupling of the limits is asserted.

### Comparison law, quantitative coupling and all tails

For a mean-one exponential E, the exact quantile representation is

\[
R_c=\log\coth(E/(2c)),\quad
R_c-\ell=-\log E+\eta_c(E),\quad
0\le\eta_c(E)\le E^2/(12c^2).
\tag{18}
\]

Indeed tanh(R_c/2)=exp(-E/c), giving (11). The bounds follow from 1<=v coth v<=1+v^2/3 and log(1+x)<=x. For completeness, the upper hyperbolic bound is equivalent to (v^2+3)sinh v-3v cosh v>=0. Its coefficient of v^(2n+1) is 4n(n-1)/(2n+1)! for n>=1; lower coefficients vanish. Hence E eta_c<=1/(6c^2), and -log E has the stated Gumbel law.

We also have, uniformly in c and for every x>=0,

\[
\mathbb P(R_c-\ell>x)\le e^{-x},\qquad
\mathbb P(R_c-\ell<-x)\le e^{-e^x}\le e^{-1}e^{-x}.
\tag{19}
\]

For the second bound use log tanh(r/2)<=-2e^-r; below r=0 the probability is zero. The first follows from Section 4. Thus E|R_c-ell|<2 and E(R_c-ell)^2<4.

### Cutoff law, including mass in both tails

At r=2ell+x put u=exp(-x/2). Then q=u/(2c), b(r)^c->exp(-u), and c q/(1-q^2)->u/2. The envelope (15) at r/2=ell+x/2 shows S_m(r/2)->1. The negative epsilon term of (14) tends to zero. Therefore the shifted density, extended by zero when r<=0, tends pointwise on the whole real line to

\[
\tfrac12e^{-x/2}\exp[-e^{-x/2}].
\]

Both the native densities and this limiting density have mass one. Dominated convergence applied to their minimum proves L1 convergence: integral |f-g|=2-2 integral min(f,g). This is not compact convergence followed by an unproved normalization. Integrating proves the second law in (17). QED.

The main Mellin mass lives at r=ell+O(1), while the cutoff lives at r=2ell+O(1). The comparison's rare tail at the latter scale determines the correction.

## 6. HBR29-5: a gamma profile on growing complex windows

Fix K>=0. Uniformly for 0<=sigma<=1, |tau|<=K ell, t=tau/ell and s=sigma+i tau,

\[
\boxed{\ell^{s-1}\widetilde F_m(s)=\Gamma(1+it)+o_K(1),\qquad
\ell^{s-1}F_m(s)=\Gamma(1+it)+o_K(1).}
\tag{20}
\]

An explicit comparison error is

\[
A_c(K)=\frac{4+4K}{\ell}+\frac6{\sqrt{2c}}+\frac K{6c^2};
\tag{21}
\]

the native error is at most A_c(K)+2E_c+192/c.

**Proof.** Write Y_c=R_c-ell and alpha=1-sigma. The normalized integrand is

\[
(1+Y_c/\ell)^\alpha\exp[-it\ell\log(1+Y_c/\ell)].
\]

On |Y_c|<=ell/2 its difference from exp(-itY_c) is at most (2|Y_c|+K Y_c^2)/ell. Use the moments after (19). Outside that event the difference is at most 2+(Y_c)_+/ell. The complete two tails in (19) bound this contribution by 6 exp(-ell/2). The coupling (18) then bounds the characteristic-function difference by K/(6c^2), and Euler's gamma integral gives E exp(it log E)=Gamma(1+it). Add (16) for the native claim. QED.

### Explicit zero-free MODE windows

Gamma has no zeros, and on each fixed compact |t|<=K its modulus has a positive minimum. Thus (21) proves nonvanishing of F_m,Ftilde_m throughout these expanding windows at all sufficiently large modes. These are NOT Xi zero-free regions.

For an explicit conservative example, for EVERY odd c>=2^64,

\[
F_m(s)\ne0,\quad\widetilde F_m(s)\ne0
\quad(0\le\Re s\le1,\ |\Im s|\le\ell).
\tag{22}
\]

For odd c>=127, E_c<=1/c: check cE_c<1 at 127, and note its successive-odd ratio is (9/25)(c+2)(c+4)/c^2<1 for c>=5. Since log2>2/3, the error for K=1 is strictly below

\[
12/65+6/2^{32}+1/(6\,2^{128})+194/2^{64}<1/4.
\]

The gamma product [D3] gives

\[
|\Gamma(1+it)|^2=\prod_{n\ge1}(1+t^2/n^2)^{-1}\ge e^{-2t^2},
\]

using sum n^-2<2. For |t|<=1 this is |Gamma|>=e^-1>1/3. The strict triangle inequality proves (22). The non-strict product inequality at t=0 is intentional. These are exact paper constants, not a computation at astronomically large m.

By (13) the raw G_m,Gtilde_m have no zero in the OPEN critical strip at these heights. On its closed boundary, their forced zero at s=0 must be retained. The normalized F_m is only asserted holomorphic on Re s<c+1, not entire on all C.

## 7. HBR29-6: the sharp rare-tail correction and relative comparison

Uniformly in the same growing windows with fixed K,

\[
\boxed{c(2\ell)^{s-1}[\widetilde F_m(s)-F_m(s)]
                  =\Gamma(2+it)+o_K(1).}
\tag{23}
\]

Consequently, for all sufficiently large m,

\[
\boxed{\frac{G_m(s)}{\widetilde G_m(s)}
=1-\frac{2^{1-s}}c\left(1+i\frac{\Im s}{\ell}+o_K(1)\right),
\quad0\le\Re s\le1,\ |\Im s|\le K\ell.}
\tag{24}
\]

At s=0 use the removable quotient F_m/Ftilde_m. The uniform o_K(1) is proved, but an effective rate for this sharp correction is not supplied. Equation (16), in contrast, is explicit. No all-imaginary-height relative estimate is asserted.

**Proof, retaining both full tails.** In (12) put r=2ell+x. For fixed x,

\[
c f_c(2\ell+x)\to\tfrac12e^{-x},\quad
1-S_m(2\ell+x)\to e^{-e^{-x/2}},\quad
(r/(2\ell))^{1-s}\to e^{-itx/2}.
\]

The last convergence is uniform in sigma,t on the indicated compact parameter set and compact x sets. The contribution of min(1-S_m,E_c) is at most c E_c E[(R_c/(2ell))^(1-sigma)]<=cE_c->0.

For the remaining positive part, (15) gives (1-S_m-E_c)_+<=6 exp[-e^(-x/2)/4]. Also c f_c(2ell+x)<=(1/2)exp(-x), and (r/(2ell))^(1-sigma)<=1+x_+. Therefore

\[
3(1+x_+)e^{-x}\exp[-e^{-x/2}/4]
\]

is an integrable, c-independent majorant on the ENTIRE real x axis, after extending by zero when r<=0. Dominated convergence is uniform in sigma,t. The limiting integral is

\[
\frac12\int_{-\infty}^{\infty}e^{-x}e^{-e^{-x/2}}e^{-itx/2}dx
=\int_0^\infty u^{1+it}e^{-u}du=\Gamma(2+it),
\]

using u=exp(-x/2). This proves (23). Divide by (20), whose limiting gamma is uniformly separated from zero, and use Gamma(2+it)/Gamma(1+it)=1+it. The prefactors in (13) cancel. QED.

Thus a genuine relative comparison has replaced the factorial-loss obstruction, on a declared growing height regime. It does not compare either function to Xi itself.

## 8. HBR29-7: every sufficiently high individual mode fails the phase ending

Let A(z)=Xi(z)=xi(1/2+iz), and keep the actual odd-reflected companion

\[
B_m(z)=\frac{G_m(1/2+iz)-G_m(1/2-iz)}{2i}.
\tag{25}
\]

For ANY fixed z=x+iy with x>0, 0<y<1/2 and A(z)!=0, the phase Im[A(z) conjugate(B_m(z))] has positive and negative values for infinitely many integer m. More strongly, fix y in (0,1/2) and a compact interval [a,b], 0<a<b, on which A(x+iy) has no zero. For EVERY sufficiently large m the phase takes both signs somewhere on this fixed interval. Thus merely choosing a sufficiently high individual mode cannot give the original all-band positive phase condition.

**Proof.** For fixed s, (20) tends to Gamma(1)=1. Equation (13) becomes, uniformly on compact subsets of 0<=Re s<=1,

\[
G_m(s)=d_m\frac{\pi^{s/2}}{\Gamma(-s/2)}\ell^{1-s}(1+o(1)).
\tag{26}
\]

For s=1/2+iz, the reflected G_m(1-s) has smaller amplitude by ell^(-2y). Exactly conjugate(B_m)=i(conjugate(G_m(s))-conjugate(G_m(1-s)))/2, so

\[
\frac{\operatorname{Im}[A(z)\overline{B_m(z)}]}
{(d_m/2)\ell^{1/2+y}}
=\Re\{C(z)e^{ix\log\ell}\}+o(1),\quad
C(z)=A(z)\overline{\pi^{s/2}/\Gamma(-s/2)}\ne0.
\tag{27}
\]

The phase x log ell increases without bound, with successive m increments tending to zero. It therefore approaches every prescribed phase modulo 2pi along unbounded subsequences, giving the fixed-point assertion.

On [a,b], C has a positive minimum modulus and a continuous argument. The difference of the endpoint arguments of C(x+iy) exp(ix log ell) is (b-a)log ell plus a fixed constant. It tends to infinity. The intermediate value theorem supplies both even and odd multiples of pi inside the interval for every sufficiently large m. The uniform o(1), smaller than min|C|, preserves both signs. QED.

Such an interval exists without RH: A(iy)>0 by the positive real Mellin identity (2), and continuity gives a short horizontal interval with x>0. No zero ordinate, simplicity assumption or sampled sign is used.

The neutral identity G_1(s)=-s xi(s)/4 can be recovered directly: differentiate L(t)=integral_1^2 L(t/u^2)^2 du to identify P_1=-L' as the size-biased X transform. Then H_1=-LL' is the size-biased pair transform (pair mean two), so E C_1^(q-1)=E(X+X')^q/2. Substitution into (4) proves the identity.

The high-mode normalized limit is a gamma profile, not Xi. No descent preserving exclusion of OFF-critical zeros, while allowing central zeros to form, has been proved. Total zero-freedom cannot be transported to G_1, which has the actual critical-line zeros. The obstruction above concerns individual companions, not every signed combination or RH.

## 9. HBR29-8: a classical orthogonal family in the shift coefficients

The literal HBR28 coefficient polynomial is

\[
\mathcal B_m(v)=4\sum_{l=0}^{m-1}\binom{m-1}{l}
\frac{4^l}{(2l+1)!}\prod_{j=1}^l(v^2-j^2).
\tag{28}
\]

It satisfies

\[
\boxed{\mathcal B_m(v)=\frac{4(-1)^{m-1}}{2m-1}
P_{2m-2}^{(1)}(iv;\pi/2),}
\tag{29}
\]

where P is the CLASSICAL Meixner–Pollaczek polynomial. All coefficients in v^2 are strictly positive, and for m>=2 all roots are simple, nonzero and purely imaginary.

### Generating-function proof from the finite sum

Put a_l(v)=4^l product_(j=1)^l(v^2-j^2)/(2l+1)!. The even function J(w)=cosh(2v asinh w) satisfies

    (1+w^2)J''+wJ'-4v^2J=0, J(0)=1.

Its coefficient recurrence gives

\[
\sum_{l\ge0}a_l(v)w^{2l}=\frac{J'(w)}{4v^2w}
=\frac{\sinh(2v\operatorname{asinh}w)}{2vw\sqrt{1+w^2}},
\]

with removable values at v=0 or w=0. Sum the binomial transform in (28), set w=z/sqrt(1-z^2), and use asinh w=atanh z near zero. The result and its derivative are

\[
\sum_{n\ge0}\frac{\mathcal B_{n+1}(v)}4z^{2n+1}
=\frac{\sinh(2v\operatorname{atanh}z)}{2v},
\tag{30}
\]

\[
\sum_{n\ge0}\frac{(2n+1)\mathcal B_{n+1}(v)}4z^{2n}
=\frac{\cosh(2v\operatorname{atanh}z)}{1-z^2}.
\tag{31}
\]

These hold as convergent series near zero and coefficientwise for every v. In the classical MP generating function [D6], put lambda=1, phi=pi/2, x=iv and series variable iz. Its even part has coefficients (-1)^n P_(2n)^(1)(iv;pi/2) and equals the right side of (31). This proves (29), not just finite coefficient agreement.

### Explicit Jacobi matrix and polynomial zeros

Write p_n(x)=n! P_n^(1)(x;pi/2)/2^n. The classical recurrence [D5] becomes

\[
p_0=1,\quad p_1=x,\qquad p_{n+1}=xp_n-\frac{n(n+1)}4p_{n-1}.
\tag{32}
\]

Hence p_N is the characteristic polynomial of the symmetric N-by-N tridiagonal matrix with zero diagonal and off-diagonal entries sqrt(j(j+1))/2, j=1,...,N-1. Its eigenvalues are real and simple: an eigenvector's first component cannot vanish, and the recurrence determines every later component from it. Its spectrum is symmetric under x -> -x by alternating diagonal conjugation. At even N=2n,

    p_(2n)(0)=(-1)^n product_(j=1)^n (2j-1)(2j)/4 !=0.

Thus (29) is a positive constant times product_(j=1)^(m-1)(v^2+x_j^2), x_j>0. This proves the coefficient and root assertions without a numerical eigenvalue solve.

The classical weight is |Gamma(1+ix)|^2=pi x/sinh(pi x), and the squared norm of P_n^(1)(x;pi/2) is pi(n+1)/2 [D4]. The gamma factor in the two-scale limit is also the classical weight underlying these shift coefficients. These Jacobi eigenvalues are NOT Xi zeros, and no positive Xi characteristic operator follows.

General orthogonal-polynomial approaches to Xi predate this packet, including Romik's Meixner–Pollaczek expansions [R], with different parameters, and earlier work discussed there. The contribution here is the direct identification of the exact HBR28 array (28), not discovery of that broad programme.

## 10. End-to-end disposition and exact remaining gap

The completed proposed component chain is

    unchanged source -> exact cutoff -> global envelope -> two-scale limits
    -> complete Mellin comparison -> growing-window MODE zero-freedom.

The proposed single-companion phase ending fails by (27). A successful signed combination still needs a genuinely Xi-specific sign theorem, with no common-zero loophole. A descent preserving critical-line confinement, rather than total zero-freedom, would require a new proof. The signed zero-production estimate in PR #876 concerns a different parameter and is not settled by these mode asymptotics. None of those closing assertions is supplied or assigned to reviewers as a routine check.

**No complete RH proof, Xi zero, Xi verification height, or independent mathematical acceptance is claimed.** The finite checker supports bounded algebra; it does not formalize the all-order analytic arguments.

### Frozen repository sources and reading scope

[P] PR #872 at `45281093179434e08d28d8e589a8c70d70ead5b9`, path `standalone/2026-09-12-astra-hyperbolic-renormalization/PROOF.md`, blob `d2f12cf36103161b36c21010051770fda8d7d585`. The full supplied local manuscript was read and its Git blob checked against the connector's remote blob. Selected live excerpts and PR metadata were read. Parent code/certificates were not rerun.

[H] PR #876 at `8002444ec4d4bd1c6f8fa073820bcc575cb218e1`, path `standalone/2026-09-12-beta-fixedpoint-homotopy/PROOF.md`, blob `bb82833e204abb8a69a7602642b3d0cb4e7b7024`. Sections 1–6 and the start of Section 7 were inspected in connector excerpts. This is context, not an imported theorem or independent acceptance. The #865–#875 descriptions received targeted body/metadata reconnaissance only; no full-branch audit is claimed.

### Classical primary references

[B] Biane, Pitman and Yor, *Probability laws related to the Jacobi theta and Riemann zeta functions, and Brownian excursions*, arXiv:math/9912170. https://arxiv.org/abs/math/9912170 . Classical identity (2), inherited through the preceding packets; abstract metadata rechecked, not a fresh independent review of the complete external proof.

[D1] NIST DLMF 5.2: gamma integral and zero-free property. https://dlmf.nist.gov/5.2 .
[D2] NIST DLMF 5.5: gamma recurrence/reflection. https://dlmf.nist.gov/5.5 .
[D3] NIST DLMF 5.8.3: gamma modulus product. https://dlmf.nist.gov/5.8 .
[D4] NIST DLMF 18.19.8–9: MP weight and norm. https://dlmf.nist.gov/18.19 .
[D5] NIST DLMF 18.22.8: MP recurrence. https://dlmf.nist.gov/18.22 .
[D6] NIST DLMF 18.23.7: MP generating function. https://dlmf.nist.gov/18.23 . The specialized proofs and constants used here are given above.

[R] Dan Romik, *Orthogonal polynomial expansions for the Riemann xi function*, arXiv:1902.06330; Acta Arithmetica 200 (2021), 259–329. https://arxiv.org/abs/1902.06330 . Abstract and selected PDF pages were inspected, including screenshots in the earlier part of this attempt; not a complete paper audit or imported RH result. No comprehensive novelty claim.
