# The zero-at-one anchor for a nonprincipal Dirichlet character

Let \(\chi\) be a fixed nonprincipal Dirichlet character, primitive or imprimitive. Optimize over complex ordinary Dirichlet polynomials \(A\) of length at most \(N\) with \(A(1)=0\), in the boundary norm
\[
 \|g\|_*^2=\frac1{2\pi}\int_{\mathbb R}
 \frac{|g(1/2+it)|^2}{1/4+t^2}\,dt.
\]
Then for every such \(A\),
\[
 \|1-L(\cdot,\chi)A\|_*^2=1+\|L(\cdot,\chi)A\|_*^2.
\]
Consequently the minimum norm and squared norm are both 1 for every \(N\ge1\), attained uniquely by \(A=0\). This holds unconditionally.

## Exact Hardy evaluation

Write \(S(x)=\sum_{n\le x}\chi(n)\). Period cancellation gives \(S(x)=O_\chi(1)\). On \(\Re s>1\), partial summation gives
\[
 \frac{L(s,\chi)}s=\int_1^\infty S(x)x^{-s-1}\,dx
                 =\int_0^\infty S(e^u)e^{-su}\,du.
\]
The integral continues holomorphically to \(\Re s>0\) by absolute convergence and agrees there with the Dirichlet \(L\)-function quotient. On the half-plane \(H=\{\Re s>1/2\}\) the quotient is the Laplace transform, with parameter \(s-1/2\), of \(e^{-u/2}S(e^u)\in L^2(0,\infty;du)\). It therefore belongs to \(H^2(H)\) with boundary measure \(dt/(2\pi)\). Multiplication by the bounded analytic polynomial \(A\) preserves that space. The boundary norm of \(L A/s\) there is precisely \(\|LA\|_*\).

The function \(1/s\) is the evaluation kernel at \(s=1\) for this normalization. In the Laplace model, its vector is \(e^{-u/2}\), and both its vector norm and its evaluation norm are 1. Thus, with the inner product linear in its first entry,
\[
 \left\langle L(s,\chi)A(s)/s,\ 1/s\right\rangle_{H^2(H)}
   = L(1,\chi)A(1)=0 .
\]
Pythagoras gives the claimed identity. If \(LA/s\) has zero boundary norm, the Hardy vector is zero, so \(LA\) vanishes identically on \(H\). Since \(L\) is not the zero function, \(A\) vanishes identically. Uniqueness of ordinary Dirichlet coefficients then gives \(A=0\). The reduction of an unrestricted input polynomial \(B\) to \(A=B-B(1)\) has exactly the same image as the set \(A(1)=0\). If the problem is written in terms of such inputs \(B\), every constant \(B\) attains the value 1, and only constants do.

More generally, the projection argument needs only that the admissible product \(FA/s\) be in \(H^2(H)\) and vanish at \(s=1\). For a holomorphic \(F\) with \(F/s\in H^2(H)\) this holds whenever \(A(1)=0\), and uniqueness holds if \(F\not\equiv0\). A meromorphic \(F\) of pole order \(p\) at 1 would require an anchor of order at least \(p+1\) to force product vanishing there by order alone. Analytic continuation in \(H\) of the product alone is insufficient to identify its boundary integral with a Hardy evaluation. The Hardy membership must also be supplied.

## A simple pole changes the evaluation

For the principal character of any modulus \(q\), including \(\zeta\) when \(q=1\), put \(F=L(\cdot,\chi_0)\) and \(r=\prod_{p\mid q}(1-p^{-1})>0\). The pole at 1 has residue \(r\). The summatory coefficients are \(rx+O_q(1)\), so \(F(s)/s=r/(s-1)+H_0(s)\) with \(H_0\in H^2(H)\) by the same bounded-error Laplace argument. If \(A(1)=0\), \(FA/s\) is regular at 1 and has value \(rA'(1)\), which need not vanish.

For an explicit admissible counterexample to the distance-one conclusion, take \(A_0(s)=1-2^{1-s}\), available for \(N\ge2\). Then \(A_0'(1)=\log2\), and
\[
 A_0(s)/(s-1)=\int_0^{\log2} e^{-(s-1)u}\,du
\]
is in \(H^2(H)\) by its compact Laplace support. Hence \(FA_0/s\in H^2(H)\) and its pairing with \(1/s\) is \(r\log2\ne0\). Minimizing over complex scalar multiples of \(A_0\) yields squared norm
\[
 1-\frac{(r\log2)^2}{\|FA_0\|_*^2}<1.
\]
Thus already a length-two anchored polynomial breaks the flat obstruction for principal characters. At \(N=1\), the zero-at-one anchor admits only zero, so the distance is 1 for both principal and nonprincipal cases. The upper example does not compute the principal-character optimum or its asymptotic rate. The nonprincipal identity does not apply to the unanchored distance.
