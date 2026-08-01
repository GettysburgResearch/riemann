# X-18502 — Full-complement exact verifier

Claim ID: `X-18502`  
Status: `EXACT FINITE RATIONAL REPLAY`  
Authoring agent: `gpt56-02-p`  
Created: 2026-08-01  
Dependencies: `L-18501`, `L-18507`

## Purpose

Verify one finite proof object for

```text
U = R direct-sum_G W,
K|W > tau G|W,
K|R < epsilon G|R,
epsilon < tau.
```

The checker then certifies

```text
N_(G^-1/2 K G^-1/2)(tau)=dim R
```

and the automatic angle bound `epsilon/tau`.

## Trust boundary

The implementation uses only Python integers, `fractions.Fraction`, JSON, and
SHA-256. It reconstructs ranks, metric orthogonality, complete packet span, and
strict rational LDL pivots. It does not trust a supplied eigenvalue or count.

## Retained result

```text
ambient dimension       4
radical/complement rank  2 / 2
threshold                1
radical endpoint         1/100
count                    2
angle squared upper      1/100
proof-object SHA-256
a89de5b1155948aaa524dcb3eabeff62b9e7d5d074fdbd9b2ff2336361c25f68
```

Nine central/adversarial tests pass.

## Scope

The exact replay checks the finite consequence only. The Paley--Wiener
uniqueness theorem, proof-grade zeta-zero isolation, harmonic normalization, and
cofinal frame-to-tail moat remain separate analytic gates.
