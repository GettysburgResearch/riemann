# Principal correction near the contour residue: a candidate factorization

**Status:** Proposed extension; corrected local algebra and bounds checked internally, no zeta zero-free claim.
**Source and dependencies:** The imported source-local identities and notation are as in [the residue-point factorization](2026-10-28-principal-factorization.md). The source identity itself has not been checked here. The Hecke continuation is a standard imported theorem.
**What was run:** Symbolic simplification of the source-local expression; the power bounds below were derived by hand.
**Smallest gap:** Audit of the imported source identities. The bound does not control nonprincipal rows, the whole original contour, low estimates, or the size of the Hecke factor.

For fixed σ0>1/2, set κ=σ0−1/2 and h=min(κ/20,1/100). In the tube

    Re(s)≥σ0,  Re(w)≥1−h,  Re(z)≥1/6−h,

let V=Q^(−6z), W=Q^(−w), D=η(p)Q^(−s), R=ψ_eta(p)Q^(4−6s−6z) for each good prime of norm Q, where ψ_eta=conj(α)^6η^6. The u=1 source-local identities imply

    E=[R((1−1/Q)/(1−V)+W−D)−D(Q−1)WV/(1−V)]/(1−R),
    H_p−1=[D(V+W−VW)−VW+(1−V)(1−W)E]/(1−D).

Define K_p=(1−R)H_p initially where the source expression converges. Direct algebra yields

    (1−D)(K_p−1)
       = D[V+W−Q V W+(Q−1)V W²]−VW
         + R[VW²−W²+W/Q−1/Q].

This polynomial identity extends K_p holomorphically where Re(s)>0, since 1−D stays away from zero uniformly on the tube. With c=min(6κ−12h, σ0−7h, 1−7h)>0, each term in this expression has magnitude O(Q^(−1−c)), uniformly in η and all three imaginary parts. Indeed |R|≤Q^(−6κ+6h); the bracket multiplying R is O(Q^(−1+6h)), the D terms are O(Q^(−1−σ0+7h)), and VW is O(Q^(−2+7h)). Hence the product K_eta(s,w,z) converges absolutely and uniformly in the tube. Excluding all primes of norm at most P0 gives K_eta=1+O(P0^(−c)), with constants depending on σ0; for large enough P0 it is nowhere zero there.

Initially on the intersection with the source Euler-product region, and thereafter by continuation, this gives

    H_eta,1(s,w,z) = L^S(6s+6z−4, ψ_eta) K_eta(s,w,z).

The L-function factor is entire because ψ_eta has nontrivial angular infinity type. This formula continues one principal correction to a tube around (w,z)=(1,1/6), but a zero or large value of the auxiliary Hecke L-function remains a real obstruction: K_eta's contraction alone is not a bound or nonvanishing theorem for H_eta. The source's nonprincipal corrections and full contour geometry are not treated.
