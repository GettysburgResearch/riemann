# PFR-T10 — Symmetric positive-definite prime-knot resolvent

Status: **AUTHOR-PROVED EXACT ANALYTIC THEOREM / REVIEW PENDING**  
RH status: **unproved**  
External novelty: **unestablished; Weil/Suzuki overlap review required**

For `a>1/2`, `m>=2`, and centered zeros `lambda_rho=rho-1/2`, define

\[
S_{a,m}(t)=\sum_\rho
\frac{e^{\lambda_\rho t}}{(a^2-\lambda_\rho^2)^m}.
\]

Then:

1. `S_(a,m)` is real and even and is `C^(2m-2)` on positive time;
2. if `F(z)=xi'/xi(1/2+z)` and `H_(a,m-1)F` is its two-point Hermite
   interpolant at `+/-a`, then
   \[
   \frac{F(z)-H_{a,m-1}F(z)}{(a^2-z^2)^m}
   =\sum_\rho\frac1{(a^2-\lambda_\rho^2)^m(z-\lambda_\rho)};
   \]
   the left side is source-defined on `Re z>1/2` by the absolutely convergent
   prime series and completion terms;
3. distributionally on positive time,
   \[
   (a^2-D^2)^mS_{a,m}=\mathscr Z,
   \]
   and at every prime power `n`,
   \[
   S_{a,m}^{(2m-1)}((\log n)^+)-S_{a,m}^{(2m-1)}((\log n)^-)
   =(-1)^{m+1}\Lambda(n)/\sqrt n;
   \]
4. the pointwise exponential type and weighted-`L2` abscissa of `S_(a,m)`
   equal `Theta-1/2`;
5. RH is equivalent to boundedness of `S_(a,m)`, positive definiteness of
   `S_(a,m)`, positive-realness of its Laplace transform, positivity of the
   corresponding Pick kernel, and every-positive-shift Hardy-`H2` membership.

Under RH the common positive measure is

\[
\mu_{a,m}=\sum_\gamma(a^2+\gamma^2)^{-m}\delta_\gamma.
\]

No prime-side proof of positivity is supplied.  That is the remaining
RH-strength theorem.
