# Early closeout: equivariant source pass

Status: reviewed checkpoint, closed early at the user's request on
2026-09-01.  RH and GRH remain unproved.

The pass kept PR #782 at
`552fe0b78fd96b02fe5836269e6795a992c935be` as a frozen synthesis
dependency and worked only on the actual ternary-cube source of PR #769.
Its purpose was to replace character identities by chain maps.

## Proved results

1. **Complementary quotient action.**  For
   (Q=R_1/W), the actual multiplication map
   [
   Qotimes B_{1,2}longrightarrow B_{1,3}
   ]
   has rank (65) and is surjective.  The complete computation is
   equivariant and not a dimension fit.

2. **The first actual change-of-rings differential.**  The three complete
   target blocks have ranks (1,4,6).  Globally the resulting (d_2) has
   rank (65) and surjects onto (B_{2,4}).  Hence this source does not
   degenerate at (E_2).

3. **Complete first (Q)-syzygy.**  Across all 46 weights,
   [
   Lambda^2Qotimes B_{1,2}longrightarrow Qotimes B_{1,3}
   ]
   is surjective of rank (1105).  Its kernel has character
   ((1615,-25,-35)).  After the actual (d_2), the surviving character is
   [
   (1550,0,-70)
    =235,mathbf 1+235,mathrm {sgn}+540,mathrm {std}.
   ]
   This proves a filtered (operatorname {Sym}(Q))-linear nonformality
   obstruction and defines a canonical secondary spectral-sequence
   operation.  It is not identified with a particular minimal
   (A_infty) convention.

Frozen commits for these three results are respectively
`c7ea79747`, `6cacc948f`, and `2c65d7ba3`.

## Exact frontier

The first possible (d_3) was not acquired.  Its unrestricted weight-744
target has chain dimensions
[
 (180,763,1143,730,178,9),
]
so it was refused by the registered 512-dimensional cap.  A separately
registered sign-isotypic complex reduced these dimensions to
((27,110,150,76,8,0)), passed complete shape and chain tests, but its
full acquisition timed out at 240 seconds after an earlier call-site failure
had been repaired.  No verification artifact exists.  There is no (d_3)
rank, zero/nonzero, source-dimension, or global differential claim.

This is useful information: the sign factor is a complete bounded route to
the one-dimensional ([744]) target, but the next pass must optimize the
second-lift combination rather than raise memory or infer a result from the
timeout.  The remaining ([555]) determinant constituent must be registered
separately.

## Interpretation and limits

The pass supplies an honest chain-level bridge between the Segre cofactor
language and a nontrivial higher source operation.  It does not construct an
automorphic object, a Frobenius action, an archimedean completion, a positive
polarization, or a purity theorem.  An alternating Tor character remains
distinct from a superdeterminant, and none of these finite syzygy results
implies RH or GRH.

The highest-value continuation is:

1. stream the sign-isotypic second lifts and decide the registered (d_3)
   constituent;
2. formulate the resulting secondary/tertiary operations directly in Schur
   functor language and compare them with PR #782's cofactor complex;
3. only then register the complementary ([555]) constituent and a
   representation-valued strand theorem.
