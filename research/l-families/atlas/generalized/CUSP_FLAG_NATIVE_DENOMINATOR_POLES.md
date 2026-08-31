# Canonical cusp quotient: native denominator-induced real poles

Status: PROPOSED SOURCE-SPECIFIC THEOREM, requiring independent frozen-SHA review.
Exactly five new files; LS/AW/EP/UQ/CZ/CF and every main branch remain unchanged.
The contribution is a SOURCE-SPECIFIC noncancellation proof at the second cusp
scale. It is not a generic Schur example, a numerical period calculation, or RH.

The complete frozen LS1653565cc80cde6fa882ae9e150626187d3071d0,
AW98b4058ac29ba88cf993d7a3ce67579fab0c7844 and
EP27496745df9dd49fcde17699d333a54cf8620772 packets are authenticated as15 blobs.
CF1--CF4, the source Fourier normalization, and all-vector moment bounds are
the same imported native objects. Classical analytic inputs are not machine proofs.

## 1. Result and what was not previously known

For each fixed0<delta<12 there is a NON-EFFECTIVE k_0(delta) such that for
EVERY even k>=k_0(delta), the actual first-q-coefficient quotient Q_k has
exactly ONE pole, counted with multiplicity, in each disc
\[
 |s-(1-24/k)|<\delta/k,\qquad |s-24/k|<\delta/k.             \tag{NP1}
\]
These poles are real, simple, reflected, and genuinely UNCANCELLED zeros of
the denominator determinant, not the already known poles at0 and1.
Writing the right pole s_{p,k}=1-c_{p,k}/k,
\[
 c_{p,k}\longrightarrow24,\qquad
 \operatorname{Res}_{s=s_{p,k}}Q_k(s)
   ={1152 A_2(k)\over k^2}(1+o(1))>0,\quad
 A_N(k):={\Gamma(k-1)\over(4\pi N)^{k-1}}.                \tag{NP2}
\]
The reflected residue is its negative. Every threshold/error assertion here
is eventual, uniform over the six fixed residue classes, but NOT effective.
There is no inheritance of65536 or6144 as a pole threshold.

CF4 proved the two endpoint residues but allowed cancellation at every other
denominator zero. RV's signed zero-minus-pole count also permits that
possibility; its positive net main term does not force any additional pole.
AW/LS treat the first scale c=12 inside a denominator-zero-free chamber.
Here the positive surviving cross-period is new load-bearing work.
We claim no global pole census, no absence of zeros in NP1's discs, no
uniqueness over a whole moving chamber, no critical-line result, no new
automorphic family, and no effective pole/zero separation.

## 2. Actual nested flags and an exact native shear

Keep k=12d+r, r in{0,4,6,8,10,14}, r=4a+6b,0<=a<=2,0<=b<=1.
The class k mod12=2 uses r14 and d=(k-14)/12. For sufficiently large k,d>=3.
Set
\[
 g_1=\Delta E_4^pE_6^b,\quad
 g_2=\Delta^2E_4^{p-3}E_6^b,\quad p=3d-3+a,
\]
\[
 W_2=\ker[q],\qquad W_3=\ker[q]\cap\ker[q^2].
\]
These are the native coefficient flags, not generic subspaces.
CF1's Miller basis gives W_2=span(f_2,...,f_d) and
W_3=span(f_3,...,f_d). Define the EXACT coefficient and shear
\[
 t_k=[q^2]g_1=-24+240p-504b=60k-744-864b,\qquad
 h=g_1-t_kg_2.                                          \tag{NP3}
\]
Then [q]h=1,[q^2]h=0 and [q^2]g_2=1. The basis
(h,g_2,f_3,...,f_d) is a unit-triangular change from the native Miller
basis. Both Q_k and its literal first-coefficient normalization are unchanged.
This cancellation is an AUTHORIZED fixed native basis shear, not a new flag.

The original Petersson norm is
G(f)=integral_F y^(k-2)|f|^2 dxdy. All dual norms below use G restricted to
the indicated flag. Write G_2=G(g_2). No free coefficient model is used.

## 3. Entire q tails and a cutoff that resolves exponential scales

Fix eta=1/10000 and Y=eta*k, with k sufficiently large that Y>=1.
Write rho=|q|=exp(-2pi y). On the complex q disc of radius
R_k=1/(1000k), the absolutely convergent AW product/series majorants imply,
for j=1,2 and p_j=3(d-j)+a,
\[
 |g_j/q^j|
 \le\exp\{24jR_k/(1-R_k)+480p_jR_k+1008bR_k\}<2.          \tag{NP4}
\]
Indeed p_j<=k/4, so the exponent is at most
120/1000+[48/(1-R_k)+1008]/(1000k)<1/4 for k>=48.
The same majorants are valid on this complex q disc by absolute convergence;
they are not bounds restricted only to real q or to points in F.

Cauchy's coefficient estimate applied to g_1/q and g_2/q^2, each bounded
by2 on |q|=R_k, gives for rho<=R_k/2
\[
 |g_1/q-1-t_kq|\le4\rho^2/R_k^2,\qquad
 |g_2/q^2-1|\le4\rho/R_k.
\]
Using |t_k|<=100k for k>=48 and NP3,
\[
 |h-q|\le4400000 k^2\rho^3,\qquad
 |g_2-q^2|\le4000 k\rho^3.                               \tag{NP5}
\]
As exp(-2pi eta k)k tends to0, these bounds hold throughout y>=Y for
all sufficiently large k. They imply |h|<=2rho, |g_2|<=2rho^2 there.
The tails in NP5 are full convergent q tails, not finite-prefix evidence.

On ALL of F the unchanged AW bounds |Delta|<1,|E4|<4,|E6|<16 yield
\[
 |g_j|^2\le2^{k-12j+2b}\le2^k\ (j=1,2),\qquad
 |h|^2\le21000k^2 2^k.                                  \tag{NP6}
\]
For the low mass M(f;Y)=integral_(F,y<=Y)y^(k-2)|f|^2,
the width of F is at most1, so NP6 bounds it by the displayed supremum
times Y^(k-1)/(k-1). The elementary factorial lower bound
(k-2)!>=((k-2)/e)^(k-2) now gives
\[
 M(h;Y)+M(g_2;Y)\le C k^4 10^{-k} A_3(k)                 \tag{NP7}
\]
with C=100000 for k>=10000 (and the native d>=3 chart).
For clarity, before absorbing constant/polynomial factors the exponential
base is at most48*pi*e*eta: use k/(k-2)<=2 for k>=4.
It is strictly smaller than1/10 since pi<4,e<3 give
48*pi*e/10000<576/10000<1/10. All remaining factors in the preceding
explicit factorial ratio are bounded by a constant times k^4. More explicitly,
use M(h;Y)+M(g_2;Y)<=22000k^2 2^k Y^(k-1)/(k-1); dividing by A_3
and using the factorial bound gives
1056000*pi*eta*k^3/(k-1) times
[24*pi*e*eta*k/(k-2)]^(k-2). For k>=4 this is at most
84480k^2 10^(-k), which is below the bound in NP7.
Thus NP7 is uniform for ALL sufficiently large weights, not a threshold sample.
The same calculation bounds any pure q^N low integral for fixed N<=3.

For m=0,1 use the exact auxiliary integrals
\[
 A_N^{[m]}=\int_0^\infty y^{k-2+m}e^{-4\pi Ny}dy,\quad
 A_N^{[0]}=A_N,\quad A_N^{[1]}={k-1\over4\pi N}A_N.
\]
In particular A_N^[1]<=kA_N for N>=1, and
\[
 {A_N\over A_2}=(2/N)^{k-1}.                             \tag{NP8}
\]
Nonintegral N such as5/2 below is only an absolute ERROR ENVELOPE,
not a new native Fourier frequency. Exact x-orthogonality of q^2 to the
tail g_2-q^2 on the high rectangle and NP5--NP7 give
\[
 G_2=A_2(1+o(1)).                                       \tag{NP9}
\]

## 4. Native analytic bounds, the second scalar quotient and its simple zero

Put c=k(1-s). For any fixed complex disc
Omega_R={|c-24|<R},0<R<12, work first on its CLOSED disc.
It is strictly inside the deeper coercivity chamber:
\[
 \operatorname{Re}{1\over2c}-{1\over72}
 ={324-|c-18|^2\over72|c|^2}
 \ge {324-(6+R)^2\over72(24+R)^2}=:m_R>0.                \tag{NP10}
\]
The EP8 Parseval bound applies to ALL f in W_3 with first order N=3:
E_f max(1,y)<=1+(k-1)/(12pi). LS5--LS10 apply to this same probability
measure and complex c; in particular E_f|y^(c/k)-1|=O_R(log k/k).
The unchanged Fourier normalization is
E*=C(s)y^s+D(s)y^(1-s)+R_s, with
C=pi/6+O_R(1/k), D=-k/(2c)+O_R(1), and |R_s|<=3rho.
The complex Bessel modulus bound is exactly LS8. Consequently
\[
 \operatorname{Re}{I_{1-c/k}(f,f)\over G(f)}
 \le k/72-k\operatorname{Re}(1/(2c))+O_R(\log k)
 \le-\kappa_R k,\qquad \kappa_R=m_R/2.                  \tag{NP11}
\]
After Petersson whitening, J_3=G_3^(-1/2)I_W3 G_3^(-1/2) has negative
Hermitian part and ||J_3^-1||<=1/(kappa_R*k). This follows from
||J_3 v||||v||>=|v*J_3v|; it assumes neither Hermitian nor normal J_3.

Thus E_k(c):=I_W3(1-c/k) is invertible on the same Omega_R for ALL
sufficiently large k. Entry poles c=0,k are outside. In the adapted
(g_2,W_3) basis define the actual second flag quotient
\[
 d_k(c)={\det I_W2\over\det I_W3}
       =I_s(g_2,g_2)-I_s(g_2,W_3)E_k(c)^{-1}I_s(W_3,g_2).
                                                               \tag{NP12}
\]
It is holomorphic on that fixed Omega_R. The two complex cross directions
are separate; transpose/adjoint substitutions are not used to bound them.

The same full-space absolute form estimate LS13--LS14 holds here:
|I_s(u,v)|<=C_R k sqrt(G(u)G(v)). Combining it with NP11 bounds
|d_k|<=C_R' kG_2, uniformly on the closed disc without a dimension factor.
Below we prove for every fixed real compact J in(12,36) that
\[
 {d_k(c)\over kG_2}\longrightarrow
 F_2(c):={1\over48}-{1\over2c}={c-24\over48c}             \tag{NP13}
\]
uniformly for real c in J. Only its restriction to Omega_R's real interval
is needed. The proof is supplied in section7; it does not presuppose NP13.

For completeness, the LS normal-family argument now has all hypotheses:
eventual holomorphy on ONE fixed Omega_R and a uniform local bound.
Cauchy estimates and Arzela--Ascoli give subsequential compact convergence;
the real interval limit NP13 and the identity theorem force every limit
to be F_2. Hence convergence is locally uniform throughout Omega_R.
It also holds for derivatives by the Cauchy integral formula.

Given fixed0<delta<12 choose delta<R<12. On |c-24|=delta,
|F_2|>=delta/[48(24+delta)]>0. Rouche therefore gives exactly one zero
counting multiplicity inside, for every sufficiently large even k.
Conjugation of the actual period determinant makes it real; it is simple.
Denote it c_{p,k}; compact convergence and simplicity imply
\[
 c_{p,k}\to24,\qquad
 d_k'(c_{p,k})={kG_2\over1152}(1+o(1))>0,               \tag{NP14}
\]
since F_2'(24)=1/(2*24^2)=1/1152. This is a c derivative.
This proves a denominator zero only. Its survival still requires sections5--8.

## 5. The positive principal cross-period, with its exact coefficient

For the remaining estimates c ranges over a FIXED real compact
J contained in(12,36), for example J=[23,25] near the zero.
Write P_s(y)=C(s)y^s+D(s)y^(1-s). The native bounds give
|P_s|<=C_J kX, |E*|<=C_J kX, X=max(1,y), and |R_s|<=3rho.
All q^N cross integrals of P_s on the high rectangle vanish unless
their Fourier indices match.

The q-to-q^2 principal R_s term has ONLY Fourier mode n=1.
The native cosine coefficient is4sqrt(y), not the inconsistent printed
factor previously corrected in CZ. Since the x integral of
exp(2pi ix)cos(2pi x) is1/2, this principal term is exactly
\[
 B_0(k,c)=2\int_Y^\infty
          y^{k-3/2}e^{-6\pi y}K_{s-1/2}(2\pi y)\,dy.    \tag{NP15}
\]
There is no zeta, extra factor2, or independent coefficient inserted.

Here is a quantitative real-order Bessel lower bound. The primary integral
DLMF10.32.8, with its variable written1+v/x, gives
\[
 {K_\nu(x)\over K_{1/2}(x)}
 =\mathbb E(1+V/(2x))^{\nu-1/2},
 \quad V\sim\operatorname{Gamma}(\nu+1/2,1).
\]
For0<=nu<=1/2 the exponent is nonpositive. Convexity and its tangent at0 give
\[
 1-{1/4-\nu^2\over2x}\le
 {K_\nu(x)\over K_{1/2}(x)}\le1,\qquad
 {K_\nu(x)\over K_{1/2}(x)}\ge1-{1\over8x}.              \tag{NP16}
\]
All distributions in this display merely abbreviate a positive explicit
Gamma integral; no probabilistic limit is assumed. With nu=s-1/2 and
x=2pi y>=2pi eta k, and K_1/2(2pi y)=e^(-2pi y)/(2sqrt y),
NP7's pure-q bound gives
\[
 B_0/A_2=1+O_J(1/k),\qquad B_0>0.                       \tag{NP17}
\]
Indeed the high integral is between1-1/(16pi eta k) and1 times
integral_Y^infinity y^(k-2)e^(-8pi y)dy. This makes the constant1 explicit.

## 6. Entire cross-tail errors and dimension-free elimination

Let u=h-q and v=g_2-q^2 on the high rectangle. NP5 says
|u|<=Ck^2rho^3, |v|<=Ckrho^3. In the P_s integral, the principal term
and the two single-tail terms vanish EXACTLY by Fourier orthogonality.
Only bar(u)v remains. Its absolute integral is at most
Ck^4 A_3^[1]<=Ck^5 A_3.

For the R_s integral subtract the principal term NP15. The three errors
bar(u)q^2, bar(q)v, bar(u)v have bounds after multiplication by |R_s|
respectively Ck^2rho^6, Ckrho^5, Ck^3rho^7.
Thus their integrals are at most C(k^2 A_3+k A_(5/2)+k^3 A_(7/2)).
The low integral of the actual h,g_2 is bounded by
CkY sqrt(M(h;Y)M(g_2;Y)), using NP7.
Every such error is o(A_2), uniformly on J, by NP8. We have proved
\[
 I_s(h,g_2)=B_0+o(A_2)=A_2(1+O_J(1/k)).                 \tag{NP18}
\]
The error is over the entire fundamental domain and entire q tails.

It remains to pay the actual W_3 inverse correction, not just a displayed
2x2 subpanel. For every f in W_3, q and q^2 are exactly x-orthogonal to f
against P_s on the high rectangle. Weighted Cauchy--Schwarz, EP8's
E_fX<=k and NP5 give
\[
 |I_P(h,f;y>=Y)|\le Ck^4\sqrt{A_3G(f)},\qquad
 |I_P(g_2,f;y>=Y)|\le Ck^3\sqrt{A_3G(f)}.
\]
For example the weighted u norm is <=Ck^(5/2)sqrt(A_3), the f norm
is <=sqrt(kG(f)), and the bound |P_s|<=CkX supplies the remaining k.
For R_s use |R_sh|<=6rho^2, |R_sg_2|<=6rho^3 and ordinary
Cauchy--Schwarz; this costs at most Csqrt(A_2G(f)) and Csqrt(A_3G(f)).
The low pieces are <=CkY sqrt(M(h;Y)G(f)) and its g_2 analogue and
are absorbed by NP7. Thus the ACTUAL dual norms satisfy
\[
 \|I_s(h,\cdot)|_{W_3}\|_{G^*}
       \le C(k^4\sqrt{A_3}+\sqrt{A_2}),\qquad
 \|I_s(g_2,\cdot)|_{W_3}\|_{G^*}\le Ck^3\sqrt{A_3}.      \tag{NP19}
\]
These bounds hold simultaneously for ALL f; no dimension factor or
unproved coefficient freedom occurs.

By NP11, the effective cross entry after eliminating W_3 is
\[
 b_k(c)=I_s(h,g_2)-I_s(h,W_3)E_k(c)^{-1}I_s(W_3,g_2),
\]
with correction bounded by
\[
 C(k^6 A_3+k^2\sqrt{A_2A_3})=o(A_2).
\]
The ratio sqrt(A_2A_3)/A_2=(2/3)^((k-1)/2) tends to0 exponentially.
Consequently
\[
 b_k(c)/A_2=1+O_J(1/k),\qquad b_k(c)>0                  \tag{NP20}
\]
for every sufficiently large even k, uniformly on J. This is the crucial
nonzero native cross-period theorem. A merely superpolynomial bound relative
to sqrt(G(h)G_2) would NOT suffice, since that normalization is exponentially
larger than A_2. No nonconstant inner/projection commutation is assumed.

## 7. Verification of the real scalar limit used in section4

NP19 and NP11 bound the g_2 self-Schur correction by Ck^5 A_3=o(A_2).
In the high P_s integral for g_2, x-orthogonality removes the q^2/tail
cross terms. The tail square costs at most Ck^4 A_3. The absolute R_s
integral costs at most CA_(5/2), using |g_2|<=2rho^2.
Low terms are negligible by NP7. Therefore its principal scalar term is
\[
 C(s)A_2^{[s]}+D(s)A_2^{[1-s]},
 \quad A_2^{[\beta]}={\Gamma(k-1+\beta)\over(8\pi)^{k-1+\beta}},
\]
up to o(A_2); truncating the low principal integral has the same negligible
bound. EP26's elementary shrinking-shift Gamma argument, now with8pi rather
than4pi, gives for epsilon=c/k uniformly on fixed real J:
\[
 {A_2^{[\epsilon]}\over A_2}\to1,\qquad
 {A_2^{[1-\epsilon]}\over kA_2}\to{1\over8\pi}.
\]
These follow by integrating psi(x)=log x+O(1/x) over an interval of
length O_J(1/k); no growing-parameter numerical experiment is used.
Combine C=pi/6+O_J(1/k), D=-k/(2c)+O_J(1), NP9 and the paid
self-correction. This proves NP13, without a circular use of its zero.

## 8. Literal noncancellation and residue

Eliminate W_3 in the actual adapted full period matrix. On the real interval
its remaining 2x2 matrix has entries a_k,b_k,d_k and
\[
 Q_k(1-c/k)=a_k(c)-{b_k(c)^2\over d_k(c)},\qquad
 \det I_k=\det E_k\,(a_kd_k-b_k^2),\quad
 \det I_W2=\det E_k\,d_k.                               \tag{NP21}
\]
This identity is meromorphic, not minimization at an indefinite form.
For nonreal c the row/column entries are treated analytically, separately;
the square in NP21 is legitimate on the REAL source interval, where the
real coefficient basis makes the period real symmetric. Explicitly F is
invariant under x->-x, E* is even in x for real s, and every real-q source
form satisfies f(-x+iy)=overline(f(x+iy)). Changing x to -x makes each
period entry equal to its conjugate; the original Hermitian symmetry then
gives real symmetry. The same holds after real W_3 elimination. Analytic
continuation of the real-interval identity justifies meromorphic NP21;
it does not replace analytic cross entries by complex adjoints.

At c=c_{p,k}, NP14 gives a simple d_k zero, E_k is invertible, and
NP20 gives b_k>0. Hence the full numerator determinant equals
-det(E_k)b_k^2!=0. Cancellation is impossible: Q has a SIMPLE POLE.
There are no other denominator zeros on the fixed small disc by section4,
so there is exactly one pole there, with no claim about numerator zeros.

The c-residue is -b_k(c_p)^2/d_k'(c_p).
Since dc/ds=-k, the s-residue is b_k(c_p)^2/[k d_k'(c_p)].
Using NP9, NP14 and NP20 proves NP2, including its positive sign and1152.
Reflection I(s)=I(1-s) transfers the simple pole to the other disc and
reverses its residue sign. The two discs are disjoint for large k.
All native weights, norms, full W_3 coefficients and completion factors
have been retained. This does not assert a new Euler product or RH failure.

## 9. Exact replay, sources and remaining scope

The finite producer checks all-six-class q shears against authenticated AW
functions and independent coefficient recurrences, the vanished q^2 term,
the actual leading q^3 tail coefficients, the exact Cauchy/envelope constants,
low-cutoff exponential majorant, moment/rate algebra, the Fourier n=1 factor,
Bessel convexity polynomials, the deeper complex-disc margin, and the exact
pole-residue scaling1152. It also checks the conditional Schur numerator
identity; that algebra alone is NOT evidence for native noncancellation.

Arithmetic is MIXED with CERTIFIED_INTEGER_COVERAGE and EXACT_RATIONAL.
Strict bool/int/rational types,4096-bit outputs,128-bit rational inputs,
q order<=8, source weight<=2^20, separately capped source work, byte/JSON
caps, literal LF-normalized source/artifact hashes and typed reconstruction
fail closed in normal and -O Python. No special function, period, zero,
Gamma integral, limit or sufficient-weight threshold is numerically sampled
or claimed machine-certified. The analytic proof above requires review.

Primary inputs beyond the source contracts are the classical
[DLMF10.32.8 Bessel integral](https://dlmf.nist.gov/10.32.E8) and
[DLMF10.39.2 half-order formula](https://dlmf.nist.gov/10.39.E2);
NP16 derives the needed uniform inequality directly.
The normal-family/Rouche tools are the same classical inputs as LS, with
their actual fixed-domain hypotheses re-established here.
Remote bytes are not authenticated by this offline replay. No exhaustive
priority or new abstract Bessel, Schur, complex-analysis or automorphic
theory claim is made. Independent frozen-SHA review is required.
