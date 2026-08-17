# The accumulated-parity firewall for grouped and scalar factor-67 source chains

**Status:** unconditional correction and sharp producer reduction.  
**Base:** PR #561 at `db9bdc63c855c6ddf664b763d748f8155a6a2c67`.  
**Riemann Hypothesis:** unproved.

## 1. What survives from the paired factor-67 program

Three predecessor ideas are individually useful:

1. PR #555 supplies the exact least-owner factor-67 source recursion and finite
   scale descent.
2. PR #556 correctly insists that the signed `d|P_61` colors are not positive
   objects individually; the complete annular family must be grouped before
   observation.
3. PR #559 identifies the scalar `R_X=5c_X(2)+3c_X(3)` whose reciprocal-zeta
   numerator is zero-free in the required half-plane.

PR #561 adds the missing interface datum: a rough history of length `m` changes
signed observation by `(-1)^m`. The present packet composes all four facts
without discarding that sign.

## 2. Grouping does not erase accumulated parity

Write a parity-labelled source as `(E,O)` and let `S(E,O)=(O,E)`. Any signed
row observation has the form

\[
O_j(E,O)=L_j(E)-L_j(O),
\]

so `O_j S=-O_j`. Complete finite-color grouping acts in the same way on both
parity coordinates and commutes with `S`. Consequently

\[
O_j G S^m=(-1)^m O_j G.
\]

The same identity holds for every scalar linear combination of rows, in
particular

\[
R S^m=(-1)^m R,
\qquad R=5O_2+3O_3.
\]

Thus grouping cures the colorwise-positivity mistake, and scalarization cures a
Mellin numerator-cancellation issue, but neither cures history parity.

## 3. Why squaring the recursion at a fixed depth fails

PR #561 proves that the current block after truncating all rough histories at a
fixed depth `L` satisfies

\[
B_{L,X}(q)/\sqrt X
=a_q(-1)^{L-1}(\log\log X)^{L-1}/(L-1)!+
O((\log\log X)^{L-2}),
\qquad a_q>0.
\]

At even `L`, the recursive frontier has canonical parity but the current block
is eventually negative. At odd `L`, the current leading term is positive but
the frontier parity is reversed. Because grouping and scalarization preserve
the parity character, this dichotomy survives both operations.

At the first even depth, PR #561's directed enclosures imply

\[
5B_{2,200000}(2)+3B_{2,200000}(3)
<-62.7181678185658877324.
\]

Hence the two-level “parity-squared” proposal is not a valid positive
decomposition, even after complete annular grouping or `5:3` scalarization.

## 4. The surviving scalar consumer

Let `z=s+1/2`, `x=2^{-z}`, and `y=3^{-z}`. The two fixed-row numerators are

\[
P_2=2x-1-y,
\qquad
3P_3=5y-x-1-3x^2.
\]

Therefore

\[
5P_2+3P_3=-3(x-1)(x-2)
=-3(1-x)(2-x).
\]

For `Re z>0`, `|x|<1`, so this numerator cannot vanish. Thus eventual or global
nonnegativity of

\[
R_X=5c_X(2)+3c_X(3)
\]

is by itself sufficient for the fixed-row Mellin–Landau implication to RH.

## 5. Exact remaining producer

The only surviving factor-67 target is global in rough depth:

> Expand the complete parity-labelled native source with exact least-owner
> ownership; keep every finite color grouped; sum all rough histories before
> signed observation; and produce one positive common-source packing whose
> scalar observation is exactly `R_X`.

This statement is called `ASHP67`. If `ASHP67` holds for all `X`, then `R_X>=0`
for all `X`, the zero-safe scalar Mellin transform excludes zeta zeros to the
right of the critical line, and the functional equation gives RH.

`ASHP67` is open. Any valid proof must justify an all-depth finite
representation, an Abel/projective limiting argument, or a full scalar-cone
dual certificate. Fixed-depth, leafwise, and individual-color arguments are
now formally excluded.

## 6. Conclusion

The paired factor-67 chain has been hardened to one honest boundary:

\[
\boxed{\mathrm{ASHP67}\Longrightarrow R_X\ge0\Longrightarrow RH.}
\]

The implication is exact; the producer remains unproved. This packet therefore
advances the architecture by eliminating three false salvage routes and
compressing the surviving RH-bearing obligation to one scalar all-depth Hall
problem.
