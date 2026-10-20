# Independent review of the joint unequal-cutoff pair

20 October 2026. Reviewer: the type-I subagent, independently of the
boundary subagent who wrote the proof. Verdict: no unresolved defect
found in the stated source-dependent mean or its free-column consumer.

Reviewed file: ../mixed/JOINT_PAIR_UNEQUAL_CUTOFFS.md, SHA256
36277fce41d0c5d425b534b885cd08cd3444a33fbeb49dfa45303f1c13d195c7.
This review uses the previously reviewed exact pair and finite-profile
reflection. It does not constitute an independent proof of the imported
large-sieve theorems.

The quadratic row family is explicitly the native residue family
\(\xi_S=(\cdot/S)_2\), not an arbitrary conductor-by-conductor
choice. Goldmakher--Louvel's primary-generator bridge is recorded
in the separate source audit. The sextic partner is exactly
\(\eta_2=\chi_{6,S}\). The de Faveri n=6 operator bound permits
the stated squarefree coefficients and positive row restrictions.
Fixed ramified profiles and ray sectors are admissible.

In the original integral, fixing r before the S sieve leaves only
an allowed arbitrary column coefficient. At fixed cube d, the
factor \(\xi_S(d)\) is a bounded row multiplier with its zero;
discarding it inside the positive norm is legitimate. Minkowski's
four cube sums have exponents
\(-1-3\delta,-5/2,-3/2,-9/4\), so all converge in the stated range.
This checks the full completion, not just d=1.

The reflection keeps S, exchanges 0 and 2, reverses the included
angular sign, and produces only k dividing r. Thus coprimality
survives. Its squared moving factor is the one in (JQ9).
Every R exponent of both F_j is greater than 2delta, so the
weighted divisor sum costs \(R^{-2\delta}F_j\) by partial
summation. This holds at all R,H, including the smaller divisor
rows; a calculation only on R=H would not have sufficed.

The original terms and coupling factors obey (JQ11)--(JQ12).
One especially useful independent check is that
\[
 RH^{1/3}V^{5/6-2\delta}
 =c_2 R W^{1-2\delta}
 =R^{16/11-12\delta/11}H^{12/11-20\delta/11}.
\]
This identity holds for all R,H. At R=H, these terms dominate
every other term for \(0<\delta<1/6\); their nearest row competitor
would cross only at \(\delta=3/17>1/6\).

The two finite conductor suprema are finite before absorption:
the continued source theta functions have a common height degree,
and their constants are bounded on each finite conductor set.
The height normalization can be enlarged before taking the
supremum. The enlarged cutoffs cancel the reflected height power,
and the arbitrarily small divisor loss is dominated by
\((RH)^{-4\delta\theta}\). A fixed large C0 contracts both
normalized partner maps uniformly down to R,H=1.
The two inequalities then bound both suprema before the cutoffs
are removed. There is no circular assumption of the claimed mean.

For the free-column consumer, twisted multiplicativity has the
correct conjugate cubic character. The inverse completed cube
factor is absolutely bounded at \(3\sigma-1/2=1+3\delta\),
uniformly in both conductors and fixed angular order. Cauchy
over at most O(RH) row pairs gives exactly (JQ16). The balanced
exponents and their limiting values in (JQ17) are correct.
The inner coefficient remains a free smooth column, not a prime
indicator or an arbitrary row-dependent arithmetic weight.

The final source-overlap discussion is material and correct.
rStation paper 5 v3 (11.4), after undoing its 1/R label
normalization, gives \(RH+R^2H^2/D\) for this completed sextic
annulus. Combining it with the ordinary original-side sieve
already recovers the displayed exponent 28/11. The new proof
removes that recursion from the dependency chain; it does not
establish a stronger numerical mean than all supplied inputs.
It improves only the direct bound obtained by summing the earlier
fixed-S estimate. The detector's coherent marked edge remains
outside this conclusion.

Polynomial uniformity in growing angular order is proved separately
in JOINT_ANGULAR_UNIFORMITY.md. It is not silently attributed to
the fixed-angular theorem reviewed here.
