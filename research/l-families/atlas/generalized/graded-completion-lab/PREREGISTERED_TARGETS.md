# Six-hour completion laboratory: predictions before producer execution

Status: research targets and analytic derivations awaiting a complete proof and replay.
Scope: the existing S3 coherent graded source and its even nontrivial Lie generators.
Sources: PR769 head `7b320b3a9a55a16e73d99dd9bbab5bf592d50c93`, especially
`koszul-analytic-parent/FINITE_RESONANT_COHERENT_POLES.md` and
`koszul-analytic-parent/CONSTRUCTIBLE_POLE_CLEARING_SOURCE.md`.
What was run: source reads only when this file was first written; no new producer.
Smallest gap: authenticate the source characters, prove the limiting source and
analytic normalizations, and check the derived coefficients independently.

## Source and exact multiplicity prediction

For the actual Lie module M_n write A_n,B_n,C_n for trivial, sign and standard
S3 multiplicities, and a_n=B_n+C_n. This is the dimension of the (-1)-eigenspace
of a transposition on M_n, not on the original Segre grade R_n.

For every even n>=2 the equivariant PBW inversion predicts the exact identity

    a_n = (1/(2n)) sum_(d|n, d odd) mu(d) 2^(n/d).

The initial values at n=2,4,6,8,10,12 are 1,2,5,16,51,170. The cancellation
of all even inversion divisors improves the exponential remainder from a
generic 2^(n/2) bound to an odd-divisor 2^(n/3) bound.

## Two actual finite-field panels

Reuse E:y^2=x^3+x and D:v^2=-4-27u^4 over F7. Both elliptic polynomials are
P_7(T)=1+7T^2. Frobenius squaring gives P_49(T)=(1+7T)^2; it does not require
a new count over F49. An independent seven-element enumeration must check
the initial traces and both infinity conventions.

With K_N the pure added multiplier after removing the degree-two factor,

    K_(7,N)(z)  = product_(even 4<=n<=N) (1+7 z^(2n))^a_n,
    K_(49,N)(z) = product_(even 4<=n<=N) (1+7 z^n)^(2a_n).

These have the exact finite identity K_(49,N)(z^2)=K_(7,N)(z)^2.
Each coefficient stabilizes in N. The predicted analytic radii are respectively
1/sqrt(2) and 1/2. The actual cohomological trace-class threshold remains 1/2.

In x=z^4 for F7 and x=z^2 for F49, the predicted scalar forms are

    K_7 = (1-4x)^(-7/4) A_7(x),
    K_49 = (1-4x)^(-7/2) A_49(x),

with A analytic and nonzero on a disk strictly larger than |x|<1/4.
Consequently critical finite products should grow as positive constants times
N^(7/4) and N^(7/2). These statements concern K_N, not the unnormalized Euler
function, whose fixed factor may vanish at the boundary point.

## Independent and hostile controls

* Compare direct equivariant PBW inversion with the odd-divisor formula through n64.
* Compare finite product expansion with the recurrence from its formal logarithm.
* Check stabilization and the exact field-extension/substitution identity.
* Reject the comparison with the grading variable incorrectly held fixed.
* Use rational logarithm intervals for finite critical products; no floating-point
  fit establishes a growth exponent or a radius.
* Keep actual finite-grade cohomology and its fixed source norm separate from a
  scalar analytic continuation.

## Adaptive next question (not an established result)

Under further constant-field extension F_(7^r), odd r retains trace zero,
r=2 mod4 gives two negative real eigenvalues, and r=0 mod4 gives two positive
ones. Test whether this yields a complete scalar convergence/critical-growth
classification while the same source operator retains its trace-class threshold.
At positive-eigenvalue extensions the critical finite product may decay rather
than grow; finite zeros and an infinite-order limit must not be confused.
