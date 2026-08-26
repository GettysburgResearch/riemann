# L-102836 — Square-core nonzero-phase energy has a uniform long/short bound

Claim ID: `L-102836`  
Status: **PROVED UNCONDITIONALLY**  
Created: 2026-08-24  
Depends on: `L-102832`; `L-102835`  
RH status: **not assumed**

Let `ell` be an odd prime, let `Q` be a semiprime squareclass coprime to
`ell`, and let `phi` be any fixed compact log-kernel whose autocorrelation is
supported in `[-log 8,log 8]`.

On one square-core octave `B<=b<2B`, define

\[
F_{h,Q}(u)
={1\over\sqrt Q}
\sum_{B\le b<2B}
{d_b\over b}
 e_\ell(hQb^2)
 \phi(u-\log Q-2\log b),
\]

where `|d_b|<=1` and `0<=h<ell`.

Then

\[
\boxed{
\sum_{h=0}^{\ell-1}\|F_{h,Q}\|_2^2
\ll_\phi
{1\over Q}\left(1+{\ell\over B}\right).
}
\tag{L-102836.1}

The same estimate holds with the `h=0` term removed.

## Proof

Expand the left side and use additive orthogonality:

\[
\sum_{h=0}^{\ell-1}
 e_\ell(hQ(b^2-b'^2))
=
\ell\,\mathbf1_{b^2\equiv b'^2\pmod\ell}.
\]

Because `ell` is prime and `ell` does not divide `Q`,

\[
b^2\equiv b'^2\pmod\ell
\quad\Longrightarrow\quad
b'\equiv b\ \text{or}\ -b\pmod\ell.
\]

The autocorrelation support also forces

\[
1/\sqrt8<b/b'<\sqrt8.
\]

For each fixed `b` in the octave, the harmonic weight of all admissible `b'`
in either residue progression is

\[
\ll {1\over\ell}+{1\over B}.
\]

Summing the outer weight `1/b` over one octave costs `O(1)`. Multiplication by
`ell/Q` proves (L-102836.1).

For `ell=2`, the same conclusion follows directly with a changed absolute
constant.

## Two regimes

```text
long core B>=ell:
  sum_h ||F_(h,Q)||^2 << 1/Q;

short core B<ell:
  sum_h ||F_(h,Q)||^2 << ell/(B Q).
```

This is a genuine nonzero-phase gain. It requires no cancellation in the core
coefficients.

## Scope

The theorem controls the complete phase packet for one fixed non-`ell`
squareclass. Summing coherently over different owner squareclasses is the
remaining large-sieve/dispersion interface in `T-102840`.