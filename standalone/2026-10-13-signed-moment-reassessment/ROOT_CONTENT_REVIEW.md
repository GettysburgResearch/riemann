# Root reconstruction of the trace, finite repair, and contour

Reviewer: root agent. The signed-family agent authored the signed-trace
and moving-contour notes. The historical-obstruction agent authored the
historical note and its HC1--HC6 application. Root independently read and
reconstructed those arguments, while proposing directions and requesting
scope checks. The verdicts below concern their stated component results.

Root also proposed the normalized-product converse for the determinant
model and helped develop its analytic argument. Root is therefore a
co-contributor to that part of the causal/determinant note, not an
independent reviewer of the whole note. Its separate reviews disclose
their own scope.

## Exact files reviewed

| File | SHA-256 |
|---|---|
| SIGNED_TRACE_OBSTRUCTION.md | 4e557f9ff04e88cdaea099c90a0c7c4420b44487f9ddc64a7c2649d8b1bb01b3 |
| MOVING_CONTOUR_WINDOW.md | 37407e4381ae6e056479c2847fad047e99ea9735156000983666361fc00b8412 |
| HISTORICAL_CONNECTIONS.md | 167525a54479a786117e72e09e7201927e8861b07bc562707fd36b32f22efa45 |

These are content hashes. The later publication record binds unchanged
bytes to the frozen source commit and does not silently extend these
verdicts to a changed proof.

## 1. The native signed-trace refutation

**Verdict:** accept Theorem 1.1 as a refutation of the exact unfiltered
CT1 contract at every fixed order, with the proof's full real-cutoff
quantifier and its stated row weight. This supplies no counterexample
to the actual physical moment.

I read CT1 and SC1--SC4 at PR #911 commit
2f8b6a3898a722d0602a91dea73bac344a3bb7dd and compared the entire
trace definition. The common short cutoff really is \(Y\), even at
shorter eventual column lengths. The source does not put the physical
norm weights inside CT1. Its original replacement of Euler factors by
short polynomials is asserted only after the complete coefficient filter.

The fixed cross-incidence \(q_{\{1,k+1\}}=P\) is permitted. Its row
multiplier is \(1_{(u,P)=1}\); no change to fixed \(S\) occurs. The
finite small-prime deletion makes the local numerator and denominators
uniformly nonzero in the proof's auxiliary half-plane.

I reconstructed the local two-slot factorization. After extracting
\(1-q^{-2s}\), the residual local expansion starts at degree three.
The omitted row primes require the inverse factors explicitly present
in the proof. Their product is bounded by \((Nu)^\delta\), which the
Schwartz row measure absorbs. The complete residual trace is therefore
holomorphic on the fixed scaled disk and has polynomial growth.

At the real anchor the right polynomial is the complex conjugate of
the left polynomial, while every residual local factor is positive.
This gives positivity on the complete row set at that point only.
At a good rational prime \(p\), the norm-\(p^2\) coefficient is
\(-\nu((p))\) in the inert case or \(+\nu((p))\) in the split case.
All other ideals of that norm have zero Möbius coefficient. Hence
the two adjacent real cutoffs force a polynomial unit-row lower bound.
This does not discard other rows at nonreal frequencies.

The interpolation constants are consistent: the sum of Lagrange
weights costs at most \((10e)^{n-1}\), and the radius-four Cauchy
remainder costs \((5/11)^n\). With \(n=O(\log Y)\), both the
remainder and the propagation loss have the stated polynomial scale.
The unconditional prime-ideal theorem then gives positive exponential
growth on \(1\le x\le5/4\), since \(-\cos(2x)>0\).
I personally opened the cited Omar primary reference and checked
the classical prime-counting statement; no critical-strip zero-free
assumption enters.

For higher orders I reconstructed the weighted half-plane argument.
For each fixed \(Y\) the full trace is bounded on the polyhalf-plane.
Dividing by \((1+s)^J\) permits each maximum principle with a finite
boundary supremum, even though the original fixed-\(Y\) bound grows
rapidly as \(Y\) increases. Sending the unused real parts to \(Y\)
costs a fixed power, while the additional slots differ from one by
an exponentially small quantity uniformly in every row.

The common-conjugate tube remains negligible: its pair real part
is at least \(k^2\cos(2\kappa)-k(k-1)>0\); the degree-three errors
are summable. Thus the large weighted supremum must occur in the
complement. The proof establishes a native signed trace lower bound.

Review corrections requested before acceptance were the missing
addition sign in the two-slot error formula, explicit treatment of
\(k=1\), and clarification of the real rather than lacunary scale
quantifier. All are present in the hash above.

## 2. Historical synthesis and finite compression

**Verdict:** accept the note as source-qualified historical comparison
and HC1--HC6 as consequences of the specified prior collision theorem.
This verdict does not reprove every historical theorem or rerun its
computations.

The Newton, completion, bandwidth, CRT, and collision comparisons
identify the particular quantity each cited source leaves unpaid.
The bandwidth map exceeds its input exponent below one; the CRT
translation distinguishes the local distribution from the short
physical row measure. The note does not claim that every old
representation fails or that a large selected signed component
lower-bounds the complete moment.

I read PR #916's PROOF.md at
dd70e580a5ffdbe5b140784ba6cebd173cb84792, including its local
coefficients, finite reconstruction, and sharp kernel mass.
The new historical note credits those statements rather than
claiming their rediscovery.

For HC1, an ideal monomial removed from the coordinate norm box
cannot return under multiplication by integral ideals. Applying
that projection to the exact local coefficient identity therefore
permits the finite collision polynomial in the entire Mellin integral.
Different left and right phases do not affect the formal convolution.

The critical mass bound is the inverse-kernel part of PR #916.
It remains valid for the original \(S\): every additionally
deleted small-prime inverse-kernel absolute series converges at
\(t=q^{-1/2}<1\), so those finitely many local sums can be restored
as one constant. No positivity claim about the forward kernel
at those small primes is required.

Finally \(\prod_iNd_i\le Y^{2k}\) gives precisely the displayed
subcritical factor \(Y^{k(1-2\sigma)}\). This controls the finite
collision polynomial alone. The note correctly does not pay the
short-polynomial row trace or another incidence sum with that bound.
It also correctly declines to transfer the old tube decomposition
to a different integrand.

## 3. The moving-contour window

**Verdict:** accept the uniform factor bound, its sharp order
thresholds, and the conditional moment implication. The native
positive short-polynomial premise remains unproved.

The upper bound needs only a uniformly summable cubic local
remainder and the fixed-field prime count. Partial summation
reduces its quadratic cost to

\[
\log\log Y+\frac{e^{a_Y}}{1+a_Y}.
\]

The estimates remain uniform when \(a_Y\) varies across the
whole stipulated interval. Finitely many small-prime factors
have bounded denominators; local numerator zeros cause no
problem for this upper bound.

For necessity on the factor, the unit-row pair coefficient
\(\gamma_p=k^2+k(k-1)\Re(\nu(p)^2)\) satisfies
\(k\le\gamma_p\le k(2k-1)\). The top prime interval has a
uniformly negative cosine and weighted mass comparable to
\(e^{a_Y}/a_Y\) on the relevant sequences. The moving-interval
prime-theorem error is controlled by the stated uniform
remainder, including when \(a_Y\) is a fixed fraction of
\(\log Y\). The lower prime portion is negligible at the
polynomial threshold. This proves necessity for the factor,
without assuming the same behavior of the signed trace.

In the conditional incidence calculation the auxiliary
divisor loss \(\eta>0\) keeps the partial-summation constant
uniform as \(\sigma_Y\) tends to \(1/2\). The identity

\[
D^{2k\sigma_Y}Y^{k(1-2\sigma_Y)}
=D^k b^{k(1-2\sigma_Y)}
\]

gives the promised conditional power. The arithmetic premise
uses literal sharp norm truncations, all independent frequencies,
and moving exclusions. It is explicitly not deduced from a
smooth moment by an unproved endpoint adapter.

## 4. Validation boundary

The new conclusions are analytic arguments with the hypotheses
listed in their proofs. Source hashes authenticate the objects
read. They are not numerical evidence for a limiting theorem.
No prime search, finite zero census, asymptotic fit, upstream
formal replay, or human peer review was performed here.

The native generalized moment, its required signed correlation,
and RH remain open after these accepted component arguments.
