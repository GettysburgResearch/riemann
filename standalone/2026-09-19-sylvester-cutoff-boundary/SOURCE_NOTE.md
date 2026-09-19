# Source mechanism and transfer firewall

Reference: Ashay A. Burungale and Ye Tian, *A proof of Sylvester's conjecture*, arXiv:2609.14893v2, 15 Sep 2026.

## Mechanism used in the paper

For (pequiv8pmod9), the authors choose an auxiliary (qequiv4pmod9) satisfying a nontrivial cubic-residue condition. The same condition:
- makes a complementary central L-value nonzero via 3-isogeny descent and a rank-zero converse;
- makes Frobenius act nontrivially on the first division point.

The natural conductor-(p) Hecke trace vanishes. They choose a (lambda=1-omega) division first, then trace the divisions. The result lies in (E[lambda]) and is proved nonzero by reduction/Frobenius.

On the 3-primary quotient, the norm and cubic projector are congruent mod (lambda), so
[
D=(N-Pi)/lambda
]
is integral. If the cubic component vanished, the integral identity would force a known nondivisible torsion point to acquire a forbidden (lambda)-division. Hence the cubic component is nonzero; a local argument upgrades it to non-torsion; Gross--Zagier gives nonzero central derivative.

## What transfers

- preserve arithmetic information before a lossy projection;
- auxiliary choices should solve both the main and complementary obstruction;
- seek exact integral identities rather than approximate projector comparisons;
- source-specific local/arithmetic data must do the work;
- keep a sharp distinction between nonvanishing and norm/size control.

## What does not transfer literally

- scalar division in a complex Hilbert space has no finite kernel, so 'divide before trace' is trivial there;
- the Möbius cutoff residual is not a Tate cohomology class;
- the paper proves nonvanishing; #848 needs an upper bound;
- central rank-one information in an elliptic family is not information about all zeta zeros.

This packet therefore uses the paper as proof-design guidance and as an L-family fixture, not as a theorem imported into the RH chain.
