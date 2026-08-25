# L-106126 — Physical-squareclass collisions are at most four linear core lines

Claim ID: `L-106126`  
Programme aliases: `LFAM1.FOUR_CORE_LINES`, `LFAM2.KUMMER_COLLISION_LINEARIZATION`, `STRESS.PC2_LINE_GEOMETRY`  
Status: **PROVED EXACT FINITE-FIELD COLLISION LINEARIZATION**  
Created: 2026-08-25  
Depends on: `T-106121`; `L-106001`, `L-106027`; quadratic residue algebra  
Programme issues: #743, #736, #737  
RH status: **not assumed**

Consider one anchor physical-squareclass collision modulo the opposite least
prime `rho`:

\[
 Pc^2\equiv\varepsilon P'c'^2\pmod\rho,
 \qquad
 \varepsilon\in\{+1,-1\},
\tag{L-106126.1}
\]

with all variables units modulo `rho`.  The source has already been split by
the owner quadratic class

\[
 \tau(P)=\kappa_\rho(P).
\]

The squared family moment pairs only atoms in declared class sectors; cross
class recombination is a fixed two-sector operation.

## 1. Positive component

If `P` and `P'` lie in the same owner quadratic class, then

\[
 P'P^{-1}=\xi^2
\]

for some `xi in F_rho^*`.  Equation (L-106126.1) with `epsilon=+1` becomes

\[
 c^2\equiv\xi^2c'^2\pmod\rho.
\]

Hence exactly

\[
\boxed{
 c\equiv \xi c'\pmod\rho
 \quad\text{or}\quad
 c\equiv-\xi c'\pmod\rho.
}
\tag{L-106126.2}
\]

The two lines are disjoint for odd `rho`.

## 2. Negative component

For `epsilon=-1`, solvability requires

\[
 -P'P^{-1}
\]

to be a square modulo `rho`.  Inside one owner quadratic class this is
equivalent to

\[
 \kappa_\rho(-1)=+1,
\]

or

\[
 \rho\equiv1\pmod4.
\]

If `rho` is congruent to `3 mod 4`, the negative collision component is empty.
If `rho` is congruent to `1 mod 4`, choose `iota^2=-1`; then the two negative
lines are

\[
\boxed{
 c\equiv \iota\xi c'\pmod\rho
 \quad\text{or}\quad
 c\equiv-\iota\xi c'\pmod\rho.
}
\tag{L-106126.3}
\]

Thus the complete even-character collision is supported on two lines for
`rho=3 mod 4` and four lines for `rho=1 mod 4`.

## 3. Opposite source side

For

\[
 Qd^2\equiv\pm Q'd'^2\pmod\ell
\]

one obtains identically two or four lines

\[
 d\equiv\zeta d',
 \quad
 d\equiv-\zeta d',
\]

and, when `ell=1 mod 4`, their two `sqrt(-1)` rotations.

## 4. Exact line packets

After fixing owner products and one of the admissible roots, every mixed
physical-squareclass moment is a Hilbert-valued line sum of the form

\[
\boxed{
 \sum_{c'\in\mathcal C'}
 u_{c(c')}\otimes\overline{v_{c'}},
 \qquad
 c(c')\equiv\omega c'\pmod\rho,
}
\tag{L-106126.4}
\]

with at most one declared root `omega` per packet.  The double nonprincipal
channel is the tensor product of one such line modulo `rho` and one line
modulo `ell`.

All Boolean coefficients, roughness conditions, core gcd extraction, physical
shells and marked-prime labels remain attached to the line vectors.

## 5. Scale-matched local consequence

If the relevant core interval has length strictly smaller than `rho`, then one
line in (L-106126.4) is a partial matching: for every `c'` there is at most one
admissible `c`, and conversely.  The same statement holds on the `d` line
when its interval length is smaller than `ell`.

This is a local geometry theorem only.  As `R-106123` emphasizes, a positive
sum over power-many conductor fibres is a separate global theorem.

## 6. Correct analytic target

The global mixed/double gates of `T-106121` may be attacked as coherent sums of
these source-faithful line packets.  A successful estimate must exploit at
least one of:

```text
cancellation along each incomplete core line;
large-sieve orthogonality across varying roots and conductors;
trace-sheaf monodromy of the Kummer line family;
principal/nonprincipal recombination before conductor fibres are squared.
```

## Scope

The lemma proves the exact two/four-line decomposition and the local
partial-matching criterion.  It does not prove any global tensor moment,
`BCI102990`, or RH.
