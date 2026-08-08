# M-23702 — Centered digital Hardy review protocol

Claim ID: `M-23702`  
Title: Fail-closed review protocol for the corrected fifth-aligned cumulative-shell proposal  
Status: **METHODOLOGY / REVIEW GATE**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08

## 1. Frozen dispositions

Before reviewing the live proposal, record these corrections.

```text
R-23706  uncentered subquadratic energy is false;
R-23707  centered little-o linear energy is too strong;
T-23704  superseded as a front-door theorem;
T-23705  current conditional theorem;
RH       unproved.
```

No later repair retroactively verifies either superseded energy condition.

## 2. Review order

1. `L-23709-cumulative-green-profile-and-fifth-aligned-forcing.md`
2. `R-23706-uncentered-cumulative-energy-condition-is-false.md`
3. `R-23707-centered-little-o-energy-is-too-strong.md`
4. `L-23715-centered-digital-forcing-is-bounded.md`
5. `L-23716-centered-digital-energy-descent.md`
6. `T-23705-centered-digital-hardy-proof-candidate.md`
7. PR #241 reflected coefficient algebra and two-frequency scope repair
8. PR #234 `L-23405`, with `2` replaced by `5`
9. `L-23710/X-23704` only as finite normalization checks
10. square-screw/other consumers only after the direct Landau chain is audited

## 3. Algebraic checks

A reviewer should reconstruct independently:

- the cumulative kernel `p(y)=4sqrt(y)-4-log y`;
- the transform
  \[
  \widehat C(z)=
  {(1-5^{-(z+1/2)})(z+1/2)
   \over z^2(z-1/2)\zeta(z+1/2)};
  \]
- the principal coefficient
  \[
  a_5=-(1-5^{-1/2})/\zeta(1/2)>0;
  \]
- the base-five digital series and the identity
  \[
  a_5\sum c_5(n)n^{-1/2}=\sqrt5-1;
  \]
- the bounded centered forcing;
- every endpoint in the centered Abel identity;
- the continuous-to-discrete energy orientation;
- the Hardy multiplier in `T-23705.6`.

## 4. Mandatory energy-scale mutations

The review must reject all three wrong scales:

1. no centering and `o(T^2)`;
2. derivative centering only and `o(T)`;
3. a bound that suppresses critical-line boundary poles or assumes simple zeros.

The accepted scale is

\[
\int_0^T|V(t)|^2dt=O(T),
\]

which permits arbitrary finite boundary-pole mass but excludes every interior exponential mode.

## 5. Reflected-Selberg production obligations

A claimed proof of `CDHB(5)` must emit:

```text
complete p=5 inverse coefficients a_5(n)=v_5(n)+1;
complete generalized primes Lambda_5#;
correct generalized-Lambda sign;
independent frequencies t and u before diagonalization;
full coefficient collision ledger;
rational-factor terms from s/(s-1);
anchor h(0) and every cross term;
a strict positive Schur/Hardy reserve;
a finite uniform constant independent of sigma;
no copy of the target Hardy energy on the forcing side.
```

The one-frequency global vertical identity is admissible only in its all-line scope. It may not be relabeled as a unit physical block.

## 6. Multiplicity firewall

The final bound must remain valid in the presence of multiple critical-line zeros. Any step that turns a boundary pole of order greater than one into a uniformly simple pole has inserted an undeclared simplicity hypothesis.

If the proposed `O(T)` energy itself implies simplicity, that stronger consequence must be stated explicitly and proved compatible with the actual reflected reserve. It cannot be hidden in the norm estimate.

## 7. Landau audit

The conditional deduction uses eventual positivity, not positivity on every finite interval. Verify that:

1. `CDHB(5)` gives `Z(y)>=-O(sqrt(log y))`;
2. `a_5>0` gives eventual positivity of `C`;
3. removing a compact initial segment changes the Mellin transform by an entire function;
4. no positive real singularity remains;
5. every off-line zero creates an uncancelled pole;
6. functional-equation symmetry completes RH.

## 8. Automatic rejection conditions

Reject the full proposal if any one of the following occurs:

- wrong half-shift or Euler factor;
- incorrect principal-part subtraction;
- unbounded centered digital forcing;
- missing endpoint charge;
- wrong energy scale;
- one-frequency/one-block conflation;
- scalar analytic square in place of a Hermitian square;
- target energy returned unchanged to the right-hand side;
- implicit simple-zero assumption;
- finite computation promoted to `CDHB(5)`;
- use of RH, Mertens square-root cancellation, or a zero-free critical strip in the proof of the Hardy bound.

## 9. Status boundary

```text
finite and transform algebra          proposed exact
centered digital forcing              proposed complete
centered descent                      proposed complete conditional
CDHB(5)                               open
CDHB(5) -> RH                         proposed complete
Riemann Hypothesis                    unproved
```
