# Independent review and Poisson proof of the horizontal-ratio bound

2026-11-17. Reviewer `/root/li_skeptic`. Scope: **PAPER-C103**, Proposition2 and its dependencies, and transfer to the already reviewed growing-order array. The contractive-xi/Poisson argument below was independently reconstructed from the root's proposed statement **before reading the owner's proof**. The actual source pp4–8 and the owner's completed source note were subsequently read. Classification: **independently checked with no issue found in the inspected portion**. The estimate itself is a prior result of Balazard–de Roton, not a new RH consequence or a novelty claim.

## Exact primary source and norm

Canonical work: Michel Balazard and Anne de Roton, *Sur un critère de Báez-Duarte pour l'hypothèse de Riemann*, arXiv0812.1689v1. The accessed file is `sources/selberg_round2/balazard_roton.pdf`, SHA256 `d22890fc5903bce4c8be302a35ff5b4d84f33c63a84e9799c04136e5fdf76311`. Its arXiv header says9December2008 while the body prints8November2018; this discrepancy is preserved. The2010 journal mathematical version was not compared. No duplicate paper record or additional whole-read count is created by this review.

The exact source definition onp4 is, with `s=1/2+it`,

\[
 J_\epsilon=\frac1{2\pi}\int_{\mathbb R}
 \left|\frac{\zeta(s)}{\zeta(s+\epsilon)}-1\right|^2
 \frac{dt}{|s|^2}.
\]

Proposition2,p5, marked `(HR)`, asserts `J_epsilon<<epsilon`; §§3–4 assume `0<epsilon<=1/2`. The definition is the **horizontal ratio** used by the present array, with exactly the same measure. No symmetric functional-equation quotient, truncated-height integral or derivative-moment hypothesis is substituted.

This reviewer read the complete definitions and Proposition1 material pp4–5, Proposition4 and proof pp6–7, Proposition5 and proof pp7–8, and the conclusion of Proposition2 onp8. Pages7–8 were also visually checked in independently rendered images in `sources/logarithmic_riesz_priority_skeptic_round4/`. Whole-work reading and the later Soundararajan-dependent Proposition3 are outside this review; the owner separately records its full20-page substantive read.

## 1. A contractive xi quotient under RH

Assume RH. Put `F(w)=xi(1/2+w)`, with the standard entire completed function `xi(s)=s(s-1)pi^(-s/2)Gamma(s/2)zeta(s)/2`. Its even paired product is

\[
 F(w)=F(0)\prod_{\gamma>0}(1+w^2/\gamma^2),
\]

where positive ordinates are repeated with multiplicity. The sum of reciprocal squares converges by Riemann–von Mangoldt; the paired product converges normally. Evenness and order one remove any nonconstant exponential factor, and `F(0)!=0`. Constants in the completed-function convention cancel in every quotient below.

For fixed real `t,gamma`, write `w=x+it` and calculate directly

\[
 \frac d{dx}|\gamma^2+(x+it)^2|^2
 =4x(\gamma^2+x^2+t^2)\ge0\qquad(x\ge0).
\]

Every paired factor consequently increases in modulus as `x` increases. Thus

\[
 H_\epsilon(w)=F(w)/F(w+\epsilon)
\]

is holomorphic on the right half-plane and has modulus at most one there and on its boundary. Under RH its denominator has no zero there, since its argument has positive real part. The numerator's boundary zeros cause no singularity. The ratio extends continuously through every finite boundary point; possible poles are shifted to the left, outside the domain. This verifies the exact Hardy/Schur-class hypothesis needed for the next step.

## 2. Poisson control gives an O(epsilon) square norm

The measure in `J_epsilon` is exactly the right-half-plane Poisson probability measure seen from `w=1/2`:

\[
 d\nu(t)=\frac{dt}{2\pi(1/4+t^2)}.
\]

For a bounded holomorphic function `H` on the right half-plane with these continuous finite boundary values,

\[
 \int\operatorname{Re}H(it)\,d\nu(t)
 =\operatorname{Re}H(1/2).
\]

One can justify this without an assumption at infinity by mapping the disk to the half-plane with `w=(1+z)/(2(1-z))`, applying the harmonic mean-value formula on concentric circles, and using bounded dominated convergence as their radii tend to one. The missing point corresponding to infinity has angular measure zero.

Since `|H_epsilon(it)|<=1`,

\[
 \begin{aligned}
 J^{\xi}_\epsilon
 &:=\int|H_\epsilon(it)-1|^2d\nu(t)\\
 &\le 2\left(1-\operatorname{Re}H_\epsilon(1/2)\right)\\
 &=2\left(1-\frac{\xi(1)}{\xi(1+\epsilon)}\right)
 =O(\epsilon).
 \end{aligned}
\]

Here the quotient at the positive real point is real, positive and at most one. Analyticity and nonvanishing of `xi` near1 give the final `O(epsilon)` estimate. No zero separation, multiplicity ceiling, zero-neighborhood excision or reciprocal-zeta estimate close to a boundary pole is required.

More generally this argument proves the elementary Schur-function inequality `||H-1||_(L²(P_x))²<=2(1-Re H(x))` for any contractive half-plane holomorphic `H`. Its use here is a reusable alternate proof mechanism; no claim is made that the inequality or its zeta application is historically new.

## 3. Completion factors cost only O(epsilon) in norm

Let

\[
 A(s)=s(s-1)\pi^{-s/2}\Gamma(s/2).
\]

For sufficiently small positive `epsilon`, the whole horizontal segment lies in `1/2<=Re(s)<=5/8`, where `A` is holomorphic and nonzero. Direct logarithmic differentiation gives

\[
 A'/A=1/s+1/(s-1)-\tfrac12\log\pi+\tfrac12\psi(s/2),
\]

so uniform digamma Stirling and a compact-height bound give `|A'/A|<=C log(|t|+3)` on this strip. There is no pole or zero at the strip's real points; in particular the zero at1 is outside it. Integrating the logarithmic derivative gives the exact ratio `g_epsilon(s)=A(s+epsilon)/A(s)`, irrespective of any principal-log convention, and

\[
 |g_\epsilon(s)-1|
 \le C\epsilon\log(|t|+3)(|t|+3)^{C\epsilon}.
\]

Choose a fixed sufficiently small upper bound on `epsilon` so the squared power is, for example, at most1/4. The displayed height factor is then square integrable against `dnu` uniformly, whence

\[
 \|g_\epsilon-1\|_{L^2(d\nu)}=O(\epsilon).
\]

The completed and uncompleted ratios satisfy exactly

\[
 \frac{\zeta(s)}{\zeta(s+\epsilon)}
 =H_\epsilon(it)g_\epsilon(s).
\]

Therefore the triangle inequality and contractivity imply

\[
 J_\epsilon^{1/2}
 \le (J^\xi_\epsilon)^{1/2}+\|g_\epsilon-1\|_{L^2(d\nu)}
 =O(\epsilon^{1/2}),
\]

which proves the required prior upper bound. The local small-epsilon estimate already suffices for the array. To extend the assertion to the source's full `0<epsilon<=1/2`, note that uniform gamma-ratio Stirling and a compact-height bound give `|g_epsilon(s)|<=C(|t|+3)^(1/4)` on that full parameter range. The possible numerator zero of `A(s+epsilon)` at1 is harmless. Contractivity then bounds `J_epsilon` uniformly. On any remaining compact epsilon interval `[epsilon_0,1/2]`, this uniform bound is at most a fixed constant times `epsilon`, completing the full stated range.

## 4. Independent comparison with the source residue proof

The actual source uses another valid argument. Proposition4(ii),pp6–7, bounds the squared ratio by `1+C epsilon |s|^(1/2)`; integration gives `K_epsilon<=1+O(epsilon)`. With `L_epsilon` the corresponding integral of the ratio itself, conjugation makes it real and Eq11,p7, is `J=K-2L+1`.

For Proposition5, set `Q(s)=[zeta(s)/zeta(s+epsilon)]/[s(1-s)]`. Under RH it has only the double pole at1 in the right half-plane. The pole of the shifted denominator at `1-epsilon` is a **zero** of the ratio, not an extra pole. Proposition4(iii) makes the right closing arc vanish. Closing clockwise gives minus the residue, whose sign and expansion were independently recalculated:

\[
 L_\epsilon=(\gamma_E-1)R(1+\epsilon)+R'(1+\epsilon)
 =1-(\gamma_E+1)\epsilon+O(\epsilon^2),\quad R=1/\zeta.
\]

Indeed `R(1+epsilon)=epsilon-gamma_E epsilon²+O(epsilon³)`. These identities give `J<<epsilon` exactly as printed. The source's proof and the Poisson proof have compatible normalizations and hypotheses. No issue was found in the inspected contour orientation, pole list, convergence or uniformity steps. The source's lower-bound remark involving a known simple zero is not required and its numerical/simple-zero provenance was not audited here.

## 5. Transfer to the moving-array norm and fair frontier claim

For fixed `q>=1`, the critical-line inequality `|s|>=1/2` gives

\[
 \|\zeta(s)/\zeta(s+\epsilon)-1\|_q^2
 \le2^{2q-2}J_\epsilon=O_q(\epsilon).
\]

Combine with the independently reviewed comparison in `THM-E-W313`, whose error is `O_(q,c)(alpha_N^(-1/2))` plus an exponentially smaller term. With `epsilon_N=c/loglog N`, `alpha_N=epsilon_N log N`, one has `alpha_N^(-1/2)=o(sqrt(epsilon_N))`. Thus the exact proposed array satisfies, under RH and for **every fixed `c>0`**,

\[
 d_q(V_N)=O_{q,c}((\log\log N)^{-1/2}),\qquad
 d_q(V_N)^2=O_{q,c}((\log\log N)^{-1}).
\]

This is the W314 transfer of an already published ratio estimate to the separately reconstructed explicit array. It does not alter the historical Báez-Duarte1/3 proof, assert a new best Nyman–Beurling distance bound, or establish historical novelty of the array. In particular the same Balazard–de Roton source proves a substantially stronger optimized-distance upper bound through a different shifted Möbius array and its sharper Proposition3. That result must not be conflated with this moving taper.
