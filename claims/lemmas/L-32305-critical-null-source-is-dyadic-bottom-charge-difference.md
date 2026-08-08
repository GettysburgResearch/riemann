# L-32305 — The critical-null source is the dyadic first difference of the bottom-charge source

Claim ID: `L-32305`  
Title: The six-row critical-null scalar is exactly the dyadic first difference of PR #268's compact bottom-charge Riesz coordinate, with the unit carry column retained explicitly  
Status: **PROPOSED COMPLETE EXACT CROSS-BRANCH IDENTITY — independent review requested**  
Authoring agent: `gpt56-pro-xhigh`  
Created: 2026-08-08  
Dependencies: PR #268 `L-26204`; `L-32302/T-32301`  
Scope: exact source and scalar identity; no sign estimate

## 1. Source factorization

PR #268 uses

\[
\omega_2
=\mu-{3\over2}\delta_2*\mu+{1\over2}\delta_4*\mu,
\]

with transform

\[
\Omega_2(s)
={(1-2^{-s})(1-2^{-s-1})\over\zeta(s)}.
\]

The critical-null source of `L-32302` factors exactly as

\[
\boxed{
\omega_\dagger
=(\varepsilon-\sqrt2\,\delta_2)*\omega_2.
}
\tag{L-32305.1}
\]

This is merely the polynomial identity

\[
P_\dagger(x)=(1-\sqrt2 x)(1-x)(1-x/2).
\]

## 2. Full Riesz coordinates

Include the unit source and define, for real `X>=1`,

\[
\widetilde{\mathcal R}_\omega(X)
=\sum_{q\le X}{\omega_2(q)\over\sqrt q}\log(X/q),
\]

\[
\widetilde{\mathcal R}_\dagger(X)
=\sum_{q\le X}{\omega_\dagger(q)\over\sqrt q}\log(X/q),
\]

with the convention that a sum is zero below its first support.

Reindexing the shifted term in (L-32305.1) gives

\[
\begin{aligned}
\widetilde{\mathcal R}_\dagger(X)
&=\widetilde{\mathcal R}_\omega(X)
-\sqrt2\sum_{2m\le X}{\omega_2(m)\over\sqrt{2m}}\log(X/(2m))\\
&=\boxed{
\widetilde{\mathcal R}_\omega(X)
-\widetilde{\mathcal R}_\omega(X/2).
}
\end{aligned}
\tag{L-32305.2}
\]

The coefficient `sqrt(2)` is exactly cancelled by the critical normalization `sqrt(2m)`.

Thus the extra factor is literally a scale derivative in the critical Riesz coordinate.

## 3. Carry scalars and the unit-column correction

PR #268 defines the carry-facing coordinate

\[
\mathcal R_\omega(X)
=\sum_{2\le q\le X}{\omega_2(q)\over\sqrt q}\log(X/q).
\]

Since `omega_2(1)=1`,

\[
\widetilde{\mathcal R}_\omega(X)
=\mathcal R_\omega(X)+\log X.
\tag{L-32305.3}
\]

Similarly `omega_dagger(1)=1`, so the six-row scalar `mathcal C_dagger` of `T-32301` satisfies

\[
\widetilde{\mathcal R}_\dagger(X)
=\mathcal C_\dagger(X)+\log X.
\tag{L-32305.4}
\]

Combining (L-32305.2)--(L-32305.4), for `X>=2`,

\[
\boxed{
\mathcal C_\dagger(X)
=\mathcal R_\omega(X)
-\mathcal R_\omega(X/2)
-\log(X/2).
}
\tag{L-32305.5}
\]

This is the exact origin of the real `-log X` mode in the corrected Mellin formula of `T-32301`.

## 4. Bottom-charge form

PR #268 proves

\[
5c_X(2)+3c_X(3)=-6\mathcal R_\omega(X).
\]

Write

\[
B(X)=5c_X(2)+3c_X(3).
\]

Then (L-32305.5) becomes

\[
\boxed{
\mathcal C_\dagger(X)
=-{B(X)-B(X/2)\over6}-\log(X/2).
}
\tag{L-32305.6]
\]

(the bracket typo in the tag is typographical only).

Hence the six-row criterion is exactly a dyadic increment theorem for the old two-row bottom charge, not a logically independent RH condition.

For integer-only conventions one may replace `X/2` by the corresponding real-endpoint Riesz coordinate; no floor is introduced in the source identity.

## 5. Connection to the exact Cycle-Debt commutator

PR #272 `L-27207` proves that at `X=2Y`, the critical target divergence decomposes into

\[
2^{-1/2}\mathcal D_2r_Y
+\text{bottom charge}
+\text{odd-node adjacent-tree commutator}.
\]

The coefficient `2^{-1/2}` is neutral on the square-root moment and gives the exact factor `1/2` only on the divisible-column part of Cycle Debt.  The additional critical source difference in (L-32305.1) removes precisely that neutral lower-scale component at the Riesz level.

Therefore the new finite six-row source should be viewed as the scalar boundary channel which has to be controlled together with the odd-column leakage, not as an unrelated new positivity problem.

## 6. Proof boundary

Closed exactly:

- critical source factorization;
- full dyadic Riesz difference;
- exact unit-column normalization;
- relation to the PR #268 bottom charge;
- identification with the PR #272 dyadic commutator frontier.

Open:

- a one-sign or subpower estimate for the dyadic bottom-charge increment;
- cancellation with the complete odd-column commutator in Cycle Debt;
- RH.
