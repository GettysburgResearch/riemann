# T-21501 — Prime-power polygon criterion for the Riemann hypothesis

Claim ID: `T-21501`  
Title: RH is equivalent to eventual domination of one explicit convex curve by the finite prime-power moment polygon  
Status: `PROPOSED — COMPLETE CONSEQUENCE OF L-21501 AND L-19801/L-19802`  
Authoring agent: `gpt56-02-p`  
Created: 2026-08-07  
Dependencies: `L-21501`; `L-19801`; `L-19802`; the prime number theorem for the exponent corollary  
Scope: full scalar RH criterion and complete finite negative semidecision

## 1. Arithmetic vertices

Retain the prime-power notation of `L-21501`:

\[
A_j=\sum_{q_i\le q_j}{\Lambda(q_i)\over\sqrt{q_i}},
\qquad
B_j=\sum_{q_i\le q_j}{\Lambda(q_i)\log q_i\over\sqrt{q_i}}.
\tag{T-21501.1}
\]

Let `F^*` be the explicit archimedean conjugate in `L-21501.9` and define the vertex deficit

\[
\boxed{
D_j=F^*(A_j)-B_j.
}
\tag{T-21501.2}
\]

Every `D_j` is a finite arithmetic quantity plus one one-dimensional explicit archimedean optimization.

## 2. Main equivalence

The following are equivalent:

1. the Riemann hypothesis;
2. `D_j<=0` for every `j>=1`;
3. `D_j<=0` for every sufficiently large `j`;
4. the prime-power polygon `G^*` lies above `F^*` on `[0,infinity)`;
5. the prime-power polygon lies above `F^*` on every sufficiently late edge.

Equivalently,

\[
\boxed{
\mathrm{RH}
\iff
B_j\ge F^*(A_j)
\quad\text{for every sufficiently large prime-power prefix }j.
}
\tag{T-21501.3}
\]

### Proof

If RH holds, the zero expansion gives `Psi(t)>=0` for every real `t`. The exact minimax identity `L-21501.14` then gives `D_j<=0` for every `j`.

Conversely, suppose `D_j<=0` for every `j>=J`. If

\[
\log q_j\le t\le\log q_{j+1}
\]

with `j>=J`, then

\[
G(t)=A_jt-B_j.
\]

By the definition of `F^*`,

\[
F(t)-A_jt\ge-F^*(A_j).
\]

Therefore

\[
\Psi(t)=F(t)-G(t)
\ge B_j-F^*(A_j)
=-D_j
\ge0.
\tag{T-21501.4}
\]

Thus `Psi` is eventually nonnegative on the complete half-line. The one-sign Landau transfer of `L-19801` excludes every zero with real part greater than `1/2`; functional-equation symmetry gives RH. This proves the equivalence of 1–3. Statements 4–5 are the polygonal form of the same argument, using `L-21501.10` and convexity on each edge. QED.

## 3. Complete finite disproof interface

For any prefix `j` and any trial `t>=log 2`, define

\[
\boxed{
W_j(t)=A_jt-F(t)-B_j.
}
\tag{T-21501.5}
\]

If a directed calculation proves

\[
\boxed{W_j(t)>0,}
\tag{T-21501.6}
\]

then

\[
F^*(A_j)-B_j\ge W_j(t)>0.
\]

By `L-21501.16`, `Psi` is strictly negative at a finite real point, and therefore

\[
\boxed{
W_j(t)>0
\quad\Longrightarrow\quad
\mathrm{RH\ is\ false}.
}
\tag{T-21501.7}
\]

No zeta-zero ordinate, zero count, or matrix complement appears in this certificate. It uses only:

```text
a complete prime-power prefix;
directed log/square-root arithmetic for A_j and B_j;
one rational or directed trial t;
the explicit archimedean constants and geometric series tail;
a strict final rational inequality.
```

Conversely, if RH is false, (T-21501.3) implies that some finite prefix has `D_j>0`. Since the maximizer defining `F^*(A_j)` is finite and the inequality is strict, a rational trial point sufficiently close to it gives `W_j(t)>0`. Therefore exhaustive directed enumeration of these tangent witnesses is a complete semidecision for `not RH`.

## 4. Exact rightmost-zero exponent

Let

\[
\Theta_\zeta
=\sup_{\xi(\rho)=0}
 \left(\Re\rho-{1\over2}\right)
\tag{T-21501.8}
\]

and put

\[
d_j=(D_j)_+.
\tag{T-21501.9}
\]

Then

\[
\boxed{
\Theta_\zeta
 =\limsup_{j\to\infty}
 {\log(1+d_j)\over\log q_j}.
}
\tag{T-21501.10}
\]

### Proof

Let `t_j` maximize `A_jt-F(t)`. By `L-21501.16`,

\[
d_j\le(-\Psi(t_j))_+.
\tag{T-21501.11}
\]

The zero expansion used in `L-19802` gives

\[
|\Psi(t)|\ll1+e^{\Theta_\zeta t}.
\tag{T-21501.12}
\]

The prime number theorem and partial summation give

\[
A_j=2\sqrt{q_j}+o(\sqrt{q_j}).
\tag{T-21501.13}
\]

Together with the exact slope formula `L-21501.21`, this yields

\[
t_j=\log q_j+o(1).
\tag{T-21501.14}
\]

Equations (T-21501.11)–(T-21501.14) give the upper bound in (T-21501.10).

For the reverse bound, take a square sample `t=2log N` from the subsequence realizing `L-19802.5`, and let `j` be the active prefix:

\[
\log q_j\le t<\log q_{j+1}.
\]

Then

\[
-\Psi(t)
=A_jt-B_j-F(t)
\le F^*(A_j)-B_j
=D_j.
\tag{T-21501.15}
\]

Bertrand's postulate gives `q_(j+1)<2q_j`, hence

\[
\log q_j=t+O(1).
\tag{T-21501.16}
\]

The lower exponent from `L-19802` therefore transfers to `d_j`, proving the reverse inequality in (T-21501.10). QED.

Consequently, if RH is false, then for every `theta<Theta_zeta`,

\[
\boxed{
{d_j\over q_j^\theta}
\text{ is unbounded on every prime-power tail}.
}
\tag{T-21501.17}
\]

The polygon deficit does not merely test RH; its growth recovers the horizontal position of the rightmost zero exactly.

## 5. Exact remaining theorem

The positive route is now one statement:

\[
\boxed{
B_j-F^*(A_j)\ge0
\quad\text{for every sufficiently large prime-power prefix }j.
}
\tag{T-21501.18}
\]

Equivalently, the integrated prime-power quantile polygon must dominate the explicit archimedean quantile curve. This is the same RH-strength arithmetic content seen by the square-screw and D-0001 principal coordinate, but with every continuum, phase, packet, and complement removed.

## 6. Proof boundary

- The theorem proves the equivalence and finite negative semidecision, not (T-21501.18).
- Formula (T-21501.10) imports the standard PNT only to identify the natural prime-power abscissa with the screw abscissa.
- A finite list of nonnegative deficits does not prove RH.
- Any claimed negative witness must use directed transcendental arithmetic and a complete prefix manifest.
- No RH resolution is claimed at this stage.
