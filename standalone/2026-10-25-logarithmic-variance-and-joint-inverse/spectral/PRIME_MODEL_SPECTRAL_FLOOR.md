# A complete-source spectral floor from the prime discrepancy

Status: proposed analytic estimate with a complete proof below; not independently reviewed.
Scope: exact full or even finite trigonometric compressions of the complete Weil form. The bound is unconditional in its discrepancy-integral form. Its power-saving specialization is conditional on the stated prime number theorem error term.
Exact source: PR #1017, `450dd8abecf58dfe60b3bc39bda0f792ea82ce95`, complete semilocal Weil form, its Fourier convention, pole terms, and all prime powers.
External input for the unconditional asymptotic corollary: Johnston--Yang, *Some explicit estimates for the error term in the prime number theorem*, arXiv:2204.01980v2, Theorem 1.4, equation (1.7).
What this achieves: an actual source-dependent lower estimate, including the exact pole/main-prime cancellation and an unconditional improvement over the crude exponential floor along polynomial Fourier schedules.
What it does not achieve: a smaller zero-free strip. A supplied prime discrepancy exponent \(\beta\) is returned unchanged; it is not bootstrapped to a smaller exponent.

## 1. Definitions and the explicit lower bound

For \(a>0\) and an integer \(N\ge0\), use

\[
\mathcal T_{a,N}=\operatorname{span}\{e^{in\pi x/a}:|n|\le N\}
\]

on \([-a,a]\), with zero extension and the \(L^2\) inner product. Let \(T_{a,N}\) be the exact compression of the complete Weil form from the pinned source. For \(f\in\mathcal T_{a,N}\), put

\[
F(t)=\int f(x)e^{-itx}\,dx,\qquad
C_f(u)=\int\overline{f(x)}f(x+u)\,dx,
\qquad S_f(u)=C_f(u)+C_f(-u).
\tag{1}
\]

Let

\[
\psi(x)=\sum_{n\le x}\Lambda(n),\qquad
E(x)=\psi(x)-x+1,
\qquad
I(a)=\int_0^{2a}|E(e^u)|e^{-u/2}\,du.
\tag{2}
\]

Write \(\psi_\Gamma(z)=\Gamma'(z)/\Gamma(z)\) for the digamma function, to distinguish it from the prime-counting function \(\psi\) in (2). The harmless constant \(+1\) makes \(E(1)=0\), which removes the lower endpoint in Stieltjes integration by parts. Define

\[
D_{a,N}=\frac{\pi N+(2N+1)/2}{a},\qquad
b_*=4-\gamma-\frac\pi2-3\log2-\log\pi.
\tag{3}
\]

**Theorem 1 (actual finite spectral floor).** For all \(a>0\), \(N\ge0\),

\[
\boxed{\min\operatorname{spec}(T_{a,N})
\ge b_*-2(D_{a,N}+1/2)I(a).}
\tag{4}
\]

The same bound holds for the even block. The matrix in (4) is the complete source matrix; no prime, archimedean, pole, parity, or boundary term has been omitted. The quantity \(I(a)\) depends only on the actual finite prime discrepancy up to \(e^{2a}\).

## 2. Exact cancellation with the continuous prime model

The prime part of the source form is

\[
-\int_1^{e^{2a}}x^{-1/2}S_f(\log x)\,d\psi(x).
\tag{5}
\]

The continuous model \(d\psi(x)=dx\) contributes

\[
-\int_0^{2a}e^{u/2}S_f(u)\,du
=-\int_{-2a}^{2a}e^{|u|/2}C_f(u)\,du.
\tag{6}
\]

The full pole term is exactly

\[
2\Re\bigl(F(i/2)\overline{F(-i/2)}\bigr)
=\int_{-2a}^{2a}2\cosh(u/2)C_f(u)\,du.
\tag{7}
\]

Since \(2\cosh(u/2)=e^{|u|/2}+e^{-|u|/2}\), (6) cancels the growing half of (7). Their sum is the positive convolution form

\[
\int_{\mathbb R}e^{-|u|/2}C_f(u)\,du
=\frac1{2\pi}\int_{\mathbb R}
 \frac{|F(t)|^2}{t^2+1/4}\,dt.
\tag{8}
\]

Retaining this whole term sharpens the base constant. Indeed

\[
\Re\psi_\Gamma(1/4+it/2)+\frac1{t^2+1/4}
=\Re\psi_\Gamma(5/4+it/2)
\tag{9}
\]

by the digamma recurrence. Thus the continuous-model form is exactly

\[
q^{\mathrm{model}}[f]
=\frac1{2\pi}\int_{\mathbb R}
 \bigl(\Re\psi_\Gamma(5/4+it/2)-\log\pi\bigr)|F(t)|^2\,dt.
\tag{10}
\]

The digamma series gives \(\Re\psi_\Gamma(x+iy)\ge\psi_\Gamma(x)\) for \(x>0\): the difference is the sum of the nonnegative terms
\(y^2/((n+x)((n+x)^2+y^2))\). Its value at \(x=5/4\), with reflection and duplication, gives

\[
q^{\mathrm{model}}[f]\ge
\bigl(\psi_\Gamma(5/4)-\log\pi\bigr)\|f\|_2^2
=b_*\|f\|_2^2.
\tag{11}
\]

Equation (10) is a full-source cancellation, not an assumption that the arithmetic error or the original form is positive.

## 3. Exact arithmetic remainder and its finite-frequency estimate

For \(0\le u\le2a\),

\[
C_f(u)=\int_{-a}^{a-u}\overline{f(x)}f(x+u)\,dx.
\]

It is absolutely continuous and, almost everywhere,

\[
C_f'(u)
=-\overline{f(a-u)}f(a)
 +\int_{-a}^{a-u}\overline{f(x)}f'(x+u)\,dx.
\tag{12}
\]

For a trigonometric polynomial of degree \(N\), orthogonality and Cauchy--Schwarz give

\[
\|f'\|_2\le\frac{\pi N}{a}\|f\|_2,
\qquad
\|f\|_\infty^2\le\frac{2N+1}{2a}\|f\|_2^2.
\tag{13}
\]

The endpoint term in (12) is essential because zero extension need not be continuous. Combining (12)--(13),

\[
|C_f'(u)|\le D_{a,N}\|f\|_2^2,
\qquad |C_f(u)|\le\|f\|_2^2.
\tag{14}
\]

Since \(C_f(-u)=\overline{C_f(u)}\), these imply

\[
|S_f(u)|\le2\|f\|_2^2,
\qquad |S_f'(u)|\le2D_{a,N}\|f\|_2^2.
\tag{15}
\]

Set \(H(x)=x^{-1/2}S_f(\log x)\). It is absolutely continuous on \([1,e^{2a}]\), and \(H(e^{2a})=0\) because the endpoint autocorrelation vanishes. Since \(E(1)=0\), Stieltjes integration by parts gives the **exact** remainder identity

\[
\begin{aligned}
q_a[f]-q^{\mathrm{model}}[f]
&=-\int_1^{e^{2a}}H(x)\,dE(x)\\
&=\int_1^{e^{2a}}E(x)H'(x)\,dx\\
&=\int_0^{2a}E(e^u)e^{-u/2}
 \bigl(S_f'(u)-\tfrac12S_f(u)\bigr)\,du.
\end{aligned}
\tag{16}
\]

There is no endpoint correction from a possible prime power at \(e^{2a}\): its multiplier \(H(e^{2a})\) is zero. Both signs in (16) are fixed by retaining the negative prime term in (5).

It follows from (15) that

\[
|q_a[f]-q^{\mathrm{model}}[f]|
\le2(D_{a,N}+1/2)I(a)\|f\|_2^2.
\tag{17}
\]

Together with (11), this proves (4) by the finite-dimensional variational principle. Restricting to the even block preserves the inequality. QED.

## 4. What a power-saving prime input buys

**Corollary 1.** Suppose for some fixed \(\beta>1/2\) that

\[
|\psi(x)-x|\le C_\beta x^\beta\qquad(x\ge2).
\tag{18}
\]

Then, for \(a\ge1\),

\[
\min\operatorname{spec}(T_{a,N})
\ge b_*-C_\beta'(1+N/a)e^{(2\beta-1)a}.
\tag{19}
\]

**Proof.** The bounded initial interval and the \(+1\) in \(E\) are absorbed in a constant. Equation (18) gives

\[
I(a)\le C_\beta''\int_0^{2a}e^{(\beta-1/2)u}\,du
\le C_\beta'''e^{(2\beta-1)a}.
\]

Insert this in (4), observing \(D_{a,N}+1/2\ll1+N/a\) for \(a\ge1\). QED.

For any fixed polynomial mode schedule, the prefactor \(1+N/a\) is absorbed into \(e^{\epsilon a}\). Along a schedule covered by the finite spectral-growth consumer, such as \(N=\lceil ca^2\rceil\) with fixed \(c>0\) or \(N=\lceil a^3\rceil\), the consumer then excludes zeros with \(\Re\rho>\beta\), precisely the same exponent as the arithmetic input. In particular the proof gives no implication of the form \(\beta\mapsto\beta'<\beta\).

## 5. An unconditional asymptotic improvement, with its limit stated

Johnston--Yang, Theorem 1.4, equation (1.7), proves the explicit estimate

\[
|\psi(x)-x|
\le0.026x(\log x)^{1.801}
\exp\left(-0.1853\frac{(\log x)^{3/5}}
 { (\log\log x)^{1/5}}\right)
\qquad(x\ge23).
\tag{20}
\]

This external theorem is imported as a known prime-number-theorem bound; its underlying verification computations have not been rerun here. For a literal bound in (4), set \(u_0=\log23\). For \(a\ge u_0/2\), the elementary initial-interval estimate and (20) give

\[
\begin{aligned}
I(a)\le{}&\int_0^{u_0}e^{u/2}(u+1)\,du+2\\
&+0.026\int_{u_0}^{2a}u^{1.801}
 \exp\left(\frac u2-0.1853
 \frac{u^{3/5}}{(\log u)^{1/5}}\right)\,du.
\end{aligned}
\tag{21}
\]

The initial bound uses \(\psi(x)\le x\log x\). The extra \(2\) bounds the integral of \(e^{-u/2}\) contributed by \(+1\) in \(E\). All quantities in (21) are explicit real integrals.

In particular there exist absolute positive constants \(c,C\) such that, for every sufficiently large \(a\),

\[
I(a)\le C e^a
\exp\left(-c\frac{a^{3/5}}{(\log a)^{1/5}}\right).
\tag{22}
\]

One elementary derivation is to split the integral at \(u=a\). On the first part, the crude estimate gives \(O((1+a)^C e^{a/2})\). On the second, the increasing function \(u^{3/5}/(\log u)^{1/5}\) is at least its value at \(a\), so the result is at most
\(C(1+a)^{1.801}e^a\exp(-0.1853a^{3/5}/(\log a)^{1/5})\). A fixed reduction of the positive exponential constant absorbs the polynomial. This proves (22) without an endpoint asymptotic formula.

Consequently (4) gives an **unconditional actual-source bound**

\[
\boxed{
\min\operatorname{spec}(T_{a,N})
\ge b_*-C(1+N/a)e^a
\exp\left(-c\frac{a^{3/5}}{(\log a)^{1/5}}\right)
}
\tag{23}
\]

for \(a\ge a_0\). Along the quadratic mode schedule of the signed-selector theorem, this improves the older crude \(-O(ae^a)\) lower bound by a factor tending to zero faster than every inverse power of \(a\).

The exponent of \(a\) in the leading exponential remains one. Therefore (23) does **not** yield a new fixed zero-free strip through the spectral consumer. The gain is a baseline estimate imported from known prime cancellation, not a claimed number-theoretic breakthrough.

## 6. The precise place where an improvement would have to enter

Equation (16), before taking absolute values, contains more information than the PNT majorant. Its test function is a derivative of an actual autocorrelation, not an arbitrary bounded function. A sharper source argument would need to bound the negative part of

\[
\int_0^{2a}E(e^u)e^{-u/2}
 \bigl(S_f'(u)-\tfrac12S_f(u)\bigr)\,du
\]

uniformly over the stated finite space, using those autocorrelation constraints. Simply replacing \(E\) by the available pointwise power bound cannot improve that bound's exponent, as the exact calculation (19) shows. No cancellation estimate beyond (17) has been established in this note.

## Primary references

- A. Connes, C. Consani, H. Moscovici, *Zeta Spectral Triples*, arXiv:2511.22755v1, <https://arxiv.org/html/2511.22755v1>, with the exact source convention authenticated by pinned PR #1017.
- D. R. Johnston and A. Yang, *Some explicit estimates for the error term in the prime number theorem*, arXiv:2204.01980v2, <https://arxiv.org/html/2204.01980v2>, Theorem 1.4, equation (1.7). Only the stated \(\psi\) bound is used; the proof of the spectral estimate above is native.
