# Internal review of the global tail counterterm

Status: **source-qualified component review. The complete mixed mean
and a new zero-free region remain unproved.**

The coordinator reconstructed `eisenstein/TAIL_DEBIASED_MOLLIFIER.md`
at raw SHA256
`66415deed8a2c97c89c20049f8dd6d70ff33a41a1666a84ddc0cdcfa58b5a27a`.
The exact coefficient algebra and detector preservation were checked
against the pinned original source's full detector proof, lines
4510--4695. The unrestricted zero-slot two-plain moment was read
directly in that same source, lines 12505--12605; its physical
sixth-power-free row eligibility was read around lines 14950--14995.
The comparison residue theorem was read in the primary rStation paper8,
including its unrestricted plain index, fixed numerator-ray filters,
Type-I error, and explicit continuous-remainder limitation. This is
not an independent validation of either entire imported manuscript.

The two coefficient responses are independent because the positive
counterterm lives strictly above the original prefix cutoff. Its
normalization B_D is bounded below by the fixed-field squarefree density;
it is not an inverse of an unknown signed sum. The finite mollifier
still equals mu on every ideal of norm at most D. Its convolution with
one therefore has exactly the same low-product unit gate, including
every shared prime and every original zero extension. Multiplication
of an entire nonprincipal L-function by this finite polynomial does
not remove any of its zeros.

The original Gamma integral, moved to -1/4, has the same coarse
negative exponent after the support grows by a fixed factor three.
Its complete product tail is -1+o(1), with the same terminal cutoff.
Keeping only PRODUCT annuli is essential: the zero's real and imaginary
parts then occur in one product profile, so the residue leading
functional is the single exact sum canceled by construction. Imposing
separate plain or inverse dyadic profiles first would instead create
a Mellin family of different functionals; one scalar would not cancel
that family. The note correctly preserves this order of operations.

For low product annuli the rescaling X'=max(X,3D) keeps the whole outer
support inside the theorem's length hypothesis. The profile change has
bounded seminorms and leaves its X^(5/6) Mellin prefactor invariant.
Thus no missing counterterm tail is hidden at the endpoint. The error
still costs U^(1/3)X^(-1/3)D^(4/3) in the squared adjoint pairing:
the favorable corner U^(7/6) is not a uniform global estimate, whose
X approximately D end is larger.

The Euler identity for the positive tail is exact: its additional
factor has local coefficients (Q^-1-Q^-2)(-1)^(j-1), j>=1, and finite
absolute coefficient mass at real part1/2. Extracting a=h^2 b n gives
the coefficient 1/(Nh sqrt(Nb)); the h sum is logarithmic and the b
sum converges. All shared primes and zero masks stay in the character
values. Minkowski invokes the NAMED unrestricted two-plain source
theorem, not an unjustified extrapolation of a short-length second
moment. The resulting correction has row-size joint cost up to logs.

During review the coordinator caught an underestimated pointwise
coefficient bound: v(a)^-1 is unbounded. The final note pays it by
v(a)^-1<=sum_(d|rad a)1/Nd=O(log(2Na)), so the modified coefficients
are O(log(D)^2). The contour and Type-I errors absorb those explicit
logarithms. This correction changes no claimed power exponent.

No blocking gap was found at these stated scopes. The cheap correction
makes the original and modified complete mixed-norm targets equivalent
up to a row-size term; cancellation of the residue functional alone
does not prove either norm. The primitive continuous family, growing
residue labels and complementary row space remain open. The exact
finite ideal/Euler fixtures were also replayed under Python -O in an
isolated export; their role is coefficient verification, not a proof
of an infinite analytic estimate.
