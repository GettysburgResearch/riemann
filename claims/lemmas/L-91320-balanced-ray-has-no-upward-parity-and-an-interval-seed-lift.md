# L-91320 — The balanced rough-prime channel has a strict no-upward parity shadow and an exact divisor-faithful interval-seed lift

Claim ID: `L-91320`  
Status: **PROPOSED COMPLETE EXACT FINITE-WINDOW / SEED-LIFT THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-12  
Depends on: `L-91105`, `L-91109`, `L-91311`, `L-91315`  
RH status: **unproved**

## 1. The balanced channel is one ordinary parity channel

Put

\[
 z_0=\zeta(1/2),
 \qquad
 \kappa_*=-\frac{2(1+z_0)}{2+z_0},
 \qquad
 c_*=\frac1{2+z_0}.
\]

Retain

\[
 H_*=L+\kappa_*R.
\]

Since

\[
 1+\kappa_*=-\frac{z_0}{2+z_0},
 \qquad
 2+\kappa_*=rac2{2+z_0},
\]

one has

\[
 \boxed{
 a_*:=\frac{2+\kappa_*}{1+\kappa_*}
 =-\frac2{z_0}
 }
\tag{L-91320.1}
\]

and

\[
 \boxed{
 H_*(x)
 =(1+\kappa_*)
 \left[a_*\sqrt x\,B(x)-A(x)\right].
 }
\tag{L-91320.2}
\]

Moreover

\[
 \boxed{
 c_*=\frac{(1+\kappa_*)a_*}{2}.
 }
\tag{L-91320.3}
\]

Thus the unique mass-and-score-neutral ray is not an artificial linear
combination.  It is one ordinary Möbius parity channel with parameter
`a_*=-2/zeta(1/2)`, followed by a positive scalar normalization.

For every squarefree `n<=x`, define

\[
 w_*(x,n)=w_2(x,n)+\kappa_*w_1(x,n)
 =(1+\kappa_*)w_{a_*}(x,n)>0.
\tag{L-91320.4}
\]

Let `E_*^x` and `O_*^x` be the corresponding positive even- and odd-parity
measures. Then

\[
 \boxed{
 \|E_*^x\|-\|O_*^x\|=H_*(x).
 }
\tag{L-91320.5}
\]

## 2. A directed lower bound for the balanced coefficient

The alternating eta series gives

\[
 \eta(1/2)=\sum_{n\ge1}(-1)^{n-1}n^{-1/2},
 \qquad
 z_0=\frac{\eta(1/2)}{1-\sqrt2}.
\]

The companion verifier encloses the first 100 terms and the alternating
remainder using exact `Fraction` arithmetic and directed square-root intervals.
It proves

\[
 \boxed{
 -\frac85<z_0<-\frac43,
 \qquad
 \kappa_*>1.
 }
\tag{L-91320.6}
\]

Only the weak lower bound `kappa_*>1` is used below.

## 3. Strict equality Hall margin without the historical `+1`

For an active odd threshold `t`, define the strict no-upward equality margin

\[
 \mathcal H^{0}_{2,t}(x)
 =
 \sum_{\substack{e\le t\\\mu(e)=1}}w_2(x,e)
 -
 \sum_{\substack{o\le t\\\mu(o)=-1}}w_2(x,o).
\tag{L-91320.7}
\]

Unlike the one-step margin of `L-91109`, this quantity can be negative.  The
directed checker proves on the complete reset window

\[
 \boxed{
 \mathcal H^{0}_{2,t}(x)>-\frac9{50}.
 }
\tag{L-91320.8}
\]

`L-91109` already gives

\[
 \mathcal H_{1,t}(x)>\frac{39}{100}.
\tag{L-91320.9}
\]

The balanced Hall margin is

\[
 \mathcal H_{*,t}(x)
 =\mathcal H^{0}_{2,t}(x)
  +\kappa_*\mathcal H_{1,t}(x).
\tag{L-91320.10}
\]

Using `kappa_*>1`,

\[
 \boxed{
 \mathcal H_{*,t}(x)
 >-\frac9{50}+\frac{39}{100}
 =\frac{21}{100}>\frac15
 }
\tag{L-91320.11}
\]

for every

\[
 1\le x\le c_0^{-1}
\]

and every active odd threshold.

Therefore Hall's theorem gives a positive transport

\[
 \boxed{
 \pi_*^x:O_*^x\longrightarrow E_*^x
 }
\tag{L-91320.12}
\]

with the stronger support condition

\[
 \boxed{e\le o.}
\tag{L-91320.13}
\]

No upward adjacent correction is needed in the balanced channel.  The unspent
even mass is exactly `H_*(x)`.

This is the first state in the factor-54 architecture which is simultaneously:

```text
strictly inside the positive (L,R) wedge;
mass neutral after centering;
endpoint-score neutral after centering;
and monotone-parity transportable with no +1 displacement.
```

## 4. Monotone parity transport is a nonnegative interval seed

Let `pi(e,o)>=0` be any finite transport supported on `e<=o`.  Define

\[
 \boxed{
 I_\pi(n)
 =\sum_{e<n\le o}\pi(e,o).
 }
\tag{L-91320.14}
\]

Then `I_pi(n)>=0` coefficientwise.  With the adjacent-difference convention

\[
 c_\pi(n)=I_\pi(n)-I_\pi(n+1),
\]

each edge contributes

\[
 1_{e<n\le o}-1_{e<n+1\le o}
 =1_{n=o}-1_{n=e}.
\]

Consequently

\[
 \boxed{
 c_\pi
 =O_\pi-E_\pi,
 }
\tag{L-91320.15}
\]

where `O_pi` is the complete matched odd demand and `E_pi` is the even capacity
used by the transport.

If `E_*=E_pi+E_res`, then

\[
 \boxed{
 E_*-O_*=E_{res}-c_\pi,
 \qquad E_{res}\ge0.
 }
\tag{L-91320.16}
\]

Thus the signed parity cancellation splits exactly into:

```text
one nonnegative residual even measure;
minus the adjacent difference of one nonnegative interval seed.
```

No signed Möbius inversion is used in this step.

## 5. Exact divisor and radix-four lift

For a finite seed `F`, write

\[
 v_q(F)=\sum_{k\ge1}[F(kq)-F(kq+1)].
\]

Equation (L-91320.15) gives

\[
 \boxed{
 v_q(I_\pi)
 =\sum_{k\ge1}c_\pi(kq)
 =\sum_{e,o}\pi(e,o)
  [1_{q\mid o}-1_{q\mid e}].
 }
\tag{L-91320.17}
\]

Hence the transport preserves the exact divisor destinations of every matched
odd/even atom.  The radix-four detail is likewise

\[
 \boxed{
 \mathcal D_4v_q(I_\pi)
 =\sum_{e,o}\pi(e,o)
  [h_q(o)-h_q(e)],
 }
\tag{L-91320.18}
\]

with

\[
 h_q(n)=1_{q\mid n}-2\,1_{4q\mid n}.
\]

The companion replay checks (L-91320.15)--(L-91320.18) for all 1,485 monotone
edges in the factor-54 state space and every column `q<=54`.

This closes the previously missing passage

```text
ordered Hall transport
    -> exact divisor destinations
    -> exact radix-four destinations
```

at the positive-seed level.

## 6. Exact score of the interval seed

Let

\[
 \ell_n=\log\frac n{n-1}.
\]

For one edge `e<o`,

\[
 \sum_n1_{e<n\le o}\ell_n
 =\log\frac oe.
\]

Therefore

\[
 \boxed{
 \sum_nI_\pi(n)\ell_n
 =\sum_{e<o}\pi(e,o)\log\frac oe
 \ge0.
 }
\tag{L-91320.19}
\]

The monotone parity correction is not merely a coefficientwise positive seed;
it is automatically score-favorable.

## 7. Consequence for the rough-prime reset

At every factor-54 child scale, the balanced state `H_*` can now be handled by:

1. the strict no-upward parity transport `pi_*`;
2. the nonnegative interval seed `I_(pi_*)`;
3. its exact divisor/radix-four carry image;
4. the nonnegative unspent even reserve of total mass `H_*`.

The historical equality `+1` displacement and its special adjacent correction
disappear on the balanced ray.

Together with `L-91315`, this shows that the canonical rough-prime bulk state is
simultaneously neutral in both scalar ledgers and admits a source-faithful
monotone parity cancellation in every reset window.

## 8. Remaining endpoint-row gate

The interval seed `I_(pi_*)` is nonnegative, exact, divisor-faithful and
score-favorable.  What is not proved is that it belongs to the cone generated
by nonnegative parabolic endpoint rows after the already constructed outer
packing is fixed.

Equivalently, one must prove one of:

```text
the positive endpoint Volterra inverse of I_(pi_*);
a nonnegative butterfly/boundary realization of I_(pi_*);
or domination of I_(pi_*) by the resident positive outer endpoint reserve.
```

That is now the sole local lift between the balanced rough branching and the
actual endpoint-row cone.  The complementary positive reserve
`(2-kappa_*)R` and the decaying finite boundary port of `L-91315` remain to be
included in the same column ledger.

## 9. Proof boundary

```text
balanced ray = one ordinary parity channel             EXACT
kappa_*>1 directed from eta series                      DIRECTED EXACT
strict equality no-upward margin > -9/50               DIRECTED EXACT
balanced no-upward Hall margin > 1/5                   DIRECTED EXACT
monotone Hall transport e<=o                            EXACT
nonnegative interval-seed lift                          EXACT
exact divisor and radix-four destination preservation  EXACT
nonnegative interval-seed score                         EXACT
endpoint-row cone realization                           OPEN
complete coefficient-one rough allocation               OPEN / RH-BEARING
Riemann Hypothesis                                      UNPROVED
```
