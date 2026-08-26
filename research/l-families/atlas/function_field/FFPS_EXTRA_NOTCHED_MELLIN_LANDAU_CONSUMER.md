# A direct Mellin--Landau consumer for the extra-notched current

Status: **exact conditional analytic consumer; arithmetic source adapter and
negative-mass estimate open; RH unproved**

Bounded exact replay:
[`ffps_extra_notched_mellin_landau_consumer.py`](ffps_extra_notched_mellin_landau_consumer.py).

Frozen interfaces: PR #751 `L-102500`, `L-102504`, `L-102701`,
`L-106134`, and `T-106150`.  Read first:
`FFPS_COMMON_MOTHER_OUTER_NOTCH_MISMATCH.md`.

## 0. Outcome

The missing dyadic notch in the native-outer adapter need not be inverted.
The extra-notched self-convolution current is itself a fixed zero-safe
Mellin--Landau detector.

Let

\[
\widehat A(s)
={q(s)r(s)\over s(s-1/2)},
\qquad
q(s)=1-\sqrt2\,2^{-s},
\qquad
r(s)=1-2^{-s},
\tag{0.1}
\]

and

\[
\mathcal D_{\rm out}
={1\over2}D(D-1)(5D+3/2)(2D-1).
\tag{0.2}
\]

The compact signed logarithmic measure

\[
K_{\rm ext}=\mathcal D_{\rm out}(A*_M A)
\tag{0.3}
\]

has multiplier

\[
\boxed{
M_{\rm ext}(s)
={q(s)^2r(s)^2(s-1)(5s+3/2)\over s(s-1/2)}.}
\tag{0.4}
\]

It has no zero or pole in

\[
0<\Re s<1/2.
\]

For the duplicate-`67` source

\[
\beta(n)=\mu(n)-1_{67\mid n}\mu(n/67),
\]

let `tau_n` denote multiplicative translation by `n` and put

\[
\nu_{\rm ext}
=\sum_n{\beta(n)\over\sqrt n}\,\tau_nK_{\rm ext}.
\tag{0.5}
\]

This is a locally finite signed Radon measure on the multiplicative half-line,
not an ordinary function.  The same specialized negative-mass Landau theorem
used by `L-102504`, after the fixed positive mollification described below,
gives

\[
\boxed{
\nu_{\rm ext}^-([1,Y])=Y^{o(1)}
\quad\Longrightarrow\quad \mathrm{RH}.}
\tag{0.6}
\]

Here `Y^{o(1)}` means `O_epsilon(Y^epsilon)` for every `epsilon>0`, and
`nu_ext^-` is the negative measure in the Jordan decomposition.  Thus the
dyadic atoms are included.

This produces a precise repair target for `T-106150`:

```text
EXTSRC106150:
  the complete beta-source extra-notched current equals
  D_out J_U^diamond plus an absolute-subpower closed field.

EXTSRC106150 AND WKSFSC106150 -> RH.
```

`EXTSRC106150` is an exact source-adapter gate.  It is not supplied by the
incorrect unnotched naming in `L-102740/L-106134`, and it is not claimed here.

## 1. Exact Mellin audit

First, (0.3) really is a finite measure.  In logarithmic coordinate
`t=log X`, with `L=log 2`, the positive ratio-four kernel is

\[
a(t)=
\begin{cases}
2(e^{t/2}-1),&0<t<L,\\
\sqrt2(2-e^{t/2}),&L<t<2L,\\
0,&\text{otherwise}.
\end{cases}
\tag{1.1}
\]

It is continuous and piecewise smooth, so `a''` is a compact finite signed
measure.  Consequently

\[
D^4(a*a)=a''*a''
\]

is a compact finite signed measure; all lower derivatives in the polynomial
`D_out` are finite measures as well.  Differentiation does not enlarge
support, hence

\[
\boxed{K_{\rm ext}\text{ is a finite signed measure supported in }[1,16].}
\tag{1.2}
\]

This also justifies every distributional differentiation below.

Squaring (0.1) and multiplying by the polynomial (0.2) gives

\[
\begin{aligned}
M_{\rm ext}(s)
&={1\over2}s(s-1)(5s+3/2)(2s-1)
 {q(s)^2r(s)^2\over s^2(s-1/2)^2}\\
&={q(s)^2r(s)^2(s-1)(5s+3/2)\over s(s-1/2)},
\end{aligned}
\]

proving (0.4).  This is a Mellin--Stieltjes transform: in log coordinate it
is `int exp(-st) dK_ext(t)`.

The zeros are completely explicit:

- `r(s)=0` only on `Re(s)=0`;
- `q(s)=0` only on `Re(s)=1/2`;
- `s-1=0` at `s=1`;
- `5s+3/2=0` at `s=-3/10`.

The apparent singularities at `s=0` and `s=1/2` are removable because
`r(s)^2` and `q(s)^2`, respectively, vanish to second order.  Hence (0.4) is
holomorphic and nonzero throughout the open strip.

Since `K_ext` is finite and compactly supported and `|beta(n)|<=2`, absolute
Mellin--Stieltjes Fubini holds for `Re(s)>1/2` and gives

\[
\boxed{
\mathcal M \nu_{\rm ext}(s)
=M_{\rm ext}(s)
 {1-67^{-(s+1/2)}\over\zeta(s+1/2)}.}
\tag{1.3}
\]

The source factor is exact because, for `Re(z)>1`,

\[
\sum_{n\ge1}{\beta(n)\over n^z}
=(1-67^{-z})\sum_{n\ge1}{\mu(n)\over n^z}
={1-67^{-z}\over\zeta(z)}.
\tag{1.4}
\]

If `rho` is a zeta zero with `Re(rho)>1/2`, then
`s_rho=rho-1/2` lies in the open strip.  The kernel multiplier is nonzero
there and `1-67^(-rho)` cannot vanish because `|67^(-rho)|<1`.  Thus (1.3)
has a genuine pole at `s_rho`, of the same order as the zero.

On the positive real axis, `zeta(s+1/2)` has no zero.  Indeed, the Euler
product is positive for `s+1/2>1`; for `1/2<s+1/2<1`, the paired alternating
eta series is positive while `1-2^(1-(s+1/2))` is negative, so zeta is
negative.  At `s=1/2`, its pole makes `1/zeta(s+1/2)` vanish, while the
apparent singularity of (0.4) is already removable.  Thus (1.3) is
holomorphic at every positive real point.

## 2. Why the measure causes no loophole

`K_ext` contains dyadic atoms, whereas `L-102504` is written with a function
kernel.  This is removed without weakening the one-sided premise.

In log coordinate, let

\[
\eta_\varepsilon(t)=\varepsilon^{-1}\mathbf1_{[0,\varepsilon]}(t)
\]

and let `h_epsilon=eta_epsilon*nu_ext`, using the convention in which an atom
at `u` is spread over `[u,u+epsilon]`.  Then `h_epsilon` is an ordinary
locally integrable density with respect to `dt=dX/X`.  Its Laplace/Mellin
multiplier is

\[
\widehat\eta_\varepsilon(s)
={1-e^{-\varepsilon s}\over\varepsilon s}.
\tag{2.1}
\]

Every nonremovable zero of (2.1) lies on `Re(s)=0`, so it does not cancel an
open-strip pole.  Positivity and the one-sided support give the stronger
finite-horizon contraction

\[
\boxed{
\int_0^T(h_\varepsilon(t))_-\,dt
\le \nu_{\rm ext}^-([0,T])
\qquad(T\ge0).}
\tag{2.2}
\]

Indeed, `h_epsilon^- <= eta_epsilon*nu_ext^-` pointwise, and integration over
`[0,T]` loses no mass from a future input point because the box is supported
in `[0,epsilon]`.  The corresponding global contraction follows whenever
the global negative variation is finite.

No limiting passage in `epsilon` is required: any one fixed positive
`epsilon` works.

## 3. Self-contained measure-to-Landau lemma

For completeness, here is the exact analytic step rather than an appeal to a
function-kernel slogan.

**Lemma (one-sided mollified negative-mass Landau).**  Let `nu` be a locally
finite signed measure supported on `[0,infinity)` in log coordinate.  Suppose

\[
|\nu|([0,T])=O(e^{\sigma_0T})
\quad\text{for some finite }\sigma_0,
\qquad
\nu^-([0,T])=O_\delta(e^{\delta T})
\quad(\delta>0).
\tag{3.1}
\]

If the Mellin--Stieltjes transform of `nu` has a meromorphic continuation
which is holomorphic at every positive real point, then it has no pole in
`Re(s)>0`.

**Proof.**  Fix one `epsilon>0` and put `h=eta_epsilon*nu`.  Equation (2.2)
implies that

\[
N(s)=\int_0^\infty h_-(t)e^{-st}\,dt
\]

converges absolutely and locally uniformly in `Re(s)>0`.  Thus `N` is
holomorphic there.  The first bound in (3.1) gives the nonnegative density
`h_+` a finite Laplace abscissa `sigma_c<=sigma_0`.  Initially,

\[
P(s):=\int_0^\infty h_+(t)e^{-st}\,dt
=\widehat\eta_\varepsilon(s)\mathcal M\nu(s)+N(s).
\tag{3.2}
\]

If `h_+` vanishes identically, (3.2) already makes the mollified transform
holomorphic in `Re(s)>0`.  Otherwise, Landau's theorem for a nonzero
nonnegative density says that a finite abscissa `sigma_c` is a singularity.
But the right side of (3.2) is holomorphic at every positive real point.
Therefore `sigma_c<=0`, so `P`, and hence the mollified transform, is
holomorphic throughout `Re(s)>0`.  Finally, (2.1) is nonzero there; division
by it proves the assertion for `M nu`.  QED.

For `nu=nu_ext`, the required finite exponential bound is elementary:

\[
|\nu_{\rm ext}|([1,Y])
\le \|K_{\rm ext}\|_{\rm TV}
\sum_{n\le Y}{|\beta(n)|\over\sqrt n}
=O(\sqrt Y).
\tag{3.3}
\]

Thus `sigma_0=1/2` is available without any arithmetic cancellation.  The
premise in (0.6), (2.2), the lemma, and the genuine pole in (1.3) exclude
every zeta zero with real part greater than `1/2`.  The zeta functional
equation excludes zeros to the left of the line as well.  This proves (0.6),
including the measure/function and finite-abscissa hypotheses.

## 4. What the repair does and does not solve

The corrected architecture is

```text
complete beta source
  -> extra-notched locally finite signed measure nu_ext
  -> zero-safe Mellin pole detector
  -> negative-mass Landau consumer.
```

This bypasses the power-lossy causal inverse of
`Q=I-sqrt(2)S_2`.  It also shows that the notch mismatch is not, by itself, a
reason to abandon the half-source programme.

What remains is arithmetic and exact:

1. start from the complete `beta` source, not only the live balanced sector;
2. repeat the source decomposition with `K_ext` typed throughout;
3. prove every inherited closed sector remains absolute-subpower;
4. identify the surviving live term with `D_out J_U^diamond`;
5. prove its Jordan negative variation is subpower.

Steps 1--4 are exactly `EXTSRC106150`.  Step 5 is `WKSFSC106150` under the
signed-measure convention.

The fixed extra notch preserves absolute-subpower closed fields once their
native absolute bounds are available, because a finite shift combination is
bounded on logarithmic `L^1`.  But the repository's frozen source chain must
still state that operation at the correct stage; this packet does not infer
it from a misnamed equation.

## 5. Relation to the coherent atomic shell

The exact negative dyadic atoms in
`FFPS_SIGNED_DIFFERENTIAL_ATOMIC_SHELL_FIREWALL.md` belong precisely to
`K_ext`.  They show that `WKSFSC106150` cannot follow from a deletion-stable,
source-blind diagonal argument.  They do not affect the analytic implication
(0.6): the Jordan convention and mollification include them exactly.

The combined lesson is sharper than either packet alone:

```text
the extra-notched detector is analytically sufficient;
its arithmetic negative-mass estimate needs global source-sector
cancellation and cannot be proved by local diagonal interpolation.
```

## 6. Proof ledger

Proved exactly:

- the simplified multiplier (0.4);
- compact finite-measure support of `K_ext`;
- absolute Fubini and the exact duplicate-`67` source factor;
- all zero locations and open-strip nonvanishing;
- persistence of every hypothetical off-line-zero pole;
- finite-horizon positive-mollifier contraction of Jordan negative variation;
- noncancellation of open-strip poles by the log-box multiplier;
- the self-contained finite-abscissa Landau lemma and conditional implication
  (0.6).

New exact gate:

- `EXTSRC106150`, the complete-source adapter to the extra-notched current.

Not proved:

- `EXTSRC106150`;
- `WKSFSC106150` or any complete-source negative-mass estimate;
- `BCI102990`, RH, or GRH.

## 7. Bounded replay

```text
python -B research/l-families/atlas/function_field/ffps_extra_notched_mellin_landau_consumer.py --check
python -B -O research/l-families/atlas/function_field/ffps_extra_notched_mellin_landau_consumer.py --check
python -B -m unittest tests.test_ffps_extra_notched_mellin_landau_consumer
python -B -O -m unittest tests.test_ffps_extra_notched_mellin_landau_consumer
```

The replay checks exact zero locations, four exact Mellin samples, and four
open-strip mollifier panels.  It enumerates no source atom, conductor, curve,
or point.
