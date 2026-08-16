# L-94200 — The radix-four dual pairs the native target with the prime-power ramp, not with the parabolic seed

Claim ID: `L-94200`
Status: **PROVED EXACT FINITE ALGEBRA**
Created: 2026-08-16
RH status: **unproved**

## 1. The finite radix-four adjoint

For a finitely supported sequence \(C(q)\), put

\[
(\mathcal D_4 C)(q)=C(q)-2C(4q),
\]

with zero extension. Define

\[
Y_4(q)=\sum_{\substack{j\ge0\\4^j\mid q}}
2^j\Lambda(q/4^j).
\]

Equivalently,

\[
Y_4(q)-2\mathbf 1_{4\mid q}Y_4(q/4)=\Lambda(q).
\]

Finite reindexing gives

\[
\begin{aligned}
\sum_qY_4(q)(\mathcal D_4C)(q)
&=\sum_qY_4(q)C(q)-2\sum_qY_4(q)C(4q)\\
&=\sum_q\bigl(Y_4(q)-2\mathbf 1_{4\mid q}Y_4(q/4)\bigr)C(q)\\
&=\boxed{\sum_q\Lambda(q)C(q)}.
\end{aligned}
\tag{L-94200.1}
\]

No positivity, limit, or analytic continuation is used.

## 2. Apply the adjoint to the native target

Let

\[
w_X(q)=q^{-1/2}\log(X/q)\mathbf 1_{q\le X},
\qquad
\Omega_X=\mathcal D_4w_X.
\]

Then

\[
\boxed{
\langle Y_4,\Omega_X\rangle
=\sum_{q\le X}\frac{\Lambda(q)}{\sqrt q}\log(X/q)
=:P_\Lambda(X).
}
\tag{L-94200.2}
\]

Thus the positive native detail benchmark is dual to the complete prime-power
ramp \(P_\Lambda\).

## 3. Apply the adjoint to a physical row

For a finite nonnegative physical row \(d\), let \(C_d(q)\) be its ordinary
response and

\[
\Xi_d=\mathcal D_4C_d.
\]

The exact average-binomial entropy identity is

\[
\mathcal H(d)=\sum_q\Lambda(q)C_d(q).
\]

Therefore (L-94200.1) gives

\[
\boxed{
\mathcal H(d)=\langle Y_4,\Xi_d\rangle.
}
\tag{L-94200.3}
\]

Subtracting (L-94200.3) from (L-94200.2),

\[
\boxed{
\langle Y_4,\Omega_X-\Xi_d\rangle
=P_\Lambda(X)-\mathcal H(d).
}
\tag{L-94200.4}
\]

The right side is the weighted residual packing slack. It is **not**
\(J_\Lambda(X)-\mathcal H(d)\).

## 4. Boundary

```text
radix-four adjoint identity                exact
native target pairing                      P_Lambda(X)
physical row pairing                       H(d)
weighted detail slack                      P_Lambda(X)-H(d)
pairing with J_Lambda(X)                   false unless F_Lambda(X)=0
Riemann Hypothesis                         unproved
```
