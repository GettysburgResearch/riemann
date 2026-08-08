# L-30410 — The parity child is a critical-compatible scale filter

Claim ID: `L-30410`  
Title: After the mandatory endpoint halving is included, the parity recurrence is isometric on critical-line zero modes and strictly contractive on every hypothetical zero to their right  
Status: **PROPOSED COMPLETE EXACT SPECTRAL LEMMA — INDEPENDENT REVIEW REQUESTED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Dependencies: `L-30407`; elementary eta factorization  
Corrects scope of: `R-30405`, which applies only to a same-scale multiplier and does not include endpoint descent  
Scope: spectral multiplier of the exact half-scale child; no boundary estimate or RH conclusion

## 1. Even-endpoint recurrence

Take an even endpoint

\[
N=2Q.
\tag{L-30410.1}
\]

For a complex parameter `z`, put

\[
s={1\over2}+z.
\]

The source recurrence of `L-30407` contains the child term

\[
[1-\eta(s)]M_s(Q/m).
\tag{L-30410.2}
\]

A scale mode of horizontal-frequency exponent `z` has the form

\[
\boxed{
\mathfrak e_z(N,m)
=N^z m^{-1/2-z}.}
\tag{L-30410.3}
\]

At the child endpoint,

\[
\mathfrak e_z(Q,m)
=2^{-z}\mathfrak e_z(N,m).
\tag{L-30410.4}
\]

Therefore the complete child multiplier relative to the current endpoint is

\[
\boxed{
\kappa_2(z)
=2^{-z}
[1-\eta(1/2+z)].}
\tag{L-30410.5}
\]

The factor `2^(-z)` is part of the theorem. Omitting it replaces a scale
recurrence by an incorrect same-scale statement.

## 2. Value at zeta zeros

Let

\[
\rho={1\over2}+z_\rho
\]

be a nontrivial zeta zero. Since

\[
\eta(s)=(1-2^{1-s})\zeta(s),
\]

one has

\[
\eta(\rho)=0.
\]

Consequently

\[
\boxed{
\kappa_2(z_\rho)=2^{-z_\rho}.}
\tag{L-30410.6]
\]

The closing bracket in the tag is typographical only.

Taking moduli gives

\[
\boxed{
|\kappa_2(z_\rho)|
=2^{-\Re z_\rho}
=2^{-(\Re\rho-1/2)}.}
\tag{L-30410.7]
\]

## 3. Exact critical compatibility

If `rho` lies on the critical line, then `Re z_rho=0`, and

\[
\boxed{|\kappa_2(z_\rho)|=1.}
\tag{L-30410.8]
\]

Thus the scale recurrence does not suppress legitimate critical-line modes.
They are transported isometrically to the half-scale child, up to their phase
`2^(-i Im rho)`.

If a hypothetical zero satisfies `Re rho>1/2`, put

\[
\delta=\Re\rho-1/2>0.
\]

Then

\[
\boxed{|\kappa_2(z_\rho)|=2^{-\delta}<1.}
\tag{L-30410.9]
\]

The same recurrence is strictly contractive on that off-line mode.

This is precisely the spectral orientation required of an RH-compatible scale
filter.

## 4. Correction of the same-scale no-go

`R-30405` correctly observes that

\[
1-\eta(\rho)=1
\]

at every zeta zero. It therefore rejects a **same-scale** strict norm estimate
which uses only the eta multiplier.

It does not reject the actual endpoint recurrence, whose child is evaluated at
`Q=N/2`. The correct conclusions are:

```text
same-scale parity multiplier at a zero       1;
full half-scale child multiplier             2^(-z_rho);
critical-line modulus                        1;
right-off-line modulus                        <1.
```

Any use of `R-30405` which declares the full half-scale recurrence saturated at
an off-line zero is superseded by (L-30410.7).

## 5. Exponent-level consequence

Suppose a source-compatible block quantity has exponential scale exponent
`lambda` and the child is evaluated at half endpoint. A mode with endpoint
growth `N^delta` contributes

\[
N^\delta
\longmapsto
2^{-\delta}N^\delta
\]

under the zero-mode child coefficient. Iterating `j` times gives

\[
2^{-j\delta}N^\delta
=(N/2^j)^\delta.
\tag{L-30410.10]
\]

Thus an exact recurrence with subexponential forcing is neutral at `delta=0`
and decays geometrically for every `delta>0`.

This is stronger and more correctly typed than a uniform constant contraction:
it preserves the entire critical line while separating every rightward mode.

## 6. Remaining boundary obligation

The lemma does not prove that the forcing source `sigma_N` is subexponential in
a compatible physical norm. `R-30404` rules out proving that through absolute
atomic variation. `L-30405`--`L-30409` provide its exact signed structure and
positive moment hierarchy.

A completed RH proof still needs a pole-preserving reflected estimate which
shows that the boundary forcing is either:

1. lower safe-order and inductively controlled;
2. a tempered critical-line channel; or
3. a genuinely smaller-scale packet.

Only after that estimate is proved may (L-30410.9) be used as the strict
right-half-plane scale contraction.

## 7. Proof boundary

Proved exactly here:

- the complete half-scale multiplier;
- its value at every zeta zero;
- isometry on the critical line;
- strict contraction on every right-off-line zero;
- the exact correction to the same-scale interpretation.

Not proved here:

- a compatible norm estimate for the boundary forcing;
- a complete scale recurrence;
- RH.
