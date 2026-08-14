# Factor-67 compact reserve: the remaining SONTR obligation is explicit

Date: 2026-08-14  
Branch parent: `research/gpt56-pro/91690-factor67-sontr` at
`13ad1fdbf06edc931dc0c524327b701c5c8f86a3`  
Status: **compact reserve proved on frozen interfaces; SONTR remains subject to independent reconstruction; RH unproved**

## Executive result

The remaining compact reserve obligation in the factor-67 SONTR packet does not
require an abstract finite/continuum atom approximation or the stability
multiplier `10152`.

The target-Hall output is exactly transparent in the **total physical equality
row**.  For every component row,

\[
\text{signed row}
=
\text{positive residual row}
+
\text{positive target-null Hall bonus}.
\]

This is an identity before ordinary and radix-four observation.  Therefore the
Hall-induced physical atom error is zero.

The one-global endpoint quantizer sees the equality density `L`, not the SHARP
target density `Psi`.  A directed census of all 66 one-sided arithmetic cells
proves

\[
159/500<L(x)<183/100<2,
\qquad 1\le x<67.
\]

The hostile distinction is real:

```text
max L on the strict factor-67 window:   2 sqrt(2)-1 = 1.828427...
max Psi on the first cell:              4 sqrt(2)-3 = 2.656854...
```

Thus the existing collar theorem keeps its `M=2` constant.

## Exact reserve

Put

\[
K=\lfloor X/67\rfloor+1,
\qquad
\sigma_K=K/(K+178).
\]

The genuine finite/continuum discrepancy is retained.  Exact directed
calculation gives

\[
C_{67}<19.
\]

Consequently, on `K<=q<=X/4`,

\[
\frac{|\mathcal D_4v_q(C_X-E_X)|}{\Omega_X(q)}
<\frac{5655}{32K}.
\]

After the one-use factor `sigma_K`, the strict unused detail is

\[
\boxed{
 s_X(q)\ge
 \frac{41}{32(K+178)}\Omega_X(q)>0.
}
\]

On the terminal annulus, possible overfill is below

\[
4452X^{-3/2},
\]

while the fixed source-owned top omission removes more than

\[
5033X^{-3/2}.
\]

The terminal margin is therefore

\[
\boxed{581X^{-3/2}.}
\]

## Source ownership and the port

The outer support starts at `K+2`, so its width-three quantization collar remains
above the recursive cutoff and every root quotient is strictly below `67`.  The
bottom width-two strip is unused labelled source, not a child.

On the top quotient cell `1<=X/s<2`, the equality density is

\[
L(X/s)=2\sqrt{X/s}-1\ge1
\]

and no odd Hall demand is active.  The terminal omission is therefore literal
source-owned equality mass.

For each positive branch, the `P_61/67` Schur port has reserve at least
`(1/9)V_b`, while its projective correction is less than `(1/9)V_b`.  Positive
summing before observation gives one aggregate port covering the aggregate
correction.  The normalized port mass remains below `14/3`.

## Causal grouping

The causal identity is applied to the one globally thinned parent packet.  All
fibrewise child contributions carrying the same rough prime are grouped inside
one positive child packet.  Hence the outer coefficient list appears once and

\[
\sum_i\alpha_i<67^{-1/2}<1/8.
\]

Applying the reset independently with a fresh coefficient list to every
endpoint fibre is not used.

## Score and SONTR consequence

The global thinning fraction is less than `11926/X`; its score cost against the
frozen polynomial majorant is bounded and tends to zero.  Bottom and top
omissions have fixed endpoint width, the martingale quantizer is
score-favourable, and the aggregate port is bounded.

Together with the frozen target-mass causal debt and the subcritical packet
envelope, this yields

\[
J_\Lambda(X)-\operatorname{Score}(d_X)
\le4\log X+C.
\]

The frozen radix-four dual identifies this with the `Y_4`-weighted native slack,
which is therefore `o(log^2 X)`.

## Replay

```bash
cd experiments/X-91692-factor67-reserve-closure
python3 verify.py
python3 -m py_compile verify.py
sha256sum -c SHA256SUMS
```

Retained verdict:

```text
PASS_FACTOR67_COMPACT_RESERVE_PROOF_OBLIGATION
```

The exact proof-object digest is recorded in the retained verification JSON and
the integration lock.

## Boundary

```text
Hall-induced total-row error                    PROVED ZERO
factor-67 equality-density bound                DIRECTED EXACT
interior compact reserve                        PROVED EXPLICITLY
terminal compact reserve                        PROVED EXPLICITLY
one aggregate P61/67 port                       PROVED ON FROZEN PORT INPUT
nonduplicating grouped causal coefficients      PROVED FORMALLY
compact SONTR proof obligation                  CLOSED
full frozen-stack SONTR composition             REVIEW-READY PROPOSAL
Riemann Hypothesis                              UNPROVEN
```
