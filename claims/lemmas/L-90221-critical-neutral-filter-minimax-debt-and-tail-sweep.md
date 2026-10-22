# L-90221 — The critical-neutral dyadic filter has an unavoidable minimax Pascal debt and one exact low-row tail sweep

Claim ID: `L-90221`  
Status: **PROPOSED COMPLETE EXACT FILTER / MARKOV LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Depends on: dyadic filter cone `L-90216`; canonical reward `L-90210/L-90214`; uniform-Pascal Green pairing `L-33107/L-33109`  
Scope: all finite dyadic filters with both the neutral and square-root critical roots; one canonical signed adapter; no sign theorem for its arithmetic pairing and no RH conclusion

## 1. Critical-neutral dyadic filters

Let

\[
 Q(t)=\sum_{j=0}^{J}q_jt^j,
 \qquad q_0=1,
 \tag{L-90221.1}
\]

and impose

\[
 \boxed{
 Q(1)=0,
 \qquad
 Q(2^{-1/2})=0.
 }
 \tag{L-90221.2}
\]

Put

\[
 S_j=\sum_{\ell=0}^{j}q_\ell,
 \qquad
 A_j=2\sum_{\ell=0}^{j-1}2^\ell S_\ell,
 \qquad A_1=2.
 \tag{L-90221.3}
\]

By `L-90216`, `A_j` is the right-end reward numerator on the `j`th
dyadic block.

Let

\[
 r=2^{-1/2},
 \qquad
 \lambda=\frac r2=\frac1{2\sqrt2}.
 \tag{L-90221.4}
\]

Since `Q(1)=0`,

\[
 Q(t)=(1-t)\sum_{j=0}^{J-1}S_jt^j.
 \tag{L-90221.5}
\]

The second root in (L-90221.2) is therefore equivalent to

\[
 \sum_{j=0}^{J-1}S_jr^j=0.
 \tag{L-90221.6}
\]

## 2. Exact weighted debt identity

The coordinates satisfy

\[
 A_{j+1}-A_j=2^{j+1}S_j.
 \tag{L-90221.7}
\]

Substitute

\[
 S_j=\frac{A_{j+1}-A_j}{2^{j+1}}
 \qquad(j\ge1)
\]

into (L-90221.6), use `S_0=1` and `A_1=2`, and telescope.  One obtains

\[
 \boxed{
 \sum_{k=2}^{J-1}
 (1-\lambda)\lambda^{k-1}A_k
 +\lambda^{J-1}A_J
 =-2(1-\lambda).
 }
 \tag{L-90221.8}
\]

Every weight on the left is positive, and their sum is exactly

\[
 \lambda.
 \tag{L-90221.9}
\]

Hence their weighted average is

\[
 -\frac{2(1-\lambda)}{\lambda}
 =\boxed{2-4\sqrt2}.
 \tag{L-90221.10}
\]

Consequently every critical-neutral dyadic filter obeys

\[
 \boxed{
 \min_{2\le k\le J}A_k\le2-4\sqrt2<0.
 }
 \tag{L-90221.11}
\]

This is a quantitative signed-reward obstruction at the square-root mode,
independent of degree.

### Nonnegative-tail strengthening

Because `S_J=0`, the eventual Pascal reward has numerator `A_J`.  If its
tail is required to be nonnegative,

\[
 A_J\ge0,
 \tag{L-90221.12}
\]

then some pre-tail block satisfies

\[
 \boxed{
 \min_{2\le k\le J-1}A_k
 \le
 \frac{2-4\sqrt2}{1-\lambda^{J-2}}.
 }
 \tag{L-90221.13}
\]

Thus moving the signed debt into a finite collar while restoring a positive
tail necessarily makes that collar more negative than the global minimax
level.

## 3. Unique minimax filter

Equality in (L-90221.11) forces every positively weighted coordinate in
(L-90221.8) to equal the common average,

\[
 A_k=2-4\sqrt2
 \qquad(k\ge2).
 \tag{L-90221.14}
\]

The recurrence (L-90221.7) then gives

\[
 S_1=-\sqrt2,
 \qquad
 S_k=0\quad(k\ge2).
 \tag{L-90221.15}
\]

Therefore, up to trailing zero coefficients, the unique minimax polynomial is

\[
 \boxed{
 Q_\star(t)
 =(1-t)(1-\sqrt2\,t)
 =1-(1+\sqrt2)t+\sqrt2\,t^2.
 }
 \tag{L-90221.16}
\]

It distributes the unavoidable debt uniformly over every block after the
first rather than concentrating it in a finite collar.

## 4. Exact uniform-Pascal reward of `Q_star`

The dyadic increment source associated to (L-90221.16) has

\[
 a(1)=0,\qquad
 a(2)=2+\sqrt2,\qquad
 a(4)=1-\sqrt2,
\]

and `a(n)=1` otherwise.  Its normalized node potential is

\[
 f(1)=0,\qquad
 f(2)=1+\frac{\sqrt2}{2},\qquad
 f(3)=1+\frac{\sqrt2}{3},\qquad
 f(m)=1\quad(m\ge4).
 \tag{L-90221.17}
\]

The reward `d_star=f-Pf` is

\[
 \boxed{
 \begin{aligned}
 d_\star(2)&=\frac{2+\sqrt2}{2},\\
 d_\star(3)&=\frac13,\\
 d_\star(m)&=\frac{2-4\sqrt2}{m(m-1)}
 \qquad(m\ge4).
 \end{aligned}}
 \tag{L-90221.18}
\]

Thus the globally minimax critical adapter has two positive low rows and one
pure reciprocal-square negative tail.

## 5. Sweep the entire negative tail exactly

Let `M-MP=s` be any finite uniform-Pascal Green occupation with the
size-conservation identity

\[
 \sum_{n\ge1}s_n=0.
 \tag{L-90221.19}
\]

The reward

\[
 e(m)=\frac1{m(m-1)}
 \qquad(m\ge2)
 \tag{L-90221.20}
\]

has the exact potential

\[
 g(1)=0,
 \qquad
 g(m)=\frac12\quad(m\ge2).
 \tag{L-90221.21}
\]

Indeed `g-Pg=e` row by row.  Therefore

\[
 \boxed{
 \sum_{m\ge2}\frac{M_m}{m(m-1)}
 =\sum_ns_ng(n)
 =-\frac{s_1}{2}.
 }
 \tag{L-90221.22}
\]

Let

\[
 \mathcal L_\star=\sum_{m\ge2}M_md_\star(m).
 \tag{L-90221.23}
\]

Subtract the reciprocal-square tail from the first two rows and apply
(L-90221.22).  The exact result is

\[
 \boxed{
 \mathcal L_\star
 =\frac{\sqrt2}{6}\,[15M_2+4M_3]
 +(2\sqrt2-1)s_1.
 }
 \tag{L-90221.24}
\]

The canonical boundary identity of `L-90210` is

\[
 15M_2+4M_3=-12s_1+3s_2+2s_3.
 \tag{L-90221.25}
\]

Consequently

\[
 \boxed{
 \mathcal L_\star
 =-s_1+\frac{\sqrt2}{2}s_2
       +\frac{\sqrt2}{3}s_3.
 }
 \tag{L-90221.26}
\]

If `s_n=n[U(n)-U(n+1)]`, then

\[
 \boxed{
 \mathcal L_\star\ge0
 \iff
 3s_2+2s_3\ge3\sqrt2\,s_1
 \iff
 2[U(2)-U(4)]\ge
 \sqrt2[U(1)-U(2)].
 }
 \tag{L-90221.27}
\]

Thus an infinite signed Pascal reward has collapsed to one three-source
inequality.

## 6. Arithmetic source and positive renewal

Let

\[
 b_\star
 =Q_\star(\delta_2)*\mu
 =(\varepsilon-\delta_2)
  *(\varepsilon-\sqrt2\,\delta_2)*\mu.
 \tag{L-90221.28}
\]

For real `x>=1`, define

\[
 \mathcal K_\star(x)
 =-\sum_{2\le q\le x}b_\star(q)
  (q^{-1/2}-x^{-1/2}).
 \tag{L-90221.29}
\]

Since

\[
 1*b_\star
 =\varepsilon-(1+\sqrt2)\delta_2+\sqrt2\,\delta_4,
 \tag{L-90221.30}
\]

the critical divisor operator of `L-90215` gives

\[
 \boxed{
 \mathcal P\mathcal K_\star(x)=\Psi_\star(x),
 }
 \tag{L-90221.31}
\]

where

\[
 \boxed{
 \Psi_\star(x)=
 \begin{cases}
 0,&1\le x<2,\\[1mm]
 J(x)+\dfrac1{\sqrt2}-\sqrt{\dfrac2x},
     &2\le x<4,\\[3mm]
 J(x),&x\ge4.
 \end{cases}}
 \tag{L-90221.32}
\]

Here

\[
 J(x)=\sum_{n\le x}n^{-1/2}
      -\frac{\lfloor x\rfloor}{\sqrt x}.
\]

The forcing is nonnegative on the full domain:

- it is zero on `[1,2]`;
- on `[2,3)` it is
  \[
  1+\sqrt2-\frac{2+\sqrt2}{\sqrt x}\ge0;
  \]
- on `[3,4)` it is
  \[
  1+\sqrt2+\frac1{\sqrt3}
  -\frac{3+\sqrt2}{\sqrt x}>0;
  \]
- for `x>=4`, `J(x)>0` term by term.

Therefore

\[
 \boxed{\Psi_\star(x)\ge0\qquad(x\ge1).}
 \tag{L-90221.33}
\]

Exact Möbius inversion gives

\[
 \boxed{
 \mathcal K_\star(x)
 =\sum_{d\le x}\frac{\mu(d)}{\sqrt d}
  \Psi_\star(x/d).
 }
 \tag{L-90221.34}
\]

As with `L-90215`, the forcing is positive but the final Möbius boundary sign
is not inferred.

## 7. Relation to the Haar route

The two factors in `Q_star` have separate meanings:

```text
1-t                 neutral dyadic difference;
1-sqrt(2)t          critical half-power Haar difference.
```

Thus `b_star` is the neutralized critical Haar source.  Its deterministic
reward is the least-negative uniform-Pascal realization possible among all
finite critical-neutral dyadic filters, and its entire infinite tail is
summed by (L-90221.24).

This is the smallest exact interface currently connecting:

- the critical Haar scalar of PR #333;
- the canonical `15:4` Pascal reward;
- the finite dyadic filter cone;
- the positive divisor-renewal normal form.

## 8. Proof boundary

Proved exactly:

- the weighted debt identity for every finite critical-neutral dyadic filter;
- the universal minimax debt `2-4sqrt(2)`;
- uniqueness of `Q_star`;
- its complete Pascal reward;
- exact sweeping of the infinite reciprocal-square tail;
- reduction to one three-source inequality;
- the complete nonnegative renewal forcing.

Not proved:

- the three-source inequality (L-90221.27);
- sign of `K_star` after Möbius inversion;
- the factor-64 payment, SHARP, or RH.
