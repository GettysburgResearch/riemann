# Independent review of actual all-order size-two Hankel positivity

Verdict: ACCEPT AH1–AH9 at
`../../operators/ALL_ORDER_TWO_BY_TWO_HANKEL.md`, SHA
`f1a0ac4be55d892708980ae47e05391054e9cd6e30e1ecb907d2b2cfafd463c8`,
and its checker SHA
`14e09f3581bba10f67d2a34f581fa677a0c65ce50f3da187e104023804786f28`.
I independently read the complete source, proof and code, then directly
ran the exact rational checker normally and under -O. Own preserved
`two_by_two_hankel_normal.json` and optimized receipts are byte-identical
to the owner, SHA
`4c0d4237e0ef7158c9eec5d532b2d65042fe26474f9bdf097e2e220211b084bc`.
This replay performs no native root, moment or heat evaluation.

The result preserves the complete actual source: with c3/4 and
`b_n=c^n C_(n+1)(1)`, EVERY n>=0 satisfies

\[
 \begin{pmatrix}b_n&b_{n+1}\\b_{n+1}&b_{n+2}\end{pmatrix}
       \succeq\frac{I}{1125000\,600^{n+1}}.
\]

The first two authenticated real nodes have separation greater than1/500
and both exceed1/600. Their Vandermonde Gram matrix has determinant above
1/250000 and trace below3, hence least eigenvalue above1/750000. Multiplying
the positive selected weights supplies the full head gap in AH4. Every
other complete real-head term is positive semidefinite.

For n>=2, I checked the complete Stieltjes derivative and endpoint payment.
The sharper actual count `N(x)<x log(x)` is essential to the small constant
in AH5; the weaker N<=x² alone would not supply it. It yields total tail
node mass below20c/R. Cauchy–Schwarz applies to BOTH polynomial factors at
each complex node; it does not replace the source term by an absolute
square. Using `1+alpha²<1/(1-alpha²)` gives the complete quadratic-form
norm bound. The exact ratio `1350000/65000^n` is below1/2 at n2 and decreases
for every larger n. This proves the infinite high-order range.

At n0 and n1, I independently expanded both conjugate-pair determinants.
Their exact Schur complements are respectively
`-y²|z|²/x` and `-y²|z|⁴/(x²-y²)`. Their positive rank-one parts remain
positive on every complex vector; the residual negative diagonal prices
are retained. Translating z=c/D with `Re D>=gamma²` and `|Im D|<=gamma`
gives the displayed per-occurrence bounds. Summing BOTH conjugates and
their multiplicities with the complete count yields the whole prices
`4c²/(3R⁶)` and `5c³/(2R⁸)`. Each is less than half its head gap. The
factor of two from conjugate grouping has not been lost or counted twice.

All seven direct hashes, six inherited hashes, nine further inherited
count/source bindings, and the original native census's transitive source
table were checked against current frozen files. The complete count-free
5419 real head, first two native strict-root intervals, strip, paired
product and theta/Jensen count remain explicitly reviewed mathematical
imports. The finite checker replays their source contracts and exact
guards, not the infinite analytic proof itself. Sixteen rational pair
fixtures agree with the polynomial identities; the full identities were
independently established above rather than inferred from those samples.

The determinant is exactly
`c^(2n+2)[C_(n+1)(1)C_(n+3)(1)-C_(n+2)(1)^2]`, so the theorem proves strict
actual complete-moment log-convexity at EVERY order k>=1. It also supplies
positive scalar diagonals at this fixed shift. Larger Hankel matrices,
the universal Hausdorff condition and complete heat monotonicity remain
unproved. No simplicity, cofinal success or RH is inferred.
