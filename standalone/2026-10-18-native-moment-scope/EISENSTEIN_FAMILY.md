# Explicit source for the complete nonprincipal-family fixtures

Status: exact source specification and finite replay. No asymptotic estimate
is inferred from the data. This experiment is in addition to, and distinct
from, the complete principal-replica experiment in GAUSSIAN_CONTRACT.md.

## Fixed field, generators and characters

Let O=Z[w], w^2+w+1=0, with the fixed embedding w=(-1+i sqrt(3))/2.
Its units are the six roots of unity. Their images modulo the ideal (3)
are distinct and exhaust (O/(3))^times. Norm-Euclideanity makes every ideal
principal. Consequently EVERY ideal u prime to 3 has a unique generator

    alpha_u = 1 modulo (3).

The generators multiply exactly: alpha_(u v)=alpha_u alpha_v, since both
sides generate u v and are 1 modulo (3). This includes common primes.
Set S to contain the prime ideals above 2 and 3, and define for exterior
prime ideals P

    chi_u(P) = alpha_u^((NP-1)/6) modulo P,

identified with its unique root in mu_6, and set the value to zero if
P divides u. Extend multiplicatively to every ideal column, keeping zero
at nonunits even for exponents divisible by six. This is the usual Kummer
sixth-power symbol `(alpha_u/n)_6`, with its embedding fixed above.

Classical Kummer/Artin reciprocity identifies the values on coprime columns
with the finite-order Hecke character of F(alpha_u^(1/6))/F. We import
that standard analytic identification, not a new proof of class field
theory. Outside S its inducing conductor is the product of the primes
whose row exponents are nonzero modulo six. At S the local classes
F_v^times/(F_v^times)^6 form a fixed finite list, so the conductor there is
bounded by a fixed S-ideal. Thus Q_u<=C_F,S Nu. If a sixth-power row factor
has disappeared from the primitive conductor, its nonunit mask is still
retained in the original chi_u. All infinity types are trivial.

This supplies one explicit fixed family satisfying the source contracts
in PROOF.md. It is not an assertion that every unspecified generator or
local-class choice in another packet is numerically identical. The stated
normalization makes the finite values reproducible without that ambiguity.
The field contains mu_6; it does not contain mu_12, so these values are NOT
the CT reflected theta source.

## Complete ideal and residue-field coverage

`kummer.py` reconstructs alpha_u by solving the exact norm equation
(2a-b)^2=4Nu-3b^2 and testing HNF membership and the primary congruence.
It accepts only a unique solution. Every ideal is its full HNF, not its
rational norm. For a split rational p, the two distinct prime ideals are
(p,B+w) for the two roots of B^2-B+1 mod p. For inert p the ideal (p) has
norm p^2 and residue field F_p[w]/(w^2+w+1). All residue reductions and
sixth powers are exact integer arithmetic.

The fast split-prime root construction is compared with independent brute
enumeration. On every residue of every exterior prime ideal in the small
declared cap, binary-power character evaluation is compared with literal
repeated multiplication. Each of the six character values has exactly
(NP-1)/6 unit preimages and zero occurs exactly once. The complete row and
column ideal caps in KUMMER_CHECKS.json then verify zero extension, primary
generator multiplicativity, all principal sixth-power copies and complete
native coefficient aggregation.

## Full native Gaussian production

The norm coefficients are exact elements a+bw. At a split rational p their
Euler factor is

    1-[chi_u(P)+chi_u(Pbar)]X+chi_u(P)chi_u(Pbar)X^2;

at an inert p it is 1-chi_u(P)X^2. The factors at 2 and 3 are deleted.
This generates ALL coefficients of mu_F(n)chi_u(n) at every declared norm,
including conjugate columns, shared primes and nonunit zeros. The two
signed-int32 coefficient arrays per row have separate portable SHA-256
hashes. Their support is contained in the full principal Mobius norm
support: this follows immediately from the displayed local degrees and
the inert parity restriction, and justifies the producer's shared zero skip.

`gaussian_native.py` uses the SAME fixed tau=1,c=0 Gaussian as the principal
experiment. It reconstructs every row ideal with Nu<=64, evaluates every
norm up to the declared cutoff, and adds the proven complete complex tail
bound (G2). A complex tail of modulus <=T has both coordinates in [-T,T];
that enclosing rectangle is used, including the square-root-three embedding.
The sum of actual |A_u(D)|^(2k) is evaluated with directed arithmetic.

`--replay NATIVE_GAUSSIAN.json` authenticates the complete row cap, reconstructs
the integer source, doubles the cutoff, adds 128 precision bits, and demands
containment in the deposited real, imaginary and moment enclosures. On the
first two scales it additionally sums individual HNF ideals rather than
using norm-coefficient aggregation.

Here the row cap is on u ITSELF. The principal experiment's cap is instead
on b with u=b^6; these are different finite families. The report never
substitutes either family for the other. Neither finite experiment proves
the infinite cofinal moment target, a zero-free half-plane or RH.
