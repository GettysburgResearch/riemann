# QPTI proof attempt: Euler–Beta owner–core dispersion

Date: 2026-08-26  
PR: #719  
Starting head: `426fe1c34a35d21b38a393456a7071c0902170f1`  
Cross-check heads: PR #730 `b3114562acbeb8c5890ef7a5fc59eed8db71d29a`; PR #751 `98af0db6ec7f77d6333a77a3dac53c4698852f43`; PR #756 `6e4609dfe1b073f1eb58445fdd1d7164dbc450d6`  
RH status: **unproved**

## Executive disposition

I did not obtain a valid proof of `QPTI103112`.

The pass did produce a stronger exact reconstruction.  The adaptive
quarter-power Type-I packets can be removed completely from the final
arithmetic formula.  QPTI is the one-sided bounded observation of one explicit
Euler–Beta owner–core transform.  The canonical Beta coefficient does not
cancel the owner mode; cancellation has to occur between different
Möbius-signed core layers or through an exactly equivalent connected family
construction.

```text
quarter-power support annihilation        retained exact
fixed-owner Type-I endpoint               retained subpower
complete Euler-Beta transform             proved exact
fixed live-core owner mode                proved nonzero
fibrewise/Tonelli closure                 ruled out
cross-core signed dispersion              open / RH-bearing
QPTI103112                                open / RH-bearing
RH                                        unproved
```

## 1. Exact reconstruction

For the canonical equal-pair physical source, one owner pair and one literal
square core have the form

\[
N=pq c^2,
\qquad
{\mu(c)\over\binom{\omega(c)+2}{2}\sqrt{pq}\,c}.
\]

Writing `z_p(s)=p^(-s-1/2)`, the finite-horizon Mellin polynomial is

\[
\mathscr E(s)
=
\sum_{p<q}\sum_{(c,pq)=1}
{\mu(c)\over\binom{\omega(c)+2}{2}}
 z_pz_q\prod_{r\mid c}z_r^2.
\]

The exact Beta identity gives

\[
\mathscr E(s)
=
\int_0^1(1-\theta)P_\theta(s)
\bigl(A_\theta(s)^2-B_\theta(s)\bigr)d\theta.
\]

This is also the second owner derivative at `u=0` of

\[
\prod_p(1+u z_p-\theta z_p^2).
\]

The subtraction `B_theta` is the exact distinct-owner/Wick diagonal removal.
No random-family, asymptotic Euler product, or source-blind square is used.

The corrected direct detector symbol is

\[
\widehat K_L(s)
=
{4(s-1)(1-2^{-s})^2(1-\sqrt2\,2^{-s})
 \over s(s-1/2)}.
\]

Thus the direct QPTI current is the inverse Mellin transform of
`Khat_L E_live`.  This avoids the historical common-mother multiplier identity
corrected on PR #730.

## 2. Why the hoped-for Beta cancellation fails

For a fixed squarefree core `c`, the owner contribution is

\[
{\mu(c)\over\binom{\omega(c)+2}{2}}
\left(\prod_{r\mid c}z_r^2\right)
\sum_{p<q,(pq,c)=1}z_pz_q.
\]

For real `s>1/2`, the owner polynomial is strictly positive.  A two-prime core
is already beyond root and first chaos and retains a positive owner mode.
The Beta integral reproduces the same coefficient exactly.

Therefore the following attempted proof is invalid:

```text
fixed-owner zero-moment bound
  -> take absolute values
  -> sum owner pairs using Beta normalization
  -> QPTI.
```

The pair normalization divides one labelled occurrence among its legal pairs;
it does not normalize the number of distinct occurrences or physical owner
products.

## 3. Other proof mechanisms tested

### Reflection/common-mother positivity

The exact half-source square and reflection mismatch remain valuable, but PR
#730 corrected the direct observation bridge.  The reflection coordinate
requires the stable dyadic/differential resolvent and still leaves the
RH-bearing positive variation gate.  No positivity of an ordinary modulus
square transfers to the Boolean analytic square.

### Incidence-masked phase packing

`L-102959` accepts the complete quarter-power incidence mask.  Its bound still
contains source-specific `M_1,M_2` terms.  Beta normalization does not prove
those terms subpower, so this does not close the owner sum.

### L-family averaging

PR #756 gives the correct physical-squareclass architecture, but its current
family theorems stop before the varying-core Wick-centered estimate and before
principal-member individualization.  A family average cannot be inserted as a
proof of the principal zeta row.

### Absolute owner/core summation

Absolute values erase the only remaining signs, `mu(c)`.  The fixed-core owner
polynomial is nonzero and grows with the owner box.  Thus an absolute or
source-blind estimate cannot reach the conclusion-facing scale.

## 4. Sharp next theorem

The exact remaining target is `EBD103120`:

```text
retain the full physical products p*q*c^2;
retain mu(c) through owner summation and all phase/Wick recombinations;
prove subpower logarithmic negative mass for the resulting bounded K_L row.
```

Two routes remain credible:

1. a direct bilinear dispersion in which different owner fibres and different
   core layers are correlated before an absolute value;
2. a connected Kummer/character family that retains the varying-core signs,
   followed by a subpower-loss amplifier, exact inversion, or rigidity theorem
   isolating the principal member.

Anything that estimates each owner fibre separately has already discarded the
needed cancellation.

## Scientific status

`L-103120`, `R-103120`, and `T-103120` are exact and useful reductions.  They
are not a proof of QPTI.  The replay checks finite Boolean/Beta algebra and
explicitly records `qpti_proved=false` and `rh_established=false`.
