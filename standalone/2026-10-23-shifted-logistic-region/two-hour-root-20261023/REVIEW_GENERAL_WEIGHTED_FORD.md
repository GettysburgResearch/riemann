# Independent source audit of the weighted Ford lemma

23 October 2026. Scope: equations G1--G8 in
`../two-hour-global-20261023/GENERAL_WEIGHTED_FORD_DETECTOR.md`, read
before the later Poisson-kernel zero-count refinement. This receipt is
not a review of later edits, an infinite-tail arithmetic certificate,
or the final global assembly.

The reviewed source SHA256 is
`c52fa826706a26aec19cf0ed448ca4944dd86ad45ec67cc69da106fef5e6bf50`.

I compared the displayed derivation with the extracted corrected Ford
arXiv:1910.08205v5 PDF, sections 4--7 and 9, including the source formulas
4.4--4.6, 5.3--5.4, 6.3, 7.2--7.8 and 9.1--9.7. The proposed argument
does not rely on the inconsistent printed implication after 9.3 or on
the printed 9.6 remainder expression.

The general-theta transform and the H(R0) majorant are the original
algebraic identities. The half-disc boundary proof gives the compatible
c5=(4/pi^2)(c4-1/R0), so the retained count coefficient is -4/R0.
The required condition is lambda<=1/[2(R0+1)]. It is not legitimate to
improve c4 alone and leave an independently chosen c5 in that calculation.

The proof of the Euler-product smoothing inequality uses only P>=0
and b0=1. It is valid for the new finite degree, as is the nonnegative
left Dirichlet sum. Nonnegative b_j are also needed when applying the
individual upper bounds and discarding the local-count term. The exact
degree-12 polynomial satisfies all three requirements.

At q=jt, the source outside-height estimate and the interval zero count
combine with coefficients .8664+4*.59231=3.23564,
1.772+4*.886=5.316, and 5.77+4*2.591=16.134. Replacing log q by
h_j=log(q+1) is favorable. Adding the explicit-formula remainder gives
3.5691 h_j+5.316 log h_j+17.934, with a separate 1.8 zero-frequency
term. Thus the frequencywise version is licensed without a restriction
j<=4. The one chosen zero can be retained even if the count used for
the unfavorable bound includes it; this only weakens that bound.

The cotangent loss in G8 has the correct unfavorable sign. At the same
global minimizing zero, lambda=B/log(Kt+1) provides the full local strip
at every center. Finite verification covers any lower heights, while
the published Littlewood input ensures existence of the finite minimum.

The shifted Revers envelope covers the entire smoothing line. The larger
10^-7 error for log v>=60 is consistent with D/v<2*10^-8 and with the
Lipschitz estimate; the old 10^-10 allowance was only valid above70.
An exact elementary check of these inequalities is still required in
the new endpoint checker.

Verdict: no analytic defect found in G1--G8 under their stated hypotheses.
The G11 endpoint enclosure and its infinite-tail monotonicity also check:
the signal increases as eplus decreases, and every adverse resource
divided by h0 or h0^2 decreases under the displayed derivative bounds.
Independent endpoint arithmetic, the complementary
logistic rectangle, and an exact-commit assembly review remain separate.
Any replacement of G6 must receive a separately identified review.
