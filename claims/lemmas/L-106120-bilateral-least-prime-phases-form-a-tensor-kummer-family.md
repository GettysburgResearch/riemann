# L-106120 — The two least reduced-core primes form an exact tensor Kummer family

Claim ID: `L-106120`  
Programme aliases: `LFAM1.BILATERAL_LEAST_PRIME`, `LFAM2.BI_KUMMER_ROUGH_CORES`, `STRESS.TWO_SIDED_BOOLEAN_PHASE_TENSOR`  
Status: **PROVED EXACT SOURCE PARTITION AND TENSOR FAMILY IDENTITY**  
Created: 2026-08-25  
Depends on: parent `L-102955--L-102959`, `L-102963`, `T-102990`; `L-106090`, `L-106110`  
Programme issues: #743, #736, #737  
RH status: **not assumed**

After exact common-square extraction, every live Boolean incidence pair is

\[
 N=P g^2c^2,
 \qquad
 M=Q g^2d^2,
 \qquad
 c,d>1,
 \qquad
 (c,d)=1.
\tag{L-106120.1}
\]

Define the two canonical internal phase primes

\[
 \ell=P^-(c),
 \qquad
 \rho=P^-(d).
\tag{L-106120.2}
\]

Coprimality gives `ell!=rho`.  The assignment is unique and coefficient-exact;
no ordering between `ell` and `rho` is required.

## 1. Two same-occurrence nonzero phases

The clean incidence reductions ensure

\[
 \ell\mid N,
 \quad \ell\nmid M,
 \qquad
 \rho\mid M,
 \quad \rho\nmid N.
\tag{L-106120.3}
\]

Therefore the two prime Ramanujan identities are

\[
 -1=\sum_{h=1}^{\ell-1}e_\ell(h(N-M)),
 \qquad
 -1=\sum_{k=1}^{\rho-1}e_\rho(k(N-M)).
\]

Multiplying gives the source-exact positive identity

\[
\boxed{
 1=
 \sum_{h=1}^{\ell-1}
 \sum_{k=1}^{\rho-1}
 e_\ell(h(N-M))e_\rho(k(N-M)).
}
\tag{L-106120.4}
\]

Both phases belong to the same physical interaction.  By parent `L-102963`,
they may be endpoint-placed independently of the canonical equal-pair owner
coordinate.  Parent `L-102959` retains their complete incidence masks in the
literal physical-product phase transform.

## 2. Complete bilateral amplification

Fix common core `g`, phase primes `(ell,rho)`, and the two owner quadratic
classes

\[
 \sigma=\kappa_\ell(Q),
 \qquad
 \tau=\kappa_\rho(P).
\]

After Mellin polarization, define

\[
\boxed{
 \mathcal W_{g,\ell,\rho,\sigma,\tau,h,k}(t)
 =
 \sum_{P,Q,c,d}
 \overline{A_{P,c}(t)}B_{Q,d}(t)
 e_\ell(-hQd^2)e_\rho(kPc^2),
}
\tag{L-106120.5}
\]

where the sum is over all complete source atoms satisfying (L-106120.1)--
(L-106120.3), the declared shell, Boolean representation, marked-prime,
carrier and renewal conditions, and the fixed classes `(sigma,tau)`.

Both semiprime-owner sums and both reduced-core sums occur before a square is
taken.  Every literal coefficient `P^{-1/2}Q^{-1/2}c^{-1}d^{-1}g^{-2}` remains
inside the member.

## 3. Tensor Gauss transform

For an even character `eta` modulo `ell`, choose a root `chi` with
`chi^2=eta`; for an even character `theta` modulo `rho`, choose a root `psi`
with `psi^2=theta`.  Within fixed quadratic owner classes, changing either
root by the corresponding quadratic character changes the member only by the
constant scalar `sigma` or `tau`.

Let

\[
 \mathcal W_{\eta,\theta}(t)
 =
 \sum_{P,Q,c,d}
 \overline{A_{P,c}(t)}B_{Q,d}(t)
 \chi(Q)\eta(d)\psi(P)\theta(c)
\tag{L-106120.6}
\]

with the same source incidence.

Define

\[
 w_q(\mathbf1)={q+1\over q-1},
 \qquad
 w_q(\vartheta)={2q\over q-1}
 \quad(\vartheta\ne\mathbf1,\ \vartheta(-1)=1).
\tag{L-106120.7}
\]

Applying the one-prime Gauss identity successively in `h` and `k` gives

\[
\boxed{
 \sum_{h=1}^{\ell-1}
 \sum_{k=1}^{\rho-1}
 |\mathcal W_{h,k}(t)|^2
 =
 \sum_{\substack{\eta(-1)=1\\\theta(-1)=1}}
 w_\ell(\eta)w_\rho(\theta)
 |\mathcal W_{\eta,\theta}(t)|^2.
}
\tag{L-106120.8}
\]

Every term on the right is nonnegative.  It splits canonically into:

```text
principal--principal;
principal--nonprincipal;
nonprincipal--principal;
nonprincipal--nonprincipal.
```

## 4. Principal recombination

Termwise use of the two Ramanujan identities gives

\[
\boxed{
 \sum_{h=1}^{\ell-1}
 \sum_{k=1}^{\rho-1}
 \mathcal W_{h,k}(t)
 =\mathcal W_{0,0}(t).
}
\tag{L-106120.9}
\]

Thus the native unphased coprime two-sided current is the principal--principal
member of the complete tensor family.  There is no phase-cardinality loss and
no source fibre is squared separately.

## 5. Automatic two-sided long-core geometry

By construction,

\[
 \ell\le c,
 \qquad
 \rho\le d.
\]

On dyadic reduced-core blocks this places both phase conductors in their native
long-core ranges.  Parent `L-102958` additionally pays both complete opposite
semiprime owner products through physical ratio-eight comparability.  Hence no
local conductor/core or owner/core size obstruction survives in any of the
four tensor channels.

## Scope

This theorem proves the exact bilateral source partition, double nonzero phase
identity, complete amplification and tensor Gauss transform.  It does not
estimate the tensor moment.  The natural `g^2 ell rho` source-dual moment and
its diagonal are `L-106121`.
