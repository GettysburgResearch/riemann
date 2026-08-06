# L-20201 — Exact prime formula for the Haar renormalization defect

Claim ID: `L-20201`  
Title: The dyadic screw defect is one finite two-scale prime-power inequality with a positive Lerch remainder  
Status: `PROPOSED — COMPLETE ALGEBRAIC CONSEQUENCE OF THE IMPORTED SCREW FORMULA`  
Authoring agent: `gpt56-pro-09-n`  
Created: 2026-08-07  
Dependencies: the exact finite formula for `Psi` in `L-19801`; elementary Lerch-series algebra  
Scope: every integer `n>=2`

## 1. Exact finite formula

Let

\[
 C_\Gamma=\psi(1/4)-\log\pi
\]

and abbreviate

\[
 \Phi(z)=\Phi(z,2,1/4).
\]

For an integer `n>=2`, put

\[
 \mathcal H(n)=\mathcal D(\log n)
 =4\Psi(\log n)-\Psi(2\log n).
\]

Substitution into the Nakamura–Suzuki finite formula gives

\[
\boxed{
\begin{aligned}
\mathcal H(n)={}&
 -4\left(\sqrt n+n^{-1/2}-2\right)^2
 +C_\Gamma\log n\\
&+\sum_{q\le n}\frac{\Lambda(q)}{\sqrt q}
  \log\frac{q^3}{n^2}
 +\sum_{n<q\le n^2}\frac{\Lambda(q)}{\sqrt q}
  \log\frac{n^2}{q}\\
&-n^{-1/2}\Phi(n^{-2})
 +\frac1{4n}\Phi(n^{-4})
 +\frac34\Phi(1).
\end{aligned}}
\tag{1}
\]

Both sums range over every prime power, with `Lambda(p^a)=log p`. Thus each level is a finite exact arithmetic object through `n^2`.

## 2. Derivation of the prime weights

Write

\[
 P(t)=\sum_{q\le e^t}
 \frac{\Lambda(q)}{\sqrt q}(t-\log q).
\]

The prime part of `Psi` is `-P(t)`, so the prime contribution to the defect is

\[
 P(2t)-4P(t).
\]

At `t=log n`, a term `q<=n` has weight

\[
 (2\log n-\log q)-4(\log n-\log q)
 =\log(q^3/n^2),
\]

while a term `n<q<=n^2` has weight `log(n^2/q)`. This proves the two finite sums in (1).

The sign split is explicit:

\[
\boxed{
 w_n(q)<0\iff q<n^{2/3},
 \qquad
 w_n(q)\ge0\iff n^{2/3}\le q\le n^2.}
\tag{2}
\]

Thus the entire negative prime channel is confined to the old prefix below `n^(2/3)`; every prime power from `n^(2/3)` through `n^2` enters positively.

## 3. Prefix-moment form

Define

\[
 A(x)=\sum_{q\le x}\frac{\Lambda(q)}{\sqrt q},
 \qquad
 B(x)=\sum_{q\le x}\frac{\Lambda(q)\log q}{\sqrt q}.
\]

Then the complete prime term in (1) is exactly

\[
\boxed{
 2\log n\,A(n^2)-4\log n\,A(n)+4B(n)-B(n^2).}
\tag{3}
\]

This permits a single complete prime-power stream with reusable prefix moments.

## 4. Pole square

The polar terms simplify without approximation:

\[
\begin{aligned}
&16(\sqrt n+n^{-1/2}-2)
 -4(n+n^{-1}-2)\\
&\qquad=-4(\sqrt n+n^{-1/2}-2)^2.
\end{aligned}
\tag{4}
\]

The pole channel is therefore one exact negative square.

## 5. Positive Lerch factorization

Using

\[
 \Phi(z)=\sum_{k=0}^\infty\frac{z^k}{(k+1/4)^2},
\]

set

\[
 y_k=n^{-1/2-2k}.
\]

The complete Lerch combination in (1) is

\[
\begin{aligned}
&-n^{-1/2}\Phi(n^{-2})
 +\frac1{4n}\Phi(n^{-4})
 +\frac34\Phi(1)\\
&\quad=\frac14\sum_{k=0}^\infty
 \frac{(1-y_k)(3-y_k)}{(k+1/4)^2}.
\end{aligned}
\tag{5}
\]

Since `0<y_k<1` for `n>=2`, every summand is positive. Therefore

\[
\boxed{
 \mathcal L_{\rm Haar}(n)>0.}
\tag{6}
\]

This isolates the sign competition in (1): a negative pole square and the low-prime prefix oppose the positive high-prime band, positive Lerch series, and the fixed gamma term.

## 6. Exact relation to the square-screw matrix coordinate

Let

\[
 \mathcal S(M)=\Psi(2\log M)
\]

be the square-screw scalar of `L-20704`. Then

\[
\boxed{
 \mathcal H(n)=4\mathcal S(\sqrt n)-\mathcal S(n),}
\tag{7}
\]

where the first term means the same continuous screw statistic at support `n`, not necessarily an integer square-screw level.

In the original continuous variable this is simply the Haar second difference

\[
 \mathcal H(e^t)=4\Psi(t)-\Psi(2t).
\]

The scalar matrix coordinate and the dyadic defect are therefore two resolutions of the same global screw function rather than unrelated criteria.

## 7. Proof-producing implications

A production certificate for one level needs:

1. a complete prime-power manifest through `n^2`;
2. directed `log q`, `sqrt q`, and weighted accumulation;
3. directed gamma and pole terms;
4. a finite partial Lerch sum plus the positive monotone tail from (5);
5. a strict final interval.

A finite negative level does **not** disprove RH: `T-20201` requires eventual or subpower control. The formula is designed for symbolic/cofinal estimates and scalable reconnaissance, not finite overclaiming.
