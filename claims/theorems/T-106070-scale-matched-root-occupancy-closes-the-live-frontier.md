# T-106070 — Retracted scale-matched root-occupancy closure proposal

Claim ID: `T-106070`  
Programme aliases: `LFAM1.RETRACTED_SCALE_MATCHED_CLOSURE`, `STRESS.HBC_CLOSURE_AUDIT`, `LFAM2.BLOCK_KUMMER_RETRACTION`  
Status: **RETRACTED AFTER HOSTILE SELF-AUDIT**  
Created: 2026-08-25  
Retracted: 2026-08-25  
Superseded by: `R-106071`, `L-106074--L-106075`, `T-106071`  
Programme issues: #743, #736, #737  
RH status: **unproved**

The first version of `T-106070` claimed a full chain

\[
\mathrm{SMCROP}_{106070}
\Longrightarrow
\mathrm{HBCQDSP}_{102888}
\Longrightarrow
\mathrm{RH}.
\]

That chain is withdrawn.  The exact failure is identified by `R-106071` and
the retraction record `L-106073`.

## 1. What the attempted proof established correctly

On each stopped-Vaughan block \(c\in[B,8B)\), a three-prime palette and a
disjoint linear owner colouring provide a modulus

\[
16B<\ell<256B,
\qquad \ell\ne67,
\]

which divides no physical index in the colour.  Thus the principal character
is literally the native coloured source.

For each fixed owner pair, every surviving congruence

\[
Pc^2\equiv Qd^2\pmod\ell
\]

is a union of at most two partial matchings

\[
c\equiv\pm\tau d\pmod\ell.
\]

The exact block energy

\[
E_{P,B}\ll\frac{X^{o(1)}}{PB}
\]

pays the conductor on the diagonal and on the quartic matched-pair tensor.
These are genuine advances and remain proved in `L-106070--L-106072` after
their corrected scope statements.

## 2. Why the conclusion failed

The character family is governed by the quadratic residue Gram

\[
\mathcal Q
=
\sum_{r\ne0}
\left\|
\sum_{Pc^2\equiv r}Z_{P,c}
\right\|^2.
\tag{T-106070.R1}
\]

The attempted proof instead bounded the quartic shadow

\[
\sum_{P,Q,d}
\|Z_{P,c(d)}\|^2\|Z_{Q,d}\|^2.
\tag{T-106070.R2}
\]

Scaling every source atom by \(\lambda\) multiplies (T-106070.R1) by
\(|\lambda|^2\) and (T-106070.R2) by \(|\lambda|^4\).  Therefore the claimed
adapter is impossible.  Many different owner packets may occupy one residue
cell coherently even though every fixed owner-pair core line is injective.

The first false edge was

```text
quartic matched-pair tensor occupancy
    -> quadratic character-family moment.
```

No detector or Mellin edge was reached.

## 3. Corrected frontier

`L-106074` proves the exact quadratic normal form, and `L-106075` closes the
diagonal and every cell with only subpower owner crowding.  The live theorem is

```text
HQORO106071:
  control the quadratic residue Gram on the remaining cells containing a
  power-sized coherent family of distinct owner packets.
```

The corrected implication is

\[
\boxed{
\mathrm{HQORO}_{106071}
\Longrightarrow
\mathrm{HBCQDSP}_{102888}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-106070.R3}
\]

`HQORO106071` is open.

## 4. Relation to the common repository obstruction

The remaining high-crowding residue Gram is a finite-field coordinate of
`BPOE103300`, the physical occupancy norm which survives across the principal
proof routes.  The failed proposal therefore did not reveal an independent
new assumption; it rediscovered the same owner-coherence interface after
removing core multiplicity and conductor costs.

## Exact final status

```text
linear scale-matched palette                       PROVED EXACT
coefficientwise unramified principal recovery      PROVED EXACT
fixed-owner-pair core matching                     PROVED EXACT
diagonal conductor payment                         PROVED
quartic matched-pair conductor payment              PROVED
quartic -> quadratic family adapter                 REFUTED
first L-106073 HBC closure                          RETRACTED
first T-106070 full RH proof proposal               RETRACTED
quadratic normal form                               PROVED
low owner-crowding cells                            PROVED
high owner-crowding assembly HQORO106071             OPEN / RH-BEARING
Riemann Hypothesis                                  UNPROVED
```

The rapid retraction is part of the proof record: the repository must preserve
both the promising mechanism and the exact reason it does not yet prove RH.