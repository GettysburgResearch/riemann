# Square-part stratification of the mixed theta tail

**Status.** Source-qualified restricted-slice calculation, with an exact p=6 scalar certificate independently reviewed internally. It is not an individual zero-free theorem. The physical Poisson/profile identifications and the GL quadratic, sixth-order and completed-theta source inputs are those of [the eighth/tenth Hölder tail](../2026-10-29-eighth-holder-tail/README.md). Floating-point grid outputs below are diagnostic, not certificates.

Write each good sixth-free row uniquely as \(b=w v^2\), with \(w\) squarefree and \(v\) cube-free; common primes of \(w,v\) are allowed. Fix the dyadic norm \(Nv\asymp V\), so \(V\le B^{1/2}\), \(Nw\ll M=B/V^2\), and the number of rows in this slice is \(\ll B^{1+\epsilon}/V\). Its original masks and all bounded fixed-row multipliers remain in place.

For every fixed positive integer \(p\), the prefix moment has the refined bound
\[
 \sum_{b\text{ in slice}}|A_b(x)|^{2p}
 \ll (Bx)^\epsilon\left(\frac BV x^p+V x^{2p}\right).\tag{1}
\]
Indeed, fix v and expand \(A_b^p\). The squarefree column part of each product has a common quadratic source coefficient; the column square part gives a row contraction and incurs a harmonic sum. Since \(\chi_c(v^2)^3\) is the original 0/1 mask, the v-factor is also a contraction. GL then bounds the fixed-v 2p-moment by \((Bx)^\epsilon[(B/V^2)x^p+x^{2p}]\); summing over \(O(V^{1+\epsilon})\) values of v gives (1). Since \(1\le V\le B^{1/2}\), (1) is never weaker than the reviewed all-row bound. Keeping both in the minimum is harmless.

The completed-theta fourth moment also admits
\[
 T_4(Z)\ll (BZ)^\epsilon\min\{\Theta_6(B,Z^2),\ V\Theta_6(B/V^2,Z^2),\ (B/V)Z^2\}.\tag{2}
\]
For the middle expression fix v first: the fixed multiplier \(\chi_n(v)^2\) is absorbed into the common theta coefficient, including its zeros, and the theta cube-index row factors are bounded contractions. Squaring the remaining squarefree n-polynomial has sixth-free columns, so the same Θ₆ argument applies to the squarefree w rows; finally sum over v. The last expression is the actual-row-count and pointwise theta bound. These common-vector and sector identifications are a source interface to verify, not a new printed source theorem.

Use simultaneously
\[
 T_2(Z)\ll(BZKF)^\epsilon\min\{(B/V)Z,\ BK+B^2K^2F/Z,\sqrt{(B/V)T_4(Z)}\}.\tag{3}
\]
The middle expression is the unrefined completed-theta source mean and remains valid for a subset; the first and last use only the actual slice count. The short cube-index contribution likewise retains its earlier unrefined source estimate. This choice avoids assuming any new moving-v theta mean.

For fixed \(2\le p\le6\), Hölder and T2–T4 interpolation bound the Abel integrand by
\[
 A_{2p}(x)^{1/(2p)}T_2(D/x^3)^{(p-2)/(2p)}T_4(D/x^3)^{1/(2p)}\!/x^2.\tag{4}
\]
The scale-wise minimum over these p may be used before integration. Under \(e\)-rescaling \(x=x_0/(Ne)^{1/3}\), every prefix term loses at least \((Ne)^{-p/3}\), the source T2 can grow by \(Ne\), and T4 is unchanged. Including the exterior mask coefficient and \(dx/x^2\), each p-bound has norm factor at most \((Ne)^{1/6-1/p}\), nonincreasing for \(p\le6\). Thus a common cutoff satisfying \(Ne\le C_*^3\) permits the same divisor summation as the earlier note. No p>6 conclusion follows from this argument without additional divisor bookkeeping.

Using the earlier short mean, the minimum of stratified and unstratified moments, and the physical prefactor from the eighth/tenth note, [corner.py](corner.py) samples the corner \(d=7/50,\kappa=g=0\) and cube cutoffs; [grid.py](grid.py) samples the full core coarsely. At \(b=.945\) the worst sampled exponent is about 1.04761, at \(v=0,d=.14,\kappa=g=0\); at \(b=.95\) it is about 1.05430. These values use finite grids and do not establish the continuous supremum or the exact source matching. A rigorous gain requires a rational polyhedral certificate for all \(d,\kappa,g,v\), all cube scales and a single admissible cutoff per physical dyad, plus an independent check of (1)–(3).

## Exact p=6 source-qualified bound

The further hypotheses and interpretation are exactly those of the [physical dual-core reduction](../2026-10-29-eighth-holder-tail/README.md): fixed original column sector; source Poisson, reciprocity, profile and finite-ray calibration; and a separately budgeted artificial diagonal. Under these inputs the following slice bound uses **only** (1), the original all-row Θ₆ term of (2), and all three branches of (3). In particular it does not require the optional fixed-v Θ₆ refinement. Take the common dyad-dependent cutoff
\[
 \log_Y C_*=\frac1{20}+\frac d{15}-\frac g{20}.\tag{5}
\]
For \(b\ge23/25\), the earlier calculation gives \(\log_Y Ne\le3\log_Y C_*-7/1500\) throughout \(d+g+6\kappa/5\le7/50\); the smaller b range is covered by the earlier eighth/tenth bound. The p=6 norm factor in the divisor-rescaling lemma is exactly \((Ne)^0\), and the divisor count is \(Y^\epsilon\).

With \(u=\log_Y V\in[0,b/2]\), \(z=\log_Y x\), \(\Delta=6/5-d-g\), \(Z_e=\Delta-3z\) and \(p_0=1/30+2d/3-5\kappa/6-b/6\), insert into (4)
\[
 \begin{aligned}
 A_{12}&:\quad \max\{b-u+6z,\ u+12z\},\\
 T_4&:\quad \max\{b,2Z_e,5b/6+2Z_e/3,b/3+5Z_e/3\},\\
 T_2&:\quad \min\{b-u+Z_e,\ \max(b+\kappa,2b+3\kappa+g-Z_e),\ (b-u+T_4)/2\}.
 \end{aligned}\tag{6}
\]
The tail mean exponent is \(p_0-2z+A_{12}/6+2T_2/3+T_4/6\), maximized over the core, \(0\le u\le b/2\) and \(\log_Y C_*\le z\le\Delta/3\). The [checker](check_stratified_p6.py) produces and exactly verifies nonnegative rational dual certificates for each of its sixteen face programs, including all T2 branches. It yields:

| \(C_{\rm core}\) | \(b_{\max}\) | tail exponent upper bound | short exponent upper bound | target |
|---|---|---|---|---|
| \(7/50\) | \(4213/4450\) | \(21/20\) | \(21813/22250\) | \(21/20\) |
| \(1925877/15625000\) | \(1348218883/1390625000\) | \(19949123/18750000\) | \(13778849011/13906250000\) | \(19949123/18750000\) |

Thus, with any fixed \(\epsilon>0\), the indicated slice through \(b\le4213/4450\) has target size \(Y^{21/20+\epsilon}\); every fixed \(b\) strictly below the second endpoint has a strict saving relative to the current θ threshold, after choosing \(\epsilon\) smaller than the margin. To cover all smaller b using the endpoint check, enlarge the u-domain to \([0,b_{\max}/2]\) and then increase b to \(b_{\max}\); every tail and short face increases with b in this enlarged domain. Earlier estimates cover b below \(23/25\).

High_match and Other_families independently checked the stratified moment identities, the overlap masks, and p=6 divisor scaling. High_match and Other_families independently reran and audited the exact scalar checker. These results remain conditional on the named analytic and physical-source interfaces and control a restricted slice, leaving the full mixed moment and individual zero-free conclusion open.
