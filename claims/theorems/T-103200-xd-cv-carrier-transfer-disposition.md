# T-103200 — Exact disposition of the XD and CV proof attempts

Claim ID: `T-103200`  
Status: **UNCONDITIONAL HARDENING; XD, CV, RH UNPROVED**  
Created: 2026-08-20  
Base main: `677203992eb0168920365ee45ae9db76bfa97dcf`  
RH status: **unproved**

## XD

`R-103200` removes a mistyped implication edge: the frozen largest-prime and
Vaughan decompositions used different kernels.

`L-103201` proves the correct same-\(K_1\) hybrid.  Its two terminal forms are
equivalent modulo \(L^1(dX/X)\).

`L-103200` proves that every fixed notch leaves a deterministic regional prime
carrier.  `L-103202` gives the exact first-chaos quotient that must precede any
regional norm.

The correct open gate is

```text
CPXD103200:
  subpower logarithmic negative mass for the complete same-K1 terminal scalar,
  after exact carrier recombination and without a regional absolute value.
```

It remains RH-equivalent through the fixed compact-wavelet detector.

## CV

Corrected PR #684 proves positivity only for a finite completed packet after
including the noncompact inactive tail.  It withdraws the former standalone
large-prime collar positivity.

`L-103210` proves the exact moving-cutoff source transition.
`R-103210` proves that coefficient-budget variation cannot bound that
transition.
`L-103211` identifies the transition with the compact activation-wavelet
channel of PR #697.

The correct open gate is

```text
SCTV103210:
  subpower one-sided variation of the complete centered transfer/collar packet,
  including active, inactive, and moving-cutoff activation terms.
```

A uniformly subcritical two-channel matrix coupling `SCTV103210` to
`CPXD103200` would close through PR #697.  PR #698 supplies additional
deterministic sparsity×energy and regionwise-Schur hyperedges, but their
arithmetic premises remain open.

## Boundary

```text
same-K1 XD hybrid                         PROVED EXACT
fixed-notch carrier asymptotic            PROVED
first-chaos carrier quotient              PROVED EXACT
CPXD103200                                OPEN / RH-EQUIVALENT

moving completion source identity         PROVED EXACT
budget-BV shortcut                        REFUTED
transfer = activation-wavelet channel     PROVED EXACT
SCTV103210                                OPEN / RH-EQUIVALENT

Riemann Hypothesis                        UNPROVED
```
