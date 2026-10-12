# The completed native window has an open right extension

Status: proposed analytic consequence of the completed source-bound
codimension14 certificate, pending independent review. No numerical value
of the right-extension radius is certified here.

**Claim.** There exists eta>0, with eta<=1/10000, such that the exact native
q_L is strictly positive on every nonzero complex L2(0,L) test for every
0<L<=1+eta. This gives a qualitative right extension of the completed
0<L<=1 certificate. It supplies neither a specified larger length nor
unbounded-window positivity or RH.

## Uniform complement near one

Retain the complete arithmetic kernel W, b=3/2, c=1/2 and the exact
all-frequency supporting line from CODIMENSION_14_REFINEMENT.md,

    P(x)V_2(sqrt(x)) >= (13/10)x-710.

For native length L, let E_L be the span of sin(j*pi*t/L), j=1,...,11,
exp(+-t/2), and cosh(3t/2), and V_L=E_L^perp. The original clamped
primitive argument, with sine frequencies j*pi/L, gives

    q_L(v,v)>= (3/2)[13/10-710*L^2/(12*pi)^2] ||G_L v||_2^2
                                                            (P1)

for v in V_L. The exact full prime tail has the same protected rank-two
form because L<=10001/10000<log3. No additional prime cusp occurs in this
interval. The sign transfer of the sine constraints and every clamped
boundary term are identical to the reviewed L-dependent argument in
WINDOW_FAMILY_TO_LOG3.md; only the number of removed sines is increased.

The rational inequality

    710*(10001/10000)^2 < 72*(333/106)^2 < 72*pi^2

therefore gives q_L(v,v)>=(6/5)||G_L v||_2^2 throughout
1<=L<=10001/10000. The primitive G_L is injective. This is a uniform
primitive gap, not a native L2 spectral gap.

## Continuous finite tests and residual

Construct the L2-orthonormal basis e_i(L) of E_L using the same ordered
native Gram Cholesky rule as at L=1. All native basis functions and their
Gram entries vary continuously after rescaling t=L*s to [0,1], and they
are linearly independent. Hence e_i(L) vary continuously near one.

Let v_k(L) be the high sines sin((11+k)*pi*t/L), k=1,...,100, projected
orthogonally into V_L. Write the exact completed trial correction as
u_i(1)=sum_k A_ki*v_k(1). Keep these exact coefficients fixed and define

    u_i(L)=sum_k A_ki*v_k(L),   z_i(L)=e_i(L)-u_i(L).

At one these are exactly the already certified z_i. At nearby lengths
they are legitimate finite trial corrections in V_L. Energy-Galerkin
optimality away from one is not required by the completion inequality.
Define U_ij(L)=q_L(z_i(L),z_j(L)) and let R_ij(L) be the complete protected
source-residual Gram, with F_z=-K_z'+c^2*integral_0^t K_z and
K_z(t)=integral_0^L W(t-u)z(u)du. The protected projection is the same
length-dependent primitive constraint projection used in O1--O4.

Both U(L) and R(L) are continuous. For completeness, on the fixed length
cap W is continuous and bounded, while away from zero its derivative has
the uniform local bound

    |W'(x)|<=C*(1+|log|x||),   0<|x|<=10001/10000.            (P2)

Indeed the literal gamma derivative has coefficients O(1/j), bounded by
the convergent geometric logarithm sum; every other native term and the
prime2 derivative on its two sides is bounded. Its finite jump at log2
causes no failure of dominated convergence. Under rescaling, the
integrable majorant 1+|log|s-r|| bounds the complete convolution derivative
uniformly for L near one. Thus K_z' and F_z vary continuously in L2, by
dominated convergence, with a uniform pointwise integrable majorant. The
finite protected Gram and its inverse vary continuously because their
functions remain linearly independent for every L>0. This proves the
claimed continuity of the complete projected R, including its entire
gamma series and full prime tail.

## Opening the finite positive gate

The completed outward receipt and independent rational-LDL review prove

    U(1)-(15/8)R(1)>=10^-11 I.                               (P3)

Continuity of this finite Hermitian matrix gives some eta>0, eta<=1/10000,
such that

    U(L)-(15/8)R(L)>=(1/2)*10^-11 I,
                  1<=L<=1+eta.                             (P4)

The uniform complement gap (P1), the exact native coupling identity and
ordinary square completion give (P4) as a lower bound for the finite
effective form at every such L. The decomposition h=sum_i x_i*z_i(L)+v
is available for every native h, with v in V_L. If x is nonzero, (P4)
pays a strictly positive finite reserve; if x=0 and h is nonzero, (P1)
and primitive injectivity pay strict positivity. Together with the
already completed small lengths, this proves the claim.

The radius eta is a mathematical existence result from an actual strict
finite gate. Certifying a particular eta requires a directed uniform
modulus for these matrices, not a sampled length scan. No such modulus or
specified L>1 sign is asserted here. Existing frozen numerical producers,
receipts and baseline constants are unchanged.
