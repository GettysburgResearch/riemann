# Integration handoff — fixed-ratio Mertens shell

Agent: `gpt56-pro-09-p`  
Date: 2026-08-07  
Branch: `agent/gpt56-pro-09-p/234-fixed-ratio-mertens-shell`  
Status: **PROPOSED / GAP-BLOCKED / RH NOT PROVED**

## Frozen dependency graph

| Role | Frozen source |
|---|---|
| repository-wide reduction and first-cell audit | PR #229, `2fc74c11b9929f694d8c13d060c9d55b99dc9621` |
| exact Möbius decoder and high-order Euler closure | PR #158, `ec0b8fb0c877bb6f3140e12f4cdf80cacac34cd0` |
| terminal Euler / replacement Type-II proposal | PR #165, `13d32ea7a694acf64f5e55b4a41b9b632cd22dd0` |
| corrected Type-I routing and balanced packet interface | PR #233, `b64b9878006733e59e9c988de0c5e33242134afb` |
| reflected Selberg identity and audited closing claim | PR #226, `63a4d7c0f482a57893db420e64b22f6a605c72e6` |
| prime-only Hardy and semiprime source | PR #216, `b76eef1b769584aa9d66d082bfc6634126f986a2` |

Later mutable heads do not inherit this handoff automatically.

## Main new coordinate

For fixed `0<c<1`, define

\[
I_c(x)=M(x)-M(cx),
\qquad
Q_c(t)=e^{-t/2}I_c(e^t).
\]

Then

\[
Q_c(t)=\sum_n\frac{\mu(n)}{\sqrt n}
 e^{-(t-\log n)/2}
 \mathbf1_{[0,\log(1/c))}(t-\log n)
\]

and

\[
\mathcal LQ_c(z)
=
\frac{1-c^{z+1/2}}
{(z+1/2)\zeta(z+1/2)}.
\]

For `c=2/3`, this is the first Farey-cell Mertens increment.

The exact fixed block energy is one finite positive balanced Möbius Gram. `T-23401` proposes

\[
\mathrm{RH}
\iff
E_{c,B}(J)=e^{o(J)}.
\]

## New claims

- `L-23401` — compact fixed-ratio shell transform and positive finite Gram;
- `T-23401` — shell second moment/rightmost-zero criterion;
- `L-23402` — divisor recurrence and centered prime renewal;
- `L-23403` — high-order shell hierarchy;
- `L-23404` — top-order concentration after free-variable Euler closure;
- `R-23401` — one-prime parity pairing exits the shell;
- `R-23402` — reflected terminal endpoint counting does not prove the balanced packet theorem;
- `M-23401` — minimal balanced shell proof programme;
- `X-23401` — exact finite algebra, Gram, and mutation regression.

## Exact experiment

The retained proof-object digest is

```text
0772b74939f89a2e9ac45fe38fbc0e3fd4f131c9e3d83ecdbf7ab1debb3aeff1
```

with nine passing fail-closed tests.

## Review order

1. `L-23401-fixed-ratio-mertens-shell-safe-window.md`
2. `T-23401-fixed-ratio-shell-energy-rh-criterion.md`
3. `L-23402-mertens-shell-divisor-and-prime-renewal.md`
4. `R-23401-one-prime-parity-pairing-leaves-the-shell.md`
5. `L-23403-high-order-fixed-ratio-shell-hierarchy.md`
6. `L-23404-top-order-concentration-of-the-hard-heath-brown-core.md`
7. `R-23402-reflected-terminal-count-does-not-prove-balanced-contraction.md`
8. `M-23401-minimal-balanced-mobius-shell-program.md`
9. `X-23401-fixed-ratio-shell/`
10. report and this handoff

## Exact remaining theorem

Prove

\[
E_{2/3,\log2}(J)=e^{o(J)},
\]

or a source-specific recurrence with vanishing coefficient exponent relative to its strict scale contraction.

The proof must retain:

- complete Möbius signs;
- the reflected balanced prime/Möbius common-cell channel;
- all top-order packet cross terms;
- block boundaries and transitions;
- the first-cell shell source map.

## Integration cautions

1. Do not call `T-23401` a proof of the energy bound; it is a transfer theorem.
2. Do not use the generic Farey-cluster norm refuted on PRs #229/#231.
3. Do not infer balanced closure from terminal Euler closure.
4. Do not use PR #226 `L-9517` without repairing the missing `BTP(K)` step identified in `R-23402`.
5. Do not take total variation over the signed high-order shell vector.
6. Do not infer the cofinal bound from `X-23401` or the non-directed reconnaissance.

## Current classification

```text
exact shell algebra and finite Gram       PROPOSED COMPLETE
shell RH transfer                         PROPOSED COMPLETE
terminal/free-variable sectors            PROPOSED CLOSED ON FROZEN SOURCES
balanced shell contraction                OPEN
full RH proof                              NOT READY
RH                                         UNPROVED
```
