# Independent component review of the tail-debiased mollifier

**Pass at the stated source-qualified scope.** Reviewed
`../eisenstein/TAIL_DEBIASED_MOLLIFIER.md`, actual-byte SHA-256
`66415deed8a2c97c89c20049f8dd6d70ff33a41a1666a84ddc0cdcfa58b5a27a`.
This is an internal mathematical reconstruction, not an external referee
report, validation of either entire imported analytic proof, a full mixed
moment bound, or a new zeta region.

I independently reconstructed the exact tail response and prefix gate.
The denominator B_D is a positive squarefree-density quantity; the scalar
counterterm is only logarithmically large. The inverse local weight in
the tail is essential. The complete divisor convolution below D is
unchanged, so the original Gamma-contour zero detector survives for every
original nonprincipal character, including its literal zero extensions.
The product cutoff removes only the unit contribution, giving the
nonvanishing complete tail. The height/profile dependence remains in a
single product profile, as required by the later leading-functional
cancellation. The shifted-contour and terminal estimates remain explicit
imports of the pinned original detector, with only fixed support and
logarithmic losses.

The Euler identity for the positive correction was reconstructed locally:
its remaining Dirichlet coefficients have absolutely summable central
mass, since each local defect is O(Q^(-3/2)). The square denominator
convolution has coefficient mass O(log D), allows all shared primes,
and never divides out an imprimitive zero mask.

I read the literal original source's row-family definitions and zero-slot
TWO-PLAIN theorem around lines 12490--12565 of
`../eisenstein/_source-original-quasi.tex`. Its rows are nonprincipal
inducing characters, with no lower conductor condition in this slot;
the two plain lengths have no restriction apart from the stated bounded
polynomial range. Thus Minkowski really gives the proposed cheap joint
correction norm. An elementary single-plain U+D^2 bound would not suffice.
The unit-scale second plain factor is legal for the unmarked mean.

I also read the pinned rStation paper 8 version 1 Type-I statement. Its
literal leading functional contains v(a)/Na and the plain factor is
unrestricted. Keeping one whole-product profile makes its leading term
zero exactly, rather than assuming dyadic cancellation after different
profiles have been inserted. The fixed numerator-ray restriction and
fixed-bad-prime interfaces remain stated source imports. Summing its
errors gives X^(1/3)D^(2/3), and the normalized adjoint squared cost is
U^(1/3)X^(-1/3)D^(4/3), as claimed. This cost does not settle the full
mixed moment. The triangle-inequality equivalence in the final section
correctly prevents that overclaim.

A fresh optimized replay of the unmodified finite checker passed. Only
`__file__` was redirected to this directory's ignored `adversarial/`
subdirectory to prevent overwriting the author's receipt; the checker
source itself was compiled unchanged. It checked 117 complete exterior
ideals through norm384, 67 low-product unit gates, 238 prime-power Euler
identities and rejected all 3 missing-inverse-v mutations. Its record
hash was `07a436d30f86bafcc6bb9a447e29471c1bfc0fdfe97b389ad453267be9b5ae64`.
These finite checks support the elementary algebra only; the analytic
source gates and the open complete mixed estimate remain separate.
