# L-91670 — A single SHARP channel has exact native row and score normalization

Claim ID: `L-91670`  
Status: **PROVED EXACT NORMALIZATION / SOURCE-TREE THEOREM ON FROZEN ROW-MONOTONICITY INPUTS**  
Created: 2026-08-14  
Supersedes for root normalization: `L-91330`'s two-channel row conclusion and
the false row identification in `L-91668`  
Primary inputs: the parameter-`a` source recursion of `L-91333`, the normalized
component-row monotonicity of `L-91322/L-91330`, and the exact parent
target/score/row normalization of `L-91556`  
RH status: **unproved**

## 1. One typed source atom

For a real local quotient `Y>=1`, put

\[
T_\Psi(Y)=4\sqrt Y-3,\qquad
S_\Psi(Y)=5\sqrt Y-3.
\tag{L-91670.1}
\]

Both are strictly positive. For a squarefree source index `n` at physical
endpoint `X`, with `Y=X/n`, define

\[
t_X(n)=\frac1{\sqrt n}T_\Psi(Y),
\qquad
s_X(n)=\frac1{\sqrt n}S_\Psi(Y),
\tag{L-91670.2}
\]

and the literal component-row atom

\[
r_X(n;j)=\frac1{\sqrt n}Q_Y(j),\qquad j\ge2.
\tag{L-91670.3}
\]

The target is the SHARP atom:

\[
t_X(n)=w_\Psi(X,n)
=\frac{4\sqrt X}{n}-\frac3{\sqrt n}.
\tag{L-91670.4}
\]

## 2. Exact single-channel source recursion

Since

\[
w_\Psi(X,n)=3w_{4/3}(X,n),
\tag{L-91670.5}
\]

define the paired positive source state

\[
\boxed{
\mathbf P_j^\Psi(x):=3\mathbf P_j^{(4/3)}(x).
}
\tag{L-91670.6}
\]

The parameter-`a` least-prime recursion gives

\[
\boxed{
\mathbf P_j^\Psi(x)
=
\binom{4\sqrt x-3}{0}
+
\sum_{\substack{k\ge j\\p_k\le x}}
p_k^{-1/2}S\mathbf P_{k+1}^\Psi(x/p_k).
}
\tag{L-91670.7}
\]

Every summand is a positive measure and every squarefree source atom occurs
once. No balanced/reserve channel duplication is present.

Iteration through the finite block through `61` yields the exact labelled
Boolean expansion with parameter `4/3`. All later rough children retain that
same parameter before the one-prime cocycle is applied.

## 3. Exact native row observation

Define the single SHARP normalized row profile

\[
\boxed{
\mathcal H_{\Psi,j}(Y)
=
\frac{Q_Y(j)}{4\sqrt Y-3}
=
\frac13\mathcal Q_{j,4/3}(Y).
}
\tag{L-91670.8}
\]

The normalized component-row theorem proves that
`\mathcal Q_{j,4/3}` is nondecreasing in `Y`; hence the same is true of
`\mathcal H_{\Psi,j}`.

Atomwise,

\[
\boxed{
t_X(n)\mathcal H_{\Psi,j}(X/n)
=
\frac1{\sqrt n}Q_{X/n}(j).
}
\tag{L-91670.9}
\]

After the parity observation, `(-1)^{\omega(n)}=\mu(n)`, the signed row is

\[
\boxed{
\frac{\mu(n)}{\sqrt n}Q_{X/n}(j).
}
\tag{L-91670.10}
\]

Thus the complete fixed-endpoint observation is exactly one copy of

\[
c_X(j)=\sum_{n\le X}\frac{\mu(n)}{\sqrt n}Q_{X/n}(j).
\tag{L-91670.11}
\]

The old factor-three overcount is absent.

## 4. Exact score normalization

The target-per-row-budgeted-score ratio is

\[
q_\Psi(z)=\frac{4z-3}{5z-3},
\qquad z=\sqrt Y\ge1.
\tag{L-91670.12}
\]

Its derivative is

\[
\boxed{
q_\Psi'(z)=\frac3{(5z-3)^2}>0.
}
\tag{L-91670.13}
\]

Consequently every no-upward Hall edge is score-superordinate in the same
orientation as the row profile.

The triple

\[
\boxed{
(T_\Psi,S_\Psi,Q_Y)
=
(4\sqrt Y-3,\ 5\sqrt Y-3,\ Q_Y)
}
\tag{L-91670.14}
\]

is exactly the native parent triple consumed by `L-91556/L-91560`. Therefore no
new target, score, or row scaling is introduced at the one-prime cocycle.

## 5. Hall lift

For a no-upward edge `e<=o`, one has `X/e>=X/o` and hence

\[
\mathcal H_{\Psi,j}(X/e)
-
\mathcal H_{\Psi,j}(X/o)\ge0.
\tag{L-91670.15}
\]

The target Hall transport therefore lifts to every component row, while
(L-91670.13) gives score superordination. Matched edges produce nonnegative
target-null row bonuses; unmatched even masses remain positive source measures.

This statement is stable under finite or countable source-disjoint sums and
under positive endpoint-parameter integration.

## 6. Exact firewall

The following operation is forbidden:

\[
(1+\kappa_*)w_{a_*}\mathcal Q_{a_*}
+
(2-\kappa_*)w_1\mathcal Q_1
\stackrel{\rm false}{=}
\frac1{\sqrt n}Q_Y.
\]

Its left side is three times the right side. The only load-bearing root
normalization in the successor proposal is (L-91670.8)--(L-91670.10).

```text
single SHARP source positivity                    EXACT
least-prime source recursion                      EXACT
source atom nonduplication                        EXACT
target/score/row parent normalization              EXACT
native row observation                            ONE COPY / EXACT
Hall row monotonicity                             RETAINED
balanced/reserve two-row identification            REJECTED
Riemann Hypothesis                                UNPROVED
```
