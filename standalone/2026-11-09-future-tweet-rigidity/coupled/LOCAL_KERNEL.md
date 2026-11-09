# The affine sextic covariance has an exact rank-two hypergeometric transform

**Status.** Complete finite-field component arguments, followed by a specifically identified external analytic corollary. No native inverse-moment estimate, improved zero-free region, or RH proof is claimed. The new contribution here is an explicit adapter and its complete local spectrum, not a new hypergeometric-monodromy theorem.

The motivating source is the exact prime-extracted covariance in [PR #1022, OFF_DIAGONAL_TRANSFER.md](https://github.com/GettysburgResearch/riemann/blob/8b2c6d50ad2d729c681745717c615095bd8f1d9d/standalone/2026-10-25-hlc-zero-free-transfer/fourth-pass/OFF_DIAGONAL_TRANSFER.md). Its local affine constraint is

\[
 A_0p-B_0b=h,
 \qquad A_0=a_1dc_1,\quad B_0=a_2c_2,
\]

and its character phase is exactly

\[
 \psi_u(A_0p)\overline{\psi_u(B_0b)}.
\]

The remaining coefficient contains all four signs
\(\mu_E(a_1)\mu_E(a_2)\mu_E(d)\mu_E(b)\), the prime weight, the coprimality condition \((d,p)=1\), and the original profiles. None may be replaced by a coefficientwise absolute value. In particular, the collected column coefficient \(\lambda(n)\) of that note is not the Möbius function.

## 1. Fields, characters, and the two different completions

Let \(k=\mathbb F_q\), let \(\psi:k\to\mathbb C^\times\) be a nontrivial additive character, and let \(\chi:k^\times\to\mathbb C^\times\) be a nontrivial multiplicative character. Extend \(\chi(0)=0\). The elementary identities below do not require order six. This includes quadratic and cubic local characters obtained from powers of a sextic character.

For good Eisenstein residue primes, \(q\) is a prime or the square of a prime. The residue-field identities cover both. The imported short-interval bilinear theorem below is asserted only for prime \(q>3\).

If a local conductor prime divides \(A_0B_0\), the displayed zero-extended character phase is identically zero; do not divide by that coefficient. Otherwise put \(x=A_0p\), \(y=B_0b\). The constraint becomes \(x-y=h\), with exactly the masks \(x\ne0\), \(y\ne0\).

There are two inequivalent ways to arrange the Fourier variables.

1. Fourier expansion of the constraint, followed by independent sums over \(p,b\), gives, at each fixed additive frequency \(t\),

   \[
   \chi(A_0p)\psi(tA_0p)\,
   \overline{\chi(B_0b)\psi(tB_0b)}.
   \tag{1.1}
   \]

   This is a matrix of rank one. Calling the bare ratio kernel a higher-rank trace function would be incorrect.

2. Retaining the shift \(h\) and Fourier transforming in the common coordinate \(x\) produces

   \[
   T_\chi(h,t)=\sum_{x\in k}
           \chi(x)\overline{\chi(x-h)}\psi(tx).
   \tag{1.2}
   \]

   This second operation produces a nonseparable product kernel. Its source weights now depend on both \(h\) and \(t\); that cost remains explicit.

## 2. Exact product argument and complete axis terms

Define

\[
 f_\chi(y)=\chi(y)\overline{\chi(y-1)},\qquad
 S_\chi(z)=\sum_{y\in k}f_\chi(y)\psi(zy),\qquad
 K_\chi(z)=q^{-1/2}S_\chi(z).
\]

**Theorem 1.** The complete joint kernel is

\[
 T_\chi(h,t)=
 \begin{cases}
 S_\chi(ht),&h\ne0,\\
 q-1,&h=t=0,\\
 -1,&h=0,\ t\ne0.
 \end{cases}
 \tag{2.1}
\]

Moreover \(S_\chi(0)=-1\), so \(T_\chi(h,0)=-1\) for every nonzero \(h\).

**Proof.** For \(h\ne0\), substitute \(x=hy\). The two factors \(\chi(h)\) cancel. At \(h=0\), the product is the indicator of \(x\ne0\), whose additive transform gives the stated values. Finally, \(y\mapsto y/(y-1)\) maps \(k\setminus\{1\}\) bijectively to \(k\setminus\{1\}\); character orthogonality gives \(S_\chi(0)=-1\). Every excluded point has its original zero value. □

These axis terms are not synonymous with the global pair diagonal. A nonzero Eisenstein shift can vanish modulo a row prime. Nor does the same-sixth-power-free-core exclusion remove every local \(h=0\) term.

For comparison, if the local multiplicative character is principal but still zero-extended, then

\[
 S_1(z)=
 \begin{cases}q-2,&z=0,\\-1-\psi(z),&z\ne0.\end{cases}
 \tag{2.2}
\]

That reducible case must be separated. It is not covered by the nontrivial-character hypergeometric result.

## 3. Exact hypergeometric identification

Set \(G(\chi)=\sum_{v\in k^\times}\chi(v)\psi(v)\), so \(|G(\chi)|^2=q\). Use the normalization

\[
 H_\chi(z)=\frac1q
 \sum_{\substack{r,s,v\in k^\times\\rs/v=z}}
       \chi(v)\psi(r+s-v),\qquad z\ne0.
 \tag{3.1}
\]

This is \(\operatorname{Hyp}(z;\{1,1\},\{\bar\chi\};\psi)\) in FKMS §9.6. The denominator character is \(\bar\chi\), because the sum conjugates the denominator-list character.

**Theorem 2.** For every \(z\ne0\),

\[
 \boxed{\quad qH_\chi(z)=\bar\chi(-1)G(\chi)S_\chi(z).\quad}
 \tag{3.2}
\]

Thus

\[
 K_\chi(z)=\varepsilon_\chi^{-1}H_\chi(z),\qquad
 \varepsilon_\chi=\bar\chi(-1)G(\chi)/\sqrt q,
 \quad |\varepsilon_\chi|=1.
 \tag{3.3}
\]

**Proof.** Eliminate \(v=rs/z\) in (3.1). Then

\[
 qH_\chi(z)=\bar\chi(z)
 \sum_{r,s\ne0}\chi(r)\chi(s)
                   \psi\bigl(r+s(1-r/z)\bigr).
\]

The \(s\)-sum is \(G(\chi)\bar\chi(1-r/z)\), including its zero when \(r=z\). Consequently

\[
 qH_\chi(z)=G(\chi)
      \sum_r\chi(r)\bar\chi(z-r)\psi(r).
\]

Substitute \(r=zy\) and use \(\bar\chi(1-y)=\bar\chi(-1)\bar\chi(y-1)\). This is (3.2). □

The identity is a complete finite-sum calculation. It does not infer higher rank from a numerical matrix rank. The two notions are different: the sheaf has generic rank two, while the finite \((h,t)\)-matrix below has rank \(q-1\).

## 4. Rank, conductor, and the precise imported bilinear consequence

The lists \(\{1,1\}\) and \(\{\bar\chi\}\) are disjoint. Type \((2,1)\) has no common divisor allowing Kummer induction and cannot be Belyi-induced in the criterion of FKMS §9.6. For prime \(q>3\), FKMS Theorem 9.1 therefore supplies an infinite gallant geometric monodromy group. A constant phase twist (3.3) changes no geometric monodromy.

The standard local data are rank two, lisse on \(\mathbb G_m\), tame at zero, and Swan conductor one at infinity. Under the convention \(c_{\rm an}=\operatorname{rank}+\#\operatorname{Sing}(\mathbb P^1)+\sum\operatorname{Swan}\), the analytic conductor is therefore \(2+2+1=5\). These local-data facts are imported from the hypergeometric construction, as summarized in Katz–Rojas-León–Tiep §1; they are not certified by the finite checker. The needed FKMS hypothesis is bounded complexity, independently of this numerical conductor convention.

For separated complex arrays \(\alpha_h,\beta_t\) supported on integer intervals \(h\sim H,t\sim T\), with \(1\le H,T\le q/2\), \(H\ge q^\delta\), and \(HT\ge q^{3/4+\delta}\), FKMS Theorem 1.1 gives

\[
 \sum_{h\sim H}\sum_{t\sim T}\alpha_h\beta_tK_\chi(ht)
 \ll_\delta \|\alpha\|_2\|\beta\|_2(HT)^{1/2-\eta}
 \tag{4.1}
\]

for some \(\eta>0\). The complexity is bounded in this family. This is an imported theorem applied to an explicitly identified kernel, not a new proof of (4.1).

The finite-field identities also hold over \(\mathbb F_{p^2}\), but (4.1) is not automatically a theorem about two-dimensional Eisenstein boxes or composite conductors. Those interfaces remain to be proved or supplied by an appropriate theorem. In particular, an inert prime's residue-field size is \(p^2\), not \(p\).

## 5. The complete local dilation spectrum

**Theorem 3.** For \(h,k\in k^\times\),

\[
 \boxed{\quad
 \sum_{t\ne0}\overline{S_\chi(th)}S_\chi(tk)
   =q^2\mathbf1_{h=k}-q\chi(h/k)-(q+1).
 \quad}
 \tag{5.1}
\]

**Proof.** Add the \(t=0\) term, which equals one, and apply additive orthogonality:

\[
 \sum_{t\in k}\overline{S_\chi(th)}S_\chi(tk)
 =q\sum_{y\in k}\overline{f_\chi((k/h)y)}f_\chi(y).
\]

If \(h=k\), the inner sum is \(q-2\). Otherwise put \(a=k/h\). On its original support the integrand is

\[
 \bar\chi(a)\chi(ay-1)\bar\chi(y-1).
\]

The full Möbius substitution \(y\mapsto(ay-1)/(y-1)\) maps \(k\setminus\{1\}\) bijectively onto \(k\setminus\{a\}\). Its full character sum, after multiplication by \(\bar\chi(a)\), is \(-1\). The original point \(y=0\) must then be removed; its substituted value is \(\bar\chi(a)\). The inner sum is therefore \(-1-\bar\chi(a)\). Subtracting the \(t=0\) term proves (5.1), including the diagonal. □

Let \(\mathcal S_\chi b(t)=\sum_{h\ne0}S_\chi(th)b(h)\), with counting-measure norms. Then

\[
 \|\mathcal S_\chi b\|_2^2
 =q^2\|b\|_2^2
   -q\left|\sum_h b(h)\bar\chi(h)\right|^2
   -(q+1)\left|\sum_h b(h)\right|^2.
 \tag{5.2}
\]

The singular values of \(\mathcal S_\chi\) are \(q\) with multiplicity \(q-3\), \(\sqrt q\) on the input \(\chi\)-mode, and \(1\) on the constant mode. In particular the finite product matrix has full rank \(q-1\), and all distinct nonzero dilations have bounded correlations after the \(q^{-1/2}\) normalization.

Write \(P_1,P_\chi\) for the orthogonal projections onto the constant and \(\chi\)-vectors. For \(B_\chi=\mathcal S_\chi/q\),

\[
 B_\chi^*B_\chi
 =I-(1-q^{-2})P_1-(1-q^{-1})P_\chi.
 \tag{5.3}
\]

After removing the constant input, the paired \(\chi,\bar\chi\) channels give a uniformly stable map when \(\chi\ne\bar\chi\); the separate [local-operator note](../local_operator/TWO_CHANNEL_LOCAL_ADAPTER.md) develops that reconstruction and its CRT accounting. A single channel is invertible but loses \(q^{1/2}\) in the nonconstant exceptional mode, so omitting this defect would be a material normalization error.

## 6. The source adapter retains all arithmetic weights

For any complex joint weight \(W(h,x)\), define

\[
 \widehat W(h,t)=\sum_{x\in k}W(h,x)\psi(-tx).
\]

Finite Fourier inversion gives exactly

\[
 \sum_{h,x}W(h,x)\chi(x)\bar\chi(x-h)
 =\frac1q\sum_{h,t}\widehat W(h,t)T_\chi(h,t).
 \tag{6.1}
\]

One obtains the actual native weights by grouping the original tuples by the residue of \(h=A_0p-B_0b\) and \(x=A_0p\), leaving every Möbius sign, prime restriction, other local character, smooth cutoff, and gcd condition inside \(W\). This is exact finite regrouping. The prime variable is still prime; a residue completion is not a license to replace its coefficient by the constant one.

The off-axis part of (6.1) is

\[
 q^{-1/2}\sum_{h,t\ne0}\widehat W(h,t)K_\chi(ht).
 \tag{6.2}
\]

The axes are supplied exactly by (2.1). The coefficient \(\widehat W(h,t)\) is in general joint and arithmetically complicated. Formula (4.1) cannot be applied to it as if it were \(\alpha_h\beta_t\). The source-dependent decomposition cost, the local-axis aggregate, and the prime-power/composite/archimedean interfaces are therefore remaining mathematical obligations. The [weighted transfer note](../transfer/WEIGHTED_ADAPTER.md) records that cost explicitly.

**A useful new research target.** Prove that the native completed joint weight has a sufficiently inexpensive decomposition into separated rectangular pieces, or prove cancellation for its actual arithmetic dependence directly. The kernel needed for such an estimate is now explicit, has its two exceptional local modes identified, and satisfies a verified external bilinear interface at split prime moduli.

### Alternative to nuclear-norm separation: the difference-of-ratios input

FKMS v2, immediately after Remark 1.5 (PDF page 6), also states a power saving for

\[
 \sum_{m_1,m_2\sim M}\alpha_{m_1}\alpha_{m_2}
 \sum_{n_1,n_2\sim N}K(m_1^{-1}n_1-m_2^{-1}n_2)
 \ll \|\alpha\|_2^2 MN^2(MN)^{-\eta},
 \tag{6.3}
\]

when \(q^{1/6+\delta}\le M\le q^{1/2-\delta}\) and
\(MN^2\ge q^{1/2+\delta}\). This is an unnumbered consequence attributed to
Xi–Zheng and FKMS Proposition 1.5, not a separately proved result of this packet.
Formula (6.3) preserves the printed coefficient pattern: no conjugate on the
second \(\alpha\), and no arbitrary coefficients on either \(n\)-sum. The PDF
was visually checked; this is not an HTML transcription assumption.

The affine expression can formally be written
\(A_0p-B_0b=m_1^{-1}n_1-m_2^{-1}n_2\), with
\((m_1,m_2,n_1,n_2)=(A_0^{-1},B_0^{-1},p,b)\). This only matches its argument:
inverse affine coefficients need not range over the required intervals, the
prime and Möbius weights remain on \(n_1,n_2\), and (6.1) still carries its
joint completed weight and frequency \(t\). Moreover the original phase is
\(\chi(A_0p)\bar\chi(B_0b)\), not \(K(A_0p-B_0b)\).

Xi–Zheng's actual §3.1 shifts the numerator variables and uses their smooth
weights to separate the new averaging parameter. An arbitrary Möbius weight
on a shifted numerator does not have that property. Removing it by
Cauchy–Schwarz creates sums of products of two difference kernels with four
denominator variables; (6.3) alone does not estimate that new expression.
Thus preserving the additive relation and proving the requisite weighted
shift estimate is a credible alternative next step, but no application to
the native coefficient is asserted here.

## 7. Verification and scope

Run from this directory:

```sh
python -I -S -B verify.py --output CHECKS.json
```

The checker uses exact integer arithmetic in \(\mathbb Q(\zeta_6,\zeta_p)\), with no floating-point tolerances. It covers both sextic orientations in \(\mathbb F_7,\mathbb F_{13},\mathbb F_{19},\mathbb F_{31},\mathbb F_{25},\mathbb F_{49}\). It directly checks (2.1), every dilation ratio in (5.1), the complete double-sum identity (3.2), signed-weight completion, the exceptional singular modes, and finite autocorrelation reconstruction. Wrong mask, conjugation, and axis controls are rejected.

The count in [CHECKS.json](CHECKS.json) counts finite identity predicates, including all small-field \((h,t)\) pairs; it is not a count of analytic theorems. The arguments above establish the elementary identities over all finite fields. Hypergeometric geometry and (4.1) remain explicitly attributed external inputs. No global arithmetic saving is inferred from a finite computation.

## Sources

1. [GettysburgResearch/riemann #1022, exact affine source](https://github.com/GettysburgResearch/riemann/blob/8b2c6d50ad2d729c681745717c615095bd8f1d9d/standalone/2026-10-25-hlc-zero-free-transfer/fourth-pass/OFF_DIAGONAL_TRANSFER.md). Inspected directly; source formulas (15)–(18).
2. É. Fouvry, E. Kowalski, Ph. Michel, W. Sawin, [Bilinear forms with trace functions](https://arxiv.org/html/2511.09459v2), §9.6 and Theorems 9.1, 1.1. These specific statements were read directly in both v1 and v2 HTML; v2 is the reference used here. The fetched HTML displays manuscript date August 24, 2026; the [arXiv v2 PDF](https://arxiv.org/pdf/2511.09459v2) displayed December 9, 2025 and was also checked for the unnumbered quadrilinear statement on page 6. The separate [author PDF](https://people.math.ethz.ch/~kowalski/bilinear-forms.pdf) displayed November 14, 2025. These endpoints are not represented as byte-identical snapshots.
3. N. M. Katz, A. Rojas-León, P. H. Tiep, [A rigid local system with monodromy group the big Conway group 2.Co1 and two others with monodromy group the Suzuki group 6.Suz](https://web.math.princeton.edu/~nmk/krlt3pub.pdf), Transactions AMS 373 (2020), 2007–2044, §1, especially page 2008 and Corollary 1.3. Used only for the stated standard hypergeometric local data and primitivity context.
4. P. Xi, J. Zheng, [On the Brun–Titchmarsh theorem. II](https://arxiv.org/html/2504.12692v3), equations (1.3), (2.7), and §3.1. Inspected only to identify which variables carry coefficients and which are shifted in the method behind (6.3); no weighted generalization is imported.

No exhaustive literature search or priority claim is made for the finite character identities.
