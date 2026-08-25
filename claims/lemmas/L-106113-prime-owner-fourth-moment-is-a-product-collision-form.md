# L-106113 — The prime-owner fourth moment is an exact product-collision form

Claim ID: `L-106113`  
Programme aliases: `LFAM1.PRIME_PRODUCT_COLLISIONS`, `LFAM2.KUMMER_OWNER_FOURTH_MOMENT`, `STRESS.WICK_AMPLIFIER_TRACE_FORM`  
Status: **PROVED EXACT CHARACTER-ORTHOGONALITY NORMAL FORM; OFF-DIAGONAL COLLISIONS OPEN**  
Created: 2026-08-25  
Depends on: `L-106110--L-106112`; finite character orthogonality  
Programme issues: #743, #736, #737  
RH status: **not assumed**

Let `ell` be an odd prime and let `(x_p)` be an arbitrary finitely supported
complex sequence on primes not equal to `ell`.  Put

\[
 \mathcal P_\chi=\sum_p x_p\chi(p).
\]

The coefficients may contain any fixed Boolean-core, shell, common-core,
least-discrepancy, marked-prime or Mellin-frequency mask.  No factorization of
`x_p` is assumed.

## 1. Complete character fourth moment

Expanding and applying multiplicative orthogonality gives

\[
\boxed{
 {1\over\ell-1}
 \sum_{\chi\ ({\rm mod}\ \ell)}
 |\mathcal P_\chi|^4
 =
 \sum_{\substack{p_1,p_2,p_3,p_4\\
 p_1p_2\equiv p_3p_4\ ({\rm mod}\ \ell)}}
 x_{p_1}x_{p_2}
 \overline{x_{p_3}x_{p_4}}.
}
\tag{L-106113.1}
\]

This is a quadratic product-incidence Gram.  It is homogeneous of degree four
in the one-prime amplifier and degree two in the semiprime Wick square of
`L-106112`.

## 2. Even-character quotient

The even character group has order `(ell-1)/2`.  Its exact orthogonality is

\[
\boxed{
 {2\over\ell-1}
 \sum_{\substack{\eta\ ({\rm mod}\ \ell)\\\eta(-1)=1}}
 \eta(u)\overline{\eta(v)}
 =
 \mathbf1_{u\equiv v\ ({\rm mod}\ \ell)}
 +
 \mathbf1_{u\equiv-v\ ({\rm mod}\ \ell)}
}
\tag{L-106113.2}
\]

for nonzero residues `u,v`, with the two indicators disjoint unless
`ell=2`.  Therefore an even-character fourth moment is the exact union of the
two product-collision varieties

\[
 p_1p_2\equiv p_3p_4\pmod\ell,
 \qquad
 p_1p_2\equiv-p_3p_4\pmod\ell.
\tag{L-106113.3}
\]

In the Gauss frame of `L-106110`, the map `chi -> eta=chi^2` is two-to-one.
The two roots of each nonprincipal even character have equal Gauss weight, so
the nonprincipal owner-Wick contribution is equivalently a complete-character
collision form with the principal and quadratic root channels removed
explicitly.

## 3. Exact diagonal

The integer equal-product solutions

\[
 p_1p_2=p_3p_4
\]

are, up to the fixed labelled order and the two marked copies of `67`, the same
unordered owner pair.  Their contribution is part of the atomic/equal-product
ledger already paid by `L-106112`, parent `L-102747`, and the repeated-label
ledger.

Likewise the repeated-prime terms in which `p_1=p_2` or `p_3=p_4` are the
closed diagonal polynomial `mathcal D_{chi,d}` of `L-106112`.

Consequently only the strict congruence collisions

\[
\boxed{
 p_1p_2\equiv\pm p_3p_4\pmod\ell,
 \qquad
 p_1p_2\ne p_3p_4,
}
\tag{L-106113.4}
\]

remain in the nonprincipal fourth moment.

## 4. Principal versus family channels

The dual-amplified moment therefore has two genuinely different arithmetic
parts.

```text
principal/quadratic-root channel:
  an untwisted, incidence-masked fourth moment of the prime owner polynomial;

nonprincipal channel:
  the strict product-congruence form (L-106113.4), with the two root
  characters and the ell-rough Boolean tail retained.
```

A large-sieve or trace-formula proof of the second line does not automatically
bound the first.  Conversely, a principal cancellation theorem does not pay
the complete nonprincipal family.

## 5. Geometric target

Over a function field, (L-106113.4) is the fibre product of two Kummer
multiplication maps, together with the Artin--Schreier phase selected by the
least-discrepancy prime.  A geometric proof must separate:

```text
integer/equal-product diagonals;
quadratic-root constant constituents;
shared-owner and owner/core renewal strata;
genuinely geometrically nonconstant product-collision components.
```

The last components are the exact trace objects requested by
`FFDA106110` in `T-106110`.

## Scope

This lemma proves the exact fourth-moment/collision dictionary and closes its
literal diagonal.  It does not bound the strict congruence collisions or the
untwisted principal fourth moment.  Those are the live gates in `T-106110`.
