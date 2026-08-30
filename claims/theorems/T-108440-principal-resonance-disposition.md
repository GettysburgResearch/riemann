# T-108440 — The shared-fibre geometric route ends at the principal resonance

Claim ID: `T-108440`  
Status: **EXACT DISPOSITION THEOREM; NONRESONANT GEOMETRY CLOSED LOCALLY, PRINCIPAL ARITHMETIC OPEN**  
Created: 2026-08-31  
Depends on: `L-108430`, `L-108440`; PR #771; PR #776  
RH/GRH status: **unproved**

The shared-conductor programme now has an exact three-part disposition.

## 1. What the geometric/Frobenius machinery genuinely closes

The following statements remain valid:

```text
honest reduced Kummer augmentation object;
complete clean nonresonant square-root traces;
rank-free twisted squareclass Plancherel;
positive occupancy quotient;
positive mixture and physical-pushforward contraction;
literal source-vector bound by cell-summed coefficient energy.
```

Thus there is no remaining local object, family-size, atom-multiplicity or
positive rectangle-gluing obstruction in the complete clean nonresonant
sector.

## 2. What cannot be closed geometrically

When both marked residue fields admit the even quadratic character,
`L-108440` proves

\[
\widehat Z(\kappa_\ell,\kappa_\rho)
=
\sigma\tau\widehat Z(\mathbf1,\mathbf1).
\]

Therefore the double quadratic resonance is exactly the principal physical
member, and its positive moment differs from the principal moment only by the
explicit factor

\[
{4\ell\rho\over(\ell+1)(\rho+1)}.
\]

It has no nonconstant core variable and cannot receive Deligne or
square-root cancellation. Any theorem bounding that row after an absolute
value is already a theorem bounding the principal conclusion channel.

Hence `QRESBIND107300` was not a finite local cleanup. Its double-resonance
component contains the original principal arithmetic problem.

## 3. Correct remaining split

Replace the former single gate by:

```text
MIXEDRES108440:
  control the one-coordinate quadratic rows, live masks and endpoints after
  exact signed recombination;

PRINCIPALCELL108440:
  control the literal principal physical cell energy, equivalently the
  double-quadratic row on fibres where it exists, with valid principal
  binding.
```

The exact implication becomes

\[
\boxed{
\mathrm{COEFCELL}_{108430}
\wedge
\mathrm{MIXEDRES}_{108440}
\wedge
\mathrm{PRINCIPALCELL}_{108440}
\Longrightarrow
\mathrm{CBKM}_{106130}
\Longrightarrow
\mathrm{BCI}_{102990}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-108440.1}
\]

But `PRINCIPALCELL108440` is the conclusion-bearing arithmetic estimate. It
is not supplied by the function-field nonresonant trace theorem.

## 4. Programme verdict

The shared-fibre route has produced a useful local mechanism and a faithful
source coordinate, but it has **not** moved the principal number-field
obstruction into geometry. The clean nonresonant sector is solved; the
remaining double resonance is the principal channel itself.

Future work on this branch is justified only if it attacks the literal
principal cell energy or proves a new signed principal/resonance
recombination. More occupancy, rank or complete-fibre geometry will not close
RH.

```text
clean nonresonant local geometry            CLOSED
positive source-vector quotient             CLOSED
unweighted occupancy necessity              REFUTED
double quadratic row = principal member     PROVED EXACT
geometric disposal of double row            IMPOSSIBLE
mixed one-coordinate rows                    OPEN
principal arithmetic cell energy             OPEN / CONCLUSION-BEARING
RH / GRH                                      UNPROVED
```
