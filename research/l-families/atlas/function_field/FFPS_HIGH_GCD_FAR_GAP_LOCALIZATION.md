# Only high far-separated reduced product shells remain

Status: **exact reduced-gap decomposition of the high gcd-wavelet sector,
unconditional absolute control of every prescribed subpower additive-gap
window, and an exact high/far gate equivalent to `HIGHGCDWAVE`; the far gate,
RH, and GRH remain open**.

Architecture: **Architecture A only**.

Bounded replay:
[`ffps_high_gcd_far_gap_localization.py`](ffps_high_gcd_far_gap_localization.py).
Canonical fixture:
[`ffps_high_gcd_far_gap_localization.json`](ffps_high_gcd_far_gap_localization.json).

Frozen source: PR #760 head
`680be76bd31acdd96925d0b73f1a469226a19c9f`, specifically the high balanced
gcd-wave localization and shifted-zeta Fourier packets pinned by the replay.

## 0. Outcome

The high-gcd predecessor reduces the open Architecture A burden to
\[
\begin{aligned}
 \mathfrak O_\alpha(H)
 =\sum_g{\kappa_2(g)\over g}
 \sum_{\substack{(a,b)=(ab,g)=1\\(a,b)\ne(1,1)}}
 {\mu(a)\mu(b)\over\sqrt{ab}}
 \sum_{I\in\mathscr D_H}
 \mathcal W_I^\alpha(ga)
 \overline{\mathcal W_I^\alpha(gb)} ,
\end{aligned}
\tag{0.1}
\]
where all variables are squarefree and 67-free, and every surviving reduced
pair satisfies
\[
 {1\over64}<a/b<64.
\tag{0.2}
\]

The earlier packet pays absolutely for `min(a,b)<=B(H)` whenever
`B(H)=H^{o(1)}`.  There is a second unconditional localization.  For `G>=0`,
let `O_alpha^near(H;G)` be the portion of (0.1) with
\[
 |a-b|\le G.
\tag{0.3}
\]
Then
\[
\boxed{
 |\mathfrak O_\alpha^{\rm near}(H;G)|
 \ll_{\mathcal R}
 L_H(2G+1)
 \bigl(1+\log(4H^2+G+2)\bigr)^{12}.
}
\tag{0.4}
\]

Thus every fixed reduced-product shift and every prescribed subpower
additive-gap window are harmless without Möbius cancellation.

For prescribed functions
\[
 B(H)=H^{o(1)},\qquad G(H)=H^{o(1)},
\tag{0.5}
\]
define `HIGHFARGCDWAVE[B,G]` by restricting (0.1) to
\[
\boxed{
 a>B(H),\quad b>B(H),\quad |a-b|>G(H),\quad {1\over64}<a/b<64.
}
\tag{0.6}
\]
Then, at the all-positive-exponent scale,
\[
\boxed{
 \mathrm{HIGHFARGCDWAVE}[B,G]
 \Longleftrightarrow
 \mathrm{HIGHGCDWAVE}[B]
 \Longleftrightarrow
 \mathrm{OFFGCDWAVE}
 \Longleftrightarrow
 \mathrm{PRIMCAR}
 \Longrightarrow\mathrm{RH}.
}
\tag{0.7}
\]

The remaining pair is therefore simultaneously:

```text
high in both reduced product-shell coordinates;
balanced multiplicatively;
far from every prescribed subpower additive diagonal;
coprime in the reduced variables and to the positive common shell g.
```

This is a sharper Type-II/dispersion target.  It does not prove its estimate.

## 1. Absolute near-gap estimate

The predecessor proves
\[
 \sum_{I\in\mathscr D_H}
 |\mathcal W_I^\alpha(ga)\mathcal W_I^\alpha(gb)|
 \le
 L_H\|\mathcal R\|_\infty^2
 \tau(ga)\tau(gb).
\tag{1.1}
\]
On the support of (0.1), `g,a,b` are pairwise coprime and squarefree.  Hence
\[
 \tau(ga)=\tau(g)\tau(a),\qquad
 \tau(gb)=\tau(g)\tau(b),\qquad
 \kappa_2(g)\le\tau(g).
\tag{1.2}
\]
The absolute common-shell weight is therefore bounded by
\[
 {d_8(g)\over g}.
\tag{1.3}
\]

Write `b=a+h`.  Dropping coprimality and squarefreeness can only enlarge the
absolute sum.  For one integer shift `h`, Cauchy gives
\[
\begin{aligned}
 \sum_{\substack{a\ge1\\a+h\ge1}}
 {\tau(a)\tau(a+h)\over\sqrt{a(a+h)}}
 &\le
 \left(\sum_{a\le X}{\tau(a)^2\over a}\right)^{1/2}
 \left(\sum_{b\le X+G}{\tau(b)^2\over b}\right)^{1/2}.
\end{aligned}
\tag{1.4}
\]
The local inequality
\[
 \tau(n)^2\le d_4(n)
\tag{1.5}
\]
and the four-fold divisor expansion imply
\[
 \sum_{n\le Y}{\tau(n)^2\over n}
 \le
 \sum_{n\le Y}{d_4(n)\over n}
 \le(1+\log Y)^4.
\tag{1.6}
\]
There are `2G+1` shifts.  The elementary eight-fold bound
\[
 \sum_{g\le X}{d_8(g)\over g}\le(1+\log X)^8
\tag{1.7}
\]
then proves (0.4), using the product-shell support
`ga,gb<=4H^2/67^alpha`.

No Chowla theorem, zero-free region, or cancellation in `mu(a)mu(b)` is used.

## 2. Exact three-way partition

For `B,G>=0`, split the off-diagonal terms into the disjoint sectors
\[
\begin{aligned}
 \mathfrak O_\alpha^{\rm low}
 &: \min(a,b)\le B,\\
 \mathfrak O_\alpha^{\rm high,near}
 &: \min(a,b)>B,\quad |a-b|\le G,\\
 \mathfrak O_\alpha^{\rm high,far}
 &: \min(a,b)>B,\quad |a-b|>G.
\end{aligned}
\tag{2.1}
\]
The previous packet pays the first sector for subpower `B`; (0.4) pays the
second for subpower `G`.  Therefore the full off-diagonal estimate and the
third-sector estimate are equivalent after exponent renaming.  This proves
(0.7).

The cutoffs are prescribed independently of any hypothetical zero or bad
scale.

## 3. Shifted-correlation normal form

In the far sector write
\[
 b=a+h,\qquad |h|>G.
\tag{3.1}
\]
The reduced coprimality becomes
\[
 (a,b)=1\Longleftrightarrow(a,h)=1.
\tag{3.2}
\]
Thus the exact remaining form is
\[
\boxed{
\begin{aligned}
 \mathfrak O_\alpha^{\rm high,far}(H;B,G)
 =\sum_g{\kappa_2(g)\over g}
 \sum_{\substack{|h|>G}}
 \sum_{\substack{a>B,\ a+h>B\\
                  (a,h)=1,\ (a(a+h),g)=1\\
                  1/64<a/(a+h)<64}}
 &{\mu(a)\mu(a+h)\over\sqrt{a(a+h)}}\\[-1mm]
 &\times\sum_{I\in\mathscr D_H}
 \mathcal W_I^\alpha(ga)
 \overline{\mathcal W_I^\alpha(g(a+h))}.
\end{aligned}}
\tag{3.3}
\]
All sums are finite through native product-shell support.

This is an averaged shifted-Möbius correlation, but a qualitative
density-saving averaged Chowla theorem is not automatically enough.  The
target is subpower after the half-weight normalization and the assembled
`g,h,I` summation.  A proof must preserve cancellation across those variables
or produce a square-root-scale bilinear estimate.

## 4. Relation to the Fourier packet

The shifted-zeta predecessor proves that each isolated untruncated Fourier
mode carries
\[
 {1\over
 \zeta^{(67)}(s-i\xi)\zeta^{(67)}(s+i\xi)}.
\tag{4.1}
\]
The present theorem removes all small reduced additive shifts before that
Fourier analysis.  Consequently the remaining analytic mechanism cannot be
a theorem only about finitely many fixed shifts.  It must exploit long-shift
averaging, common-shell averaging, the paired frequency integral, or a new
signed reflection identity.

## 5. Scope firewall

- The gap is in the reduced **product-shell** variables `a,b` of the gcd
  decomposition, not in the original primitive orientation variables.
- The bound (0.4) is absolute and does not estimate the far sector.
- `HIGHFARGCDWAVE` remains an RH-strength open gate.
- Standard averaged Chowla results are not silently imported.
- Architecture B is not used.

**No HIGHFARGCDWAVE, HIGHGCDWAVE, OFFGCDWAVE, PRIMCAR, RH, or GRH estimate
is proved.**

## 6. Proof ledger

| statement | grade |
|---|---|
| near-gap bound (0.4) | **PROVED UNCONDITIONALLY** |
| three-way partition (2.1) | **PROVED EXACT** |
| shifted form (3.3) | **PROVED EXACT** |
| HIGHFARGCDWAVE equivalent to HIGHGCDWAVE | **PROVED AT ALL-EXPONENT SCALE** |
| HIGHGCDWAVE to RH chain | **IMPORTED FROM FROZEN SOURCE** |
| HIGHFARGCDWAVE / RH / GRH | **NOT PROVED** |

## 7. Bounded replay

```text
python -B research/l-families/atlas/function_field/ffps_high_gcd_far_gap_localization.py --check
python -B -O research/l-families/atlas/function_field/ffps_high_gcd_far_gap_localization.py --check
python -B -m unittest tests.test_ffps_high_gcd_far_gap_localization
python -B -O -m unittest tests.test_ffps_high_gcd_far_gap_localization
```
