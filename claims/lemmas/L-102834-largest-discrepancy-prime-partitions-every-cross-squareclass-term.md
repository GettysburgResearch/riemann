# L-102834 — Every cross-squareclass term has one largest discrepancy prime

Claim ID: `L-102834`  
Status: **PROVED EXACT PRIME-OWNER PARTITION**  
Created: 2026-08-24  
Depends on: `L-102831--L-102833`  
RH status: **not assumed**

Let

\[
N=pq\,a^2,
\qquad
M=rs\,b^2
\]

be two completed largest-two products, with

\[
p>q>P^+(a),
\qquad
r>s>P^+(b),
\]

and suppose their owner pairs are different. Put

\[
\ell=\max\bigl(\{p,q\}\triangle\{r,s\}\bigr),
\]

using the fixed labelled order when the two copies of `67` occur.

Because the square cores have even valuation at every prime,

\[
\boxed{
v_\ell(N)-v_\ell(M)\equiv1\pmod2.
}
\tag{L-102834.1}

Thus `ell` belongs to exactly one squarefree owner pair and distinguishes the
two physical squareclasses. In particular `N!=M`.

## 1. Exact partition of the cross term

Every distinct-pair cross term is assigned to its unique largest discrepancy
prime. Therefore

\[
\boxed{
\mathcal C_{\rm cross}
=
\sum_\ell \mathcal C_\ell
}
\tag{L-102834.2}

coefficient-exactly, with no multiplicity or source fraction.

Inside `C_ell`:

```text
ell is unsquared in exactly one physical product;
all larger labelled primes have identical parity on the two products;
all square-core primes are invisible to the parity test;
the remaining differing owner labels are smaller than ell.
```

The sectors split further into:

```text
shared-owner pairs:
  the symmetric difference has two labels;

disjoint-owner pairs:
  the symmetric difference has four labels.
```

## 2. Arithmetic interface

The parity identity (L-102834.1) gives an exact quadratic-character and
prime-modulus interface for each cross term. It is the natural starting point
for a source-faithful dispersion or large-sieve estimate; no arbitrary owner
choice remains.

Define

```text
LDPC102834:
  the sum of the carrier-recombined largest-discrepancy-prime sectors has
  subpower logarithmic negative mass in the fixed ratio-eight observation.
```

Then

\[
\mathrm{LDPC}_{102834}
\Longrightarrow
\mathrm{L2SC}_{102833}
\Longrightarrow
\mathrm{DPWNC}_{102749}
\Longrightarrow
\mathrm{RH}.
\]

The theorem constructs the exact prime-indexed partition. It does not prove the
final dispersion estimate.