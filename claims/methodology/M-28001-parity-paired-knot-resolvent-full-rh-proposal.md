# M-28001 — Parity-paired knot-resolvent attack on RH

Claim ID: `M-28001`  
Title: Contract the smooth eta bulk and the reciprocal-knot Möbius source in one parity-paired reflected energy  
Status: **FULL CONDITIONAL PROPOSAL / ONE SOURCE-SPECIFIC BOUNDARY RECURRENCE OPEN**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Frozen parent: PR #280 at `6a2195f4c173dfc3db1ac42596dce58706062b28`  
Imported interfaces: PR #241 independent-frequency block; PR #263 parity-paired positive Bezout reconstruction; PR #269 factor-five source localization; PR #272 Pascal-cycle debt  
RH status: **not proved**

## 1. Why a new proposal is needed

`R-28001` gives exact counterexamples to both proposed smooth fixes:

```text
all-stage continuum central positivity      false;
fixed third-Abel producer positivity         false.
```

`L-28001` explains why. The full central resolvent has multiplier

\[
1/\eta(s)=1/[(1-2^{1-s})\zeta(s)],
\]

so the cascade contains the signed odd-Möbius source. The boundary knots are not lower-order decoration; they are the RH-bearing channel.

The exact two-pass positive packing remains valuable and should be retained. What must be replaced is the claim that the later stages are a smooth contraction plus a harmless scalar commutator.

## 2. Correct decomposition

For every logarithmic block, decompose the central cascade output as

\[
\boxed{
\mathcal C_J
=
\mathcal C_J^{\mathrm{bulk}}
+
\mathcal C_J^{\partial}.
}
\tag{M-28001.1}

The first term is the open-cell dilation contribution. At the critical mass coordinate it contracts by

\[
\rho=1-\log2<1.
\]

The second term is the complete reciprocal-knot ledger, including:

```text
all endpoint distributions;
all dyadic valuation siblings;
the odd-Möbius coefficient a_eta(n);
every finite-support transition;
the fixed-ratio 2/3 Mertens mutation.
```

This split must be made before norms, positive parts, or rowwise absolute values.

## 3. Parity pairing

The single eta channel is signed. Import the exact parity analysis pair from PR #263. Its two finite Euler fibers satisfy:

1. a uniform nonvanishing frame on the closed counterexample annulus;
2. a coefficientwise-positive finite Bezout reconstruction of the reciprocal-zeta source;
3. a finite synthesis to the opposite-parity source `omega_2`;
4. retention of every off-line zeta pole before any carry window introduces a zeta factor.

Apply the pair to the complete decomposition (M-28001.1), not just to the smooth bulk. This gives two physical source channels

\[
\mathcal C_{J,+},
\qquad
\mathcal C_{J,-},
\]

whose reflected two-frequency energy is positive and phase complete.

## 4. Factor-five localization of the knot source

PR #269 proves for the complete opposite-parity carry wavelet that every potentially negative logarithmic Kummer interaction lies in

\[
2m\le n<5m.
\]

Thus the infinite reciprocal-knot ledger has a finite transition grammar:

```text
quotient cell 2;
quotient cell 3;
quotient cell 4;
finite n<210 boundary;
all translate and parity cross terms.
```

The far quotient tail is positive in carry coordinates. The smooth central bulk supplies the strict mass contraction; the finite transition block is where the physical source reserve must be proved.

## 5. Sole load-bearing theorem — `PKRC`

A **Parity-paired Knot-Resolvent Contraction** certificate must emit, for every sufficiently large logarithmic block `J`, the complete independent-frequency source matrix and prove

\[
\boxed{
\kappa E_\partial(J)+Q_J
\le
C(1+J)^A
+
\sum_{r=1}^{R}\theta_r E_\partial(J-r),
}
\tag{M-28001.2}

with

\[
Q_J\ge0,
\qquad
\kappa>0,
\qquad
\theta_r\ge0,
\qquad
\sum_r\theta_r<\kappa.
\tag{M-28001.3}

Here `E_partial(J)` is the reflected physical energy of the complete reciprocal-knot source after the finite parity/Bezout synthesis, with no carry zeta factor applied to the boundary line.

The certificate must also prove the coupled bulk estimate

\[
E_{\mathrm{bulk}}(J)
\le
\rho E_{\mathrm{bulk}}(J-1)
+C E_\partial(J)+C(1+J)^A.
\tag{M-28001.4}

Equations (M-28001.2)--(M-28001.4) give polynomial block energy by a finite-dimensional renewal argument.

## 6. Required production ledger

A valid `PKRC` artifact must contain:

```text
both parity physical channels;
positive Bezout synthesis coefficients;
the full odd-Mobius eta-resolvent coefficient;
all reciprocal-knot distributions;
independent reflected frequencies;
all four translate cross terms;
quotient cells 2,3,4;
finite n<210 table;
all endpoint and cutoff rows;
the m=1 boundary source;
bottom charges 2 and 3;
the exact 2/3 Mertens mutation;
strict reserve and lower-block charge totals.
```

It must reject the three mutations from `R-28001`.

## 7. Completion to RH

Under `PKRC`, the parity-paired reciprocal-zeta source has polynomial block energy. Finite synthesis and the causal all-ratio filters then give subexponential energy for one safe Möbius shell. Its Laplace transform contains

\[
\frac{P(s)}{\zeta(s)}
\]

where the finite Euler polynomial `P` has no zero in the open critical strip.

A hypothetical zeta zero with real part greater than `1/2` would create an uncancelled pole and exponential block-energy growth. Polynomial energy excludes it. Functional-equation symmetry gives RH.

Thus

\[
\boxed{
\mathrm{PKRC}
\Longrightarrow
\text{subexponential safe-shell energy}
\Longrightarrow
\mathrm{RH}.
}
\tag{M-28001.5}

The implication is conditional; `PKRC` is not proved here.

## 8. Relation to the live proposals

This proposal consolidates rather than duplicates:

- PR #280's exact central residual and two-pass packing;
- PR #263's parity frame and positive Bezout reconstruction;
- PR #269's factor-five carry localization and source reserve;
- PR #241's correct independent-frequency physical block;
- PR #272's cycle-debt repair language.

It also sharpens their common boundary:

```text
smooth central contraction alone           insufficient;
fixed Abel-prefix positivity               false;
pure carry-window physical coercivity      pole-canceling;
parity-paired physical knot recurrence      honest remaining theorem.
```

## 9. Automatic rejection

Reject an asserted completion if it:

1. drops the reciprocal-knot distributions;
2. quotes `D T=T D` across the stopped boundary;
3. uses the false third-Abel positivity;
4. applies a carry window before retaining the physical pole channel;
5. omits a parity or translate cross term;
6. takes absolute values before odd-core recombination;
7. loses the bottom charge or `2/3` shell;
8. has total lower-block charge at least the strict reserve;
9. promotes a finite matrix ladder to the cofinal theorem.

## 10. Exact status

```text
central residual and two-pass packing          retained / proposed complete
all-stage smooth continuum positivity          refuted
fixed third-Abel repair                         refuted
central eta-resolvent identity                  proposed complete exact
parity/Bezout/factor-five imports               proposed complete at stated scopes
PKRC physical knot recurrence                   open / RH-bearing
PKRC -> RH                                      complete conditional composition
Riemann Hypothesis                              unproved
```

The branch is appropriate for adversarial review as a corrected full-problem proposal, not as an unconditional proof.