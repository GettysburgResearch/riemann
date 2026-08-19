# L-99050 — Expand first, score last: the complete causal tree is literal-score isometric

Claim ID: `L-99050`  
Status: **PROPOSED COMPLETE EXACT THEOREM**  
Created: 2026-08-19  
Frozen parent: PR #620 at `493e12fcba3f9b98dda7c3595bff73b256e00ca4`  
RH status: **not assumed**

## 1. The score-last principle

Let `R(P)` be the physical component row of a positive residual-source packet
`P`, and let

\[
 \mathcal H(R)=\sum_{j\ge2}R(j)G_j
\]

be its literal average-binomial entropy score. The weights `G_j` are
nonnegative, and `H` is a linear functional of the **physical row**.

The conclusion-producing recursion should therefore be scored only after its
complete positive row has been assembled. No declared source-score coordinate
is needed in the recursion.

## 2. One exact node

At a node with endpoint `Y`, let the active rough primes be

\[
 67\le p_1<\cdots<p_k,
 \qquad r_i=p_i^{-1/2},
\]

and put

\[
 s_i=\prod_{h\le i}(1-r_h),
 \qquad
 \lambda_i=r_i s_{i-1},
 \qquad
 \alpha_i=r_i\lambda_i.
\]

With the same-index child placement `U_i`, the exact causal identity of
`L-99021` is

\[
 P=s_kP+\sum_i\lambda_i(P-r_iU_iP_i)
   +\sum_i\alpha_iU_iP_i.
\tag{L-99050.1}
\]

Define the current packet

\[
 P^{\rm cur}:=s_kP+\sum_i\lambda_i(P-r_iU_iP_i).
\tag{L-99050.2}
\]

Every coefficient and every row coordinate of `P^cur` is nonnegative. Since

\[
 s_k+\sum_i\lambda_i=1,
 \qquad
 \alpha_i=r_i\lambda_i,
\]

one has the simpler exact row identity

\[
\boxed{
 R(P)=R(P^{\rm cur})+\sum_i\alpha_iR(U_iP_i).
}
\tag{L-99050.3}

Applying literal entropy gives, with no inequality,

\[
\boxed{
 \mathcal H(R(P))
 =\mathcal H(R(P^{\rm cur}))
  +\sum_i\alpha_i\mathcal H(R(U_iP_i)).
}
\tag{L-99050.4}

This is a physical-row identity. It neither uses nor compares a declared
source score.

## 3. The recursion has finite depth

Every recursive child endpoint satisfies the frozen scale bound

\[
 Y'\le Y/67+1.
\tag{L-99050.5}
\]

Put

\[
 a=\frac{67}{66}.
\]

Then

\[
 Y'-a\le\frac{Y-a}{67}.
\tag{L-99050.6}
\]

Consequently, after `n` recursive transitions,

\[
 Y_n-a\le67^{-n}(Y_0-a).
\tag{L-99050.7}
\]

Every path reaches `Y<67` after finitely many steps. At fixed `X`, every node
has only finitely many active rough primes. Hence the complete causal tree is
finite; no limiting, martingale-convergence, leaf-count, or summability theorem
is required to define its final row.

## 4. Exact finite-tree identity

Expand every child in (L-99050.3) until it reaches its terminal node. Let
`I(P)` be the set of all current nodes and `L(P)` the set of terminal leaves,
with their products of causal coefficients denoted by `w_v>=0`. Repeated
substitution gives

\[
\boxed{
 R(P)
 =\sum_{v\in I(P)}w_vR(P_v^{\rm cur})
  +\sum_{\ell\in L(P)}w_\ell R(P_\ell).
}
\tag{L-99050.8}

Every summand is a nonnegative physical row and every source occurrence has
exactly one current or terminal owner. Applying literal entropy once, after
the expansion, gives

\[
\boxed{
 \mathcal H(R(P))
 =\sum_{v\in I(P)}w_v\mathcal H(R(P_v^{\rm cur}))
  +\sum_{\ell\in L(P)}w_\ell\mathcal H(R(P_\ell)).
}
\tag{L-99050.9}

Thus the arithmetic causal tree is **literal-score isometric**. It has no
terminal score-realization debt.

## 5. Hall and endpoint integration

The compact Hall identity of `L-99020` is an exact physical-row equality

\[
 R_{\rm signed}=R(P_{\rm res})+B,
 \qquad B(j)\ge0.
\tag{L-99050.10}

The Hall bonus `B` is current-only. Since `G_j>=0`, it has nonnegative literal
score. Apply (L-99050.8) to the residual source only and then add `B` once.
The resulting row is exactly `R_signed`.

Positive endpoint integration and the optional exact finite cubature of
`L-99022` commute with every finite sum in (L-99050.8). Therefore the complete
unthinned common-parent row has exactly the literal score of the equality-frame
row. On the frozen endpoint-frame identity,

\[
\boxed{
 \mathcal H(R_X^{\rm eq})=4\sqrt X.
}
\tag{L-99050.11}

No score is assigned to a target-null Hall edge, no source-declared score is
substituted for literal entropy, and no packetwise positive part is taken.

## 6. Scope

This theorem does not replace the compact Hall/profile theorem, the exact
endpoint-frame identity (L-99050.11), or the all-column capacity theorem. It
proves that, once those physical-row identities hold, the complete arithmetic
recursion introduces **zero** literal-score loss.

```text
one-node causal row identity              exact
finite depth of actual rough-prime tree   exact
complete positive row expansion           exact
literal-score preservation                exact
Hall bonus recursive export               forbidden
terminal declared-score debt              unnecessary
Riemann Hypothesis                         unproved
```
