# The complete fixed-order numerator hierarchy, with the conductor cost

Status: PROPOSED deduction from de Faveri Theorem 1.1 and the complete Hecke
AFE/functional equation; independent mathematical review required. No unknown
native moment or zero-free theorem is assumed. The central exponent formula
already occurs in #968; the new statement collects its full-strip extension,
actual-conductor proof and finite-anchor structure. No global priority claim
is made for these classical moment/interpolation arguments.

## 1. Full-strip theorem

Fix de Faveri's field F containing mu_6, admissible finite S and generator
data. Rows a are SIXTH-POWER-FREE exterior integral ideals with FULL norm
Na<=U. Take one fixed finite-order S-supported twist psi, or the fixed finite
list used in the CT adapter. Characters retain every original nonunit zero.
These are not arbitrary growing-conductor twists or angular characters.
The inducing conductor Q is O(Na), not necessarily comparable to Na.

Let r>=1 be any FIXED integer and 0<sigma<1 any FIXED real number. Put

    kappa_r=max(1, r/2, 5/6+r/6, 1/3+5r/12),
    F_r(sigma)=max(1, 1+r(1-2sigma),
                         kappa_r+r(1/2-sigma)).            (1)

Then for every epsilon>0,

    sum_(Na<=U)^flat |L_F^S(sigma+it,psi chi_a)|^(2r)
       << U^(F_r(sigma)+epsilon)(2+|t|)^C.                 (2)

The height exponent C and constants may depend on r,sigma,epsilon,F,S,psi.
No uniform r=r(U), field-degree or discriminant assertion is made. This is
an entire fixed-even-order theorem, not merely a calculation for r=1,2,4.
It concerns NUMERATOR L-values, not reciprocal-L/Mobius moments.

For sigma>=1/2, formula (1) simplifies to

    F_r(sigma)=max(1,kappa_r+r(1/2-sigma)).                (3)

The right-hand lines on which this bound first becomes U^(1+epsilon) are

    r=1: sigma=1/2;
    r=2: sigma=7/12;
    r=3: sigma=25/36;
    r>=4: sigma=1-1/r.                                   (4)

For example at the critical line F_1=1, F_2=7/6, F_3=19/12 and F_r=r/2
for r>=4. The diagonal-sized right-hand lines in (4) move TOWARD ONE as
r increases, not toward 1/2. Left-reflected estimates include the conductor
factor in the functional equation. At r=4, sigma=1/4, F_4=3, recovering the
published eighth-moment component rather than calling it new again.

For any subset E of at most U^nu rows, regardless of its zero-based selection,
Holder gives

    sum_E |L_F^S(sigma+it,psi chi_a)|
       << U^((1-1/(2r))nu+F_r(sigma)/(2r)+epsilon)
                                                   (2+|t|)^C. (5)

One must still bound any reciprocal/correction multiplying these L-values.
No independence between E and L is presumed.

## 2. Complete product columns, actual conductor and both AFE pieces

The freshly read source theorem is

    sum_(Na<=U)^flat |sum_(Nc<=V)^flat z_c chi_a(c)|^2
     << (UV)^eta K(U,V) sum_c |z_c|^2,
    K(U,V)=U+V+U^(5/6)V^(1/3)+U^(1/3)V^(5/6).             (6)

A fixed twist multiplies common column coefficients. For a full product
column v write uniquely v=c d^6, c flat. There is NO condition (c,d)=1.
The exact identity is

    (psi chi_a)(c d^6)
     =psi(c)psi(d)^6 chi_a(c) 1_((a,d)=1).                (7)

For a full dyad Nv~V with coefficients <=(Nv)^(-sigma+eta), fixing d gives
coefficient square mass <<V^(1-2sigma+eta)/(Nd)^6. Use (6), retain its row
mask, then Minkowski in row l^2. Summing (Nd)^(-3+eta) is convergent. Thus

    sum_rows |full dyadic polynomial|^2
          << (UV)^eta V^(1-2sigma) K(U,V).               (8)

Fixed divisor-function coefficients from L^r are absorbed by choosing a
smaller initial eta. All product ideals and shared primes remain. Formula
(8) also treats common norm twists and the conjugate family.

Split rows into actual inducing-conductor dyads Q0<=Q<2Q0, 1<=Q0<<U, and
the fixed gamma/S types. The complete AFE for L(s)^r has two pieces of
balanced length Q0^(r/2) times a polynomial height factor. Its main and
dual coefficient lines are sigma and 1-sigma; the dual scalar has modulus
Q^(r(1/2-sigma)) times a polynomial in height. On taking a squared row norm,
its conductor factor is Q0^(r(1-2sigma)), NOT U to that power when negative.

Separate the smooth conductor weights by Mellin inversion on a sufficiently
small positive line. Imaginary conductor powers are row phases. Real powers
and fixed divisor bounds cost U^O_r(eta); the coefficient arrays are common
across rows after separation. Dyadic AFE tails are rapidly decreasing and
are summed before renaming losses. These are standard AFE operations, not a
supremum over arbitrary coefficients independently selected at each row.
Inducing-principal rows (finitely many in this family) are omitted during
analytic interpolation and handled separately for each sigma in (0,1).
Their fixed-function contributions have polynomial height bounds.

For sigma>=1/2, the main dyads range from 1 to Q0^(r/2). For a monomial
U^a V^b in K, the maximum of U^a V^(b+1-2sigma) occurs at one endpoint.
The lower endpoint is at most U because a<=1. At the upper endpoint it
is U^a Q0^((r/2)(b+1-2sigma)); if the Q0 exponent is negative this too
is <=U^a<=U. If it is positive, Q0<<U gives the corresponding term in (3).

The dual polynomial in (8) has weight V^(2sigma-1). Its monomials are
nondecreasing in V, so multiplication of the endpoint by the ACTUAL dual
factor gives

    Q0^(r(1-2sigma)) U^a
                     Q0^((r/2)(b+2sigma-1))
       =U^a Q0^((r/2)(b+1-2sigma)).                     (9)

Exactly the same bound applies, including Q0 much smaller than U. Summing
the conductor dyads, AFE tails and separated Mellin integrals proves (3).
For 0<sigma<1/2, the functional equation has positive conductor power
Q^(2r(1/2-sigma))=Q^(r(1-2sigma)). Replace it legitimately by U to that
power, then apply (3) at 1-sigma to the conjugate family. This is (1)-(2).
No zeros or nonvanishing are used. QED.

## 3. Why arbitrarily high orders do not add independent bounds here

This section is a statement about the hierarchy (1), NOT an impossibility
theorem for sharper arithmetic estimates. All of its exponent data are
generated by the second, fourth and eighth moments, classical convexity,
complex interpolation and the functional equation.

At the central line, r=3 follows by ordinary Holder between p=4 and p=8:
weights 1/3 and2/3 in reciprocal p give

    (1/3)(7/24)+(2/3)(1/4)=19/72=F_3(1/2)/6.

For r>=4, the eighth moment U^2 and individual conductor convexity U^(1/4)
give U^(2+(2r-8)/4)=U^(r/2). Thus the large-r central exponents introduce
no information beyond that eighth moment and convexity.

On the diagonal-sized right lines, use vector-valued three-lines interpolation.
The p=6 anchor is the interpolation of p=4,sigma=7/12 and p=8,sigma=3/4,
again with weights 1/3,2/3:

    1/6=(1/3)/4+(2/3)/8,
    25/36=(1/3)(7/12)+(2/3)(3/4),
    1/6=(1/3)(1/4)+(2/3)(1/8).                          (10)

The last equality is the exponent of the row-norm bound. For r>=4 the
limiting interpolation weights between (p,sigma)=(8,3/4) and (infinity,1)
are 4/r and1-4/r. They give p=2r, sigma=1-1/r and row-norm exponent 1/(2r).
We do NOT assert a uniform Euler bound on sigma=1. To make this rigorous,
choose a fixed eta>0, use the Euler side at 1+eta, and use the eighth-moment
line 3/4-(r-4)eta/4. Its already proved exponent is1+(r-4)eta. The same
weights then land exactly on 1-1/r, with moment exponent 1+(r-4)eta. Choose
eta sufficiently small for the requested loss; r remains fixed. The r=4
case needs no limiting argument.

For completeness, the vector interpolation used here follows from the
three-lines theorem by duality on the FINITE row set. For a target dual
vector b with l^(p') norm1, write b_j(z) with modulus |b_j| raised to the
standard affine exponent p'[(1-z)/p0'+z/p1'] and its fixed complex phase.
Then sum_j f_j(s(z))b_j(z) is analytic and Holder bounds it on each vertical
edge by the corresponding l^p norm. Three-lines and duality give the desired
norm at the interior line. An exp(delta z^2) damping handles polynomial
height growth, then the common imaginary center gives a polynomial factor
in2+|t|. Zero coordinates are omitted and restored by a limit. Principal
rows, which could have a pole at1 inside the interpolation strip, were
removed beforehand. No logarithm of L or nonvanishing premise is needed.

For fixed p=2r, interpolate between its central estimate and its diagonal
anchor. This gives (3) up to arbitrary losses. To the right of the anchor,
use the Euler side and the trivial row-count lower norm scale U^(1/p),
yielding exponent 1. Reflect by the functional equation to get (1) on the
left. This proves the stated finite-generation property of this PARTICULAR
all-order envelope. Sharper numerator moments are not ruled out.

## 4. An asymmetric AFE is not an unpriced escape in this model

Consider an allowed worst conductor dyad Q~U and choose lengths U^u and
U^(r-u), 0<=u<=r, for the two pieces of L^r. Let d=2sigma-1>=0. After
squared norms the endpoint exponents contributed by a monomial U^a V^b
are

    main: a+u(b-d),
    dual: a+(r-u)b-u d.                                  (11)

Their difference is (2u-r)b. If b>d, their maximum is minimized at u=r/2:
the dual decreases up to that point and the main increases afterwards.
If b<=d, the balanced value is already <=a<=1 and cannot dominate the
unavoidable unit-column exponent 1. It follows that

    inf_(0<=u<=r) max(1, all eight exponents (11))
                       =F_r(sigma), sigma>=1/2.           (12)

This is a proof for every r, not a finite optimizer extrapolation. It is a
ceiling on improvement by balancing THESE positive estimates, not a lower
bound on an actual arithmetic moment. Actual conductor ranges are preserved
in the upper theorem; Q~U only specifies an allowed worst range in this
comparison of envelopes. The left side is reflected as before.

The user-requested RH-bearing all-moment claim cannot be obtained by silently
renaming these numerator bounds as inverse-L bounds, or by taking r to grow
without controlling the constants. CRITICAL_TARGET.md spells out that gap.
