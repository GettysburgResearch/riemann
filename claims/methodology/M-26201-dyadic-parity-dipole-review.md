# M-26201 — Adversarial review protocol for the dyadic parity-dipole proposal

Claim ID: `M-26201`  
Title: Reconstruct the complete opposite-parity source, Hall dual, and reflected reserve before reviewing the RH composition  
Status: **PROPOSED REVIEW PROTOCOL**  
Authoring agent: `gpt56-pro-source-specific`  
Created: 2026-08-08  
Dependencies: `L-26201`--`L-26203`, `T-26201`; PRs #241, #248, #254, #257  
Scope: fail-closed review of one source-specific proposal

## 1. Freeze the exact inputs

Record the current head SHA of every imported source:

```text
PR #257 live proof graph
PR #254 signed carry dipole
PR #248 elementary carry/Green stack
PR #244 greedy slack and Möbius adjoint
PR #241 two-frequency reflected block
PR #236 dyadic shell and binary-digit source
```

Do not replace a frozen failure by a later repair without opening a new claim.

## 2. Replay the exact finite algebra

Run

```bash
python experiments/X-26201-dyadic-parity-dipole/verify.py
```

and require

```text
EXACT_DYADIC_PARITY_DIPOLE_ALGEBRA_VERIFIED
```

The checker must independently verify:

1. the affine Möbius carry row;
2. all four `2`-adic source layers;
3. compact support in `[m,4m)`;
4. the positive/negative band signs;
5. the positive inverse convolution;
6. the binary-digit three-atom output;
7. stable shell inversion;
8. exact positive-block incidence transport;
9. all mutation failures.

This verifies finite algebra only.

## 3. Reconstruct the source at two representations

For a small production level and one symbolic level, emit:

### Dirichlet representation

```text
omega_2 coefficients
a_2^star coefficients
Lambda_2^star coefficients
c_2 digital dual
```

### Carry representation

```text
complete beta rows
Mobius contraction
dyadic sibling recombination
inner [m,2m) band
outer [2m,4m) band
```

The two representations must agree exactly.  An omitted sibling or an
absolute-value substitution must break both the compact dipole and the digital
output.

## 4. Prime-only residual ledger

For each retained `X`, emit directed or exact enclosures for

```text
d_X(p)=v_p(b_X^(0))-p^(-1/2)log(X/p)
d_X^+(p)
d_X^-(p)
```

for every prime `p<=X`.

Bind the prime list and every repeated transcendental evaluation.  Do not
independently widen the same residual in the primal and dual consumers.

## 5. Primal transport replay

A certificate must verify exactly:

```text
1<=A<B<=X
t>=0
complete factorizations of A,B
all prime incidences
b_X^star>=0
all repaired prime constraints
objective change=sum t log(B/A)>=0
```

The checker may consume directed logarithm intervals, but the incidence algebra
must be exact.

## 6. Hall dual replay

If the proposal is reviewed through the dual, emit exact nonnegative
`alpha,beta` and verify every licensed block inequality

\[
 \sum_{p\mid A}\alpha_p
 \le
 \sum_{p\mid B}\beta_p.
\]

Then contract the same weights against the complete defect and slack vectors.

A dual witness is not permitted to omit a licensed block or to use a block not
present in the source grammar.

## 7. Two-frequency reflected block

Reconstruct PR #241 `L-9518` with independent variables `t,s`.  Insert the
complete `omega_2` source before any band split.

The proof object must expose:

```text
inner source vector
outer source vector
all inner-inner terms
all outer-outer terms
all inner-outer terms
block kernel Phi_(J,alpha)(t-s)
normal-Gram orientation
```

Reject any replacement by the global diagonal `t=s` integral.

## 8. Digital endpoint ledger

Replay

\[
 c_2*\omega_2
 =
 \varepsilon-\frac52\delta_2+\delta_4
\]

and the additive three-tap identity.  Every boundary term in the proposed RDH
identity must map to one of these atoms or to a separately declared outer
parabolic term.

The binary digit partial sums may be used only through a written Abel
summation with all endpoint signs displayed.

## 9. Load-bearing identity

The review target is the exact source formula

\[
 \sum_p d_X^-(p)\beta_p
 -
 \sum_p d_X^+(p)\alpha_p
 =
 \mathfrak R_X+\mathfrak D_X+\mathfrak O_X.
\]

Return one of:

```text
VERIFIED_REFLECTED_DYADIC_HALL
VERIFIED_WITH_NORMALIZATION_FIXES
GAP_MISSING_HALL_BLOCK_SOURCE_MAP
GAP_DIGITAL_ENDPOINT_SIGN
REJECTED_OMITTED_REFLECTED_CROSS_TERM
REJECTED_OUTER_RESERVE_SIGN
```

A proposed repair is a new theorem; it does not retroactively verify
`T-26201`.

## 10. Mandatory mutations

The following must fail:

1. `mu -> |mu|`;
2. delete the `4`-dilate sibling;
3. replace `-3/2` by `-1`;
4. drop one inner/outer reflected cross term;
5. replace the physical block by the diagonal vertical integral;
6. omit a prime from a transport block factorization;
7. allow `A>=B`;
8. independently widen a shared residual;
9. route a higher prime power without the prime-only error budget;
10. remove the first fixed-ratio Mertens shell.

## 11. Scope boundary

Successful finite transport computations are evidence for the source grammar,
not a proof of RDH.  Conversely, failure of one greedy producer does not refute
existence of a transport certificate.

The proposal is accepted only through the symbolic source identity and its
cofinal arithmetic bounds.
