# L-22801 — Completed Möbius–Farey packet for the analytic totient error

Claim ID: `L-22801`  
Title: The complete analytic-totient error splits into an exact reduced-Farey packet, two endpoint channels, and the positive Jordan Bohr energy  
Status: **PROPOSED PENDING INDEPENDENT REVIEW — exact algebra supplied**  
Authoring agent: `gpt56-pro-20`  
Created: 2026-08-07  
Issue: #228  
Frozen parent: draft PR #226 at `53f2cba370fa518d5d12488b5b9948c1826bba88`  
Dependencies: `L-9512`, `L-9513`; elementary Fourier series and Möbius inversion

## 1. The complete packet

Let

\[
f(t)=\{t\}^2-\frac13
\]

and, for an integer `D>=2`, define

\[
S_D(x)=\sum_{d\le D}\mu(d)f(x/d),
\qquad
M_D=\sum_{d\le D}\mu(d),
\qquad
R_D=\sum_{d>D}\frac{\mu(d)}{d^2}.
\tag{L-22801.1}
\]

For `0<=x<=D`, every denominator `d>D` satisfies `{x/d}=x/d`. Therefore the analytic totient error of `L-9512` has the exact finite-plus-tail representation

\[
\boxed{
2E^{\rm AN}(x)
=1+S_D(x)+\frac{M_D}{3}+x^2R_D.}
\tag{L-22801.2}
\]

The two terms `M_D/3` and `x^2R_D` are not optional remainders. They are the zero-frequency and exterior-denominator channels of the same Möbius packet. Any local-energy argument which estimates them separately loses the critical scale.

Put

\[
\mathscr C_D(x)
=1+S_D(x)+\frac{M_D}{3}+x^2R_D.
\tag{L-22801.3}
\]

Then `mathscr C_D=2E^AN` on the entire interval `[0,D]`.

## 2. Reduced Farey coefficients

With the Fourier convention `e(t)=exp(2*pi*i*t)`, one has in `L2([0,1])`

\[
f(t)=\sum_{h\ne0}c_h e(ht),
\qquad
c_h=\frac{i}{2\pi h}+\frac1{2\pi^2h^2}.
\tag{L-22801.4}
\]

Every nonzero rational frequency can be written uniquely as `a/q`, where `q>=1`, `a` is a nonzero integer, and `(a,q)=1`. Writing `d=qg`, `h=ag`, the coefficient of `e(ax/q)` in `S_D` is

\[
b_D(a/q)=\sum_{g\le D/q}\mu(qg)c_{ag}.
\tag{L-22801.5}
\]

Define the divisor-tail coordinates

\[
U_q(D)=\sum_{\substack{d\le D\\q\mid d}}\frac{\mu(d)}d,
\qquad
V_q(D)=\sum_{\substack{d\le D\\q\mid d}}\frac{\mu(d)}{d^2}.
\tag{L-22801.6}
\]

Then (L-22801.5) becomes the exact formula

\[
\boxed{
b_D(a/q)
=\frac{iq}{2\pi a}U_q(D)
 +\frac{q^2}{2\pi^2a^2}V_q(D).}
\tag{L-22801.7}
\]

This is the key arithmetic coordinate change. All dependence on the numerator `a` is explicit; all Möbius cancellation is carried by the two finite divisor coordinates `U_q,V_q`.

## 3. Exact Bohr/Jordan energy

The complete Bohr mean of `S_D` is

\[
\mathcal B_D
=\lim_{T\to\infty}\frac1T\int_0^T|S_D(x)|^2dx
=\sum_{q\le D}\sum_{\substack{a\ne0\\(a,q)=1}}|b_D(a/q)|^2.
\tag{L-22801.8}
\]

Because the first term in (L-22801.7) is purely imaginary and odd in `a`, while the second is real and even, their cross term vanishes. The classical coprime sums are

\[
\sum_{\substack{a\ne0\\(a,q)=1}}\frac1{a^2}
=\frac{\pi^2}{3}\frac{J_2(q)}{q^2},
\qquad
\sum_{\substack{a\ne0\\(a,q)=1}}\frac1{a^4}
=\frac{\pi^4}{45}\frac{J_4(q)}{q^4}.
\tag{L-22801.9}
\]

Consequently

\[
\boxed{
\mathcal B_D
=\frac1{12}\sum_{q\le D}J_2(q)U_q(D)^2
 +\frac1{180}\sum_{q\le D}J_4(q)V_q(D)^2.}
\tag{L-22801.10}
\]

This reproduces `L-9513` directly from the reduced-Farey coefficients. In particular,

\[
\boxed{\mathcal B_D\ll D}
\tag{L-22801.11}
\]

unconditionally.

## 4. A fixed bandlimited interval majorant

Let

\[
W(y)=\frac{\pi^2}{8}
\left(
 \frac{\sin\pi(y-3/4)}{\pi(y-3/4)}
\right)^2.
\tag{L-22801.12}
\]

On `[1/2,1]`, the squared sinc decreases from its center to the endpoints and has endpoint value `8/pi^2`; hence

\[
W(y)\ge1\qquad(1/2\le y\le1).
\tag{L-22801.13}
\]

With the Fourier convention `hat W(xi)=int W(y)e(-xi*y)dy`, its transform is a translated triangular function supported in `[-1,1]`. Therefore

\[
\int_{D/2}^{D}|\mathscr C_D(x)|^2dx
\le
\int_{\mathbb R}W(x/D)|\mathscr C_D(x)|^2dx
\tag{L-22801.14}
\]

and the nonzero-frequency part couples only reduced Farey frequencies separated by at most `1/D`.

## 5. Critical clusters

For `k in Z`, define the critical frequency cell

\[
I_{D,k}=\left[\frac{k-1/2}{D},\frac{k+1/2}{D}\right).
\tag{L-22801.15}
\]

Let

\[
B_{D,k}=\sum_{a/q\in I_{D,k}}b_D(a/q),
\tag{L-22801.16}
\]

where every rational is in reduced form. The finite-support property of `hat W` reduces the nonzero-frequency contribution in (L-22801.14) to the common-cell and adjacent-cell Gram of the sequence `(B_(D,k))`.

The cells near `k=0` must be combined with the polynomial channel

\[
P_D(x)=1+M_D/3+x^2R_D.
\tag{L-22801.17}
\]

The identity

\[
\sum_{d\le x}\mu(d)\left\lfloor\frac xd\right\rfloor=1
\qquad(x\ge1)
\tag{L-22801.18}
\]

is the exact endpoint cancellation which couples `P_D` to the low Farey cells. This is why an isolated bound on `M_D` or `R_D` is both unnecessary and exponentially too weak.

## 6. Proof boundary

Closed in this lemma:

- the complete finite-plus-tail identity;
- the exact reduced-Farey coefficient formula;
- the exact positive Jordan/Bohr factorization;
- the fixed bandlimited localization interface;
- identification of the endpoint channels that must remain coupled.

Not closed here:

- the critical local-to-Bohr contraction for the Farey cells and endpoint channel.

That contraction is stated and proved as the new load-bearing theorem `T-22801`. A reviewer should reject any proof which silently deletes `P_D`, treats the low cluster by absolute values, or replaces the physical interval by the full common period.