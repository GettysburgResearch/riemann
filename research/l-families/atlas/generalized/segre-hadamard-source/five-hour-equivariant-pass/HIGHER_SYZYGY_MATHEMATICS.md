# The complete first Q-syzygy and the nonformality obstruction

Status: proved for the ternary-cube source by the complete46-weight calculation and the frozen actual d2.

Let C=K(W;R), with its commuting Q multiplication, and put B=H(C). Filtering the total complex K(Q;C) by Q-Koszul degree gives the change-of-rings spectral sequence used by the actual d2 packet. At internal degree4,

    E2_(2,1)=ker(Lambda^2 Q tensor B_(1,2) -> Q tensor B_(1,3)),

because B_(1,1)=0. The displayed map is the ordinary Q-Koszul differential induced on B. Thus its complete kernel, rather than just the three d2 target weights, is an intrinsic source for the higher operation.

For a factor permutation g, the trace on an exterior square is

    tr(g | Lambda^2 Q)=(tr(g|Q)^2-tr(g^2|Q))/2.

The frozen character of Q=B_(0,1) is (17,-1,-7), and B_(1,2) has character (20,0,-10). Hence Lambda^2Q has character (136,-8,28), and the source has character (2720,0,-280). The target Q tensor B_(1,3), using the frozen character (65,-25,35), has character (1105,25,-245).

The complete source calculation does prove surjectivity in all46 weights. Its kernel has dimension1615; direct factor-permutation actions on the exact kernel bases give character (1615,-25,-35), independently matching the character quotient above. The accepted actual d2 is equivariant and surjects from this kernel onto B_(2,4), whose character is (65,-25,35). Its E3 kernel therefore has character (1550,0,-70). Solving the S3 character equations gives multiplicities235,235,540 for trivial, sign and standard.

Finally, suppose there were a Sym(Q)-linear formality equivalence C -> H(C) compatible with this filtration and inducing the accepted homology identification. Applying the functorial Q-Koszul construction would identify the filtered total object with K(Q;B), whose differential has no hidden component producing the displayed source-chain d2. Its spectral sequence would degenerate at E2. The accepted nonzero d2 contradicts this. Thus the ternary-cube W-Koszul dg module is not formal in this filtered Sym(Q)-linear sense. This statement is relative to the declared Q quotient and does not canonize the marked rational lifts used to exhibit d2.

The chain formula also defines an intrinsic secondary Q operation. For a contraction that chooses representatives c and homotopies h(qc), its value on a Q-Koszul cycle z is the B_(2,4) class of delta h(delta z). Replacing representatives or homotopies changes this formula by the usual source and target indeterminacies, so the induced map on E2 is the canonical spectral-sequence transgression. The source calculation proves that this operation is onto B_(2,4). Individual marked formulas are gauge-dependent; the induced operation, its rank and its factor character are not. We call this a secondary Q operation rather than identifying it with a particular convention for a minimal A-infinity module operation.
