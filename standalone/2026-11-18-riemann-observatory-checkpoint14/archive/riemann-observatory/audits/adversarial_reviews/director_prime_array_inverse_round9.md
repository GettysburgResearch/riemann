# Director adjudication: what the prime-array limits determine

17 November 2026. I reconstructed the Fourier identities, logarithmic quadrature, mass estimate and finite-data controls after the independent complete proofs prime_array63_inverse_fourier_review.md and generator63_prime_array_inverse_skeptic.md. The arithmetic premise is the separately adjudicated RH-conditional fixed-target prime-array theorem. This is an inverse theorem about exact limiting data, not a numerical algorithm inferring zeros from three finite error bounds.

Let nu be the finite symmetric atomic measure assigning |zeta'(rho)|^2/|rho|^2 to each simple critical-line ordinate, both signs. F(t)=integral exp(-it gamma)dnu and B=nu(R). Finiteness follows from an unconditional fixed-strip derivative bound and the zero count. Under RH the fixed-target limits C_k and their polarized form satisfy

    C_k=(k+1)B-2 sqrt(k)F(log k),
    Q(R_k-R_l)=(k+l)B-2 sqrt(kl)F(log(k/l)).

Therefore B=lim C_k/k and C_k/(sqrt(k)+1)^2<=B<=C_k/(sqrt(k)-1)^2. Full real forms determine F on the dense group log Q_(>0); continuity and Fourier uniqueness determine every finite symmetric measure. Complex polarization and simultaneous scaling recover nonsymmetric measures if those are the intended unknowns. Real forms alone see only reflection symmetrization.

More surprisingly, singleton C_k alone determine every atom. With Delta_k=log(1+1/k) and L_K=log(K+1),

    nu({x})=lim (1/L_K)sum_(k=2)^K Delta_k F(log k) exp(ix log k).

Uniform continuity controls the logarithmic quadrature, and bounded convergence in the continuous Cesaro mean isolates the atom. Substituting B_K=C_K/K in the reconstruction of every F(log k) in this finite sum adds only O(B/log K). Thus the first K singleton limits suffice for the Kth estimator. All these limits take the arithmetic N to infinity at each fixed k before K increases. No joint effective convergence modulus has been established.

The atomic measure is consequently unique from all singleton limits, recovering simple-zero ordinates and derivative magnitudes, but not multiple zeros or derivative phases. Diffuse measures need the cross data: an even smooth Fourier bump supported inside 0<|t|<log 2 produces two distinct positive diffuse measures of equal mass and identical singleton values. Any finite list of full form data also admits distinct positive atomic profiles, even with supplied equal mass, in any chosen open height interval. Without supplied mass, evaluate the entire Gram kernels at z=i/2, where all vanish but the constant function does not, to construct different-mass competitors. These are synthetic controls, not possible alternative zeta functions.

Singleton errors o(sqrt k) still permit atomic reconstruction; O(sqrt k) errors can conceal different equal-mass atomic profiles. Normalized full-form errors cannot uniformly bound total variation, as the independent Rudin–Shapiro finite atomic construction shows. Toeplitz positivity is a useful finite necessary test. Exact singularity restricts support modulo one sampling period; two incommensurate grids can remove those aliases. Positivity on all rational-log frequencies needs continuity at zero in the usual real topology to represent a real-line measure. The additional topology cannot be inferred from positive matrices alone. Quantitative recovery requires a numerical tail/moment bound and controlled limiting-data errors.
