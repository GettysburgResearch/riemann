# L-96501 — The complete paired first-owner stopping tree terminates at finite depth for every endpoint

Claim ID: `L-96501`  
Status: **PROPOSED COMPLETE SOURCE-EXHAUSTION THEOREM — HOSTILE REVIEW REQUIRED**  
Created: 2026-08-17  
Depends on: `L-96500`; exact paired stopping theorem `L-91362`; causal identity `L-91650`; frozen reconstruction `L-96302`

## 1. Labelled state

The root is the exact positive parity-labelled native source

\[
\mathscr N_X=
\bigoplus_{\substack{k\le X/2\\\mu(k)\ne0}}
{1\over\sqrt k}\,\mathscr Q_{X/k}^{\operatorname{parity}(\mu(k))}.
\tag{L-96501.1}
\]

Signed component-row observation is postponed. When it is finally applied, the
row marginal is exactly the native Möbius row `c_X`.

Every squarefree colour has the unique factorization

\[
k=d p_1\cdots p_t,
\qquad d\mid P_{61},
\qquad67\le p_1<\cdots<p_t.
\tag{L-96501.2}
\]

The label records `d`, the ordered rough history, parity, causal path and least
unused rough owner.

## 2. Exact paired stopping step

The exact least-prime stopping identity of `L-91362`, with the coefficients
reconstructed in `L-96500`, partitions one unresolved paired source as

\[
\mathscr P_v=\mathscr G(v)\oplus\mathscr F(v).
\tag{L-96501.3}
\]

Here `G(v)` is the finite family of stopped current leaves produced by the full
paired identity, and `F(v)` is the unresolved paired frontier. Intermediate
oriented children remain inside `F(v)` and are never observed as positive rows.
Every source occurrence appears in exactly one side because the least-prime
owner is unique and the parent coefficients sum to one.

For every frontier component `v'` of `F(v)`,

\[
Z_{v'}\le Z_v/67,
\qquad
M(\mathscr F(v))<M(\mathscr P_v)/8.
\tag{L-96501.4}
\]

The scale estimate is the termination mechanism; the mass estimate is only an
independent audit and does not invoke rough-number density.

## 3. Finite iteration

Substitute (L-96501.3) only in the unresolved frontier. After `n` levels,

\[
\mathscr N_X=\mathscr G_n\oplus\mathscr F_n,
\qquad
\operatorname{scale}(\mathscr F_n)\le X/67^n.
\tag{L-96501.5}
\]

Choose

\[
D_X=\min\{n:X/67^n<67\}.
\tag{L-96501.6}
\]

Then the construction stops after exactly finitely many substitutions. Every
leaf in `G_{D_X}` is a canonical current leaf

\[
(p,y,d),\qquad p\ge67,\quad1\le y<67,\quad d\mid P_{61},
\]

and every remaining source in `F_{D_X}` has outer scale below 67. There is no
infinite projective limit, no residual frontier, and no interchange of a limit
with physical observation.

Thus the exact finite stopping line is

\[
\boxed{
\mathscr N_X
 =\bigoplus_{\ell\in\mathcal L_X}
   \gamma_\ell\mathscr D(p_\ell,y_\ell,d_\ell)
 \oplus
 \bigoplus_{u\in\mathcal O_X}\eta_u\mathscr N_{x_u},}
\tag{L-96501.7}
\]

where all coefficients are nonnegative, `1<=x_u<67`, and every root occurrence
has exactly one leaf owner. The same path coefficient occurs in target, score,
every component row, ordinary `q`, ordinary `4q`, and detail.

## 4. Proof

Induct on the integer rank

\[
\operatorname{rk}(v)=\min\{m:Z_v/67^m<67\}.
\]

Rank zero is an outer terminal source. At positive rank, the exact paired
stopping theorem gives (L-96501.3), unique first ownership, and lower rank for
every unresolved frontier component by (L-96501.4). Apply the induction
hypothesis separately to those disjoint components and take their finite direct
sum. This proves (L-96501.7) and source exhaustion.
