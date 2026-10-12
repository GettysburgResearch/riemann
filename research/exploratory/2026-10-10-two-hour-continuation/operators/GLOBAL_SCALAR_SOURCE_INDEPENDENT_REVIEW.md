# Independent review of global actual heat/scalar positivity

Verdict: ACCEPT at the stated complete actual-source scope and inherited
native count-free census. The conclusion is K(u)>0 at every u>0 and
C_k(t)>0 at every integer k>=1 and real t>=0. It does not prove complete
monotonicity of K, all Hankel/mixed signs, simplicity beyond the imported
finite census, or RH.

Frozen owner proof `../xi/GLOBAL_SCALAR_MOMENT_POSITIVITY.md` SHA256
`bc0e85724fdd33ff1a0c5fe1a6e97d7f925823066847d2eff74435ab71db1826`;
checker `../xi/check_global_scalar_positivity.py` SHA256
`acf8c360928d4a2c7987ecc0eca5d499f13581c35749b5af27e1b1575d65a3ca`.
Both were read in full. I also checked the inherited complete count-free
SIXTEENTH_MOMENT_CENSUS_RECOVERY.md horizontal-coordinate scope, the
complete theta/Jensen count and the previously accepted full heat identity.

The small-time gamma estimate pays its entire signed integral. Comparing
the real exponents gives I_u(q)>=0 exactly when q>=12u. Below12u,
dropping the negative Gaussian factor and using1-exp(-q)>=qexp(-q)
gives I_u(q)>=-(3/4)exp(3q/4). The finite exp(9U)<2 guard therefore
pays every negative contribution by-18u. The positive interval[delta,1]
lies outside this region. Its first term integrates to the stated J,
while the negative term is at most
(1-delta)/(1-exp(-delta))*exp[-delta²/(16U)]<20exp(-125/8).
All discarded parts outside the negative region have proved nonnegative
sign. Consequently the lower constant C is a bound for the COMPLETE
gamma bracket, rather than for a truncated quadrature.

The prime estimate retains every prime power. On integers2..8, the
literal boundLambda(n)<=log n gives the21exp[-(log2)²/(4U)] envelope.
For the rest, the scalar function has logarithmic derivative
1/q-1/2-q/(2U)<0 when q>=log8>2. Sum-to-integral is therefore safe.
The log8>4U condition pays the linear exponent q/2, and integrating the
remaining Gaussian gives exactly4Uexp[-(log8)²/(8U)]. These are uniform
bounds for EVERY0<u<=U, including the full Euler tail. The strict directed
constant C-2D>0 proves the entire small-time region.

The other region uses the COMPLETE real head through horizontal coordinate
5419, not just known sign roots. That scope follows explicitly from the
native sixteenth-moment exclusion proof, including its closed boundary.
The selected root in(14,15) gives a positive head boundexp(-225u).
The previously checked complete count/strip/Stieltjes estimate gives
the whole unknown tail bound(R²+1/u)exp[-u(R²-1/4)]. Its ratio to the
head lower bound is strictly decreasing for all positive u. The strict
finite ratio atU consequently covers EVERYu>=U. Both regions includeU;
there is no interpolation gap or unaccounted complex-zero block.

All source nodes have Re(rho²)>0: the closed low head is real, and every
remaining gamma exceeds5419>|beta|. The complete absolute inverse-square
sum then pays the Laplace/Gamma interchange at EVERYnonnegative shift
and every finite integer order. The strictly positive K integral gives
each stated strict scalar moment. The completed entire product identifies
the same integral with the native logarithmic derivatives, including the
regular unshifted limit. Thus the normalized log is a Bernstein function;
the assertion concerns derivatives of its first derivative, rather than
derivatives of K. No all-order Hankel inference is made.

Independent normal and optimized directed checker runs both passed and
their JSON files are byte identical, matching the owner SHA256
`316a88278fc8854c3a649d39c478b43d6e35588160eae0bc325e9b983cb45ace`.
The paired files are global_scalar_independent.normal.json and
global_scalar_independent.optimized.json in this operator directory.
They authenticate the constants, exact inherited source map and native
backend. They do not rerun the old endpoint signs/jet or enumerate the
infinite time/order ranges; those are covered by the analytic proof above.

Positive heat/scalar countermodels with off-real nodes are consistent
with this conclusion. Complete monotonicity of K, or every mixed/Hankel
inequality, is a stronger all-order source condition and remains open.
