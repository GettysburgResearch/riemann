# Unconditional long-row moments and a short-row coefficient obstruction

**Status:** proved partial result and proved counterexample to a stronger coefficient class; no proof or refutation of the requested short-row inverse moment.

**Scope:** the exact sextic row characters over \(K=\mathbb Q(\sqrt{-3})\), with all nonzero Eisenstein-integer rows retained. The long-row result is independent of the imported quasi-Riemann theorem.

**Exact sources:** GettysburgResearch/riemann PR #910, frozen head `670a76c1a3a8f325c43c1755b1cfc24d313a3e3c`; `standalone/2026-10-10-quasi-riemann-height-descent/UPSTREAM_HEIGHT_AND_MOMENTS.md`, Section 7, and `FOURTH_MOMENT_REDUCTION.md`, Proposition 2.1. The original character definition is in the imported October 5 `paper2.tex`, lines 250–263, at OpenAI source commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`.

**What was checked:** the stated character definition, the full algebraic diagonal count, the fixed-prime sixth-power replication, primitive Gauss-sum orthogonality, and elementary lattice Poisson summation. No numerical experiment or zero computation is used.

**Smallest remaining gap:** remove the \(D^{3k+\epsilon}\) off-diagonal error, or replace it by \(HD^{k+\epsilon}\), for the exact Möbius coefficients at \(H=D^{1+\theta}\). The positive-coefficient counterexample shows this cannot be done for arbitrary bounded squarefree coefficients.

## 1. An unconditional general moment estimate

Let \(\mathcal O=\mathbb Z[\omega]\), and take the source's primary generators. For a squarefree ideal \(n\) prime to \(6\), put

\[
\chi_n(u)=(u/n)_6,
\]

with the exact zero extension when \((u,n)\ne1\). Let \(k\ge1\) be a fixed integer, let \(b>0\) be fixed, and let \((a_n)\) be any complex coefficients with \(|a_n|\le1\), supported on squarefree ideals prime to \(6\) with \(Nn\le bD\). Define

\[
F_u=\sum_n a_n\chi_n(u).
\]

Then, for every \(\epsilon>0\), uniformly for \(D\ge2\) and \(H\ge1\),

\[
\boxed{\displaystyle
\sum_{0<Nu\le H}|F_u|^{2k}
\ll_{K,k,b,\epsilon}
HD^{k+\epsilon}+D^{3k+\epsilon}.}
\tag{1.1}
\]

In particular, the requested diagonal-size moment is unconditional in the range

\[
H\ge D^{2k}.
\tag{1.2}
\]

For the exact inverse family, take \(a_n=\mu_K(n)\nu(n)W(Nn/D)\) and rescale by \(\|W\|_\infty\). Fixed bad-prime restrictions only shrink the column support. No uniformity in derivatives of \(W\) is required for (1.1); its support and supremum norm suffice.

### 1.1 A uniform smooth character-sum bound

Choose once and for all a nonnegative radial function \(\Phi\in C_c^\infty(\mathbb C)\) satisfying \(\Phi(z)\ge1\) for \(|z|\le1\). If \(\psi\) is a nonprincipal primitive character of \(\mathcal O/f\), extended by zero, then for every \(T>0\),

\[
\left|\sum_{u\in\mathcal O}\psi(u)\Phi(u/\sqrt T)\right|
\ll_\Phi\sqrt{Nf}.
\tag{1.3}
\]

Here the implied constant is independent of \(T\), the ideal \(f\), and \(\psi\).

To prove (1.3), split the sum into residue classes modulo \(f\) and apply Euclidean lattice Poisson summation. The ideal lattice \(f\) is a rotation and dilation of the fixed Eisenstein lattice. A primitive character has zero Gauss sum at frequency zero and Gauss sums of absolute value at most \(\sqrt{Nf}\) at every frequency. Consequently, after absorbing fixed covolume and dual-lattice constants,

\[
|S_f(T)|\ll_\Phi
\frac{T}{\sqrt{Nf}}
\sum_{0\ne v\in\mathcal O}
\left(1+\sqrt{T/Nf}\,|v|\right)^{-A}
\tag{1.4}
\]

for any fixed \(A>2\). The nonzero-frequency condition is essential. For every \(r>0\), lattice counting gives

\[
\sum_{0\ne v\in\mathcal O}(1+\sqrt r\,|v|)^{-A}
\ll_A r^{-1}.
\tag{1.5}
\]

For \(r\le1\), this follows by comparison with the planar integral, together with a bounded central contribution. For \(r\ge1\), the sum is \(O_A(r^{-A/2})\), which is \(O_A(r^{-1})\). Substitution of \(r=T/Nf\) proves (1.3).

Now let \(q=fq_0\) be squarefree, with \((f,q_0)=1\), and consider the imprimitive zero-extended function

\[
\psi(u)\mathbf 1_{(u,q_0)=1}.
\]

By inclusion–exclusion and the substitution \(u=dv\),

\[
\sum_u\psi(u)\mathbf1_{(u,q_0)=1}\Phi(u/\sqrt H)
=\sum_{d\mid q_0}\mu_K(d)\psi(d)
\sum_v\psi(v)\Phi(v/\sqrt{H/Nd}).
\tag{1.6}
\]

The radiality of \(\Phi\) removes the rotation from multiplication by the primary generator of \(d\). Estimate (1.3), valid even for \(H/Nd<1\), yields

\[
\left|\sum_u\psi(u)\mathbf1_{(u,q_0)=1}\Phi(u/\sqrt H)\right|
\ll_\Phi d_K(q_0)\sqrt{Nf}
\ll_{\Phi,\epsilon}(Nq)^\epsilon\sqrt{Nf}.
\tag{1.7}
\]

This treats imprimitive masks explicitly; it does not silently replace an imprimitive character by its primitive part.

### 1.2 Moment expansion and exact local characters

By positivity,

\[
\sum_{0<Nu\le H}|F_u|^{2k}
\le\sum_{u\in\mathcal O}\Phi(u/\sqrt H)|F_u|^{2k}.
\tag{1.8}
\]

Expand the right-hand side over squarefree tuples

\[
(n_1,\ldots,n_k,m_1,\ldots,m_k).
\]

Let

\[
e_p=\sum_i v_p(n_i)-\sum_jv_p(m_j),\qquad
q=\operatorname{rad}\!\left(\prod_i n_i\prod_jm_j\right).
\]

At each prime \(p\mid q\), the row factor is \(\chi_p(u)^{e_p}\) on units, and is zero at multiples of \(p\). If \(e_p\not\equiv0\pmod6\), this is a nontrivial primitive character modulo the prime ideal \(p\). If \(e_p\equiv0\pmod6\), it is the principal mask \(\mathbf1_{p\nmid u}\). Therefore the full row factor is exactly the function in (1.6), where

\[
f=\prod_{\substack{p\mid q\\e_p\not\equiv0\ (6)}}p,
\qquad q_0=q/f.
\tag{1.9}
\]

If \(f\ne1\), the primitive character is nonprincipal and (1.7) applies. Since

\[
Nq\le\prod_iNn_i\prod_jNm_j\le(bD)^{2k},
\]

the corresponding row sum is \(O_{k,b,\epsilon}(D^{k+\epsilon})\). There are \(O_{k,b}(D^{2k})\) tuples. Their total absolute contribution is consequently

\[
O_{k,b,\epsilon}(D^{3k+\epsilon}).
\tag{1.10}
\]

### 1.3 Principal tuples

When \(f=1\), all local exponent differences are multiples of six. These are precisely the full algebraic sextic diagonals in Proposition 2.1 of `FOURTH_MOMENT_REDUCTION.md`. Their number is \(O_{k,b,\epsilon}(D^{k+\epsilon})\), also for support \(Nn\le bD\) without a positive lower cutoff.

For completeness, attach to each occurring prime its incidence pattern \((I,J)\) among the left and right factors. Every permitted nonempty pattern has total multiplicity \(m_{I,J}=|I|+|J|\ge2\), because \(|I|-|J|\equiv0\pmod6\). If \(q_{I,J}\) is the product of primes with that pattern, then

\[
\prod_{I,J}(Nq_{I,J})^{m_{I,J}}
\le(bD)^{2k},\qquad
\prod_{I,J}Nq_{I,J}\le(bD)^k.
\]

There are only finitely many patterns for fixed \(k\). The ideal divisor bound and ideal counting thus bound their total choices by \(D^{k+\epsilon}\). This includes all extra sixth-power quotient diagonals for \(k\ge6\).

Each principal row sum is at most \(\sum_u\Phi(u/\sqrt H)\ll H\) for \(H\ge1\). This gives the first term of (1.1), while (1.10) gives the second. The argument also covers the unit ideal and the possible \(u=0\) contribution in the positive majorant. This proves (1.1).

## 2. A genuine obstruction to arbitrary bounded coefficients

The preceding long-row result cannot simply be strengthened to the desired short-row result for arbitrary bounded squarefree coefficients.

Fix a smooth nonnegative function \(W\), supported in a fixed compact interval of \((0,\infty)\), and positive on a nonempty subinterval. Set

\[
C_u(D)=\sum_{(n,6)=1}\mu_K(n)^2\chi_n(u)W(Nn/D).
\tag{2.1}
\]

Let \(H=D^h\) with fixed \(h>0\), and put \(Y=H^{1/6}\). For prime ideals \(p\nmid6\) with \(Y/2<Np\le Y\),

\[
C_{p^6}(D)
=\sum_{\substack{(n,6)=1\\p\nmid n}}\mu_K(n)^2W(Nn/D).
\tag{2.2}
\]

The ordinary squarefree ideal density gives

\[
\sum_{(n,6)=1}\mu_K(n)^2W(Nn/D)=c_{K,W}D+o(D),
\qquad c_{K,W}>0.
\]

The discarded multiples of \(p\) are at most \(O_W(D/Np)\), uniformly when \(Np\le bD\), and are absent when \(Np>bD\). Hence (2.2) is at least \(cD\) for all these primes once \(D\) is large. The classical prime ideal theorem supplies \(\gg Y/\log Y\) such primes. Their sixth powers are distinct permitted rows. Therefore

\[
\boxed{\displaystyle
\sum_{0<Nu\le D^h}|C_u(D)|^{2k}
\gg_{K,W,k,h}\frac{D^{2k+h/6}}{\log D}.}
\tag{2.3}
\]

The bound \(D^{k+h+\epsilon}\), for every \(\epsilon>0\), is impossible if

\[
k>\frac{5h}{6}.
\tag{2.4}
\]

In particular, for \(h=1+\theta\) with \(0<\theta\le1/10\), it is false for **every** integer \(k\ge1\).

This is directly relevant to attempted extensions of the inverse theorem by arbitrary residual coefficients: a residual coefficient equal to \(\mu_K(n)\overline{\nu(n)}\) would cancel the inverse coefficient and produce (2.1). The counterexample uses the very sixth-power rows needed for principal-member extraction, so excluding those rows would change the requested theorem.

There is a quantitative method barrier. An all-row diagonal-size theorem uniform for arbitrary bounded squarefree coefficients can only hold when \(h\ge6k/5\). Inserting that necessary condition into the already proved prime-extraction exponent gives

\[
\alpha=\frac12+\frac{5h}{12k}\ge1.
\tag{2.5}
\]

Thus **no diagonal-size theorem with this arbitrary coefficient scope, on any power-law row range, can yield a nontrivial principal-member cancellation exponent through the stated extraction**. This conclusion is a rigorous scope obstruction, not a statement that the exact inverse theorem is false.

## 3. Consequence for the present research target

No counterexample to the exact Möbius moment has been found in this audit. The algebraic diagonal has the appropriate size at every fixed \(k\), and higher sixth-power quotient diagonals do not destroy that size. Formula (1.1) proves a genuine generalized moment result, but only reaches diagonal size at a row length growing with \(k\). It therefore does not yield the source's desired limiting exponent \(1/2\).

The necessary arithmetic saving is in the aggregate nonprincipal contribution at the original short row length. It must exploit the exact inverse coefficients: the strongest apparently convenient version with arbitrary bounded squarefree coefficients is ruled out by (2.3), even at the second moment.
