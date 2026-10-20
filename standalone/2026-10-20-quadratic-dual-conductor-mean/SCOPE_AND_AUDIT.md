# What is improved, what was audited, and why 0.874 is not claimed

## 1. Claims and dependencies

| Claim | Mathematical content | Imported input |
|---|---|---|
| QD-LOCAL | The varying sextic exponent 1 becomes quadratic on the dual side; fixed matching/nonmatching factors retain their different costs | DR finite transform; exact coefficient derivation from #1010 |
| QD-MEAN | Conductor-uniform completed-series second moment H_sigma(K,C), including the three split regimes and every dual cube power | DR general functional equation; DF sextic large sieve; GL quadratic large sieve |
| QD-SUM | X^(2p)H_p(K,C) for the smooth cubic Gauss sums | QD-MEAN and a common finite-order Hecke zero-free half-plane |
| QD-MARK | A^(2p)B^2 H_p(KB,C) with an actual coherent divisor mark and all zero-only masks | QD-SUM; exact multiplicativity and positive-norm triangle |
| QD-ALLROWS | The complete centered sixth-power-free row estimates, including all powerful parts and their residues | QD-SUM, QD-MARK and the audited pointwise convexity input |
| QD-SCALAR | Exact parameter inequalities, exponent identities, and local type bookkeeping | Standard-library finite checker |

These are proposed analytic arguments requiring independent review.
The finite checker is not an independent analytic referee. The original
DR theorem is used at its general periodic-twist scope. DF and LIU are
preprint dependencies; their full proofs were not independently rebuilt.
GL's full proof was not rebuilt either. No GRH-dependent result from
DR, no proposed infinite-order theorem from #1009, and no conclusion
from the repository's still-open mixed mean is used.

## 2. Audit of the previous transfer

The #1010 packet at a1afee36313ff5994dad7b97983948113571965e was fetched
at its immutable GitHub commit and checked against the supplied archive.
Its PROOF.md blob is 9853b589ca3906fd14702f1383eb2de3647ddfa4.
The old ordinary and optimized finite replays were run again in this
continuation. No repair to the old finite conductor identity was needed.

The analytic audit focused on the interfaces consumed here:

- The source's twist is psi(lambda^4 nu). On nu=lambda^(-3)ab^3 it
  really is psi(lambda)psi(a)psi(b)^3. Cubing the finite character is
  necessary; applying the cubic-only Lemma 5.4 literally would be wrong.
- The entire dual a_star series, not the specially cube-inverted cubic
  level series, is required. Its b^3 replicas have not been dropped.
- At a nonmatching prime the transform has mass q on units, not sqrt(q).
  That loss survives in (8) and is recovered only by a different average.
- On the new varying conductor the dual is quadratic, but on the fixed
  matching part it is Ramanujan. Treating both as arbitrary primitive
  quadratic characters would lose the C F0^(2sigma) term in (11).
- The reciprocal must be uniform in conductor. The source common
  half-plane, not an unspecified constant for each individual character,
  is what licenses the Borel--Caratheodory/three-lines argument.
- A finite character on primary generators has the requisite bounded
  bad-prime adjustment to be an actual Hecke character. Fixed finite
  partitions at 2,3 must precede the large sieves.

The new proof makes these interfaces explicit. This is an author-side
reconstruction, not a claim that a different agent or human reviewed it.

## 3. Comparison with the previous estimate

For f=1, #1010 followed by summation of individual squared bounds would
cost

    X^(2p) C^(3-2p+epsilon).

The new conductor average costs

    X^(2p) C^(2-7p/4+epsilon).

At p=11/24 these conductor exponents are 25/12 and 115/96. The comparison
is for a positive family mean, not a stronger estimate for every row.
A more informative generic baseline is the sextic sieve at X=C=U:
after dividing each sum by sqrt(X), it costs U^(7/6+epsilon), whereas
the specific Gauss-coefficient estimate costs U^(107/96+epsilon).
That is a 5/96 power saving in this specified squared norm.

The short-mark example in ALL_ROWS_AND_MARKS.md has centered RMS exponent
109/160, compared with 153/220 for the Euler-only version of the same
averaged argument. At the Euler endpoint the powerful series in the
marked proof is borderline; its truncated sum is U^epsilon by the
powerful-ideal counting bound. Thus that comparison remains valid with
prescribed small powers. No estimate on the line Re(z)=1 is assumed.

Using B_flat rather than 7/8 slightly increases the conductor exponent
in H but lowers the X exponent. For the displayed Y example the combined
RMS exponent improves from 0.68125 to about 0.681237118981814.
This tradeoff is expected when shifting farther left. It is another
reason not to identify one isolated exponent with a zero-free boundary.

## 4. Explicit attempted transfer to the boundary consumer

The desired original norm in #1006 is

    sum_(Nu~U, u sixth-power-free) |M_u(D) S_u(N)|^2,

where M has the literal Mobius coefficients and S has the literal plain
coefficients, both normalized by the square roots of their lengths. The
hypothesis sufficient for 437/500=0.874 is U^(6/5+epsilon) on the WHOLE
robust witness polygon

    1<=r<=3/2, 0<=m<=1/2, 3/2<=r+m<=2,
    D=U^r, N=U^m,

with its specified small neighborhoods, all profiles, heights and masks.
This remains a hypothesis, not a theorem in this packet.

Our marked coefficients are instead

    sum_(av=n) b_v g_tilde(n) W_A(Na/A)W_B(Nv/B).

They are not the original truncated Mobius/plain convolution. A Gauss
factor and a functional-equation reflection cannot simply be removed
from a norm bound. The complete source's Poisson representation also
has pair-conductor weights, common-divisor allocations, outer
cross-component terms and natural nonunit zeros. Its signed projections
are not positive norms to which Minkowski applies automatically.

There is a direct numerical warning even before that missing transfer.
Normalize the new marked sum by sqrt(DN), and generously set A=D,B=N.
Our bound is then

    D^(2p-1) N H_p(N,U).

At beta=7/8, D=U and N=U^(1/2), this equals U^(11/6), not U^(6/5).
This calculation is an upper-bound cost for our actual Gauss-marked
expression, not a lower bound on either expression and not a theorem
that a sharper transfer is impossible. It shows that the complete
Minkowski-treated short mark cannot be declared adequate by quoting
115/96 from the unmarked estimate. The exact checker rejects that
misidentification as a deliberate false-consumer control.

The source in #1006's CUBIC_CORE_ALL_POWER_TRANSFER.md was inspected
again: it correctly carries cross-component cubic twists and all
powerful row parts, but it only bounds the low-cubic-core signed
sector. Its complementary high-core form has not been identified with
(24) or (26). No source sum, variance term, or principal residue is
silently replaced by our better-behaved average.

## 5. What a further improvement must retain

The new useful resource is a conductor average with an explicit
moving fixed-level price, rather than a pointwise bound followed by a
triangle in every conductor. To activate the original consumer one
still needs a legal comparison to the complete signed physical source
and a stronger treatment of its Mobius-marked divisor correlation.
The present proof uses triangle in that mark and makes no cancellation
claim for it. Its angular degree is zero, so the original source's
larger profile interface cannot be assumed for free either.

A common-zeta shortcut also needs an additional argument: the completion
here is psi_f^3 theta_c, which varies with c. Its zero-free input is
imported, not generated by the new second moment. This packet does not
create a new common-zeta pole contradiction.

Thus the remaining status is precise: a stronger structured mean with
complete norm-row accounting, but no new numerical boundary for zeta,
for the finite-order Hecke family, or for all L-functions. The original
0.01225 native-inverse-exponent milestone has not been established.
No RH proof, literature-wide priority claim, or integration approval
is made. Parameter optimality is asserted only for the displayed
six-monomial two-piece resource, not for possible new analytic estimates.
