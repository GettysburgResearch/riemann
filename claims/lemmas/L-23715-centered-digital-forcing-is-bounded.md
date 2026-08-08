# L-23715 — The centered base-five digital forcing is bounded

Claim ID: `L-23715`  
Title: Subtracting the explicit linear cumulative mode cancels the complete logarithmic growth of the base-five digital forcing  
Status: **PROPOSED COMPLETE ELEMENTARY ANALYTIC LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Dependencies: `L-23709`, `L-23708`  
Scope: exact centering and elementary Abel estimates; no RH input

## 1. Digital coefficients and their partial sums

Put

\[
c_5(n)=1-4v_5(n),
\qquad
S_5(N)=\sum_{n\le N}c_5(n)=s_5(N),
\]

where `s_5(N)` is the base-five digit sum. Hence

\[
0\le S_5(N)\le4(1+\log_5N).
\tag{L-23715.1}
\]

Define

\[
A(y)=\sum_{m\le y}\frac{c_5(m)}{\sqrt m},
\qquad
B(y)=\sum_{m\le y}\frac{c_5(m)\log m}{\sqrt m}.
\tag{L-23715.2}
\]

Finite Abel summation and (L-23715.1) show that both series converge as `y->infinity`:

\[
A_\infty=\sum_{m\ge1}\frac{c_5(m)}{\sqrt m},
\qquad
B_\infty=\sum_{m\ge1}\frac{c_5(m)\log m}{\sqrt m},
\tag{L-23715.3}
\]

with the explicit error bounds

\[
\boxed{
A(y)=A_\infty+O\left(\frac{1+\log y}{\sqrt y}\right),
}
\tag{L-23715.4}
\]

\[
\boxed{
B(y)=B_\infty+O\left(\frac{(1+\log y)^2}{\sqrt y}\right).
}
\tag{L-23715.5}
\]

All implied constants are absolute and may be made explicit from the digit bound.

## 2. Exact value of the leading coefficient

The Dirichlet series of `c_5` is

\[
C_5(s)
=\zeta(s)\frac{1-5^{1-s}}{1-5^{-s}}.
\tag{L-23715.6}
\]

The convergence proved above permits evaluation at `s=1/2`, giving

\[
\boxed{
A_\infty=C_5(1/2)=-\sqrt5\,\zeta(1/2)>0.
}
\tag{L-23715.7}
\]

Let

\[
\boxed{
a_5=-\frac{1-5^{-1/2}}{\zeta(1/2)}>0.
}
\tag{L-23715.8}
\]

Then

\[
\boxed{
a_5A_\infty=\sqrt5-1.}
\tag{L-23715.9}
\]

This is the exact cancellation of the logarithmic forcing slope.

## 3. Centered shell

Let

\[
C(y)=\mathfrak S_5(y)
\]

and define

\[
\boxed{
Z(y)=C(y)-a_5\log y.
}
\tag{L-23715.10}
\]

The digital convolution identity in `L-23709` is

\[
\sum_{m\le y}\frac{c_5(m)}{\sqrt m}C(y/m)=R_5(y).
\]

Therefore

\[
\boxed{
\sum_{m\le y}\frac{c_5(m)}{\sqrt m}Z(y/m)=F_5(y),
}
\tag{L-23715.11}
\]

where the centered forcing is explicitly

\[
\boxed{
F_5(y)
=R_5(y)-a_5\left[(\log y)A(y)-B(y)\right].
}
\tag{L-23715.12}
\]

For `y>=5`,

\[
R_5(y)=(\sqrt5-1)\log y+r_5,
\qquad
r_5=4(\sqrt5-1)-\sqrt5\log5.
\]

Using (L-23715.4)--(L-23715.9),

\[
\boxed{
F_5(y)=F_{5,\infty}
+O\left(\frac{(1+\log y)^2}{\sqrt y}\right),
}
\tag{L-23715.13}
\]

with

\[
\boxed{
F_{5,\infty}=r_5+a_5B_\infty.
}
\tag{L-23715.14}
\]

In particular,

\[
\boxed{
F_5(y)=O(1)
\qquad(y\ge1).
}
\tag{L-23715.15}
\]

No zeta-zero estimate enters this boundedness theorem. The cancellation uses only the explicit principal part and the base-five digit partial sums.

## 4. Review meaning

The positive logarithmic forcing in the uncentered Abel recurrence is the known main mode. After it is removed, the remaining digital forcing is bounded rather than of logarithmic size. This is the correct normalization for an `O(log y)` boundary-energy theorem.

The result does not assert that `Z` is bounded or positive. It identifies the finite forcing against which the centered lower-scale recurrence must be solved.

## 5. Proof boundary

Closed here:

- convergence and rates of the two digital weighted sums;
- exact evaluation of their leading coefficient;
- cancellation of the complete logarithmic forcing;
- boundedness of the centered forcing.

Open:

- a centered digital boundary-energy bound;
- eventual positivity of `C` from that bound;
- Greedy Slack/DCRS;
- RH.
