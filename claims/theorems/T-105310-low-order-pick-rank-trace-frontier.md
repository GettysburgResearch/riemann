# T-105310 — Quantitative low-order Pick-compression frontier

Claim ID: `T-105310`  
Status: **CONDITIONAL XI THEOREM; FINITE/MODEL SPINE PROVED**  
Created: 2026-08-23  
Depends on: `L-105300--L-105303`, `L-105310--L-105312`  
RH status: **unproved**

## 1. Relation to the existing low-order theorem

The current PR already proves the exact full Hermite--Pick signature and the
regular entire-window compression inequality.  This checkpoint adds:

1. confluent/nonreal positive-index control for growing subcompressions;
2. an exact use of both unconditional xi-prime proportions;
3. a concrete Cauchy-power gamma model with a one-percent arithmetic target;
4. a rounding-safe comparison with the published Montgomery--Taylor constant.

Let `K_T` be a source-fixed finite compression of the affine-centered Pick
kernel of `Xi/Xi'` on `(T,2T]`.  Put

\[
\eta_T=
\frac{(\operatorname{tr}K_T)_+^2}
{N_1(T)\|K_T\|_{\rm HS}^2},
\tag{T-105310.1}
\]

where `N_1(T)` is the total xi-prime zero count, with multiplicity.  The
canonical-product, generic-splitting, boundary and compression-tail errors
must contribute `o(N_1(T))` to positive index or to the reverse--Rolle count.

## 2. Multiplicity-robust descent

The unconditional quartic xi-prime theorem supplies

\[
S_1/N_1\ge 5429/6250-o(1),
\qquad
D_1/N_1\ge11679/12500-o(1).
\]

By `L-105310/L-105311`, every nonreal or confluent positive-inertia block has
total charge at most

\[
\nu_T\le\frac{821}{10000}N_1(T)+o(N_1(T)).
\tag{T-105310.2}
\]

Thus the number `G_T` of simple real Rolle-generating critical points obeys

\[
G_T\ge
\left(\eta_T-\frac{821}{10000}\right)N_1(T)-o(N_1(T)).
\tag{T-105310.3}
\]

Exact reverse Rolle and the adjacent zero-count comparison then give

\[
\boxed{
\liminf\frac{N_0(T,2T)}{N(T,2T)}
\ge
2\liminf\eta_T-1-\frac{821}{5000}.
}
\tag{T-105310.4}

Here `N_0` counts critical-line zeros with multiplicity.  A simple-zero
version additionally needs the common-zero/multiple-parent charge to be
`o(N(T))`.

## 3. Rounding-safe record threshold

The published optimized Montgomery--Taylor constant is

\[
0.672500703679\ldots<0.672501.
\]

Therefore the safe target

\[
\boxed{\liminf\eta_T\ge919/1000}
\tag{T-105310.5}
\]

implies

\[
\boxed{
\liminf\frac{N_0(T,2T)}{N(T,2T)}
\ge3369/5000=0.6738,
}
\tag{T-105310.6}

which is numerically larger.  This is a **record-breaking criterion**, not a
proved new record.

## 4. Concrete one-percent Cauchy-power target

`L-105312` proves that the archimedean Cauchy-power model has normalized
effective rank at least `49/51`.  If the arithmetic Xi matrix satisfies

\[
\operatorname{tr}K_T\ge0.99\operatorname{tr}G_T,
\qquad
\|K_T\|_{\rm HS}\le1.01\|G_T\|_{\rm HS},
\tag{T-105310.7}
\]

with matching dimension and `o(N_1)` tails, then

\[
\eta_T\ge
\frac{49}{51}\left(\frac{99}{101}\right)^2
=
\frac{160083}{173417}
=0.923110\ldots.
\]

The multiplicity-robust conclusion becomes

\[
\boxed{
\liminf\frac{N_0(T,2T)}{N(T,2T)}
\ge
\frac{591369643}{867085000}
=0.682020\ldots.
}
\tag{T-105310.8}

On fully regular windows, the existing `L-105303` full-signature inequality
would instead give the stronger direct value

\[
2\frac{160083}{173417}-1
=
\frac{146749}{173417}
=0.846220\ldots,
\]

but the robust theorem does not assume that all multiplicity/common-zero
interfaces have already disappeared.

## 5. Exact remaining theorem

```text
LPRT105310:
  construct the source-owned Cauchy-power compression of Xi/Xi', prove the
  99% trace and 101% HS comparisons, and bound all canonical-product,
  splitting, boundary and common-zero errors at o(N_1(T)).
```

This is a low-order explicit-formula/prime-side matrix estimate.  It does not
descend from a high derivative and it does not ask for pointwise residue
coherence.

## 6. Boundary

```text
full simple-window Hermite inertia           inherited proved
confluent compressed inertia                 proved exact
xi-prime nuisance density 0.0821             proved exact
Cauchy-power gamma reserve                   proved
0.919 -> 0.6738                              proved conditional
one-percent arithmetic Xi comparison         open
simple-zero upgrade                          open
new record / RH                              unproved
```
