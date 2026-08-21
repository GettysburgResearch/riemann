# L-32406 — The tau-one Jordan pole filter has deterministic parity sign

Claim ID: `L-32406`  
Title: Dyadically canceling the real pole of the positive Euler-totient quotient produces `eta(s-1)/zeta(s)` with coefficients positive exactly on odd integers and negative exactly on even integers  
Status: **PROPOSED COMPLETE EXACT ARITHMETIC LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: `L-32405`; elementary identities for Euler's totient  
Scope: exact coefficients, floor potential, carry profile, and Riesz transform; no eventual sign theorem

## 1. Start from the positive Jordan source at tau=1

At `tau=1`, `L-32405` gives

\[
 J_1(n)=\varphi(n)>0
\]

and

\[
 \sum_{n\ge1}{\varphi(n)\over n^s}
 ={\zeta(s-1)\over\zeta(s)}.
\tag{L-32406.1}
\]

The numerator has its real pole at `s=2`.

Multiply by the exact dyadic pole-killing factor

\[
 1-2^{2-s}.
\]

Since

\[
 \eta(s-1)=(1-2^{2-s})\zeta(s-1),
\]

one obtains

\[
\boxed{
 {\eta(s-1)\over\zeta(s)}.
}
\tag{L-32406.2}
\]

## 2. Exact coefficient formula

Let `c` be the coefficient sequence of (L-32406.2). Multiplication by the finite Euler polynomial gives

\[
\boxed{
 c(n)=\varphi(n)-4\mathbf1_{2\mid n}\varphi(n/2).
}
\tag{L-32406.3}
\]

Write

\[
 n=2^k m,
 \qquad m\text{ odd}.
\]

Using

\[
 \varphi(2^km)=
 \begin{cases}
 \varphi(m),&k=0,\\
 2^{k-1}\varphi(m),&k\ge1,
 \end{cases}
\]

one gets

\[
\boxed{
 c(2^km)=
 \begin{cases}
 \varphi(m),&k=0,\\
 -3\varphi(m),&k=1,\\
 -2^{k-1}\varphi(m),&k\ge2.
 \end{cases}}
\tag{L-32406.4}
\]

Hence

\[
\boxed{
 c(n)>0\iff n\text{ is odd},
 \qquad
 c(n)<0\iff n\text{ is even}.
}
\tag{L-32406.5}
\]

There are no zero coefficients.

Equivalently,

\[
 c=\mu*a,
 \qquad
 a(n)=(-1)^{n-1}n,
\tag{L-32406.6}
\]

because the Dirichlet series of `a` is `eta(s-1)`.

## 3. Exact floor potential

Define

\[
 H(n)=\sum_{q\le n}c(q)\left\lfloor{n\over q}\right\rfloor.
\]

Since `1*c=a`,

\[
 H(n)=\sum_{m=1}^n(-1)^{m-1}m.
\]

Thus

\[
\boxed{
 H(2r)=-r,
 \qquad
 H(2r+1)=r+1.
}
\tag{L-32406.7}
\]

Equivalently,

\[
 H(n)={1-(-1)^n(2n+1)\over4}.
\tag{L-32406.8}
\]

## 4. Exact carry profile

For a split `n=j+k`,

\[
 Y(n,j)=H(n)-H(j)-H(k).
\]

A parity case split gives:

### Even parent

If `n` is even and `j,k` are even,

\[
\boxed{Y(n,j)=0.}
\tag{L-32406.9}
\]

If `n` is even and `j,k` are odd,

\[
\boxed{Y(n,j)=-(n+1).}
\tag{L-32406.10}
\]

### Odd parent

Exactly one child is even. If the even child is `e`, then

\[
\boxed{Y(n,j)=e>0.}
\tag{L-32406.11}
\]

Thus the pole-filtered totient source has a completely deterministic parity carry geometry:

```text
even -> even+even       zero;
even -> odd+odd         strictly negative;
odd  -> even+odd        strictly positive, equal to the even child.
```

No Möbius sign remains in this carry table.

## 5. Riesz scalar as one dyadic totient defect

Define the positive totient Riesz mean

\[
 P(X)=\sum_{n\le X}{\varphi(n)\over\sqrt n}\log{X\over n}.
\tag{L-32406.12}
\]

Then (L-32406.3) gives the exact filtered scalar

\[
\boxed{
 D_\varphi(X)
 :=\sum_{n\le X}{c(n)\over\sqrt n}\log{X\over n}
 =P(X)-2\sqrt2\,P(X/2).
}
\tag{L-32406.13}
\]

The leading `X^(3/2)` pole of the positive totient source has canceled exactly.

Initially for `Re z>3/2`, Mellin transformation gives

\[
\boxed{
 \int_1^\infty D_\varphi(X)X^{-z-1}dX
 ={\eta(z-1/2)\over z^2\zeta(z+1/2)}.
}
\tag{L-32406.14}
\]

The real numerator pole is absent because `eta` is entire.

## 6. Off-line zero firewall

Let `rho` be a nontrivial zeta zero with `Re rho>1/2` and put `z_rho=rho-1/2`.

The numerator at that point is

\[
 \eta(\rho-1).
\]

It is nonzero. Indeed:

1. `zeta(rho-1)` cannot be a nontrivial zero because `Re(rho-1)<0`;
2. it cannot be a trivial zero because `rho-1` is nonreal;
3. the finite eta factor vanishes only when `rho=2-2\pi i k/\log2`, whose real part is two.

Therefore every off-critical zeta zero remains an uncancelled nonreal pole of (L-32406.14).

## 7. Proof boundary

Closed exactly:

- dyadic cancellation of the totient real pole;
- deterministic parity coefficient signs;
- explicit floor potential;
- complete carry-profile table;
- one-scalar dyadic totient Riesz formula;
- Mellin pole firewall.

Open:

- an eventual one-sided theorem for `D_phi(X)`;
- RH.
