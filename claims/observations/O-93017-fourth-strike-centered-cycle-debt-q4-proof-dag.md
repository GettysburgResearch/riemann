# O-93017 - Fourth-strike proof DAG for the centered Cycle-Debt and Q4 routes

Claim ID: `O-93017`  
Status: **ROUTE MAP / NO RH CLAIM**  
Created: 2026-08-15  
Depends on: PR #474 through `0a7e95a6d22f4bed9bbfa4e04b632b2c5827b53b`; PR #483 at `87bd7ad2127f98b6141b4c03355556f2b95f6404`; `L-93017`--`L-93019`; `T-93011`

## 1. Cycle-Debt route after carry-coordinate diagonalization

```text
critical carry target
    |
    v
triangular carry-coordinate basis
    |
    v
one-sided discrepancy LP
    N_X = max_{-W <= A psi <= 0} <ell_X,psi>
    |
    v
bottom-free dyadic recurrence
    N_(2Y) <= (1/2) N_Y + B_(2Y)
    |
    v
OPB: B_(2Y) <= polylog(Y)
    |
    v
polylog Cycle Debt
    |
    v
sharp prime ramp
    |
    v
Mellin-Landau pole exclusion
    |
    v
RH
```

Exact first open arrow:

\[
\boxed{
\mathfrak B_{2Y}\ll\log^A(2Y).
}
\]

`OPB` is the baseline-free form of the centered parity problem. It removes the
fixed \(K_X/2\) baseline, the absolute-value orientation, and the logarithmic
bottom payment from the controlling recurrence.

## 2. Q4 route after backward Hardy scalarization

```text
complete compact-Q4 source
    |
    v
one zero-safe endpoint mean M_circ(N)
    |
    v
backward Hardy inversion
    C_circ(N) reconstructed from future means
    |
    v
all complete endpoint rows R_N(j)
    |
    v
complete endpoint PIG
    |
    v
zero-safe Mellin pole exclusion
    |
    v
RH
```

Exact first open arrow:

\[
\boxed{
M_\circ(N)
\ll
\sqrt N\,\log^A N.
}
\]

The distinct-prime Gram and square-root-major-arc packet remains a useful
arithmetic coordinate for attacking this scalar, but it is not a second
logical gate once the global mean envelope is known.

## 3. Exact source-level bridge

Define

\[
A_4(s)
=
\frac{1-4^{1-s}}
     {(1-4^{-s})\zeta(s)}.
\]

Then

\[
\sum_n\frac{c_\circ(n)}{n^s}
=
(1-4^{1-s})\frac{A_4'(s)}{A_4(s)}.
\]

Thus

```text
scale-four zero-safe Mobius state
    |
    | logarithmic derivative
    v
complete compact-Q4 source.
```

Coefficientwise,

\[
c_\circ*a_4
=
-(\varepsilon-4\delta_4)*(a_4\log).
\]

This bridge is exact but not yet capacity-faithful. A future closing theorem
must transport the logarithmic-derivative relation without replacing signed
convolution by an unjustified positive map.

## 4. Interfaces stress-tested in this packet

```text
Cycle Debt:
  node potentials <-> carry coordinates          exact triangular
  centered dual <-> one-sided discrepancy        exact
  q=2 bottom term                                nonpositive
  dyadic inherited coefficient                   exactly 1/2
  upper certificate                              positive split multipliers
  source rationality                             not assumed

Q4:
  mean <-> prefix                                exact Hardy transform
  finite backward inversion                     exact with boundary
  infinite inversion                            requires C=o(N)
  compact-Q4 boundary                            removed by unconditional PNT
  mean -> all endpoint rows                      no Fourier estimate
  mean <-> PIG at RH scale                       exact growth transfer

Cross route:
  Q4 gauge                                       exact B_4 logarithmic derivative
  scale-four Mobius coefficients                 explicit
  zero safety                                    no open-strip cancellation
```

## 5. Current scientific boundary

```text
One-sided Parity Borrowing                       OPEN / RH-BEARING
Q4 zero-safe mean square-root bound              OPEN / RH-BEARING
capacity-faithful logarithmic-derivative bridge  OPEN
Riemann Hypothesis                               UNPROVEN
```

The two routes are now one finite discrepancy theorem and one scalar arithmetic
estimate. No factor-67 producer is imported.
