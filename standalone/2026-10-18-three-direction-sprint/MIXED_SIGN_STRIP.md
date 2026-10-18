# An explicit zero-strip budget for mixed-sign Ising couplings

Status: **PROPOSED elementary finite-model theorem and cofinal construction
test.** It extends the real-field ferromagnetic class of PR #1001, at
f6beb3774ae7ff5eca4cb046786eae10e4f88abc, by allowing negative couplings
with an explicit local price. It does not construct growth-controlled
approximants to the actual theta law or prove a zeta zero-free region.

Consider a finite graph with real couplings J_e, real fields h_i, and
positive observable weights w_i. Its Gibbs observable is X=sum_i w_i sigma_i.
Write q_e=tanh(J_e), and define the nonnegative edge price

    a_e = 0                                      if J_e>=0,
    a_e = (1/2) arcosh(exp(-2J_e))
        = atanh(sqrt(-q_e))                      if J_e<0.

Put a_i=sum_(e incident to i) a_e. The entire characteristic function of
X has no zeros outside the interval of imaginary parts

    min_i (h_i-a_i)/w_i <= Im z <= max_i (h_i+a_i)/w_i.       (1)

In particular, the enforceable budget

    |h_i|+a_i <= b w_i                            for every i

places every Fourier zero in |Im z|<=b. A field-reversing graph involution
preserving couplings and weights additionally makes the law symmetric.

This is an application of the classical contraction idea associated with
Asano and Ruelle. A primary source for the general method is
[Lebowitz, Ruelle and Speer, Location of the Lee--Yang zeros and absence of
phase transitions in some Ising spin systems]
(https://preprints.ihes.fr/storage/Lebowitz_R_Speer.pdf), Lemma2.4.
Only the elementary disk case is needed here, and its complete proof is
given below; the general set-valued lemma is not an additional premise.

## A complete disk-contraction proof

For a multiaffine polynomial A+Bu+Cv+Duv with no zeros when |u|<r and
|v|<s, substitute u=rt,v=st. Its quadratic has no zero in |t|<1.
If D is nonzero, Vieta's formula gives |A/D|>=rs, so the contracted
polynomial A+Dz has no zero in |z|<rs. If D=0, the conclusion follows
from A!=0. Fixing all other variables in their allowed disks proves the
same statement with coefficients depending on those variables. Thus it
can be iterated across any finite graph.

The edge polynomial, after dropping a nonzero constant, is

    P_e(u,v)=1+E_e(u+v)+uv, E_e=exp(-2J_e)>0.

If E_e<=1, it is nonzero when |u|,|v|<1. For E_e<1, solving for v and
using

    |1+E_e u|^2-|E_e+u|^2=(1-E_e^2)(1-|u|^2)>0

proves this immediately. For E_e=1 it factors as (1+u)(1+v).

If E_e>1, let r_e=E_e-sqrt(E_e^2-1)=exp(-2a_e). For |u|=rho<r_e,
the minimum over the argument of u of

    |1+E_e u|^2-r_e^2|E_e+u|^2

occurs at u=-rho. There it equals

    [1-r_e E_e-(E_e-r_e)rho]
    [1+r_e E_e-(E_e+r_e)rho] > 0,

because r_e^2-2E_e r_e+1=0. Therefore a possible zero v has
|v|>r_e. The edge polynomial is nonzero in the pair of disks of radius
r_e. This includes the complete edge interaction, rather than a small-J
expansion.

Multiply all edge polynomials using a separate variable for each edge
incidence. At a vertex contract its incidence variables: the constant
and all-incidences terms survive, enforcing the common spin at that
vertex. Repeated disk contraction gives radius

    r_i=product_(e incident to i) r_e=exp(-2a_i).

An isolated vertex contributes 1+z_i and has radius1. The resulting
partition polynomial is nonzero if every |z_i|<r_i. Global spin reversal
of the coupling-only polynomial gives

    Z(z_i)=(product_i z_i) Z(1/z_i),

so it is also nonzero if every |z_i|>1/r_i.

For the actual fields and Fourier variable, take
z_i=exp(-2h_i-2izw_i). Its modulus is exp(-2h_i+2w_i Im z).
The inner and outer disk conditions give precisely the two exterior
regions in (1). The nonzero exponential prefactor and Gibbs
normalization do not change zeros. This completes the proof.

An unobserved vertex with w_i=0 is also permitted when h_i=a_i=0.
Give it positive weight epsilon, apply the finite theorem with the same
symmetric band |Im z|<=b, and let epsilon tend to zero. This limiting
argument is asserted for the symmetric budget band, not for a general
asymmetric interval excluding zero. Finite sums converge locally uniformly.
Hurwitz applies in each exterior half-plane; the limiting characteristic
function is not identically zero since its value at0 is1.

## What this does and does not repair in a cofinal attempt

Weak negative edges have a square-root price: a_e is asymptotic to
sqrt(-q_e). A single negative edge with equal endpoint weights reproduces
the exact three-point Fourier band, so replacing this by a linear price
in |q_e| would be false. The theorem offers a concrete larger search
class while retaining a rigorous global band.

It does not repair the domain-wall construction in
theta/COFINAL_WALL_CONSTRUCTION.md. That construction forces opposite
endpoints with fields of magnitude H and therefore requires endpoint
weights at least H/b. Its aligned all-positive state has a vanishing
probability but an observable of size at least2H/b. The explicit bound
there forces the moment-generating function to diverge at every R>=b.

Replacing the opposite fields by a strongly antiferromagnetic endpoint
constraint has the same resource problem: a_e=(1/2)arcosh(exp(2|J_e|))
is asymptotic to |J_e|. The endpoint weights required by the band budget
again grow proportionally to the forcing energy. No bounded exponential
moment follows from this substitution. A successful cofinal construction
must control that rare sector, not merely reproduce each finite moment
list or replace the mechanism used to force the boundary condition.

The proof-relevant target remains an actual theta approximation with this
uniform band budget AND a uniformly bounded exponential moment at some
R>b. The sharper consumer is theta/ONE_POINT_ENTIRE.md; PR #1002 also
gives the sufficient R>1/2 consumer tailored to the zeta critical strip.
No such growth-controlled construction is supplied by this finite
zero-strip theorem.
