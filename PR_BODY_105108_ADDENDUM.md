## Checkpoint 9 — Green–Gram selector conditioning

Exact checkpoint base:
cf07de0ba009e8b288eb98b6b4a0ed1d8f12e251.

The boundary-optimal L-105107 selector now has an exact geometric ledger.
Every target value is a conformal-radius factor times an exponentiated
positive Green potential, while all target interaction is the joint
normalized-Szegő-Gram operator

\[
\tau=\|G^{-1/2}D_yG^{1/2}\|_2.
\]

Finite Blaschke target cardinals give the unconditional envelope

\[
\tau\le
\sum_c|\gamma_c|r_\Omega(c)^{d_c-1}
\exp\!\left(\sum_{a\ne c}d_ag_\Omega(c,a)\right).
\]

The bounds are sharp.  The packet also proves three firewalls: identical
Green magnitudes can have different optimal norms because of phase; every
two-target Pick restriction can pass while the full three-target problem
fails; and a fixed smooth disk with fixed total order still has unbounded
collision cost.

Exact replay:

    PASS_T105108_GREEN_GRAM_SELECTOR_CONDITIONING
    15/15 focused tests in normal and optimized Python
    digest 6c2484c4e63612b238f1ec6044c9b8778b725899d4be643d7e80b6a6dc345cdb

Xi manifests, certified rectangle maps, cofinal Green loads/product
separation/joint Gram norms, unweighted quotient bounds, RCMV104530, and RH
remain open.
