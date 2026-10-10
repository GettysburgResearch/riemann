# Retain every known far factor in a finite Taylor jet and remainder

Status: proposed exact finite-product adapter, pending independent review.
Scope: a complete finite simple real-zero census. Its directed root balls
enclose the exact real roots. This adapter accelerates finite arithmetic;
the complete unseen infinite tail remains a separate analytic dependency.

Let a finite paired product have a selected far part with real roots
`gamma>D>B>0`, and put

\[
S_k=\sum_{\gamma\text{ in the selected finite far part}}\gamma^{-2k},
\qquad q=B^2/D^2<1.
\tag{FJ1}
\]

Every retained root contributes to every `S_k`; directed balls for the
root positions give directed enclosures of these finite sums. For a fixed
integer `K>=1`, the exact logarithmic derivatives are

\[
L_1=-2z\sum_{j=0}^{K-1}S_{j+1}z^{2j}+e_1(z),
\quad
L_2=-2\sum_{j=0}^{K-1}(2j+1)S_{j+1}z^{2j}+e_2(z).
\tag{FJ2}
\]

Expanding each exact finite factor by the geometric series and retaining
all its remaining terms gives, on `|z|<=B`,

\[
|e_1|\le \varepsilon_1
 :=\frac{2BS_1q^K}{1-q},
\tag{FJ3}
\]

\[
|e_2|\le \varepsilon_2
 :=2S_1q^K\left[\frac{2K+1}{1-q}
                         +\frac{2q}{(1-q)^2}\right].
\tag{FJ4}
\]

Indeed `S_(j+1)<=S_1/D^(2j)` for every `j>=K`, and
`sum_(j>=K)(2j+1)q^j=q^K[(2K+1)/(1-q)+2q/(1-q)^2]`.
There is no discarded finite root or fitted coefficient. The complex
error disk is enclosed by the square with both component radii equal to
the directed upper bound for the relevant epsilon. Adding that full
square to the finite Horner evaluation preserves outward enclosure.

## Cross local real zeros without dividing by their vanishing factors

On a compact complex box, select any nearby paired factors into the exact
polynomial `f`, and leave all other known factors in the nonvanishing bulk
`b`. Include the Gaussian factor in that bulk:

\[
G_a=e^{-az^2}P=b_af,\qquad
\ell_1=b_a'/b_a,\quad\ell_2=(b_a'/b_a)'.
\tag{FJ5}
\]

The selected factors and their first two derivatives are multiplied by
the full polynomial product rule. The bulk derivatives combine the
explicit remaining near factors, (FJ2)--(FJ4) for every far finite factor,
and the exact Gaussian contributions `-2az`, `-2a`.
Every bulk division is guarded; the local factor `f` itself may vanish.
Exact normalized derivatives are

\[
G_a/b_a=f,\quad G_a'/b_a=f'+f\ell_1,
\quad G_a''/b_a=f''+2f'\ell_1+f(\ell_1^2+\ell_2).
\tag{FJ6}
\]

Consequently its exact companion quotient is enclosed through

\[
W_a=i\frac{f-i\lambda(f'+f\ell_1)}
 {f'+f\ell_1-i\lambda[f''+2f'\ell_1+f(\ell_1^2+\ell_2)]}.
\tag{FJ7}
\]

This formula remains valid at a simple real zero of the complete finite
product. The checker must guard the companion denominator in (FJ7), rather
than dividing by `f` or accepting an unguarded logarithmic singularity.

All root and parameter uncertainty is included in the directed factors,
finite sums and error squares. This is an exact finite-product enclosure,
with an explicit remainder for all retained far factors. A separate
complete-tail transport predicate is still required to bind it to Xi.
