# Technical audit of the claimed fixed zero-free boundary for zeta

**Disposition.** The preprint of 13 November 2026 explicitly claims a zero-free half-plane for the Riemann zeta function with boundary $B_*=0.8733458561067185768\ldots$. I verified the specialization from the auxiliary field, reconstructed the supremum contradiction, checked the floor-bin change against its cited detector, and replayed the 240-stage scalar construction in exact rational arithmetic. The remaining verification depends on the complete arithmetic moment estimates, particularly the signed ordinary-moment and detector transfers specified below. These findings establish how the source's claim would follow from those estimates. The analytic transfers remain open in this audit. [Liu, Hexagon 2611.00421v1](../sources/latest62_density_frontier/hex_2611.00421v1.pdf)

## Specialization and comparison

Set $E=\mathbb Q(\zeta_{12})$. Its Galois group is $C_2\times C_2$. With primitive Dirichlet factors, including the ramified local identities, one has
$$
\zeta_E(s)=\zeta(s)L(s,\chi_{-4})L(s,\chi_{-3})L(s,\chi_{12}).
$$
The three nontrivial characters have conductors 4, 3 and 12. All three nonprincipal factors are entire. Consequently a zero of $\zeta(s)$ in $B_*<\Re s<1$ would force a zero of $\zeta_E(s)$. Classical nonvanishing on $\Re s=1$ and the Euler product to its right handle the rest of the prescribed half-plane, with the pole at 1. Thus the zeta claim needs only the finite-order argument for the fixed cyclotomic field $E$; it needs no unitary or Weil extension. [Theorem 8.14 and equation (62)](../sources/latest62_density_frontier/hex_2611.00421v1.pdf)

The analytic comparison is structurally a supremum contradiction. Take $\beta=\beta_*(E)>B>B_*$ and let $c_0=(4+b)/6$ in the source's geometric notation. The principal term satisfies
$$
f_\eta(Z)=\frac{1}{2\pi i}\int_{(2)}Z^{s-c_0}
   \frac{e^{(s-5/6)^2}H_\eta(s)}{L^S_E(s,\eta)}\,ds.
$$
The two required estimates are a direct bound for the compensated average $J_\eta$ of size $Z^{B-c_0+\epsilon}$ and a difference bound of size $Z^{\beta-c_0-\delta}$ for $J_\eta-f_\eta$. Here $B+\epsilon<\beta$ and $\delta>0$ must be common numerically across all targets over $E$. The triangle inequality gives $\sigma=\max(B+\epsilon,\beta-\delta)<\beta$. Moving the principal integral right bounds $f_\eta(Z)$ by arbitrary positive powers at zero. Thus $\int_0^\infty f_\eta(Z)Z^{c_0-s}\,dZ/Z$ converges locally uniformly in $\Re s>\sigma$ and, by Mellin inversion on the original right half-plane, continues the displayed reciprocal times its numerator. The numerator $H_\eta$ is holomorphic and nonzero for $\Re s>437/500$, and $\sigma>B_*>437/500$. The omitted local factors introduce zeros only on $\Re s=0$. Each target is therefore zero-free to the right of the same $\sigma$, which contradicts the supremum without requiring its attainment. Target-dependent implied constants, finite cutoffs and onsets are allowed. [Earlier Lemma 13.11 and Remarks 13.12–13.13](../sources/latest62_density_frontier/2610.26835.pdf)

The principal contour stays to the right of $\beta$ before estimating the Mellin inverse. The older pointwise prime bound used in the new count has premise $\beta_*(E)\le(1+\kappa_1)/2$, with $\kappa_1=374887/500000$. The cited earlier claimed bound $B_\flat=0.874886647039964\ldots$ is strictly below $(1+\kappa_1)/2=0.874887$. This comparison identifies a prior analytic dependency, with a gap about $3.52960\times10^{-7}$. The earlier bound is itself an input from another preprint. Its full proof was outside this audit. [Earlier Theorems 14.12 and 18.2](../sources/latest62_density_frontier/2610.26835.pdf)

The floor at $509/1000$ does not supply a half-plane of global nonvanishing. For each nonprincipal row, the earlier detector proof defines $B_i$ as the maximum of the floor and the zero real parts up to a specified multiple of $T_1$. Pigeonholing gives $B_{i+1}-B_i\le e$. Rounding $B_i$ down to its bin edge $a$ gives $B_{i+1}<a+2e$, including the floor bin. This is the local buffered nonvanishing needed for the truncated reciprocal contour at $a+16e$. The logarithmic bounds in the detector proof precede the extraction of an actual zero, which only takes place above the floor bin. The local correction estimate on $\Re z=17/50$ permits any $a$ between $1/2$ and $11/12$. Thus the cited proof has the ingredients for the new floor, provided the retained row and test-function conditions of that detector are met. [Proposition 8.13](../sources/latest62_density_frontier/hex_2611.00421v1.pdf) · [Earlier Lemmas 13.7 and 13.10](../sources/latest62_density_frontier/2610.26835.pdf)

## Strict-stage arithmetic

I recomputed the recursion (8)–(13) with rational arithmetic, using the decimal ceiling and floor in equations (9) and (11) as exact rational operations. At the endpoints of each interval I used
$$
H=r/R,\quad u=(1-H)/6,\quad S=(1-r)/2+Hz_R+(1/k-2)u,\quad s=S-u
$$
and the unpadded cutoffs $w(k)=w_b$ and
$w_+=w_b+(u/H)(1/k-4/3)/D$, where $D=1/2-a_1$. All 480 checks were positive, including both branches of condition 13. Some minima are recorded below. For condition 1 the reported value omits the subtractive margin $\rho_{\rm high}$.

| Condition | Minimum | Stage, endpoint |
|---|---:|---|
| 1, before subtracting $\rho_{\rm high}$ | 0.0000416015724559 | 238, lower |
| 2 | 0.0006698503488630 | 239, lower |
| 3 | 0.0036357755557214 | 239, lower |
| 6 | 0.0185570110445737 | 0, lower |
| 9 | 0.129798237699057 | 239, lower |
| 12 | 0.0124474085210720 | 0, lower |
| 13, smaller branch | 0.166751111528735 | 0, lower |
| 14 | 0.0125 | 0, upper |

The last improvement is $3850137/1250000000$. In condition 1 even subtracting $3\times10^{-5}$ leaves positive margin. The finite set of strict cutoff margins admits sufficiently small positive padding by continuity. At fixed incoming data the conditions are affine in $r$ after clearing positive $H$ in the cutoff formulas, so their endpoint signs control the interval. Condition 13 is treated as two separate affine tests. The endpoint $r=R$ is used only for checking the scalar margins; the analytic propagation requiring $u>0$ is applied at $r<R$. This computation audits the fixed scalar chain, while the limiting approximation and comparison certificates in §§6.1 and 7.1 are separate. [Proposition 5.1 and §8.7](../sources/latest62_density_frontier/hex_2611.00421v1.pdf)

Several inequalities in the analytic proof can also be checked directly. The gaps in (53) follow from conditions 2–4 and 6–8 and $u\le10^{-4}$. In particular the third gap is greater than $1/6-137/1000-3/10000$, which is positive. The reflected reference faces have numerical bounds $1/3+7/25+(49/20)(137/1000)=0.9489833\ldots<0.95$ and $7/50+1/2+(49/20)(137/1000)=0.97565<0.99$. The identity $2a-k_C+q_C=1+t-6u_C$ follows by substituting $a=A-c-u_C$, $q_C=q+c-d$, $k_C=2A-c-d+q-1-t+4u_C$. The paired-side cancellation in §8.9 follows by adding it to the counterpart with $c,d$ exchanged. These checks validate the indicated exponent algebra. [Propositions 8.10 and 8.11](../sources/latest62_density_frontier/hex_2611.00421v1.pdf)

Under the two count inputs in (48), the large-value argument in Proposition 8.9 gives a strict common saving. For $g=Hw-H\omega$, the definitions imply $D(g-r)=H(z_R-\lambda(R))+u(1/k-1/\nu)\ge0$ and $s-H((1-g/H)/2+\lambda(g/H))=g-r+u/\nu$. The short count plus $\nu r+es$ is then at most $H+u-H\nu(\omega/10-\pi)$ using $e\le\nu$ and $a_1\le2/5$. For the unpadded long exponent the saving above its value at $\nu=k$ is
$$
(\nu-k)\left(\frac{3g(\nu)}2-(r+s)-(5/6-k)\frac{3u}{2k\nu D}\right)\ge0,
$$
by condition 9 and $g\ge r$. Its value at $k$ is $HF_{\rm high}>0$, leaving room for positive cutoff padding. For sixth powers the short branch's two possible $M$-slopes are $-\nu w$ and $-\nu w-e\sigma(w)$, bounded below by $-5/6$ by condition 13. The long and small-core slopes have the same lower bound. Since supremum, infimum and maximum preserve the resulting one-sided bound, the loss per sixth-power cofactor of norm $N B$ is at least $\log_Z N B$; adding $\delta M$ to the exponent upgrades its sum to $\sum_B(N B)^{-1-6\delta}$, convergent over ideals of a fixed field. Thus the scalar comparison and cofactor summation are consistent once the asserted per-core detector and moment estimates hold. [Proposition 8.9 and §8.7](../sources/latest62_density_frontier/hex_2611.00421v1.pdf)

## Outstanding analytic verification

1. **Large-value detector in (48).** Proposition 8.9 proves exponent savings given the two count estimates in (48). A direct verification still needs a term-by-term application of the earlier detector to each retained canonical inverse and ordinary final-term family, including the same rowwise character and twist, complete prime subsets, normalization by actual ideal-norm width, marked natural zeros, and exceptional inducing classes. The output to verify is exactly the two displayed counts $H-\nu Hw-e\min\{s,H\sigma(w)\}$ and $H/6+(5/6-\nu)Ht(w)$ for the same amplitude class and a common cutoff, with losses that can shrink with the stage. The numerical margin proof begins after this assertion. [§§8.5–8.7](../sources/latest62_density_frontier/hex_2611.00421v1.pdf) · [Earlier detector, Lemmas 13.7–13.9](../sources/latest62_density_frontier/2610.26835.pdf)

2. **Ordinary comparison and reference transfer.** Proposition 8.10's local Euler kernel exponents show summability conditional on the stated collision degree ranges and the erasure cost. Proposition 8.11 imports the signed equal-product and common-divisor identities and quotes the side constraints (52). The concrete remaining check is to expand the two sides, including diagonal and inducing-character terms, and verify that every surviving signed/common-divisor term is either controlled directly or delivered to the weighted reference or retained final-term family with precisely the stated prime factors and normalization. This includes the auxiliary prime averaging, equality of the ordinary characters after transformation, cases $S_*-f<u$ and $S_*-f\ge u$, and compatibility of the reference erasure estimate with the full cubic kernel. This is needed to conclude the new bounds from the strictly earlier coefficient-two theorem. Neither the checked exponent cancellation nor the finite scalar replay verifies the claimed analytic transfer. [Propositions 8.10–8.12](../sources/latest62_density_frontier/hex_2611.00421v1.pdf) · [Earlier ordinary coefficient-two theorem, Theorem 4.9](../sources/latest62_density_frontier/hex_2611.00082v1.pdf)

3. **Mellin transfer.** The contradiction establishes the consequence of the two bounds for the same $J_\eta,f_\eta$. The prior theorem requires identity (13.11) with one retained numerator and the ordered contour/truncation rules, then a uniform numerical saving in (13.20). The remaining check is the insertion of the new rectangle bounds through all detector and numerator terms of the full compensated comparison, especially the rowwise use of prime coefficients and the choice of one common height allowance before the outer contours. The source's floor calculation alone addresses only one of the comparison branches. [Theorem 8.14 and Remark 8.15](../sources/latest62_density_frontier/hex_2611.00421v1.pdf) · [Earlier §§13.3–13.6](../sources/latest62_density_frontier/2610.26835.pdf)

No contradiction with the retained source or counterexample to the stated zero-free claim was found in these checks. The preprint's numerical boundary is unconditional in its statement, while independent verification here remains conditional on the indicated analytic steps and earlier preprint inputs. The proof uses thresholds and constants that may depend on the field, fixed target and chosen boundary $B>B_*$. It asserts neither a common effective onset in those parameters nor a statement on the boundary itself. The source says its Lean formalization is in progress. [Author's account and Theorem 8.14](../sources/latest62_density_frontier/hex_2611.00421v1.pdf)
