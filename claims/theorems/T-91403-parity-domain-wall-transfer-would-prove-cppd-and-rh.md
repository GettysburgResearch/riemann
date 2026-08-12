# T-91403 — A parity-domain-wall transfer would prove CPPD and RH

Claim ID: `T-91403`  
Status: **FULL CONDITIONAL RH PROPOSAL / EXPLICIT PARITY TRANSFER OPEN**  
Created: 2026-08-12  
Depends on: corrected `T-91008`; `L-91414`, `L-91415`, `R-91406`  
RH status: **unproved**

## 1. Exact reduced source identity

At one fixed safe scale `a>1/2`, the complete delayed two-sided-plus-bridge
screw/Weil Gram is

\[
 \mathbb K_a^{\rm del}
 =\mathcal C_a^\lambda
  +\mathcal P_a^{\rm par}
  -\mathcal N_a^{\rm par},
 \tag{T-91403.1}
\]

where the parity ledgers are the explicit Grams of `L-91414`.

The adverse map is

\[
 \mathcal A_a^{\rm adv}
 =E_{\rm p}
  \oplus\frac{C+J}{\sqrt2}
  \oplus O_-
  \oplus\mathcal A_a^{\rm ref,delay,bridge},
 \tag{T-91403.2}
\]

and the favourable production map is

\[
 \mathcal A_a^{\rm fav}
 =O_{\rm p}
  \oplus T_{\rm sh}
  \oplus\frac{C-J}{\sqrt2}
  \oplus E_-
  \oplus\mathcal A_a^{\rm ref,delay,bridge,+}.
 \tag{T-91403.3}

## 2. Parity-Domain-Wall Transfer (`PDWT_a`)

Construct explicitly a positive Hilbert connection space

\[
 \mathcal G_a
\]

and a contraction

\[
 \boxed{
 W_a:
 \overline{\operatorname{ran}\mathcal A_a^{\rm adv}}
 \longrightarrow
 \mathcal G_a\oplus
 \overline{\operatorname{ran}\mathcal A_a^{\rm fav}}
 }
 \tag{T-91403.4}
\]

such that

\[
 \boxed{
 W_a\mathcal A_a^{\rm adv}
 =G_a\oplus\mathcal A_a^{\rm fav},
 }
 \tag{T-91403.5}

where

\[
 G_a^*G_a=\mathcal C_a^\lambda
 \tag{T-91403.6}
\]

in the exact resident Guinand--Weil/Suzuki normalization.

The construction must be source ordered.  It may use:

```text
the safe prime Wick-Green spaces;
the direct short-jump translation source;
the long-jump mode spaces;
the six-safe-jet completed connection;
the compressed-delay Julia cocycle;
both Hardy reflections;
the bridge residue modes.
```

It may not define `G_a` by taking a square root of the unknown target screw
Gram.

## 3. Consequence

Contractivity gives

\[
 \mathcal N_a^{\rm par}
 \preceq
 \mathcal C_a^\lambda+
 \mathcal P_a^{\rm par}.
 \tag{T-91403.7}
\]

By (T-91403.1),

\[
 \mathbb K_a^{\rm del}\succeq0
 \tag{T-91403.8}
\]

on every finite packet.  The corrected fixed-scale delayed form-core theorem
then gives RH.

## 4. Why this route is promising

Compared with CPPD in its original endpoint ledger, `PDWT_a` has three
advantages.

1. It removes two redundant endpoint coordinates in every Wick--Green block.
2. It identifies the source sign as a parity domain wall rather than an
   arbitrary signed measure.
3. It exposes the canonical Cayley graph that the completed connection must
   regularize.

The one-node Cauchy vector diagonalizes this graph and automatically closes the
long adverse port; that specialization is pursued independently on the sibling
one-node branch.

## 5. Firewall

`R-91406` proves that no channelwise parity contraction can work.  The transfer
must use the completed connection and the endpoint channels jointly.  A proof
of only scalar diagonals, only the continuous channel, or only one Hardy
orientation is insufficient.

## 6. Exact boundary

```text
full parity source identity                         EXACT
canonical Cayley graph                              EXACT
one-node long-port domination                       EXACT
channelwise parity domination                       REFUTED
PDWT source-ordered joint contraction                OPEN / RH-EQUIVALENT
Riemann Hypothesis                                  UNPROVED
```