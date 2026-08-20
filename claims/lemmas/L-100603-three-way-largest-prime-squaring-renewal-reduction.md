# L-100603 — Completion dilations are not divisor restrictions

Claim ID: `L-100603`  
Status: **WITHDRAWN AS STATED; EXACT TYPE FIREWALL PROVED**  
Depends on: corrected `L-100600`; PR #671 `L-99961`  
RH status: **unproved**

The former version of this file identified the finite-completion expansion with divisor-restricted native tails and then invoked PR #671's positive divisor renewal.  That identification is false.

## 1. The two operations

For a finite completion set `P_Z`, the forward completion is

\[
\mathscr C_Z f
=
\prod_{q\in P_Z}(I+q^{-1/2}S_q)f
=
\sum_{d\mid \prod_{q\in P_Z}q}
 d^{-1/2}S_df.
\tag{L-100603.1}
\]

Every term in (L-100603.1) is a **dilation** of the complete packet.

By contrast, PR #671 studies the divisor restriction

\[
B_d(z)=\sum_{m\ge1}\frac{\beta(dm)}{m^z}
=eta(d)B(z)G_d(z),
\tag{L-100603.2}
\]

whose coefficients select source integers divisible by `d` and reindex the quotient.  Dilation and restriction are different functors.

A one-prime coefficient test already separates them.  For `q!=67`,

\[
S_qB(z)=q^{-z}B(z),
\]

whereas

\[
B_q(z)=-B(z)(1-q^{-z})^{-1}.
\]

Their coefficient at the first quotient/source state has opposite type and they cannot be interchanged by a positive scalar.

## 2. Consequence for finite squaring

The exact forward identity of `L-100600` remains valid:

\[
(I+q^{-1/2}V_q)(I-q^{-1/2}V_q)=I-q^{-1}V_{q^2}.
\]

But expanding the completion does **not** create the hypotheses of (L-100603.2).  Therefore PR #671's positive renewal does not desquare the cofactor source, and the former packet `HDRB100603` is not an established reduction.

The honest comparison is still

\[
\text{native packet}
\xrightarrow{\text{positive finite completion}}
\text{squared packet},
\]

with no positive inverse.  Any use of divisor renewal requires a genuine independently proved divisibility indicator `1_(d|n)` in the physical source ledger.

## 3. Surviving result

Largest-prime ownership, the corrected cofactor-squaring identity, the square-root cutoff geometry, and the double-owner decomposition remain exact.  The claimed three-way largest-prime/squaring/renewal implication is withdrawn.
