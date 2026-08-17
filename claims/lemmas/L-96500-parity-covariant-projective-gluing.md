# L-96500 - Projective gluing is valid only after the terminal realization is made parity-covariant

Claim ID: `L-96500`
Status: **PROVED EXACT ABSTRACT GLUING THEOREM**
Created: 2026-08-17
Supersedes the parity-blind use of `L-94120` in PR #550
RH status: **unproved**

Let `S(E,O)=(O,E)` on positive paired sources and let

\[
\mathcal O(E,O)=R(E)-R(O)
\]

be signed physical observation. Then

\[
\boxed{\mathcal O(S^mP)=(-1)^m\mathcal O(P).}
\tag{L-96500.1}
\]

Consider a finite or finitely terminating labelled source tree. Each node `v`
has an ordered rough-prime history `h(v)`, cumulative parity

\[
\varepsilon(v)=(-1)^{|h(v)|},
\]

and a terminal local signed datum `K_v` written in canonical local parity. The
actual root-oriented terminal datum is therefore `epsilon(v) K_v`.

Assume the source identity is a direct sum with one owner per atom and that
recursive coefficients are nonnegative. Then replacing each terminal node by a
positive physical row preserves the root marginal **if and only if** the row
installed at `v` realizes

\[
\boxed{\varepsilon(v)K_v,}
\tag{L-96500.2}
\]

not merely `K_v`.

In particular, a terminal map proved only for canonical even orientation may be
used on all leaves only when every stopped history has even length, or when a
second positive realization for the reversed datum `-K_v` has been proved.
Recording parity in a label without using it in the terminal realization does
not satisfy the theorem.

The proof is finite induction. Apply signed observation to every direct-sum
identity. Equation (L-96500.1) supplies the path sign. One-use ownership and
nonnegative recursive coefficients permit substitution exactly when every
terminal marginal equals (L-96500.2). Conversely, if one terminal replacement
has the wrong sign, apply a coordinate functional separating the two terminal
marginals; the root equality changes by twice that terminal coordinate.

```text
source ownership                         exact
coefficient magnitudes                   exact
history parity cocycle                   exact
terminal sign requirement                necessary and sufficient
parity-blind terminal substitution       invalid in general
Riemann Hypothesis                       unproved
```
