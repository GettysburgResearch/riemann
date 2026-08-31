# A source formula for the first higher change-of-rings differential

Status: the complete three-weight source calculation passed. The actual higher differential has rank65 and is surjective onto B_(2,4).

Use R, W, Q and B from the first action packet, frozen at c7ea79747208dfa6e164cb87c2e4f9ee523cbb3d. The complement Q=(1-e_sym)R_1 is GL3 times S3 stable and canonically identifies with R_1/W. The chosen rational cycle representatives and boundary lifts are marked choices; the induced spectral-sequence differential is natural and equivariant. In the double complex Lambda^p Q tensor K_q(W;R), let delta remove a Q wedge factor and multiply R, and let d be the W-Koszul differential. These commute before totalization. Fix total differential D=d+(-1)^q delta.

Take z in the kernel of delta: Lambda^2 Q tensor B_(1,2) -> Q tensor B_(1,3), and replace each B_(1,2) class by its accepted source cycle. Since B_(1,1)=0, there are no incoming Q boundaries in this internal degree. Thus z represents an actual E2_(2,1),internal4 class.

For each multiplication, the first packet supplies

    q_i c_a = sum_b M_i(b,a)c_b + d eta_(i,a).

On q_i wedge q_j tensor c_a, delta is q_j tensor q_i c_a minus q_i tensor q_j c_a. Therefore the homology terms cancel for z and the explicitly assembled eta_z satisfies d eta_z=delta z. Its bidegree is (p,q)=(1,2). The total differential of z+eta_z is delta eta_z. This is W-closed because d delta eta_z=delta d eta_z=delta^2 z=0. Its W-homology class is precisely d2[z], with this totalization convention.

Changing a boundary lift changes delta eta_z by the standard spectral-sequence indeterminacy. Here the target is B_(2,4) itself, since B_(2,3)=0. The accepted explicit lifts therefore give legitimate representatives without a choice-dependent image rank. No ambient Betti table is used to construct or identify the map.

## Why three complete weight blocks suffice for surjectivity

The accepted character theorem gives

    B_(2,4)=[552] tensor (1+standard)
             +[642] tensor sign+[543] tensor sign.

All operations defining d2 are GL3 times S3 equivariant. In characteristic zero its image and cokernel are semisimple finite-dimensional representations. If the cokernel were nonzero, some irreducible GL3 constituent would have highest weight 552,642 or543. Its highest-weight vector gives a nonzero cokernel at that weight. Consequently full surjectivity in those three complete weight spaces proves full surjectivity. If it is verified, the higher differential has rank65 and the change-of-rings spectral sequence does not degenerate at E2.

This implication uses both a complete source calculation in each selected weight and the imported complete target character. Three sampled vectors or three matrix entries would not suffice. A rank deficiency in one block must be reported literally and is not repaired by an Euler-character identity.

## Independent checks

The degree4 W-Koszul source is generated directly from the original coefficient-one orbit sums, within each fixed weight. Kernel and boundary dimensions are calculated over Q. Their quotient is matched with the frozen B_(2,4) character at that weight. Each proposed d2 vector is verified in the original chain coordinates before quotient reduction; full action identities and factor permutations provide additional independent checks. The owned replay note will report which rank statements actually passed.

## Accepted source calculation and consequence

The initial full acquisition on 2026-09-01 gave complete image dimensions1,4,6 at weights642,552,543, respectively. These equal the complete target dimensions. Their identity/transposition/three-cycle traces are respectively (1,-1,1), (4,0,1), and (6,-2,3). Every Q-kernel basis vector was lifted, including vectors with zero higher image. The original-chain lift and target-boundary identities were checked exactly, not inferred from these character values.

The preceding highest-weight argument therefore proves that d2 surjects onto all65 dimensions of B_(2,4). In particular E3_(0,2),internal4 is zero and this change-of-rings spectral sequence does not degenerate at E2. This is a higher-differential theorem for the specified ternary-cube source. It does not identify every surviving ambient Tor class or imply a uniform theorem for other ranks or factor counts.
