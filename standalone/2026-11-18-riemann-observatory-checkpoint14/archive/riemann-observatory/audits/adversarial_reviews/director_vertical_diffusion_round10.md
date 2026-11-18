# Director adjudication: a zero crossing becomes Gaussian

18 November 2026. I derived the bridge independently from the completed Hadamard product, then checked both full reconstructions uniform64_vertical_shift_diffusion.md and positivity64_vertical_diffusion_skeptic.md. Source normalizations and exact degree-one witnesses are independently checked in release64_vertical_shift_skeptic.md and geometry64_vertical_shift_counterexample.md. The probability conclusions retain GRH. The local diffusive Poisson limit is standard; publication priority of this combined application is unassessed.

Start with a pole-free Selberg-class F whose completion is nonzero at1/2, and write E(z)=xi_F(1/2−iz), zeros gamma with multiplicities. For real tau, F_tau(s)=F(s+i tau) stays in the class with the same degree. Its completion differs from xi_F(s+i tau) only by the constant Q^(-i tau), its gamma shifts are mu_j+i lambda_j tau, and its root number is omega Q^(-2i tau). Thus E_tau(z)=Q^(-i tau)E(z−tau) and its zeros are gamma+tau. Nonzero vertical shifts of zeta are excluded by the pole-location axiom; this construction must not be silently applied to zeta itself within that class.

Use b for the uncompensated Lévy drift. If the raw Hadamard product uses exp(B_raw z), then b=−B_raw. Away from a central crossing, the exact shift identity is

    b_tau=b_0+sum_gamma m_gamma[1/(gamma+tau)−1/gamma],
    g_tau(t)=i b_0 t+sum_gamma m_gamma{
      (exp(−i(gamma+tau)t)−1)/(gamma+tau)²
      +it[1/(gamma+tau)−1/gamma]}.

The differences are absolutely summable; for large gamma every term and its tau derivative are uniformly O_T(|gamma|^(-2)) on compact tau,t sets. Constants multiplying E have no logarithmic-derivative effect. These formulas use the drift sign of the Nakamura–Suzuki exponent, not an unconverted raw constant from another source.

At tau0=−gamma0, multiplicity m, put delta=tau−tau0. Its combined term is

    m[(exp(−i delta t)−1+i delta t)/delta²−it/gamma0]
       -> −m t²/2−im t/gamma0.

The remainder of the compensated exponential is at most m|delta||t|³/6 for real delta,t. All other terms are locally uniformly Lipschitz after isolating the finite neighborhood, so the whole exponent is continuous through the crossing. The finite regular part in the drift is essential. Keeping the individual jump and divergent drift separate and taking their limits would fail.

On GRH the singular factor is precisely the characteristic function of

    −delta [Poisson(m/delta²)−m/delta²].

It tends to N(0,m). The full infinitely divisible laws are weakly continuous by locally uniform exponent convergence and Lévy continuity. Thus the central Gaussian variance is the finite diffusive limit of an increasingly frequent small jump, not an unexplained discontinuity in the law. The canonical-height normalization still matters for the arithmetic meaning of a central zero.

There is a useful finite-measure formulation. In the compensated convention let c_tau be the drift and let

    K_tau=a_tau delta_0+[lambda²/(1+lambda²)]nu_tau
      =sum_all_gamma m_gamma/[1+(gamma+tau)²] delta_(-gamma-tau).

The mass at zero is exactly the central multiplicity. This formula and

    c_tau−c_0=sum_gamma m_gamma[f(gamma+tau)−f(gamma)],
    f(x)=x/(1+x²),

are continuous through every crossing, with uniformly summable tails on compact tau sets. The compensated kernel (1+lambda²)(exp(it lambda)−1−it lambda/(1+lambda²))/lambda² extends continuously at0 with value−t²/2 and is bounded for fixed t. This gives the same weak continuity directly from K_tau and c_tau. Positivity here relies on GRH; it supplies no independent proof of that premise.

For chi4, an actual certified nonzero line-zero ordinate gives a degree-one central crossing; beta(1/2)>0 at the original height. This makes the normalization issue concrete without assuming GRH or simplicity merely to establish the central zero. The laws and their Gaussian interpretation then use the shared GRH of the shifted and original function. Proposed compensated-drift sign issues in other versions remain separate and unadjudicated; this note relies on the displayed independent derivation.
