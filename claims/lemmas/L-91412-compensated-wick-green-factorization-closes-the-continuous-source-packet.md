# L-91412 — Compensated Wick–Green factorization closes the continuous source packet

Claim ID: `L-91412`  
Status: **PROVED EXACT COMPENSATED FULL-PACKET FACTORIZATION; FINAL DOMINATION OPEN**  
Created: 2026-08-12  
Depends on: `L-91408`, `L-91409`, `L-91410`  
RH status: **unproved**

## 1. The missing issue in the continuous source

The prime measure of `L-91409` is supported on

\[
 u\ge\log2>\frac12,
\]

so its source maps require no Lévy compensation.  The positive continuous
part of the completed base measure is different:

\[
 d\mathfrak M_{\rm c}^+(u)
 =e^{-u/2}B(u)\mathbf1_{0<u<\kappa}du,
 \qquad
 B(u)=\frac1{1-e^{-2u}}-(1+e^u),
 \tag{L-91412.1}
\]

where

\[
 d\mathfrak M_{\rm c}^+(u)
 =\left(\frac1{2u}+O(1)\right)du
 \quad(u\downarrow0).
 \tag{L-91412.2}
\]

The uncentered endpoint vectors used in the prime Wick--Green identity are not
separately square integrable against this measure.  Their difference is
square integrable, because the two endpoints have the same no-jump trace.
The correct operation is therefore a compensated, rather than an uncentered,
Wick--Green split.

## 2. Abstract compensated two-vector identity

Let `H` be a complex Hilbert space, let `mu` be a positive measure on
`(0,infinity)`, and fix a compensation radius `h>0`.  Put

\[
 \chi(u)=\mathbf1_{0<u\le h}.
\]

For each label `i`, suppose strongly measurable vectors

\[
 U_i(u),V_i(u)\in H
\]

have a common no-jump trace `C_i in H`, and define

\[
 \widetilde U_i(u)=U_i(u)-\chi(u)C_i,
 \qquad
 \widetilde V_i(u)=V_i(u)-\chi(u)C_i.
 \tag{L-91412.3}
\]

Assume `tilde U_i,tilde V_i in L2(mu;H)` and that the Bochner vector

\[
 \boxed{
 J_i
 =\int_0^h
  \left(\widetilde U_i(u)+\widetilde V_i(u)\right)d\mu(u)
 }
 \tag{L-91412.4}
\]

exists in `H`.  Define the compensated cross kernel

\[
\boxed{
\begin{aligned}
 K_{ij}^{\rm comp}
 =-\int_0^\infty\Big[
 &\langle U_i(u),V_j(u)\rangle
 +\langle V_i(u),U_j(u)\rangle\\
 &-2\chi(u)\langle C_i,C_j\rangle
 \Big]d\mu(u).
\end{aligned}}
\tag{L-91412.5}

Then all terms below are finite and

\[
\boxed{
\begin{aligned}
 K_{ij}^{\rm comp}
 ={}&
 \left\langle
  \widetilde U_i-\widetilde V_i,
  \widetilde U_j-\widetilde V_j
 \right\rangle_{L^2(\mu;H)}\\
 &+\langle C_i-J_i,C_j-J_j\rangle_H\\
 &-\langle\widetilde U_i,\widetilde U_j\rangle_{L^2(\mu;H)}\\
 &-\langle\widetilde V_i,\widetilde V_j\rangle_{L^2(\mu;H)}\\
 &-\langle C_i,C_j\rangle_H
 -\langle J_i,J_j\rangle_H.
\end{aligned}}
\tag{L-91412.6}

Thus a compensated cross term is exactly

```text
two positive production Grams
minus four positive endpoint/connection Grams.
```

No indefinite metric is used.

## 3. Proof

Expanding `U=tilde U+chi C` and `V=tilde V+chi C`, the two copies of

\[
 \chi^2\langle C_i,C_j\rangle
\]

cancel the compensation in (L-91412.5).  The remaining short-jump terms are

\[
 -\langle C_i,J_j\rangle
 -\langle J_i,C_j\rangle.
\]

The ordinary polarized Wick identity gives

\[
\begin{aligned}
-&\langle\widetilde U_i,\widetilde V_j\rangle
 -\langle\widetilde V_i,\widetilde U_j\rangle\\
={}&
 \langle\widetilde U_i-\widetilde V_i,
        \widetilde U_j-\widetilde V_j\rangle
 -\langle\widetilde U_i,\widetilde U_j\rangle
 -\langle\widetilde V_i,\widetilde V_j\rangle,
\end{aligned}
\]

and the finite connection identity

\[
\boxed{
 -\langle C_i,J_j\rangle
 -\langle J_i,C_j\rangle
 =\langle C_i-J_i,C_j-J_j\rangle
  -\langle C_i,C_j\rangle
  -\langle J_i,J_j\rangle
 }
\tag{L-91412.7}
\]

finishes the proof.

## 4. Application to the short completed channel

For the causal source maps of `L-91408`, the two endpoint states satisfy

\[
 U_i(u)=C_i+O_H(u),
 \qquad
 V_i(u)=C_i+O_H(u)
 \quad(u\downarrow0).
 \tag{L-91412.8}
\]

The estimate follows directly from the finite exponential-polynomial mode
form and the relative-degree-three conditions

\[
 \psi_a(0)=\psi_a'(0)=0.
\]

Since `dM_c^+(u)~du/(2u)`, one has

\[
 \int_0^h
 \|U_i(u)-C_i\|^2d\mathfrak M_{\rm c}^+(u)<\infty,
\]

and likewise for `V_i`; moreover the Bochner integral (L-91412.4) converges.
Therefore (L-91412.6) gives an exact positive-metric factorization of every
pure-orientation short-jump completed block.

For mixed causal/anti-causal labels the zero-jump overlap vanishes, so

\[
 C_i=0
\]

and the identity reduces to the ordinary triangular Wick--Green factorization
of `L-91409`.

## 5. Delays and the bridge

A physical delay changes the no-jump trace `C_i` linearly and preserves the
`O(u)` expansion.  Hence arbitrary finite mixed-delay packets satisfy the same
identity with one common packet-level `C` and `J` map.

The bridge components have the same finite exponential-polynomial modes as the
causal and anti-causal mothers.  The removable zero of `Psi_a/u` gives the
same common-trace property and the same `O(u)` compensation.  Therefore all
bridge-to-carrier, bridge-to-delay, and bridge-to-opposite-orientation
continuous cross terms are included.

## 6. The long channel needs no compensation

The positive measure

\[
 d\mathfrak M^-(u)
 =-e^{-u/2}B(u)\mathbf1_{u>\kappa}du
 \tag{L-91412.9}
\]

is supported away from zero.  Its source vectors are individually square
integrable after the safe exponential tilts.  Taking `C=J=0` in
(L-91412.6) gives the ordinary identity

\[
 K^-=\operatorname{Gram}(D^-)
     -\operatorname{Gram}(U^-)
     -\operatorname{Gram}(V^-).
 \tag{L-91412.10}
\]

Because the completed signed measure is `M_plus-M_minus`, the long channel
enters with the opposite sign:

\[
 \boxed{
 -K^-
 =\operatorname{Gram}(U^-)
  +\operatorname{Gram}(V^-)
  -\operatorname{Gram}(D^-).
 }
 \tag{L-91412.11}
\]

This is a sharper port ledger than treating the entire long channel as one
undifferentiated negative source.  Its endpoint Grams are positive reserve;
only its jump-production port enters negatively.

## 7. Exact full continuous packet ledger

Let tildes denote the compensated short-channel maps.  On every finite
carrier/delay/orientation/bridge packet the complete continuous source block is

\[
\boxed{
\begin{aligned}
 K^{\rm cont}
={}&
 \operatorname{Gram}(\widetilde U^+-\widetilde V^+)
 +\operatorname{Gram}(C-J)\\
&+\operatorname{Gram}(U^-)
 +\operatorname{Gram}(V^-)\\
&-\operatorname{Gram}(\widetilde U^+)
 -\operatorname{Gram}(\widetilde V^+)\\
&-\operatorname{Gram}(C)
 -\operatorname{Gram}(J)
 -\operatorname{Gram}(D^-).
\end{aligned}}
\tag{L-91412.12}

Every displayed Gram is taken in an explicit positive Hilbert space.
Together with the prime packet of `L-91409`, this closes the full compensated
atomic-plus-continuous source factorization requested in `L-91410`.

## 8. The deterministic connection remains finite

The drift term

\[
 \mathfrak C_a^\lambda
\]

of `L-91410` is a finite carrier kernel obtained from the six safe pole jets.
Equation (L-91412.12) does not assign it an arbitrary positive norm.  It places
the two genuine compensation vectors `C` and `J` beside that deterministic
connection, so the remaining comparison is now a finite connection Schur
complement coupled to explicit production and endpoint ports.

## 9. Correct remaining domination

After adjoining the prime source, the negative side is no longer an opaque
continuous tail.  It consists of

```text
short-channel endpoint ports;
short compensation ports C and J;
long-channel jump-production D_minus;
prime endpoint ports;
the finite deterministic connection Schur complement.
```

The positive side consists of

```text
prime jump production;
short jump production;
short connection production C-J;
long endpoint ports;
delay leakage and reflected copies.
```

Proving coefficient-one domination between these two explicit ledgers is the
remaining RH-bearing theorem.

## 10. Exact boundary

```text
abstract compensated Wick-Green identity             EXACT
short singular continuous channel factorized         EXACT
long channel endpoint/production reversal             EXACT
all carriers and delays                               EXACT
both Hardy orientations                               EXACT
bridge continuous source placement                    EXACT
full atomic-plus-continuous packet source factorization EXACT
deterministic connection Schur complement             EXPLICIT
positive production >= negative ledger                OPEN / RH-BEARING
Riemann Hypothesis                                    UNPROVED
```
