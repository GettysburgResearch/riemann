# Independent audit of the minimum-owner Boolean Vaughan proposal

Date: 2026-08-25  
Reviewed PR: #751  
Frozen head: `8743ba4230097c296dee1dec40d09b59cdf56599`  
Review branch: PR #719  
RH status: **unproved**

## Executive verdict

The proposal identifies a real and useful new coordinate, but its submitted
proof does not yet establish the final physical owner-indexed restriction.

```text
Boolean squarefree source identity       VERIFIED
minimum-owner geometry                   VERIFIED
Boolean Type-I analytic transport        VERIFIED WITH REPAIR
same-family scalar centered kernel       VERIFIED
literal owner-indexed physical collapse  UNPROVEN / GAP
T-106080                                 UNPROVEN / GAP
RH                                        UNPROVED
```

The proposal is not refuted. Its first open arrow has been isolated and then
narrowed substantially.

## What survived and strengthened

1. The unique harmonic Hodge class on PR #719 is exactly the native squarefree
   Euler source modulo squared activity.
2. Owner exclusion commutes with Boolean convolution; the balanced core
   coefficient is universal on every allowed core.
3. The squarefree Type-I lattice is an `l1` square-shift transfer of the parent
   zero-moment lattice. The complete Type-I Hilbert/source transport is
   power-saving.
4. The minimum-owner rule is source-defined and proves `lambda^2<=a`.
5. Every balanced Boolean core exceeds `Y^(1/3)`.
6. Consequently the equal-core and one-sided reduced-core packets are
   absolutely subpower by common-square extraction.
7. Centered phase packing has been reproved directly for literal physical
   products; owner multipliers need not be erased.

## First remaining arrow

The two-sided coprime packet assigns its phase moduli from the source atom
itself. The parent scalar kernel theorem does not automatically commute with
this incidence mask and physical collapse.

The exact residual is:

```text
ICPR102970:
  source-incidence transport of the two literal internal discrepancy primes
  into the physical centered phase transform, with every prime/core/owner
  weight used exactly once.
```

Then

```text
ICPR102970
 -> OICP102960
 -> HMO102940
 -> fixed Mellin–Landau consumer
 -> RH.
```

## Why the gap is not merely wording

Keeping owner labels orthogonal deletes the physical cross-owner terms.
Collapsing first makes the additive phase depend on the complete physical
product rather than one common core sequence. A source-blind finite model has
labelled norm squared `N` and collapsed norm squared `N^2`.

This does not disprove the arithmetic restriction. It proves that the
restriction must use the literal incidence geometry rather than only the
same-family scalar identity.

## Best next attack

Use the Boolean two-sided coprime packet after `L-102955` and construct one
incidence-centered large-sieve operator on literal physical products. The
operator should combine:

```text
full internal-prime weights;
common-square extraction;
physical-product centered kernels from L-102956;
minimum-owner endpoint placement;
all-chaos recombination before the norm.
```

No further detector, owner rule or completion gauge is needed.
