# M-101100 — How to use the conjunctive implication matrix

Methodology ID: `M-101100`  
Status: **BINDING RESEARCH CONTRACT**  
Created: 2026-08-20

Do not dispatch every agent against a complete RH-equivalent scalar statement.
Freeze source ownership first, then assign different representations and
marginal estimates to different source regions.

```text
short / compact endpoint intervals
    -> PR #691 short theorem or c=-1 homotopy
    -> no activation atoms
    -> activation sparsity + phase/dispersion energy

long / renewal endpoint intervals
    -> c=0 homotopy
    -> no pre-activation collar
    -> finite interior squaring + divisor renewal

centered long-interval matrix
    -> source-owned regional partition
    -> first-owner estimate where squaring is strongest
    -> largest-owner estimate where renewal is strongest
    -> regional two-sided Schur product
```

Invalid substitutions:

```text
global positive mixing of c=0 and c=-1;
source-blind absolute values before the source split;
calling short-block scalar positivity an invariant cone;
requiring one global FOCR/LOCR proof when regional pairs suffice;
using a wavelet estimate on a differently normalized source;
adding estimates without exact owner provenance.
```

A new result should name the exact premise it supplies:

```text
SCPE101100
LARE101100
ROW_REGION_<name>
COLUMN_REGION_<name>
BSP(<source sector>)
DEP(<source sector>)
```

and include a statement-to-use map into `T-101100` and the inherited Landau
consumer.
