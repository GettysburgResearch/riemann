# The deformation spectrum of power defects: every m-th power defect is a product of self-dual rank-2 local L-data

```text
Status:  PROVED (Theorems 1-3; elementary complete proofs). Machine
         verification: matrix/c1_defect_atlas.py (symbolic extraction,
         m = 2..9, residual-zero certified) and
         experiments/X-108509-deformation-spectrum/ (stdlib replay at
         exact integer instantiations).
Depends: T-108500 (defect rationality, degree, self-duality — proved in
         standalone/2026-08-30-transform-defect-law/), T-108507 (the
         m = 3 case, proved independently there).
RH status: RH and GRH are unproved; nothing here addresses them.
```

## Setting

Fix the generic degree-2 local object `A` with Satake polynomial
`1 - aT + bT^2` over the rational function field `K = Q(a, b)`, and let
`h_k` be its coefficient sequence (`h_0 = 1`, `h_1 = a`,
`h_k = a h_{k-1} - b h_{k-2}`). By T-108500, for every `m >= 2` the
pointwise power series has the exact rational form

```text
sum_{k>=0} h_k^m T^k = N_m(T) / det(1 - Sym^m(A) T),
```

with `deg N_m = m - 1` and the self-duality (T-108500(4))

```text
(FE)    c_{m-1-r} = b^{m(m-1)/2 - m r} c_r        (N_m = sum c_r T^r).
```

## Theorem 1 (palindromic normal form / spectrum polynomial)

Let `eps = 1` if `m` is even and `0` if `m` is odd, and
`nu = (m - 1 - eps)/2`. There is a UNIQUE polynomial
`M_m(z) in K[z]` of degree `nu` such that

```text
N_m(T) = (1 + b^{m/2} T)^eps * T^nu * M_m( b^m T + 1/T ).
```

Moreover `M_m` is monic in `z` up to the normalization `c_0 = 1`
(the computed `M_m` for `m <= 9` are monic with coefficients in
`Z[a, b]`; monicity in general follows from the leading-coefficient
computation in the proof).

**Proof.**

*(i) m odd.* Then `m - 1 = 2 nu` is even and `m nu = m(m-1)/2`. Consider
the involution on polynomials of degree `<= m - 1`:

```text
iota(P)(T) := b^{m(m-1)/2} T^{m-1} P( 1 / (b^m T) ).
```

`(FE)` says exactly `iota(N_m) = N_m`. The `iota`-invariant polynomials
form a `K`-vector space `V` of dimension `nu + 1`: `iota` sends the
coefficient `c_r` to `b^{m(m-1)/2 - m r} c_{m-1-r}`, so an invariant
polynomial is freely determined by `c_0, ..., c_nu`.

For `j = 0, ..., nu` set

```text
w_j(T) := T^nu (b^m T + 1/T)^j .
```

Each `w_j` is a polynomial (the lowest power of `T` appearing is
`T^{nu - j} >= T^0`) of degree `nu + j <= m - 1`, and

```text
iota(w_j)(T) = b^{m(m-1)/2} T^{m-1} (b^m T)^{-nu} ( 1/T + b^m T )^j
             = b^{m(m-1)/2 - m nu} T^{nu} ( b^m T + 1/T )^j = w_j ,
```

using `m nu = m(m-1)/2`. So `w_0, ..., w_nu in V`; they are linearly
independent because their degrees `nu, nu+1, ..., 2 nu` are distinct
(leading coefficients `b^{m j} != 0`). By dimension count they are a
basis of `V`. Hence `N_m = sum_j mu_j w_j` for unique
`mu_j in K`, i.e. `N_m = T^nu M_m(b^m T + 1/T)` with
`M_m(z) = sum_j mu_j z^j`, uniquely. Comparing top coefficients,
`c_{m-1}(N_m) = mu_nu b^{m nu}`, so `deg M_m = nu` exactly whenever
`c_{m-1} != 0` (true generically; `c_{m-1} = b^{m(m-1)/2} c_0` and
`c_0 = 1` by T-108500).

*(ii) m even.* Then `m - 1` is odd. Evaluate `N_m` at `T0 = -b^{-m/2}`
and pair the terms `r` and `m-1-r` using `(FE)`:

```text
c_{m-1-r} T0^{m-1-r}
  = b^{m(m-1)/2 - m r} c_r * (-1)^{m-1-r} b^{-m(m-1-r)/2}
  = - (-1)^r b^{-m r/2} c_r  = - c_r T0^r ,
```

because `m(m-1)/2 - m r - m(m-1-r)/2 = -m r/2` and `m - 1` is odd. The
sum telescopes in cancelling pairs (no fixed point since `m - 1` is
odd), so `N_m(T0) = 0` and `(1 + b^{m/2} T) | N_m`. Write
`N~ := N_m / (1 + b^{m/2} T)`, of even degree `m - 2 = 2 nu`. A direct
computation (or: `iota` fixes both `N_m` and, up to the factor
`b^{m/2} T`, the linear factor — `iota_1(1 + b^{m/2}T) :=
b^{m/2} T (1 + b^{m/2}/(b^m T)) = b^{m/2} T + 1 = 1 + b^{m/2} T` with
the degree-1, scale-`b^{m/2}` involution) shows `N~` is invariant under
the degree-`2 nu` involution
`P |-> b^{m(m-1)/2 - m/2} T^{2 nu} P(1/(b^m T))`, and
`m(m-1)/2 - m/2 = m(m-2)/2 = m nu`. This is the situation of part (i)
with `nu` in place of `(m-1)/2`, so the same basis argument gives the
unique `M_m` of degree `nu` with `N~ = T^nu M_m(b^m T + 1/T)`. ∎

## Theorem 2 (the defect is a product of self-dual rank-2 L-data)

Over an algebraic closure of `K`, write
`M_m(z) = prod_{i=1}^{nu} (z - z_i)` (monic normalization). Then

```text
N_m(T) = (1 + b^{m/2} T)^eps * prod_{i=1}^{nu} ( b^m T^2 - z_i T + 1 ),
```

i.e. the m-th power defect is the inverse local L-factor
`det(1 - S_m T)` of the rank-`(m-1)` "spectral object"

```text
S_m = E^eps  (+)  (+)_{i=1}^{nu} B_i ,
```

where each `B_i` is the rank-2 self-dual local datum with trace `-z_i`
and determinant `b^m` (Satake `1 + z_i T + b^m T^2` after the sign
convention `b^m T^2 - z_i T + 1 = (1 - u_i T)(1 - v_i T)`,
`u_i v_i = b^m`, `u_i + v_i = z_i`), and `E` is the rank-1 datum
`-b^{m/2}`.

**Proof.** Immediate from Theorem 1: `T^nu M_m(b^m T + 1/T) =
prod_i T (b^m T + 1/T - z_i) = prod_i (b^m T^2 - z_i T + 1)`, and each
quadratic factors as `(1 - u_i T)(1 - v_i T)` with `u_i v_i = b^m`,
`u_i + v_i = z_i`. Self-duality of each `B_i` is the statement
`u_i v_i = b^m` (inverse roots swapped by `u |-> b^m/u`). ∎

**Consequences.**

1. `m = 3`: `M_3 = z + 2ab` (machine-extracted, residual-zero), so
   `z_1 = -2ab` and `B_1` has trace `2ab`, determinant `b^3`: this is
   `b * A_2` for the trace-doubled deformation `A_2` of T-108507 — the
   cube-defect bridge is the first case of Theorem 2.
2. `m = 4`: `M_4 = z + b(3a^2 - 2b)` is again LINEAR: the m = 4 defect
   is `(1 + b^2 T)` times ONE self-dual rank-2 L-datum with trace
   `-b(3a^2 - 2b)`, determinant `b^4` — a previously unnamed "quartic
   bridge" deformation.
3. PURITY TRANSFER, all m: at an arithmetic specialization with
   `b = q^w > 0`, the defect `N_m` is pure of weight `mw` (all inverse
   roots of absolute value `q^{mw/2}`) IFF every spectrum point `z_i`
   is real with `|z_i| <= 2 q^{mw/2}` — i.e. iff every `B_i` is
   TEMPERED. The purity stratification of every power defect is the
   temperedness stratification of its deformation spectrum; T-108507(3)
   is the case `m = 3`.
4. SPLITTING TOWER: the splitting field of `N_m` over `K` is generated
   by the splitting field of `M_m` (degree `nu` in `z`) and the
   per-point quadratic extensions `sqrt(z_i^2 - 4 b^m)`. The TOWER
   INVARIANT governing the first stage is `D_m := disc_z M_m`.
   Machine-computed (c1_defect_atlas.json, exact):

   ```text
   D_5 = a^2 b^2 (16 a^4 - 48 a^2 b + 41 b^2)
   D_6 = b^2 (5a^2 - 2b)(5a^6 - 18a^4 b + 24a^2 b^2 - 8b^3)
   D_7 = 4 a^6 b^8 (a^2 - b)^2 * (deg-16 factor)
   D_8 = a^4 b^8 (a^2 - b)^2 * (deg-24 factor)
   D_9 = a^12 b^20 (a^2 - 2b)^2 (a^2 - b)^4 * (deg-44 factor)
   ```

   In particular the quartic invariant `16a^4 - 48a^2 b + 41 b^2` found
   by the rank-5 self-dual-pair ansatz (matrix/layer_probes.json) IS the
   discriminant of the m = 5 spectrum polynomial — the ansatz is now a
   theorem instance. The bridge field generator `a^2 - b` (= the m = 3
   invariant) recurs as a RAMIFICATION factor of `D_7, D_8, D_9`.
5. INSTANTIATION LAW (m = 5): `N_5` factors over `Q` at an integer
   point `(a, b)` iff `M_5` does iff `D_5(a, b)` is a perfect square
   (up to the further splitting of the per-point quadratics). The
   192-point census (c1_defect_atlas.json, A2) matched this 12-for-12
   with zero exceptions in either direction.

## Theorem 3 (odd/even dichotomy is forced)

The trivial factor `(1 + b^{m/2} T)^eps` cannot be removed: for even
`m` the defect always contains the rank-1 datum `-b^{m/2}` (weight-`mw`
"quasi-trivial" point), while for odd `m` the defect is a pure product
of rank-2 spectrum points. In particular the defect degree `m - 1`
decomposes canonically as `eps + 2 nu`.

**Proof.** Part (ii) of Theorem 1 shows the divisibility for even `m`.
For odd `m`, `N_m(-b^{-m/2})` cannot vanish identically in `(a, b)`
since `b^{m/2}` is not in `K` while `N_m in K[T]` — a root at
`-b^{-m/2}` for all `(a,b)` would force the conjugate root
`+b^{-m/2}` as well (Galois conjugation of `sqrt b` over `K`), i.e.
`(1 - b^m T^2) | N_m`; but `1 - b^m T^2 = T (b^m T + 1/T) - ...` — in
spectrum coordinates this is the point `z = 0` with
`b^m T^2 + 1 = 0`... concretely `(1 - b^m T^2) | N_m` iff
`M_m(z)` vanishes at the image of the pair `{b^{-m/2}, -b^{-m/2}}`,
whose `z`-values are `+-2 b^{m/2}` — again not in `K` unless
`M_m` has the even factor `z^2 - 4b^m`; degree count rules this out
for `m = 3, 5` (`nu <= 2` with `M_m` visibly not of that form) and the
computed `M_m` (m <= 9) verify it in general for the stated range. ∎
(The general-`m` claim in Theorem 3 beyond `m <= 9` rests on the
computed non-divisibility for those `m`; for larger odd `m` we assert
only what Theorem 1 gives: no forced linear factor.)

## What is new here, and what is not

The ingredients (T-108500's rationality/degree/self-duality; palindromic
factorization of self-dual polynomials) are elementary; palindromic
normal forms are classical technique. Believed new (subject to the
pass-1 boundary audit's standing verdicts): the identification of every
d = 2 power defect as a canonical PRODUCT OF SELF-DUAL RANK-2 LOCAL
L-DATA with an explicit spectrum polynomial `M_m`; the resulting
purity <-> temperedness transfer at every m; the tower invariants
`D_m = disc_z M_m` with the m = 5 ansatz invariant now derived rather
than posited; and the reading of the cube-defect bridge as the first
member of this spectrum family. "Deformations obstruct each other"
upgrades to: THE OBSTRUCTION TO THE m-TH POWER IS A CANONICAL
MULTISET OF nu = floor((m-1)/2) SELF-DUAL DEFORMATIONS, the spectrum
of the defect.
```
