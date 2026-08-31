# Canonical cusp quotient: a locally unique simple endpoint zero

Status: PROPOSED SOURCE-SPECIFIC THEOREM; independent frozen-SHA review required.
Exactly five new files, no changes to frozen AW/EP/UQ/CF sources.
The new conclusion is LOCAL uniqueness and simplicity, with a NON-EFFECTIVE
sufficient-weight threshold. It is not a global zero census or an RH claim.

The complete AW source at98b4058ac29ba88cf993d7a3ce67579fab0c7844 and complete
EP source at27496745df9dd49fcde17699d333a54cf8620772 are pinned as ten literal
Git blobs. AW supplies the actual all-six-class quotient and REAL asymptotic.
The new complex estimates below are proved directly, not inferred by analytic
continuation of pointwise real inequalities.

## 1. Precise shrinking-disc theorem

Use AW's actual weight-k source for every sufficiently large EVEN k:
k=12d+r, r in{0,4,6,8,10,14}, h_k=Delta E4^(3d-3+a)E6^b, ell=[q],
W=ker ell, and Q_k(s)=det I_k(s)/det I_W(s). In particular k mod12=2
uses r14, not r2. Let G be the original Petersson form and G_h=G(h_k)>0.
For each fixed real delta with0<delta<12, there is k_0(delta) such that
for EVERY even k>=k_0(delta), Q_k has exactly ONE zero COUNTING MULTIPLICITY
in each of the discs
\[
 \left|s-\left(1-\frac{12}{k}\right)\right|<\frac{\delta}{k},
 \qquad
 \left|s-\frac{12}{k}\right|<\frac{\delta}{k}.             \tag{LS1}
\]
There are no denominator zeros in these discs for such k.
The zeros form a reflected pair, are REAL and SIMPLE, and are uncancelled.
At them the full period matrix has corank one with ell nonzero on its kernel.

Their real location is the already source-bound AW expansion
\[
 1-s_k=\frac{12}{k}+\frac{288\log k+O(1)}{k^2},
\]
\[
 k(1-s_k)=12+\frac{288L_k-288C_{12}}{k}
                 +O(\log^2k/k^2),\quad
 L_k=\log(k/(4\pi)),\quad
 C_{12}=\frac{\gamma-\log(4\pi)}2-\frac1{24}
                       -\frac{6\Lambda'(2)}\pi.         \tag{LS2}
\]
Constants and thresholds are uniform across the six classes.
The new k_0(delta) is NOT computed and is NOT asserted equal to65536 or6144.
There is no complex error-rate claim, no global uniqueness, no uniqueness
on the entire open chamber uniformly up to its boundary, and no exclusion
of additional zeros escaping toward that boundary or other scales.
Delta is fixed; it may not vary with k in this theorem.

## 2. Scaled chamber and the required native moment estimate

Put c=k(1-s) and
\[
 \mathcal D=\{|c-12|<12\},\qquad
 \Omega_R=\{|c-12|<R\},\quad0<R<12.
\]
We work uniformly on the CLOSED disc |c-12|<=R for sufficiently large k.
There Re(c)>0, |c|<=12+R, |c|>=12-R, and the exact identity is
\[
 \operatorname{Re}\frac1{2c}-\frac1{48}
 =\frac{144-|c-12|^2}{48|c|^2}
 \ge m_R:=\frac{12-R}{48(12+R)}>0.                       \tag{LS3}
\]
No boundary point c=0 or point on |c-12|=12 is included.

For a nonzero cusp form f, let dmu_f=y^(k-2)|f|^2 dxdy/G(f)
on the standard domain F, a=sqrt(3)/2<=y, and X=max(1,y).
The source Parseval bound EP8, valid for every form starting at q^N, gives
\[
 {\mathbb E}_f X\le1+\frac{k-1}{4\pi N}\le k.             \tag{LS4}
\]
N=2 applies uniformly to ALL W; N=1 applies to the full cusp space.
For epsilon=c/k, prove uniformly in f and c on the fixed disc:
\[
 {\mathbb E}_f|y^\epsilon-1|
       =O_R(\log k/k),\qquad
 {\mathbb E}_f |y^\epsilon|=O_R(1).                      \tag{LS5}
\]
Positive real logarithms define y^epsilon throughout.

Here is a direct proof. Below y=1, |log y| is bounded since y>=a, so
|y^epsilon-1|<=|epsilon||log y|exp(|epsilon||log y|)=O_R(1/k).
For y>=1,
|y^epsilon-1|<=|epsilon| log(y)y^(Re epsilon).
Set alpha=1/log k and beta=Re epsilon+alpha. For large k,0<beta<1.
Since log y<=y^alpha/alpha, concavity and LS4 give
\[
 {\mathbb E}_f[{\bf1}_{y\ge1}\log(y)y^{\operatorname{Re}\epsilon}]
 \le\log k\,{\mathbb E}_f X^\beta
 \le\log k\,k^\beta
 =\log k\,\exp(1+\operatorname{Re}(c)\log k/k)
 =O_R(\log k).                                         \tag{LS6}
\]
Multiplication by |epsilon|=O_R(1/k) proves the first assertion.
For the second, y^(Re epsilon)<=X^(Re epsilon), and the same Jensen
bound gives expectation<=k^(Re epsilon)=O_R(1).
These estimates cover the whole actual probability measure, including
the part below y=1, and incur no dimension or basis-coordinate factor.

## 3. Complex Eisenstein remainder, not a real-only bound

The unchanged half-lattice Fourier expansion, with its native coefficient
4sqrt(y), is
\[
 E^*(z,s)=C(s)y^s+D(s)y^{1-s}+\mathcal R_s(z),
 \quad C(s)=\Lambda(2s),\quad D(s)=\Lambda(2s-1).          \tag{LS7}
\]
For c on the fixed disc and large k,3/4<=Re(s)<1.
The classical positive-real Bessel argument remains valid for COMPLEX order:
\[
 |K_\nu(t)|
 \le\int_0^\infty e^{-t\cosh u}|\cosh(\nu u)|du
 \le K_{\operatorname{Re}\nu}(t)\le K_{1/2}(t),
 \quad0\le\operatorname{Re}\nu\le1/2,\ t>0.              \tag{LS8}
\]
Indeed |cosh(x+iy)|^2=cosh^2x-sin^2y<=cosh^2x.
Take nu=s-1/2. Also
|sigma_(1-2s)(n)|<=sigma_(1-2Re(s))(n)<=tau(n)<=n
and |n^(s-1)|<=1. The exact EP7 bound therefore persists:
\[
 |\mathcal R_s(z)|\le\frac{2\rho}{(1-\rho)^2}<1,
 \quad\rho=e^{-2\pi y}<1/100.                            \tag{LS9}
\]
Absolute Bessel/divisor domination gives local normal convergence in these
complex parameter regions. Thus the source meromorphic Fourier identity is
legitimately continued here; no real-parameter inequality was analytically
continued as an inequality.

The regular Taylor expansion at2 and Laurent expansion at1 give uniformly
\[
 C(1-c/k)=\pi/6+O_R(1/k),\qquad
 D(1-c/k)=-k/(2c)+O_R(1).                               \tag{LS10}
\]
The parameters c are bounded and bounded away from0. The constants may depend
on R. No effective remainder constant is required or claimed.

## 4. The actual complex W block is invertible

For every nonzero f in W use LS7--LS10 and LS5. Since Re epsilon>0,
y^(1-Re epsilon)<=X. Hence
\[
 \operatorname{Re}\frac{I_{1-c/k}(f,f)}{G(f)}
 \le(\pi/6+O_R(1/k))
       \left(1+\frac{k-1}{8\pi}\right)
       -k\operatorname{Re}\frac1{2c}+O_R(\log k)
\]
\[
 \le-km_R+O_R(\log k)\le-\kappa_R k,
 \qquad\kappa_R=m_R/2>0                                \tag{LS11}
\]
for all sufficiently large k, uniformly over the closed disc and ALL W.
The O(log k) term includes D times the LS5 difference
E_f(y^epsilon)-1; this term may not be silently discarded.

Let D_k(c)=I_W(1-c/k) and whiten with the constant positive Petersson Gram:
J_k(c)=G_W^(-1/2)D_k(c)G_W^(-1/2).
LS11 says its HERMITIAN PART satisfies
\[
 \operatorname{Re}(v^*J_k(c)v)\le-\kappa_R k\|v\|^2.
\]
At nonreal c, J_k is NOT asserted Hermitian or normal. Cauchy--Schwarz yields
\[
 \|J_k(c)v\|\|v\|\ge|v^*J_k(c)v|
 \ge\kappa_R k\|v\|^2.
\]
The finite square matrix is therefore invertible, with
\[
 \|J_k(c)^{-1}\|\le1/(\kappa_R k).                       \tag{LS12}
\]
This is the needed singular-value/inverse estimate in the source metric,
not an eigenvalue calculation or a Hermitian replacement of the source.

For k>24, the entry poles at s=0,1 correspond to c=k,0, outside the disc.
The entries are holomorphic there, and denominator nonvanishing now makes
the ACTUAL quotient Q_k(1-c/k) holomorphic throughout Omega_R.

## 5. Full-space absolute-form bound and locally bounded quotient

For any nonzero f in the full cusp space, LS4 with N=1 and LS5 give
\[
 \int_F |E^*(z,1-c/k)|y^{k-2}|f|^2dxdy
 \le C_R kG(f).                                        \tag{LS13}
\]
Indeed the C term uses E_f X=O(k), the D term uses
|D|=O_R(k) and E_f y^(Re epsilon)=O_R(1), and LS9 bounds the remainder.
Weighted Cauchy--Schwarz consequently gives, for ALL source vectors u,v,
\[
 |I_{1-c/k}(u,v)|\le C_R k\sqrt{G(u)G(v)}.               \tag{LS14}
\]
Neither positivity of E* nor Hermitian symmetry of I at complex s is used.

In the fixed adapted basis (h_k,f_2,...,f_d), write the genuine block matrix
\[
 I=\begin{pmatrix}a&r\\t&D_k\end{pmatrix},
 \qquad Q_k=a-rD_k^{-1}t.                               \tag{LS15}
\]
The two off-diagonal blocks r,t are estimated separately; replacing one by
the adjoint of the other would generally change this analytic matrix.
By LS14,
|a|<=C_R kG_h,
||rG_W^(-1/2)||<=C_R k sqrt(G_h), and
||G_W^(-1/2)t||<=C_R k sqrt(G_h).
Together with LS12,
\[
 |Q_k(1-c/k)|\le(C_R+C_R^2/\kappa_R)kG_h.                \tag{LS16}
\]
This is an ABSOLUTE bound, not a positive Schur correction and not a claim
that the complex correction is small. It suffices for the next step.

## 6. Normal-family convergence with the native hypotheses proved

Define the holomorphic scalar
Phi_k(c)=Q_k(1-c/k)/(kG_h) on Omega_R for all sufficiently large even k.
LS16 makes this family uniformly bounded, independently of dimension.
For every real c in(12-R,12+R), AW4 gives
\[
 \Phi_k(c)\longrightarrow F(c):=\frac1{24}-\frac1{2c}
                              =\frac{c-12}{24c}.       \tag{LS17}
\]
This convergence is along ALL even weights, not merely one residue subsequence.

For completeness the classical Montel/identity argument is as follows.
Uniform local bounds and Cauchy's derivative estimate give equicontinuity
on every compact subset of Omega_R. Arzela--Ascoli and a diagonal compact
exhaustion give a locally uniformly convergent subsequence from any sequence
of the Phi_k. Its limit is holomorphic by the Cauchy integral formula.
LS17 identifies it with F on a real interval; the holomorphic identity theorem
identifies it with F throughout connected Omega_R. Thus EVERY subsequential
limit is F. If the full sequence did not converge uniformly on some compact
set, a subsequence separated there by a fixed positive error would have a
convergent subsubsequence, a contradiction. Therefore
\[
 \Phi_k\longrightarrow F
 \quad\hbox{locally uniformly on }\Omega_R.              \tag{LS18}
\]
Only finitely many initial k were discarded; their possible denominator
behavior is irrelevant to this eventual family. This supplies all the
normal-family hypotheses; it is not a bare appeal to real analytic continuation.
No numerical or effective rate of complex convergence is asserted.

## 7. Rouche, conjugation, simplicity and the reflected disc

Given fixed0<delta<12 choose delta<R<12. On |c-12|=delta,
\[
 |F(c)|=\frac{\delta}{24|c|}
             \ge\frac{\delta}{24(12+\delta)}>0.         \tag{LS19}
\]
LS18 makes |Phi_k-F| smaller than this constant on that circle for every
sufficiently large even k. Both functions are holomorphic on a neighborhood
of its closed interior by LS12 and the choice R>delta.
Rouche's theorem gives exactly ONE zero COUNTING MULTIPLICITY in the disc,
since F has its single simple zero at12 and its pole0 is outside.
In particular the actual quotient zero is simple, and none lies on the circle.

Conjugation is legitimate for the source: E*(z,bar s)=overline(E*(z,s))
and the original sesquilinear period imply
\[
 I(\bar s)=I(s)^*,\qquad I_W(\bar s)=I_W(s)^*,\qquad
 Q_k(\bar s)=\overline{Q_k(s)}.                          \tag{LS20}
\]
Taking determinants removes the transpose in the adjoint; I(s) itself
need not be Hermitian. The c disc is conjugation-invariant, so a nonreal zero
would have a distinct conjugate zero in it. The unique zero is therefore real.

Its affine s-image is the first disc in LS1. CF reflection Q_k(s)=Q_k(1-s)
transfers simplicity and uniqueness to the second disc, including denominator
nonvanishing. For sufficiently large k these discs are disjoint and lie on
opposite sides of1/2. Nonzero det I_W makes the zero uncancelled; block
elimination gives full corank one and ell nonzero on the nullvector.
Once reality is established, AW6 applies on the fixed real compact c interval
and supplies LS2. There is no need to rederive a complex fine expansion.

The theorem says exactly one in EACH FIXED shrinking disc eventually.
It does not say there is only one zero in the full moving chamber, because
its sufficiently-large threshold may depend on delta or a chosen compact set.

## 8. Exact controls, primary inputs and exclusions

The producer checks the Gaussian-rational identity LS3 at interior, boundary
and exterior control points, the exact radius lower bounds LS3/LS19, and
the k-power accounting in LS16. It replays native six-class source prefixes
from authenticated AW, not sampled analytic periods or zeros.

Two explicit NONNATIVE orientation controls guard the argument:
D=-1+i, b=1+i, a=0 in a symmetric2x2 block gives
Q-a=-b^2/D=-1+i, whereas the false conjugated product gives1+i.
Thus a negative real part of D does not make the complex Schur correction
nonnegative. A nonnormal symmetric block
D=[[-2,i],[i,-1]] has Hermitian part diag(-2,-1);
D^*D-Id=[[4,-i],[i,1]] has positive principal minors4 and3.
These exact examples check orientation/inverse reasoning only. They are NOT
claimed to be actual cusp matrices or counterexamples to any native theorem.

Arithmetic taxonomy is MIXED with CERTIFIED_INTEGER_COVERAGE and EXACT_RATIONAL.
Gaussian rationals are pairs of exact Fractions, not floating complex numbers.
All arithmetic outputs have4096-bit caps; point/radius rational inputs have
128-bit caps; finite matrix size<=2, q order<=8, local work<=2,000,000, source
work separately capped, and JSON/source bytes<=2,000,000 with<=20,000 JSON nodes.
Strict types, LF-normalized literal source/artifact hashes, payload seal and
complete reconstruction fail closed in normal and -O Python.
No machine claim certifies Montel, Rouche, analytic integrals or an onset.

The Bessel inequalities use the same primary
[DLMF10.32.9](https://dlmf.nist.gov/10.32.E9) and
[DLMF10.39.2](https://dlmf.nist.gov/10.39.E2) as UQ, with the complex-order
modulus step proved in LS8. The classical normal-family and zero-count inputs
are [Tao, Math246A Notes4, Exercise58(i) and Theorem37](https://terrytao.wordpress.com/2016/10/11/math-246a-notes-4-singularities-of-holomorphic-functions/).
LS18 writes out the needed normal-family argument. No new abstract complex
analysis theorem or exhaustive priority claim is made. Remote bytes are not
authenticated by the offline replay.

There is no global uniqueness, effective simplicity threshold, new automorphic
family, zeta/RH counterexample, critical-line theorem, or boundary-uniform claim.
Replay requires normal/-O tests and checks, all four exact LF emission checks,
Ruff, full authoring-base whitespace checks and fresh frozen-SHA verification.
Independent scientific review is required before acceptance.
