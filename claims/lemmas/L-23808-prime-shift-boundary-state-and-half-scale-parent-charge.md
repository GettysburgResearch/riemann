# L-23808 — Prime-shift boundary state and half-scale parent charge

Claim ID: `L-23808`  
Status: `PROPOSED — exact identities; global charge-capacity theorem open`  
Scope: direct attack on `L-23805` Gamma–carry positivity  
RH status: **unproved**

Put

\[
h_0(t)=\left(e^t-\frac78e^{t/2}-\frac3{16}t e^{t/2}\right)\mathbf1_{t\ge0}
\]

and define the actual prime-shift state

\[
\boxed{
G(t)=\prod_{p\le e^t}(I-\tau_{\log p})h_0(t)
=\sum_{n\le e^t}\mu(n)h_0(t-\log n).
}
\tag{L-23808.1}
\]

By `L-23805`,

\[
G(t)=e^t a(t),
\]

so `G(t)>=0` for all `t>=0` is exactly the global Gamma–carry factor positivity theorem.

## 1. Exact quotient-layer state

Fix an integer `r>=1` and `log r<=t<log(r+1)`. Put

\[
A_r=\sum_{n\le r}\frac{\mu(n)}n,
\quad
B_r=\sum_{n\le r}\frac{\mu(n)}{\sqrt n},
\quad
C_r=\sum_{n\le r}\frac{\mu(n)\log n}{\sqrt n}.
\]

Then exactly

\[
\boxed{
G(t)
=A_re^t+e^{t/2}\left[
-\frac78B_r-\frac3{16}tB_r+\frac3{16}C_r
\right].
}
\tag{L-23808.2}
\]

Thus every open quotient layer is one three-dimensional exponential-polynomial trajectory. There is no interior combinatorial complexity left.

At the knot `t=log r`, the new term enters with

\[
h_0(0)=\frac18,
\]

hence

\[
\boxed{
G((\log r)^+)-G((\log r)^-)=\frac{\mu(r)}8.
}
\tag{L-23808.3}
\]

This is the complete boundary ledger. All downward jumps occur exactly at squarefree integers with `mu(r)=-1`.

## 2. Interior ODE

On every open layer,

\[
\boxed{(\partial_t-1)(\partial_t-1/2)^2G(t)=0.}
\tag{L-23808.4}
\]

Therefore a production proof can treat the interior exactly and must spend all arithmetic effort on the knot jumps. In particular the boundary cannot be discarded as a lower-order remainder.

## 3. Exact negative-jump parent decomposition

The Dirichlet identity

\[
\boxed{(\Lambda*\mu)(n)=-\mu(n)\log n}
\tag{L-23808.5}
\]

holds for every integer `n>=2`.

If `mu(n)=-1`, then `n` is squarefree with an odd number of prime factors, and (L-23808.5) becomes the positive convex decomposition

\[
\boxed{
1=\sum_{p\mid n}\frac{\log p}{\log n},
\qquad
\mu(n/p)=+1.
}
\tag{L-23808.6}
\]

Consequently the downward boundary charge has the exact parent representation

\[
\boxed{
-\frac18
=-\sum_{p\mid n}\frac{\log p}{\log n}\frac18,
}
\tag{L-23808.7}
\]

where every parent index satisfies

\[
\boxed{n/p\le n/2.}
\tag{L-23808.8}
\]

Thus every negative boundary atom routes with positive weights to favorable boundary states at a strict half scale. No signed or same-scale parent is needed at the local charge level.

## 4. Seed capacity

For `x>=1`, set

\[
f(x)=h_0(\log x)=x-\frac78\sqrt x-\frac3{16}\sqrt x\log x.
\]

The elementary inequality

\[
\boxed{f(x)\ge \frac x8\qquad(x\ge1)}
\tag{L-23808.9}
\]

follows after dividing by `sqrt(x)`, writing `u=sqrt(x)>=1`, and checking that

\[
\frac78u-\frac78-\frac38\log u\ge0
\]

has nonnegative derivative for `u>=1`.

Hence a favorable parent active at multiplicative horizon `x` carries at least `x/8` raw positive mass, whereas each child boundary atom costs exactly `1/8` before the logarithmic parent weights in (L-23808.6).

This is the first genuine capacity reserve in the boundary route.

## 5. What is still missing

One positive parent can feed many negative children, so (L-23808.6)--(L-23808.9) do not by themselves prove that the total routed demand stays below parent capacity. A valid completion needs a **global no-double-spend ledger**.

The required ledger must use the strict half-scale routing and the actual continuous growth of each parent state between its birth and its children. It may not simply reuse the same `f(x)` mass independently for every child.

The proposed closing theorem is isolated in `T-23802`.

## Review boundary

Exact here:

- prime-shift identity;
- three-state quotient-layer formula;
- knot jump `mu(r)/8`;
- interior ODE;
- positive half-scale parent decomposition of every negative jump;
- elementary `x/8` parent capacity reserve.

Open:

- a global disjoint/Carleson charge allocation proving that no parent capacity is overspent;
- Gamma–carry positivity;
- RH.
