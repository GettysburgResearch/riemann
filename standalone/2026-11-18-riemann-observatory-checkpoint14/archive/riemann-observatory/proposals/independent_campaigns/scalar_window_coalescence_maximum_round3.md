# Does complete coalescence maximize the fixed-window error?

Date:2026-11-17. Status: **open for general degree m≥3**, not claimed as a theorem. This continues the proved scalar-window bounds in `unit_circle_scalar_window_round3.md`; no novelty claim or RH transfer.

Let Q=∏_(j1m)(1−q_jz), |q_j|=1, b_n=[z^n]1/Q, A_M=Σ_(n0M−1)b_n(1−n/M)^m z^n. The conjecture is

\[
 \|1-QA_M\|_{H^2}^2\le
 \|1-(1-z)^m A_M^{\rm coal}\|_{H^2}^2
\]

for every m,M≥1. Common rotation is irrelevant. It is proved for m=1,2 in the preceding campaign, with exact quadratic maximum4/M+3/M²−2/M³ and sharp all-M constant5.

## A real obstruction to the simplest proposed proof

For n≥1 and a monomial q^α with |α|=n, write s(α)=#{j:α_j>0}. The coefficient of q^α in(QA_M)_n is exactly

\[
 \Delta^{s(\alpha)}w_n,
 \qquad w_n=(1-n/M)_+^m.
\]

Indeed selecting a subset S of the support of α in Q contributes(−1)^|S|w_(n−|S|), and there are binomial(s,|S|) such subsets. This gives a direct integer algorithm for every Laurent coefficient of M^(2m)‖1−QA_M‖², using w_n M^m=(M−n)_+^m.

For m=3,M=2, the coefficient of q3²/(q1q2), i.e. multi-index(−1,−1,2), in this scaled energy is **−4**. In the energy itself it is−1/16. This was obtained by exact integer arithmetic, not a floating optimization. It follows that the two-root argument by nonnegative Laurent coefficients does **not** extend unchanged to degree3. It is not a counterexample to the maximum conjecture: a function can have negative Fourier coefficients yet be maximized at coalescence.

`experiments/code/scalar_window_laurent_round3.py` computes all coefficients in29 finite cases: m2,M1–10; m3,M1–10; m4,M1–6; m5,M1–3. Negative coefficients occur already at the witness above and in later cases. These finite computations diagnose the proof route; they prove no universal maximum theorem.

## Exact three-root example: a different positivity mechanism

The conjecture is nevertheless true for m=3,M=2. Put

\[
 S=q_1+q_2+q_3,\quad P=q_1q_2q_3,\quad
 \Delta=\prod_{i<j}|q_i-q_j|^2\ge0.
\]

Since e2=P\overline S for unit roots, the four residual coefficients are

\[
 r_1=7S/8,\quad r_2=S^2/8-P\overline S,\quad
 r_3=P(1-|S|^2/8),\quad r_4=PS/8.
\]

Their energy is

\[
 E=1+49|S|^2/32+|S|^4/32-\Re(S^3/P)/4.
\]

The cubic discriminant identity, with its unit-root sign included, is

\[
 \Delta=27-18|S|^2-|S|^4+8\Re(S^3/P).
\]

One can verify this directly by expanding the discriminant of x³−Sx²+P\overline Sx−P. It gives

\[
 E=(59+31|S|^2-\Delta)/32,
\]

and therefore

\[
 \boxed{E(1,1,1)-E(q_1,q_2,q_3)
 =\frac{31\sum_{i<j}|q_i-q_j|^2+\prod_{i<j}|q_i-q_j|^2}{32}\ge0.}
\]

Here9−|S|²=Σ_(i<j)|q_i−q_j|². This positive decomposition is compatible with the negative Laurent coefficient. Equality requires all roots equal. This finite example does not establish arbitrary M or m.

An exact symbolic program, `scalar_window_m3_invariants_round3.py`, expresses m3 energies through M8 in v=|S|² and u=Re(S³/P), then substitutes the discriminant. Its output is an algebraic exploration, **not** an unreviewed claim that every resulting polynomial is nonnegative on all feasible configurations. For example M3 gives gap[(119−5t)Δ+t(1016−41t−t²)]/1458, with t=9−v∈[0,9]; those particular factors are nonnegative, but a general-M representation remains missing.

## Counterexample search and its precise limits

`scalar_window_coalescence_search_round3.py` used seed20261117, rational unit-circle parameterizations q=(r²−p²+2ipr)/(r²+p²), and ordinary floating arithmetic to explore33,600 configurations with m3–6,M∈{1,2,3,5,10,20,40}. It included separated roots, tight clusters, repeated subclusters and fourth-root configurations. No apparent counterexample was found. Any apparent violation was set up to be recomputed using exact rational complex arithmetic; none was produced. **Absence of a counterexample in this search is not evidence equivalent to a proof**, and no validated numerical enclosure is claimed.

## Next precise steps

1. Prove or refute the full maximum statement. A counterexample must give explicit unit rational roots, integer m,M and a positive exact rational difference E(q)−E(coal).
2. The negative Laurent witness eliminates coefficientwise positivity of the raw energy as a general proof. Seek a gap decomposition in pair differences, a valid symmetric-function inequality, or another norm contraction.
3. For m=3, derive the energy as a polynomial in v,u and exploit the feasible cubic-root region (including the nonnegative discriminant), rather than treating v,u as independent arbitrary real numbers.
4. Preserve the already proved collision-uniform K_m/M bound regardless of this conjecture's outcome. Its proof needs no coalescence-maximum assumption.
