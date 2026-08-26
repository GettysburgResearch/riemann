# The fixed-mollified beta detector is an exact boundary difference

Status: **exact primitive-detector, dyadic-compression, boundary-shell, and
RH-equivalence theorem; no bound for either detector and no proof of RH or
GRH**

Bounded exact replay:
[`ffps_mollified_beta_boundary_shell_identity.py`](ffps_mollified_beta_boundary_shell_identity.py).
Canonical summary:
[`ffps_mollified_beta_boundary_shell_identity.json`](ffps_mollified_beta_boundary_shell_identity.json).

Source boundary:

1. the repaired fixed-mollified equivalence and native reflection packets at
   `a678292fd6d19d5b18f499aef35d2263cfc2b4ec`;
2. the finite scout at
   `1a4e7f73addaeec3d13e83b7a8a967b42a47ce1b`;
3. the exact inverse kernel calculation at
   `9f29bdb6ea7375df84de550d62f9d0984634a8dd`.

The replay pins every Markdown, producer, JSON, and test blob used from those
packets.  No uncommitted source is imported.

## 0. Outcome

Let `L=log 2`, let `K_ext` be the compact signed logarithmic measure of the
extra-notched detector, and use the translation convention

\[
 (\tau_a f)(t)=f(t-a).
\tag{0.1}
\]

The factor `D` in `K_ext` implies that its total mass is zero.  Its causal
primitive

\[
 K_{\rm bd}(t)=K_{\rm ext}(( -\infty,t])
\tag{0.2}
\]

is therefore an ordinary compact BV function supported in `[0,4L]`, with

\[
 DK_{\rm bd}=K_{\rm ext},
 \qquad
 \widehat K_{\rm bd}(s)={M_{\rm ext}(s)\over s}.
\tag{0.3}
\]

Define the **boundary field**

\[
 \boxed{
 G(t)=\sum_{n\ge1}{\beta(n)\over\sqrt n}
             K_{\rm bd}(t-\log n).}
\tag{0.4}
\]

It is a causal, locally integrable function.  For every fixed
`epsilon>0`, not only for the scout width, the complete mollified detector is
the exact first difference

\[
 \boxed{
 h_\varepsilon(t)
 ={G(t)-G(t-\varepsilon)\over\varepsilon}.}
\tag{0.5}
\]

Consequently its signed mass telescopes to one terminal shell:

\[
 \boxed{
 \int_0^T h_\varepsilon(t)\,dt
 ={1\over\varepsilon}\int_{T-\varepsilon}^{T}G(u)\,du,}
\tag{0.6}
\]

where `G(u)=0` for `u<0`.  At the finite scout's
`epsilon=L/2`, this is literally a half-dyadic boundary-shell identity.

The primitive is itself an exact RH detector:

\[
 \boxed{
 \mathrm{RH}
 \Longleftrightarrow
 \int_0^T|G(t)|\,dt=e^{o(T)}
 \Longleftrightarrow
 \int_0^T(G(t))_-\,dt=e^{o(T)}.}
\tag{0.7}
\]

Thus one integration removes both the box parameter and the atomic measure
without losing zero detection.  Equation (0.7) is a calibration theorem, not
an estimate: neither displayed subpower bound is proved here.

There is also an exact dyadic compression.  Put

\[
 w(t)=1_{t\ge0}(13+3t-8e^{t/2})
\tag{0.8}
\]

and

\[
 P(z)=(1-z)^2(1-\sqrt2z)^2(1-z/\sqrt2),
 \qquad \psi=P(\tau_L)w.
\tag{0.9}
\]

Then `psi` is supported in `[0,5L]` and

\[
 \boxed{
 G(t)=\sum_{\substack{m\ge1\\m\ \mathrm{odd}}}
       {\beta(m)\over\sqrt m}\psi(t-\log m).}
\tag{0.10}
\]

This is the full telescope supplied by the displayed kernel factors and the
exact 2-adic source pairing.  Its leading coefficient is `P(0)=1`, so those
finite shifts do not annihilate an independent odd source fibre.  Cancellation
needed for (0.7) must still occur between distinct odd indices, or through
arithmetic equivalent in strength to that cancellation.

## 1. The causal primitive

The exact inverse calculation used by the finite scout writes

\[
 K_{\rm ext}
 =(1-\tau_L)^2(1-\sqrt2\tau_L)^2 R_0,
\tag{1.1}
\]

where

\[
 R_0=5\delta_0+(3-4e^{t/2})1_{t\ge0}\,dt.
\tag{1.2}
\]

The function in (0.8) has a jump from `0` to `5` at the origin and ordinary
derivative `3-4e^(t/2)` on the positive half-line.  Hence, distributionally,

\[
 Dw=R_0.
\tag{1.3}
\]

It follows that

\[
 K_{\rm bd}
 =(1-\tau_L)^2(1-\sqrt2\tau_L)^2w.
\tag{1.4}
\]

For `t>4L`, all translated copies in (1.4) lie on the smooth tail of `w`.
The factor `(1-tau_L)^2` annihilates its affine part, and
`(1-sqrt(2)tau_L)^2` annihilates `e^(t/2)` because

\[
 \tau_L e^{t/2}=2^{-1/2}e^{t/2}.
\tag{1.5}
\]

This proves compact support directly.  It also agrees with the intrinsic
construction (0.2): a compact measure of total mass zero has a compact
causal cumulative.  Endpoint conventions change only point values and never
the identities of locally integrable densities below.

For the causal box

\[
 \eta_\varepsilon=\varepsilon^{-1}1_{[0,\varepsilon]},
\]

the fundamental theorem for distributions gives

\[
 \eta_\varepsilon*DK_{\rm bd}
 ={1\over\varepsilon}(1-\tau_\varepsilon)K_{\rm bd}.
\tag{1.6}
\]

Convolving (1.6) with the locally finite complete beta source proves (0.5).
No limit `epsilon->0`, numerical quadrature, or source truncation is used.

## 2. Exact odd-fibre compression

For every odd positive integer `m`, including those divisible by `67`,

\[
 \beta(2m)=-\beta(m),\qquad \beta(4m)=0.
\tag{2.1}
\]

Indeed `mu(2m)=-mu(m)` for odd `m`, with both sides zero when `m` is not
squarefree; the same identity applies to `m/67` when that term is present.
Both Mobius terms vanish after multiplication by `4`.  Therefore the
normalized source has the exact formal decomposition

\[
 \sum_{n\ge1}{\beta(n)\over\sqrt n}\delta_{\log n}
 =\left(1-{1\over\sqrt2}\tau_L\right)
   \sum_{\substack{m\ge1\\m\ \mathrm{odd}}}
       {\beta(m)\over\sqrt m}\delta_{\log m}.
\tag{2.2}
\]

Moving this last finite difference onto (1.4) proves (0.9)--(0.10).  The
full polynomial is

\[
\begin{aligned}
P(z)={}&1-(2+\tfrac52\sqrt2)z+(5+5\sqrt2)z^2\\
 &-(8+\tfrac72\sqrt2)z^3+(4+2\sqrt2)z^4-\sqrt2z^5.
\end{aligned}
\tag{2.3}
\]

The first four factors already make `K_bd` compact in `[0,4L]`; the final
source shift enlarges the odd-fibre kernel support only to `[0,5L]`.
Equivalently, the exact double roots

\[
 P(1)=P'(1)=P(1/\sqrt2)=P'(1/\sqrt2)=0
\tag{2.4}
\]

annihilate the affine and exponential tails.  This is finite-difference
telescoping, not an asymptotic cancellation claim.

Dyadic translation preserves the odd part of an integer.  Since `P(0)=1`,
the formal coefficient vector attached to each odd `m` is nonzero.  Thus no
further annihilation of an odd fibre follows from the finite shifts in
(2.2)--(2.3) alone.  The analytic overlap of the compact translates belonging
to different odd `m` remains, and it is precisely where a bound could still
live.

## 3. Boundary shells and the scout's balanced Jordan sides

Integrating (0.5), changing variables in the translated term, and using
causality gives (0.6).  More discretely, set

\[
 B_j=\int_{j\varepsilon}^{(j+1)\varepsilon}G(t)\,dt,
 \qquad
 H_j=\int_{j\varepsilon}^{(j+1)\varepsilon}h_\varepsilon(t)\,dt.
\tag{3.1}
\]

Then

\[
 \boxed{H_j={B_j-B_{j-1}\over\varepsilon},\qquad B_{-1}=0.}
\tag{3.2}
\]

This is the exact shell-by-shell telescope requested by the finite data.  It
controls signed mass, not Jordan mass.  If

\[
 A_\varepsilon(T)=\int_0^T|h_\varepsilon(t)|\,dt,
 \qquad
 N_\varepsilon(T)=\int_0^T(h_\varepsilon(t))_-\,dt,
\]

then the elementary Jordan identity and (0.6) give

\[
 \boxed{
 A_\varepsilon(T)
 =2N_\varepsilon(T)
  +{1\over\varepsilon}\int_{T-\varepsilon}^{T}G(u)\,du.}
\tag{3.3}
\]

This explains the finite scout's nearly `2:1` absolute-to-negative masses:
their discrepancy is exactly the signed terminal-shell term, not a second
independent bulk slope.  Using only the scout's reported rounded values,

\[
\begin{array}{c|rrr}
Y&2^{10}&2^{14}&2^{18}\\ \hline
A_\varepsilon(\log Y)-2N_\varepsilon(\log Y)
&4.623131028&5.497318419&-0.948171540.
\end{array}
\tag{3.4}
\]

These three floating-point residuals inherit every discretization caveat of
the scout.  Equation (3.3), by contrast, is exact.  It explains the balance
of the two fitted slopes; it does **not** explain or prove their apparent
linear growth in `log Y`.

## 4. Removing the box does not weaken the absolute criterion

Write

\[
 J(T)=\int_0^T|G(t)|\,dt,
 \qquad
 H_\varepsilon(T)=\int_0^T|h_\varepsilon(t)|\,dt.
\]

Equation (0.5) gives immediately

\[
 H_\varepsilon(T)\le {2\over\varepsilon}J(T).
\tag{4.1}
\]

Causal inversion of the same first difference gives the finite identity

\[
 G(t)=\varepsilon
 \sum_{0\le j\le t/\varepsilon}h_\varepsilon(t-j\varepsilon).
\tag{4.2}
\]

Hence

\[
 J(T)\le
 \varepsilon(\lfloor T/\varepsilon\rfloor+1)H_\varepsilon(T).
\tag{4.3}
\]

Multiplication by a fixed constant or by `1+T` preserves `e^(o(T))`.
Therefore, for every fixed `epsilon>0`,

\[
 \boxed{
 J(T)=e^{o(T)}
 \Longleftrightarrow
 H_\varepsilon(T)=e^{o(T)}.}
\tag{4.4}

Combining (4.4) with the repaired mollified-beta equivalence already proves
the absolute part of (0.7).  The next section gives the direct primitive
argument and also supplies its one-sided version.

## 5. Direct Mellin--Landau criterion for the primitive

For `Re(s)>1/2`, absolute Mellin--Stieltjes Fubini and (0.3) give

\[
 \boxed{
 \widehat G(s)
 ={M_{\rm ext}(s)\over s}
 {1-67^{-(s+1/2)}\over\zeta(s+1/2)}.}
\tag{5.1}
\]

The apparent quotient at `s=0` is removable because `K_ext` has the factor
`D`.  In the open half-strip `0<Re(s)<1/2`, division by `s` introduces no
zero or pole, and the source-audited multiplier `M_ext` is nonzero.  The
duplicate-`67` factor is also nonzero there.  Thus every zeta zero `rho`
with `Re(rho)>1/2` produces a genuine pole at `s=rho-1/2`.

Assume RH.  The normalized beta summatory function is
`O_delta(exp(delta t))` for every `delta>0`.  Since `K_bd` is compact BV,
the same Stieltjes summation-by-parts argument used for the mollified kernel
gives

\[
 |G(t)|=O_\delta(e^{\delta t}),
 \qquad J(T)=O_\delta(e^{\delta T}).
\tag{5.2}
\]

Conversely, suppose

\[
 \int_0^T(G(t))_-\,dt=e^{o(T)}.
\tag{5.3}
\]

The transform of `G_-` is then holomorphic in `Re(s)>0`.  The trivial bound
`|beta(n)|<=2` and the compact bounded kernel `K_bd` give `G_+` a finite
Laplace abscissa.  If that abscissa were positive, (5.1) plus the transform
of `G_-` would continue the transform of `G_+` holomorphically through its
positive real abscissa, contradicting Landau's theorem for a nonnegative
density.  Therefore both Jordan transforms converge in `Re(s)>0`, so (5.1)
is holomorphic there.  The genuine poles described above cannot occur.  The
functional equation then excludes their reflections and proves RH.

This proves (0.7).  It does not establish (5.3); (5.3) is another exact
RH-equivalent arithmetic target.

## 6. Native reflection form of the boundary field

Let `i_1(x)=I_1(e^x)` be the native half-divisor self-convolution of the
geodesic packet.  Since

\[
 \mathcal D_{\rm out}
 =D\mathcal R(D),
 \qquad
 \mathcal R(D)=5D^3-6D^2+\tfrac14D+\tfrac34,
\tag{6.1}
\]

the source identity gives

\[
 \boxed{G=\mathcal R(D)i_1.}
\tag{6.2}
\]

For a causal cutoff `R>T`, the exact reflection decomposition is

\[
 i_1(x)=\mathcal N_{1,R}-2\mathcal O_{1,R}(x)
 \qquad(x<R).
\tag{6.3}
\]

The constant term of `R(D)` is `3/4`, so

\[
 \boxed{
 G(x)=\tfrac34\mathcal N_{1,R}
      -2\mathcal R(D)\mathcal O_{1,R}(x)
 \qquad(x<R).}
\tag{6.4}
\]

Applying `(1-tau_epsilon)/epsilon` kills the norm term exactly and recovers
the native reflection criterion:

\[
 h_\varepsilon
 =-{2\over\varepsilon}(1-\tau_\varepsilon)
       \mathcal R(D)\mathcal O_{1,R}.
\tag{6.5}
\]

This identifies a load-bearing obstruction in any attempt to estimate the
primitive directly from positivity of the odd reflection energy: before the
finite difference, the large cutoff norm survives with coefficient `3/4`.
The box difference removes that constant algebraically, but it does not give
a sign to the remaining third-order energy current.

## 7. Exact limit of formal telescoping

Boundary telescoping cannot be applied after taking a positive, negative, or
absolute part.  This failure is not a technicality.  For an arbitrary
`A>0`, take the causal field

\[
 G_A=A1_{[0,\varepsilon)}.
\]

Then

\[
 {1\over\varepsilon}(1-\tau_\varepsilon)G_A
 ={A\over\varepsilon}1_{[0,\varepsilon)}
  -{A\over\varepsilon}1_{[\varepsilon,2\varepsilon)}.
\tag{7.1}
\]

For every `T>=2epsilon`, its terminal boundary and signed mass are zero,
while its negative mass is `A` and its absolute mass is `2A`.  Thus no bound
for either Jordan side can follow from (0.6) alone.

This counterexample is deliberately scoped to the formal finite-difference
argument; it is not a counterexample to the beta detector.  Together with
`P(0)=1`, it gives the precise no-go:

```text
exact dyadic/source compression             complete
exact signed boundary-shell telescope       complete
Jordan-mass telescope from those identities impossible in general
cross-odd-index arithmetic cancellation     still RH-bearing and open
```

The near-logarithmic finite variation remains a numerical observation.  The
new exact information is that the near equality of its positive and negative
bulk is a boundary phenomenon, and that one cannot turn this signed
telescope into the required one-sided estimate without additional
arithmetic input.

## 8. Scope and replay

Proved here:

- the compact BV causal primitive `K_bd` and the exact first-difference
  identity (0.5);
- the signed boundary-shell identities (0.6), (3.2), and (3.3);
- exact odd-fibre compression and the compact kernel (0.9)--(0.10);
- the box-independent absolute and one-sided RH criterion (0.7);
- the native reflection primitive identity (6.4);
- the formal Jordan-telescoping obstruction (7.1).

Not proved here:

- logarithmic, polylogarithmic, or subpower variation for `G` or
  `h_epsilon`;
- a sign orientation for the reflection current;
- cancellation between distinct odd beta indices;
- RH or GRH.

Replay:

```text
python -B research/l-families/atlas/function_field/ffps_mollified_beta_boundary_shell_identity.py --check
python -B -O research/l-families/atlas/function_field/ffps_mollified_beta_boundary_shell_identity.py --check
python -B -m unittest tests.test_ffps_mollified_beta_boundary_shell_identity
python -B -O -m unittest tests.test_ffps_mollified_beta_boundary_shell_identity
```

The replay checks exact `Q(sqrt(2))` polynomial arithmetic, the two tail
annihilations, sample duplicate-`67` source fibres, finite-difference/Jordan
identities, the canonical JSON, and every frozen source blob.  It enumerates
no source range, prime interval, conductor, curve, point, or zeta zero.
