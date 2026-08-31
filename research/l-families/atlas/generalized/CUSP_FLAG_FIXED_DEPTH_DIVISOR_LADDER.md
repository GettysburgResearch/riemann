# Fixed-depth cusp flags: surviving local divisor clusters

Status: PROPOSED SOURCE-SPECIFIC THEOREM; independent frozen-SHA review required.
This is a new packet based on G7ee5e024e1d8c3dd187b40ea5d48f9c9ff46d95e.
No earlier scientific source or programme front is modified.
The result concerns the ACTUAL completed Eisenstein periods, not an abstract
matrix surrogate. RH remains unsolved.

The accepted NP source2f636755ef8605eff725562094017f501fb1db70 proves the
first additional pole pair. The present proof pays the new Fourier-projection
gate for deeper clusters of the ORIGINAL first-coefficient quotient.
Its analytic quantifiers are FIXED DEPTH, then sufficiently large even weight.
There is no effective onset, uniform growing-depth claim, or fixed-weight
global divisor census. Finite arithmetic below does not certify an integral.

## 1. Objects, theorem and the distinction between flag quotients

Retain CF's weight-k cusp space, q coordinate, real integral Miller basis,
completed period I(s), and original Petersson form G. For1<=i<=d set

    W_i={f:[q]f=...=[q^(i-1)]f=0},   D_i(s)=det I(s)|W_i,
    W_(d+1)={0},   D_(d+1)=1,        Q_i(s)=D_i(s)/D_(i+1)(s).

Each determinant uses the corresponding Miller basis. Equivalently Q_i is
canonical on W_i relative to the normalized functional [q^i].
Q_1 is the already reviewed original quotient. Every fixed coefficient flag
has entrywise reflection, so D_i(s)=D_i(1-s) and Q_i(s)=Q_i(1-s).
Changing a flag or using parameter-dependent basis changes is not allowed.

Fix integers J>=1 and1<=i<=J, and a real0<delta<12. There is a NON-EFFECTIVE
k_0(J,delta) such that for every even k>=k_0, d>=J+1 and the following hold.
Write c=k(1-s) and

\[
 A_n(k)={\Gamma(k-1)\over(4\pi n)^{k-1}},\qquad
 F_n(c)={1\over24n}-{1\over2c}.                         \tag{DL1}
\]

Every D_i, i<=J, has exactly one zero counting multiplicity in
|c-12J|<delta. It is real and simple; denote its c-coordinate by c_(i,J).
The deeper determinant D_(J+1) is nonzero there. Moreover

\[
 c_{(i,J)}\longrightarrow12J,\qquad
 c_{(J,J)}<c_{(J-1,J)}<\cdots<c_{(1,J)}.                \tag{DL2}
\]

Consequently Q_J has exactly one simple real zero and no pole in this disc.
For i<J, Q_i has exactly one simple real zero and exactly one simple real
pole in the disc, with NO cancellation. The zero is at c_(i,J), the pole at
c_(i+1,J). In the right s-disc, the zero is strictly to the left of the pole.
Reflection gives the corresponding left clusters and reverses residue signs.

Put S_h=sigma_(-1)(h)=sum_(e|h)1/e for h>=1. At the right pole of Q_i, i<J,

\[
 \operatorname{Res}Q_i
 ={288J^2 S_{J-i}^2 A_J\over k^2}(1+o(1))>0.           \tag{DL3}
\]

The exact Schur identities also resolve the exponentially small separation:

\[
 c_{(i,J)}-c_{(i+1,J)}
 ={288J^2 S_{J-i}^2\over F_i(12J)}
       {A_J\over k^2A_i}(1+o(1)),\qquad
 F_i(12J)={J-i\over24iJ}>0.                            \tag{DL4}
\]

The corresponding positive s-gap (pole minus zero) is DL4 divided by k.
This is an asymptotic with a proved relative error, not subtraction of
numerically located almost-equal zeros.

For the ORIGINAL Q_1 the right-pole constants at J=2,3,4 are respectively
1152,5832,8192 times A_J/k^2. The c-gap constants are
55296,209952,262144 times A_J/(k^2 A_1).
For the ADJACENT Q_(J-1), S_1=1, giving288J^2 A_J/k^2.
These are different quotients and different residue constants.

Only local nested-flag interlacing in DL2 is asserted. For any fixed finite
L, the result implies at least L reflected simple zero pairs and L-1
additional reflected pole pairs for Q_1 at sufficiently large weights,
by using disjoint small discs for J=1,...,L.
It does not imply infinitely many poles for a fixed weight.
A literal uniform ladder up to J=d is excluded: at k=12d,J=d the proposed
center is s=0, where Q_d has the inherited nonzero endpoint pole.

## 2. Fixed partial echelon chart and complete native q tails

Write k=12d+r, r in{0,4,6,8,10,14}, r=4a+6b,0<=a<=2,0<=b<=1.
The native CF forms are

\[
 g_l=\Delta^l E_4^{3(d-l)+a}E_6^b,\quad
 [q^{l+1}]g_l=60k-744l-864b.                            \tag{DL5}
\]

For a FIXED J with d>=J+1 construct h_J=g_J and, descending in l,

\[
 h_l=g_l-\sum_{m=l+1}^J[q^m]g_l\,h_m,\qquad1<=l<J.      \tag{DL6}
\]

Thus [q^m]h_l=delta_(lm) for1<=m<=J.
The basis (h_1,...,h_J,f_(J+1),...,f_d) is a real unit-triangular change
from the Miller basis. Its trailing subbases preserve every W_i with i<=J+1.
No free coefficients are introduced.

Set R=1/(1000k). On the FULL complex q-disc |q|<=R, the convergent products
and series from AW imply

    |g_l/q^l| <= exp{24lR/(1-R)+480p_lR+1008bR}<2,
    p_l=3(d-l)+a,   l<=J<=d,   k>=48.

Indeed24l<=2k and p_l<=k/4, so the exponent is bounded by
[2/(1-R)+120+1008/k]/1000<1/4. This bound is not restricted to real q.
Cauchy's coefficient estimate gives |[q^m]g_l|<=2R^(-(m-l)).
The recursion DL6 therefore proves, on |q|=R,

    |h_l/q^l|<=H_l:=2*3^(J-l).

For rho=|q|<=R/2 its vanished coefficients give the COMPLETE tail estimate

\[
 |h_l-q^l|
 \le 2H_l R^{-(J+1-l)}\rho^{J+1}
 \le B_J k^J\rho^{J+1}.                                \tag{DL7}
\]

Here and below B_J,C_(J,R) denote finite constants depending only on the
fixed displayed parameters; they never depend on d or a vector in a flag.
For example B_J=4*3^(J-1)*1000^J suffices for k>=1.
No finite q-prefix is extrapolated to prove DL7.

On all of the fundamental domain the native bounds
|Delta|<1,|E4|<4,|E6|<16 give |g_l|<=2^(k/2).
Induction in DL6 also gives

\[
 |h_l|\le3^{J-l}R^{-(J-l)}2^{k/2}.                      \tag{DL8}
\]

For that induction, multiply the bound for h_l by R^(J-l)2^(-k/2);
the recurrence is at most1+2 sum_(m>l)3^(J-m)=3^(J-l).

Fix N=J+1, eta=1/(10000N), and Y=eta k. For all sufficiently large k,
Y>=1 and exp(-2pi Y)<=R/2. The global bound DL8, width(F)<=1,
and (k-2)!>=((k-2)/e)^(k-2) imply

\[
 M_l:=\int_{F,y<=Y}y^{k-2}|h_l|^2dxdy
       \le C_J k^{2J}10^{-k} A_N.                      \tag{DL9}
\]

For explicit exponential accounting, after the polynomial factor from DL8,
the factorial ratio is bounded by

    16pi N eta k/(k-1)
      [8pi N e eta k/(k-2)]^(k-2).

Its bracket is at most16pi N e eta<16*4*3/10000<1/10 for k>=4.
All remaining factors are fixed constants and powers of k. The same estimate
bounds each pure q^l low integral for1<=l<=N.
This pays the whole low domain relative to A_N, not to a larger A_1.

For real n>=1,

\[
 A_n^{[1]}=\int_0^\infty y^{k-1}e^{-4\pi n y}dy
 ={k-1\over4\pi n}A_n\le kA_n,\qquad
 A_n/A_m=(m/n)^{k-1}.                                  \tag{DL10}
\]

All errors described as a polynomial times A_N are exponentially smaller
than EVERY A_l with l<=J. Parseval on the high rectangle plus DL7--DL9 gives
G(h_l)=A_l(1+o(1)), uniformly over the finitely many l and six classes.

## 3. The new full-Fourier projection estimate

This section is the gate absent from the unprojected NP norm estimate.
For c in any fixed compact subset of Re(c)>0, s=1-c/k has
3/4<=Re(s)<1 for all sufficiently large k.
The unchanged completed Eisenstein Fourier expansion is

\[
 E^*(z,s)=P_s(y)+{\cal R}_s(z),\quad
 P_s=C(s)y^s+D(s)y^{1-s},
\]
\[
 {\cal R}_s(x+iy)=\sum_{n\ne0}r_{|n|}(s,y)e^{2\pi inx},
\quad r_n=2\sqrt y\,n^{s-1/2}\sigma_{1-2s}(n)
                  K_{s-1/2}(2\pi n y).                \tag{DL11}
\]

The coefficient2 in the two-sided exponential series is the SAME native
coefficient4 in its cosine series, not an altered normalization.
LS's complex-order bound |K_nu(t)|<=K_(Re nu)(t)<=K_(1/2)(t) proves

\[
 |r_n(s,y)|\le n^{\operatorname{Re}s-1}
             \sigma_{1-2\operatorname{Re}s}(n)\rho^n
          \le n\rho^n,\qquad
 |{\cal R}_s|\le2\rho/(1-\rho)^2\le3\rho.               \tag{DL12}
\]

For f in W_N and l<N, write f=sum_(m>=N)a_m q^m.
At each y>=Y, EXACT Fourier orthogonality gives

    integral_x bar(q^l) f R_s
       =sum_(m>=N) a_m rho^(m+l) r_(m-l)(s,y).

By Cauchy--Schwarz and Parseval its absolute value is bounded by

\[
 \left(\sum_{m>=N}(m-l)^2\rho^{2m}\right)^{1/2}
       \|f(\cdot+iy)\|_{L^2_x}
 \le2N\rho^N\|f(\cdot+iy)\|_{L^2_x}.                   \tag{DL13}
\]

To justify the infinite reserve, with x=rho^2<=1/10000 and L=N-l,

    sum_(t>=0)(L+t)^2 x^t
      =L^2/(1-x)+2Lx/(1-x)^2+x(1+x)/(1-x)^3
      <=N^2(1+x)/(1-x)^3<4N^2.

The Fourier and q series converge absolutely on this high rectangle.
Alternatively apply the identities to finite sums and pass by their
dominated L2 limits; no bounded coefficient freedom is assumed.
Integrating DL13 in the ORIGINAL weight y^(k-2) and using Cauchy--Schwarz gives

\[
 |I_{\cal R}(q^l,f;y>=Y)|\le2N\sqrt{A_NG(f)}.           \tag{DL14}
\]

This is projection in the x Fourier coordinate on the high rectangle,
not a claimed commutation of an operator with a global Petersson projection.
For complex s the two cross directions are bounded separately; conjugation
replaces s by bar(s), within the same compact family.

The naive unprojected q-to-deep estimate would leave
sqrt(A_2 A_4)/A_3=(9/8)^((k-1)/2) at J=3. DL14 removes that loss.
It cannot be replaced by a generic norm estimate for R_s q.

## 4. Complete cross functionals and the actual deep inverse

Let X=max(1,y). The imported EP moment bound, valid for EVERY f beginning
at q^n, is

    integral_F X y^(k-2)|f|^2 <=[1+(k-1)/(4pi n)]G(f).

The complex-power estimate LS5 and Laurent/Taylor expansions give
|P_s|<=C kX on the fixed real compact c interval used for detailed estimates;
the full LS absolute form bound is available on each fixed complex compact.
On the high rectangle, the P_s cross of q^l and f in W_N vanishes exactly.
For u_l=h_l-q^l, DL7 and the moment bound give

    |I_P(u_l,f;high)|<=C_J k^(J+2) sqrt(A_N G(f)).

Here the modular moment bound is used ONLY for f. For the nonmodular
tail u_l, DL7 directly gives
integral_high X y^(k-2)|u_l|^2<=B_J^2 k^(2J)(A_N+A_N^[1]).

For the remainder use DL14 for q^l and
|R_s u_l|<=3B_J k^J rho^(N+1) for its entire tail.
The low piece is <=CkY sqrt(M_l G(f)), absorbed by DL9.
It follows, simultaneously for ALL f in W_N, that

\[
 \|I_s(h_l,\cdot)|W_N\|_{G^*}
     \le C_J k^{J+2}\sqrt{A_N},\qquad1<=l<=J.           \tag{DL15}
\]

The same bounds hold uniformly on fixed complex c discs: there
|P_s|<=C kX still holds since Re(s),Re(1-s) lie in[0,1],
and the complex bounds DL12--DL14 apply. No coordinate or dimension factor
has been hidden in DL15.

Fix0<R<12 and Omega_R={|c-12J|<R}. Whenever uniform convergence on its
closed disc is used below, run the same estimates first on a larger FIXED
disc Omega_(R') with R<R'<12. Local uniform convergence there is uniform
on the closed radius-R disc. This fixed buffer also supplies its boundary
inverse estimates; no k-dependent domain is used.
The all-W_N moment estimate and
LS's complex-power proof imply

\[
 \operatorname{Re}{I_{1-c/k}(f,f)\over G(f)}
 \le {k\over24N}-k\operatorname{Re}{1\over2c}
                   +O_{J,R}(\log k).
\]

The exact reserve is

\[
 \operatorname{Re}{1\over2c}-{1\over24N}
 ={(6N)^2-|c-6N|^2\over24N|c|^2}
 \ge{(6N)^2-[6(J-1)+R]^2\over24N(12J+R)^2}>0.          \tag{DL16}
\]

Thus E=I|W_N is holomorphic and invertible on the SAME closed disc for every
sufficiently large k; the poles c=0,k lie outside. In the original Petersson
metric its inverse norm is O_(J,R)(1/k), from negative Hermitian PART.
No normal-matrix or eigenvalue-only inference is used.

Eliminate the whole W_N and call the remaining J-by-J analytic matrix H.
The source basis is the one in DL6, and row/column directions remain separate.
DL15 bounds EVERY entry of the deep correction by

\[
 C_{J,R} k^{2J+3}A_N.                                  \tag{DL17}
\]

The indefinite deep block is not discarded; this is its complete correction.

## 5. Surviving actual arithmetic cross coefficients

For l<m<=J put h=m-l. The pure q^l-to-q^m cross against P_s vanishes.
Against R_s, only mode h occurs. Its exact integral is

\[
 B_{lm}=2h^{s-1/2}\sigma_{1-2s}(h)
     \int_Y^\infty y^{k-3/2}e^{-2\pi(l+m)y}
                         K_{s-1/2}(2\pi h y)\,dy.      \tag{DL18}
\]

For real c in the fixed interval and nu=s-1/2, NP's primary
Gamma-integral inequality gives
1-1/(8x)<=K_nu(x)/K_(1/2)(x)<=1.
Using K_(1/2)(2pi h y)=e^(-2pi h y)/(2sqrt(hy)), the exact coefficient
after this substitution is h^(s-1)sigma_(1-2s)(h), and the decay is
exp(-4pi m y). Therefore

\[
 B_{lm}/A_m=S_{m-l}(1+O_{J,R}(1/k))>0.                 \tag{DL19}
\]

Here h is fixed, so the finite divisor sum has its ordinary uniform Taylor
bound. The discarded low pure integral is controlled by DL9.
For complex c, the upper bound |B_lm|<=h A_m suffices.

All remaining cross-tail terms are small in the CORRECT A_m normalization.
For each single R_s tail, apply DL13 to the tail, whose first order is N:
its integrated bound is C_J k^J A_N. The double-tail bound follows from
|R_s|<=3rho and DL7. The P_s single tails vanish exactly; the double tail
is <=C_J k^(2J+2)A_N. The complete low-domain term is paid by DL9.
DL13 uses only Fourier support and Parseval, so it applies to the
nonmodular u_l on the high rectangle with its directly bounded high norm.
No modular all-vector moment estimate is asserted for u_l.
For diagonal entries the pure R_s term vanishes because its mean is zero;
the same projected single-tail estimates apply.

Together with DL17 these prove, uniformly on the fixed complex disc,

\[
 H_{ll}=T_l(c)+O_{J,R}(k^{2J+3}A_N),\quad
 T_l=C(s){\Gamma(k-1+s)\over(4\pi l)^{k-1+s}}
      +D(s){\Gamma(k-s)\over(4\pi l)^{k-s}},             \tag{DL20}
\]
\[
 |H_{lm}|\le C_{J,R}A_{\max(l,m)}\quad(l\ne m),         \tag{DL21}
\]

for sufficiently large k. On the real interval the sharper conclusion is

\[
 H_{lm}/A_m=S_{m-l}(1+O_{J,R}(1/k)),\quad l<m.           \tag{DL22}
\]

The terms polynomial(k) A_N/A_m decay exponentially, which justifies
absorbing them into O(1/k). This is the actual arithmetic off-diagonal,
not a generic Schur control or a leading finite-prefix fit.

The shrinking-shift Gamma calculation from EP/NP gives
T_l/(kA_l)->F_l(c) uniformly on real compact subintervals.
For completeness this follows from psi(x)=log x+O(1/x),
C(1-c/k)=pi/6+O(1/k), D(1-c/k)=-k/(2c)+O(1):
A_l^[c/k]/A_l->1 and A_l^[1-c/k]/(kA_l)->1/(4pi l).
Complex local boundedness follows from LS's absolute form bound and
G(h_l)/A_l->1, together with DL17.
The fixed-domain normal-family/identity argument in LS then gives

\[
 H_{ll}/(kA_l)\longrightarrow F_l(c)                   \tag{DL23}
\]

locally uniformly on Omega_R, also for derivatives by Cauchy.
This imports no real inequality as a complex inequality.

## 6. Earlier finite-block elimination without exponential norm loss

Let M be any subset of{1,...,J-1}; it will be an interval below.
Set A_M=diag(A_m:m in M) and C_M=H_MM A_M^(-1).
DL21--DL23 give

    C_M/k -> diag(F_m(c):m in M)

locally uniformly on Omega_R. Indeed H_lm/A_m=O(1) if l<m,
and is O(A_l/A_m)<=O(1) if l>m. Each F_m is nonzero there:
its zero12m is at least12 from12J and its pole0 is outside.
Hence H_MM is invertible for sufficiently large k and

\[
 H_{MM}^{-1}=A_M^{-1}C_M^{-1},\qquad
 \|C_M^{-1}\|=O_{J,R}(1/k).                             \tag{DL24}
\]

This COLUMN scaling is load-bearing. A coarse Petersson-normalized
Cauchy estimate between unequal earlier A_m scales could lose an
exponential factor and does not replace DL24.

For i<J eliminate M={i+1,...,J-1}, in addition to the already eliminated
deep space. The remaining block on(h_i,h_J) is written

    [[a_i,b_i],[tilde_b_i,d_i]].

The two crosses are analytic separately; on the real interval they agree
and are real, by x->-x and the real q coefficients exactly as in NP.
DL21--DL24 show, on the real interval near12J,

\[
 a_i/(kA_i)\to F_i(c),\qquad
 b_i/A_J=S_{J-i}(1+O(1/k)),\qquad
 d_i/(kA_J)\to F_J(c).                                 \tag{DL25}
\]

To see the cross estimate explicitly, H_iM A_M^(-1)=O(1) entrywise,
C_M^(-1)=O(1/k), and H_MJ=O(A_J), so its correction is O(A_J/k).
The a_i correction is O(A_(i+1)/k), and the d_i correction is at most
C A_J^2/(k A_(J-1)); empty M has zero correction.
These estimates incur only fixed J factors, not growing dimension.
The d_i convergence is locally uniform COMPLEX and hence holds for its
derivative. The same argument applies to the scalar obtained by eliminating
{i,...,J-1} and retaining h_J.

## 7. Actual determinant zeros, noncancellation and exponentially close gaps

For each i<=J let delta_i be that last scalar, with M={i,...,J-1}.
Then the exact determinant identity is

    D_i=det(E) det(H_MM) delta_i,

with the empty determinant equal to1. All displayed prefactors are nonzero
on the fixed disc, and delta_i/(kA_J)->F_J locally uniformly there.
Given delta<R<12, Rouche on |c-12J|=delta gives exactly one zero
counting multiplicity, since F_J=(c-12J)/(24Jc).
Conjugation makes it real, and it is simple. This proves the individual
D_i zero assertions and c_(i,J)->12J. It also gives, uniformly in a fixed
small real neighborhood of12J,

\[
 \delta_i'(c)/(kA_J)\to F_J'(c),\qquad
 F_J'(12J)=1/(288J^2)>0.                               \tag{DL26}
\]

For i<J, d_i in DL25 is delta_(i+1), and the full source Schur identity is

\[
 Q_i=a_i-{b_i^2\over d_i},\qquad
 \delta_i=d_i-{b_i^2\over a_i}.                        \tag{DL27}
\]

These identities hold on the real interval and continue meromorphically;
a complex adjoint is never inserted. Since F_i(12J)>0, a_i>0 near the
roots for all sufficiently large k. Also b_i>0 there by DL25.
At d_i=0 the numerator a_i d_i-b_i^2 is strictly nonzero.
Thus Q_i has a genuine simple pole, while its distinct numerator root
is the simple D_i zero. This proves the precise zero/pole count in the
disc, not just the existence of a denominator root.

At c=c_(i,J), the second identity in DL27 gives
d_i(c)=b_i(c)^2/a_i(c)>0; at c=c_(i+1,J), d_i=0.
DL26 makes d_i' positive between these nearby real points.
The mean-value theorem proves their strict order and the EXACT relation

    c_(i,J)-c_(i+1,J)
      = b_i(c_(i,J))^2 / [a_i(c_(i,J))*d_i'(xi_k)]

for a point xi_k between them. Inserting DL25--DL26 proves DL4 with
relative error1+o(1), despite its exponential size. No inaccurate
subtraction of two coarse asymptotic root locations is used.

Finally the c-residue of Q_i is -b_i^2/d_i'; since dc/ds=-k, its
s-residue is b_i^2/(k d_i')>0. This proves DL3 and its reflection sign.
The case i=J uses Q_J=H_JJ and the already nonzero deep denominator.
All local statements hold simultaneously for fixed finitely many i,J
and all six residue classes by taking the maximum of finitely many thresholds.

## 8. Finite controls and sharp scope boundary

The producer retains the source's exact coefficient chart and tests partial
echelon lifts, complete bounded q prefixes, the projection geometric-series
reserve, the full-tail exponential scales, fixed-disc coercivity identities,
column-scaled Schur algebra, and the residue/gap constants.
It binds primitive source blobs, artifact hashes, and the complete fixture.
Strict integer/rational types, charged finite work, input/output bit limits,
JSON coverage/caps and full typed reconstruction must fail closed under -O.

No machine control proves the analytic integral estimates, all-weight limits,
normal-family convergence, or a sufficient onset. Those are written proofs
requiring separate scientific review. No floating determinant is certified.
In particular, the ledger's finite test weight65536 evaluates rational
constants only: it does NOT certify the eventual conditions Y>=1 and
exp(-2pi Y)<=1/(2000k), and is not an analytic onset.

The direct primary Bessel inputs remain
[DLMF10.32.8](https://dlmf.nist.gov/10.32.E8),
[DLMF10.32.9](https://dlmf.nist.gov/10.32.E9), and
[DLMF10.39.2](https://dlmf.nist.gov/10.39.E2), in their stated domains.
The Miller basis, Eisenstein period and completion are classical source
imports from the frozen CF/NP lineage, not new automorphic constructions.
Remote reference bytes are not authenticated by an offline source hash.

The first missing uniform extension is quantitative control as J grows
with k; constants, cutoff and coercivity reserves here depend on FIXED J.
The result supplies no critical-line theorem, RH consequence, fixed-weight
infinite pole count, global interlacing, unsigned global divisor asymptotic,
or new Euler product. It does not change any earlier effective threshold.
