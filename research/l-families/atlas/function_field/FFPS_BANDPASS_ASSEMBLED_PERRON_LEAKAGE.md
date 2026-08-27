# Band-pass assembly survives exactly, but the Perron max cusp refills every notch linearly

Status: **exact band-pass assembled-wavelet identity, exact bilateral
double-Perron bridge, exact Barnes collapse, and exact linear max-tilt leakage
theorem; no contour estimate and no proof of RH or GRH**

Bounded exact replay:
[`ffps_bandpass_assembled_perron_leakage.py`](ffps_bandpass_assembled_perron_leakage.py).
Canonical summary:
[`ffps_bandpass_assembled_perron_leakage.json`](ffps_bandpass_assembled_perron_leakage.json).

Read first:

1. [`FFPS_BANDPASS_BETA_ENERGY_LADDER.md`](FFPS_BANDPASS_BETA_ENERGY_LADDER.md);
2. [`FFPS_ASSEMBLED_BETA_PERRON_FOURIER_BRIDGE.md`](FFPS_ASSEMBLED_BETA_PERRON_FOURIER_BRIDGE.md).

The replay pins the committed beta boundary sources at
`b870366141fe8d5f43d5b81f6e50a67d2a888070`, the band-pass predecessor at
`05aaabe69060c24c8db4ca33c350e109231960f1`, and the audited assembled
predecessor at `afd49590f1a7e70e68054b8932eb9cadfaa62c40` by Git blob ID. No
front door or predecessor is modified here.

## 0. Outcome

Fix

\[
 \varepsilon,\ell>0,
 \qquad r\ge1,
 \qquad j\ge0,
\]

and let

\[
 B_{r,j}=\eta_\ell^{*j}*\Delta_\varepsilon^rK_{\rm bd},
 \qquad
 \mathcal R_{r,j}(x)
 =\int_{\mathbf R}B_{r,j}(u)B_{r,j}(u+x)du.
\tag{0.1}
\]

The band-pass packet proves

\[
 \widehat{\mathcal R}_{r,j}(t)
 ={\lvert1-e^{-i\varepsilon t}\rvert^{2r}\over\varepsilon^{2r}}
 |\widehat\eta_\ell(t)|^{2j}
 |\widehat K_{\rm bd}(t)|^2,
\tag{0.2}
\]

so the translation-invariant weight has an exact zero of order `2r` at
`t=0`. It also proves that the corresponding sharp prefix energy

\[
 \mathcal E_{r,j}(X)
 =\sum_{m,n\le X}{\beta(m)\beta(n)\over\sqrt{mn}}
 \mathcal R_{r,j}\!\left(\log{m\over n}\right)
\tag{0.3}
\]

is RH-equivalent.

This successor proves four facts.

1. The complete assembled divisor-wavelet identity survives **verbatim**
   after replacing `R` by `R_(r,j)`. It remains exactly RH-equivalent.
2. The sharp prefix has a bilateral double-Perron formula in which
   `Rhat_(r,j)(t)` is not tilted and its exact `t=0` notch remains visible.
3. Changing to total and relative Perron variables and eliminating the
   relative contour gives the exact Barnes identity

   \[
    \boxed{
    {1\over2\pi i}\int_{(a)}
    {e^{-vx}\over(z/2+v)(z/2-v)}dv
    ={e^{-z|x|/2}\over z},
    \qquad
    -{\Re z\over2}<a<{\Re z\over2}.}
   \tag{0.4}
   \]

   Thus the familiar max cusp is exactly what relative-contour elimination
   creates.
4. That cusp refills every nontrivial finite-difference notch to **first
   order in `z`**, independently of `r`.

The fourth statement is not merely generic. Put

\[
 F_{r,j}(x)=\int_{-\infty}^xB_{r,j}(u)du.
\tag{0.5}
\]

Then `F_(r,j)` is compact and nonzero, and

\[
 \boxed{
 \widehat{\mathcal R_{r,j}(\cdot)e^{-z|\cdot|/2}}(0)
 =z\|F_{r,j}\|_2^2+O_{r,j,\varepsilon,\ell}(|z|^2).}
\tag{0.6}
\]

The coefficient is strictly positive. Raising `r` never changes the leakage
from linear to `z^(2r)` or any higher power. Repeated notching improves the
untwisted `t` zero but does not improve the order of the Perron max leakage.

## 1. The exact band-pass assembled divisor wavelet

Write

\[
 (c_0,c_1,c_2)=(1,-2,1).
\]

For squarefree `67`-free `N`, retain the harmonic common-factor sum

\[
 H_N(Y)=
 \sum_{\substack{g\le Y,\ g\ \mathrm{squarefree}\\(g,67N)=1}}{1\over g}.
\tag{1.1}
\]

Define the band-pass assembled wavelet

\[
\begin{aligned}
 \mathscr W_X^{r,j}(N)
 ={}&\sum_{\alpha,\gamma=0}^2
 {c_\alpha c_\gamma\over67^{(\alpha+\gamma)/2}}
 \sum_{a\mid N}
 \mathcal R_{r,j}\!\left(
  \log{67^{\alpha-\gamma}a^2\over N}
 \right)\\
 &\qquad\times
 H_N\!\left(
 {X\over\max(67^\alpha a,67^\gamma N/a)}
 \right).
\end{aligned}
\tag{1.2}
\]

Exactly the same unique decomposition

\[
 m=67^\alpha ga,
 \qquad
 n=67^\gamma gb,
 \qquad
 N=ab
\tag{1.3}
\]

used by the assembled predecessor applies to an arbitrary ratio kernel.
It does not use positivity, the value of the support radius, or the Fourier
transform of that kernel. Therefore

\[
 \boxed{
 \mathcal E_{r,j}(X)
 =\sum_{\substack{N\ \mathrm{squarefree}\\67\nmid N}}
 {\mu(N)\over\sqrt N}\mathscr W_X^{r,j}(N).}
\tag{1.4}
\]

This is a finite exact identity. Combining it with the band-pass energy
criterion gives

\[
 \boxed{
 \mathrm{RH}
 \Longleftrightarrow
 \left|
 \sum_N{\mu(N)\over\sqrt N}\mathscr W_X^{r,j}(N)
 \right|=X^{o(1)}.}
\tag{1.5}
\]

Thus the sharp assembled RH identity survives verbatim. What changes is the
kernel's spectral shape, not the arithmetic source reindexing.

## 2. A double-Perron formula which retains the notch

Let

\[
 B_\beta(w)={1-67^{-w}\over\zeta(w)}
 =\sum_{n\ge1}{\beta(n)\over n^w}
 \qquad(\Re w>1).
\tag{2.1}
\]

To avoid the classical half-weight at a Perron endpoint, take `Y>0` outside
the positive integers and define the sharp prefix by `m,n<Y`. For an integer
cap `X`, one may take any `Y` in `(X,X+1)`, for example `Y=X+1/2`.

For `c_1,c_2>1/2`, iterated truncated Perron inversion and the absolutely
convergent beta series give

\[
\boxed{
\begin{aligned}
 \mathcal E_{r,j}(<Y)
 ={}&{1\over(2\pi i)^2}
 \int_{(c_1)}\int_{(c_2)}
 {Y^{z_1+z_2}\over z_1z_2}\\
 &\times\left\{
 {1\over2\pi}\int_{\mathbf R}
 \widehat{\mathcal R}_{r,j}(t)
 B_\beta(1/2+z_1-it)
 B_\beta(1/2+z_2+it)dt
 \right\}dz_2dz_1.
\end{aligned}}
\tag{2.2}
\]

The two Perron integrals in (2.2) are understood as the standard iterated
truncated limits. The Dirichlet series and the `t` integral are absolutely
convergent on the displayed lines: `B_(r,j)` is in `L2`, so
`Rhat_(r,j)=|Bhat_(r,j)|^2` is in `L1`.

Crucially, the kernel in (2.2) is the unmodified
`Rhat_(r,j)(t)`. Therefore

\[
 \widehat{\mathcal R}_{r,j}(t)
 =|\widehat K_{\rm bd}(0)|^2t^{2r}
 +O_{r,j,\varepsilon,\ell}(t^{2r+2})
\tag{2.3}
\]

at zero. The sharp two-contour coordinate retains the complete notch.

No contour displacement toward `Re(z_1)=Re(z_2)=0` is proved. Formula (2.2)
trades the max cusp for two independently shifted reciprocal-zeta sources
and two Perron denominators.

## 3. Total/relative variables and the Barnes normalization

Put

\[
 z=z_1+z_2,
 \qquad
 v={z_1-z_2\over2},
\tag{3.1}
\]

so

\[
 z_1={z\over2}+v,
 \qquad
 z_2={z\over2}-v,
 \qquad
 dz_1\wedge dz_2=-dz\wedge dv.
\tag{3.2}
\]

The Jacobian has absolute value one, and

\[
 z_1z_2=(z/2+v)(z/2-v).
\tag{3.3}
\]

For a source pair, put `x=log(m/n)`. Its two Perron powers become

\[
 m^{-z_1}n^{-z_2}
 =(mn)^{-z/2}e^{-vx}.
\tag{3.4}
\]

The original lines put the relative line strictly between the two poles:

\[
 -\Re(z)/2<\Re(v)<\Re(z)/2.
\]

If `x>0`, close right. The pole `v=z/2` has residue
`-e^(-zx/2)/z`, while the right closure reverses orientation, giving
`+e^(-zx/2)/z`. If `x<0`, close left; the pole `v=-z/2` has residue
`e^(zx/2)/z`. Both cases give (0.4). The value at `x=0` follows by
continuity.

Equivalently, the sharp product cutoff satisfies

\[
 \mathbf1_{m<Y}\mathbf1_{n<Y}
 =\mathbf1_{\max(m,n)<Y},
\]

and single Perron inversion of the right side contributes

\[
 {Y^z\over z}\max(m,n)^{-z}
 ={Y^z\over z}(mn)^{-z/2}e^{-z|x|/2}.
\tag{3.5}
\]

Thus the Barnes residue calculation and the elementary max identity have
the same normalization, including the factor `1/z`.

On a safe line `Re(z)>1`, Fourier inversion now produces the one-variable
sharp formula

\[
\begin{aligned}
 \mathcal E_{r,j}(<Y)
 ={1\over2\pi i}\int_{(c)}{Y^z\over z}
 \left\{{1\over2\pi}\int_{\mathbf R}
 \widehat{\mathcal R_{r,j,z}}(t)
 B_\beta(s-it)B_\beta(s+it)dt\right\}dz,
\tag{3.6}
\end{aligned}
\]

where

\[
 s={1+z\over2},
 \qquad
 \mathcal R_{r,j,z}(x)
 =\mathcal R_{r,j}(x)e^{-z|x|/2}.
\tag{3.7}
\]

The exact notch in (2.2) and the tilted kernel in (3.6) are therefore two
coordinates on the same sharp cutoff. The tilt is not an arbitrary analytic
artifact; it is the residue of the eliminated relative contour.

## 4. The absolute-lag identity

The finite differences give

\[
 \int_{\mathbf R}B_{r,j}(x)dx=0.
\]

Hence the cumulative `F_(r,j)` in (0.5) is compactly supported. It is
nonzero because its distributional derivative is the nonzero kernel
`B_(r,j)`.

For any real compact integrable mean-zero `B`, with cumulative `F`, let

\[
 R(x)=\int B(u)B(u+x)du.
\]

Then

\[
\begin{aligned}
 \int_{\mathbf R}|x|R(x)dx
 &=\iint_{\mathbf R^2}B(u)B(v)|u-v|dudv\\
 &=-2\int_{\mathbf R}|F(y)|^2dy.
\end{aligned}
\tag{4.1}
\]

One proof sets

\[
 P(u)=\int|u-v|B(v)dv.
\]

Distributionally `P''=2B`, while mean zero gives `P'=2F` and makes `P'`
vanish off a compact interval. Integration by parts yields

\[
 \int BP={1\over2}\int P''P
 =-{1\over2}\int(P')^2
 =-2\int F^2,
\]

proving (4.1). Applying this to `B_(r,j)` gives the strict inequality

\[
 \boxed{
 \int|x|\mathcal R_{r,j}(x)dx
 =-2\|F_{r,j}\|_2^2<0.}
\tag{4.2}
\]

The cumulative also has the explicit source-faithful form

\[
 \boxed{
 F_{r,j}
 =\eta_\ell^{*j}*\eta_\varepsilon*
 \Delta_\varepsilon^{r-1}K_{\rm bd}.}
\tag{4.3}
\]

Indeed `D(eta_epsilon*f)=Delta_epsilon f`, and all operators commute.

## 5. Exact linear leakage and quantitative bounds

Put

\[
 L_{r,j}(z,t)
 =\widehat{\mathcal R_{r,j,z}}(t)
 =\int\mathcal R_{r,j}(x)e^{-z|x|/2}e^{-itx}dx.
\tag{5.1}
\]

Because `R_(r,j)` is compactly supported, this is entire in `z` and smooth
in real `t`. At `t=0`, use `integral R=0`, expand the exponential, and apply
(4.2):

\[
\begin{aligned}
 L_{r,j}(z,0)
 &=-{z\over2}\int|x|\mathcal R_{r,j}(x)dx+O(|z|^2)\\
 &=z\|F_{r,j}\|_2^2+O(|z|^2).
\end{aligned}
\tag{5.2}
\]

This proves (0.6), including strict positivity of its leading coefficient.

There are explicit support-only bounds. Let

\[
 S=4\log2+r\varepsilon+j\ell.
\]

Since `supp R` lies in `[-S,S]` and
`||R||_1<=||B||_1^2`, for every complex `z` and real `t`,

\[
 \boxed{
 |L_{r,j}(z,t)-\widehat{\mathcal R}_{r,j}(t)|
 \le {|z|S\over2}e^{|z|S/2}\|B_{r,j}\|_1^2.}
\tag{5.3}
\]

Taylor's remainder gives the sharper zero-frequency expansion

\[
 \boxed{
 \left|L_{r,j}(z,0)-z\|F_{r,j}\|_2^2\right|
 \le {|z|^2S^2\over8}e^{|z|S/2}\|B_{r,j}\|_1^2.}
\tag{5.4}
\]

Finally, evenness and compact support give the joint local form

\[
 \boxed{
 L_{r,j}(z,t)
 =c_{\rm bd}^2t^{2r}
  +zA_{r,j}
  +O_{r,j,\varepsilon,\ell}
   (t^{2r+2}+|z|t^2+|z|^2),}
\tag{5.5}
\]

where

\[
 c_{\rm bd}=3(1-\sqrt2)^2(\log2)^2,
 \qquad
 A_{r,j}=\|F_{r,j}\|_2^2>0.
\]

For positive real `z`, the two leading terms balance at the local scale

\[
 |t|\asymp z^{1/(2r)}
\tag{5.6}
\]

up to the fixed coefficient ratio. This is a local diagnostic, not an
arithmetic estimate.

## 6. The exact no-go and the live escape

The no-go is precise:

> No nonzero fixed finite-difference autocorrelation can retain a
> higher-than-linear zero-frequency leakage order after the physical
> Perron max tilt `exp(-z|x|/2)` is introduced.

The obstruction is the cusp `|x|`, whose first absolute moment is not one of
the polynomial moments killed by repeated differencing. In fact its
coefficient is forced positive by (4.2). Adding any finite number of fixed
box convolutions changes `A_(r,j)` but never makes it zero.

The live escape is equally precise: retain the bilateral relative contour
`v`. Formula (2.2) keeps the exact `t^(2r)` notch. What it does not provide is
an estimate for two independently shifted reciprocal-zeta factors with the
coupled denominators

\[
 (z/2+v)^{-1}(z/2-v)^{-1}.
\]

Thus the sharp analytical choice is now visible:

```text
retain v  -> exact t=0 notch, but a genuinely bilateral contour problem;
remove v  -> one max variable, but forced linear zero-mode leakage.
```

Neither side is estimated here.

## 7. Scope firewalls

- The parameters remain fixed independently of `X`, the Perron contours,
  and every zero.
- The leakage expansion is local as `z->0`; it does not control a complete
  vertical contour with large imaginary part.
- The support bounds (5.3)--(5.4) are kernel bounds, not beta cancellation.
- The crossover (5.6) does not show that the corresponding frequency window
  contributes a main term or an error term to the arithmetic integral.
- The double-Perron identity preserves the notch algebraically but supplies
  no contour shift.
- No assembled-wavelet estimate, `ASMPERRON`, RH, or GRH theorem is proved.

## 8. Proof and scope ledger

| statement | grade |
|---|---|
| band-pass assembled wavelet (1.2)--(1.4) | **PROVED EXACT BY KERNEL-INDEPENDENT SOURCE REINDEXING** |
| RH equivalence (1.5) | **PROVED FROM PINNED BAND-PASS ENERGY THEOREM** |
| bilateral double-Perron formula (2.2) | **PROVED AS ITERATED SHARP PERRON INVERSION OFF ENDPOINTS** |
| retention of exact `t^(2r)` notch in double-Perron coordinates | **PROVED EXACT** |
| Barnes identity and `1/z` normalization (0.4) | **PROVED BY BOTH RESIDUES** |
| equivalence of Barnes collapse and the max cusp | **PROVED EXACT** |
| absolute-lag identity (4.1)--(4.2) | **PROVED EXACT** |
| strict linear leakage (5.2) | **PROVED FOR EVERY NONZERO BAND-PASS RUNG** |
| bounds (5.3)--(5.4) and joint expansion (5.5) | **PROVED FROM COMPACT SUPPORT** |
| improvement of leakage order by increasing `r` | **REFUTED EXACTLY** |
| boundary contour estimate, RH, or GRH | **NOT PROVED** |

## 9. Bounded replay

```text
python -B research/l-families/atlas/function_field/ffps_bandpass_assembled_perron_leakage.py --check
python -B -O research/l-families/atlas/function_field/ffps_bandpass_assembled_perron_leakage.py --check
python -B -m unittest tests.test_ffps_bandpass_assembled_perron_leakage
python -B -O -m unittest tests.test_ffps_bandpass_assembled_perron_leakage
```

The replay checks the committed source blobs and local predecessor digests,
an exact bounded band-pass assembled reindex, `2r` signed moment vanishings,
the discrete absolute-lag identity, strict linear leakage for
`r=1,2,3,4`, and both Barnes residue signs and orientations. It uses only
rational arithmetic and bounded arrays. It enumerates no zeta zero, finite
field, curve, conductor family, or L-function.
