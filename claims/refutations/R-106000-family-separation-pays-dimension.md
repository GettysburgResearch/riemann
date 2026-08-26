# R-106000 — Exact family separation without hybrid cancellation pays the family dimension

Claim ID: `R-106000`  
Programme aliases: `LFAM1.UNIFORM_AVERAGE_DIMENSION_BARRIER`, `LFAM2.SEPARATION_IS_NOT_CANCELLATION`  
Status: **PROVED EXACT METHOD FIREWALL**  
Created: 2026-08-24  
Depends on: `L-106001--L-106003`; PR #719 `R-102867`  
RH status: **not assumed**

This refutation separates three statements that must not be conflated:

```text
character orthogonality;
exact squareclass separation;
a subpower principal-member estimate.
```

The first two do not automatically give the third.

## 1. Quadratic-only families erase the core

For a quadratic character and a unit `c`,

\[
\chi(Pc^2)=\chi(P).
\]

Thus a quadratic-only family cannot see the stopped-Vaughan square core.
PR #719 `R-102867` further proves that the naive product of the four owner
Legendre symbols collapses to a residue-class sign by reciprocity.

The full family in `L-106002` avoids this exact failure because all but two
characters have `chi^2` nontrivial.

## 2. Dimension cost of exact owner separation

Let `H` be a finite-dimensional Hilbert space and let

\[
v_1,\ldots,v_K\in H
\]

be nonzero pairwise orthogonal feature vectors representing `K` active owner
squareclasses. Then

\[
\boxed{\dim H\ge K.}
\tag{R-106000.1}
\]

For a uniform family of `H` characters, exact orthogonality has the form

\[
\sum_{\chi\in\mathcal F}
\left|\sum_{j=1}^K a_j v_j(\chi)\right|^2
=
H\sum_{j=1}^K |a_j|^2\|v_j\|_{\rm norm}^2.
\tag{R-106000.2}
\]

The principal character is one coordinate, so positivity alone gives

\[
\boxed{
|F_{\chi_0}|^2
\le
H\sum_j |a_j|^2\|v_j\|_{\rm norm}^2.
}
\tag{R-106000.3}
\]

If exact separation requires `K=X^{delta+o(1)}` independent owner labels, then
`H>=K` and (R-106000.3) pays a power-sized factor. Exact diagonalization is
not, by itself, a subpower principal extraction.

For a character family modulo `M`, `H` is at most the number of available
characters and in the complete uniform family equals `phi(M)`. Therefore a
claim that a large modulus makes every physical product distinct must also pay
the resulting family dimension.

## 3. Collision density is not cancellation

The congruence

\[
Pc^2\equiv Qd^2\pmod\ell
\]

has density roughly `1/ell` in an unstructured box. Multiplying this density by
the principal extraction cost `ell-1` produces no saving.

The loss is sharp. Choose coefficients supported entirely on one surviving
line

\[
c\equiv\tau d\pmod\ell
\]

with a phase that is constant there. Then every term in that line contributes
with the same sign, and the complete character moment attains the congruence
occupancy bound.

Thus neither of the following is valid:

```text
few congruence collisions -> principal member is small;
nonsquare elimination of some owner pairs -> the surviving family moment is
subpower.
```

A new cancellation theorem is still required on the square-ratio lines.

## 4. What is not refuted

This theorem does not rule out:

- nonquadratic core oscillation;
- a nonuniform positive amplifier;
- a trace formula with an arithmetic off-diagonal saving;
- a family moment theorem exploiting the inherited additive phases;
- a function-field purity/monodromy theorem;
- a family whose principal leverage remains subpower without exact owner
  separation.

Those are precisely the live options in `T-106000`.

## 5. Binding review rule

Reject a proposed CV/XD family closure if it:

```text
uses only quadratic characters;
quotes orthogonality but omits the principal extraction factor;
chooses a modulus large enough to diagonalize the packet but does not pay the
family cardinality;
replaces a collision-line sum by its density without proving cancellation;
treats a function-field memberwise theorem as a number-field theorem.
```
