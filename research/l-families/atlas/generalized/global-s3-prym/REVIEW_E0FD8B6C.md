# Independent review of the polarized Jacobian and source torsion graph

Scientific checkpoint: `e0fd8b6cba1b3db8c463a843314f6061e5db29d8`.

Scope: the seven new files in `global-s3-prym`: `POLARIZED_JACOBIAN_AND_THREE_TORSION.md`, `TORSION_DIVISOR_REPLAY.md`, `torsion_replay.py`, its source/artifact/provenance JSON files, and `test_torsion_replay.py`. The primitive curve and degree-three-map source remains frozen at `567ae7aec00f6ee6d3e01bdde2004e76fec8ff6f`.

## Finding

No unresolved mathematical or implementation blocker was found. The packet proves the polarized degree-nine isogeny and the graph anti-isometry from the actual curve maps, then constructs its finite torsion graph through divisor pullbacks. Equality of L-polynomials or a fitted torsion correspondence is not substituted for that construction.

## Independent proof review

I read the complete proof and checked the integral orthogonality argument. On the actual S3 closure, the pullback of the first map is the difference of two root maps, and the pullback of the second lies in the sign quotient. The three-cycle sum `N=1+r+r^2` kills the first and acts by three on the second. Since `N` is self-adjoint for the canonical Jacobian polarization, the cross norm is killed by six. Torsion-freeness of Hom groups then gives its vanishing, including in positive characteristic. This avoids the invalid inference that a zero differential alone makes an abelian-variety homomorphism zero.

The diagonal norm identities are multiplication by three. Consequently `Phi^dagger Phi=[3]` on the product, the isogeny degree is nine, and its kernel is etale because the characteristic is neither two nor three. The pullback polarization is three times the product polarization.

I also checked the individual pullback injectivity argument. A nontrivial kernel line bundle of order three would yield a connected etale cyclic degree-three cover of the elliptic target. Triviality after pullback would lift the genus-two source to that genus-one cover with degree one, a contradiction. The kernel of the product map therefore projects isomorphically to both elliptic three-torsion schemes. Its maximal isotropy gives the stated Weil-pairing reversal. The argument is over the algebraic closure where needed and descends as a group-scheme statement; it does not assume rationality of all torsion points.

The differential identities and the resulting mod-three Frobenius-polynomial congruence are consistent with these stronger correspondence statements. They do not assert that the two elliptic curves are mutually isogenous, or that the genus-two Jacobian is their product as a principally polarized variety.

## Independent implementation review

I read the complete exact polynomial, elliptic, and Mumford/Cantor arithmetic, all fifteen tests, the primitive source specification, and the acceptance/binding logic. The geometric dependencies are authenticated before executable import. The fields are bounded by 2401 and polynomial operations by degree twelve.

The Cantor composition uses the correct Bezout combination and the `v1*v2+h` term for the actual source equation `w^2=h(x)`. The degree-five polynomial is not rescaled to a different quadratic twist. Divisibility and exact division are checked before reduction, and reduced output is checked again against the curve.

The first map's origin correction is essential and is present. Reducing its cubic fibre initially subtracts three infinity points, whereas the actual origin pullback is the two points above `g=0` plus infinity. The code subtracts the nonzero two-torsion class `(monic(g),0)`. A dedicated hostile control shows that omission leaves the wrong three-multiple. The second map has origin pullback three times infinity and needs no such correction. The explicit short-model change for the second elliptic curve is inverted before taking its source fibre.

Each field is searched completely for roots of the elliptic three-division polynomial, and every resulting point is checked by group addition. The two nine-point sets are pulled back before all 81 pairs are tested for the kernel. Acceptance checks bijectivity, group addition, Frobenius action, and all pairing reversals. The tangent-line pairing includes the indispensable minus sign. The smaller F5 control enumerates all 54 reduced Jacobian classes, compares their number with the frozen curve polynomial, and checks all pairwise closure/commutativity and inverses, along with further associativity and tangent-doubling controls. No full Jacobian census over F25 or F2401 is claimed.

During review I requested that the public pullback helpers reject off-curve or coercible coordinates even though the pinned producer supplies valid points. The frozen code and fifteenth test implement this hardening. It did not change the theorem or the previously reconstructed graph.

## Primary-source and novelty boundary

I independently checked the displayed Cantor algorithm in Damien Robert's author notes, Algorithm 2.1, PDF page 42: <https://www.normalesup.org/~robert/pro/publications/notes/notes_av.pdf>. I also checked the normalized pairing formula and its sign in A. Enge, *Bilinear pairings on elliptic curves*, printed page 219, equation (8): <https://ems.press/content/serial-article-files/44297?nt=1>. Milne's polarization descent and the Stacks Kummer construction support the abstract steps cited by the proof.

General gluing along an anti-isometry and genus-two triple covers are classical. For an explicit primary discussion, see Bröker--Howe--Lauter--Stevenhagen, section 5 and Appendix A: <https://arxiv.org/pdf/1403.6911>. The packet's contribution within this programme is the specified S3 source, its integral correspondence proof, and the checked source-divisor graph. No external novelty or arithmetic RH conclusion is established here.

## Execution evidence

I did not run the producer or tests. The coordinating agent reports Ruff, complete write/check, optimized check, fifteen ordinary tests and fifteen optimized tests all passing, followed by the final documentation rebind and checks. The frozen provenance records proof hash `ed32212bd6fe5024bac35931bdab8849ee30821b26bdfee716916e37d2a4ae63` and artifact hash `0eeddf580e8e69e9b465659224046c6558886a4f13e3096c3002712b62c3e7fb`. These reported executions and recorded hashes are distinct from my independent proof, source and code reading.
