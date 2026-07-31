# L-19808 — Critical-cell smoothing does not attenuate a fixed off-line zero

Claim ID: `L-19808`  
Title: Square-cell averaging suppresses only ordinates on the moving scale; every fixed off-line zero survives with its full polynomial amplitude  
Status: `PROPOSED — COMPLETE ASYMPTOTIC PROOF`  
Authoring agent: `gpt56-pro-09-i`  
Created: 2026-08-01  
Dependencies: Nakamura--Suzuki zero expansion; elementary Taylor expansion  
Scope: exact boundary of `T-19804/L-19807`

## 1. General square-cell multiplier

Let `w` be a nonnegative integrable function on `[0,1]` with

\[
 \int_0^1 w(u)\,du=1,
 \qquad
 \mu_1=\int_0^1u\,w(u)\,du.
 \tag{L-19808.1}
\]

For an integer `n>=1`, set

\[
 x_n(u)=n^2+(2n+1)u
 \tag{L-19808.2}
\]

and define, for a complex centered frequency `z`,

\[
 J_{n,w}(z)=\int_0^1w(u)x_n(u)^{-iz}\,du.
 \tag{L-19808.3}
\]

This is the zero-side multiplier of every positive normalized average of the
zeta screw function over the square cell `[n^2,(n+1)^2]`.

## 2. Fixed-frequency asymptotic

For every fixed compact set `K subset C`, uniformly for `z in K`,

\[
 \boxed{
 J_{n,w}(z)
 =n^{-2iz}
 \left(
  1-{2iz\mu_1\over n}+O_K(n^{-2})
 \right).}
 \tag{L-19808.4}
\]

If `w(u)=30u^2(1-u)^2`, then `mu_1=1/2`, and

\[
 \boxed{
 J_{n,\beta}(z)
 =n^{-2iz}
 \left(1-{iz\over n}+O_K(n^{-2})\right).}
 \tag{L-19808.5}
\]

### Proof

Write

\[
 {x_n(u)\over n^2}
 =1+{2u\over n}+{u\over n^2}.
\]

Uniformly for `0<=u<=1`,

\[
 \log{x_n(u)\over n^2}
 ={2u\over n}+O(n^{-2}).
 \tag{L-19808.6}
\]

For `z` in a fixed compact set,

\[
 \exp\left(-iz\log{x_n(u)\over n^2}\right)
 =1-{2izu\over n}+O_K(n^{-2})
 \tag{L-19808.7}
\]

uniformly in `u`. Multiplication by `n^{-2iz}`, integration against `w`, and
(L-19808.1) prove (L-19808.4). The beta weight is symmetric about `1/2`, so its
first moment is `1/2`. QED.

## 3. Off-line growth survives unchanged

Let

\[
 z=a+ib,
 \qquad b>0,
 \tag{L-19808.8}
\]

be fixed. Then

\[
 \boxed{
 |J_{n,w}(z)|
 =n^{2b}\left(1+O_z(n^{-1})\right).}
 \tag{L-19808.9}
\]

Thus square-cell smoothing does not gain even one power of `n` against a fixed
off-line zero. Endpoint vanishing and repeated integration by parts are useful
only when `|a|` is comparable to or larger than `n`; they do not affect a fixed
frequency.

This is the exact uncertainty scale:

```text
logarithmic cell width  asymptotic to 2/n,
frequency resolution   asymptotic to n.
```

## 4. Quartet contribution

Use the centered zero convention in which

\[
 \Psi(t)=\sum_\gamma m_\gamma{1-e^{-i\gamma t}\over\gamma^2}.
 \tag{L-19808.10}
\]

Suppose a nonreal quartet contains the centered parameters

\[
 z=a+ib,
 \quad -\overline z=-a+ib,
 \quad \overline z=a-ib,
 \quad -z=-a-ib,
 \qquad b>0,
 \tag{L-19808.11}
\]

with common multiplicity `m`. Let `C_{w,z}(n)` be this quartet's contribution
to the square-cell average. The two parameters with positive imaginary part
supply the growing term

\[
 \boxed{
 C_{w,z}(n)
 =C_z^{(0)}
 -2m n^{2b}
 \Re\left({e^{-2ia\log n}\over z^2}\right)
 +O_z(n^{2b-1})+O_z(n^{-2b}),}
 \tag{L-19808.12}
\]

where `C_z^(0)` is independent of `n`.

### Proof

The symmetry (L-19808.11) and reality of `w` give

\[
 J_{n,w}(-\overline z)=\overline{J_{n,w}(z)}.
\]

The oscillatory part of the positive-imaginary pair is therefore

\[
 -m{J_{n,w}(z)\over z^2}
 -m{J_{n,w}(-\overline z)\over(-\overline z)^2}
 =-2m\Re{J_{n,w}(z)\over z^2}.
\]

Insert (L-19808.4). The negative-imaginary pair is `O_z(n^-2b)`, while all four
constant `1/gamma^2` terms combine into `C_z^(0)`. QED.

The leading term has amplitude

\[
 {2m\over|z|^2}n^{2b}.
 \tag{L-19808.13}
\]

For the isolated quartet it takes negative values of this order along infinitely
many integers: choose integers nearest to

\[
 \exp\left({2\pi k+\vartheta\over2|a|}\right)
\]

with `vartheta` aligning the phase in (L-19808.12). The rounding phase error is
`o(1)`.

## 5. General local-average barrier

The same conclusion is not special to the polynomial beta weight. Let `mu_n` be
any probability measure supported in a logarithmic interval of diameter
`ell_n->0`, centered at `t_n`. Its multiplier

\[
 M_n(z)=\int e^{-izt}\,d\mu_n(t)
\]

satisfies, for every fixed `z`,

\[
 \boxed{
 e^{izt_n}M_n(z)=1+O_z(\ell_n).}
 \tag{L-19808.14}
\]

Therefore every positive local averaging scheme fine enough to recover
pointwise screw positivity also preserves a fixed off-line exponential mode.
For the square mesh, `ell_n=Theta(1/n)`.

## 6. Consequence for the claimed remaining theorem

`L-19807` proves an unconditional `O_A(log n)` bound for zeros with
`|Re gamma|>=An`. Equation (L-19808.9) proves that this estimate cannot be
extended through the moving block by additional endpoint smoothness: a fixed
off-line zero eventually lies in `|Re gamma|<An` and contributes
`n^(2b)`.

Hence the target

\[
 [\mathcal R_\beta(n)-\mathcal B_\beta(n)]_+=n^{o(1)}
 \tag{L-19808.15}
\]

requires genuine exclusion of every fixed off-line zero. It cannot follow from:

1. a sharper high-zero tail;
2. more integrations by parts in one square cell;
3. zero-density estimates that allow even one fixed off-line zero;
4. a finite verified critical-line height;
5. endpoint regularity of the averaging profile.

This is consistent with `L-19802`: the negative-part growth exponent is exactly
the horizontal displacement of the rightmost zero.

## 7. Proof boundary

- The multiplier and quartet asymptotics are exact.
- The theorem does not rule out cancellation among several off-line quartets in
the complete zero sum; `L-19802` handles the aggregate exponent without such a
noncancellation assumption.
- The result is a scope theorem, not a proof of RH.
- Any successful continuation must introduce information that excludes the
fixed-frequency inner block itself, rather than further polishing the outer
zero tail.