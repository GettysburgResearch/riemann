# L-99100 — One random key realizes every factor-67 child from one literal parent

Claim ID: `L-99100`  
Status: **PROVED EXACT MEASURE-THEORETIC THEOREM**  
Created: 2026-08-19  
RH status: **unproved**

## 1. Exact common-parent theorem

Let `(Omega,F,P)` be a finite positive measure space. Let `C_1,...,C_k` be positive measures absolutely continuous with respect to `P`, and let `alpha_j>=0`. Write

\[
 f_j=\frac{d(\alpha_jC_j)}{dP}.
\]

Assume

\[
 \boxed{\sum_{j=1}^k f_j\le1\quad P\text{-a.e.}}
 \tag{L-99100.1}
\]

and put `F_0=0`, `F_j=sum_(i<=j)f_i`. On the enlarged source `Omega x [0,1]`, equipped with `P tensor du`, define

\[
 E_j=\{(omega,u):F_{j-1}(omega)\le u<F_j(omega)\}.
 \tag{L-99100.2}
\]

The sets `E_j` are pairwise disjoint. If `pi(omega,u)=omega`, then for every measurable `A subset Omega`,

\[
\begin{aligned}
 \pi_*\bigl(1_{E_j}(P\otimes du)\bigr)(A)
 &=\int_A\int_0^1 1_{E_j}(\omega,u)\,du\,dP(\omega)\\
 &=\int_A f_j\,dP
 =\alpha_jC_j(A).
\end{aligned}
\tag{L-99100.3}
\]

The residual set

\[
 E_0=\{(\omega,u):\sum_jf_j(\omega)\le u\le1\}
\]

projects to

\[
 \boxed{P-\sum_j\alpha_jC_j.}
 \tag{L-99100.4}
\]

Thus all child measures and the residual are restrictions of one literal parent source. No compatibility inference from separately constructed marginals is required.

## 2. Factor-67 coefficients

Let the active rough primes satisfy

\[
67\le p_1<\cdots<p_k,
\qquad r_j=p_j^{-1/2}.
\]

Put

\[
 s_j=\prod_{i\le j}(1-r_i),
 \qquad
 \lambda_j=r_js_{j-1},
 \qquad
 \alpha_j=r_j\lambda_j.
\tag{L-99100.5}
\]

Telescoping gives

\[
 s_k+\sum_{j=1}^k\lambda_j=1.
\tag{L-99100.6}
\]

For any parent measure `P` and child measures `C_j`, finite algebra gives

\[
\boxed{
 s_kP+\sum_{j=1}^k\lambda_j(P-r_jC_j)
 =P-\sum_{j=1}^k\alpha_jC_j.
}
\tag{L-99100.7}
\]

Moreover,

\[
\begin{aligned}
 \sum_j\alpha_j
 &=\sum_jr_j\lambda_j\\
 &\le \frac1{\sqrt{67}}\sum_j\lambda_j
 <\frac1{\sqrt{67}}<\frac18,
\end{aligned}
\tag{L-99100.8}
\]

where the last strict inequality is exactly `64<67`.

If each `C_j<=P`, then

\[
 \sum_j\frac{d(\alpha_jC_j)}{dP}
 \le\sum_j\alpha_j<\frac18.
\]

Therefore (L-99100.1) holds automatically and the common-parent residual obeys

\[
\boxed{
 P-\sum_j\alpha_jC_j
 \ge\left(1-\frac1{\sqrt{67}}\right)P
 >\frac78P.
}
\tag{L-99100.9}

## 3. Scope

The theorem closes simultaneous ownership **provided** the weighted children are literal submeasures of the same unnormalized parent source. It does not prove that an independently normalized native child datum has that domination. That application interface is isolated in `M-99100`.
