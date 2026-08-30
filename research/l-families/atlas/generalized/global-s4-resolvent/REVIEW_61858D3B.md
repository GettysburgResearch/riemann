# Independent review: S4 sign-sector polarized elliptic splitting

Reviewed scientific commit: `61858d3bd8a18365404c7bfd7b8bfac58a529cc1`.

I independently read the full proof, producer and 14 tests. I did not execute computational jobs. Root reports Ruff, generation, ordinary/optimized producer checks, and 14 tests in each mode passing after final bindings.

Both degree-two elliptic maps and their Weierstrass transformations are correct. The minus quotient must use the quartic point (0,0) as origin; the producer and proof do so. On the genus-two source, the two origin pullbacks are the degree-two divisors at zero and infinity, whose difference is div(u). This handles nonsplit individual points without assuming rational source origins.

The involution eigenspaces give integral cross-norm vanishing; together with the diagonal norm-pullback maps this proves the degree-four polarized isogeny. The injectivity argument via an etale double-cover lift is valid. The common cubic roots explicitly identify the three nonzero two-torsion pairs, and the origin-divisor equality identifies their source pullbacks. The four resulting kernel elements exhaust the kernel. At order two the inverse Weil pairing equals the pairing, so the graph is the required maximal isotropic anti-isometry. This establishes source geometry and polarization, not merely matching Frobenius traces.

The j=0 factor and its forced polynomial `1+QT^2` when Q is 2 modulo 3 follow from the displayed quotient and the cube bijection. The result is classical even-sextic and elliptic geometry, appropriately identified as such in the note.

The exact code uses the generalized Weierstrass group law with its quadratic coefficient, validates source and target points, checks every rational affine source point under both maps, and handles zero and infinity explicitly. Elliptic polynomials are reconstructed from two independent counts and checked against further counts and the frozen genus-two factor. Torsion points are constructed from common cubic roots before the group and Frobenius comparisons. The declared pairing formula is used only on the already verified complete two-torsion groups.

The tests include a complete small F5 group check, direct prime-field map identities, off-curve and coercible-input refusal, nonsplit origin/infinity controls, and three distinct arithmetic Frobenius patterns on nonzero two-torsion. No complete genus-two Jacobian enumeration or general even-sextic divisor-addition algorithm is claimed. I found no remaining blocking mathematical or implementation defect.
