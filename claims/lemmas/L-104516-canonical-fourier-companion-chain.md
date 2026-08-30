# L-104516 — Canonical one-sided Fourier companions form an exact derivative chain

Claim ID: `L-104516`  
Status: **PROVED EXACT**  
Created: 2026-08-22  
Depends on: the classical positive Fourier representation of Xi  
RH status: **not assumed**

Use

\[
\Xi(z)=2\int_0^\infty \Phi(u)\cos(zu)\,du,
\qquad
\Phi(u)>0.
\]

For every integer `m>=0`, define

\[
M_m=\int_0^\infty u^m\Phi(u)\,du
\]

and the one-sided Fourier companion

\[
\boxed{
\mathscr E_m(z)
=
i^m\int_0^\infty u^m\Phi(u)e^{izu}\,du.
}
\tag{L-104516.1}
\]

All integrals define entire functions because `Phi` has double-exponential
decay.

## 1. Exact derivative ladder

Differentiation under the integral gives

\[
\boxed{
\mathscr E_m'(z)=\mathscr E_{m+1}(z).
}
\tag{L-104516.2}
\]

Thus the one-sided Fourier companions form an exact derivative chain.  No
scalar parameter `lambda`, moving normalization or approximate covariance is
introduced.

## 2. Xi derivatives are the reflected real parts

Since

\[
\Xi(z)
=
\int_0^\infty\Phi(u)e^{izu}\,du
+
\int_0^\infty\Phi(u)e^{-izu}\,du,
\]

one obtains

\[
\boxed{
\Xi^{(m)}(z)
=
\mathscr E_m(z)+(-1)^m\mathscr E_m(-z).
}
\tag{L-104516.3}
\]

For real `x`,

\[
(-1)^m\mathscr E_m(-x)=\overline{\mathscr E_m(x)},
\]

and hence

\[
\boxed{
\Xi^{(m)}(x)=2\Re\mathscr E_m(x).
}
\tag{L-104516.4}
\]

The critical-line zero problem is therefore a phase-crossing problem for one
canonical analytic signal.

## 3. Native normalization

Let

\[
d\nu_m(u)=M_m^{-1}u^m\Phi(u)\,du
\]

and put

\[
A_m(z)=\int_0^\infty e^{izu}\,d\nu_m(u).
\]

Then

\[
\mathscr E_m(z)=i^mM_mA_m(z),
\]

and

\[
\boxed{
A_m'(z)
=
i\mu_m A_{m+1}(z),
\qquad
\mu_m={M_{m+1}\over M_m}>0.
}
\tag{L-104516.5}
\]

The positive sequence `mu_m` is the exact moment-ratio frequency.  Log
convexity of the moments gives

\[
\mu_{m+1}\ge\mu_m.
\]

## 4. Boundary-at-infinity antiderivative

For `Im z>0`, the one-sided transform decays along a vertical ray.  Hence

\[
\boxed{
\mathscr E_m(z)
=
-\int_z^{z+i\infty}\mathscr E_{m+1}(w)\,dw,
}
\tag{L-104516.6}
\]

where the integral is taken vertically and converges absolutely.

This is the complex analogue of selecting the native integration constant.
Unlike a free polynomial antiderivative, the Xi companion is pinned by its
positive-frequency boundary condition.

## Scope

The theorem supplies:

```text
one canonical companion at every derivative order;
exact derivative covariance;
exact reflected recovery of Xi^(m);
a positive tilted measure;
and a native antiderivative boundary condition.
```

It does not assert that every `mathscr E_m` is Hermite--Biehler or zero-free in
a complete half-plane.  The unconditional high-order zero-free band is
`L-104517`.
