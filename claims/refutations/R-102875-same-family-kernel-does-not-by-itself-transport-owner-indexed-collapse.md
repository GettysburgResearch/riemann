# R-102875 — The same-family centered kernel does not by itself transport owner-indexed physical collapse

Claim ID: `R-102875`  
Status: **PROVED COMPOSITION FIREWALL / ACTUAL ARITHMETIC CASE OPEN**  
Created: 2026-08-25  
Depends on: `L-102882--L-102883`; PR #751 `L-106081--L-106082`  
RH status: **not assumed**

The identity

\[
\sum_{\substack{\ell,\rho\in\mathcal P\\\ell\ne\rho}}
A_\ell(d)A_\rho(d)
=
K_{\mathcal P}(d)^2-
\sum_{\ell\in\mathcal P}A_\ell(d)^2
\]

is exact. It extends the scalar same-family centered kernel after deleting the
shared-prime diagonal. It does **not**, by itself, identify that scalar kernel
with the physical minimum-owner packet.

## 1. The two noncommuting operations

Let

\[
\mathcal H_{\rm lab}=\bigoplus_\lambda\mathcal H_\lambda
\]

be the owner-labelled Hilbert space and let

\[
J:\mathcal H_{\rm lab}\to\mathcal H_{\rm phys}
\]

be physical collapse. For a modulus `ell`, the nonzero phase operator is
diagonal on labelled source coordinates:

\[
D_{\ell,h}v_{P,a}
=e_\ell(hPa^2)v_{P,a}.
\]

There are two possible orders.

### Keep labels orthogonal

Applying the Hilbert-valued centered theorem before `J` controls

\[
\sum_\ell\sum_h\|D_{\ell,h}v\|_{\mathcal H_{\rm lab}}^2.
\]

But cross-owner physical inner products are absent from this orthogonal norm.
They are precisely the terms created by `J`.

### Collapse first

After applying `J`, the phase multiplier is no longer a scalar function of the
core alone. It depends on the owner product `P` through

\[
e_\ell(hPa^2).
\]

Therefore the scalar kernel in `L-106082.2`, which is written only in terms of
one common core difference, is not automatically the exact kernel of the
collapsed packet.

## 2. Source-blind finite firewall

Take

\[
\mathcal H_{\rm lab}=\mathbf C^N,
\qquad
v=\sum_{j=1}^Ne_j,
\]

and define physical collapse by

\[
J(e_j)=1.
\]

Then

\[
\|v\|_{\rm lab}^2=N,
\qquad
\|Jv\|_{\rm phys}^2=N^2.
\]

Any collection of diagonal unitary phase maps preserves the labelled norm, but
cannot bound this physical collapse with a source-independent constant.

This fixture does not refute the actual arithmetic packet. It proves the
logical firewall:

\[
\boxed{
\text{labelled centered phase energy}
\not\Longrightarrow
\text{owner-indexed physical restriction}
}
\]

without an additional source-specific theorem.

## 3. Exact missing theorem

The required statement is:

```text
OICP102960:
  on every minimum-owner Boolean block, the literal owner-indexed centered
  phase packet, including the selected-owner and co-owner weights, maps to the
  physical distinct-product observation with subpower norm/negative mass.
```

A proof must specify one common operator whose expansion contains the physical
cross-owner terms with their exact coefficients. It must also show that:

```text
selected owner weights are used once;
co-owner weights remain attached;
shared-owner and owner/core sectors are removed only by the frozen renewals;
all-chaos coefficients are recombined before the physical norm;
the moduli-dependent owner projections do not create a power-sized collapse.
```

## Disposition of PR #751

`L-106082.2` is verified as an algebraic identity. The implication

\[
\text{L-106082.2 plus }L^2<2B
\Longrightarrow
\text{L-106082.3--L-106082.5 for the literal owner packet}
\]

is not established by the submitted proof text. It may be true, but it is the
first unproved conclusion-bearing arrow.
