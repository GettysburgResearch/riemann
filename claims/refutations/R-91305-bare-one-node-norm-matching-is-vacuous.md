# R-91305 — Bare one-node norm matching is vacuous without the analytic source intertwiner

Claim ID: `R-91305`  
Status: **EXACT METHOD FIREWALL / CORRECTION TO THE READING OF `L-91313`**  
Created: 2026-08-12  
RH status: **unproved**

## 1. Abstract scalar rescaling

Let `S>0` and `T>=0` be any two finite scalars. If `S>=T`, then the map

\[
 \sqrt S\longmapsto \sqrt T\oplus\sqrt{S-T}
 \tag{R-91305.1}
\]

is an isometry between one-dimensional source and a two-port output. If
`S=T`, it is an exact norm exhaustion.

Thus a statement of the form

```text
there exists a source vector at one node whose norm equals the proposed
critical+stable output norm
```

is empty unless the source vector and the output map are fixed independently
of the target norm.

## 2. Why the model-space diagonal remains useful

For the exact model-space ledger,

\[
 \mathcal K_a^{\rm src}
 =\mathcal K_a^{\rm crit}
  +\mathcal K_a^{\rm st,0}
  +\mathcal K_a^{\rm zero,\Delta},
 \tag{R-91305.2}
\]

one interior diagonal detects the complete zero port:

\[
 \mathcal K_a^{\rm zero,\Delta}(\eta,\eta)=0
 \iff B_a\text{ is constant}.
 \tag{R-91305.3}
\]

This implication is exact. What is not automatic is the identification of an
arithmetic vector with the model source evaluation vector.

## 3. Mandatory rigidity data

A valid one-node theorem must construct a map

\[
 \mathfrak J_a:
 \mathcal H_a^{\rm arith}
 \longrightarrow
 \mathscr S_a^{\rm model}
 \tag{R-91305.4}
\]

before the target norm is known, and must satisfy at least:

1. **fixed source vector:** the input is the pole-, anchor-, or cocycle-aligned
   Jordan/Green vector defined from the positive arithmetic measure;
2. **amplitude matching:** its visible scalar transfer equals the completed Xi
   quotient on a nonempty safe uniqueness set, not merely at one number;
3. **cocycle compatibility:** the maps commute with the coefficient-one
   divisor/scattering factorization in the scale parameter;
4. **tangent matching:** logarithmic jets are sent to the declared Cauchy/
   theta boundary jets with the recorded normalizations;
5. **no target-defined scaling:** no coefficient may use
   `K_src(eta,eta)`, the Blaschke factor `B_a`, or the desired residual norm;
6. **one common closure:** the one-node vectors arise by restriction of one
   closable source-to-model operator, not unrelated scalar isometries at each
   scale.

Only after these requirements hold does exhaustion at one node have content.

## 4. Planted-factor control

The symmetric planted-factor controls of PR #398 preserve:

```text
the true zeta Jordan Euler channel;
a positive completed one-Green source;
the functional equation;
boundary unitarity;
the horizontal cocycle;
```

while retaining an interior pole and a negative target Pick determinant.

Any proposed one-node construction that uses only a positive source norm may
be repeated for that control by scalar rescaling and therefore cannot prove RH.
The construction must fail there at one of the rigidity requirements in §3.

## 5. Corrected status of the one-node route

The exact model-theoretic statement survives:

```text
once a genuine arithmetic-to-model intertwiner is constructed,
one interior diagonal exhausts the complete zero port.
```

The following shortcut is refuted:

```text
one arbitrary scalar norm equality by itself proves zero-port absence.
```

Accordingly, `ONAE_a/PAAE_a` means **one-node exhaustion by a common analytic,
source-ordered, cocycle-compatible intertwiner**, not a one-dimensional norm
fit.
