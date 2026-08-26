# R-106122 — Owner-only product collisions do not survive varying core characters

Claim ID: `R-106122`  
Programme aliases: `LFAM1.TENSOR_SQUARECLASS_FIREWALL`, `LFAM2.KUMMER_CORE_OWNER_COUPLING`, `STRESS.BILATERAL_COLLISION_SELF_AUDIT`  
Status: **PROVED EXACT CHARACTER-KERNEL FIREWALL; THE GLOBAL COLLISION CLAIMS OF THE FIRST `L-106122` AND `L-106125` ARE RETRACTED**  
Created: 2026-08-25  
Depends on: `L-106120--L-106122`; `R-106080`; `L-106001`, `L-106020`  
Programme issues: #743, #736, #737  
RH status: **unproved**

The bilateral tensor identity of `L-106120` is correct.  The first global
collision interpretation in `L-106122` omitted the character carried by the
varying reduced core.

## 1. Exact character seen by one source side

On the anchor side, a root character `psi` modulo `rho` appears as

\[
 \psi(P)\theta(c),
 \qquad
 \theta=\psi^2.
\]

Therefore

\[
\boxed{
 \psi(P)\theta(c)=\psi(Pc^2).
}
\tag{R-106122.1}
\]

Similarly, on the opposite side,

\[
\boxed{
 \chi(Q)\eta(d)=\chi(Qd^2).
}
\tag{R-106122.2}
\]

The core labels cannot be absorbed into character-independent coefficients
when `c` or `d` varies before the family square.

## 2. Correct global orthogonality

For two complete anchor atoms `(P,c)` and `(P',c')`, full character
orthogonality gives

\[
\boxed{
 Pc^2\equiv P'c'^2\pmod\rho.
}
\tag{R-106122.3}
\]

The even-character quotient gives the union

\[
\boxed{
 Pc^2\equiv\pm P'c'^2\pmod\rho.
}
\tag{R-106122.4}
\]

The opposite side similarly gives

\[
\boxed{
 Qd^2\equiv\pm Q'd'^2\pmod\ell.
}
\tag{R-106122.5}
\]

Thus the nonprincipal--nonprincipal channel is a double **physical
squareclass** collision variety, not an owner-product-only collision variety.

## 3. What the owner Wick identity still proves

For one fixed core `c`, the equal-pair owner sum factors exactly as

\[
 {1\over2}
 \left[
  \mathcal P_{\psi,c}^2-\mathcal D_{\psi,c}
 \right].
\]

This remains useful.  But when the square is expanded between two different
cores `c,c'`, the correct congruence is

\[
 p_1p_2c^2\equiv\pm p_3p_4c'^2\pmod\rho,
\tag{R-106122.6}
\]

not

\[
 p_1p_2\equiv\pm p_3p_4\pmod\rho.
\]

The latter follows only after fixing the core residue ratio or setting
`c=c'`.

## 4. Exact finite mismatch

Choose units `P,P',c,c'` modulo `rho` with

\[
 Pc^2\equiv P'c'^2\pmod\rho
\]

but `P` not congruent to `P'`.  Such fixtures exist whenever
`c/c'` is not `+/-1`; for example modulo `5`,

\[
 P=1,
 \quad c=1,
 \quad P'=4,
 \quad c'=2,
\]

gives

\[
 Pc^2\equiv1,
 \qquad
 P'c'^2\equiv4\cdot4\equiv1\pmod5,
\]

while `P` and `P'` are distinct.  The physical-squareclass kernel is positive
on this pair and the owner-only kernel is not.

## 5. Consequence for the large-conductor claim

The first `L-106125` used `rho>4A`, where `P,P'~A`, to force `P=P'`.  The
actual difference is

\[
 Pc^2-P'c'^2,
\]

whose size is governed by the physical squareclass scale, not by `A`.  Hence
`rho>4A` does not force equality when `c` varies.  The global mixed/double
nonprincipal closure claimed there is retracted.

A fixed-core version remains true: if `c=c'` and `rho>4A`, the owner products
must agree.  That fibrewise fact is already covered by `L-106124` and does not
pay the varying-core family.

## 6. Binding status

```text
L-106120 bilateral source/tensor identity                RETAINED
L-106121 source-dual moment and atomic diagonal          RETAINED
L-106112 owner Wick factorization at fixed core          RETAINED
first L-106122 owner-only global collision variety       RETRACTED
first L-106125 global large-conductor closure            RETRACTED
L-106124 fixed-core local large sieve                    RETAINED
L-106130 function-field complete owner shell             RETAINED LOCALLY
```

The corrected tensor frontier is `T-106121`.  Its nonprincipal collision
varieties retain the complete physical squareclasses `Pc^2` and `Qd^2`.

## Meaning

The bilateral family has repaired the source order, but it has not separated
owner and core arithmetic.  Their coupling is exactly the Kummer map

\[
 (P,c)\longmapsto Pc^2.
\]

Any trace formula, large sieve, or function-field sheaf must act on that map
rather than on the owner product alone.
