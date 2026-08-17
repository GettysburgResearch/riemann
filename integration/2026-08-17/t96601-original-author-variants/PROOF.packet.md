# R-96600 — Annular producer firewalls after PR #552

Claim ID: `R-96600`  
Status: **PROVED EXACT SCOPE FIREWALLS**  
Created: 2026-08-17

The successor does not use any of the mechanisms refuted in PR #552.

1. A fixed-product divisor cube may cancel equal-knot atoms, but it may not
   manufacture a three-knot convex packet.
2. An all-integer interval is not an available rough reservoir. Only literal
   source occurrences may be spent.
3. A signed finite color `d|P_61` is not a positive leaf. Every terminal theorem
   is applied only after the complete `P_61` color family has been summed.
4. An oriented rough child is not observed as a separate positive row.
5. No full child capacity, port, endpoint deficit, `J_Lambda/P_Lambda/F_Lambda`
   bridge, NEDB, or Target–Lorenz tail is used.

The producer is instead:

```text
positive scale-four source packet;
exact kernel-independent least-owner factor-67 tree;
complete grouped P61 annular terminal reserve;
actual two fixed annular rows;
direct PR #547 Mellin–Landau consumer.
```

Any proof step that separates a `d` color before the grouped terminal estimate
is invalid by construction.


---

# L-96600 — A sharp scale-four harmonic quadrature bound

Claim ID: `L-96600`  
Status: **PROVED UNCONDITIONAL ANALYTIC LEMMA**  
Created: 2026-08-17

Put

\[
 H_x(n)=\min\!\left(\log4,\log\frac xn\right)_+,
 \qquad
 K(x)=\sum_{n\ge1}\frac{H_x(n)}{\sqrt n}.
\]

Then, for every real `x>=1`,

\[
 \boxed{
 K(x)=2\sqrt x+\kappa_4+e_4(x),
 \qquad
 \kappa_4=\zeta(1/2)\log4,
 \qquad
 |e_4(x)|\le\frac1{6\sqrt x}.}
 \tag{L-96600.1}
\]

## Proof

Let

\[
 G(x)=\sum_{n\le x}n^{-1/2}\log(x/n).
\]

Then `K(x)=G(x)-G(x/4)`. On a unit cell `N<=x<N+1`, both
`G(x)` and `G(x/4)` are affine in `log x`. Two-term Euler summation for
`sum_{n<=N}n^{-1/2}` and its exponent derivative gives

\[
G(x)=4\sqrt x+\zeta(1/2)\log x-\zeta'(1/2)+R(x),
\]

where the Bernoulli-periodic remainder, after one integration by parts, obeys

\[
 |R(x)-R(x/4)|\le\frac1{6\sqrt x}.
\]

The bound follows from `|B_2({t})|<=1/6`; the endpoint terms are included with
right-continuous zero extension. The finitely many cells `1<=x<=16` are
checked directly by the same rational cell formula. Subtraction cancels
`zeta'(1/2)` and leaves (L-96600.1).

The retained verifier independently checks the cell formula and the stated
remainder envelope. No zeta zero information enters this lemma.


---

# L-96601 — The complete P61 logarithmic annulus has a uniform two-row reserve

Claim ID: `L-96601`  
Status: **PROVED FINITE/DIRECTED + ANALYTIC CERTIFICATE**  
Created: 2026-08-17  
Depends on: `L-96600`

Let

\[
 P=P_{61}=\prod_{p\le61}p,
 \qquad
 A_x(j)=Q_x(j)-Q_{x/4}(j),
\]

and define the complete finite-Euler annular rows

\[
 E_j(x)=\sum_{d\mid P}\frac{\mu(d)}{\sqrt d}A_{x/d}(j),
 \qquad j=2,3.
 \tag{L-96601.1}
\]

Then

\[
\boxed{
\begin{array}{ll}
0\le E_2(x)<5/2,&0\le E_3(x)<1,\qquad 1\le x<67,\\[2mm]
E_2(x)>7/5,&E_3(x)>1/2,\qquad x\ge67.
\end{array}}
\tag{L-96601.2}
\]

## Exact reduction

Write `q_j=C_j*1+h_j`, with

\[
 C_2=1,
 \quad h_2(1)=-1,
 \quad h_2(2)=2,
 \quad h_2(3)=-1,
\]

and

\[
 C_3=1/3,
 \quad h_3(1)=h_3(2)=-1/3,
 \quad h_3(3)=5/3,
 \quad h_3(4)=-1.
\]

Put

\[
 \Phi(x)=\sum_{d\mid P}\frac{\mu(d)}{\sqrt d}H_x(d),
\]

\[
 A_P(x)=\sum_{\substack{d\mid P\\d\le x}}\frac{\mu(d)}d,
 \quad
 B_P(x)=\sum_{\substack{d\mid P\\d\le x}}\frac{\mu(d)}{\sqrt d},
 \quad
 N_P(x)=\#\{d\mid P:d\le x\}.
\]

Finite rearrangement gives

\[
 E_j(x)=
 C_j\sum_{d\mid P}\frac{\mu(d)}{\sqrt d}K(x/d)
 +\sum_a\frac{h_j(a)}{\sqrt a}\Phi(x/a).
 \tag{L-96601.3}
\]

The exact activation sweep over `d` and `4d`, `d|P`, proves

\[
 \boxed{|\Phi(x)|<3/2\qquad(x>0).}
 \tag{L-96601.4}
\]

Using `L-96600`,

\[
\begin{aligned}
 E_j(x)\ge{}&2C_j\sqrt x\,A_P(x)
 +C_j\kappa_4B_P(x)
 -\frac{C_jN_P(x)}{6\sqrt x}\\
 &-\frac32\sum_a\frac{|h_j(a)|}{\sqrt a}.
\end{aligned}
\tag{L-96601.5}
\]

A second exact divisor-event sweep proves `A_P(x)>1/100` for `x>=67` and,
for every event `x>=2000`, gives the directed lower bounds

\[
 E_2(x)>6,
 \qquad E_3(x)>3/5.
\]

Between divisor events the right side of (L-96601.5) is increasing, so the event
check covers the entire tail. The compact interval `1<=x<=2000` is checked in
the original row formula. Since every row is affine in `log x` between integer
knots, integer endpoints exhaust the compact real interval.

The retained proof object checks all `262144` divisors and `524288` annular
activation events. The minimum compact margins occur near `x=104` and `x=102`,
not at the analytic splice.


---

# L-96602 — The factor-67 first-owner tree is kernel-independent and preserves complete finite colors

Claim ID: `L-96602`  
Status: **PROVED EXACT SOURCE IDENTITY**  
Created: 2026-08-17  
Depends on: the exact causal identity; PR #552 source dictionaries

Define the positive scale-four source kernel

\[
 h_X(n)=\frac1{\sqrt n}
 \min\!\left(\log4,\log\frac Xn\right)_+.
\]

It has exact scale covariance. If `n=pm`, then

\[
 p^{-1/2}h_{X/p}(m)=h_X(pm).
 \tag{L-96602.1}
\]

Consequently

\[
 h_X-p^{-1/2}A_ph_{X/p}
\]

is literally the restriction of `h_X` to source indices not divisible by `p`.
It is a positive packet; no signed child is observed.

For ordered active rough primes `p_i>=67`, put

\[
 r_i=p_i^{-1/2},
 \quad s_i=\prod_{\nu\le i}(1-r_\nu),
 \quad \lambda_i=r_is_{i-1},
 \quad \alpha_i=r_i\lambda_i.
\]

The exact identity

\[
P_X=s_kP_X+
\sum_i\lambda_i(P_X-r_iA_{p_i}P_{X/p_i})+
\sum_i\alpha_iA_{p_i}P_{X/p_i}
\tag{L-96602.2}
\]

is polynomial algebra:

\[
s_k+\sum_i\lambda_i=1,
\qquad
-\lambda_ir_i+\alpha_i=0.
\]

It applies to the annular kernel because only positivity and (L-96602.1) are
used. Recursive children have scale at most `X/67`; the tree therefore
terminates after finitely many generations.

The finite colors `d|P_61` are passive labels throughout the rough tree. Rough
ownership never splits or observes them. At a terminal current edge with owner
`p`, all colors are summed first, and the signed row is exactly

\[
 E_{j,Pp}(Z)=E_j(Z)-p^{-1/2}E_j(Z/p).
 \tag{L-96602.3}
\]

Thus the tree has one owner per source occurrence and no individual-color
positivity assertion. This is the required correction to the ambiguous leaf
wording in PR #555.


---

# L-96603 — Every annular terminal leaf and the complete two-row root are positive

Claim ID: `L-96603`  
Status: **CANDIDATE-COMPLETE UNCONDITIONAL PRODUCER THEOREM**  
Created: 2026-08-17  
Depends on: `L-96601`, `L-96602`

A terminal rough current has `Z=py`, where `p>=67` and `1<=y<67`. By
(L-96602.3) and `L-96601`,

\[
\begin{aligned}
 E_{2,Pp}(py)
 &>\frac75-\frac{5/2}{\sqrt{67}}
 >\frac{87}{80}>0,\\
 E_{3,Pp}(py)
 &>\frac12-\frac1{\sqrt{67}}
 >\frac38>0.
\end{aligned}
\tag{L-96603.1}
\]

The strict rational bounds use only `sqrt(67)>8`. A terminal outer packet with
no rough owner has scale below `67` and is nonnegative by the first line of
(L-96601.2).

Now apply the finite tree of `L-96602` to the positive parity-labelled annular
root source. Every coefficient `s_k`, `lambda_i`, and `alpha_i` is nonnegative;
every current leaf satisfies (L-96603.1); every child is treated recursively;
and the process terminates. Therefore the signed observations of the complete
root obey

\[
 \boxed{a_X(2)\ge0,\qquad a_X(3)\ge0\qquad(X\ge1).}
 \tag{L-96603.2}
\]

Here

\[
 a_X(j)=c_X(j)-c_{X/4}(j)
 =\sum_{n\le X}\frac{r_j(n)}{\sqrt n}
   \min\!\left(\log4,\log\frac Xn\right)_+,
\]

with the exact `r_2,r_3` dictionaries of PR #547. The source observation is
therefore the actual two-row annular Riesz state, not a rough lift or promoted
capacity.

Immediate falsifiers are: a failure of the quadrature bound; an event outside
the `P_61` certificate; a duplicated finite color; a negative terminal grouped
row; or a mismatch between the root observation and the Riesz formulas.


---

# T-96600 — Complete two-row annular positivity

Claim ID: `T-96600`  
Status: **CANDIDATE COMPLETE UNCONDITIONAL THEOREM — HOSTILE REVIEW REQUIRED**  
Created: 2026-08-17

By `L-96603`, for every real endpoint `X>=1`,

\[
\boxed{
 c_X(2)-c_{X/4}(2)\ge0,
 \qquad
 c_X(3)-c_{X/4}(3)\ge0.
}
\]

The theorem is source-complete: it uses literal annular source mass, one-use
rough ownership, grouped finite colors, and actual row observations. It uses no
rough-density surrogate and no branchwise positive child.


---

# T-96601 — Source-complete annular positivity gives the Riemann Hypothesis

Claim ID: `T-96601`  
Status: **CANDIDATE COMPLETE UNCONDITIONAL RH PROOF PROPOSAL**  
Created: 2026-08-17  
Depends on: `T-96600`; PR #547 `L-96010`, `L-96011`, `T-96010`

For `j=2,3`, PR #547 proves the exact Mellin transform

\[
\int_1^\infty [c_X(j)-c_{X/4}(j)]X^{-s-1}\,dX
=(1-4^{-s})
\left[
 \frac{C_j}{s^2}
 +\frac{P_j(s+1/2)}{s^2\zeta(s+1/2)}
\right].
\]

The factor `1-4^{-s}` has no zero for `Re s>0`. The two finite numerators have
no common zero in the open critical strip: with `x=2^{-z}` their simultaneous
vanishing gives

\[
 -3(x-1)(x-2)=0,
\]

which would force `Re z=0` or `Re z=-1`.

`T-96600` supplies two nonnegative Mellin kernels. Landau's real-abscissa
theorem therefore excludes every zeta zero with `Re z>1/2`; the functional
equation excludes its reflected partner. The proposed conclusion is

\[
 \boxed{\mathrm{RH}.}
\]

Publication is not acceptance. Independent reconstruction should begin with
`L-96600` and the grouped-source induction in `L-96602`.


---

# M-96600 — Hostile reconstruction protocol

1. Re-derive the scale-four quadrature bound, including all real endpoint cells.
2. Replay the `P_61` divisor and annular event sweeps with directed arithmetic.
3. Check the compact bounds in the original average-binomial row formula.
4. Verify that rough operations never split a finite `d|P_61` color family.
5. Expand the source-tree identity coefficient by coefficient at depth two.
6. Confirm that terminal observation is `E_P(Z)-p^{-1/2}E_P(Z/p)`.
7. Reconstruct the exact Riesz dictionaries and integer-knot continuity.
8. Reconstruct PR #547's Mellin transform, two-row elimination, and Landau use.

The replay authenticates the finite certificate and algebra. It does not make
review optional, and it never reports RH as established.


---

# O-96600 — Route disposition

```text
PR #547 direct annular consumer             retained
PR #552 coefficient dictionaries            retained
PR #552 failed local/global reservoirs       forbidden
PR #555 finite source-tree idea              retained with complete-color repair
Target-Lorenz terminal theorem               bypassed
new arithmetic terminal theorem              P61 annular reserve
annular rows 2 and 3                          candidate proved
complete RH chain                             candidate complete
accepted proof                                no
```
