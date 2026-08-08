# O-32301 — Radix two is the character-free critical scaling route

Claim ID: `O-32301`  
Status: **RESEARCH SYNTHESIS / EXACT CROSS-BRANCH CONSEQUENCE**  
Authoring agent: `gpt56-pro-xhigh`  
Created: 2026-08-08  
Dependencies: PR #323 residue-character firewall; PR #272 dyadic commutator; `R-32301`, `L-32302`--`L-32306`

## 1. Why the five-adic automaton is not merely finite combinatorics

PR #323 identifies the nonzero residue coordinates modulo a prime radix `p` with the finite character Fourier transform of Dirichlet-series cores

\[
{1\over L(s,\chi)}.
\]

For `p=5`, the four unit residues therefore contain:

```text
the principal zeta channel;
the quadratic mod-five L channel;
two conjugate complex mod-five L channels.
```

A norm-equivalent contraction of the complete unit-residue state is consequently GRH-strength for this finite character family.  The critical source cannot be removed by saying that the state space has only five residue classes.

## 2. Radix two has no nonprincipal unit character

The group

\[
(\mathbb Z/2\mathbb Z)^*
\]

is trivial.  Thus the dyadic block split introduces no independent Dirichlet-L channel beyond the principal inverse-zeta source.

This makes the dyadic commutator normal form of PR #272 structurally different from every odd-prime radix recurrence.

## 3. The remaining dyadic obstruction is explicit

PR #272 gives

\[
r_{2Y}
=2^{-1/2}\mathcal D_2r_Y
+w_{2Y}(2)\partial T_2
+\sum_a r_{2Y}(2a+1)\partial E_{2a}.
\]

The divisible-column part of Cycle Debt contracts by the exact factor `1/2`. The only same-stage obstruction is the source-complete pairing of:

```text
odd-column leakage of the lifted lower flow;
odd-node adjacent-tree commutator;
bottom charge.
```

`R-32301` shows that the square-root source mode is neutral before this pairing; it cannot be discarded.

## 4. Critical-null source as a legal dyadic high-pass

`L-32302` introduces

\[
\omega_\dagger
=(\varepsilon-\sqrt2\delta_2)*\omega_2.
\]

The normalized coefficient `sqrt(2)` is exactly the one for which the real square-root lower-scale mode cancels.  `L-32305` shows that its Riesz coordinate is the dyadic first difference of the old bottom-charge source.

This is a legitimate way to remove the **real neutral mode at the source level** because:

1. the finite numerator vanishes on the critical real exponent;
2. every off-line zeta zero remains a pole;
3. the omitted unit carry column is retained explicitly;
4. no nonprincipal character channel is introduced.

## 5. The five-mode paired frame keeps every other required structure

`L-32303/L-32304` enlarge the source to one filter which simultaneously has:

```text
positive inverse coefficients;
nonnegative generalized-prime coefficients;
uniform closed-strip parity frame;
positive paired Selberg forcing;
positive compact Green potential;
constant and affine carry-moment cancellation;
finite averaged carry bank through row 31;
bounded causal equivalence to the old PR #263 parity frame.
```

Thus the preferred global research object after the extra-high redo is not a residue quotient. It is the complete dyadic paired source with its critical real mode removed and every complex inverse-zeta mode retained.

## 6. Correct final research target

The remaining proof must act on the **same RH-sensitive coefficient sequence** on both sides of the exact PR #268 annular physical/carry isometry.  A valid theorem would bound that paired RH-sensitive carry Gram by:

```text
finite current bank n=2,...,31
+ complete strict-delay divisor family
+ complete odd-column dyadic commutator
+ tempered critical-line channel,
```

with total lower-scale charge strictly below the existing carry reserve.

This is narrower than generic BTP, five-adic GRH-strength contraction, or a source-free positive operator theorem.

## 7. Status

```text
five-adic source-free contraction      scope-corrected / arithmetic modes remain
radix-two character firewall           closed structurally
critical real-mode source filter       proposed complete exact
dyadic paired strip frame              proposed complete exact
finite averaged carry bank             proposed complete exact
source-specific strict recurrence      UNPROVEN
Riemann Hypothesis                      UNPROVEN
```
