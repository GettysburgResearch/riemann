# R-105640 — Small current charge does not remove a boundary zero

Claim ID: `R-105640`  
Status: **PROVED EXACT ONE-FACTOR FIREWALL**  
Created: 2026-08-25  
Depends on: `L-105642--L-105643`; sibling `L-106430--L-106431`  
RH status: **not assumed**

## 1. One fixed topological factor

Fix `H>0` and let

\[
B_y(z)={z-iy\over z+iy},
\qquad y>0.
\]

This is one simple upper-half-plane Blaschke factor. Its model space has

\[
\boxed{\dim K_{B_y}=1}
\tag{R-105640.1}
\]

and its boundary winding has one unit of topological degree, independently of
`y`.

## 2. Its current-weighted charge vanishes at the boundary

`L-105642` gives exactly

\[
\boxed{
\operatorname{tr}_{K_{B_y}}M_{e^{-H\xi}}
={2y\over H+2y}.
}
\tag{R-105640.2}

Therefore

\[
\boxed{
\operatorname{tr}_{K_{B_y}}M_{e^{-H\xi}}
\longrightarrow0
\qquad(y\downarrow0),
}
\tag{R-105640.3}

while the model-space dimension and winding remain equal to one.

For the actual Xi current profile, `L-105641` only decreases the charge:

\[
\operatorname{tr}_{K_{B_y}}M_{r_{H,h}}
\le {h\over H}{2y\over H+2y}
\longrightarrow0.
\tag{R-105640.4}

## 3. Consequence

No estimate of the form

```text
current-weighted anti-inner trace = o(1)
```

can, by itself, imply that the corresponding all-pass degree is zero. A
boundary zero is precisely the configuration in which the source metric loses
coercivity relative to topological count.

This is the model-space version of the zero-height/spatial-escape obstruction:
source energy can migrate to frequencies of order `1/y`, while the integer
index remains unchanged.

## 4. Correct use of the depth theorem

`L-105643` remains valuable because it proves that every fixed-depth packet is
source-expensive and localizes all possible cheap adverse geometry to a
vanishing collar. But the final collar must be treated by a signed index,
confluent boundary theorem, or pointwise evaluation identity. It cannot be
removed by taking the current trace to zero.

Accordingly the valid implication is

```text
soft depth estimate
 -> only a microscopic boundary collar remains,
```

not

```text
soft depth estimate
 -> no anti-inner zero.
```

## 5. Scope

The firewall does not refute an Xi-specific collar theorem. It proves that such
a theorem must retain topology or pointwise phase information; weighted source
smallness alone is insufficient.