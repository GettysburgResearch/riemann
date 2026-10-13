# Root reconstruction of the conductor and native structural lanes

**Reviewer:** root researcher, same team. I authored the short-trace
composition and the finite-horizon necklace application, helped direct
the other lanes, and made assembly decisions. This is not an independent
review of my own proofs or an external mathematical certification.

**Frozen files reconstructed here:**

| File | SHA256 |
|---|---|
| `CONJUGATE_PAIR_CONDUCTOR_SIEVE.md` | `220d767a03ed6c61b8e5a3ea34b48a0a2adae92607047fbfa0bb96e5be876ef2` |
| `CONDUCTOR_COROLLARIES.md` | `49d471154fbfb2b8589742a70343f9abfa8e407172648b73f33a14d5f3e3031d` |
| `PRIME_DEGREE_COHERENCE.md` | `2290ce3d8d24f832259b3d701607beb125ceb5111f86b39d82be200eea1c27fb` |
| `SHORT_FACTOR_NONSMALLNESS.md` | `0af49f68a90bc19253e6543abd2e8d8af295a2bb133c5ebb59686e516655a935` |
| `EULER_TRACE_RESONANCE.md` | `c8931a93f3fc47805143ab4074ca4e315656a87e58abd5e0e7ba59c03079fb10` |

**Verdict:** the stated deductions pass my reconstruction, with the
source and scope qualifications below. The imported fixed-order sieve,
the prime ideal theorem and classical Hecke analytic machinery are
named inputs, not results proved by this review.

## 1. General-order conjugate-pair reduction

I read the complete manuscript and directly opened de Faveri's primary
version arXiv:2610.04045v1, especially Theorem 1.1, Lemmas 2.4, 3.1,
3.3, Proposition 8.1 and Section 9. I also read the exact #929 conductor
adapter, preserved in this packet.

The decisive order-independent structure is the pair
\(\chi_q(a)\overline{\chi_q(b)}\), not the notation \(ab^2\) from
the cubic case. In order six it is \(ab^5\). Opening the square and
separating the common squarefree divisor retains its nonunit masks.
Primitive Poisson on the conjugate factor reflects the remaining dual
character to the orientation of the \(a\)-character. The two then
combine as \(\chi_h(ae)\), with zero at a nonunit still zero.

I checked the use of the general root-number lemma: both residual
indices are squarefree, so the additional higher-power cross factors
in that lemma are one. This is the reason that the claimed separated
coefficient vectors exist. It would not justify the same statement
for arbitrary higher-power residual indices.

The final manuscript explicitly uses Cauchy for the two potentially
different Mellin coefficient vectors before applying the positive
all-row norm. The divisor labels from coprimality removal remain exact
up to that step. Their eventual positive multiplicities are bounded by
fixed-order divisor functions; no arbitrary row-dependent coefficient
is inserted into an unproved native inverse estimate.

For the unrestricted row norm, \(x=e^n x_0\) is a unique decomposition
without a condition \((e,x_0)=1\). The literal coefficient mask is
\((q,e)=1\). The three convergent ideal series have exponents
\(n,n-1,2\), all greater than one for \(n\ge3\). This gives exactly
the four displayed all-row monomials.

Substitution of
\[
U=AQ^2P/(B\Delta^2),\quad V=Q/\Delta,
\quad \text{prefactor }B\Delta/(QP)
\]
gives the four monomials in Section 3. All the residual powers of
\(P,\Delta\) are nonpositive, and the first \(AQ\) is absorbed by
\(A^{1-1/n}B^{1/n}Q\) when \(A\le B\). This checks both the
normalization and the asymmetric exponents; an exponent-only test
would not have supplied the preceding character reduction.

## 2. Moving background and native accounting

The background is taken to be its primitive associate before its
coefficient zero extension is used. Its good conductor is disjoint
from \(a,b\). The primitive conductor is therefore \(RNaNb\) outside
the fixed bad set. The infinity type and bad data are fixed, so the
approximate functional equation can be separated with common length
\((RAB)^{1/2+\eta}\) times a vertical polynomial.

The ideal index decomposition \(m=sqr_0^2\), with \(q\) squarefree,
does not impose \((q,r_0)=1\). The fixed \(s,r_0\) factor is an
outer bounded multiplier. The weighted Cauchy sum converges because
the exponent of \(Nr_0\) is \(1+2\eta>1\), and only fixed bad primes
occur in \(s\). The remaining coefficient vector includes
\(\psi(q)\), hence the moving exclusion, with bounded squared norm
on each dyad. Dropping outer restrictions happens only after a
nonnegative square is available.

I independently substituted the AFE length into the four pair-sieve
terms. For \(n=6\) the three nonconstant ratios are
\[
R^{1/6}M^{-2/3},\qquad
R^{1/2}(M/N_0)^{1/3},\qquad
R^{1/4}M^{-5/12}N_0^{-1/12}.
\]
They are all at most \(R^{1/2}\). For fixed background they are
bounded, including the endpoints \(M=1\) and \(M=N_0\).

For the native tuple application, the unit average and fixed ray split
precede the ideal character adapter. The good singleton conductor is
the conjugate pair \(a_+a_-^5\). Every other nonprincipal multiplicity
is frozen in the moving background. Principal prime masks enter the
Mellin row kernel through their deleted Euler factors and are paid by
their divisor-subpower upper bound. There is no pole for a nonprincipal
tuple kernel. The final theorem now explicitly fixes a compact smooth
nonnegative radial row majorant.

The complete column budget counts the principal-mask label with power
two, singletons with power one, and every multiplicity-\(m\) label with
power \(m\). Cauchy and the conductor mean give the singleton factor
\(L\), which combines with the principal-mask budget \(D^kL^{-1/2}\).
Every remaining \(m\ge3\) sum has exponent at least
\(m/2-1/4\ge5/4\) and therefore converges. This reconstructs the
full positive accounting bound, rather than only its two-singleton
slice.

I checked the explicit fourth-tuple incidence: each of its four
column exponents sums to one. Its aggregate exponents are
\((L,M,N_0,G,q_0)=(19/20,1/8,33/40,1/2,41/40)\).
The largest new excess is \(-1/24\); the best stated one-sign
comparison leaves \(+1/480\). These are comparisons of upper bounds
on a feasible pattern. They are not lower bounds for an arithmetic sum,
and they do not supersede stronger signed estimates on different objects.

## 3. Global conductor corollary and the failed five-label improvement

Summing \(AB\) over dyads with \(AB\ll X\) costs \(O(X\log(2X))\).
The fixed-background corollary therefore follows from the pair theorem.
In the standard sextic family, exact local order six has exponents
\(1,5\); the other nonzero exponents have lower local order and are
not all covered. The parallel statement for locally primitive powers
uses the same two-label coverage only at \(n=3,4,6\).

The five-label calculation is an exact bound-envelope argument.
At \(Q_1=\cdots=Q_5=X\), each listed best mean retains an
\(X^{3/2}\) ratio above the \(X^5\) family volume. Thus these
inequalities cannot certify an exponent below \(11/8\) in the stated
weighted uniform objective. The elementary choice of the largest label
gives the matching \(11/8\) upper bound. No conclusion about the
true minimum arithmetic mean follows from that coincidence.

## 4. Complete signed prime-sector lower bound

The finite partition identity is essential: \(Q_k\) can be negative
at an individual row. A lower bound on a selected positive set of rows
would not by itself lower-bound its complete row sum.

I checked the partition coefficient
\(\prod_C(-1)^{|C|-1}(|C|-1)!\), the cancellation for every equality
partition, and the absolute coefficient sum \((2k)!-1\) away from
the singleton partition. A nontrivial partition has at most
\(2k-2\) singleton slots. Each other power sum is bounded by \(V\).
With \(U=1+V\), scaling by \(|B|/\sqrt U\) proves the stated Young
inequality and its explicit constant. The argument covers \(k=1\)
and \(V<1\).

For the prime-selected polynomial and \(\nu=1\), a row generated
by the sixth power of a copying prime deletes at most its one matching
column prime. Its amplitude is at least \(L_D-1\). This remains true
whether the copying prime is smaller or larger than the column scale;
there is no hidden \(h<6\) assumption. The prime ideal theorem gives
enough copies and enough column primes. The row-summed error is
\(O(HD^k/(\log D)^k)\), whereas the main lower term has power
\(D^{2k+h/6}\). Their power difference is \(k-5h/6\).

The final prose correctly restricts the conclusion to removing every
repeated column. An undefined graph-connected selector would be a
different restriction and is not covered. Primality is an additional
arithmetic column selector; the full composite native moment remains
unrefuted.

## 5. Deformation, tangent, and exact prime-rooting

For the deformed coefficient \(\mu_K^2z^\omega\), the factorization
\(F_z=\zeta_K^zE_z\) has an analytic nonzero \(E_z\) near one.
The chosen disk around \(-1\) excludes every other integer and every
possible local zero at one. Thus its noninteger local order prevents
holomorphic continuation across one. The nonnegative fixed norm test
has nonzero Mellin transform there, so a power-saving smoothed sum
would give precisely the forbidden continuation.

At \(z=-1\), the derivative has a nonzero
\((s-1)\log(s-1)\) term. The sign in the differentiated coefficient
is \(-\mu_K(n)\omega_K(n)\), which is harmless for the asserted
absolute growth obstruction but is written correctly in the proof.

The moving prime deletion is
\(O(D^\epsilon(D/N\mathfrak r+1))\), and is empty if the copying
prime exceeds the support. Choosing the preliminary exponents
strictly below \(h/6\) makes it negligible on the arbitrarily large
scales furnished by the Mellin contradiction. This proves the limsup
statement without a Selberg–Delange asymptotic.

Finally, prime-rooting uses
\(\sum_{p\mid n}\log Np/\log Nn=1\) on squarefree ideals. It keeps
the exact \(p\) exclusion, all nonunit zeros, and the whole composite
companion. The final wording identifies its unit-companion part with
the untwisted prime polynomial only at \(\nu=1\); for general
\(\nu\) it retains \(\nu(p)\). No estimate is inferred merely
from this identity.

## 6. Analytic short-factor lemma and first-order resonance

I checked the ideal multiplicity bound by the ordinary divisor function,
the explicit \(505/2304<1/4\) anchor, the product derivative estimate,
and the complex interpolation remainder. The divided-difference simplex
formula is valid for complex nodes; it does not use a false real
mean-value assertion for a complex-valued function. The single successful
node concerns the product of all factors, so separate zeros cannot defeat
the composition.

For the original Euler resonance I reconstructed the fixed legal mask,
positivity of every actual paired row, the two exact logarithm
inequalities, and the top-prime versus small-prime comparison. Its
critical-line consequence already holds at \(k=1\), illustrating
that failure of an unfiltered contract says nothing by itself about
the corresponding norm-filtered second moment.

## 7. What was run and what was not

I ran all three newly authored finite diagnostics from their repository
copies under ordinary Python and `python -O`. Their reports are
byte-identical in each pair. The native diagnostic was rebound and
rerun after its two wording corrections; its arithmetic code was
unchanged. Exact source transports were checked by both SHA256 and
Git blob identities during assembly.

These are exact finite algebra and provenance checks. They do not
verify de Faveri's proof, prime ideal distribution, Hecke functional
equations, an infinite moment, or a zero-free region. The complete
source-qualified written arguments are the mathematical evidence.
The separate review files disclose who authored, suggested or checked
each component. Final Git-commit receipts bind the reviewed bytes;
they are not an additional theorem.
