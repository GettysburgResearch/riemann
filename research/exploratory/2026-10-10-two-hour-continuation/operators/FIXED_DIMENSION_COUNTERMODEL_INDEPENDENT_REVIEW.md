# Independent audit of the all-row-shift fixed-dimension countermodel

Verdict: ACCEPT at the explicit inherited Bessel/Fourier source contracts.
Read in full: `../xi/cofinal-audit/fixed-size-countermodel/FIXED_DIMENSION_ALL_ROW_SHIFT_COUNTERMODEL.md`,
SHA2568ecd23a243fdf939abb9e6c1d850221170976276437b1055227fbc1a0697f35b.
All four named frozen dependency identities match their current bytes.
This is an analytic audit; no native numerical computation is performed.
The comparison sources are not actual Xi or its literal theta/Euler source.

FD1–FD6 have the correct quantifiers: for each fixed finite dimension d,
prescribed a,A,t0 and census height H0, a single sufficiently large X
works for EVERY nonnegative row shift. The source may depend on d.
The complete simple real Bessel spectrum is an explicit independently
reviewed selfadjoint spectral input. Its gamma_r^2<=B^2*r^2 bound gives
the heat comparison with each successive pair of Bessel roots. The
cosine factor's complete off-real roots are (2j+1)X+-iA, each simple;
they cannot coincide with a real Bessel root. Its positive atomic Fourier
measure makes the product a strictly positive translation mixture.

The real-head Vandermonde least eigenvalue beta is positive and independent
of X. FD9's determinant/trace bound is valid also at d=1. Each complete
real-node term is positive semidefinite, so FD10 pays any polynomial of
degree at most d-1 uniformly relative to the decaying z_d^(n+1) margin.
No absolute uniform-in-n eigenvalue gap is asserted.

FD12 counts BOTH members of every complex lattice pair. The exact odd-square
sum gives c*pi^2/(4X^2), not a single-member half of that value. FD13 uses
ordinary transpose; FD14–FD15 bound the modulus of each complex polynomial
product and retain the entire unknown lattice. Dividing by the real-head
gap yields exactly FD17, including its factor c/z_d. Both its prefactor
and alpha/z_d can be made strictly small by one choice of X, so EVERY row
shift passes simultaneously. Real symmetric positivity extends from real
coefficient vectors to complex vectors. No complex node is incorrectly
declared a positive Hermitian square.

The heat condition X^2>4B^2+A^2 correctly dominates each complex pair by
the two distinct real roots gamma_(2j+1),gamma_(2j+2). Complete normal
convergence justifies grouping. Every squared source root has positive
real part, so absolute Gamma/Laplace transport proves every scalar order
at every nonnegative spectral shift on the SAME source.

For the separate triple-root variant, removing one occurrence at any
finite set of distinct real roots leaves at least two real occurrences
at EVERY node. The residual real matrix therefore supplies twice FD10;
the unchanged complex price is less than half FD10, giving FD22's exact
3beta/(2c) margin. Its residual heat is at least2K_G+K_C>0. Triple real
roots still cross sign, but they are explicitly not a SIMPLE census and
one-occurrence selections do not exhaust their multiplicities.

These countermodels therefore explain the exact limitation of the newly
proved actual all-order size-four hierarchy: an arbitrary fixed dimension
and every row shift, even combined with every scalar sign and positive
Fourier/heat kernels, do not replace the all-dimension criterion. The
statement does not construct one off-real source passing EVERY dimension,
or an actual-Xi counterexample, and makes no cofinal/RH inference.
