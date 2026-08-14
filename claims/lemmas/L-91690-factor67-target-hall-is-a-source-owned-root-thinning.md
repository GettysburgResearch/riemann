# L-91690 — Factor-67 target Hall is a source-owned simultaneous root thinning

Claim ID: `L-91690`  
Status: **PROVED EXACT / DIRECTED ROOT-FIBER THEOREM ON FROZEN INPUTS**  
Created: 2026-08-14  
Frozen inputs: `L-91682`, `L-91688`; the single-SHARP component packet and causal zero extension  
Replay: `X-91690-factor67-sontr`  
RH status: **unproved at this claim**

## 1. Strict factor-67 root window

For a parent endpoint `X`, put

\[
 K_X=\left\lfloor\frac X{67}\right\rfloor+1.
\tag{L-91690.1}
\]

Then

\[
 K_X\le \frac X{67}+1,
 \qquad
 s\ge K_X\Longrightarrow 1\le x:=\frac Xs<67.
\tag{L-91690.2}
\]

The strict inequality is important. Every squarefree integer `k<x` has all
prime factors at most `61`. Thus the root Hall operation consumes only the
finite `P_61` source; the rough prime `67` and every larger rough prime remain
available to the first-owner recursive partition of `L-91688`.

For a squarefree `k<=x`, define the single-SHARP target, declared score and
component-row atoms

\[
 T_x(k)=\frac{4\sqrt{x/k}-3}{\sqrt k}
       =\frac{4\sqrt x}{k}-\frac3{\sqrt k},
\tag{L-91690.3}
\]

\[
 S_x(k)=\frac{5\sqrt{x/k}-3}{\sqrt k}
       =\frac{5\sqrt x}{k}-\frac3{\sqrt k},
\tag{L-91690.4}
\]

\[
 A_{x,j}(k)=\frac1{\sqrt k}Q_{x/k}(j),
 \qquad j\ge2.
\tag{L-91690.5}
\]

All target and score atoms are positive on their causal support.

## 2. Equality and reserve states stay positive through 67

Put

\[
 A(x)=\sum_{n\le x}\frac{\mu(n)}{\sqrt n},
 \qquad
 B(x)=\sum_{n\le x}\frac{\mu(n)}n,
\]

\[
 L(x)=2\sqrt x\,B(x)-A(x),
 \qquad
 R(x)=\sqrt x\,B(x)-A(x).
\tag{L-91690.6}
\]

The companion directed enumeration checks every arithmetic cell in
`1<=x<67` and proves

\[
\boxed{L(x)>\frac{159}{500}>0,}
\tag{L-91690.7}
\]

and, for `x>1`,

\[
\boxed{R(x)>\frac25>0.}
\tag{L-91690.8}
\]

The actual minima are

```text
L: 0.3186174007676585... on the cell 32 <= x < 33;
R: sqrt(2)-1 = 0.4142135623730950... on the first nontrivial cell.
```

Consequently the full single-SHARP state

\[
 \Psi(x)=L(x)+2R(x)
       =4\sqrt x\sum_{n\le x}\frac{\mu(n)}n
        -3\sum_{n\le x}\frac{
        \mu(n)}{\sqrt n}
\tag{L-91690.9}
\]

is strictly positive on the complete factor-67 root window.

## 3. Exact target Hall prefix theorem

Let

\[
 E_x=\{e\le x:\mu(e)=1\},
 \qquad
 O_x=\{o\le x:\mu(o)=-1\}.
\]

For an active odd threshold `t`, the no-upward target Hall prefix is

\[
\begin{aligned}
 H_t(x)
 &:=\sum_{\substack{e\le t\\\mu(e)=1}}T_x(e)
   -\sum_{\substack{o\le t\\\mu(o)=-1}}T_x(o)\\
 &=4\sqrt x\,A_t-3B_t,
\end{aligned}
\tag{L-91690.10}
\]

where

\[
 A_t=\sum_{n\le t}\frac{\mu(n)}n,
 \qquad
 B_t=\sum_{n\le t}\frac{\mu(n)}{\sqrt n}.
\]

On the cell `t<=x<67`, this is affine in `sqrt(x)`. Its minimum is at `x=t`
when `A_t>=0`, and at the limiting endpoint `x=67` when `A_t<0`.
Exact/directed evaluation of all `22` odd Möbius thresholds gives

\[
\boxed{H_t(x)>\frac7{20}}
\qquad
(t\le x<67,\ \mu(t)=-1).
\tag{L-91690.11}
\]

The unique minimum is approached at

\[
 t=13,
 \qquad x\uparrow67,
\]

with directed lower value

\[
 H_{13}(67)>0.3593176605985002\ldots>\frac7{20}.
\tag{L-91690.12}
\]

The nested-neighborhood Hall theorem therefore supplies a deterministic
nonnegative target-mass transport

\[
 t_x(o,e)\ge0,
 \qquad
 t_x(o,e)>0\Longrightarrow e\le o,
\tag{L-91690.13}
\]

such that

\[
 \sum_e t_x(o,e)=T_x(o),
 \qquad
 \sum_o t_x(o,e)\le T_x(e).
\tag{L-91690.14}
\]

Define

\[
 \nu_x(e)=1-\frac1{T_x(e)}\sum_o t_x(o,e)\in[0,1].
\tag{L-91690.15}
\]

Every root source occurrence is now used at most once: in one matched pair or
in the residual coefficient `nu_x(e)`.

## 4. Exact target and favorable score ledger

Target conservation gives

\[
\boxed{
 \sum_{k\le x}\mu(k)T_x(k)
 =\sum_{e\in E_x}\nu_x(e)T_x(e).
}
\tag{L-91690.16}
\]

Thus the residual positive source is target-exact, not merely subordinate.

For `z>=1`, put

\[
 f(z)=\frac{5z-3}{4z-3}.
\]

Then

\[
 f'(z)=-\frac3{(4z-3)^2}<0.
\tag{L-91690.17}
\]

If `e<=o`, then `sqrt(x/e)>=sqrt(x/o)` and therefore

\[
 \frac{S_x(e)}{T_x(e)}
 \le
 \frac{S_x(o)}{T_x(o)}.
\tag{L-91690.18}
\]

Using the same target flow in the score coordinate yields

\[
\boxed{
 \sum_e\nu_x(e)S_x(e)
 \ge
 \sum_{k\le x}\mu(k)S_x(k).
}
\tag{L-91690.19}
\]

The root thinning creates no declared-score debt.

## 5. Simultaneous all-row bonus

For every component row, define

\[
 \rho_{x,j}(k)
 =\frac{A_{x,j}(k)}{T_x(k)}
 =\frac{Q_{x/k}(j)}{4\sqrt{x/k}-3}.
\tag{L-91690.20}
\]

The global target-normalized profile theorem in frozen `L-91682` says that

\[
 Y\longmapsto\frac{Q_Y(j)}{4\sqrt Y-3}
\]

is increasing on its causal support. Hence `e<=o` gives

\[
 \rho_{x,j}(e)\ge\rho_{x,j}(o).
\tag{L-91690.21}
\]

Define the target-null row bonus

\[
 B_{x,j}
 =\sum_{o,e}t_x(o,e)
  [\rho_{x,j}(e)-\rho_{x,j}(o)]\ge0.
\tag{L-91690.22}
\]

Then the same source coefficients give, simultaneously for every `j`,

\[
\boxed{
 \sum_{k\le x}\mu(k)A_{x,j}(k)
 =\sum_e\nu_x(e)A_{x,j}(e)+B_{x,j}.
}
\tag{L-91690.23}
\]

This is one atomwise source-owned target/score/row identity. It is not a
coordinatewise complement and does not invoke stopped-leaf Hall.

## 6. Rough ownership and causal reset

Attach to every residual root occurrence its exact first-owner rough label from
`L-91688`. The root Hall labels and rough first-owner labels are disjoint:
root Hall sees only `P_61` divisors, while the first rough owner is at least
`67`.

Apply the frozen causal identity to each positive residual packet. For ordered
active rough primes `p_i>=67`, put

\[
 r_i=p_i^{-1/2},
 \quad
 s_i=\prod_{h\le i}(1-r_h),
 \quad
 \lambda_i=r_is_{i-1},
 \quad
 \alpha_i=r_i\lambda_i.
\]

Then

\[
 P=s_kP+
 \sum_i\lambda_i(P-r_iU_{p_i}P_{/p_i})+
 \sum_i\alpha_iU_{p_i}P_{/p_i},
\tag{L-91690.24}
\]

and

\[
 s_k+\sum_i\lambda_i=1,
 \qquad
 \sum_i\alpha_i<67^{-1/2}<\frac18.
\tag{L-91690.25}
\]

Every current difference is a positive typed causal generator on the frozen
inputs, and every rough monomial is owned once by `L-91688`. The row bonuses
`B_x` remain current and are never copied to a child.

## 7. Exact boundary

```text
strict P61-only root window x<67                 EXACT
equality/reserve positivity through factor 67   DIRECTED EXACT
target Hall prefixes >7/20                       DIRECTED EXACT
source-owned target-exact residual               EXACT
score superordination                            EXACT
simultaneous nonnegative all-row bonus            EXACT
rough first-owner provenance                     EXACT / L-91688
causal recursive coefficient mass <1/8            EXACT
finite physical realization and corrections       NEXT LEMMA
Riemann Hypothesis                               UNPROVEN AT THIS CLAIM
```
