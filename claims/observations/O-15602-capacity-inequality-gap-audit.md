# O-15602 — Gap audit for the scalar cofinal capacity inequality

Claim ID: `O-15602`  
Title: The proposed inequality is an exact saturation statement, not a free rank-growth estimate  
Status: `RESEARCH AUDIT`  
Authoring agent: `gpt56-pro-09-d`  
Created: 2026-07-31  
Related claims: `L-15304`, `L-15603--L-15605`, `T-15602`

## Requested statement

The proposed final arrow was

\[
 D(a_j,t_j,\Gamma_j)
 \le C(a_j,\varepsilon_j),
 \qquad
 \varepsilon_j\to0.
\]

Here `D` was intended as a certified upper count for the dangerous low-symbol
packet and `C` as the largest exact near-radical packet.

## Audit verdict

For `epsilon<t<Gamma`, min--max gives the reverse chain automatically:

\[
 C(a,\varepsilon)
 \le N_A(t)
 \le N_A(\Gamma)
 \le D(a,t,\Gamma).
\]

Therefore the requested inequality can hold only through the exact equality

\[
 C=N_A(t)=N_A(\Gamma)=D.
\]

This is not a semantic objection.  It changes the proof target from a dimension
comparison to a no-extra-low-mode theorem.

A loose `D` can always be increased while remaining valid, so no theorem can
force a loose cap below `C`.  The proof must replace it by a newly certified
sharp count `D_sat=dim L`.

## What was proved

1. `L-15603`: exact index sandwich and equality consequence.
2. `L-15604`: finite symbol-outer plus visible-Schur certificate proving
   `A|L^perp>=Gamma` and hence count saturation.
3. `L-15605`: exact codimension loss for constructing radical capacity from a
   uniformly concentrated source packet.
4. `T-15602`: saturation plus vanishing packet forms gives `F_j->0-` and invokes
   the existing cofinal lower-envelope theorem.
5. `X-15602`: exact finite synthetic saturation and inverse-Ritz replay.

## What was not proved

No theorem currently shows that the finite visible Schur block is nonnegative
on an unbounded support sequence.  Equivalently, no theorem rules out one extra
low evaluation-visible direction cofinally.

This is the remaining zeta-specific substance.

## Effect of L-15304

The zero-evaluation obstruction shows why a full-packet radical approximation
can fail even under RH.  The repaired architecture must split

```text
low symbol packet
 = radical-like evaluation near-kernel
 + evaluation-visible finite block.
```

Only the first piece is absorbed into `C`.  The second is retained in the finite
saturation Schur matrix.  Ignoring it would assume the desired inequality.

## Capacity-side progress

Rank--nullity proves that exact source repair costs at most two dimensions, and
only one in a self-dual sector.  Recent pre-plunge localization estimates can
therefore give strong lower bounds for `C`, provided the tail/form estimate is
uniform on the whole growing packet.

That still does not prove saturation: a large capacity supplies low modes, but
it cannot exclude an additional low mode.

## Sharp remaining statement

The load-bearing theorem is now:

> Along a cofinal support sequence, after adjoining every repairable
> evaluation-near-kernel direction to the exact radical packet, the complete
> evaluation-visible Schur complement is bounded below by `Gamma_j`, with
> packet form scale `alpha_j=o(t_j)` and complete residual scale
> `beta_j^2=o(t_j)`.

This statement is exactly strong enough for `T-15602` and no longer asks for a
principal angle or individual eigenvector convergence.

## Counterexample and RH status

- No contradiction to RH is claimed.
- No proof of RH is claimed.
- The scalar inequality has been logically characterized and reduced to a
  finite cofinal saturation certificate.
- The final arithmetic visible-block estimate remains open.
