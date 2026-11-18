# Independent reconstruction: critical Bergman closure

2026-11-17. Reviewer `/root/li_skeptic`. The coefficient and tail argument was reconstructed from the advocate's statement before reading any completed draft. The subsequent dilation argument was also reconstructed independently from its formula. **No issue found in this scoped repair.** It supplies an unconditional closure/density statement in `D_-1`, separate from the incorrect inverse-operator endpoint. No historical novelty or new RH result is asserted.

Use the actual Noor functions

\[
 h_k(z)=\frac1{1-z}\log\frac{1+z+\cdots+z^{k-1}}k,
 \qquad k\ge2,
\]

with the analytic logarithm on the disk taking value `-log k` at zero. The polynomial inside the logarithm has its zeros on the unit circle, so this branch exists on the disk. The norm is exactly the normalized Bergman area norm

\[
 \|f\|_{-1}^2=\sum_{n\ge0}|f_n|^2/(n+1).
\]

Let

\[
 A_N=\sum_{k\le N}\mu(k)/k,\quad
 B_N=\sum_{k\le N}\mu(k)\log k/k,\quad
 V_N=\sum_{k=2}^N\frac{\mu(k)}k h_k.
\]

The only analytic-number-theory input used below is the classical unconditional bound `M(x)=O_K(x(log x)^(-K))` for every fixed `K`. It gives the two corresponding all-log-power bounds `A_N=O_K((log N)^(-K))` and `B_N+1=O_K((log N)^(-K))` after increasing the chosen input power. No numerical explicit constant from a recent source is needed. To identify the second limit, the series for `sum mu(n)log n/n` converges by partial summation from this bound; Abel's theorem and `(1/zeta)'(1)=1` give its value `-1`. This declares a classical external input, not an audit of its historical proof.

## Exact coefficients and central estimate

Writing `H_0=0`, expansion of the two logarithms gives the coefficient of `z^n` in `h_k` as

\[
 c_n(k)=H_n-H_{\lfloor n/k\rfloor}-\log k.
\]

For `n>=1`, the divisor identity is exact:

\[
 \sum_{k\le n}\frac{\mu(k)}k H_{\lfloor n/k\rfloor}
 =\sum_{m\le n}\frac1m\sum_{k\mid m}\mu(k)=1.
\]

Consequently, for `1<=n<=N`, the Taylor coefficients `v_n` of `V_N` are

\[
 v_0=-B_N,\qquad v_n=A_NH_n-1-B_N.
\]

In particular all coefficients tend to those of the constant function1, with the signs as stated in the advocate's claim. The central contribution to `||V_N-1||_-1²` is bounded by

\[
 C\bigl(|A_N|^2\log^3(N+2)+|B_N+1|^2\log(N+2)\bigr),
\]

which tends to zero by the classical input. This includes the constant coefficient; the source index `k=1` contributes no `h_1` term since that function is identically zero.

## Uniform tail bound, not tail convergence

For `n>N>=k>=2`, put `m=floor(n/k)>=1`. The harmonic integral comparisons give

\[
 \log\frac{n+1}{m+1}\le H_n-H_m\le\log\frac nm.
\]

After subtracting `log k`, the positive side is at most `1/m<=2k/n`. The negative side has magnitude at most `log((n+k)/(n+1))<=k/n`. Hence the slightly sharper bound

\[
 |c_n(k)|\le2k/n
\]

holds; the advocate's bound `5k/n` is therefore safe. It follows that `|v_n|<=2N/n` and

\[
 \sum_{n>N}\frac{|v_n|^2}{n+1}
 \le4N^2\sum_{n>N}n^{-3}\le2.
\]

The stated looser `25/2` bound also follows. This proves a **uniform bound** for the tail. It does not show that the raw sequence `V_N` converges in Bergman norm, and no such claim is made.

The central bound and the tail bound show that `V_N` is uniformly bounded in `D_-1`. Coefficientwise convergence then implies weak convergence to1: first test against any finite polynomial, and then approximate an arbitrary Hilbert-space test vector by polynomials using the uniform norm bound. Every `V_N` lies in the finite linear span of the `h_k`. A norm-closed linear subspace is weakly closed, so1 belongs to the norm closure of that span. Equivalently one may use Mazur convex combinations. This repairs precisely the unweighted critical closure assertion without invoking a bounded inverse for `T_1:D_-1->D_-3`.

## Full density by a bounded invariant dilation

Let `P_m=1+z+...+z^(m-1)` and `W_mf=P_m(z)f(z^m)`, with `m>=1`. Composition is contractive in the coefficient norm:

\[
 \|f(z^m)\|_{-1}^2=\sum|f_n|^2/(mn+1)\le\|f\|_{-1}^2.
\]

Multiplication by `P_m` has norm at most `m` by the exact Bergman area norm and `|P_m(z)|<=m` on the disk. Thus `W_m` is bounded. Direct substitution, with the analytic log branches fixed at zero, gives

\[
 W_mh_k=h_{mk}-h_m,
\]

where `h_1=0`. Let `H` be the closed linear span of the `h_k`. This identity makes `H` invariant under `W_m`. Since1 belongs to `H`, every `P_m=W_m1` belongs to `H`. Taking consecutive differences gives every monomial; polynomials are dense in the Bergman coefficient space. Therefore

\[
 \overline{\operatorname{span}\{h_k:k\ge2\}}^{D_{-1}}=D_{-1}.
\]

The proof does not extend this conclusion to a weighted `a>1` target, does not assert direct norm convergence of `V_N`, and does not repair general inverse-based closure transport merely from density of an operator's range. The matching advocate proof is `proposals/independent_campaigns/noor_critical_bergman_advocate_round4.md`; its historical priority still requires separate source comparison.

## Classical primary-source input recovered after the initial reconstruction

There is no need to depend on a recent explicit Mertens estimate. This reviewer subsequently read and visually checked **PAPER-M001**, Titchmarsh1986, Theorem3.13 and its proof, printedpp62–63 (PDF36). The image is `sources/logarithmic_riesz_priority_skeptic_round4/titchmarsh_p62_63_skeptic.png`. At `s=1`, its displayed truncated-Perron error bounds, with `c=1/log x`, `T=exp((log x)^(1/10))`, and `delta=A(log x)^(-9/10)`, give `A_N=O(poly(log N) exp(-c_0(log N)^(1/10)))` for some fixed `c_0>0`. Taking `x=N+1/2` handles every integer cutoff. The powers of the logarithm are absorbed by the exponential, so this supplies every fixed log-power decay required above. The proof's earlier zero-free-region and Perron inputs are accepted classical dependencies, not newly audited from their originals.

One can then derive the second scalar estimate using **only** this bound on `A`, rather than a separate estimate for `M`. For `h>0`, ordinary partial summation gives

`(1/zeta(1+h))/h = integral_1^infinity A(t)t^(-h-1)dt`.

The quantitative bound on `A` makes `A(t)/t` absolutely integrable, so dominated convergence and the simple pole of zeta give `integral A(t)/t dt=1`. The exact finite identity

`B_N=A_N log N−integral_1^N A(t)/t dt`

therefore yields `B_N+1=A_N log N+integral_N^infinity A(t)/t dt`, which decays faster than any fixed reciprocal logarithm after choosing a stronger fixed input power. This provides a traceable stable-source foundation for the closure proof without endorsing any later explicit constants or withdrawn version.
