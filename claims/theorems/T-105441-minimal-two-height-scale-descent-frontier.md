# T-105441 — Minimal two-height scale descent is the sharp scalar Xi frontier

Claim ID: `T-105441`  
Status: **EXACT MINIMAL EQUIVALENCE + UNCONDITIONAL COARSE ENDPOINT; SCALE DESCENT OPEN**  
Created: 2026-08-24  
Depends on: `T-105430`, `L-105438--L-105439`  
RH status: **unproved**

## 1. Minimal field

For

\[
m_r(z)={\Xi^{(r)}(z)\over\Xi^{(r+1)}(z)},
\]

put

\[
\boxed{
\mathcal Q_r(a,h)
=-{4\over3}\Im m_r(a+ih)
+{2\over3}\Im m_r(a+2ih).
}
\tag{T-105441.1}

The coefficients are uniquely determined by two requirements:

```text
cancel every affine carrier az;
recover one pole residue after multiplying by h and sending h to zero.
```

No one-height field can satisfy both.

## 2. Exact RH equivalence

Define

```text
MTM105441(r) — minimal two-height microscope

For every real a and h>0:
  Xi^(r+1)(a+ih) and Xi^(r+1)(a+2ih) are nonzero;
  Q_r(a,h)<=0.
```

Finiteness excludes all nonreal critical points. At a real critical point,

\[
\rho_c=\lim_{h\downarrow0}h\mathcal Q_r(c,h).
\]

Conversely, real critical points with nonpositive residues make `m_r` Pick and
give

\[
\mathcal Q_r(a,h)
=
\sum_c\rho_cK_{a,h}(c)\le0
\]

with `K_(a,h)>0`. Therefore

\[
\boxed{
\mathrm{MTM105441}(r)
\Longleftrightarrow
\mathrm{CRVH105330}(\Xi^{(r)})
\Longleftrightarrow
\Xi^{(r)}\text{ is real-rooted}.}
\tag{T-105441.2}

At the base rung,

\[
\boxed{
\mathrm{MTM105441}(0)
\Longleftrightarrow
\mathrm{RH}.}
\tag{T-105441.3}

## 3. Unconditional coarse endpoint

For every fixed derivative order there is `H_r` such that

\[
\boxed{
\mathcal Q_r(a,h)<0
\qquad(a\in\mathbb R,\ h\ge H_r).}
\tag{T-105441.4}

This follows only from completed-zeta Stirling asymptotics and the absolutely
convergent right-half-plane zeta series.

## 4. Exact scale equation

On the real-critical distribution stratum,

\[
\boxed{
\partial_h\mathcal Q_r
=-2|D|{I-e^{-h|D|}\over2I-e^{-h|D|}}\mathcal Q_r,
}
\tag{T-105441.5}

and

\[
\boxed{
(\partial_h+|D|)(\partial_h+2|D|)\mathcal Q_r=0.
}
\tag{T-105441.6}

The coarse-to-fine conclusion runs backward against this dissipative flow.

## 5. First obstruction

Starting at large `h` and decreasing the scale, the first failure is exactly:

```text
pole:     one sampled Xi^(r+1) value vanishes;
or
contact:  Q_r reaches zero and then becomes positive.
```

The pole is a nonreal critical point. The fine-scale limit of a positive
contact is a positive critical residue. Thus the two former sharp defects are
one scale-flow obstruction.

## 6. Single remaining theorem

Define

```text
MTSD105441 — minimal two-height scale descent

For r=0, the unconditional coarse negative solution extends to every h>0
without a pole or positive contact.
```

Then

\[
\boxed{
\mathrm{MTSD105441}
\Longrightarrow
\mathrm{MTM105441}(0)
\Longrightarrow
\mathrm{RH}.}
\tag{T-105441.7}

`MTSD105441` is RH-equivalent, but the scale representation exposes a concrete
nonlocal evolution, a terminal sign, and a precise first-failure geometry.

## 7. Relation to the three-height packet

`T-105440` remains a valid smoother microscope with sixth-order spatial decay.
The present theorem supersedes it as the minimal conclusion-facing gate:

```text
three heights: stronger localization decay, third-order scale equation;
two heights:   minimal affine-free detector, second-order scale equation.
```

## 8. Exact frontier

```text
minimality and positive two-height kernel        PROVED EXACT
residue recovery                                 PROVED EXACT
coarse negativity                                PROVED UNCONDITIONALLY / REVIEW
second-order nonlocal scale flow                  PROVED EXACT
MTSD105441 backward Xi scale control              OPEN / RH-EQUIVALENT
Riemann Hypothesis                               UNPROVEN
```
