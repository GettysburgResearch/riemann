# Möbius pairing with the complete primitive sextic residue

Status: proposed analytic lemma; not independently reviewed.

Scope: the actual pure Möbius coefficient, its fixed ray filters, and its
fixed-during-the-row-sum puncture. This controls the entire primitive
residue, including all numerator-prime terms implicit in primitive
inversion. It does not bound the continuous complementary operator or
prove a smaller zero-free boundary.

Provenance: the reference-scale argument and the optimized scalar/vector
extensions were proposed by the root agent on 22 October 2026. This note
records joint_continuation's normalization and accounting verification.

## 1. Exact imports

Work over the Eisenstein field, with good ideals prime to 6 and the
multiplicative primary representatives used in the cited sources.

**Inverse moment.** Import the inherited inverse estimate in the first
signed-boundary packet, in its actual coefficient form:

\[
 M_u(D;Q)=\sum_{(n,Q)=1}
     \frac{\mu(n)\nu(n)}{\sqrt{Nn}}W(Nn/D)
       \overline{\chi_n(u)},
\]

\[
 \sum_{0<Nu\le T}|M_u(D;Q)|^2
 \ll_{\epsilon,W}(TDNQ)^\epsilon
          \bigl(T+T^{1/6}D^{5/6}\bigr).
 \tag{1}
\]

Here the coefficient has a fixed smooth annular profile, fixed finite ray
data, and a puncture Q fixed throughout the u sum. The same estimate holds
after a fixed ray-sector restriction of n by expansion in finitely many
ray characters. We retain the source's stated uniformity in Q. In
particular, polynomially bounded Q is permitted in the applications
below. No arbitrary-coefficient replacement of (1) is made.

**Adjoint identity and continuous mean.** Import paper 10 version 2,
Section 7, equations (7.1)--(7.3), from the pinned source

<https://rstation.ai/api/v1/papers/riemann_hypothesis_10/versions/2/download>.

The local snapshot is `work/round2_sources/paper10-v2.md`, SHA256
`525c899dd4dd5cb0ed15db43f63fb6e25cc140f98358e9d41ddfe897f5a23a7a`.

For one fixed, nonzero, nonnegative, smooth annular weight w, write
\(c_w=\widehat w(2/3)>0\). On squarefree good rows z, set

\[
 A_T(z,n)=\sqrt{w(Nz/T)}\chi_n(z),\qquad
 v_{T,R}(z)=T^{-1/2}\sqrt{w(Nz/T)}\gamma_1(z)
                     \overline{\chi_z(R)}.
\]

On a fixed numerator ray sector the exact identity is

\[
 A_T^*v_{T,R}=c_wT^{1/6}\rho_R+E_{T,R},
 \qquad
 \rho_R(n)=\rho_{\mathrm{prim},\nu_{[n]}}(nR),
 \tag{2}
\]

and, uniformly for good R,

\[
 \sum_{n\asymp D}|E_{T,R}(n)|^2
 \ll_{\epsilon,w}(TDNR)^\epsilon D(NR)^{1/2}.
 \tag{3}
\]

The nR numerator is unrestricted. In particular, (2)--(3) do not impose
\((n,R)=1\), and include nR with square factors. The primitive local
zeros are already present in (2).

The ray component \(\nu_{[n]}\) is fixed on each selected n sector. If a
different fixed component is needed, multiply every v column by the same
fixed row ray character. This alters neither its norm nor its Gram
matrix. The source identity then has the corresponding fixed component.
Summing the finitely many sector estimates changes constants only.

## 2. Normalization and the scalar lemma

Let

\[
 b_n=1_{(n,Q)=1}\frac{\mu(n)\nu(n)}{\sqrt{Nn}}W(Nn/D),
 \qquad \alpha_n=\overline{b_n}.
\]

An optional fixed ray-sector indicator is included in b. We use
\(\langle x,y\rangle=\sum_n\overline{x_n}y_n\), so the target is

\[
 P_R(D)=\langle\alpha,\rho_R\rangle
       =\sum_n b_n\rho_R(n).
 \tag{4}
\]

The columns are restricted to the fixed annulus supporting W. The
elementary ideal count gives \(\|\alpha\|_2^2\ll_W1\); the weaker
subpower bound would suffice. With this conjugation,

\[
 (A_T\alpha)(z)=\sqrt{w(Nz/T)}\,\overline{M_z(D;Q)}.
\]

The squarefree row restriction is a subset of the nonnegative sum in
(1). As w has fixed support and is bounded,

\[
 \|A_T\alpha\|_2^2
 \ll (TDNQ)^\epsilon(T+T^{1/6}D^{5/6}).
 \tag{5}
\]

Also \(\|v_{T,R}\|_2^2\ll_w1\), uniformly in R: its character factors
have absolute value at most one, including at their natural zeros.
Pairing (2) with alpha, applying Cauchy--Schwarz separately to its two
terms, and using (3)--(5) gives

\[
 |P_R(D)|^2
 \ll (TDNRNQ)^\epsilon T^{-1/3}
       \left(T+T^{1/6}D^{5/6}+D(NR)^{1/2}\right).
 \tag{6}
\]

This is a reference-scale estimate. T is freely chosen; it need not equal
the row scale in a later detector.

**Scalar lemma.** For every fixed epsilon>0,

\[
 \boxed{\quad |P_R(D)|^2
       \ll (DNRNQ)^\epsilon D^{2/3}(NR)^{1/3}.\quad}
 \tag{7}
\]

Indeed choose \(T=D(NR)^{1/2}\ge D\). The middle term of (6) is at
most T, and the first and last terms coincide. In particular,

\[
 \boxed{\quad |P_1(D)|^2\ll(DNQ)^\epsilon D^{2/3}.\quad}
 \tag{8}
\]

This proof uses the entire primitive residue from (2); it never isolates
the d=1 term of primitive inversion. There is no assertion that the
sextic theta coefficients have an Euler product.

For R=1 the choice T=D minimizes the powers available from (6): for
T>=D the expression is bounded at its optimum by T^(2/3)+D T^(-1/3),
while for T<D the inherited inverse term grows as
T^(-1/6)D^(5/6). Thus an improvement of (8) needs a new input, not merely a
different reference scale in the same three estimates.

## 3. The pole at the actual detector scale

At any actual row scale U, the pole component of the adjoint pairing is
\(c_wU^{1/6}P_1(D)\). By (8),

\[
 |c_wU^{1/6}P_1(D)|^2
 \ll (UDNQ)^\epsilon U^{1/3}D^{2/3}.
 \tag{9}
\]

For U<=D, comparison with the inherited non-volume term is exact:

\[
 U^{1/3}D^{2/3}
  =U^{1/6}D^{5/6}(U/D)^{1/6}.
 \tag{10}
\]

Consequently the pole has a strict power saving whenever D/U is a fixed
positive power of D. At the currently binding length ratio, writing
U=D^h with h approximately 0.859140794, (9) has exponent
\(h/3+2/3\approx0.953046931\), compared with
\(h/6+5/6\approx0.976523466\) for the inherited inverse term.
These decimal comparisons only describe that previously identified
active regime; (9)--(10) are the exact statements.

This does not imply an upper bound for the complete inverse moment.
Even the scalar remainder bound obtained directly from (3) is
\(|\langle\alpha,E_{U,1}\rangle|^2\ll D^{1+\epsilon}\), which is
larger than the binding inherited term when U<D. Nor does a small
projection onto one Gauss vector bound the orthogonal complement.

## 4. A vector extension using the conditioned frame

Let \(\mathcal R_K\) be any subset of distinct good sixth-power-free
labels with NR<=K. Let V_T have columns v_(T,R) and put G_T=V_T^*V_T.
Import the proved hyperbolic Gram upper bound from
`standalone/2026-10-22-gram-conditioning-followup/HYPERBOLIC_PUNCTURE_GRAM.md`,
SHA256
`c75ca666d0b9600eb00fd1be79bd9fba8721d8b5f9101beb3d036f760bd910ed`.
It gives \(\|G_T\|\ll T^\epsilon\) whenever
\(K\le T^{1/2-\delta}\) for some fixed delta>0. Only this upper bound
is used here; no inverse Gram matrix is needed in this step.

Write \(\mathbf P=(P_R(D))_{R\in\mathcal R_K}\). Pairing all columns
of (2), and using \(\|V_T^*A_T\alpha\|^2\le
\|G_T\|\|A_T\alpha\|^2\), yields

\[
 \|\mathbf P\|_2^2
 \ll (TDKNQ)^\epsilon T^{-1/3}
      \left(T+T^{1/6}D^{5/6}+DK^{3/2}\right).
 \tag{11}
\]

For the error term we used exactly

\[
 \sum_R|\langle\alpha,E_{T,R}\rangle|^2
 \le\|\alpha\|_2^2\sum_R\|E_{T,R}\|_2^2
 \ll (TDK)^\epsilon D\sum_{NR\le K}(NR)^{1/2}
 \ll (TDK)^\epsilon DK^{3/2}.
\]

Choose \(T=DK^{3/2}\). Then, provided the Gram range holds,

\[
 \boxed{\quad
 \sum_{R\in\mathcal R_K}|P_R(D)|^2
      \ll(DKNQ)^\epsilon D^{2/3}K.\quad}
 \tag{12}
\]

For example, fix 0<kappa<2 and require \(K\le D^{2-\kappa}\).
Then a sufficiently small fixed delta>0 satisfies
\(K\le(DK^{3/2})^{1/2-\delta}\) uniformly in this range. One explicit
choice is any
\[
 0<\delta<\frac{\kappa}{16-6\kappa}.
\]

The denominator is positive for 0<kappa<2. Indeed the worst exponent
comparison is
\((2-\kappa)(1/4+3\delta/2)\le1/2-\delta\).

At an actual scale U for which G_U is also conditioned, the squared norm
of the pole vector after projection normalization is at most

\[
 c_w^2U^{1/3}\|G_U^{-1/2}\overline{\mathbf P}\|_2^2
 \ll(UDKNQ)^\epsilon U^{1/3}D^{2/3}K.
 \tag{13}
\]

Equation (13) retains a factor K. It is smaller than the inherited
non-volume inverse term only in the corresponding strict range
\(K<(D/U)^{1/6}\), up to subpowers. No unrestricted vector projection
gain is asserted.

The conjugation in (13) is necessary with the inner-product convention
in (4): the pole coordinate of \(V_U^*A_U\alpha\) is
\(c_wU^{1/6}\overline{P_R(D)}\). It does not change the norm upper bound.

## 5. Review boundary

The load-bearing inputs are the actual-coefficient inverse estimate (1),
the exact primitive adjoint identity (2), and its uniform remainder mean
(3). The scalar conclusion (7) needs no Gram theorem. The vector
conclusion (12) additionally uses only the Gram upper bound at the freely
chosen reference scale. Natural zeros and shared numerator primes are
not removed at any point.

No numerical computation is part of the proof. A separate review should
check the inherited uniformity of (1) under fixed ray filters and the
puncture Q, and independently verify the conjugation in (4)--(5). The
continuous remainder and the full complementary row space remain the
steps required for a smaller zero-free boundary.
