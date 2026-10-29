# Independent review: cubic-cap split through b=.97 and .99

**Conclusion.** The fixed-w cubic source bounds, moving-divisor scaling, common cutoff and exact dual checker in [check_cubic_split.py](check_cubic_split.py) are consistent under their explicitly imported source and physical-calibration inputs. I reran all 24 short and 576 tail linear programs for each of the two endpoints. This is a restricted dual-slice estimate, not a full inverse-moment or individual zero-free theorem.

Write sixth-free \(b=w v^2\), with w squarefree and v cube-free, allowing shared primes. Fix v for the quadratic prefix: \(\chi_h(v^2)^3=\mathbf1_{(h,v)=1}\) is a common h-column mask. For fixed integer p, expand the p-th power of the prefix, fix its square part and apply the quadratic Hecke large sieve on w; summing the \(O(V^{1+\epsilon})\) choices of v gives
\[
 A_{2p}(H)\ll Y^\epsilon\{(B/V)H^p+VH^{2p}\}.
\]
This works for the two fixed p=6 and p=10, with the angular factor \(\bar\alpha(h)^3\), finite-ray phase, fixed k,f masks and coefficient-divisor losses retained.

For the theta moments fix w instead. \(\chi_n(wk)\) is then a common column coefficient and \(\chi_n(v)^2\) is the powered cubic FHL family; the fixed theta cube index q contributes the row contraction \(\chi_q(v)^6=\mathbf1_{(q,v)=1}\). Applying the source cubic sieve to n and, for the fourth moment, to \(n_1n_2\), yields \((B/V^2)\Theta_3(V,X)\) and \((B/V^2)\Theta_3(V,X^2)\). The latter product has local exponents at most 2 and is cubic-free even if its two factors overlap; all q and w/v shared-prime zeros survive. These bounds are additionally conditional on the source-powered-family reciprocity/sector and common-profile interface cited in [the cubic moment note](../2026-10-29-squarepart-cubic-theta-moments.md).

For each cube scale, apply Hölder and interpolate theta \(L^2\) and \(L^4\): the prefix \(2p\)-moment contributes power \(1/(2p)\), T2 power \((p-2)/(2p)\), and T4 power \(1/(2p)\). Take the minimum between p=6 and p=10 **before** integrating the Abel tail. Its T2 inputs are the actual-row trivial bound, unstratified Θ₆ and fixed-w Θ₃; its T4 inputs are unstratified Θ₆ and fixed-w Θ₃. In particular the tail does not use the source prop:R bound containing F.

Under the physical divisor e, \(D_e=D/Ne\), \(F_e=FNe\), exterior norm factor \((Ne)^{-1/2}\). With \(H=H_0/(Ne)^{1/3}\), theta scale \(D_e/H^3=D/H_0^3\) is invariant, every prefix bound gains at least \((Ne)^{-p/3}\), and each of the selected T2/T4 tail bounds is unchanged. Including \(dH/H^2\), either Hölder norm gains \((Ne)^{-1/2-1/6+1/3}=(Ne)^{-1/3}\); its squared gain is \((Ne)^{-2/3}\). The source prop:R bound is used only in the short part. After weighted Cauchy and exterior \((Ne)^{-1}\), its growth term becomes \(B^2K^2F H_0^3/D\); all other short caps gain a factor at most one. The full allowed e sum costs a divisor subpower, and the same cutoff applies to both powers and every scale.

The cutoff exponent is
\[
 c=\frac{1583}{4000}-\frac{3b}{10}-\frac{11(d+g)}{40}-\frac\kappa{10}.
\]
The checker takes b itself as a variable in \([23/25,b_{\max}]\) and \(0\le u=\log_Y V\le b/2\), so no endpoint monotonicity assumption is needed. The displayed source root bound for e and \(d+g+6\kappa/5\le C_{\rm core}\le7/50\) give \(18c-(7/5-b+4d-5\kappa)>0\); the checker also certifies \(0<c<\Delta/3\). Thus \(1\le C_e\le D_e^{1/3}\) on every relevant dyad.

Exact rational dual upper certificates give the following maxima among the enumerated source-face programs. Floating HiGHS outputs merely propose the dual multipliers: the script reconstructs them as rationals, checks nonnegativity, and verifies the full dual identity exactly; infeasible floating outputs are not silently discarded.

| core | \(b_{\max}\) | short exponent | tail exponent | target |
|---|---|---|---|---|
| \(7/50\) | \(97/100\) | \(10961/10440\) | \(3779/3600\) | \(21/20\) |
| \(1925877/15625000\) | \(99/100\) | \(1531442043/1450000000\) | \(19873642453/18750000000\) | \(19949123/18750000\) |

All four exponents are strictly below their targets; in the first line the short margin is only \(1/10440\), so all fixed epsilon/profile losses must be selected after this margin. Earlier source-qualified slices cover \(b<23/25\). The two core regions, imported analytic theorems, Fourier/profile calibration, original sector summation and separately budgeted artificial diagonal must not be dropped from any application.
