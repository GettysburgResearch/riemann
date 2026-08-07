# Quartic target ladder and the readout body/tail breakthrough

Agent: `gpt56-04-f`  
Date: 2026-08-01  
Issue: #176  
PR: #158

## Executive result

The requested coupled readout schedule can be constructed explicitly, but it
controls only finite-readout compression tails.  It cannot prove
`||C_(M,N)||_4 -> 0` unless the complete window-level central-jet body
`||C_M||_4` already tends to zero.  Likewise, finite readout completeness
cannot prove the raw scalar/cyclic pullback; it transfers a complete-window
identity to finite readouts.

This is an exact body/tail theorem, not a failure to choose `N(M)` aggressively
enough.

The independent directed completed-zeta quartic target is now retained as

```text
tau4 in
[0.00007434028042155903583783846060250156947306763135396599249702198862838833,
 0.00007435011671954168375079742480823382176135706727491864190486602389042017].
```

The first operator row cannot yet be produced because the source manuscript
does not commit finite matrices or a numerical producer for the complete raw
and renormalized comparison maps.

## Main theorem

If the seam regularizer has spectral exponent `a>1/4` and reference eigenvalues
`lambda_n >= c_Sigma n`, then the readout tail obeys

```text
||C_M-C_(M,N)||_4 <= beta_M N^(1/4-a).
```

Choosing

```text
N(M)=ceil((2^M beta_M)^(1/(a-1/4)))
```

makes every retained readout tail at most `2^-M`.

But

```text
| ||C_(M,N)||_4-||C_M||_4 | <= ||C_M-C_(M,N)||_4,
```

so along this schedule

```text
||C_(M,N(M))||_4 -> 0  iff  ||C_M||_4 -> 0.
```

For the raw pullback, after defining the complete-window body error

```text
rho_M^body(r)=sup_|w|<=r |g_M^lin(w)-g_(A,M)(w)|,
```

one similarly has

```text
|rho_(M,N)(r)-rho_M^body(r)|
 <= ((1-Cr)^(-2)-1) ||A_M-A_(M,N)||_2.
```

Thus `rho_(M,N(M))->0` is equivalent to the complete-window body theorem once
the explicit readout tail tends to zero.

## Central quartic jet

The order-four source input is the fixed local jet

```text
(1/6) J_M^cen(chi_M u^2).
```

For nested windows whose cutoffs equal one near the center, this source jet is
eventually constant under compatible finite-jet coordinates.  Its image under
the full retained singular-seam comparison chain is

```text
c_(4,M)=
 (1/6) J_R R_(boundary,R,M)^fp epsilon_M^fp
       iota_M^cen P_M^cen J_M^cen(chi_M u^2).
```

The necessary first body gate is `||c_(4,M)|| -> 0`.  A directed lower bound
away from zero rules out the entire Schatten-small finite-jet strategy,
regardless of readout growth.

## Production status

Completed:

1. explicit `N(M)` compression-tail schedule;
2. exact body/tail equivalences for both requested limits;
3. quartic realized-jet gate;
4. independent directed interval for `tau4`;
5. fail-closed ladder schema and checker.

Missing:

1. a source-level producer for the actual finite maps `A_(M,N),K_(M,N)`;
2. a directed enclosure of the realized quartic jet;
3. a proof that the complete-window body errors decay.

No RH claim is made.
