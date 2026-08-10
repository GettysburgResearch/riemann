# L-90203 — The Liouville source generates the maximal positive Dirichlet-convolution cone for prime-power extraction

Claim ID: `L-90203`  
Status: **PROPOSED COMPLETE EXACT LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Depends on: finite Dirichlet-convolution algebra only; conceptually extends `L-90201/L-90202`  
Scope: exact arithmetic cone and maximality; no asymptotic estimate and no RH conclusion

## 1. The normalized positive convolution cone

Write `*` for Dirichlet convolution, `1(n)=1`, and `epsilon` for the convolution identity. Since

\[
 \mu*1=\epsilon,
\]

every arithmetic source `b` with `b(1)=1` has a unique representation

\[
 \boxed{
 b=\mu*h,
 \qquad h=1*b.
 }
 \tag{L-90203.1}
\]

Define the normalized Liouville/Möbius positive-convolution cone

\[
 \boxed{
 \mathcal C_\mu
 =\{\mu*h:\ h(1)=1,\ h(n)\ge0\text{ for every }n\ge2\}.
 }
 \tag{L-90203.2}
\]

No multiplicativity is required of `h`.

The point `h=epsilon` is the Möbius source itself. The point `h=1` is the unit source `epsilon`, because `mu*1=epsilon`.

## 2. Prime-power extraction by valuation potentials

For every prime `p`, let

\[
 \phi_p:\mathbb Z_{\ge0}\to\mathbb R,
 \qquad \phi_p(0)=0,
\]

and assume its increments

\[
 \ell(p^a):=\phi_p(a)-\phi_p(a-1)\ge0
 \qquad(a\ge1).
 \tag{L-90203.3}
\]

Put

\[
 g(n)=\sum_p\phi_p(v_p(n)).
 \tag{L-90203.4}
\]

Then finite inclusion-exclusion gives

\[
 \boxed{
 (\mu*g)(n)
 =\begin{cases}
 \ell(p^a),&n=p^a,\\
 0,&\omega(n)\ne1.
 \end{cases}}
 \tag{L-90203.5}
\]

Thus an arbitrary prescribed nonnegative prime-power measure `ell(p^a)` is obtained by taking

\[
 \phi_p(a)=\sum_{j=1}^a\ell(p^j).
 \tag{L-90203.6}
\]

Special cases include:

- `phi_p(a)=a log p`, which gives ordinary von Mangoldt `Lambda` on every prime power;
- `phi_p(a)=log p` for `a>=1`, which gives `log p` on ordinary primes and zero on higher powers;
- arbitrary nonnegative valuation costs, including finite prime or prime-power localization.

## 3. Universal pointwise domination

Let `b=mu*h in C_mu`. By associativity,

\[
 \boxed{
 b*g=h*(\mu*g)=h*\ell.
 }
 \tag{L-90203.7}
\]

Because `h>=0`, `ell>=0`, and `h(1)=1`, one has pointwise

\[
 \boxed{
 (b*g)(n)\ge(\mu*g)(n)=\ell(n)
 \qquad(n\ge1),
 }
 \tag{L-90203.8}
\]

where `ell` is understood to vanish away from prime powers.

Consequently, for every nonnegative arithmetic test weight `W`,

\[
 \boxed{
 \sum_nW(n)(b*g)(n)
 \ge
 \sum_{p^a}W(p^a)\ell(p^a).
 }
 \tag{L-90203.9}
\]

The domination is simultaneous in the complete nonnegative prime-power measure `ell`; no separate class argument is needed for ordinary primes, prime powers, valuations, or nonnegative mixtures of them.

## 4. The real multiplicative cube is a small face of the cone

Retain the real prime parameters of `L-90201`, `x_p in [-1,1]`, and the squarefree source

\[
 b_x(d)=\mu^2(d)\prod_{p\mid d}x_p.
 \tag{L-90203.10}
\]

Define the multiplicative nonnegative function `h_x` by the local rule

\[
 \boxed{
 h_x(1)=1,
 \qquad
 h_x(p^a)=1+x_p\quad(a\ge1).
 }
 \tag{L-90203.11}
\]

Equivalently,

\[
 h_x(n)=\prod_{p\mid n}(1+x_p)\ge0.
\]

At each prime the local generating functions obey

\[
 1+x_pz=(1-z)\bigl[1+(1+x_p)z+(1+x_p)z^2+\cdots\bigr].
 \tag{L-90203.12}
\]

Hence

\[
 \boxed{
 b_x=\mu*h_x\in\mathcal C_\mu.
 }
 \tag{L-90203.13}
\]

Therefore `L-90201/L-90202` are restrictions of the cone theorem to one multiplicative face. The positive-convolution cone is vastly larger: its deformation `h` may be arbitrary and nonmultiplicative.

## 5. Maximality theorem

The cone `C_mu` is not merely sufficient for simultaneous nonnegative prime extraction. It is maximal.

Let `b(1)=1` be arbitrary and put `h=1*b`, so `b=mu*h`. For a prime `p`, let

\[
 g_p(n)=v_p(n).
\]

Then

\[
 (\mu*g_p)(n)=\mathbf1_{n=p^a,\ a\ge1}.
 \tag{L-90203.14}
\]

If `p` does not divide `m` and `m>1`, associativity gives

\[
 \boxed{
 (b*g_p)(mp)
 =(h*(\mu*g_p))(mp)
 =h(m).
 }
 \tag{L-90203.15}
\]

Therefore the following are equivalent:

\[
 \boxed{
 \begin{aligned}
 &(i)\quad b\in\mathcal C_\mu;\\
 &(ii)\quad (b*g_p)(n)\ge(\mu*g_p)(n)
       \text{ for every prime }p\text{ and every }n;\\
 &(iii)\quad (b*g_p)(n)\ge0
       \text{ for every prime }p\text{ and every }n.
 \end{aligned}}
 \tag{L-90203.16}
\]

Indeed `(i)=>(ii)=>(iii)` follows from Section 3. For `(iii)=>(i)`, given any `m>1`, choose a prime `p` not dividing `m`; then (L-90203.15) gives `h(m)>=0`. Also `h(1)=b(1)=1`.

Thus `C_mu` is exactly the largest normalized source cone on which all elementary prime-valuation extractions remain nonnegative.

## 6. Ordered-algebra extension

The factorization (L-90203.7) uses only convolution and positivity. It therefore extends to coefficients in any ordered commutative algebra in which products of positive elements are positive. In particular, for commuting positive-semidefinite matrix coefficients `H(n)` with `H(1)=I`, the convolution `mu*H` dominates the prime-power extraction in Loewner order after every nonnegative scalar valuation test.

No noncommutative ordering statement is made.

## 7. Consequences for the multiplicative-bootstrap map

1. The real cube of `T-90202` is not the natural terminal class. The natural object is the maximal cone `C_mu`.
2. Class uniformity of every nonnegative prime-power observable is free on this cone: the worst source is the Möbius/Liouville boundary point `h=epsilon`.
3. Ordinary-prime and complete-prime-power coordinates are covered by the same theorem.
4. Any future source deformation that remains inside `C_mu` cannot create a new negative arithmetic direction; all new mass is positive convolution of genuine prime-power extraction.
5. To obtain information unavailable at the Möbius point, an argument must either use the Möbius slice itself or leave this maximal positive cone.

## 8. Proof boundary

Proved exactly:

- arbitrary nonnegative prime-power extraction by valuation potentials;
- the factorization `b*g=h*(mu*g)` and pointwise domination;
- embedding of the complete real multiplicative cube in `C_mu`;
- maximality of `C_mu` from the elementary valuation probes `v_p`;
- the commuting ordered-algebra extension.

Not proved:

- a sharp asymptotic lower bound at the Möbius boundary point;
- GFEP, sparse producer positivity, Form A at `mu`, or RH.
