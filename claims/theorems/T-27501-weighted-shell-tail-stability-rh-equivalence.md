# T-27501 — Weighted Shell-Tail Stability is equivalent to RH

Claim ID: `T-27501`  
Title: The final elementary carry frontier is one dyadic weighted prime-sampling theorem exactly equivalent to the Riemann Hypothesis  
Status: **FINAL CONSOLIDATED EQUIVALENCE THEOREM — `WSTS` REMAINS UNPROVEN**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Frozen base: PR #240 at `58c70a81dce76cd84ea50a60c15c227537f240c1`  
Dependencies: `L-23823`--`L-23826`, `T-23811`, `L-27501`; PR #248 prime-only reduction; the source-pinned square-screw/Landau transfer  
Scope: full Riemann Hypothesis

## 1. Canonical finite scalar

For the parabolic seed at endpoint `X`, put

\[
r_X(p)=v_p(b_X^{(0)})-p^{-1/2}\log(X/p)
\qquad(p\le X,\ p\text{ prime}).
\tag{T-27501.1}
\]

Let

\[
Y=\lfloor X/2\rfloor
\]

and define the dyadic shell residual

\[
s_X(p)=r_X(p)-\mathbf1_{p\le Y}r_Y(p).
\tag{T-27501.2}
\]

The weighted shell-tail charge is

\[
\boxed{
\mathcal B_X
=
\max_{2\le z\le X}
\left[
\sum_{z\le p\le X}(\log p)s_X(p)
\right]_+.}
\tag{T-27501.3}
\]

The **Weighted Shell-Tail Stability theorem** is

\[
\boxed{
\forall\varepsilon>0,
\qquad
\mathcal B_X=O_\varepsilon(X^\varepsilon).}
\tag{WSTS}
\]

Every object in this statement is finite and elementary once the primes through
`X` are listed.  There is no limiting operator, unspecified packet norm, or
hidden continuation hypothesis.

## 2. Main equivalence

The following are equivalent.

1. The Riemann Hypothesis.
2. `WSTS`.
3. The dyadic shell corrections of `L-23824/L-23826` retain the parabolic
   objective with total loss `X^(o(1))`.
4. The ordinary-prime ramp satisfies
   \[
   \boxed{
   \sum_{p\le X}{\log p\over\sqrt p}\log{X\over p}
   \ge4\sqrt X-X^{o(1)}.}
   \tag{T-27501.4}
   \]
5. The complete prime-power ramp satisfies the analogous estimate.

## 3. `WSTS` implies the sharp prime ramp

Let

\[
X_0=X,
\qquad
X_{j+1}=\lfloor X_j/2\rfloor,
\]

and stop at the first bounded endpoint.  The seed and target responses telescope
exactly across these dyadic shells.

`L-23823` proves that each continuum shell has a nonpositive weighted upper
tail, including a quantitative square-root moat.  `L-23825` reduces the finite
failure of this order to the scalar charge `mathcal B_(X_j)`, with only an
absolutely summable carry-floor error.  `L-23824/L-23826` then construct an
in-support signed incidence transport which makes the shell feasible while
losing at most `mathcal B_(X_j)` in the ordinary-prime objective.

Assume `WSTS`.  Given `eta>0`, apply it with a smaller exponent, for example
`eta/2`, at every dyadic endpoint.  Then

\[
\sum_j\mathcal B_{X_j}
\ll_\eta
\sum_jX_j^{\eta/2}
\ll_\eta X^{\eta/2}
=X^{o_\eta(1)}.
\tag{T-27501.5}
\]

The parabolic seed has objective

\[
J_{\mathbb P,X}(b_X^{(0)})
\ge4\sqrt X-O(\log^2X)
\tag{T-27501.6}
\]

by PR #248.  Therefore the corrected dyadic shell sum gives

\[
P_X
\ge4\sqrt X-O_\eta(X^\eta).
\tag{T-27501.7}
\]

This proves statement 4.

PR #248 `L-24517` gives

\[
S_X-P_X=O(\log^2X),
\tag{T-27501.8}
\]

so the ordinary-prime and complete prime-power ramp statements are equivalent at
subpower scale.

## 4. The prime ramp implies RH

The source-pinned square-screw identity at `X=N^2` has the exact archimedean main
term `4N`.  Equation (T-27501.7) gives a subpolynomial upper envelope for the
zeta screw on the square mesh.  The unconditional derivative budget fills the
gaps between consecutive square samples.  Landau's one-sign theorem applied to
the Laplace transform of the completed screw then excludes every pole of
`xi'/xi` with real part greater than `1/2+delta`, for every `delta>0`.
Functional-equation symmetry gives RH.

This is the inherited implication in `T-23811` and the square-screw programme.
No finite-height zero verification is used.

Thus

\[
\boxed{\mathrm{WSTS}\Longrightarrow\mathrm{RH}.}
\tag{T-27501.9}
\]

## 5. RH implies `WSTS`

`L-27501` proves the converse quantitatively.  Under RH,

\[
\vartheta(t)-t=O(\sqrt t\log^2(2t)).
\]

The exact shell profile satisfies

\[
|E_c(u)|\ll u^{-1/2}[1+\log(1/u)],
\]

and

\[
|E_c'(u)|\ll u^{-3/2}[1+\log(1/u)].
\]

Stieltjes integration by parts in the exact sampling remainder of `L-23825`
gives, uniformly in the lower tail endpoint,

\[
\sup_z|\mathcal E_{X,\lfloor X/2\rfloor}(z)|
\ll\log^4(2X).
\tag{T-27501.10}
\]

The continuum term is nonpositive and the carry-floor error is polylogarithmic.
Hence

\[
\boxed{
\mathcal B_X\ll\log^4(2X).}
\tag{T-27501.11}
\]

In particular `WSTS` holds.  Therefore

\[
\boxed{
\mathrm{RH}\Longleftrightarrow\mathrm{WSTS}.}
\tag{T-27501.12}
\]

## 6. What has genuinely been completed

The following parts of the elementary programme are no longer open existence or
geometry questions at the scopes used here:

```text
sharp parabolic 4 sqrt(X) seed;
positive average-binomial row representation;
positive endpoint-scale atoms;
continuum defect-to-slack tail order;
fixed-ratio shell tail order and quantitative moat;
uniform finite carry-floor approximation;
exact weighted prime-tail transport;
dyadic shell telescoping;
ordinary-prime to prime-power reduction;
prime-ramp to RH consumer.
```

The unresolved statement is precisely the finite prime sampling of the ordered
continuum shell, i.e. `WSTS`.

## 7. Disposition of parallel closing mechanisms

The following live proposals are useful attack mechanisms but are not additional
independent load-bearing theorems in the consolidated proof spine:

- endpoint-scale blocker control (`ESBT/ESGS`, PR #265);
- prime-tail queue/charge (`PTQ/PTC`, PRs #271/#274);
- fifth-scale digital–Green boundary recurrence (`DGB(5)`, PR #244);
- factor-five physical transition contraction (`F5TC`, PR #269);
- finite arithmetic Green deformation (`FAGD`, PR #270);
- annular dual frame (`ADF`, PR #267);
- parity–Green coercivity (`PGC`, PR #236);
- boundary-jet domination (`BJD`, PR #272).

Each may prove `WSTS`, the prime-ramp estimate, or another RH-equivalent scalar.
None is presently a proved implication to `WSTS` at the cofinal quantitative
scope required here.

The exact positive ordinary-prime LP of PR #271 closes positivity geometry but
has optimum equal to the unknown prime ramp; it does not estimate that optimum.

## 8. Automatic rejection conditions for a claimed completion

A proof of `WSTS` must be rejected if it does any of the following:

1. replaces the weighted prime sample by its continuum integral without an
   explicit remainder;
2. applies a fixed-ratio PNT statement uniformly at a shrinking ratio;
3. takes positive parts before complete shell recombination;
4. deletes the logarithmic/von-Mangoldt dual ray;
5. treats finite numerical ladders as a cofinal estimate;
6. loses the dyadic or `2/3` fixed-ratio Mertens mutation;
7. uses the old one-frequency physical-block identity;
8. invokes a generic bounded-rank, bounded-contact, or arbitrary-vector theorem
   already contradicted elsewhere.

## 9. Exact status

```text
continuum shell majorization                 PROPOSED COMPLETE
finite shell/floor decomposition             PROPOSED COMPLETE
weighted finite prime transport              PROPOSED COMPLETE
RH => WSTS with O(log^4 X)                   PROPOSED COMPLETE
WSTS => prime ramp => RH                     PROPOSED COMPLETE
WSTS <=> RH                                  PROPOSED COMPLETE EQUIVALENCE
unconditional WSTS                          UNPROVEN
Riemann Hypothesis                          UNPROVEN
```

This theorem consolidates the project for review.  It does not relabel the
RH-equivalent estimate as a completed lemma.