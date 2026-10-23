# Möbius residue and remainder estimates

22 October 2026. **Proposed source-dependent analytic improvements. The
zero-free boundary has not decreased.** The inherited numerical reference
remains

\[
 B_\flat=0.874886647039964\ldots.
\]

This packet extends the reviewed Gram-conditioning work in
[PR #1013](https://github.com/GettysburgResearch/riemann/pull/1013), at
commit `ff620ffe983f086eaab070311ab304a994bbf0d4`. It estimates the
actual Möbius coefficient against the complete primitive pole and the
complete primitive scalar remainder, and retains all moduli in a
finite Gauss operator estimate. The full signed inverse
moment remains a separate open estimate. In particular the earlier
conditional `0.8745` certificate is still conditional.

The statements below are deductions from the explicitly pinned inputs
in [SOURCE_MANIFEST.json](SOURCE_MANIFEST.json). The independent review
record is added as [REVIEW.md](REVIEW.md) in a later commit, preserving
the frozen mathematical files. These are standalone research results;
this packet does not change the repository's integrated baseline.

## 1. The complete primitive pole has a saving

Use good Eisenstein ideals, the fixed primary convention, and literal
zero extension of all sextic characters. For a fixed smooth annular
profile and fixed ray data, put

\[
 b_n=1_{(n,Q)=1}\frac{\mu(n)\nu(n)}{\sqrt{Nn}}W(Nn/D),
 \qquad
 P_R(D)=\sum_n b_n\rho_{\rm prim}(nR).
\]

The puncture \(Q\) stays fixed during each row sum; its permitted loss
is a subpower of \(NQ\). The ray component of the primitive residue
is fixed on each of the finitely many numerator sectors in the source.
The residue uses the raw Dirichlet exponent, with pole at \(7/6\).

The new reference-scale argument gives

\[
 \boxed{|P_R(D)|^2\ll_\epsilon
       (DNRNQ)^\epsilon D^{2/3}(NR)^{1/3}.}
\]

The argument pairs the exact primitive adjoint identity at a freely
chosen row scale \(T\) with the actual coefficient \(b\). The imported
inverse moment and continued remainder mean give

\[
 |P_R(D)|^2\ll (TDNRNQ)^\epsilon T^{-1/3}
    \bigl(T+T^{1/6}D^{5/6}+D\sqrt{NR}\bigr).
\]

Taking \(T=D\sqrt{NR}\) proves the displayed bound. It includes every
primitive-inversion divisor and requires no Euler product for the
sextic theta coefficients.

At the actual detector scale \(U\), the squared pole contribution
for \(R=1\) is therefore

\[
 \boxed{U^{1/3}|P_1(D)|^2
       \ll(UDNQ)^\epsilon U^{1/3}D^{2/3}.}
\]

Its ratio to the inherited inverse term \(U^{1/6}D^{5/6}\) is
\((U/D)^{1/6}\). At the active length ratio
\(U=D^{0.859140794\ldots}\), the corresponding powers of \(D\)
are approximately \(0.953046931\) and \(0.976523466\).
These decimals compare component estimates; they are not a new
zero-free boundary.

The proof also gives
\(\sum_{NR\le K}|P_R(D)|^2\ll(DKNQ)^\epsilon D^{2/3}K\)
on distinct sixth-power-free labels when the stated reference-scale
Gram condition holds. The factor \(K\) remains.

Full proof: [MOBIUS_PRIMITIVE_POLE_REFERENCE_SCALE.md](MOBIUS_PRIMITIVE_POLE_REFERENCE_SCALE.md).

## 2. A scalar full-series remainder bound

Let \(D_\nu(n,u)=\sum_c\nu(c)g_6(n,c)(Nc)^{-u}\) be the full
series, and let \(\mathcal E_U[D_\nu(n)]\) be its smooth contour
integral on \(\Re u=1+\eta\), with normalization
\(\widehat w(u-1/2)U^{u-1}\). For the coefficient \(b\) above and
the paper-8 fixed modulo-36 section family, the scalar theorem is

\[
 \boxed{\left|\sum_n b_n\mathcal E_U[D_\nu(n)]\right|^2
 \ll_\epsilon(UDNQ)^\epsilon
 \begin{cases}
 D^{5/6}U^{1/6},&1\le U\le\sqrt D,\\
 D^{11/12},&U\ge\sqrt D.
 \end{cases}}
\]

The proof reflects the completed finite vector
\(Z_\nu(n,u)=\zeta_S(6u-5)D_\nu(n,u)\). It retains the
nonsquarefree modulus branches \(n=em,\ c=e^2c_0\), the finite
bad-prime sections, and all completion indices. For the completed
scalar pairing \(F(Y)\), reflection and the original expansion give

\[
 |F(Y)|^2\ll
 \begin{cases}
 (DNQ\max(Y,Y^{-1}))^\epsilon D^{5/6}Y^{1/6},
       &0<Y\le\sqrt D,\\
 (YDNQ)^\epsilon DY^{-1/6},&Y\ge\sqrt D.
 \end{cases}
\]

Removing completion on the original contour is the exact sum
\(\sum_a\mu(a)(Na)^{-1}F(U/(Na)^6)\). Splitting it at
\(Na=(U^2/D)^{1/12}\) gives \(D^{11/12}\). Empty physical
windows contribute their negative residue term; they are retained in
this convergent sum. No raw-series contour is shifted across possible
zeros of its completion factor.

This theorem concerns a single pairing for the **full** series. The
primitive extension below retains its additional divisor dependence
through the proof; it is not a black-box application of this bound.

Full proof: [MOBIUS_FULL_SERIES_SCALAR_REMAINDER.md](MOBIUS_FULL_SERIES_SCALAR_REMAINDER.md).
The exact kernel and local-component calculation is recorded separately
in [COMPLETED_FE_KERNEL.md](COMPLETED_FE_KERNEL.md).

## 3. The complete primitive scalar remainder also saves a power

Retaining every term in primitive inversion gives the stronger result

\[
 \boxed{\left|\sum_n b_n\mathcal E_U[H_\nu(n)]\right|^2
       \ll_\epsilon(UDNQ)^\epsilon\bigl(U+D^{11/12}\bigr).}
\]

The proof keeps all three auxiliary indices: the primitive divisor
\(d\mid n\), its Euler variable \(k\mid n^\infty\), and the
reciprocal-completion variable \(a\). It extracts the support of
\(k\) from the squarefree numerator before applying an inverse
moment. The nonzero Gauss moduli have the exact form
\(c=e^2f^4c_0\). After the local character factors combine, the free
coefficient remains a pure Möbius coefficient with its original zeros.

The split
\[
 Na\asymp U^{1/6}D^{-1/12}(Nk)^{-1}(Nd)^{-1/2}
\]
depends only on the fixed outer indices \(d,k\). It therefore
preserves the full-residue progression pairing in the partial pole
sum. The remaining weights form convergent Euler products; the
smallest local exponent in the non-volume sum is \(7/6>1\).
The volume terms cost \(U\), and the squared partial pole bound is
\(D^{5/6}\). Neither term spoils the stated estimate.

Together with Section 1, the **actual single Gauss-vector pairing**
from the primitive adjoint identity consequently has squared bound

\[
 \boxed{(UDNQ)^\epsilon
       \bigl(U+D^{11/12}+U^{1/3}D^{2/3}\bigr).}
\]

For \(U=D^h\) with any fixed \(1/2<h<1\), the new exponent is
\(\max\{11/12,(h+2)/3\}\). Compared with the inherited bound
\((h+5)/6\), the saving is

\[
 \min\{(2h-1)/12,\ (1-h)/6\}>0.
\]

At the active ratio, this changes the power for this pairing from
approximately \(D^{0.976523466}\) to \(D^{0.953046931}\), up to
subpowers. This is a power saving for the prescribed coefficient,
including the entire primitive remainder. It still estimates one
Gauss pairing; the inverse moment is a norm over all rows.

Full proof: [MOBIUS_PRIMITIVE_SCALAR_REMAINDER.md](MOBIUS_PRIMITIVE_SCALAR_REMAINDER.md).

## 4. Exact removal of the empty primitive tail

Primitive inversion has terms indexed by \(d\mid n\) and
\(k\mid n^\infty\), with physical scale
\(U/((Nd)^2(Nk)^6)\). If the support of \(w\) is contained in
\([a,b]\), the region \((Nd)^2(Nk)^6>bU\) has no modulus at
all, including no unit modulus. Its contribution is exactly

\[
 -c_w U^{1/6}\rho_{\rm full}(n)
   \sum_{\substack{d\mid n,\ k\mid n^\infty\\
          (Nd)^2(Nk)^6>bU}}\frac{\mu(d)}{Nd(Nk)^2}.
\]

The squared pairing of this entire region with \(b\) is
\(\ll_\epsilon(UD)^\epsilon U^{-1/3}D^{5/6}\). The proof
uses the exact local residue recurrence, followed by a divisor bound
and the fixed-form residual square sum. The density input is restricted
to paper 8's fixed modulo-36 characters and their specified finite
conversions. An extension to every component of the larger functional
equation is not assumed.

Full proof: [PRIMITIVE_INVERSION_EMPTY_MODULUS_TAIL.md](PRIMITIVE_INVERSION_EMPTY_MODULUS_TAIL.md).

## 5. Two supporting estimates retain more information

**The weighted full mean.** Write \(M=AB\). The source's smoothed
two-length bound can be kept through its absorption proof, giving

\[
 \frac1B\sum_{\substack{a\asymp A,b\asymp B\\
                   ab\ {\rm squarefree},\ (ab,h)=1}}
 |D_\nu(hab^3,1+\eta+it)|^2
 \ll (NhM)^\epsilon\sqrt{Nh}(1+|t|)^6\mathcal F(A,B),
\]

where

\[
 \mathcal F(A,B)=\min\{M/B+\sqrt M B+MB^{-1/2}
                   +M^{3/4}B^{1/2},\ M/B+M^{3/2}/B\}.
\]

This saves a power over the coarser \(M\) bound in the specified
unbalanced divisor ranges. The bound retains all full moduli and
finite source sections. It does not itself sum primitive inversion
against the prescribed Möbius coefficient.

Proof: [REFINED_WEIGHTED_FULL_MEAN.md](REFINED_WEIGHTED_FULL_MEAN.md).

**The finite Gauss operator.** For arbitrary bounded modulus weights,
rows \(Nn\le X\), distinct sixth-power-free labels \(NR\le K\),
and a fixed smooth profile supported on \(Nc\ll K\), the naturally
normalized finite operator

\[
 T(n,R)=K^{-1/2}\sum_c
     \frac{a_cg_6(nR,c)}{\sqrt{Nc}}F(Nc/K),\qquad |a_c|\le1,
\]

satisfies \(\|T\|_{\rm op}^2\ll(XK)^\epsilon XK^{1/6}\)
when \(1\le K\le\sqrt X\). Nonsquarefree moduli are included.
The proof first reduces the additive fraction exactly, then uses
orthogonality of its distinct local characters. A continued primitive
remainder is not replaced by this finite operator without a separate
identity and scale calculation.

Proof: [FINITE_FULL_GAUSS_OPERATOR.md](FINITE_FULL_GAUSS_OPERATOR.md).

## 6. The missing implication to a smaller boundary

The desired full inverse estimate concerns
\(I(H,D)=\sum_{Nr\le H}|M_r(D;Q)|^2\), including all source
weights and natural zeros. A sufficient improvement near the binding
lengths would have some fixed \(\vartheta>0\) in

\[
 I(H,D)\ll(HDNQ)^\epsilon\left[H+\frac HD
       \left(\frac{D^2}{H}\right)^{5/6-\vartheta}
                    D^{1/6+\vartheta}\right].
\]

The original signed common-divisor sum must survive the two-column
Poisson return, together with its two shared profiles and moving masks.
The finite projection identity has a separate complementary norm;
small pole or Gauss pairings do not bound that norm.

The audit in [DE_FAVERI_CORRECTION_TRANSFER_AUDIT.md](DE_FAVERI_CORRECTION_TRANSFER_AUDIT.md)
locates the sixth-power cross term in the generic sieve proof and the
earlier operations that discard the needed signs. It supplies no
license to subtract that term from a finished upper bound. The exact
endpoint-sensitive target remains
[WEAKER_CENTERED_TARGET.md](../2026-10-20-boundary-iteration/mixed/WEAKER_CENTERED_TARGET.md).

## 7. Exact finite checks and review scope

The included checker uses integer pairs in \(\mathbf Q(\omega)\)
to test the finite Gauss push-forward and character orthogonality. It
covers 35 moduli through norm 2401, 9330 label cases, 200412 exact
coefficient comparisons, and 1555 quotient-character sums covering
209125 ordered pairs. Cases include inert and split primes, conjugate
primes, repeated powers, disappearing-prime zeros, and the unit modulus.
Three deliberately incorrect formula variants are rejected.

From the repository root:

```bash
python standalone/2026-10-22-residue-remainder-followup/check_full_gauss_algebra.py \
  --theorem standalone/2026-10-22-residue-remainder-followup/FINITE_FULL_GAUSS_OPERATOR.md \
  --output /tmp/riemann_full_gauss_replay.json
```

The coordinating agent replayed the check and reproduced the saved JSON
byte for byte. The exact coverage and arithmetic contract are in
[FULL_GAUSS_FINITE_CHECK.md](FULL_GAUSS_FINITE_CHECK.md). The checks
authenticate finite algebra only. Analytic continuation, inverse means,
and the infinite estimates are addressed by the proofs and their
source-specific independent reviews; they are not verified by this
computation.
