# Full primitive panels are one-variable core-wavelet assemblies

Status: **exact full-panel product-shell identity, exact divisor-core transform
and inverse, and conditional core-wavelet criterion sufficient for `PRIMCAR`
and hence for RH; the core estimate and RH are not proved**

Architecture: **Architecture A only** — direct beta / primitive-pair route.
Nothing in this packet is a family/sheaf estimate.

Bounded exact replay:
[`ffps_primitive_core_wavelet_closure.py`](ffps_primitive_core_wavelet_closure.py).
Canonical summary:
[`ffps_primitive_core_wavelet_closure.json`](ffps_primitive_core_wavelet_closure.json).

Frozen source: PR #757 head
`b870366141fe8d5f43d5b81f6e50a67d2a888070`, specifically the primitive
large-sieve, harmonic-incidence Carleson, and rho-tilt/divisor-wavelet
packets pinned by the replay.

## 0. Outcome

The predecessor exposes a one-variable divisor wavelet while studying the
coherent-color energy and its harmonic zero mode.  The same grouping applies
to **the entire primitive panel, not only its harmonic zero mode**.

For the three independent channels put

\[
 A=67^\alpha,\qquad \alpha\in\{0,1,2\},
\]

and let `I` be one finite primitive-height block.  Define

\[
 h_\alpha(a,b)=\max(Aa,b)
\]

and retain the exact compact autocorrelation `\mathcal R` from the
ratio-sixteen boundary-field Gram.  For squarefree, 67-free `d`, write

\[
\begin{aligned}
 \mathcal P_I^\alpha(d)
 =\sum_{\substack{a,b\ \mathrm{squarefree},\ 67\nmid ab\\
                   (a,b)=1,\ (ab,d)=1\\
                   h_\alpha(a,b)\in I}}
 {\mu(a)\mu(b)\over\sqrt{ab}}
 \mathcal R\!\left(\log{Aa\over b}\right).
\end{aligned}
\tag{0.1}
\]

For squarefree, 67-free `N`, define the same near-square divisor wavelet

\[
 \boxed{
 \mathcal W_I^\alpha(N)
 =\sum_{a\mid N}
 \mathcal R\!\left(\log{Aa^2\over N}\right)
 \mathbf 1_{h_\alpha(a,N/a)\in I}.}
\tag{0.2}
\]

Then the full panel is exactly

\[
 \boxed{
 \mathcal P_I^\alpha(d)
 =\sum_{\substack{N\ \mathrm{squarefree},\ 67\nmid N\\(N,d)=1}}
 {\mu(N)\over\sqrt N}\mathcal W_I^\alpha(N).}
\tag{0.3}
\]

Now define, for every squarefree 67-free core `r`,

\[
 \boxed{
 \mathcal Z_{I,r}^\alpha
 =\sum_{\substack{M\ \mathrm{squarefree},\67\nmid M\\(M,r)=1}}
 {\mu(M)\over\sqrt M}\mathcal W_I^\alpha(rM).}
\tag{0.4}
\]

A second exact Boolean transform removes the sieve condition:

\[
 \boxed{
 \mathcal P_I^\alpha(d)
 =\sum_{r\mid d}{\mathcal Z_{I,r}^\alpha\over\sqrt r}.}
\tag{0.5}
\]

It is invertible:

\[
 \boxed{
 \mathcal Z_{I,r}^\alpha
 =\sqrt r\sum_{s\mid r}\mu(r/s)\mathcal P_I^\alpha(s).}
\tag{0.6}
\]

Thus all limiting Boolean modes and all finite-`D` sieve rows are assembled
from one family of one-variable Möbius divisor wavelets.  The earlier
zero-mode/nonzero-mode split remains useful for incidence Parseval, but it is
not forced at the level of the signed primitive panel.

This gives two clean sufficient gates.  Put

\[
 \boxed{
 \begin{aligned}
 \mathrm{COREAGG}:\quad
 &\sum_{\substack{r\ \mathrm{squarefree}\\67\nmid r}}
 {\tau(r)\over r^2}
 \sum_{I\in\mathscr D_H}|\mathcal Z_{I,r}^\alpha|^2
 \ll_\varepsilon(2H)^\varepsilon,\\[2mm]
 \mathrm{COREWAVE}:\quad
 &\sum_{I\in\mathscr D_H}|\mathcal Z_{I,r}^\alpha|^2
 \ll_\eta(2Hr)^\eta
 \quad\text{uniformly in }r.
 \end{aligned}}
\tag{0.7}
\]

Both assertions range over all positive exponents and all three actual
channels.  Then

\[
 \boxed{
 \mathrm{COREWAVE}\Longrightarrow\mathrm{COREAGG}
 \Longleftrightarrow\mathrm{PRIMCAR}
 \Longrightarrow\mathrm{PRIMLS}
 \Longrightarrow\mathrm{RH}.}
\tag{0.8}
\]

The last two arrows are imported from the frozen predecessor chain.  The
COREWAVE implication and the COREAGG--PRIMCAR equivalence are proved below.
COREWAVE is open.  The COREAGG estimate is open exactly as PRIMCAR is open;
their all-exponent equivalence is an exact theorem.  COREWAVE is deliberately
a strictly stronger sufficient theorem than the assembled target: it asks for
square-function cancellation on every core before the summable `r`-assembly.
In particular, **COREAGG and PRIMCAR are equivalent** at the repository
`Y^{o(1)}` / all-`epsilon` scale.

## 1. Full product-shell collapse

In (0.1), put `N=ab`.  Because `a` and `b` are squarefree and coprime, `N`
is squarefree.  Conversely, if `N` is squarefree, every factorization
`N=a(N/a)` has squarefree coprime factors.  Moreover,

\[
 \mu(a)\mu(N/a)=\mu(N)
\tag{1.1}
\]

for every divisor `a|N`.  The sieve condition is simply `(N,d)=1`, the
normalization is `N^{-1/2}`, and the remaining oriented factorization sum is
exactly (0.2).  Grouping the finite height-supported sum by `N` proves (0.3).

No averaging, asymptotic formula, positivity step, or replacement of the
moving height block is used.  At `alpha=0`, swapped orientations contribute
equally because `\mathcal R` is even; at positive `alpha`, both oriented
terms remain in the wavelet with their actual unequal physical scales.

## 2. Exact sieve-to-core transform

For squarefree `d`, Boolean Möbius inversion gives

\[
 \mathbf 1_{(N,d)=1}=\sum_{r\mid(N,d)}\mu(r).
\tag{2.1}
\]

Insert (2.1) into (0.3), interchange finite sums, and write `N=rM`.  Since
`N` is squarefree, `(r,M)=1`, and

\[
 \mu(r)\mu(N)=\mu(r)^2\mu(M)=\mu(M).
\tag{2.2}
\]

The square-root normalization factors as `(rM)^{-1/2}`.  The result is
exactly (0.5).

Equation (0.5) is the ordinary divisor zeta transform of
`r^{-1/2}\mathcal Z_{I,r}^\alpha`.  Applying divisor Möbius inversion and
multiplying by `\sqrt r` proves (0.6).

Two consequences are worth making explicit.

1. The auxiliary sieve label no longer requires a separate analysis of every
   biased-Boolean frequency.  Those modes are different linear coordinates
   of the same core family.
2. The inversion is exact but not norm-free.  Recovering one remote core from
   the assembled panel can lose powers of `r`; therefore (0.6) does not turn
   `PRIMCAR` into COREWAVE at the stated subpower normalization.

## 3. COREAGG implies PRIMCAR

For one squarefree `d`, Cauchy--Schwarz in its divisor set and (0.5) give

\[
 \sum_{I\in\mathscr D_H}|\mathcal P_I^\alpha(d)|^2
 \le
 \tau(d)\sum_{r\mid d}{1\over r}
 \sum_{I\in\mathscr D_H}|\mathcal Z_{I,r}^\alpha|^2.
\tag{3.1}
\]

Multiply by `d^{-1}`, sum over squarefree 67-free `d<=D`, and write `d=rk`.
Squarefreeness makes `(r,k)=1` and
`\tau(rk)=\tau(r)\tau(k)`.  Hence

\[
\begin{aligned}
 &\sum_{\substack{d\le D\ \mathrm{squarefree}\\67\nmid d}}
 {1\over d}
 \sum_{I\in\mathscr D_H}|\mathcal P_I^\alpha(d)|^2\\
 &\quad\le
 \sum_{\substack{r\ \mathrm{squarefree}\\67\nmid r}}
 {\tau(r)\over r^2}
 \sum_{I\in\mathscr D_H}|\mathcal Z_{I,r}^\alpha|^2
 \sum_{\substack{k\le D/r\ \mathrm{squarefree}\\
                  67\nmid k,\ (k,r)=1}}{\tau(k)\over k}\\
 &\quad\le
 \left(\sum_{k\le D}{\tau(k)\over k}\right)
 \sum_{\substack{r\ \mathrm{squarefree}\\67\nmid r}}
 {\tau(r)\over r^2}
 \sum_{I\in\mathscr D_H}|\mathcal Z_{I,r}^\alpha|^2.
\end{aligned}
\tag{3.2}
\]

The elementary divisor expansion gives

\[
 \sum_{k\le D}{\tau(k)\over k}
 =\sum_{ab\le D}{1\over ab}
 \le(1+\log D)^2.
\tag{3.3}
\]

COREAGG and exponent renaming therefore prove

\[
 \sum_{I\in\mathscr D_H}\mathcal E_D(I)
 \ll_\varepsilon(2DH)^\varepsilon,
\tag{3.4}
\]

which is exactly the predecessor's `PRIMCAR` gate.

The placement of `\tau(r)/r^2` in COREAGG is not cosmetic.  One factor
`r^{-1}` comes from the half-weight in (0.5), and the second comes from the
harmonic `d^{-1}` norm after `d=rk`.

## 4. COREWAVE implies COREAGG

Assume COREWAVE with some `0<eta<1`.  Then

\[
\begin{aligned}
 &\sum_{\substack{r\ \mathrm{squarefree}\\67\nmid r}}
 {\tau(r)\over r^2}
 \sum_I|\mathcal Z_{I,r}^\alpha|^2\\
 &\qquad\ll_\eta
 (2H)^\eta
 \sum_{\substack{r\ \mathrm{squarefree}\\67\nmid r}}
 {\tau(r)\over r^{2-\eta}}.
\end{aligned}
\tag{4.1}
\]

The remaining series has Euler product

\[
 \prod_{p\ne67}\left(1+{2\over p^{2-\eta}}\right),
\tag{4.2}
\]

which converges exactly in the needed range `eta<1`.  Choosing a smaller
COREWAVE exponent and renaming it proves COREAGG for every requested positive
exponent.  Combining Sections 3 and 4 proves (0.8).

This summable `r^{-2+o(1)}` assembly is the main gain over a direct
triangle inequality in the sieve variable.


## 4A. PRIMCAR implies COREAGG

The reverse direction uses the finite product-shell support and the exact
inverse (0.6).  Every block `I` lies in `(H,2H]`; the ratio-sixteen support
gives

\[
 \mathcal Z_{I,r}^\alpha=0
 \qquad\text{for }r>R_\alpha(H):=\left\lfloor{4H^2\over A}\right\rfloor.
\tag{4A.1}
\]

Put

\[
 A_r=\sum_I|\mathcal Z_{I,r}^\alpha|^2,
 \qquad B_s=\sum_I|\mathcal P_I^\alpha(s)|^2.
\]

Cauchy--Schwarz in (0.6) gives

\[
 A_r\le r\tau(r)\sum_{s\mid r}B_s.
\tag{4A.2}
\]

Therefore, with `R=R_alpha(H)`,

\[
\begin{aligned}
 \sum_{r\le R}{\tau(r)\over r^2}A_r
 &\le\sum_{r\le R}{\tau(r)^2\over r}\sum_{s\mid r}B_s\\
 &=\sum_{s\le R}{\tau(s)^2B_s\over s}
   \sum_{\substack{k\le R/s\ \mathrm{squarefree}\\(k,s)=1}}
   {\tau(k)^2\over k}.
\end{aligned}
\tag{4A.3}
\]

For squarefree `k`, `tau(k)^2=4^{omega(k)}=d_4(k)`.  Hence

\[
 \sum_{\substack{k\le X\ \mathrm{squarefree}}}{\tau(k)^2\over k}
 \le\sum_{k\le X}{d_4(k)\over k}
 =\sum_{n_1n_2n_3n_4\le X}{1\over n_1n_2n_3n_4}
 \le(1+\log X)^4.
\tag{4A.4}
\]

Also, for every `delta>0`, the elementary divisor bound gives
`tau(s)^2 <<_delta s^delta`.  Thus

\[
 \sum_r{\tau(r)\over r^2}A_r
 \ll_\delta R^\delta(1+\log R)^4
 \sum_{s\le R}{B_s\over s}.
\tag{4A.5}
\]

Apply PRIMCAR with `D=R`.  Since `R<=4H^2`, choose the PRIMCAR and divisor
exponents smaller than the requested final exponent and absorb the logarithm.
This proves COREAGG.  Together with Section 3,

\[
 \boxed{\mathrm{COREAGG}\Longleftrightarrow\mathrm{PRIMCAR}}
\tag{4A.6}
\]

at the all-positive-exponent scale.  The exact divisor transform therefore
has a subpower condition number on the actual finite factor-64 support.

## 5. Fourier--hyperbola normal form

The reduction also identifies the natural analytic attack.  Let
`\mathcal R` be the autocorrelation of the compact boundary kernel
`K_{\rm bd}` and use

\[
 \widehat f(\xi)=\int_{\mathbf R}f(u)e^{-i\xi u}\,du.
\]

Then

\[
 \mathcal R(u)={1\over2\pi}\int_{\mathbf R}
 |\widehat K_{\rm bd}(\xi)|^2e^{i\xi u}\,d\xi.
\tag{5.1}
\]

For the prefix wavelet with `h_\alpha<=T`, the two inequalities
`Aa<=T` and `N/a<=T` are exactly

\[
 {N\over T}\le a\le {T\over A}.
\tag{5.2}
\]

Consequently

\[
\boxed{
 \begin{aligned}
 \mathcal W_{\le T}^\alpha(N)
 ={1\over2\pi}\int_{\mathbf R}
 &|\widehat K_{\rm bd}(\xi)|^2 A^{i\xi}N^{-i\xi}\\
 &\times
 \sum_{\substack{a\mid N\\N/T\le a\le T/A}}
 a^{2i\xi}\,d\xi.
 \end{aligned}}
\tag{5.3}
\]

A block wavelet is the difference of two such prefixes.  If the height cutoff
is temporarily removed and `N` is squarefree, the divisor polynomial factors
prime by prime:

\[
 A^{i\xi}N^{-i\xi}\sum_{a\mid N}a^{2i\xi}
 =A^{i\xi}\prod_{p\mid N}2\cos(\xi\log p).
\tag{5.4}
\]

Thus the only nonmultiplicative feature is the balanced hyperbola cutoff,
not the ratio kernel itself.

There is an equally useful geometric coordinate.  Put

\[
 z=\log{Aa^2\over N}.
\]

Since `(Aa)(N/a)=AN`, one has the exact identity

\[
 \boxed{
 h_\alpha(a,N/a)=\sqrt{AN}\,e^{|z|/2}.}
\tag{5.5}
\]

The ratio-sixteen support is `|z|<=log 16`.  If the height lies in `(H,2H]`,
then

\[
 {H^2\over16A}<N\le {4H^2\over A}.
\tag{5.6}
\]

COREWAVE is therefore a square-function theorem for Möbius on one
factor-64 multiplicative shell, tested against a Fourier superposition of
balanced truncated divisor polynomials.

A plausible proof programme is now literal rather than schematic:

```text
smooth the two hyperbola endpoints
  -> use (5.3) and Mellin/Fourier separation
  -> isolate the xi=0 divisor component
  -> apply a Vaughan or hyperbola decomposition to mu(M)
  -> prove a joint frequency/core square mean
  -> exploit the r^(-2+o(1)) outer assembly
  -> unsmooth without losing dyadic Carleson summability.
```

No step after the first exact transformations is supplied here.

## 6. Scope firewall

This packet does not claim that the Möbius difficulty has become easier than
RH.  It changes its coordinates and removes one artificial split.

In particular:

- COREWAVE is open;
- the COREAGG estimate is open, equivalently PRIMCAR is open;
- the Fourier formula does not bound its zero frequency;
- no pointwise Chowla estimate, averaged Chowla estimate, large-sieve theorem,
  or short multiplicative-interval estimate is imported;
- no estimate for `PRIMCAR` or `PRIMLS` is proved;
- no converse from RH or `PRIMCAR` to COREWAVE is claimed;
- the family/sheaf architecture is outside this packet.

**No PRIMCAR, PRIMLS, RH, or GRH estimate is proved.**

## 7. Proof ledger

| statement | grade |
|---|---|
| full primitive product-shell identity (0.3) | **PROVED EXACT** |
| core-wavelet transform and inverse (0.5)--(0.6) | **PROVED EXACT** |
| COREAGG implies PRIMCAR | **PROVED CONDITIONALLY** |
| PRIMCAR implies COREAGG at all-exponent scale | **PROVED CONDITIONALLY** |
| COREWAVE implies COREAGG | **PROVED CONDITIONALLY** |
| Fourier--hyperbola form (5.3)--(5.5) | **PROVED EXACT UNDER THE STATED FOURIER CONVENTION** |
| factor-64 support (5.6) | **PROVED EXACT** |
| PRIMCAR implies PRIMLS implies RH | **IMPORTED CONDITIONAL CHAIN FROM THE FROZEN SOURCE** |
| COREWAVE or COREAGG estimate | **OPEN / NOT PROVED** |
| RH or GRH | **NOT PROVED** |

No external novelty or priority claim is made.

## 8. Bounded replay

```text
python -B research/l-families/atlas/function_field/ffps_primitive_core_wavelet_closure.py --check
python -B -O research/l-families/atlas/function_field/ffps_primitive_core_wavelet_closure.py --check
python -B -m unittest tests.test_ffps_primitive_core_wavelet_closure
python -B -O -m unittest tests.test_ffps_primitive_core_wavelet_closure
```

The replay uses an exact compact ratio-sixteen rational toy kernel.  It checks
(0.3), (0.5), and (0.6) in all three actual `67^alpha` channels, verifies the
balanced height and factor-64 support identities, and authenticates the
finite `eta=0` divisor-cost reindexing behind (3.2).  It enumerates no zeta
zero, prime family, finite field, curve, conductor family, or `L`-function.
