# High balanced reduced rays are the only remaining gcd-wavelet sector

Status: **exact factor-64 reduced-ratio localization, unconditional absolute
control of every prescribed subpower reduced-height sector, and an exact high
balanced gate equivalent to `OFFGCDWAVE`; the high gate, RH, and GRH remain
open**

Architecture: **Architecture A only**.

Bounded replay:
[`ffps_high_gcd_wave_localization.py`](ffps_high_gcd_wave_localization.py).
Canonical fixture:
[`ffps_high_gcd_wave_localization.json`](ffps_high_gcd_wave_localization.json).

Frozen predecessor: the shared-divisor Gram packet at
`0855a61a2c719b4f93ad02d5aa8390ddff1b7765`.

## 0. Outcome

The predecessor reduces RH to the signed off-diagonal gcd-wavelet correlation
\[
\begin{aligned}
 \mathfrak O_\alpha(H)
 =\sum_g{\kappa_2(g)\over g}
 \sum_{\substack{(a,b)=(ab,g)=1\\(a,b)\ne(1,1)}}
 {\mu(a)\mu(b)\over\sqrt{ab}}
 \sum_{I\in\mathscr D_H}
 \mathcal W_I^\alpha(ga)
 \overline{\mathcal W_I^\alpha(gb)} .
\end{aligned}
\tag{0.1}
\]

Every nonzero wavelet in a height block `(H,2H]` obeys
\[
 {H^2\over16\,67^\alpha}<N\le {4H^2\over67^\alpha}.
\tag{0.2}
\]
Consequently, if both factors in (0.1) survive, then
\[
\boxed{{1\over64}< {a\over b}<64.}
\tag{0.3}
\]
The common shell `g` cancels from the ratio.

Fix `B>=1` and let `O_alpha^low(H;B)` denote the portion of (0.1) with
`min(a,b)<=B`.  Equation (0.3) forces
\[
 a,b\le64B.
\tag{0.4}
\]
This finite-width sector is unconditionally harmless:
\[
\boxed{
 |\mathfrak O_\alpha^{\rm low}(H;B)|
 \ll_{\mathcal R}
 L_H B^2\bigl(1+\log(4H^2+2)\bigr)^8.
}
\tag{0.5}
\]

Hence, for every prescribed function `B(H)=H^{o(1)}`, the low sector is
`H^{o(1)}`.  Define the complementary gate
\[
\mathrm{HIGHGCDWAVE}[B]:\qquad
 |\mathfrak O_\alpha^{\rm high}(H;B(H))|
 \ll_\varepsilon(2H)^\varepsilon,
\tag{0.6}
\]
where
\[
 a>B(H),\qquad b>B(H),\qquad {1\over64}<a/b<64.
\tag{0.7}
\]
Then at the all-positive-exponent scale
\[
\boxed{
 \mathrm{HIGHGCDWAVE}[B]
 \Longleftrightarrow
 \mathrm{OFFGCDWAVE}
 \Longleftrightarrow
 \mathrm{COREAGG}
 \Longleftrightarrow
 \mathrm{PRIMCAR}
 \Longrightarrow\mathrm{RH}.
}
\tag{0.8}
\]

Thus every fixed reduced ray, every bounded collection of rays, and every
prescribed subpower reduced-height region has been removed.  The only
Architecture A burden is a genuinely high, balanced, coprime bilinear
Möbius correlation, averaged over the positive common shell `g`.

## 1. Ratio localization

If `W_I^alpha(N)` is nonzero, one orientation `x|N` survives both the
ratio-sixteen autocorrelation and the physical height block.  Writing
\[
 X=67^\alpha x,\qquad Y=N/x,
\]
one has `H<max(X,Y)<=2H` and
`min(X,Y)>=max(X,Y)/16`.  Therefore
\[
 {H^2\over16}<XY=67^\alpha N\le4H^2,
\]
which proves (0.2).

Apply (0.2) to `N=ga` and `M=gb`.  Dividing the two inequalities gives
(0.3).  No asymptotic estimate is used.

## 2. Absolute low-sector estimate

The predecessor proves the dyadic square-function bound
\[
 \sum_{I\in\mathscr D_H}|\mathcal W_I^\alpha(N)|^2
 \le L_H\|\mathcal R\|_\infty^2\tau(N)^2.
\tag{2.1}
\]
Cauchy in `I` therefore gives
\[
 \sum_I|\mathcal W_I^\alpha(ga)\mathcal W_I^\alpha(gb)|
 \le L_H\|\mathcal R\|_\infty^2\tau(ga)\tau(gb).
\tag{2.2}
\]

On the support of (0.1), `g,a,b` are squarefree and `(g,ab)=1`, so
\[
 \tau(ga)=\tau(g)\tau(a),\qquad
 \tau(gb)=\tau(g)\tau(b),\qquad
 \kappa_2(g)\le\tau(g).
\tag{2.3}
\]
Thus the `g` weight in the absolute majorant is at most
\[
 {8^{\omega(g)}\over g}={d_8(g)\over g}.
\tag{2.4}
\]
The elementary eight-fold divisor expansion gives
\[
 \sum_{g\le X}{d_8(g)\over g}\le(1+\log X)^8.
\tag{2.5}
\]

For `Y>=1`,
\[
 \sum_{n\le Y}{\tau(n)\over\sqrt n}
 =\sum_{uv\le Y}{1\over\sqrt{uv}}
 \le\left(\sum_{u\le Y}{1\over\sqrt u}\right)^2
 \le4Y.
\tag{2.6}
\]
Using `Y=64B` in the two reduced variables and
`g<=4H^2/67^alpha` proves (0.5), with an absolute numerical factor that is
irrelevant at subpower scale.

Notice what was not used: no cancellation in `mu(a)mu(b)`, no prime number
theorem, and no estimate for an individual common shell.

## 3. Exact high gate

Let
\[
 \mathfrak O_\alpha
 =\mathfrak O_\alpha^{\rm low}(B)
  +\mathfrak O_\alpha^{\rm high}(B).
\tag{3.1}
\]
For prescribed `B(H)=H^{o(1)}`, equation (0.5) is subpower.  Therefore an
all-positive-exponent bound for either the full off-diagonal or the high
piece implies the same family of bounds for the other after renaming the
exponent.  This proves the first equivalence in (0.8); the rest is imported
from the frozen predecessor.

The cutoff may grow arbitrarily slowly.  It is not chosen after seeing an
off-line zero or a bad scale.

## 4. Relation to classical bilinear forms

The remaining geometry is now rigid:
```text
squarefree a,b;
(a,b)=(ab,g)=1;
a,b both above every prescribed subpower cutoff;
1/64 < a/b < 64;
positive outer weight kappa_2(g)/g;
signed divisor-wavelet correlation over dyadic height blocks.
```

This is the natural Type-II region.  A Type-I estimate controlling one short
reduced variable cannot close it, because every such region has already been
paid by (0.5).

A successful proof must obtain cancellation with both reduced variables
long.  It may average over `g` and over dyadic height blocks; a pointwise
theorem for each `g` is stronger than the exact gate.

## 5. Scope firewall

- `HIGHGCDWAVE` is open.
- The estimate (0.5) is absolute and applies only when one reduced coordinate
  is at most the prescribed cutoff.
- The fixed ratio window does not itself give Möbius cancellation.
- No fixed-shift Chowla theorem is imported.
- Architecture B is not used.

**No HIGHGCDWAVE, OFFGCDWAVE, COREAGG, PRIMCAR, PRIMLS, RH, or GRH estimate
is proved.**

## 6. Proof ledger

| statement | grade |
|---|---|
| product-shell support (0.2) | **PROVED EXACT** |
| reduced ratio localization (0.3) | **PROVED EXACT** |
| low-sector bound (0.5) | **PROVED UNCONDITIONALLY** |
| HIGHGCDWAVE equivalent to OFFGCDWAVE | **PROVED AT ALL-EXPONENT SCALE** |
| OFFGCDWAVE to RH chain | **IMPORTED FROM FROZEN PREDECESSOR** |
| HIGHGCDWAVE / RH / GRH | **NOT PROVED** |

## 7. Bounded replay

```text
python -B research/l-families/atlas/function_field/ffps_high_gcd_wave_localization.py --check
python -B -O research/l-families/atlas/function_field/ffps_high_gcd_wave_localization.py --check
python -B -m unittest tests.test_ffps_high_gcd_wave_localization
python -B -O -m unittest tests.test_ffps_high_gcd_wave_localization
```
