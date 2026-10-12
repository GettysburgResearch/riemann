# Explicit physical-length native continuum target

Status: new proof and full directed run submitted for independent review.
Scope: one fixed native length L=21/20, and its zero-extension consequences.
Exact sources: immutable prior-wave O1--O4, complete-Xi binding, full gamma
convolution/Taylor helper, phase line and ten-dimensional family to log3.
What was actually run: two preparatory panels and all four omitted-anchor
checks passed; the complete636-panel run is active. No new sign is claimed here.
Smallest remaining gap: complete outward R receipt and weighted finite gate.

## Native normalization and exact trials

All coordinates here are physical. Set L=21/20,b=3/2,c=1/2,d=log2,
q(h,k)=b integral_[0,L]^2 conjugate(h(t)) W(t-u) k(u) du dt.
The complete arithmetic source W is the prior-wave literal kernel, including
P2=-zeta'(2)/zeta(2) and the active prime2 term at x>=d. Since L<log3,
no further prime cusp enters; every prime power n>=3 remains in the exact
protected cosh/sinh rank-two tail. Native inputs are arbitrary complex L2
functions on[0,L]. E_L has seven sin(j*pi*t/L), exp(+-t/2),cosh(bt);
V_L=E_L^perp. The reviewed line PV>=4x/5-244 and clamped primitive
h=phi''-phi/4 give q(v,v)>=1/2 ||phi'||², uniformly L<=log3.
The transfer of all seven sine constraints and protected sinh constraint
is unchanged. This is a primitive norm bound, not an L2 spectral gap.

`physical_length_source.py` copies the independently reviewed physical
LengthSource transform and finite Galerkin construction without its ordinary
sampling imports. T_L(z)=int_0^L W(x)e^(zx)dx is entire; its derivative
contains the actual L factors. The complete gamma remainder is
exp((b-lambda0)L)/[(lambda0-b)^2 lambda0 (1-exp(-2L))], with derivative
factor L+1/(lambda0-b). D_L(alpha,beta) is
[e^((alpha+beta)L)(T_L(-alpha)+T_L(-beta))-T_L(alpha)-T_L(beta)]/(alpha+beta);
the removable sum-zero value is L(T_L(alpha)+T_L(beta))-T_L'(alpha)-T_L'(beta).
The physical ordinary Gram uses L*f((alpha+beta)L), not the unit-window Gram.

The exact orthonormal E frame and projected next100 sines (indices8..107)
produce exact trial z=e-v and U=q(z,z), with outward coefficient balls.
These are enclosures of the exact Galerkin definition, not rounded new tests.

## Complete moving-interval residual and moments

For beta!=0, write I_z(a)=int_0^a W(x)e^(zx)dx,H(a)=int_0^a W.
Then K_beta(t)=e^(beta*t)[I_(-beta)(t)+I_beta(L-t)] and

F_beta=(-beta+1/(4beta))K_beta-W(t)+e^(beta L)W(L-t)
       +[-T_L(beta)-H(t)+e^(beta L)(H(L)-H(L-t))]/(4beta).

This follows from K'=beta K+W(t)-e^(beta L)W(L-t) and integration
of K. Its endpoint formulas retain e^(beta L),W(L),H(L). The literal
source slabs are [0,L-d],[L-d,d],[d,L]. Left/right prime activation is
respectively (false,true),(false,false),(true,false). The inherited complete
incomplete-gamma formula and real Taylor acceleration are unchanged; their
semantic frequency value is now i*j*pi/L. The maximum physical frequency
107*pi/L is less than the reviewed111*pi cap. Real-rate keys remain+-c,+-b.
All other complex nodes retain the original complete hypergeometric evaluator.

Let Pi remove 1,cos(j*pi*t/L),j1..7,sinh(bt). R is the complete Gram
of PiF_z. Its physical Gram has G00=L,Gjj=L/2,
G0s=(cosh(bL)-1)/b,Gjs=b[(-1)^j cosh(bL)-1]/[b²+(j*pi/L)²],
Gss=sinh(2bL)/(4b)-L/2. The exact cosine moment for n>0 is
K_beta(0)-(-1)^n K_beta(L)-(nu+1/(4nu))D_L(sin(nu*t),e^(beta*t)),nu=n*pi/L.
The mean moment is K0-KL+(L*D_L(0,beta)-partial_alpha D_L(0,beta))/4.
The sinh moment is the difference of the two exponential-test moments.
These identities are integration by parts, without quadrature.

Physical Parseval gives the weighted dual matrix
B_N=b[t_N R+(2/L) sum_(n=8)^N (lambda_n^-1-t_N) a_n^*a_n],
lambda_n=4/5-244 L²/(n*pi)²,t_N=lambda_(N+1)^-1,
a_n=int_0^L PiF_z(t)cos(n*pi*t/L)dt.
The full infinite cosine tail is retained. The factor2/L is essential.
Then U-B_N is a valid Schur lower bound. Original protected source coupling
is retained throughout; no Fourier support is inferred from sine projection.

## New full Cauchy and endpoint budgets

On each Cauchy disk used by the producer, 0<Re(t)<L and |Im(t)|<=.01.
All directed parameter checks establish |Cb|<.5,P2<.6,q2<.5,
exp(cL)<2,exp(bL)<5,cosh(bL)<3,Gamma(0)<.4.
The complex gamma series has absolute value<=Gamma(0). Nongamma terms
obey these same exponential bounds. The analytically continued active prime
branch has |sinh(b(t-d))|<3 because |Re(t)-d|<.7 and |Im(t)|<=.01;
its absolute value is below1. Consequently |W|<8 on these disks.
For real |x|<=L, the sharper elementary sum gives |W|<4:
.5 exp(cL)<1, |Cb|<.5,Gamma<.4,(P2/b)cosh(bL)<1.2,
and the active prime term <.3 (as b(L-d)<.54). Their sum is below3.4.

The two straight base paths have total length below L+.02<1.07.
At most one active prime path occurs, of length below L-d+.01<.4.
For every native beta, the exponential integrand is bounded by
exp(bL+omega*.01),omega=107*pi/L. Thus the sum of both partial integrals
is below16 exp(2+omega*.01). Multiplication by e^(beta*t) proves
|K_beta|<32 exp(4+2omega*.01), the deliberately looser producer bound.
Also |T_L(beta)|<24,|H(t)|,|H(L-t)|<10,|H(L)|<4.2,
|e^(beta L)|<5 and1/(4|beta|)<=.5. The additive part of F is below
8+40+.5*(24+10+5*(4.2+10))=100.5<120.
Thus every primitive F has absolute value at most
M0=(omega+.5)*32 exp(4+2omega*.01)+120.
If C is the maximum directed absolute column sum of trial coefficients,
M=M0*C bounds every exact F_z. Projection tests satisfy |p|<3:
cosine bounds use exp(7*pi/(100L))<3, and sinh(b(t)) is below3 on the disks.

Normalized dyadic panels omit epsilon=2^-50 at each slab endpoint and have
width<=1/100. Their physical disk radiusR=2h is explicitly checked<=.01
and inside0<Re(t)<L. The unchanged Cauchy argument gives errors
8h M² 2^(-2n) and8h*3M 2^(-2n),n=76. All nodes/weights/transcendentals
and matrix arithmetic are outward Arb/acb. The sums of these budgets bound
EVERY covered panel, not an empirical quadrature difference.

For real |x|<=L, the nongamma derivative has piecewise absolute value below5.
Indeed .25exp(cL)<.5,b|Cb|<.75,P2*sinh(bL)<1.5,
q2*cosh(b(L-d))<.8; these sum below3.55. The continuous prime join
preserves this Lipschitz bound. The same complete gamma-series split as the
old proof therefore gives omega_W(delta)<=delta*(7+2log(1/delta)) for
delta<=1/2. The new producer uses the weaker valid12+4log bound.
All six omitted pieces have physical length<=delta=L*epsilon.
The exact trial bounds are ||z||inf<=5C and||z'||1<=L(omega+8)C.
Integration by parts in the full W^(1,1) convolution therefore bounds
F variation by delta*(12+4log(1/delta))*(2*5C+L(omega+8)C)
              +delta*L*5C.
Every exact F at all four anchors is checked<1 and this variation is checked<1.
Hence |F|<2 throughout omitted pieces. Their total length<=6L*epsilon;
entrywise added radii24L*epsilon and36L*epsilon respectively enclose
all missing FF and pF integrals. No cusp interval or endpoint is discarded.

## Strict acceptance and scope

The full R receipt must authenticate exactL21/20,m7,100trials,256bits,
order76,epsilon2^-50,636 exact panels covering all three slabs except the
paid omitted pieces, current frozen producer/physical adapter/legacy helper
hashes and exact Galerkin coefficient balls. Fresh full-source moments and
U must be rebuilt. Acceptance requires outward LDL pivots for
U-B128-10^-11 I all strictly positive. Scalar U-(9/2)R may fail without
refuting positivity. Scientific acceptance additionally requires independent
analytic/source/parameter review. Zero extension of native tests then transfers
one accepted L21/20 sign to every0<ell<=21/20. This supplies no sign atlog3,
no all-window statement, and no RH conclusion.
