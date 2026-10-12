# Quantitative primitive consequence of the explicit length gate

Status: exact general-length synthesis adapter submitted for review; the full
R and weighted finite gate are still pending. No new sign is claimed here.
Scope: physical L=21/20 and zero extension to every shorter native interval.

Apply the independently reviewed prior-wave quantitative square-completion
lemma to this physical interval. Its proof is Hilbert-space algebra and uses
only the same orthonormal finite frame, exact protected coupling, complement
coercivity and primitive synthesis. In this case the accepted family gives
kappa=1/2. Suppose the fresh weighted gate is U-B128>=epsilon I,
epsilon=10^-11; B128 is positive semidefinite by its exact Gram construction.
A directed traceB128<1 supplies M=1. A directed sum||G_L z_i||²<1 supplies
K=1. The general lemma gives theta=epsilon/(2+epsilon)=1/200000000001,

delta=min(epsilon/[2(1+2K)],theta*kappa/2)=1/800000000004.

For every complex native h inL2(0,L), q_L(h,h)>=delta||G_Lh||², where
G_Lh(t)=int_0^t cosh((t-u)/2)h(u)du. This norm is injective on native
L2, hence nonzero tests have strictly positive form. No L2 spectral gap is
asserted. Zero extension preserves the complete native form and makes the
larger primitive norm dominate its restriction, giving the same bound for
every0<ell<=21/20. This consequence is conditional on the completed finite gate,
not a proof from a positive upper section or sampled residual.

The exact primitive basis identities do not depend on interval length:

G sin(nu t)=nu/(nu²+1/4)[cosh(t/2)-cos(nu t)],nu=n*pi/L;
G exp(+-t/2)=t exp(+-t/2)/2+[exp(t/2)-exp(-t/2)]/2;
G cosh(3t/2)=3sinh(3t/2)/4-sinh(t/2)/4.

Thus every primitive trial is an exact combination of the six soft functions
exp(+-t/2),t exp(+-t/2),exp(+-3t/2), and cos(n*pi*t/L),n1..107.
Their physical Gram is enclosed without quadrature. For the entire
f(z)=(exp(z)-1)/z, its soft product moments are
int_0^L t^p exp(a t)dt=L^(p+1)f^(p)(aL),p0..2, with removable
value L^(p+1)/(p+1) when a=0. Mixed soft/cos products are the real parts
of the same entire expression at a+i*n*pi/L. Distinct cosines are exactly
orthogonal and each squared norm isL/2; all soft/cos cross terms have factor2.
These physical L factors are explicit in `enclose_length_primitive.py`.
All110 raw coefficient rows, including100 high modes8..107, are included.
The sum of exact squared primitive norms is a Hilbert--Schmidt bound for
complex coefficient synthesis. No orthogonality of the trial primitives is
assumed and no cross term is discarded.

The extractor first replays the frozen weighted checker in full, including
actual source, exact trial coefficients, current old/new helper hashes,
complete panel coverage and outward LDL gates. It compares the entire saved
weighted receipt to that fresh result before extracting any coefficient.
It then encloses traceB and the complete113-function primitive Gram:
six soft functions and107 cosines.
Acceptance requires both traces strictly below1 and exact rational delta.
The extractor is not a second continuum integration; source/R trust and
independent arithmetic review remain explicit dependencies. No sign atlog3,
all-window positivity, or RH follows from this fixed-length result.
