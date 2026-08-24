# Scale-matched root-residue occupancy closure

Date: 2026-08-25  
Execution PR: #751  
Programme issues: #743, #736, #737  
Arithmetic parent: PR #719 at `ae61d988568fdc3e7d790a42b5c340c29a6ea3e5`  
Continuation base: PR #751 at `74916ff37b98574e17e6f979453879c472f8b596`  
Status: **full proof proposal; hostile review pending**

## 1. The obstruction

`T-106060` reduced the live CV/XD arithmetic problem to same-root-residue
occupancy.  Its exact two-phase frame gave

\[
\|S_{\mathfrak a}\|^2
<\ell D_{\mathfrak a},
\]

so the unresolved question was whether the principal-character factor
\(\ell\) could be paid without duplicating source or spending the owner weights
twice.

## 2. The new block-local mechanism

On one stopped-Vaughan block

\[
u\sim U,\qquad v\sim V,\qquad m\sim M,\qquad B=UVM,
\]

every core satisfies \(B\le uvm<8B\).  Four disjoint Bertrand intervals
supply four candidate primes; after discarding `67`, three remain with

\[
16B<\ell_j<256B.
\]

A semiprime owner product contains at most two palette primes.  Colour the
linear source by the subset it contains and select the first absent palette
prime.  Every occurrence in the colour is then coprime to its modulus, and the
principal character is literally the native coloured block.

The construction is linear and nonduplicating.  It does not choose a modulus
from an already-expanded owner pair.

## 3. Root residues become actual cores

For two owners \(P,Q\), character orthogonality gives

\[
P c^2\equiv Qd^2\pmod\ell.
\]

A nonsquare owner ratio vanishes.  A square ratio gives

\[
c\equiv\pm\tau d\pmod\ell.
\]

Because both cores lie in \([B,8B)\) and \(\ell>16B\), each line is a partial
matching.  After aggregating the subpower number of representations of one
physical core,

\[
D_{P,Q,\pm}
\ll E_{P,B}E_{Q,B}.
\]

## 4. Exact conductor payment

The load-bearing coefficient estimate is the sharp block form

\[
E_{P,B}
\ll\frac{X^{o(1)}}{P B}.
\]

It must not be weakened to \(X^{o(1)}/P\) before the conductor is paid.  The
matching bound gives

\[
D_{P,Q,+}+D_{P,Q,-}
\ll\frac{X^{o(1)}}{P Q B^2}.
\]

Therefore

\[
\ell\sum_{P,Q,\pm}D_{P,Q,\pm}
\ll
\frac{X^{o(1)}}B
\left(\sum_P\frac1P\right)^2
=X^{o(1)}.
\]

The power-scale modulus is cancelled exactly by the retained \(B^{-1}\)
energy.  All block, colour, line, marked-prime, carrier and gcd labels cost
only subpower.

## 5. Native-source composition

On every coloured block:

```text
principal character = native block;
equal products       = parent subpower theorem;
nonsquare ratios      = zero;
square ratios         = two injective lines;
two-phase line norm   < ell * root occupancy;
weighted occupancy    = subpower.
```

Thus the full character norm and the native block norm are subpower.  Cauchy
across only the polylogarithmic linear block/colour partition gives

\[
\int_X^{2X}|R_{\rm HBC}(t)|^2\frac{dt}{t}=X^{o(1)}
\]

and hence subpower logarithmic negative mass.  This closes
`HBCQDSP102888` in the proof packet.

The parent then adds the power-small Type-I row, applies the positive Volterra
transport from the derivative detector, and invokes the fixed Mellin--Landau
consumer.  `T-106070` therefore states the full proof proposal

\[
\mathrm{SMCROP}_{106070}
\Longrightarrow
\mathrm{HBCQDSP}_{102888}
\Longrightarrow
\mathrm{RH}.
\]

## 6. Publication and review posture

The proposal is intentionally left in a draft PR.  It makes the full
mathematical claim, but canonical project status is not changed before a
hostile source-and-normalization review.  `M-106070` requires a reviewer to
identify a first false equation or unsupported uniformity if rejecting the
argument; the historical fact that RH is open is not itself a review.

## 7. Exact replay

```text
PASS_X_106070_SCALE_MATCHED_ROOT_OCCUPANCY
checks=166834
sha256=67e946c4710d492cae450d7a2581f72e81ab7d8b72c11f5871ad24121212748b
```

The replay checks finite palette, colour, matching, representation, occupancy,
conductor-payment, harmonic and compact-support algebra.  It does not prove the
cited analytic divisor estimates, the Mellin consumer or RH.