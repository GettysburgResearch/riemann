# L-33107 — Size-weighted balanced fragmentation is exactly a Markov occupation equation

Claim ID: `L-33107`  
Title: Multiplying node divergence by node size turns every nonnegative balanced split flow into the occupation equation of the size-biased child Markov chain, and conversely  
Status: **PROPOSED COMPLETE EXACT FINITE LEMMA — INDEPENDENT REVIEW REQUESTED**  
Authoring agent: `gpt56-pro-09-v`  
Created: 2026-08-09  
Dependencies: PR #247 `L-23810`; `L-33102/L-33104`  
Scope: exact finite primal bridge; no positivity theorem for the critical Möbius occupation and no RH conclusion

## 1. Split flow and node divergence

Fix an endpoint `X` and any declared family of balanced unordered splits

\[
 e=(n,j),\qquad n=j+(n-j),\qquad 1\le j\le n/2.
\]

Let `d_(n,j)>=0` be a nonnegative split flow and put

\[
 D_n=\sum_j d_{n,j}.
\tag{L-33107.1}
\]

Its node divergence is

\[
 r_n=D_n-
 \sum_{m>n}\sum_jd_{m,j}
 [\mathbf1_{n=j}+\mathbf1_{n=m-j}],
\tag{L-33107.2}
\]

with the central child counted twice, exactly as in `L-23810`.

Define the size-weighted outgoing occupation

\[
\boxed{M_n=nD_n.}
\tag{L-33107.3}
\]

## 2. Size-biased child kernel

Whenever `D_n>0`, normalize the split law

\[
 \pi_n(j)={d_{n,j}\over D_n}.
\]

Given one split `j+(n-j)=n`, choose one child by following a uniformly selected unit of the parent mass. Thus that edge sends the Markov state to `j` with probability `j/n` and to `n-j` with probability `(n-j)/n`.

The resulting selected-child kernel is

\[
\boxed{
 P_n(k)=\sum_j\pi_n(j)
 \left[{j\over n}\mathbf1_{k=j}
       +{n-j\over n}\mathbf1_{k=n-j}\right].
}
\tag{L-33107.4}

At a central split the two displayed contributions coincide and sum to one. Hence `P_n` is a probability distribution supported strictly below `n`.

If `D_n=0`, choose any admissible `P_n`; it will be multiplied by `M_n=0` below.

## 3. Exact occupation equation

For every child node `k`,

\[
\begin{aligned}
 \sum_{n>k}M_nP_n(k)
 &=\sum_{n>k}nD_n
   \sum_j{d_{n,j}\over D_n}
   \left[{j\over n}\mathbf1_{k=j}
   +{n-j\over n}\mathbf1_{k=n-j}\right]\\
 &=k\sum_{n>k}\sum_jd_{n,j}
 [\mathbf1_{k=j}+\mathbf1_{k=n-j}].
\end{aligned}
\]

Multiplying (L-33107.2) by `k` therefore gives

\[
\boxed{
 k r_k
 =M_k-\sum_{n>k}M_nP_n(k).
}
\tag{L-33107.5}

In row-vector notation, with

\[
 s_k=kr_k,
\]

this is

\[
\boxed{M-MP=s.}
\tag{L-33107.6}

Because `P` is strictly lower triangular in node size, `I-P` is invertible and

\[
\boxed{M=s(I-P)^{-1}=s(I+P+\cdots+P^{X-1}).}
\tag{L-33107.7}

Thus the outgoing fragmentation mass is literally the Green occupation measure of the signed size-weighted source `s` under the size-biased child chain.

## 4. Converse

Conversely choose, for every parent `n`, any probability law `pi_n` on admissible balanced splits and form its size-biased child kernel `P` by (L-33107.4).

Suppose the unique solution of

\[
 M-MP=s,
 \qquad s_n=nr_n,
\tag{L-33107.8}
\]

satisfies

\[
 M_n\ge0\qquad(2\le n\le X).
\]

Put

\[
 D_n={M_n\over n},
 \qquad
 d_{n,j}=D_n\pi_n(j).
\tag{L-33107.9}
\]

Reversing the calculation in Section 3 gives exactly

\[
 \partial d=r.
\]

Therefore

\[
\boxed{
 M\ge0
 \quad\Longleftrightarrow\quad
 \text{the chosen split policy produces a nonnegative exact fragmentation of }r.
}
\tag{L-33107.10}

For the critical Möbius divergence `r_X` of PR #247, such an occupation measure gives exact carry saturation by `L-23810`.

## 5. Uniform balanced policy

Fix `0<eta<1/2`. For each parent let

\[
 J_n=\{j:\lceil\eta n\rceil\le j\le\lfloor n/2\rfloor\}
\]

and take `pi_n` uniform on `J_n`. If `m_n=|J_n|`, then

\[
\boxed{
 P_n(k)={k\over nm_n}
 \left[\mathbf1_{k\in J_n}+\mathbf1_{n-k\in J_n}\right].
}
\tag{L-33107.11}

The central state is automatically counted twice.

Under `k/n -> v`, the selected-child law converges to

\[
\boxed{
 p_\eta(v)={2v\over1-2\eta}
 \mathbf1_{\eta\le v\le1-\eta}.
}
\tag{L-33107.12}

For the repository's standard quarter-balanced cone `eta=1/4`,

\[
\boxed{p_{1/4}(v)=4v\,\mathbf1_{1/4\le v\le3/4}.}
\tag{L-33107.13}

In logarithmic decrement `Y=-log V`, this is the compact exponential kernel

\[
\boxed{
 p_Y(y)=4e^{-2y}\,
 \mathbf1_{\log(4/3)\le y\le\log4}.
}
\tag{L-33107.14
}

and its Mellin moments are

\[
\boxed{
 \mathbb E[V^z]
 ={4\over z+2}
 \left[\left({3\over4}\right)^{z+2}
       -\left({1\over4}\right)^{z+2}\right].
}
\tag{L-33107.15
}

## 6. Why this changes the MPL interface

Previously the relation between

```text
balanced fragmentation
and
size-biased Pascal/Gamma states
```

was only expressed through individual split expectations. Equations (L-33107.5)--(L-33107.10) identify the **entire primal fragmentation problem** with one descending Markov occupation equation.

A production Martingale Pascal Lift may therefore be specified by a state-dependent balanced Markov kernel `P`; it does not need a separate Pascal-cycle object after the occupation measure is shown nonnegative or to have subpower negative debt.

The arithmetic difficulty remains in the sign of the Green occupation `s(I-P)^(-1)` for the actual Möbius source. This lemma does not infer that sign from the positive child kernel.

## 7. Proof boundary

Established exactly:

1. size-weighted divergence identity;
2. selected-child Markov kernel for an arbitrary split policy;
3. exact Green occupation equation;
4. converse reconstruction of a nonnegative balanced fragmentation;
5. explicit uniform-balanced finite kernel;
6. its compact continuum selected-child law.

Still open:

1. nonnegativity or subpower negative part of the critical Möbius Green occupation for any explicit cofinal policy;
2. MPL/Cycle Debt;
3. RH.
