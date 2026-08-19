# L-99101 — The optimal high-order Hermite notch has an exact two-saddle exponent

Claim ID: `L-99101`  
Status: **PROVED EXACT ASYMPTOTIC OPTIMIZATION THEOREM**  
Created: 2026-08-19  
Depends on: `L-99100`, the absolute-coefficient Euler product of `T-98710`  
RH status: **not assumed**

Keep the notation

\[
q=\frac12-\delta,
\qquad 0<\delta<\frac12.
\]

Let `M=alpha T+O(1)` with `alpha>0`. At logarithmic scale

\[
x=\frac{\log n}{T},
\]

the exponential rate of the coefficientwise absolute envelope of the notched packet is

\[
\boxed{
\Phi_{\alpha,q}(x)
=\frac x2-\frac{x^2}4
 +\alpha\log\frac{|1-x|}{2q}.
}
\tag{L-99101.1}
\]

The two stationary points are

\[
x_\pm=1\pm\sqrt{2\alpha}.
\]

At either stationary point,

\[
\boxed{
\Phi_{\alpha,q}(x_\pm)
=\frac14-\frac\alpha2
 +\frac\alpha2\log(2\alpha)
 -\alpha\log(2q).
}
\tag{L-99101.2}
\]

The right side is minimized uniquely when

\[
\boxed{\alpha_*=2q^2.}
\tag{L-99101.3}
\]

At the optimum,

\[
\sqrt{2\alpha_*}=2q=1-2\delta,
\]

so

\[
\boxed{x_-=2\delta,\qquad x_+=2-2\delta.}
\tag{L-99101.4}
\]

The optimal coefficientwise amplitude rate is

\[
\boxed{
\Phi_*(\delta)
=\frac14-q^2
=\delta-\delta^2.
}
\tag{L-99101.5}
\]

By contrast, the preserved off-line-zero contribution has amplitude rate `delta^2`. Their exact gap is

\[
\boxed{
\Phi_*(\delta)-\delta^2
=\delta(1-2\delta)>0.
}
\tag{L-99101.6}
\]

For squared energy the corresponding rates and gap are doubled.

This optimization is independent of the order of the zero, of `theta`, and of all subexponential factors. It identifies the exact phase saving which an arithmetic proof must supply after the best scalar Hermite notch has already been applied.
