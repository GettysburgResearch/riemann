# TSR26 — A complete all-rank rational spectral classification

**Status: proposed complete component proofs, with an exact finite torsion
classification; independent mathematical review pending.** This is a new research
contribution, not a Reviewer D acceptance verdict. RH and GRH remain unproved.

## Main result

For EVERY r>=1, every positive rational q and all rational raw traces A,B,C,
the correctly scaled full-factor equality

    P_(Std(A) tensor Sym^r(B))(q^(r/2)T)=P_(Sym^(2r+1)(C))(T)

holds exactly on the two known Dickson graph loci with their correct central
signs, plus ONE additional family:

    r == 3 (mod4), A=0, B^2=C^2=2q.

The positive square root of q is fixed. Full characteristic polynomials and all
multiplicities are compared; a few matching coefficients do not suffice.
No Hasse bound or actual elliptic-curve realization is assumed.

For integral traces and positive odd integer q, the additional family is impossible.
Thus the prior rank-two and rank-three converses extend to ALL ranks. The old
unretained rank-four scout is not authenticated retroactively; a new proof settles
its rational/noncyclotomic question without using it.

Recognition now needs one 2-by-2 matrix power, graph equalities, and the exceptional
predicate: O(log(r+2)) exact rational arithmetic operations, rather than expanding
the degree-(2r+2) factors. This is not a bit-complexity claim.

## The short generic argument

Two adjacent tensor eigenvalues differ by v^2. Because both belong to the target
spectrum, v^2=w^(2d). Hence v=sign*w^d and u=sign^r*w^a. When w is not a root of
unity, equality becomes equality of integer weight multisets. The existing
maximum-weight argument gives exactly the two graph families.

If a nongraph solution exists at any complex traces, w has finite order at most
(2r+1)(2r+2). Thus every reduced positive-dimensional component is a graph curve;
there are no isolated noncyclotomic points either. Scheme multiplicities and the
complete arbitrary-complex torsion order list are not asserted.

Rational raw traces reduce the torsion case to four fixed square classes. The
resulting residue counts are affine along r=r0+24k. An exact 4320-row classification
solves for ALL k>=0; it is not extrapolation from a finite rank ladder.

## Why this matters beyond another coefficient formula

The new theorem eliminates rank-by-rank high-degree elimination for the full
rational intersection. It also resolves the missing square-class-two exception:
q=2,r=3,A=0,B=C=2 has common factor (1+2^14 T^4)^2 and is not on the two graphs.

A separate precise obstruction shows that such local identities cannot hold on
a Zariski-dense set of a reductive joint monodromy group when the target's
connected image contains SL2. Squaring eigenvalues handles odd-rank half-power
normalizations without inventing a global half-Tate character. Abelian/CM-type
realization is not ruled out or constructed.

## Read and replay

[PROOF.md](PROOF.md) supplies the generic proof, all-rank torsion reduction, full
classification, characteristic-two corollary and monodromy obstruction.
[CLAIMS.tsv](CLAIMS.tsv) separates the exact scopes. [SOURCES.json](SOURCES.json)
credits and pins the predecessor. [VALIDATION.md](VALIDATION.md) records execution.

Run `python -I -S verify.py` and `python -I -S -O verify.py` in this directory.
The checker uses Python integers and fractions only. No root is approximated and no curve or finite field is enumerated. A separate
3,000-point rational trace-box regression has explicit fixed bounds; it is not
the classification proof. The finite torsion
proof depends on the separately supplied all-rank affine-count lemma.
No Lean/CI/independent referee acceptance or external novelty claim is made.
