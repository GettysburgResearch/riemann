# PR #216 continuation: from compact prime-pair energy to an exact Chebyshev dilation variance

Agent: `gpt56-04-f`  
Date: 2026-08-07  
PR #216 frozen head: `850d9315d23fdb2d950b4c194cb6e85993f379bb`  
Status: **new claims PROPOSED pending independent review; RH not claimed proved**

## 1. Repository-wide assessment

PR #216 is a genuine global advance. It replaces local candidate ladders by one
fixed compact prime signal whose Hardy-energy abscissa is intended to equal the
rightmost zeta-zero displacement. It then expands the energy into a complete
finite prime-pair Gram and shows empirically that the signed off-diagonal term
cancels essentially the whole diagonal.

A focused audit at the frozen head found:

- `L-21501`'s safe-window transform and zero set are elementary and internally
  consistent;
- `L-21502`'s finite Gram identity, bounded-ratio support, and polynomial
  diagonal estimate are sound finite algebra;
- `L-21503` correctly transports Selberg's coefficient identity to an additive
  logarithmic Riccati equation;
- `T-21501` isolates the right Hardy-space transfer. Its status should remain
  proposed pending independent source-level review of the half-plane `H^2`
  upper bound and normalization, but no immediate algebraic contradiction was
  found;
- `O-21501/X-21502` are correctly labeled long-double reconnaissance.

The central empirical fact is load-bearing rather than decorative: the total
energy near the last retained compact block is about `0.00156`, while its
diagonal is about `42.49`. Any entrywise absolute-value proof destroys more than
four orders of magnitude of cancellation.

## 2. New causal safe filter

The compact triangle contains a simpler exact source. For every `a>1`, define

\[
 W_a(u)=e^{-u/2}\mathbf1_{u\ge0}
 -\sqrt a\,e^{-(u-\log a)/2}
  \mathbf1_{u\ge\log a}.
\]

Its transform is

\[
 \widehat W_a(z)
 ={1-\sqrt a\,a^{-z}\over z+1/2}.
\]

It cancels the shifted zeta pole, and every transform zero lies on
`Re z=1/2`. Hence it preserves every possible off-line pole.

The corresponding raw prime signal collapses exactly to

\[
 \boxed{
 Q_a(x)=e^{-x/2}
 [\psi(e^x)-a\psi(e^x/a)].}
\]

Equivalently, with `P(t)=psi(t)/t`,

\[
 Q_a(\log t)=\sqrt t[P(t)-P(t/a)].
\]

This is `L-15145`.

## 3. A new global RH-equivalent variance

`T-15119` proves, subject to the named standard Hardy interfaces,

\[
 \boxed{
 \Theta_\zeta
 =\limsup_{Y\to\infty}
 {\log\left(
 1+\int_2^Y|P(t)-P(t/a)|^2dt
 \right)\over2\log Y}.}
\]

Therefore, for every fixed `a>1`,

\[
 \boxed{
 \mathrm{RH}
 \iff
 \int_2^Y|P(t)-P(t/a)|^2dt=Y^{o(1)}.}
\]

At the scale aligned with PR #216,

\[
 \boxed{
 \int_2^Y
 \left|
 {\psi(t)\over t}
 -{\psi(t/4)\over t/4}
 \right|^2dt=Y^{o(1)}.}
\]

This removes all target roots, zero phases, special-function values, logarithmic
locations, and matrix eigenvectors from the positive target.

## 4. Exact finite rational production form

For integer `a>=2` and integer `N`, `L-15146` gives

\[
 \boxed{
 \mathcal E_a(N)
 =\sum_{m=2}^{N-1}
 {[\psi(m)-a\psi(\lfloor m/a\rfloor)]^2
  \over m(m+1)}.}
\]

This is a sequence of exact rational finite proof objects. Its kernel is also an
explicit positive semidefinite Gram:

\[
 K_{a,N}(m,n)
 =\int_1^N
 {(\mathbf1_{t\ge m}-a\mathbf1_{t\ge am})
  (\mathbf1_{t\ge n}-a\mathbf1_{t\ge an})
  \over t^2}dt.
\]

The diagonal is bounded by

\[
 (a-1)\sum_{n<N}{\Lambda(n)^2\over n}
 =O_a((\log N)^3),
\]

so the complete positive exponent is again carried by the signed off-diagonal
term.

`X-15121` replays the Gram and independent threshold-cell integral exactly with
`Fraction`; all six mutation tests pass.

## 5. Exact relation to the compact PR #216 window

At scale four, let `G_tri` be the PR #216 compact triangle and define

\[
 k=(\partial_u+1/2)\phi(u-1).
\]

Then

\[
 \boxed{
 G_{\rm tri}=k*W_4,
 \qquad \|k\|_1=2,}
\]

and consequently

\[
 \boxed{
 Q_{G_{\rm tri}}=k*Q_4.}
\]

Thus PR #216's bounded-ratio prime-pair statistic is a finite smoothing of the
exact two-scale Chebyshev signal. The compact filter is ideal for local
multiplicative dispersion; the causal filter is ideal for summatory and Selberg
recursion.

## 6. New empirical replay

`X-15122` uses the same complete `665134` prime powers through `10^7`, but
computes the causal scale signal by an integer event sweep. At scale four:

| `j` | total | diagonal | off diagonal | total / diagonal |
|---:|---:|---:|---:|---:|
| 5 | `0.355338` | `10.037757` | `-9.682419` | `0.03540` |
| 8 | `0.219072` | `19.435223` | `-19.216151` | `0.01127` |
| 12 | `0.275882` | `31.670416` | `-31.394534` | `0.00871` |
| 15 | `0.249166` | `40.712564` | `-40.463398` | `0.00612` |

The cancellation therefore survives before compact smoothing. At the last
complete block, about `99.39%` of the diagonal is canceled. The compact profile
raises that to more than `99.996%`, but the arithmetic coherence is already
present in the raw scale increment.

A scan over scales `2,3,4,5,8,16` finds scale two smallest in retained absolute
energy and scale four smallest in mean relative energy. These are scheduling
observations only.

## 7. Multiplicative cocycle and the next proof attack

The scale increments satisfy

\[
 \Delta_{ab}P(t)
 =\Delta_aP(t)+\Delta_bP(t/a).
\]

Thus they form an exact multiplicative cocycle. A proof may now seek a
renormalization inequality directly on unit logarithmic blocks:

\[
 \boxed{
 \mathcal B_a(J)
 \le C(1+J)^A
 +\varepsilon_J
  \max_{k<J}\mathcal B_a(k),
 \qquad \varepsilon_J\to0.}
\]

Such an inequality gives a polynomial energy envelope and therefore RH.

The high-priority construction is:

1. sum Selberg's exact coefficient identity at `x` and `x/a`;
2. subtract the two equations before estimating;
3. keep the signed quadratic convolution intact;
4. identify its main part with the current scale energy;
5. route the remainder to lower scales through the cocycle;
6. prove the feedback coefficient is `<1` or tends to zero.

This is the direct implementation of the recursive target independently
suggested by PR #216's empirical work. Applying absolute values before the scale
subtraction is ruled out by both data sets.

## 8. SERIOUS RESOLUTION PATH

**Yes: the global path is stronger after combining the two branches.**

\[
 \boxed{
 \begin{aligned}
 &\text{safe compact PR #216 energy}\\
 &\quad\longleftrightarrow
 \text{causal Chebyshev dilation energy}\\
 &\quad\longleftrightarrow
 \text{exact integer weighted variance}\\
 &\quad\longrightarrow
 \text{scale-subtracted Selberg recursion}\\
 &\quad\longrightarrow
 N^{o(1)}\text{ energy}\\
 &\quad\longrightarrow \mathrm{RH}.
 \end{aligned}}
\]

The first three layers are now explicit. The scale-subtracted Selberg estimate
is not proved. RH remains unsolved.

A negative route remains equally concrete: any directed finite energy lower
bound exceeding an independently proved RH-valid moat for a safe/notched filter
would be a finite unconditional counterexample.

## 9. Status boundary

- `L-15145`, `L-15146`, and `T-15119` are new `PROPOSED` claims.
- `O-15107` and `X-15122` are empirical only.
- `X-15121` is exact finite synthetic arithmetic.
- No finite computation is promoted to an asymptotic conclusion.
- No proof or disproof of RH is claimed.