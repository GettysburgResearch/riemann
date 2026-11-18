# Exact finite-Euler-factor transfer for imprimitive Dirichlet approximation

Fix a Dirichlet character $\chi$ modulo $q$, induced by the primitive $\chi_*$ of conductor $q_*$. The modulus and both characters remain fixed as $N\to\infty$. With the norm
$$
\|f\|_*^2=\frac1{2\pi}\int_{\mathbb R}
  |f(1/2+it)|^2\frac{dt}{1/4+t^2},
$$
let $\Delta_{N,\chi}$ be the infimum of $\|1-L(s,\chi)A(s)\|_*$ over all ordinary Dirichlet polynomials $A(s)=\sum_{n\le N}a_n n^{-s}$ with arbitrary complex coefficients. No support condition at primes dividing $q$ is imposed. The normalization gives $\|1\|_*=1$.

I checked the earlier finite-factor argument and derived a product truncation with explicit polylogarithmic length. The transfer below is unconditional as an inequality. Its optimal asymptotic is conditional on the inducing primitive optimal asymptotic, whose GRH-conditional version is a separately adjudicated input. [Earlier transfer audit](../general_l_priority_and_transfer_skeptic62.md) · [Primitive theorem and proof](director_dirichlet_transfer_round6.md)

## Two inequalities with integer cutoffs

Put $\mathcal P=\{p:p\mid q,\ p\nmid q_*\}$, $M=\prod_{p\in\mathcal P}p$, and $F(s)=L(s,\chi_*)$. Then
$$
L(s,\chi)=E(s)F(s),\qquad
E(s)=\prod_{p\in\mathcal P}(1-\chi_*(p)p^{-s}).
$$
This is the comparison of the absolutely convergent Euler products on $\Re s>1$, followed by meromorphic continuation. Removing a prime already dividing $q_*$ introduces no new factor. If $\mathcal P$ is empty, the two functions and all distances are equal, even when the moduli differ.

For any admissible $A$ at length $N$, the polynomial $EA$ has length at most $MN$ and gives exactly the same residual against $F$. Thus
$$
\Delta_{MN,\chi_*}\le\Delta_{N,\chi}.
$$
For the other direction use the explicit finite factor inverse
$$
R_J(s)=\prod_{p\in\mathcal P}\sum_{j=0}^J(\chi_*(p)p^{-s})^j,\qquad
E(s)R_J(s)=\prod_{p\in\mathcal P}
 [1-(\chi_*(p)p^{-s})^{J+1}].
$$
The polynomial $R_J$ has length at most $M^J$, and on the full critical line
$$
\|1-ER_J\|_\infty\le \delta_J,\qquad
\delta_J=\prod_{p\in\mathcal P}(1+p^{-(J+1)/2})-1.
$$
To see the inequality, expand the difference as the sum over nonempty subsets and use $|\chi_*(p)|=1$ at all primes in $\mathcal P$. Given $N\ge M^J$, take $K=\lfloor N/M^J\rfloor$. Multiplying a primitive candidate $A_K$ by $R_J$ fits in length $N$ and gives
$$
\begin{aligned}
\|1-EFR_JA_K\|_*
&\le \|1-FA_K\|_*+\delta_J\|FA_K\|_*\\
&\le (1+\delta_J)\|1-FA_K\|_*+\delta_J .
\end{aligned}
$$
Taking the infimum over the primitive candidates, without needing an attained minimum, gives the combined bound
$$
\boxed{\displaystyle
\Delta_{MN,\chi_*}\le\Delta_{N,\chi}
\le(1+\delta_J)\Delta_{\lfloor N/M^J\rfloor,\chi_*}+\delta_J .}
$$
For example, for sufficiently large $N$ take $J=\lceil2\log\log N/\log 2\rceil$. Then $p^{-(J+1)/2}\le 1/\log N$ and $\delta_J=O_q(1/\log N)$. Also
$$
M^J\le M(\log N)^{2\log M/\log 2},\qquad
\log K=\log N+O_q(\log\log N).
$$
Thus if $(\log K)\Delta_{K,\chi_*}^2\to C_*$, the inequalities, applied in norm with a factor $\sqrt{\log N}$ on both sides, give
$$
\lim_{N\to\infty}(\log N)\Delta_{N,\chi}^2=C_*.
$$
The same argument supports any fixed nonnegative finite primitive constant, including zero. It does not supply conductor-uniform comparisons when $q$ varies with $N$.

## Right constant, principal case, and reciprocal domain

Under GRH for the inducing primitive character, the stated primitive input gives
$$
C_*=\sum_{\substack{\rho\ {\rm distinct}\\L(\rho,\chi_*)=0,\ \Re\rho=1/2}}
\frac{m_\rho^2}{|\rho|^2}.
$$
On $\Re s>0$ every factor of $E$ is nonzero. In particular the critical-line zeros and their orders are exactly the same for $L(s,\chi)$ and $F(s)$. For $p\in\mathcal P$, its factor zeros satisfy $\Re s=0$ and $t\log p\equiv\arg\chi_*(p)\pmod{2\pi}$. These boundary Euler zeros do not belong in the constant. For an imprimitive principal character with $\mathcal P\ne\varnothing$, each added factor vanishes at $s=0$. Naively summing $|\rho|^{-2}$ over all zeros including these factors would not even yield a finite constant.

The conductor-one primitive character induces all principal characters. Then $F=\zeta$, the premise is RH, and the transferred constant is the usual zeta multiplicity sum. The pole at $s=1$ is preserved because $E(1)\ne0$. Its residue may change, but the norm and cutoff comparison do not use the residue value. The transfer does not require an imprimitive completion or an imprimitive Selberg-class functional equation.

The reciprocal $1/E$ has an absolutely convergent ordinary Dirichlet series on each $\Re s>0$, as a product of finitely many geometric series. This includes the critical line uniformly in height. The complete reciprocal $1/L(s,\chi)$ has the ordinary Euler-product coefficients $\mu(n)\chi(n)$ for $\Re s>1$. Its Dirichlet series is not absolutely convergent on the critical line. Already for primes $p\nmid q$, its coefficient has absolute value one and $\sum_{p\nmid q}p^{-1/2}$ diverges. The upper comparison uses only the uniform finite-factor inverse, so it does not assume critical-line absolute convergence of the complete reciprocal.

The polynomial multiplier $R_J$ uses frequencies divisible by primes in $\mathcal P$ for $J\ge1$. This is allowed for ordinary unrestricted coefficients. Neither inequality establishes the same asymptotic after restricting to $(n,q)=1$, or after prescribing coefficients at the ramified integers. In particular, geometric factor division cannot be described as preserving such an admissible support. The vanishing of the natural arithmetic coefficients $\mu(n)\chi(n)$ at ramified integers is a fact about that one sequence, not about the optimizing polynomial space.

## What an anchor at one changes

The cutoff sandwich itself also preserves the condition $A(1)=0$: both $A\mapsto EA$ and $A\mapsto R_JA$ preserve that linear condition. Therefore an anchored theorem for a principal induced character follows if the inducing zeta theorem is supplied in that same anchored space. The unanchored hypothesis alone does not prove an anchored conclusion.

For a nonprincipal character the anchored distance with $A(1)=0$ is exactly one at every length, even for primitive $\chi$. To prove it, let $S_\chi(x)=\sum_{n\le x}\chi(n)$. Periodicity and the vanishing period sum give bounded $S_\chi$. The function $x\mapsto S_\chi(1/x)$ is bounded and vanishes for $x>1$. Its Mellin transform is $L(s,\chi)/s$ for $\Re s>0$, first by absolute summation on $\Re s>1$ and then by analyticity and bounded partial sums. For any ordinary polynomial $A$, the residual divided by $s$ is therefore the Mellin transform of a function $h_A$ supported on $(0,1)$, obtained by subtracting the weighted integer dilates of $S_\chi(1/x)$ from the indicator. Mellin Plancherel gives $\|h_A\|_2=\|1-L_\chi A\|_*$. Evaluation at $s=1$ and Cauchy–Schwarz give
$$
|1-L(1,\chi)A(1)|=\left|\int_0^1h_A(x)\,dx\right|\le\|h_A\|_2.
$$
If $A(1)=0$, this lower bound is one and $A=0$ attains it. Replacing $A$ by $A-A(1)$ produces exactly that anchored space. The argument cannot be applied to force the same outcome for principal characters, where $L(s,\chi)$ has a pole and the product with a vanishing $A$ may have a nonzero removable value at one.

## Bounded antecedent check

Dimitrov–Oliveira, arXiv:1608.07887v1, Theorems 1–2 and their proofs in §3, treat arbitrary Dirichlet characters, including the principal case, in the ordinary rational-weight norm. Their result is qualitative vanishing of the distance under the corresponding zero-free condition. Theorem 3 instead gives asymptotics for a separate interpolation space. De Roton supplies the multiplicity lower mechanism for the inducing primitive function, and DFMR I supplies continuous-distance zero-free criteria. This limited inspection did not identify a prior matching imprimitive logarithmic constant in those passages. The finite Euler-factor transfer was already recorded with a different explicit truncation in the earlier local audit. No priority conclusion follows. [Dimitrov–Oliveira v1](../../sources/ratio62_rstation48/dimitrov_oliveira.pdf) · [De Roton](../../sources/prefix_formula62_generalL/deroton_lower.pdf) · [DFMR I](../../sources/prefix_formula62_generalL/dfmr1.pdf) · [Earlier transfer](../general_l_priority_and_transfer_skeptic62.md)
