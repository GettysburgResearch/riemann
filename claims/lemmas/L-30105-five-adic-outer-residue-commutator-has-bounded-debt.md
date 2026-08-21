# L-30105 — The outer five-adic residue commutator has bounded Cycle Debt

Claim ID: `L-30105`  
Title: In the exact five-adic source decomposition, every cross-residue dipole above one-fifth scale is discharged by legal adjacent-tree commutators with one absolute total capacity bound  
Status: **PROPOSED COMPLETE ELEMENTARY THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: PR #322 `T-30107`; PR #272 adjacent-tree commutators; elementary calculus  
Scope: complete current-scale outer four-fifths of the five-adic residue source; the inner one-fifth residue automaton remains open

## 1. Critical source and five-adic block coefficients

Let

\[
 w_X(q)=q^{-1/2}\log(X/q),
 \qquad 2\le q\le X,
\]

and define the exact multiple-Möbius coordinate

\[
 U_X(m)=\sum_{d\le X/m}\mu(d)w_X(md),
 \qquad U_X(X+1)=0,
\]

with divergence

\[
 r_X(m)=U_X(m)-U_X(m+1).
\]

Assume for this lemma that

\[
 X=5Y.
\]

For a complete five-block and `1<=j<=4`, put

\[
 c_{a,j}=\sum_{\ell=j}^4r_X(5a+\ell).
\]

The sum telescopes exactly:

\[
 \boxed{
 c_{a,j}=U_X(5a+j)-U_X(5a+5).
 }
 \tag{L-30105.1}
\]

The elementary block identity used in `T-30107` is

\[
\boxed{
\sum_{j=0}^4r_X(5a+j)e_{5a+j}
=
\left(\sum_{j=0}^4r_X(5a+j)\right)e_{5a}
+
\sum_{j=1}^4c_{a,j}(e_{5a+j}-e_{5a+j-1}).
}
\tag{L-30105.2}
\]

The first term is the five-divisible critical channel.  This lemma closes the
current-scale part of the second term.

## 2. Explicit formula in the outer four-fifths

Extend `U_X` piecewise to real `x` by

\[
U_X(x)
=x^{-1/2}\sum_{d\le X/x}
 {\mu(d)\over\sqrt d}\log{X\over xd}.
\tag{L-30105.3}
\]

If

\[
Y<x\le X,
\]

then `floor(X/x)<=4`, except at the left endpoint where the entering `d=5`
term has value zero.  On a quotient cell with

\[
K=\left\lfloor {X\over x}\right\rfloor\le4,
\]

write

\[
A_K=\sum_{d\le K}{\mu(d)\over\sqrt d},
\qquad
B_K=\sum_{d\le K}{\mu(d)\log d\over\sqrt d}.
\]

Then

\[
\boxed{
U_X(x)=x^{-1/2}\left[A_K\log{X\over x}-B_K\right].
}
\tag{L-30105.4}
\]

Only

\[
\mu(1)=1,
\quad \mu(2)=\mu(3)=-1,
\quad \mu(4)=0
\]

occur.  Hence

\[
|A_K|<3,
\qquad
|B_K|<2,
\qquad
0\le\log(X/x)<\log5<2.
\tag{L-30105.5}
\]

Inside each cell,

\[
U_X'(x)
=x^{-3/2}
\left[-A_K-{A_K\over2}\log{X\over x}+{B_K\over2}\right],
\]

so

\[
\boxed{
|U_X'(x)|\le7x^{-3/2}
\qquad(Y<x<X).
}
\tag{L-30105.6}
\]

At a quotient boundary a new Möbius term enters with

\[
\log {X\over xd}=0,
\]

so `U_X` is continuous.  Therefore (L-30105.6) integrates across quotient
boundaries without an additional jump term.

## 3. Every outer block coefficient has cubic decay

Let

\[
n=5a+j,
\qquad1\le j\le4,
\qquad n>Y.
\]

The other endpoint in (L-30105.1) is `5a+5`, at distance at most four.  The
whole interval lies in `(Y,X]`.  Thus

\[
\begin{aligned}
|c_{a,j}|
&=|U_X(n)-U_X(5a+5)|\\
&\le\int_n^{5a+5}7x^{-3/2}\,dx\\
&\le28n^{-3/2}.
\end{aligned}
\]

Hence

\[
\boxed{
|c_{a,j}|\le28(5a+j)^{-3/2}
\qquad(5a+j>Y).
}
\tag{L-30105.7}
\]

This estimate is source-specific.  It is false to infer it for the inner
one-fifth, where further Möbius coefficients enter.

## 4. Adjacent-tree commutator realization

Let

\[
E_m=T_{m+1}-T_m
\]

be the legal adjacent-tree commutator of PR #272.  Its divergence is

\[
\boxed{
\partial E_m=e_{m+1}-e_m-e_1.
}
\tag{L-30105.8}
\]

The node `1` term is invisible to every carry column `q>=2` and is the exact
size-conservation companion of an adjacent node dipole.

The sparse recursion is

\[
E_{2h}=[2h+1,h]-[2h,h]+E_h,
\]

\[
E_{2h+1}=[2h+2,h+1]-[2h+1,h]+E_h.
\]

Every displayed split is balanced.  Since one split with parent `m` has
capacity at most `2sqrt(m)`, the total weighted variation obeys

\[
\|E_m\|_\omega
\le4\sqrt{m+1}+\|E_{\lfloor m/2\rfloor}\|_\omega.
\tag{L-30105.9}
\]

Induction gives the convenient absolute bound

\[
\boxed{
\|E_m\|_\omega\le24\sqrt{m+1}.
}
\tag{L-30105.10}
\]

Indeed the constant `24` closes (L-30105.9) already at the smallest nontrivial
parent, and the ratio of successive square-root scales is at most `2^{-1/2}`
thereafter.

For arbitrary real `c`, negative capacity debt is bounded by total variation:

\[
\mathcal N_\omega(cE_m)
\le |c|\,\|E_m\|_\omega.
\tag{L-30105.11}
\]

Thus no sign assumption on `c_(a,j)` is required.

## 5. Uniform bound for the complete outer residue family

Define the current-scale outer residue source

\[
\mathcal R_X^{\rm out}
=
\sum_{\substack{a\ge0,\ 1\le j\le4\\Y<5a+j\le X}}
 c_{a,j}(e_{5a+j}-e_{5a+j-1}).
\tag{L-30105.12}
\]

Use the explicit legal flow

\[
\boxed{
\mathcal F_X^{\rm out}
=
\sum_{\substack{a,j\\Y<5a+j\le X}}
 c_{a,j}E_{5a+j-1}.
}
\tag{L-30105.13}
\]

By (L-30105.8), its divergence agrees with
`mathcal R_X^(out)` on every node `>=2`; the accumulated node-one term is
carry-invisible.

Equations (L-30105.7), (L-30105.10), and (L-30105.11) give

\[
\begin{aligned}
\mathcal N_\omega(\mathcal F_X^{\rm out})
&\le
\sum_{Y<n\le5Y}
28n^{-3/2}\,24\sqrt n\\
&\le672\sum_{n=Y+1}^{5Y}{1\over n}\\
&\le672\log5\\
&<1344.
\end{aligned}
\]

Therefore

\[
\boxed{
\mathcal N_\omega(\mathcal F_X^{\rm out})<1344
\qquad(X=5Y).
}
\tag{L-30105.14}
\]

The constant is intentionally crude.  The theorem is the scale-free bound,
not its numerical optimization.

## 6. Consequence for the five-adic renewal programme

The five-adic source decomposition has now separated into three pieces:

```text
five-divisible critical channel
    exact scaled copy of the lower endpoint;

outer nonmultiple residue channel, nodes > X/5
    closed here with O(1) Cycle Debt;

inner nonmultiple residue channel, nodes <= X/5
    the sole unresolved residue state.
```

Thus no current-scale residue obstruction survives outside the inner fifth.
The finite residue automaton of `T-30107` is needed only to propagate/recombine
that inner source.  It may not charge the already-closed outer family again.

This is stronger than an endpoint-count statement: the theorem emits the legal
flow and an absolute negative-capacity certificate.

## 7. Proof boundary

Closed here:

1. the telescoped five-block coefficients;
2. the exact outer four-band formula using only `mu(1),...,mu(4)`;
3. continuity at quotient boundaries;
4. cubic adjacent-decay of every outer residue coefficient;
5. a legal adjacent-tree commutator realization;
6. one absolute total Cycle-Debt bound for the entire outer family.

Open:

1. the inner one-fifth residue automaton;
2. a strict all-generation Cycle-Debt recurrence;
3. RH.
