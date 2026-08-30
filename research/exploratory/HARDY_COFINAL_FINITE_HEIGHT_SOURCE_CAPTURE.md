# Hardy cofinal finite-height source capture

Status: NEW BOUNDED-SCOPE ANALYTIC RESULT; independent frozen-SHA review required.
Scope: a pure-Blaschke denominator of finite total zero height, possibly infinite;
any upper-half-plane inner numerator; the existing physical band projector and
corrected adjoint source. No actual-Xi finite-height or cofinal-capture claim.
RH remains unsolved.

Arithmetic: MIXED, with EXACT_RATIONAL and CERTIFIED_INTEGER_COVERAGE components.
Finite controls use exact rational/Gaussian arithmetic with no rounding.
They do not machine-prove the analytic limits below. Nine typed primitive
source/review bindings are pinned in the adjacent manifest.

## 1. The theorem and the precise operator being captured

Use the unitary Hardy Fourier convention
\[
 F(x)=(2\pi)^{-1/2}\int_0^\infty f(t)e^{ixt}\,dt.
\]
All projectors below act in this same physical Fourier realization.
Let \(B\) be a finite or infinite PURE Blaschke product, with zeros
\(b_j=a_j+iy_j\), \(y_j>0\), counted with multiplicity, and assume
\[
 S=\sum_j y_j<\infty.                                      \tag{HC1}
\]
There is NO denominator singular inner factor, including at infinity.
A constant denominator is allowed and has zero model space.
Let \(U\) be ANY inner function, including infinite Blaschke or singular
inner factors, and put
\[
 M=K_B=H^2\ominus BH^2,\quad P_M=P_{K_B},\quad
 P_U=P_{UH^2}=M_U M_U^*.
\]
For \(L>0\) and any measurable \(I\subset[0,L]\), define
\[
 T_I(B,U)=\|\Pi_I M_U P_M\|_{\mathcal S_2}^2,\qquad
 C_I(B,U)=\|\Pi_I P_U P_M\|_{\mathcal S_2}^2.                \tag{HC2}
\]
These are nonnegative extended traces before the theorem is applied.
They are different operators: the second is the corrected physical source
projection, not just inner multiplication of the denominator frame.

**Theorem.**
\[
 \boxed{0\le C_I(B,U)\le T_I(B,U)\le2LS<\infty.}             \tag{HC3}
\]
For \(U=1\), the sharper bound \(T_I(B,1)\le2|I|S\) also holds.
No bound with \(2|I|S\) is asserted for general \(U\).

If finite Blaschke divisors \(B_m\mid B_{m+1}\mid B\) exhaust the entire
zero divisor with its multiplicities, then
\[
 \boxed{C_I(B_m,U)\uparrow C_I(B,U),\qquad
        T_I(B_m,U)\uparrow T_I(B,U).}                       \tag{HC4}
\]
The physical trace also equals
\[
 C_I(B,U)=\operatorname{tr}
       (\Pi_I P_U P_M P_U\Pi_I).                           \tag{HC5}
\]
The numerator \(U\) and the physical projector are fixed throughout this
exhaustion. Varying approximating numerators needs separate control.

Geographic disk exhaustion is a special case ONLY when every closed
geographic disk contains finitely many denominator zeros. This is true
for a nonzero entire source divisor, but not for every Blaschke sequence
(which may accumulate at the real boundary in a bounded disk).
Otherwise (HC4) uses finite divisor exhaustion, not an invented disk census.

The theorem is a LOW-PASS bound: its cost is the upper frequency endpoint
\(L\), not the shrinking width \(|I|\). It proves nonquantitative capture
at each fixed configuration. It does not give uniform-in-physical-height
capture, a bound for total charge, or a source-relative suppression factor.

## 2. Finite origin-height identity and causality

For a finite denominator use the row basis
\(w(t)=(t^r e^{-(y_j+ia_j)t}/r!)_{0\le r<q_j}\), and write
\(G=\int_0^\infty w^*w\,dt\), \(w'=wA\), \(c=w(0)\).
The diagonal blocks of \(A\) have eigenvalue \(-y_j-ia_j\).
Integration by parts gives
\[
 A^*G+GA=-c^*c.
\]
Hence the evaluation-kernel diagonal \(k_M(t)=w(t)G^{-1}w(t)^*\) obeys
\[
 k_M'(t)=-|w(t)G^{-1}c^*|^2\le0,\qquad
 k_M(0)=-\operatorname{tr}(A+A^*)=2\sum_jq_jy_j.            \tag{HC6}
\]
The trace equality follows by multiplying the Lyapunov identity by
\(G^{-1}\). These are the finite identities HT5--HT6, with all phases and
multiplicities retained. Thus
\[
 \operatorname{tr}(P_M\Pi_{[0,L]}P_M)
   =\int_0^L k_M(t)\,dt\le2LS.                            \tag{HC7}
\]

The causal property of a Hardy inner multiplier is
\[
 \Pi_{[0,L]}M_U=\Pi_{[0,L]}M_U\Pi_{[0,L]}.                  \tag{HC8}
\]
Indeed a waveform supported in \([L,\infty)\) has Hardy transform
\(e^{iLz}F(z)\); multiplying by \(U\) leaves that delay factor in place.
Consequently, since \(M_U\) is an isometry,
\[
 \|\Pi_I M_U f\|_2
 \le\|\Pi_{[0,L]}M_U\Pi_{[0,L]}f\|_2
 \le\|\Pi_{[0,L]}f\|_2.
\]
Summing over an orthonormal denominator basis proves the finite version of
\(T_I\le2LS\). Equation (HC8) is a triangular causal identity, NOT the false
commutation \(\Pi_I M_U=M_U\Pi_I\), and it is not an identity for \(P_U\).

Model spaces are coinvariant under multiplier adjoints:
\(M_U^*K_B\subset K_B\). To check this, pair \(M_U^*f\) with \(Bh\);
the result is the pairing of \(f\) with \(BUh\), which is zero.
Thus \(A_U=M_U^*|_M\) is a contraction and
\[
 \Pi_I P_U|_M=(\Pi_I M_U|_M)A_U .
\]
The Hilbert--Schmidt ideal inequality proves \(C_I\le T_I\), for finite
or infinite \(M\) as soon as the latter operator is Hilbert--Schmidt.

## 3. Infinite denominator and the literal finite source interface

The spaces \(K_{B_m}\) increase. Their union is dense in \(K_B\):
a Hardy function in every \(B_mH^2\) has an inner zero divisor containing
every zero of \(B\), so is divisible by the pure Blaschke factor \(B\).
This uses no approximation-zero ledger. In particular
\(P_{K_{B_m}}\to P_M\) strongly.

Extend compatible orthonormal bases along this increasing sequence.
The squared norms of their images under each fixed bounded operator
\(\Pi_I M_U\) or \(\Pi_I P_U\) form a nonnegative series. Its finite
partial sums are the corresponding finite traces. Since \(S_m\le S\),
the finite bound \(2LS_m\) proves convergence, (HC3), and (HC4).
This also proves convergence in Hilbert--Schmidt norm after the input
projections are inserted. No trace of an unbounded inverse Gram is taken.

For a finite retained source frame \(E\), let \(G=E^*E\). In the column-kernel
convention of IW2--IW5,
\[
 M_U^*E=EA,\qquad A=J_U^*.
\]
For literal compatible data \(N=OU,\ D=OB,\ R=N-D\), with \(O\)
holomorphic and nonzero at the retained denominator nodes, put
\[
 C=J_O^*,\quad R_c=J_R^*=CA=AC,\quad G_O=C^*GC,\quad
 H_I=E^*M_U^*\Pi_I M_UE.
\]
The node multiplicities ensure \(J_D=0\) through all retained jets. Then
\[
 \operatorname{tr}(G_O^{-1}R_c^*H_IR_c)
 =\operatorname{tr}(G^{-1}A^*H_IA)
 =\|\Pi_I P_U E G^{-1/2}\|_{\mathcal S_2}^2
 =C_I(B_{\rm retained},U).                               \tag{HC9}
\]
This is the physical projection in (HC5). The outer metric is retained
before the exact finite congruence; no global bounded inverse outer operator
is assumed. In HT4 derivative coordinates all coefficient matrices must
also be conjugated by the diagonal \(i^r\) phase matrix.
Historical raw value jets are not coefficient matrices and are not used.

## 4. What an omitted divisor does and does not cost

Write \(B=B_mV_m\). The orthogonal decomposition
\[
 K_B=K_{B_m}\oplus B_mK_{V_m}
\]
gives the EXACT source-tail identity
\[
 C_I(B,U)-C_I(B_m,U)
   =\|\Pi_I P_U M_{B_m}P_{K_{V_m}}\|_{\mathcal S_2}^2.      \tag{HC10}
\]
Its nonnegative value tends to zero under (HC1), by (HC4), but no rate
in terms of only \(\sum_{V_m(b)=0}\Im b\) follows from the proof.

For the BARE inner-multiplied trace, causality DOES give
\[
 T_I(B,U)-T_I(B_m,U)
 =\|\Pi_I M_{UB_m}P_{K_{V_m}}\|_{\mathcal S_2}^2
 \le2L\sum_{V_m(b)=0}\Im b.                               \tag{HC11}
\]
Replacing \(M_U\) by the noncausal projection \(P_U\) in this argument is
invalid. The following geographic example refutes that replacement with
the same constant \(2L\).

Take
\[
 V(z)=\frac{z-i}{z+i},\quad b=2+i/4,\quad
 U(z)=\frac{z-i/2}{z+i/2},\quad B=V\,\frac{z-b}{z-\bar b}.
\]
The disk \(|z|\le3/2\) retains \(V\) and omits \(b\).
Use the actual compatible source \(O=1,\ N=U,\ D=B,\ R=U-B\).
The normalized omitted vector is \(Vk_b\), where the inverse Fourier
transform of \(k_b\) is \(\sqrt{2\Im b}e^{-(\Im b+i\Re b)t}\).

Let \(f\) be the inverse transform of \(P_U(Vk_b)\). Direct rational
projection gives
\[
 \frac{f(t)}{\sqrt{2\Im b}}
  =\left(\frac{24+64i}{73}\right)e^{-t}
   +\left(\frac4{73}-\frac{32i}{219}\right)e^{-t/2}
   +\left(\frac{49-64i}{73}\right)e^{-(1/4+2i)t}.           \tag{HC12}
\]
To reproduce it, divide \(V(z)/(z-\bar b)\) by \(U(z)\), discard its
upper-half-plane pole, and multiply the remaining lower-pole part by \(U\).
That is \(M_U P_{H^2}M_{\bar U}\), not an arbitrary matrix substitution.

The origin value is \(77/73-32i/219\), with squared modulus \(745/657>1\).
For the three coefficients \(d_j\) and exponents \(z_j\) in (HC12),
\[
 \sum_j(|\Re d_j|+|\Im d_j|)(|\Re z_j|+|\Im z_j|)
 =4195/876.
\]
Since \(|e^{-zt}-1|\le|z|t\) for \(\Re z\ge0\), for
\(0\le t\le L_0=24/4195\) the real part in (HC12) is at least \(75/73>1\).
Therefore for every \(0<L\le L_0\),
\[
 \boxed{C_{[0,L]}(B,U)-C_{[0,L]}(V,U)
 \ge 2L\Im b\,(75/73)^2>2L\Im b.}                         \tag{HC13}
\]
This is a source-compatible finite countercontrol, not an actual-Xi example.
It refutes the advertised constant-one tail-height replacement, not every
possible quantitative source-tail inequality.

## 5. Singular denominator and growth/count countercontrols

A denominator singular factor cannot be hidden in a zero-height sum.
For \(B(z)=e^{i\tau z}\), \(\tau>0\), there are NO zeros and hence the
zero-height sum is zero. Yet \(K_B=L^2(0,\tau)\) in the Fourier realization.
With \(U=1\), any interval \(I\subset(0,\tau)\) of positive length gives
\[
 C_I(B,1)=\operatorname{tr}\Pi_I=\infty.                   \tag{HC14}
\]
Normalized indicators of arbitrarily many disjoint subintervals of \(I\)
are an explicit orthonormal family fixed by that projection. This zero-free
example has entire exponential growth and zero local zero counts.
No assertion about more general denominator singular measures is needed:
they are all excluded from (HC1).

Even a PURE Blaschke denominator need not have finite height from a
growth/count hypothesis. For example take \(b_j=16\cdot2^j+i,\ j\ge1\).
The Blaschke condition holds, and the zero count is \(O(\log(R+2))\).
The genus-zero products with zeros \(b_j\) and \(\bar b_j\) converge;
their logarithmic maximum growth is \(O((\log(R+2))^2)\), by splitting
\(\sum_j\log(1+R/(16\cdot2^j))\) at \(j\asymp\log_2(R+2)\).
Their quotient is the Blaschke denominator, up to a unimodular constant.

The normalized kernels \(f_j(t)=\sqrt2e^{-(1+i16\cdot2^j)t}\) satisfy
\[
 |\langle f_j,f_k\rangle|\le\frac2{16|2^j-2^k|},\qquad
 \sup_j\sum_{k\ne j}|\langle f_j,f_k\rangle|\le1/4 .
\]
Indeed the lower-index reciprocal sum is at most
\((j-1)/2^{j-1}\le1\), and the upper-index sum at most \(2^{1-j}\le1\).
Every finite family therefore has Gram operator at most \(5/4\).
For any fixed \(0\le A<D<\infty\), each kernel has band mass
\(m=e^{-2A}-e^{-2D}>0\). Projection onto their span is at least
\(4/5\) times the sum of their rank-one operators. Consequently
\[
 \operatorname{tr}(\Pi_{[A,D]}P_{K_B}\Pi_{[A,D]})=\infty,   \tag{HC15}
\]
even after omitting any fixed geographic disk: its retained model space is
finite dimensional, so subtracting its finite band trace leaves infinite
trace on the orthogonal omitted-source summand. Here \(U=1\);
the compatible source may be written \(N=1,D=B,R=1-B\).
This is not a cosine repetition and not an actual-Xi counterexample.
It shows that count/growth upper bounds alone cannot pay horizontal tails.

Conversely \(b_j=2^j+i2^{-j}\) has infinite rank but \(S=1\), so (HC3)
gives finite bounded-band traces. For \(U=1\), its TOTAL charge is
\(\dim K_B=\infty\). Thus even finite total height does not make this
band theorem a total-charge theorem.

## 6. Native Xi boundary and order of limits

UC8--UC12 at the frozen Xi source gives \(L\asymp\log T\), an accepted
width \(O(1/(T\log T))\), and a small normalized trace for finite actual
geographic packets. Our estimate is \(2LS\), NOT \(2|I|S\), and cannot
simply replace the shrinking-width calculation.

We do not prove that an actual global companion denominator has finite
total height, is a pure Blaschke factor in the required global model, or
has a compatible nested native exhaustion. The historical L-106621
finite-window/cofinal ledger is not imported as any such theorem.
Actual Xi kernel asymptotics do not, by themselves, identify a pole-height
tail or an operator approximation error. The countercontrols above refute
only growth/count-based generic inferences; they do not reproduce the
actual Xi theta kernel or its arithmetic source.

Even if (HC1) is supplied separately at each physical \(T\), (HC4) gives
no uniform rate with the cutoff tied to \(T\). The native application still
needs quantitative source-tail/boundary/approximation control, compatibility
of numerators and outer-normalized jets, and the specified order of limits.
The exact unpaid source-tail operator is (HC10). There is no conclusion
about total Pick charge, free energy, topological index, a critical-line
percentage, reverse-Rolle descent, RH, GRH, or novelty.

## 7. Proof and replay provenance

The analytic ingredients are classical: model-space orthogonal decomposition,
Hardy causality, multiplier-adjoint coinvariance, and monotone trace/ideal
arguments. The decomposition is recorded in
[Fricain--Hartmann--Ross, (2.12)](https://arxiv.org/pdf/1605.07418v2).
The source-specific use and exact leakage countercontrol are the purpose;
no external priority claim is made. All load-bearing arguments are included
above rather than delegated to finite numerics.

The producer independently builds finite complex/confluent Grams and their
Lyapunov/origin-height identities, reconstructs the rational projection
(HC12) by residues and full polynomial identities, checks all quantitative
constants in (HC13), and uses exact interval indicators for (HC14).
Dyadic height and lacunary Gram controls exercise the two infinite examples,
but their limits are proved in prose, not inferred from bounded panels.

Nine primitive note/review objects are pinned by commit, Git blob and
LF-normalized SHA-256. The fixture additionally binds this note, producer,
manifest and tests. Source roles and complete typed schemas are immutable;
duplicate/nonfinite JSON, unsupported numeric types, oversized shapes/bytes,
rational overflow and altered digests fail closed. No result-bearing assert,
floating-point Fourier integration, sampled Xi zero, or unbounded search runs.
The finite model cap is degree four; the interval/lacunary cap is eight;
raw rational components use 16 bits and internal ones 1024 bits.
