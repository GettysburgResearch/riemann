# Unconditional Bergman closure of Noor's generators and the critical endpoint

Researcher: `li_advocate`; 2026-11-17. Status: explicit function-space proof independently checked by the parent and by `li_skeptic`; durable independent review: `audits/adversarial_reviews/noor_critical_bergman_skeptic_round4.md`. Novelty unassessed. This is not an RH result.

## Statement

Let \(D_\beta=\{f=\sum_{n\ge0}f_nz^n:\sum(n+1)^\beta|f_n|^2<\infty\}\), and
\[
h_k(z)=\frac1{1-z}\log\frac{1+z+\cdots+z^{k-1}}k,
\qquad \mathcal N=\operatorname{span}\{h_k:k\ge2\}.
\]
Then, unconditionally,
\[
\overline{\mathcal N}^{D_{-1}}=D_{-1}.
\tag{NOOR-A402}
\]
In particular 1 belongs to this norm closure. The proof does not assert norm convergence of the particular Möbius partial sums below. It uses their boundedness and weak convergence.

Primary formulas: Noor arXiv:1809.09577v4, p6 and pp7–8, **PAPER-NOOR-A001**. The primary arithmetic dependency is the classical **PAPER-M001**, Titchmarsh1986, Theorem3.13 and its displayed Perron errors, printedpp62–63 (PDF36), independently read and visually checked by this researcher and `li_skeptic`. With `c=1/log x`, `T=exp((log x)^(1/10))`, and `delta=A(log x)^(-9/10)`, those errors at `s=1`, `x=N+1/2`, give `A_N=O(poly(log N)exp(-c_0(log N)^(1/10)))`, hence every fixed log-power decay. Its earlier zero-free-region and Perron inputs remain accepted classical dependencies. Exact image: `sources/logarithmic_riesz_priority_skeptic_round4/titchmarsh_p62_63_skeptic.png`; durable reconstruction: `audits/adversarial_reviews/noor_critical_bergman_skeptic_round4.md`.

The second scalar estimate follows directly: writing `A(t)=sum_(n<=t)mu(n)/n`, partial summation gives `(1/zeta(1+h))/h=integral_1^infinity A(t)t^(-h-1)dt` for `h>0`. Dominated convergence, using integrability of `|A(t)|/t`, and the simple pole at1 give `integral_1^infinity A(t)/t dt=1`. The exact identity `B_N=A_N logN−integral_1^N A(t)/t dt` then gives `B_N+1=A_N logN+integral_N^infinity A(t)/t dt`, also smaller than every fixed reciprocal logarithm. This is the stable-source route used for the proof.

An optional alternative quantitative arithmetic input, not required for that route, is Lee–Leong arXiv:2208.06141v5, Theorem 1.1, p2, equation (9), **PAPER-A008 / THM-A008-MERTENS**:
\[
|M(x)|<33.56x(\log x)\exp\{-\sqrt{(\log x)/5.56}\},
\quad x\ge\exp(4589.20),\quad M(x)=\sum_{n\le x}\mu(n).
\tag{M}
\]
That exact statement was read in the actual primary PDF and visually checked by this researcher and `analytic_frontier`; its full proof and computational constants have **not** been audited here. The source record preserves a withdrawn v3 and subsequent replacement history; no audit of those revisions or allegation about v5 is made here. See `audits/mobius_quantitative_source_analytic_round4.md`. Any classical unconditional bound \(M(x)\ll_K x(\log x)^{-K}\) for every fixed \(K\) would suffice. Bare \(M(x)=o(x)\) supplies no rates adequate for the boundedness estimate below.

## 1. Optional alternative derivation from a Mertens bound

The elementary comparison \(u^A e^{-\sqrt{u/5.56}}\to0\) implies from (M)
\(M(x)=O_K(x(\log x)^{-K})\) for every fixed \(K\), as \(x\to\infty\). Partial summation then shows that \(\sum\mu(k)/k\) and \(\sum\mu(k)\log k/k\) converge. Their values are 0 and −1: for real \(s>1\), the absolutely convergent identities are
\[
\sum\mu(k)k^{-s}=1/\zeta(s),\qquad
\sum\mu(k)(\log k)k^{-s}=\zeta'(s)/\zeta(s)^2,
\]
and Abelian convergence permits \(s\downarrow1\). The Laurent expansion \(\zeta(s)=(s-1)^{-1}+O(1)\) gives the stated limits. In detail, the Mertens bound also justifies convergence and differentiation limits through the associated partial-summation integrals; no RH input is used.

Set
\(A_N=\sum_{k\le N}\mu(k)/k\), \(B_N=\sum_{k\le N}\mu(k)\log k/k\).
The tail identities give, for every fixed \(K\),
\[
A_N=O_K((\log N)^{-K}),\qquad B_N+1=O_K((\log N)^{-K}).
\tag{1}
\]
For example, bounding \(M(t)/t\) by \((\log t)^{-K-3}\) in the two tail integrals suffices. These are asymptotic statements; the large numerical starting point in (M) has no effect on the finitely many smaller partial sums.

## 2. Exact coefficients and uniform tail estimate

Put \(H_0=0\), \(H_n=\sum_{j=1}^n1/j\). Noor's coefficient formula is
\[
c_n(k):=[z^n]h_k=H_n-H_{\lfloor n/k\rfloor}-\log k.
\tag{2}
\]
For \(n\ge k\), let \(m=\lfloor n/k\rfloor\ge1\). The elementary inequalities
\(H_j=\log j+\gamma+\epsilon_j\), \(0\le\epsilon_j\le1/j\), and \(m\ge n/(2k)\) yield
\[
|c_n(k)|\le\log\frac{n}{km}+\frac1n+\frac1m
\le\frac2m+\frac1n\le\frac{5k}{n}.
\tag{3}
\]
The logarithm estimate uses \(0\le n-km<k\) and \(\log(1+u)\le u\). The constant is deliberately loose. Each \(h_k\) therefore belongs to \(D_{-1}\) (indeed to \(H^2\)).

Define
\[
V_N=\sum_{k=2}^N\frac{\mu(k)}k h_k;
\]
we may include \(k=1\) because \(h_1=0\). For \(1\le n\le N\), the divisor identity gives
\[
\sum_{k\le N}\frac{\mu(k)}k H_{\lfloor n/k\rfloor}
=\sum_{m\le n}\frac1m\sum_{k\mid m}\mu(k)=1.
\]
Consequently
\[
[z^0]V_N=-B_N,\qquad
[z^n]V_N=A_NH_n-1-B_N\quad(1\le n\le N).
\tag{4}
\]
For \(n>N\), (3) gives the distinct estimate
\[
|[z^n]V_N|\le\sum_{k\le N}\frac{|\mu(k)|}{k}\frac{5k}n
\le\frac{5N}n.
\tag{5}
\]
This bound only applies in that tail, where every \(k\le N\) also satisfies \(k<n\).

## 3. Boundedness and weak convergence, not claimed norm convergence

The central part of \(V_N-1\) satisfies, using \(H_n\le1+\log n\),
\[
\sum_{n=0}^N\frac{|[z^n](V_N-1)|^2}{n+1}
\ll |A_N|^2(1+\log N)^3+|B_N+1|^2(1+\log N)\to0
\tag{6}
\]
by (1). Meanwhile the tail is uniformly bounded:
\[
\sum_{n>N}\frac{|[z^n]V_N|^2}{n+1}
\le25N^2\sum_{n>N}\frac1{n^3}
\le\frac{25}{2}.
\tag{7}
\]
Thus \(\{V_N\}\) is bounded in the Hilbert space \(D_{-1}\), and (4) implies that every fixed coefficient converges to that of 1. Pairings with polynomials converge, since these are finite coefficient pairings. Polynomial density and the uniform norm bound extend this convergence to pairings with every \(D_{-1}\) vector. Hence
\[
V_N\rightharpoonup1\quad\text{in }D_{-1}.
\]
The norm-closed **linear** subspace \(\overline{\mathcal N}\) is weakly closed (or test against its orthogonal complement). Every \(V_N\) lies in it, so 1 lies in it. Estimate (7) is not a vanishing bound: no norm convergence of \(V_N\) is inferred.

## 4. From the constant to full Bergman density

The norm of \(D_{-1}\) is exactly the normalized unweighted area Bergman norm. Composition \(C_mf=f(z^m)\) is contractive there, because
\[
\|C_mf\|_{D_{-1}}^2=\sum_{n\ge0}\frac{|f_n|^2}{mn+1}
\le\sum_{n\ge0}\frac{|f_n|^2}{n+1}.
\]
Multiplication by \(p_m=1+\cdots+z^{m-1}\) has norm at most \(m\), by its supremum bound and the area integral. Thus \(W_m=M_{p_m}C_m\) is bounded on \(D_{-1}\). The exact analytic identity from Noor p6 remains valid:
\(W_mh_k=h_{mk}-h_m\), with \(h_1=0\).
Therefore \(\overline{\mathcal N}^{D_{-1}}\) is \(W_m\)-invariant. Since it contains 1 it contains all \(p_m=W_m1\), and then all monomials \(z^{m-1}=p_m-p_{m-1}\) for \(m\ge2\), together with 1. Polynomials are dense in \(D_{-1}\), proving (NOOR-A402).

## 5. Exact impact and remaining problem

Gallardo–Gutiérrez–Seco, published2025, Theorem5.5 p26 includes \((\alpha,a)=(-3,1)\), where its asserted approximation is exactly \(1\in\overline{\mathcal N}^{D_{-1}}\). That statement is therefore independently valid by the argument above, consistently with the elementary zero-free half-plane \(\Re s>1\). This supplies a separate proof of the critical case without the false bounded-inverse endpoint in Proposition5.1. It does not validate the proposition itself.

For \(-3<\alpha\le-2\), or \(a>1\) in the later theorem, the weighted target is \((1-z)^{1-a}\); the topology and needed rates differ. Neither weak boundedness in \(D_{-1}\), nor Noor's compact-open result, automatically gives the required special-core property in the stricter weighted graph/range norm. The unresolved precise task is to construct approximants to that target whose images converge in the pulled-back range norm \(\|g/(1-z)^{a-1}\|_{D_\alpha}\), or establish a valid core/density implication for the special arithmetic span. No generic inverse multiplier theorem supplies this automatically. No conclusion against the truth of Theorem5.5 is asserted.

## Reproducibility and status

`experiments/code/noor_exact_identities_advocate_round4.py` checks exact rational basis inner products and divisor-convolution coefficients; these checks support the identities but do not replace the infinite-dimensional estimates above. Source audit: `audits/adversarial_reviews/noor_source_and_unitary_advocate_round4.md`. External theorem (M) is a stated primary-source input, not a newly verified Mertens theorem. The new proof is offered as a scoped mathematical reconstruction with novelty unassessed, and is independently reviewed only within the stated function-space and external-dependency scope.
