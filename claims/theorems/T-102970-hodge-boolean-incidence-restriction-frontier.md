# T-102970 — Hodge–Boolean two-sided incidence restriction frontier

Claim ID: `T-102970`  
Status: **MAJOR UNCONDITIONAL REDUCTION; RH UNPROVED**  
Created: 2026-08-25  
Depends on: `T-102950`, `L-102951--L-102956`; reviewed PR #751 packet  
RH status: **unproved**

The latest minimum-owner proposal and the critical Hodge quotient now fit into
one exact source chain.

## 1. Correct source

The unique harmonic midpoint square satisfies

\[
M(x)^2\equiv1-x\pmod{x^2}.
\]

Thus, modulo the already-closed squared/higher-prime-power gauge, the final
Hodge class is exactly the native squarefree Euler parity source.

## 2. Exact Boolean decomposition

The disjoint-support Boolean Vaughan identity is coefficient-exact. Owner
restriction commutes with Boolean convolution, so the balanced core coefficient
is universal on every allowed literal core.

The complete squarefree Type-I row is an `l1` square-shift transfer of the
zero-moment parent lattice and is power-saving.

## 3. New absolute core closures

Every nonzero Boolean balanced core exceeds `U^2`, with

\[
U\asymp Y^{1/6}.
\]

Therefore the equal-core packet and the entire one-sided reduced-core packet
have common square core

\[
g\gg Y^{1/3}
\]

and are absolutely `Y^(o(1))` by common-square extraction. They may be removed
before taking a negative part.

The surviving packet has

\[
c_1>1,
\qquad d_1>1,
\qquad(c_1,d_1)=1,
\]

and hence two distinct source-owned internal discrepancy primes.

## 4. Literal physical phase theorem

`L-102956` proves the centered one- and two-family phase-energy estimates
directly for arbitrary literal physical products. The owner multiplier inside
`n=P a^2` is no longer erased or assumed fixed.

Thus the analytic centered-divisor theorem and the core-length estimates are
available at the exact physical-product scope.

## 5. Exact remaining theorem

The only unresolved operation is the incidence relation between a source atom
and the prime modulus selected from that atom.

Define

```text
ICPR102970:
  in the coprime two-sided Boolean balanced packet, the source-incidence
  assignment of the two internal discrepancy primes to the physical centered
  phase transform has subpower norm/negative mass after all owner, carrier,
  gauge and renewal recombinations.
```

Equivalently, `ICPR102970` must show that the owner/core incidence masks may be
inserted into the physical-product kernel of `L-102956` without a power-sized
label-to-physical collapse and with every literal prime weight spent once.

Then

\[
\boxed{
\mathrm{ICPR}_{102970}
\Longrightarrow
\mathrm{OICP}_{102960}
\Longrightarrow
\mathrm{HMO}_{102940}
\Longrightarrow
\mathrm{RH}.
}
\]

## Disposition of the full proposal

```text
critical Hodge -> squarefree Euler source       PROVED EXACT / POLYLOG
Boolean Vaughan identity                        PROVED EXACT
owner-excluded coefficient universality         PROVED EXACT
Boolean Type-I global transport                 PROVED POWER-SAVING
equal-core Boolean packet                       PROVED ABSOLUTE SUBPOWER
one-sided reduced-core Boolean packet            PROVED ABSOLUTE SUBPOWER
physical-product centered phase theorem          PROVED EXACT
ICPR102970 incidence restriction                 OPEN / RH-BEARING
T-106080 complete composition                    UNPROVEN / GAP
Riemann Hypothesis                               UNPROVED
```

The open theorem is narrower than both the former short-core frontier and the
owner-indexed gate in the first disposition: it concerns only coprime,
two-sided, distinct-product incidence.
