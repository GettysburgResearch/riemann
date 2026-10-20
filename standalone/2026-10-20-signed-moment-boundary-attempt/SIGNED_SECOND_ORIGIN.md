# The second origin with the complete coprimality projector retained

Research derivation, 20 October 2026. This proves an exact finite-sum
identity and its interface with Liu's first product transform. It does
not prove an improved product moment or a smaller zero-free boundary.

## 1. Source and inherited conventions

The source is Baiying Liu, *Zero-free half-planes over number fields*,
[arXiv:2610.26835v1](https://arxiv.org/abs/2610.26835v1), specifically
Lemmas 12.9–12.10 and §§12.7.1–12.7.3, printed pp. 72–78. The PDF used
has SHA-256

```
5d0fd10274c8444c789b0b7925a1cd3419017fe760be3219b6be51d7fbed9bd5
```

The derived local text has SHA-256

```
2f3c7f462d8a68a9406e37b7bbdda484e3ca5d1ed100a59bf61f00a28cf6e274
```

We use the source's field containing the twelfth roots of unity,
localized principal ideal ring, fixed compatible additive characters,
and allowed generators. Ideals or their fixed allowed generators are
identified only in this convention; write \(q_u=Nu\). The symbol

\[
\chi_u(x)
\]

is the full zero-extended sextic character modulo \(u\), including its
unit indicator when its inducing character is principal. Thus
\(\chi_u(0)=0\) for every nonunit modulus \(u\), whereas
\(\chi_1(0)=1\). None of these characters is replaced by its primitive
inducing character. All exterior primes at which a natural zero is
present remain excluded.

For the normalized full Gauss sum put

\[
G(u,h)=q_u^{-1/2}\sum_{x\bmod u}\chi_u(x)e(hx/u).
\]

Conjugates below use the source's correlation orientation. Because
\(-1\) is a sixth power in the field, changing \(h\) to \(-h\) in a
sextic Gauss sum introduces no exterior sign. Any fixed finite-place
choice in an allowed-generator convention must be kept on both sides.

Let \(r\) be the squarefree common primitive modulus in (12.2), and
let \(\xi_r\) be its primitive character, zero-extended modulo \(r\).
For \(r=1\) take \(\xi_1=1\), including at zero. Define

\[
G_{\xi_r}(r,h)=q_r^{-1/2}
 \sum_{x\bmod r}\xi_r(x)e(hx/r).
\]

After the source's complete common-support extraction, every residual
column is coprime to \(CD\), hence to \(r\). This condition is retained
on the artificial residual pairs used by the complete Möbius
extension. The two residual columns need not be coprime on that
extension.

## 2. Exact finite-origin identity

**Proposition.** Suppose \((r,uv)=1\), and retain the full Gauss sums
above. Define

\[
\mathcal F_r(u,v;0)=
 \frac{1}{\sqrt{q_rq_uq_v}}
 \sum_{h\bmod ruv}G_{\xi_r}(r,h)G(u,h)\overline{G(v,h)}.
\tag{1}
\]

Then

\[
\mathcal F_r(u,v;0)
 =\xi_r(0)\,1_{u=v}\,\varphi_F(u).
\tag{2}
\]

Consequently the complete ideal Möbius projector gives

\[
\sum_{s\mid(u,v)}\mu_F(s)\,\mathcal F_r(u,v;0)
 =1_{r=1}\,1_{u=v=1}.
\tag{3}
\]

Here equality of columns means equality of modulus ideals, with the
consistent allowed representatives used in the source.

**Proof.** Additive orthogonality gives the finite sum

\[
\sum_{h\bmod r}G_{\xi_r}(r,h)
 =\sqrt{q_r}\,\xi_r(0).
\tag{4}
\]

Its normalized average is \(q_r^{-1/2}\xi_r(0)\), not the expression
in (4). Since \((r,uv)=1\), CRT splits the sum in (1) into the product
of the sum in (4) and the sum over \(h\bmod uv\). The remaining
normalization is precisely

\[
\frac{1}{\sqrt{q_uq_v}}
 \sum_{h\bmod uv}G(u,h)\overline{G(v,h)}
 =F(u,v;0)
 =1_{u=v}\varphi_F(u),
\]

by the full finite correlation in source Lemma 12.10. This proves (2)
also when \(u,v\) share primes or have imprimitive powers. For
nonunit \(r\), its character is zero at zero, so its contribution
vanishes before any use of the Möbius signs. For \(r=1\), only the
diagonal \(u=v\) remains, and

\[
\sum_{s\mid u}\mu_F(s)=1_{u=1}.
\]

Finally \(\varphi_F(1)=1\), proving (3). Every identity includes the
natural zeros. \(\square\)

## 3. The exact interface with the allocated convolution

Fix the first-transform common-support data \(C,D,r,e\), the two full
allocated convolution coefficients, their common extra coprimality
conditions, and the source's common Fourier measure in the whole
column norms. Before Cauchy, source (12.2) still has the projector

\[
1_{(u,v)=1}=\sum_{s\mid u,v}\mu_F(s).
\tag{5}
\]

Its stipulated off-coprime extension uses the same full Gauss sums,
whole norms, retained row weight and natural coprimality indicators.
The factors other than \(1_{s\mid u,v}\) therefore do not depend on
which divisor \(s\) is used to express (5). Multiplying (3) by those
common factors proves the second-origin cancellation for the exact
convolution, whether it has two, three, or any other fixed number of
plain factors. The same statement holds for an equal-product signed
stencil: it uses no separate main-term estimate for a factor.

If the divisibility condition has already been allocated among the
plain factors, its full inclusion–exclusion expansion and the exact
extraction scalars must first be recombined. The identical whole-column
coefficient then reappears. Taking absolute values of its allocations,
or using divisor-dependent enlarged row tests without restoring their
identity, does not preserve (3).

In the unweighted sector before any amplifier extraction, the only
remaining finite origin has \(u=v=r=1\). The original full columns are
then \(C,D\). If both convolution rectangles have whole product norm
comparable to \(Z^A\), their annular support forces

\[
c=d=A+O(1/\log Z).
\]

In particular the \(A-M-d\) part of the source's second-origin excess
is \(-M+O(1/\log Z)\) on this unit sector. The dangerous \(A-M\)
term attached to long residual columns is absent from the signed
origin. This observation does not assert a new bound on any amplified
error sector.

## 4. Full primitive phases and the restored common character

The unequal first-transform presentations do not obstruct exact
restoration. This can be checked without dropping the factor
\(G_{\xi_r}\).

On the genuine pairwise coprime locus \(r,u,v\), put

\[
P(x)=\xi_r(x)\chi_u(x)\overline{\chi_v(x)},\qquad
L=ruv,
\]

and retain the complete CRT factor

\[
\mathcal C(r,u,v)=
 \xi_r(uv)\chi_u(rv)\overline{\chi_v(ru)}.
\]

The finite Fourier transform of \(P\) is

\[
\widehat P(h)=
 \mathcal C(r,u,v)\sqrt{q_rq_uq_v}\,
 G_{\xi_r}(r,h)G(u,h)\overline{G(v,h)}.
\tag{6}
\]

To verify (6), use the CRT residue variable
\(x=uvx_r+rvx_u+rux_v\). Multiplicativity produces exactly
\(\mathcal C\); the additive character splits into the three Gauss
sums. The conjugate \(v\)-factor initially has the opposite additive
sign; the retained \(-1\) convention above identifies it with the
displayed one. All cross factors are evaluated at units.

Finite inversion now gives, with its full normalization,

\[
\frac{1}{\sqrt{q_rq_uq_v}}
 \sum_{h\bmod L}
 G_{\xi_r}(r,h)G(u,h)\overline{G(v,h)}e(-jh/L)
 =\mathcal C(r,u,v)^{-1}
  \xi_r(j)\chi_u(j)\overline{\chi_v(j)}.
\tag{7}
\]

Source symmetric reciprocity cancels the two cross phases between
\(u\) and \(v\). Thus the coefficient from (12.2) is exactly

\[
\tau_C(u)\overline{\tau_D(v)}
 =\tau(u)\overline{\tau(v)}
   \chi_u(e)\overline{\chi_v(e)}\,
   \mathcal C(r,u,v).
\tag{8}
\]

Multiplying (7) and (8) restores

\[
\xi_r(j)
 \bigl[\tau(u)\chi_u(ej)\bigr]
 \overline{\bigl[\tau(v)\chi_v(ej)\bigr]}.
\tag{9}
\]

Accordingly both child columns have the same presentation
\(\tau(n)\chi_n(ej)\), and \(\xi_r(j)\) remains a row phase,
including its zeros. Whole-column norm powers from Fourier separation
can be retained on the respective sides throughout. Equation (7) is
asserted on the genuine coprime locus; on artificial pairs the complete
projector must be restored first, or the full correlation must be used.

## 5. Scope and the remaining analytic requirement

The source already supplies the exact first transform, full
correlation and complete Möbius extension. The additional result here
is the combined identity (3), with the primitive common factor kept,
and the explicit common-character restoration (7)–(9). It proves that
the long positive second diagonal is introduced by the intervening
separate norm bounds, rather than forced by the exact signed finite
origin.

It supplies no free width decrease. If the first row scale is \(H\),
the first dual scale is

\[
T=\frac{q_e q_rq_uq_v}{H}.
\]

An exact second transform with that same scale has restored row scale
\(q_rq_uq_v/T=H/q_e\). The displayed column character in (9) has
support charge \(q+\log_Zq_e\). Hence its total row-plus-support width
is again \(M\). All kernels and profiles must be transformed exactly;
replacing them by wider positive majorants is an additional operation.

Already in the sector \(r=1\) with one common presentation, the signed
coprime column form is indefinite: restricted to two distinct coprime
nonunit columns with nonzero Gauss values, its off-diagonal Hermitian
block has eigenvalues of opposite signs.
Consequently the positive row enlargement used for the source's
separate Gauss norms cannot be applied to this form merely from (3).
The companion `SIGNED_SIXTH_POWER_GRAPH.md` identifies the aliases
retained by exact sixth-power graph amplification. A sixth-moment
improvement requires a bound for the resulting signed expression, or
another argument supplying a strict width decrease while preserving
the cancellation. No such estimate is proved here.
