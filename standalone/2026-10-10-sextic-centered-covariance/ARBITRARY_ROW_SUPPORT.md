# Exact reunited-divisor support for arbitrary nonzero rows

**Status:** source-conditional analytic addendum, proposed for independent review. The exact support cutoff extends to every nonzero Eisenstein row, including repeated prime factors, units, and arbitrary valuations at the fixed bad primes. This extension needs no mixed outer Gauss-sum cancellation. It supplies exact support structure only; the quantitative coupled mean-square bounds in the companion notes remain restricted to squarefree primary rows.

**Inputs:** the imported October 5 source at OpenAI/math commit adc7f1241b42e322a6451854ab7e4b4c146bf78a, specifically eq:completed-twist, eq:theta-row-twist and its fixed bad-prime discussion, eq:theta-local-factors, and Proposition lem:reflection; and the generic finite-cusp reflection and kernel composition in reunited_cusp_cutoff.md, SHA-256 89cd204ae66ef615e7d630bf2c1e5524e134b76e30789dce7796a229e53a4340, Lemmas 1.1–2.2. This is a separate extension and does not modify those frozen files.

## 1. Original object and the row's literal zero extension

Let \(S\) be the source's fixed finite bad set, containing the primes above \(6\), and let \(\xi\) be a fixed finite-order ray character supported on \(S\). For every \(k\in\mathcal O\setminus\{0\}\) and every squarefree primary \(a\) outside \(S\), use the original completion

\[
T(B;k,a)=T(B;\Psi_{k,a}),\qquad
\Psi_{k,a}(n)=\xi(n)\chi_n(k)\chi_n(a)^4
\quad ((n,S)=1),
\]

with the source's zero extension at \(S\). Its full squarefree/cube sum and the compact original test \(V_*\) are retained.

The coupled outer coefficient is

\[
a_\xi(a)\chi_a(k)W_1(Na/A)/\sqrt A.
\]

It is identically zero if \((a,k)>1\), even when \(k\) is not squarefree. It is therefore enough to discuss \((a,k)=1\). No formula simplifying the product of this outer coefficient and the first-reflection scalar is required below.

Write

\[
k=u\,k_S k_{\rm good},
\]

where \(u\) is a unit, \(k_S\) is supported on \(S\), and \(k_{\rm good}\) is a product of chosen primary prime generators outside \(S\), with their actual positive exponents.

For every good row prime \(p\mid k_{\rm good}\), set

\[
j_p\equiv v_p(k)\pmod6,\qquad 0\le j_p\le5.
\]

After the source's fixed ray splitting, the completed twist has the form

\[
\Psi_{k,a}(n)=
\Psi_{0,k}(n)
\prod_{p\mid k_{\rm good}}\chi_p^{j_p}(n)
\prod_{p\mid a}\chi_p^4(n).                            \tag{1.1}
\]

The products are over distinct primes. In particular, when \(v_p(k)\) is a positive multiple of six, the factor in (1.1) is

\[
\chi_p^0(n)=\mathbf1_{p\nmid n}.                        \tag{1.2}
\]

It is not the constant function one. The original \(\chi_n(k)\) vanishes when \(p\mid n\), and the mask (1.2) retains that zero. The same convention applies to the cube terms of the completion.

The family \(\Psi_{0,k}\) is fixed and finite. Here is the precise dependence used. The good-prime reciprocity contribution is a character on the source's fixed ray group and depends on \(k_{\rm good}\) only through that finite group. The unit \(u\) has six possibilities. On the initial support \((n,S)=1\), each \(\chi_n(p_S)\), \(p_S\in S\), has sixth power one, so the exponent of \(p_S\) in \(k_S\) can be reduced modulo six without losing a zero: no initial denominator \(n\) or cube index \(b\) is divisible by \(p_S\). The source's fixed bad-prime reciprocity interface places these fixed-numerator factors in ray characters supported on \(S\). Their finitely many powers have a common fixed period. This is exactly the finite-family assertion accompanying eq:theta-row-twist in the imported source.

Thus arbitrarily large bad-prime valuations do not enlarge the fixed initial ray family. The argument uses reduction modulo six at bad primes only on the already excluded initial support; it does not discard the good-prime masks (1.2).

## 2. Freeze the first reflection before extracting negative divisor choices

Apply the general source reflection to (1.1). All primes of \(a\) have exponent four and are active. Let \(\mathcal R\) be the set of active good row primes in a fixed first-reflection branch, and write

\[
r=\prod_{p\in\mathcal R}p.
\]

Then

\[
\{p\mid k_{\rm good}:j_p\ne0\}
\subseteq\mathcal R
\subseteq\{p:p\mid k_{\rm good}\},
\]

and the first denominator is

\[
c=c_0ra,                                               \tag{2.1}
\]

where \(c_0\) is in a fixed finite family. Only row primes with \(j_p=0\) can be inactive.

For the raw frequency \(x=\lambda^4\ell\), retain the full row multiplier

\[
\mathcal B_{\mathcal R}(x)
=\prod_{p\in\mathcal R}B_{p,j_p}(x).                    \tag{2.2}
\]

Every factor is periodic modulo \(p\). In particular,

\[
B_{p,0}(x)=(Np)^{-1/2}\chi_p(x)^{-2},
\]

\[
B_{p,4}(x)=(Np)^{-1/2}
[-1+Np\,\mathbf1_{p\mid x}],
\]

and \(B_{p,j}(x)=\chi_p(x)^{-j-2}\) for the other exponents. All character powers retain their nonunit zeros. The row factors with \(j_p=4\) are left inside (2.2); they are not assigned to the divisor label introduced next.

An inactive \(j_p=0\) row prime contributes its zero-frequency Fourier factor to the first-reflection scalar. Its absence from (2.2) is the original active/inactive decomposition of the mask (1.2), not deletion of that mask.

Now reunite only the Ramanujan factors belonging to the outer divisor \(a\):

\[
\prod_{p\mid a}(Np)^{-1/2}
[-1+Np\,\mathbf1_{p\mid x}]
=\sum_{hg=a}\mu(g)\sqrt{Nh/Ng}\,\mathbf1_{h\mid x}.      \tag{2.3}
\]

The squarefree factors \(h,g\) are coprime. Both positive squarefree/cube possibilities stay inside \(h\). No condition \((g,x)=1\) is imposed.

Freeze \(k,a\), the first-reflection branch, and a factorization \(a=hg\). Its reunited contribution is a scalar independent of \(\ell\) times

\[
\mu(g)\sqrt{Nh/Ng}\,
S_{F_\sigma,P_{k,h,\mathcal R},\,\mathsf JV_*}(X),
\]

where the raw-frequency sum \(S\) is the one defined in the frozen cutoff note, and

\[
X=\frac{N(c_0)^2(Nr)^2(Nh)^2(Ng)^2}{B},                 \tag{2.4}
\]

\[
P_{k,h,\mathcal R}(x)=
\psi(x)\mathcal B_{\mathcal R}(x)\mathbf1_{h\mid x}
\Pi(x).                                                \tag{2.5}
\]

Here \(\Pi=1\) retains the complete cusp spectrum; a prescribed fixed periodic bad-prime projection is also allowed. The source's additive character \(\psi\) has a fixed finite period. Since the initial ray family is fixed and finite, a single fixed \(S\)-supported \(M\) contains all periods of \(\psi,\Pi\). Therefore

\[
P_{k,h,\mathcal R}\ \text{is periodic modulo }q=Mrh,
\qquad Nq=N(M)NrNh.                                    \tag{2.6}
\]

This multiplier need not have modulus at most one: active row factors of exponent four can be large. The generic reflection accepts any finite periodic multiplier, and the exact cutoff will use no norm bound for its finite Fourier coefficients.

## 3. Uniform cutoff for every nonzero row

### Theorem 3.1

There is a fixed constant \(C_*>0\), depending only on \(S\), the fixed initial ray data, the chosen projection, and the upper endpoint of \(\operatorname{supp}V_*\), such that every reunited contribution above vanishes identically whenever

\[
\boxed{(Ng)^2>C_*B.}                                   \tag{3.1}
\]

The assertion holds for every nonzero row \(k\in\mathcal O\), with no squarefreeness, primarity, coprimality to \(S\), or row-norm restriction. The original terms with \((a,k)>1\) are already zero. All source cusps and all nonzero theta frequencies are retained.

**Proof.** Apply the generic finite-cusp reflection from reunited_cusp_cutoff.md, Lemma 2.1, to (2.5). Every reduced second denominator \(c_j\) divides \(q=Mrh\), hence

\[
N(c_j)\le N(M)NrNh.
\]

Lemma 2.2 of that note gives the exact outgoing test

\[
\mathsf J_0(\mathsf JV_*)(y)=V_*(27y),
\]

with no residue. The second cusp family has the fixed nonzero frequency gap \(N\ell'\ge1/81\). Inserting (2.4), each outgoing test argument is at least

\[
27\frac{N\ell'\,N(c_0)^2(Nr)^2(Nh)^2(Ng)^2}
{B\,N(c_j)^2}
\ge
\frac{N(c_0)^2}{3N(M)^2}\frac{(Ng)^2}{B}.                \tag{3.2}
\]

The active row radical \(r\) and the positive divisor \(h\) cancel from this lower bound. Let \(v_1=\sup\operatorname{supp}V_*\), and take

\[
C_*=\frac{3N(M)^2v_1}{\min_{c_0}N(c_0)^2}.
\]

Under (3.1), every outgoing test is evaluated strictly beyond its support. Each term of the finite second Fourier expansion is zero, regardless of the size of its coefficients or the number of first-reflection branches. Horizontal differentiation kills the constant modes, and the kernel-composition contour lies inside the previously proved pole-free strip, so no omitted term remains. This proves exact vanishing.

The finite bad-prime discussion in Section 1 makes \(M\) and the \(c_0\)-family independent of all row valuations. Thus the same constant is uniform for arbitrary nonzero \(k\). Multiplying back the first-reflection scalar and the original outer coefficient preserves zero. No Gauss-sum cancellation of that outer coefficient was used. \(\square\)

### Corollary 3.2. Exact smooth restriction for arbitrary rows

In the full coupled first reflection, multiply each reunited \((h,g)\) block by a fixed smooth function of \(Ng/\sqrt{C_*B}\) that equals one on \([0,1]\) and vanishes on \([2,\infty)\). The full expression is unchanged for every nonzero row \(k\). Only after this exact insertion may the positive \(h\)-choices be split into \(e,f\) or the theta coefficients be divided into norm blocks.

The statement concerns reunited blocks. It does not assert separate vanishing of an individual \((e,f,g)\) component.

## 4. What this extension does and does not supply

The second conductor need only contain the active row radical, the reunited positive divisor, and a fixed bad modulus. This suffices for exact support cancellation even when the first row multiplier is a mixture of all six local exponents.

For squarefree rows outside \(S\), the first-reflection row factors are quadratic and the companion notes exploit additional scalar cancellation to obtain numerical mean-square estimates. For arbitrary rows, factors such as \(B_{p,2}\), \(B_{p,3}\), \(B_{p,4}\), and the active \(B_{p,0}\) remain. This addendum supplies no simultaneous norm estimate for that varying family and no extension of the \(D^{3/4}\) or \(D^{19/24}\) row ranges to nonsquarefree rows.

The new result is the exact all-row cutoff (3.1), including the original zero masks. Completion inversion, the quantitative arbitrary-row family, and centered product-column covariance control remain separate requirements for a full moment theorem.
