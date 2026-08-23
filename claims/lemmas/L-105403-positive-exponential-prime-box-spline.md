# L-105403 — The finite native Euler numerator has a positive exponential prime-box spline

Claim ID: `L-105403`

Status: **PROVED EXACT POSITIVE FINITE-SOURCE THEOREM**

Let `E` be a finite labelled prime multiset, including repeated occurrence
labels when required. Put

\[
\lambda_e=\log p_e,
\qquad r_e=e^{-\lambda_e/2},
\qquad
\mathcal E_E=\prod_{e\in E}(I-r_eS_{\lambda_e}).
\]

Let `m=|E|` and define the causal half-order Green kernel

\[
k_m(t)=e^{-t/2}\frac{t_+^{m-1}}{(m-1)!}.
\]

Distributionally,

\[
(D+\tfrac12)^mk_m=\delta_0.
\]

Applying the twisted prime-box Stokes formula of `L-105400` gives

\[
\boxed{
\mathcal E_Ek_m(t)
=
\int_{\prod_{e\in E}[0,\lambda_e]}
 e^{-\frac12\sum_eu_e}
 \delta\!\left(t-\sum_eu_e\right)\,du
\ge0.
}
\tag{L-105403.1}
\]

Thus the exact labelled native Euler corner cycle becomes a positive density
on the weighted activation sum. It is the exponential box spline attached to
the prime intervals.

For `Re s>-1/2`, its Laplace transform is

\[
\boxed{
\int_0^\infty e^{-st}\mathcal E_Ek_m(t)\,dt
=
\frac{\prod_{e\in E}(1-p_e^{-(s+1/2)})}
     {(s+1/2)^m}.
}
\tag{L-105403.2}
\]

Indeed each positive interval measure has transform

\[
\int_0^{\lambda_e}e^{-(s+1/2)u}\,du
=
\frac{1-p_e^{-(s+1/2)}}{s+1/2},
\]

and convolution multiplies the factors.

## Geometric interpretation

The source numerator is the K-theoretic Euler class of the labelled Frobenius
intervals; the Green denominator is the top-dimensional orientation kernel.
The positive spline is therefore a literal finite `F1` fundamental density,
not a positive replacement of the source.

## Scope firewall

The order `m` grows with the finite prime set. Hence (L-105403.1) is a finite
source theorem, not a fixed Mellin detector and not a cofinal RH proof. Any
attempt to invert `(D+1/2)^m` at growing order must keep its signed boundary and
its effect on the fixed detector explicit.
