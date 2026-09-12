# Review request: full heat-energy asymptotics, not an RH completion

Review the separately labeled component manuscript at its published commit.
Do not treat it as canonical mathematics or an independent acceptance of #842.
The remaining upper bound OPEN-E is a substantive unproved assertion.

## Principal checks

1. Source normalization and fixed shift. Each positive-ordinate zeta zero maps
   to z=gamma-i(beta-1/2) and a=1+z^2. Group distinct a before squaring the
   sum, and retain both nodes from any nonreal quartet. Check x^2-3y^2 in (2),
   reciprocal summability and Q=xi'(3/2)/(2xi(3/2)). No finite-height zero
   verification is required to put these shifted rates in Re(a)>0.
2. Infinite integral. Prove (9) before interchanging either series with the
   complete time integral. It must pay the SMALL-time endpoint as well as
   infinity. The bound uses the sum of integrated absolute values, not merely
   convergence for fixed t. h^(n) cannot vanish identically because its
   integral predecessor is nonzero and h decays.
3. Sharp growth. In (16), equality at the maximum requires identical rates,
   not merely conjugate ones. For D_*>0, finitely many rates attain the maximum
   since their angular ratios tend to one. Separate the entire infinite pair
   set into a finite square and its complement, yielding one strict gap below
   R^2. Multiplicity enters C_* quadratically. Verify no cancellation of the
   surviving positive diagonal is possible. In the real case, use dominated
   convergence rather than assuming a uniform gap away from one.
4. Cofinal criterion. False RH gives eventual STRICT increase, not merely a
   positive limsup of growth. This is what lets arbitrarily late downward
   steps suffice. The assertion is not that those steps have been proved.
5. Log-time identity. Check the powers of t, the factor 4^n/(2n+1)!, and the
   n+3/2 in (20). Establish H1 from the two neighboring norm identities and
   eliminate the cross term by cutoff integration. Dropping V_n would reverse
   the needed bound. The optional Mellin transform uses principal rate powers.
6. The arithmetic formula is a signed complete formula. Retain its pole term,
   the paired numerator at the archimedean origin and every prime power.
   It specifies the same h but does not produce an upper energy estimate.
7. Synthetic control. Verify E_n in (27) from all nine ordered rate pairs.
   This positive decreasing kernel violates eventual descent and prevents a
   generic inference from self-decomposability. It is NOT the actual xi law.

## Dependencies

Classical strip/symmetry/entire-xi facts, Hadamard factorization, gamma integral,
Laplace uniqueness and Fourier-Plancherel are named. The source-derived
order<1 and the sum/integral interchanges are included. The parent's new
positive-process theorem is interpretation only, not a load-bearing input to
HE1--HE4. The #881 similarity objective is different; no adapter is presumed.

## Evidence and omissions

The standard-library checker reconstructs finite Gaussian-rational identities
and complete gamma integrals for declared finite exponential sums. Its two
integral calculations are same-author controls, not independent proof review.
No actual E_n, V_n, asymptotic cutoff, new xi zero or native descent is computed.
The positive-rate model and nonreal-rate model are deliberately declared
controls, not surrogates silently substituted for the source.

An accepting source-integral engine for arbitrary derivative order, an
unbounded native energy upper bound, and a proof of the Stieltjes property
are NOT supplied. No theorem is delegated to the reviewer as a routine
missing lemma. A useful independent review would reconstruct the complete
pair-gap proof from (1)--(3) without reading the author's calculation first.
