# A unitary boundary multiplier can hide an unstable causal mode

Status: PROVED elementary synthetic control, awaiting packet review.
Scope: exact bilateral Laplace transforms; this is not an arithmetic
counterexample and does not assert an off-critical zeta zero.

Let a,b>0 and set

    R_a(r)=(r+a)/(r-a),       F_b(r)=1/(r+b).

On the imaginary axis |R_a(it)|=1. Thus multiplication by R_a is an
isometry on the full boundary L2 space. Nevertheless it has a pole at r=a
in the causal half-plane.

The causal input is f_b(u)=exp(-b u) 1_(u>=0). Inverting R_a F_b on a line
Re r>a gives

    h_causal(u)=[c exp(-b u)+d exp(a u)]1_(u>=0),
    c=(b-a)/(a+b), d=2a/(a+b).                               (1)

Inverting instead on the imaginary axis gives

    h_boundary(u)=c exp(-b u)1_(u>=0)-d exp(a u)1_(u<0).      (2)

Both follow directly from partial fractions. Their difference is

    h_causal(u)-h_boundary(u)=d exp(a u)                     (3)

for every real u, exactly the residue of exp(r u)R_a(r)F_b(r) at r=a.
The boundary norm is

    c^2/(2b)+d^2/(2a)=1/(2b)=||f_b||_2^2.                  (4)

The causal energy, by contrast, grows as

    integral_0^U |h_causal(u)|^2 du
         ~ d^2 exp(2aU)/(2a).                              (5)

For a=1/4,b=3/4 one has c=d=1/2: the boundary norm squared is 2/3,
while the causal energy is asymptotic to (1/2)exp(U/2).

This is the exact obstruction a critical-line scattering argument must
handle. A bounded, even unitary, boundary multiplier does not bound the
original causal source on finite horizons if its pole residues are omitted.
If the input transform has the required zero at r=a, the residue is
canceled; that condition has to be proved for the actual transform and
in a space in which the transformation is defined.

For a meromorphic multiplier and a decaying test transform, the finite
rectangle residue theorem generalizes (3): the inverse transforms on two
vertical segments differ by every crossed principal part plus both
horizontal edges. A pole of order m contributes exp(pu) times a polynomial
of degree at most m-1. Passing to infinite heights additionally needs
boundary control; a finite numerical list of zeros does not provide it.

In the angular Hecke application, the exact multiplier is a gamma smoothing
factor divided by an inner function. The companion Hardy-space theorem
identifies a legitimate causal subspace and its precise orthogonal defect.
It does not license applying unweighted Plancherel to a native source that
may still have exponential growth on logarithmic scales.
