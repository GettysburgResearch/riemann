# L-23812 — Binary–ternary flow: exact half-moment collapse

Claim ID: `L-23812`  
Title: A nonnegative binary–ternary producer has subpolynomial weighted variation if and only if one explicit Möbius half-moment is subpolynomial  
Status: **PROPOSED EXACT LEMMA — COMPLETE FINITE ALGEBRA; POSITIVITY AND RATE NOT ASSERTED**  
Authoring agent: `gpt56-pro-09-w`  
Created: 2026-08-08  
Issue: #238  
Dependencies: `L-23810`, `L-23811`  
Scope: exact audit and simplification of the `BTF` hinge

## 1. Binary–ternary producer

Let `r_X(1),...,r_X(X)` be the exact node divergence of `L-23810`, and let
`A_X(n)` be the unique descending producer of `L-23811`.  Thus one half of
`A_X(n)` is sent through the central binary split

\[
 n=\lfloor n/2\rfloor+\lceil n/2\rceil,
\]

and one half through the balanced ternary split

\[
 n=\lceil n/3\rceil+\bigl(n-\lceil n/3\rceil\bigr).
\]

The resulting fragmentation divergence is exactly `r_X`.

For `0<theta<1`, put

\[
\begin{aligned}
\Delta_\theta(n)={}&\frac12\left[
 \lfloor n/2\rfloor^\theta+\lceil n/2\rceil^\theta-n^\theta
 \right]\\
&+\frac12\left[
 \lceil n/3\rceil^\theta+
 \bigl(n-\lceil n/3\rceil\bigr)^\theta-n^\theta
 \right].
\end{aligned}
\tag{L-23812.1}
\]

Concavity gives `Delta_theta(n)>0` for every `n>=2`.

## 2. Exact moment identity

For every real function `f` on `{1,...,X}`, the divergence identity gives

\[
\begin{aligned}
\sum_{m=1}^X r_X(m)f(m)
={}&\sum_{n=2}^X A_X(n)\bigg[
 f(n)
 -\frac{f(\lfloor n/2\rfloor)+f(\lceil n/2\rceil)}2\\
&\hspace{35mm}
 -\frac{f(\lceil n/3\rceil)
       +f(n-\lceil n/3\rceil)}2
 \bigg].
\end{aligned}
\tag{L-23812.2}
\]

Taking `f(m)=m^theta` yields

\[
\boxed{
 -\sum_{m=1}^X r_X(m)m^\theta
 =\sum_{n=2}^X A_X(n)\Delta_\theta(n).}
\tag{L-23812.3}
\]

No positivity assumption is used in this equality.

## 3. Uniform square-root defect

At `theta=1/2`, every child ratio in both declared splits lies in
`[1/3,2/3]`.  Hence

\[
 \sqrt a+\sqrt{n-a}-\sqrt n
 \ge
 \left(\frac1{\sqrt3}+\sqrt{\frac23}-1\right)\sqrt n
\]

for each split, while concavity gives the upper bound

\[
 \sqrt a+\sqrt{n-a}-\sqrt n
 \le(\sqrt2-1)\sqrt n.
\]

Consequently, with

\[
 \kappa_-:=\frac1{\sqrt3}+\sqrt{\frac23}-1>0,
 \qquad
 \kappa_+:=\sqrt2-1,
\]

one has

\[
\boxed{
 \kappa_-\sqrt n
 \le\Delta_{1/2}(n)
 \le\kappa_+\sqrt n
 \qquad(n\ge2).}
\tag{L-23812.4]
\]

(The closing bracket in the displayed tag is typographical Markdown only; the
mathematical statement is (L-23812.4).)

Define the scalar half-moment

\[
\boxed{
 \mathfrak H_X
 :=-\sum_{m=1}^X r_X(m)\sqrt m.}
\tag{L-23812.5}
\]

If the producer is nonnegative,

\[
 A_X(n)\ge0\qquad(2\le n\le X),
\tag{L-23812.6}
\]

then (L-23812.3)--(L-23812.4) give the two-sided comparison

\[
\boxed{
 \kappa_-\sum_{n=2}^XA_X(n)\sqrt n
 \le\mathfrak H_X
 \le\kappa_+\sum_{n=2}^XA_X(n)\sqrt n.}
\tag{L-23812.7}
\]

Thus, under producer positivity,

\[
\boxed{
 \sum_{n=2}^XA_X(n)\sqrt n=X^{o(1)}
 \quad\Longleftrightarrow\quad
 \mathfrak H_X=X^{o(1)}.}
\tag{L-23812.8}
\]

The weighted-variation condition in `BTF` is therefore not an independent
large family of estimates once positivity is known.  It is one scalar
Möbius-sensitive moment.

## 4. Exact target-coordinate formula

Let

\[
 a_\theta(m)=m^\theta-(m-1)^\theta,
\]

and define

\[
 h_\theta(q)=\sum_{d\mid q}\mu(d)
 a_\theta(q/d).
\tag{L-23812.9}
\]

Then Möbius inversion gives, for every integer `m>=1`,

\[
 m^\theta=\sum_{q\le m}h_\theta(q)
 \left\lfloor\frac mq\right\rfloor.
\tag{L-23812.10}
\]

Since the target floor transform is

\[
 w_X(q)=\sum_{m=1}^Xr_X(m)\left\lfloor\frac mq\right\rfloor,
 \qquad w_X(1)=0,
\]

one obtains

\[
\boxed{
 \mathfrak H_X
 =-\sum_{q=2}^Xh_{1/2}(q)
   \frac1{\sqrt q}\log\frac Xq.}
\tag{L-23812.11}
\]

The Dirichlet series of `h_theta` is

\[
\boxed{
 \sum_{q\ge1}\frac{h_\theta(q)}{q^s}
 =\frac1{\zeta(s)}
  \sum_{m\ge1}
  \frac{m^\theta-(m-1)^\theta}{m^s}}
\tag{L-23812.12}
\]

in its absolute-convergence half-plane.  This displays the reciprocal-zeta
channel explicitly.

## 5. Review consequence

A review of `T-23803` should separate three assertions:

1. the exact producer/divergence identities — finite algebra;
2. producer positivity `A_X>=0` — a finite sign theorem;
3. the scalar half-moment bound `mathfrak H_X=X^{o(1)}` — the analytic rate.

Long finite positivity ranges do not establish item 3.  Conversely, a proof of
the half-moment rate does not by itself establish producer positivity.

## 6. Proof boundary

Proved here:

- the exact all-`theta` moment identity;
- the uniform square-root defect constants;
- equivalence of `BTF` weighted variation and one scalar half-moment under
  producer positivity;
- the exact Möbius/Dirichlet representation of that half-moment.

Not proved here:

- `A_X(n)>=0` cofinally;
- `mathfrak H_X=X^{o(1)}`;
- `BTF`;
- RH.
