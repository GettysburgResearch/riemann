# L-26202 — Dyadic signed slack is the exact carry residual seen by the fixed-ratio Möbius shell

Claim ID: `L-26202`  
Title: The dyadic Riesz coordinate equals one parity-weighted carry slack plus an automatic logarithmic term, while high-index divisor-gradient transport is invisible to it  
Status: **PROPOSED EXACT LEMMA — COMPLETE FINITE ALGEBRA AND MELLIN TRANSFER**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Dependencies: `L-26201`; PR #244 `L-23701`, `L-23705`, `L-23706`; PR #254 `L-25301`; elementary Mellin integration  
Scope: scalar bridge from the corrected dyadic source to one signed residual; no bound for that residual is claimed

## 1. Carry coefficient system

Fix an integer `X>=2`. Let

\[
B_X(n,q)=\beta_{nq},
\qquad
2\le q\le n\le X,
\tag{L-26202.1}
\]

and define the logarithmic target

\[
\boxed{
w_X(q)
=
{1\over\sqrt q}\log{X\over q},
\qquad 2\le q\le X.
}
\tag{L-26202.2}
\]

Let `d_X(n)>=0` be any carry coefficient vector satisfying

\[
B_X^{T}d_X\le w_X.
\tag{L-26202.3}
\]

Its final residual is

\[
\boxed{
s_X(q)
=
w_X(q)-\sum_{n=q}^X d_X(n)\beta_{nq}
\ge0.
}
\tag{L-26202.4}
\]

The exact backward greedy vector of PR #244 is one canonical unconditional
choice, but the identities in Sections 2--4 hold for every vector `d_X`.

## 2. Rank-one pairing

Define the dyadic signed slack

\[
\boxed{
\Pi_2(X;d_X)
=
\sum_{q=2}^X b_2(q)s_X(q).
}
\tag{L-26202.5}
\]

Also define the dyadic Riesz coordinate

\[
\boxed{
\mathcal R_2(X)
=
\sum_{q=2}^X
{b_2(q)\over\sqrt q}\log{X\over q}.
}
\tag{L-26202.6}
\]

By `L-26201.10`,

\[
(B_Xb_2)(n)=-{2\over n+1}.
\]

Pairing (L-26202.4) with `b_2` therefore gives

\[
\boxed{
\Pi_2(X;d_X)
=
\mathcal R_2(X)
+
2\sum_{n=2}^X {d_X(n)\over n+1}.
}
\tag{L-26202.7}
\]

This identity is exact. It uses no positivity except when one later wants a
uniform bound for the second term.

PR #244 proves for every nonnegative feasible vector that

\[
\sum_{n=2}^X d_X(n)\sqrt n
=O(\log^2X).
\]

Consequently

\[
\boxed{
\sum_{n=2}^X {d_X(n)\over n+1}
=O(\log^2X).
}
\tag{L-26202.8}
\]

Thus a subpower estimate for the single signed slack `Pi_2` gives the same
estimate for the RH-bearing Riesz coordinate `R_2`.

## 3. Exact greedy blocker form

For the backward greedy vector, let

\[
\widehat d_X(n)
=
{\rho_X^{(n)}(n)\over\beta_{nn}},
\qquad
d_X(n)
=
\min_{\beta_{nq}>0}
{\rho_X^{(n)}(q)\over\beta_{nq}},
\]

and put

\[
\ell_X(n)=\widehat d_X(n)-d_X(n)\ge0.
\tag{L-26202.9}
\]

`L-23706` gives the exact final slack

\[
s_X(n)=\beta_{nn}\ell_X(n)
={n-1\over n+1}\ell_X(n).
\]

Therefore

\[
\boxed{
\Pi_2^{\rm gr}(X)
=
\sum_{n=2}^X
b_2(n){n-1\over n+1}\ell_X(n).
}
\tag{L-26202.10}
\]

The full Greedy Slack theorem asks for an unsigned bound on

\[
\sum_{n=2}^X {n-1\over n+1}\ell_X(n).
\]

Equation (L-26202.10) asks only for its exact dyadic Möbius projection.

Since

\[
|b_2(n)|\le2,
\]

total greedy slack implies dyadic signed slack, but the converse is not
required. The new target is therefore strictly weaker than the existing
unsigned carry theorem.

## 4. Dyadic-chain second difference

For odd `m`,

\[
b_2(m)=\mu(m),\qquad
b_2(2m)=-2\mu(m),\qquad
b_2(4m)=\mu(m),
\]

and `b_2(2^a m)=0` for `a>=3`. With the convention `s_X(r)=0` outside
`2<=r<=X`,

\[
\boxed{
\Pi_2(X;d_X)
=
\sum_{\substack{m\le X\\m\ {m odd}}}
\mu(m)
\left[
s_X(m)-2s_X(2m)+s_X(4m)
\right].
}
\tag{L-26202.11}
\]

Thus the remaining scalar is a Möbius-weighted dyadic second difference of
the final carry slack. Large unsigned slack is permitted if it is affine, or
nearly affine, along the dyadic chains.

This is the exact point at which the parity-comb and blocker-forest structures
can interact without discarding signs.

## 5. Mellin criterion

The Dirichlet series of `b_2` is

\[
B_2(s)
=
\sum_{n\ge1}{b_2(n)\over n^s}
=
{1-2^{-s}\over\zeta(s)}.
\tag{L-26202.12}
\]

For `Re z>1/2`, termwise integration gives

\[
\boxed{
\int_1^\infty
\mathcal R_2(X)X^{-z-1}\,dX
=
{B_2(z+1/2)-1\over z^2}.
}
\tag{L-26202.13}
\]

Indeed,

\[
\int_n^\infty
\log{X\over n}\,X^{-z-1}\,dX
={n^{-z}\over z^2}.
\]

Suppose that, for every `epsilon>0`,

\[
\mathcal R_2(X)=O_\varepsilon(X^\varepsilon).
\tag{L-26202.14}
\]

Then (L-26202.13) converges normally and is holomorphic throughout

\[
\Re z>0.
\]

If `rho` were a zeta zero with `Re rho>1/2`, then `z=rho-1/2` would lie in
that half-plane and the right side of (L-26202.13) would have a genuine pole.
The numerator `1-2^(-rho)` cannot vanish there: a zero of that factor has real
part zero. Hence no such `rho` exists, and functional-equation symmetry gives
RH.

Conversely, the classical Mertens criterion implies (L-26202.14). Therefore

\[
\boxed{
\mathrm{RH}
\iff
\mathcal R_2(X)=O_\varepsilon(X^\varepsilon)
\quad\text{for every }\varepsilon>0.
}
\tag{L-26202.15}
\]

Combining (L-26202.7)--(L-26202.8) gives the sufficient theorem

\[
\boxed{
\Pi_2^{\rm gr}(X)=O_\varepsilon(X^\varepsilon)
\quad\Longrightarrow\quad
\mathrm{RH}.
}
\tag{L-26202.16}
\]

## 6. Divisor-gradient transport is invisible above the bottom boundary

The adjacent signed transport of PR #254 uses the divisor-gradient coordinate

\[
v_q(b)
=
\sum_{m=2}^X
b(m)
\left(
\mathbf 1_{q\mid m}
-
\mathbf 1_{q\mid m-1}
\right).
\tag{L-26202.17}
\]

Pair it with `b_2(q)`. From `L-26201.17`,

\[
\begin{aligned}
\sum_{q=2}^X b_2(q)v_q(b)
&=
\sum_{m=2}^X
b(m)\,[D_2(m)-D_2(m-1)]\\
&=
\boxed{-2b(2)+b(3).}
\end{aligned}
\tag{L-26202.18}
\]

For the adjacent correction

\[
b_F(m)=b(m)+F_{m-1}-F_m,
\qquad F_1=F_X=0,
\]

the dyadic projection changes by

\[
\boxed{
\sum_q b_2(q)
\bigl[v_q(b_F)-v_q(b)\bigr]
=
3F_2-F_3.
}
\tag{L-26202.19}
\]

Every transport move supported at `j>=4` is exactly invisible to the dyadic
source.

This is a structural no-go for the most direct proposed bridge to signed carry
transport. High-scale defect-to-slack routing can repair many individual
constraints, but it cannot change the fixed-`q_0=2` Möbius scalar until its
charge reaches the two bottom coordinates. A proof must therefore emit an
explicit bottom-charge telescope rather than appeal only to half-scale
transport.

## 7. Correct pivot

The surviving proof-facing target is not the unsigned total slack and not a
generic adjacent-flow cost. It is one of the equivalent two-coordinate
statements:

\[
\Pi_2^{\rm gr}(X)=X^{o(1)},
\]

or the two-charge Green form of `L-26203`.

A plausible production proof may still use:

- the blocker forest and digital-freeze law;
- dyadic chain grouping in (L-26202.11);
- the exact two-contact carry reserve of `L-26201`;
- a bottom-boundary charge recursion.

But every proposed descent must explicitly account for the charges at `2` and
`3`. Large-index signed transport alone cannot close the theorem.

## 8. Proof boundary

Closed exactly:

- rank-one pairing of carry residual with the dyadic source;
- automatic logarithmic size of the auxiliary harmonic term;
- the parity-weighted greedy blocker formula;
- the dyadic-chain second-difference formula;
- the Mellin implication to RH;
- the high-index transport invisibility theorem.

Open:

- a subpower estimate for `Pi_2^gr`;
- a valid bottom-charge recurrence;
- RH.
