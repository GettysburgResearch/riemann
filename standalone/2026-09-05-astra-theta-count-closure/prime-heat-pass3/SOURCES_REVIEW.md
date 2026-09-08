# Sources, hypothesis audit and independent review contract

This is an author-supplied review request, not an independent review verdict.
All analytic conclusions are proposed proofs pending specialist review.
No external novelty assessment is claimed.

## Exact repository dependencies

Scientific base: 401196451ef1b51e5ff4d84dd23bd75bbf9215a1, PR #790.
Root: standalone/2026-09-05-astra-theta-count-closure/.

- HEAT_BERNSTEIN.md: invariant normalization, genus-zero product, S>0 and
  Bernstein/Stieltjes implications. Original bytes at bc3c35d8f434949748a2185783bf831d3afd9126.
- THETA_COUNT.md: exact mixed-integral/Hausdorff endpoint.
- pass2/MIXED_HEAT_STRIPS.md: all-order late-time threshold T_m(H).
- pass2/SMALL_TIME_ALL_ORDERS.md: inherited global positivity through
  derivative order 10^15, used ONLY to obtain the all-order interval and the
  10^22 corollary. The new source bounds and fixed-t asymptotic do NOT depend
  on this inherited small-time theorem or on any finite zero verification.
- The concurrent mixed-differences-pass2 and quadratic-wedge-pass3 packets
  are preserved but are not analytic inputs to the present proof.

## External primary inputs, inspected September 5, 2026

1. A. Chirre and F. Goncalves, *Bounding the log-derivative of the zeta-function*,
   Mathematische Zeitschrift 300 (2022), 1041--1053; published July 28, 2021.
   DOI: 10.1007/s00209-021-02820-9.
   https://link.springer.com/article/10.1007/s00209-021-02820-9
   ONLY Proposition 5, Guinand--Weil for analytic even tests, is imported.
   That proposition states the sum over general rho=beta+i gamma WITHOUT RH.
   The article's main theorems and Lemma 4 assume RH and are NOT used.
   Their Fourier convention has exp(-2pi ixy); ours has exp(-i ell x).
   The theorem was read in publisher HTML, including all terms and hypotheses.
   No PDF analysis or external computational replay was performed.
   The site's introductory Dirichlet-series display appears to omit the minus
   sign on zeta'/zeta; that display is not used. Our positive A(y) is defined
   directly as sum Lambda(n)n^(-y-1/2), bounded by Lambda<=log n.
2. D. Platt and T. Trudgian, *The Riemann hypothesis is true up to 3*10^12*,
   Bulletin of the London Mathematical Society 53 (2021), 792--797.
   DOI: 10.1112/blms.12460; arXiv:2004.09765.
   https://arxiv.org/abs/2004.09765
   Exact import: all nontrivial zeros with 0<gamma<=3*10^12 are critical.
   No simplicity is used. The abstract/publication metadata were read;
   the full computation and zero census were NOT rerun.
3. NIST DLMF 5.9 and 5.11, digamma integral and Gamma asymptotic conventions.
   https://dlmf.nist.gov/5.9
   https://dlmf.nist.gov/5.11
   The deliberately coarse Euler--Maclaurin estimate used here is displayed
   and bounded in the manuscript, rather than imported as an optimized theorem.
4. NIST DLMF 18.5, physicists' Hermite polynomial convention.
   https://dlmf.nist.gov/18.5
   The finite expansion used in PH19 is independently reconstructed by the
   exact checker from the time-derivative recurrence; no special-function
   library is needed in that checker.

## Load-bearing review points

1. Full versus upper-half-plane zero multiplicity; verify the 4pi in PH1,
   the prime factor 2, Fourier normalization, and F(i/2)=0 only for m>=1.
2. Check PH2--PH6 from exact Gamma ratios, especially the lower-half split
   and the m>=16t(d+y^2) condition for the sharper shifted-contour bound.
3. Check Euler-sum domination on each [n-1,n]; the contour never crosses a
   singularity of F, and its chosen y is strictly greater than 1/2.
4. Check the periodic-B1 digamma remainder, the probability weights w_l,
   the factor 1/2 on the log moment, and the entire archimedean integral.
5. Check the three separate dependency levels: source theorem without V_H;
   all-order common interval using preserved pass2; late-time overlap using
   full V_(3*10^12). No finite-to-infinite inference is authorized.
6. Check uniformity of the adaptive contour in both m and t, and that the
   bracket is decreasing in t before extending from its upper endpoint.
7. Check both real peaks and the sqrt(2pi/t) factor in PH20, integrable
   domination near x=0 and infinity, and dominated convergence for the FULL
   infinite prime sum. The error is only at fixed t.
8. The signed comparison PH21 remains open; no bound derived from absolute
   values is labeled as its proof. The original counterfeits remain relevant.

A flaw in PH20 would not by itself invalidate PH12/PH17, which are direct
inequalities and do not use the asymptotic. A flaw in the inherited pass2
proof would affect PH13/PH14 but not the new verification-free source bounds.
