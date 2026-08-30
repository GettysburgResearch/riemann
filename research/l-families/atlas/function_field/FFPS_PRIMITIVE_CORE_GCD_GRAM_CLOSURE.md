# COREAGG is one signed shared-divisor Gram with a paid diagonal

Status: **exact shared-divisor Gram and gcd identities; unconditional
subpower diagonal; open off-diagonal criterion equivalent to `COREAGG` and
`PRIMCAR`, hence conditionally sufficient for RH; RH remains unproved**

Architecture: **Architecture A only**. No family/sheaf estimate is used.

Proof details:
[`FFPS_PRIMITIVE_CORE_GCD_GRAM_PROOF.md`](FFPS_PRIMITIVE_CORE_GCD_GRAM_PROOF.md).
Bounded replay:
[`ffps_primitive_core_gcd_gram_closure.py`](ffps_primitive_core_gcd_gram_closure.py).
Canonical fixture:
[`ffps_primitive_core_gcd_gram_closure.json`](ffps_primitive_core_gcd_gram_closure.json).

Frozen predecessor: PR #760 head
`aaccfe767c3d36a353056c9a2483e3824d89949f`, which proves
`COREAGG <=> PRIMCAR -> PRIMLS -> RH` conditionally.

## 0. Theorem

For `alpha in {0,1,2}`, the predecessor writes the full primitive burden as

\[
 \mathfrak C_\alpha(H)
 =\sum_{r\ge1,\ \mu(r)^2=1,\ 67\nmid r}{\tau(r)\over r^2}
  \sum_{I\in\mathscr D_H}|\mathcal Z_{I,r}^\alpha|^2,
\tag{0.1}
\]

where

\[
 \mathcal Z_{I,r}^\alpha
 =\sum_{\mu(M)^2=1,\ 67\nmid M,\ (M,r)=1}
 {\mu(M)\over\sqrt M}\mathcal W_I^\alpha(rM).
\tag{0.2}
\]

For squarefree `N,M` prime to `67`, define

\[
 \boxed{\mathscr K_2(N,M)
 =\sum_{r\mid(N,M)}{\tau(r)\over r}
 =\prod_{p\mid(N,M)}\left(1+{2\over p}\right).}
\tag{0.3}
\]

Then the exact shared-divisor Gram identity is

\[
 \boxed{\mathfrak C_\alpha(H)
 =\sum_{I\in\mathscr D_H}\sum_{N,M}
 {\mu(N)\mu(M)\over\sqrt{NM}}
 \mathcal W_I^\alpha(N)\overline{\mathcal W_I^\alpha(M)}
 \mathscr K_2(N,M).}
\tag{0.4}
\]

Its feature map is

\[
 N\mapsto\left(\sqrt{\tau(r)/r}\,\mathbf1_{r\mid N}\right)_r,
\tag{0.5}
\]

so the kernel is positive definite on finite Boolean product support. At one
prime its block is

\[
 \begin{pmatrix}1&1\\1&1+2/p\end{pmatrix},
 \qquad \det=2/p,
\tag{0.6}
\]

and the condition number is asymptotic to `2p`. Primewise whitening is not a
cost-free route.

Split (0.4) into product-shell diagonal and off-diagonal:

\[
 \mathfrak C_\alpha(H)=\mathfrak D_\alpha(H)+\mathfrak O_\alpha(H).
\tag{0.7}
\]

The diagonal is unconditionally paid:

\[
 \boxed{\mathfrak D_\alpha(H)
 \ll_{\mathcal R}L_H(1+\log(4H^2+2))^{12}=(2H)^{o(1)},}
\tag{0.8}
\]

where `L_H=ceil(log_2(N_H+1))` is the dyadic height depth.

Define

\[
 \mathrm{OFFGCDWAVE}:\qquad
 |\mathfrak O_\alpha(H)|\ll_\varepsilon(2H)^\varepsilon
 \quad(\alpha=0,1,2).
\tag{0.9}
\]

Then, at the all-positive-exponent scale,

\[
 \boxed{\mathrm{OFFGCDWAVE}
 \Longleftrightarrow\mathrm{COREAGG}
 \Longleftrightarrow\mathrm{PRIMCAR}
 \Longrightarrow\mathrm{PRIMLS}
 \Longrightarrow\mathrm{RH}.}
\tag{0.10}
\]

`OFFGCDWAVE` is open.

## 1. Exact gcd form

For `N!=M`, write `g=(N,M)`, `N=ga`, `M=gb`. Squarefreeness gives
`(a,b)=(ab,g)=1`. The Möbius signs on `g` cancel, so

\[
 \boxed{\begin{aligned}
 \mathfrak O_\alpha(H)
 =\sum_{\mu(g)^2=1,\ 67\nmid g}{\kappa_2(g)\over g}
 \sum_{\substack{\mu(a)^2=\mu(b)^2=1,\ (a,b)=(ab,g)=1\\(a,b)\ne(1,1)}}
 &{\mu(a)\mu(b)\over\sqrt{ab}}\\[-1mm]
 &\times\sum_{I\in\mathscr D_H}
 \mathcal W_I^\alpha(ga)
 \overline{\mathcal W_I^\alpha(gb)},
 \end{aligned}}
\tag{1.1}
\]

with

\[
 \kappa_2(g)=\prod_{p\mid g}(1+2/p).
\tag{1.2}
\]

The outer core has no Möbius sign. Cancellation must occur in the reduced
coprime pair and inside the signed divisor wavelets. Ratio-sixteen support
keeps `ga` and `gb` in the same factor-64 shell.

## 2. Why the diagonal is paid

For fixed squarefree `N`, group its orientations by integer physical height:

\[
 c_t^\alpha(N)=
 \sum_{a\mid N,\ h_\alpha(a,N/a)=t}
 \mathcal R\!\left(\log{67^\alpha a^2/N}\right).
\tag{2.1}
\]

A pair of heights belongs together in at most `L_H` aligned dyadic intervals,
therefore

\[
 \sum_{I\in\mathscr D_H}|\mathcal W_I^\alpha(N)|^2
 \le L_H\|\mathcal R\|_\infty^2\tau(N)^2.
\tag{2.2}
\]

Ratio-sixteen support gives `N<=4H^2/67^alpha`. For squarefree `N`,

\[
 \mathscr K_2(N,N)\tau(N)^2
 \le3^{\omega(N)}4^{\omega(N)}=d_{12}(N).
\tag{2.3}
\]

Finally,

\[
 \sum_{n\le X}{d_{12}(n)\over n}
 \le(1+\log X)^{12},
\tag{2.4}
\]

by the elementary twelve-fold divisor expansion. This proves (0.8) without a
prime number theorem, Chowla estimate, or RH.

The diagonal includes all orientation cross terms inside one product shell;
only correlations between distinct squarefree products remain open.

## 3. Analytic target

Equation (1.1) supports several attacks without strengthening the target:

1. Fourier-expand both balanced divisor wavelets, retaining the joint
   zero-frequency distinct-shell term.
2. Hyperbola/Vaughan-decompose the reduced coprime pair `(a,b)` and use
   bilinear Möbius estimates averaged in `g` with weight `kappa_2(g)/g`.
3. At `alpha=0`, reflect half-divisors before taking absolute values.
4. Use the feature map (0.5) forward; do not tensorize the badly conditioned
   local inverse.

A pointwise theorem in every `g` is stronger than necessary. The exact gate is
the assembled signed dyadic block sum (1.1).

## 4. Scope firewall

- `OFFGCDWAVE` is open.
- A positive local determinant does not bound the global Gram energy.
- The outer gcd variable has no Möbius sign.
- Fixed-shift Chowla or unsigned divisor estimates are not imported.
- Architecture B and all sheaf claims are outside this packet.

**No OFFGCDWAVE, COREAGG, PRIMCAR, PRIMLS, RH, or GRH estimate is proved.**

## 5. Proof ledger

| statement | grade |
|---|---|
| shared-divisor Gram (0.3)--(0.4) | **PROVED EXACT** |
| feature positivity and local spectrum | **PROVED EXACT** |
| unconditional diagonal (0.8) | **PROVED** |
| gcd form (1.1) | **PROVED EXACT** |
| OFFGCDWAVE equivalent to COREAGG | **PROVED AT ALL-EXPONENT SCALE** |
| COREAGG equivalent to PRIMCAR | **IMPORTED FROM FROZEN PREDECESSOR** |
| OFFGCDWAVE / RH / GRH | **NOT PROVED** |

No external novelty or priority claim is made.

## 6. Bounded replay

```text
python -B research/l-families/atlas/function_field/ffps_primitive_core_gcd_gram_closure.py --check
python -B -O research/l-families/atlas/function_field/ffps_primitive_core_gcd_gram_closure.py --check
python -B -m unittest tests.test_ffps_primitive_core_gcd_gram_closure
python -B -O -m unittest tests.test_ffps_primitive_core_gcd_gram_closure
```

The replay checks exact radical-valued Gram and gcd identities, the diagonal
split, a finite Boolean feature Gram, local determinants, and a finite dyadic
diagonal majorant. It enumerates no zeta zero, prime family, finite field,
curve, conductor family, or `L`-function.
