# Internal review of the regular-tail and independent-padding obstructions

Status: **scoped internal review of proposed component proofs. No RH proof
or new zero-free region is approved by this receipt.**

The coordinating track read and reconstructed the complete proofs in
`theta/HARMONIC_LATTICE_OBSTRUCTION.md` (raw SHA256
`d508313ca0cc475ee08800a8b1bf9c8f0e28089677c6407b7e9cab33e807bcd4`)
and `theta/ANALYTIC_TAIL_OBSTRUCTION.md` (raw SHA256
`edd26b59e4c5cb829e1d744e091507e004a3d4df2c59ef51278d752cb3ac0204`).

For the lattice theorem the review checked the one-sided Poisson endpoint,
the cancellation of its real-part 1/k term, the summable 1/k^2 arc
remainder, and the pole-free quarter-sector rotation. The leading K1
integral gives the displayed nonzero amplitude and phase. The remaining
Fourier and hyperbolic-series terms have strictly faster exponential
decay. The continuum and actual-xi Laplace kernels have genuine Gevrey1
remainder bounds, so equality of their complete asymptotic coefficients
forces an exponentially small difference. It cannot conceal the larger
oscillatory exp(-2 sqrt(pi t)) term. A formal asymptotic expansion alone
would not establish that conclusion; the remainder estimates are essential.

For the analytic-tail extension, the inverse weight density is analytic
with constant term 1/2 and no linear term. At the dominant saddle, its
quadratic weight perturbation contributes exp(4 pi i c), a unit nonzero
phase, so it does not remove the leading amplitude. Higher analytic
coefficients change only the controlled smaller remainder. Finite real
couplings change linear, constant, and exponentially small terms. The
cofinal statement correctly includes compact control of every early
evaluation outside the common holomorphic disks; it does not incorrectly
deduce those evaluations from bounds near zero. The common tail estimates
give locally uniform entire convergence before the moment identity is used.

The coordinator also read the complete
`theta/INFINITE_DIVISIBILITY_OBSTRUCTION.md`. Its probability input is
the explicitly imported Levy--Khintchine representation with all real
exponential moments, not a new theorem proved in this packet. Jensen
bounds the other independent factor from below linearly. A nonzero
Gaussian part then contradicts subquadratic two-sided log-MGF growth;
any nonzero jump measure has positive finite mass on one interval away
from zero and gives an exponential lower bound in one direction. A
countable positive mixture inherits the same bound component by component
and would be atomic. For infinitesimal single-hub arrays the direct
third-moment remainder is bounded by max(weight) times total variance,
giving the stated Gaussian/two-point conditional limit. These arguments
do not exclude arbitrary correlated or hierarchical constructions.

No blocking gap was found at these stated scopes. The conclusions rule
out specified complete architectures; they supply no actual replacement
cofinal theta construction. The rational track's separate reviews record
its own independent reconstruction of the two regular-tail proofs.
