# O-15301 — July 2026 positive-path literature audit

Claim ID: `O-15301`  
Title: The exact source domain and low-subspace comparison are the remaining positive-path bottlenecks  
Status: `LITERATURE_AND_REPOSITORY_AUDIT`  
Authoring agent: `gpt56-03-j`  
Created: 2026-07-31

## Located primary sources

1. Alain Connes and Caterina Consani, *Spectral Triples and Zeta-Cycles*,
   arXiv:2106.01715; L'Enseignement Mathématique 69 (2023), 93--148.
2. Alain Connes, Caterina Consani, and Henri Moscovici, *Zeta Spectral
   Triples*, arXiv:2511.22755 (2025).
3. Masatoshi Suzuki, *Weil's quadratic form via the screw function*,
   arXiv:2606.09096 (June 2026).
4. Aleksei Kulikov, *Sharp estimates for eigenvalues of localization operators
   before the plunge region*, arXiv:2603.07407 (March 2026).
5. Aleksei Kulikov and Martin Dam Larsen, *Sharp estimates for eigenvalues of
   localization operators with applications to area laws*, arXiv:2603.23832
   (March 2026).
6. Ahmadreza Azimifard, *An independent proof of the plunge-region conjecture
   for time-frequency localization operators in dimension one*,
   arXiv:2607.23016 (July 2026).

Every reference above was located directly. No unlocated citation is used in the
claims on this branch.

## Source-domain correction

The Connes--Consani arithmetic map uses the codimension-two even Schwartz source
space

\[
 f(0)=0,\qquad\widehat f(0)=0.
\]

The second condition is the integral condition in the standard Fourier
normalization. A finite source chosen only to have zero integral does not
automatically satisfy the value-at-zero condition. Therefore a localized target
cannot be declared a truncation of a global Weil-radical vector until both gates
are checked in the exact source domain.

`L-15301` repairs this with a smooth compact cutoff of the self-dual CCM Hermite
source and one exact integral correction. `L-15302` gives a finite three-mode
linear-algebra repair when concrete source modes are preferred.

## What the latest localization results add

The 2026 localization papers rigorously sharpen two relevant facts:

- modes lying a fixed fraction before the time-frequency plunge have
  concentration eigenvalues exponentially close to one;
- the number of intermediate plunge eigenvalues has an explicit logarithmic
  upper bound in one dimension and sharp bounds for interval/parallelepiped
  geometries.

These results support a proof architecture with:

```text
near-one concentration block
+ explicitly bounded plunge block
+ coercive far complement.
```

They do **not** by themselves prove a lower bound for the arithmetic Weil form.
In particular, concentration close to one controls Fourier leakage, not the
prime-translation operator or the full Schur-corrected low spectral floor.

## Relation to the current repository

The newest positive repository stack has already made three important advances:

1. `T-14302` reduces RH to a cofinal localized lower floor whose negative part
   vanishes;
2. `L-14308` charges low/complement coupling quadratically through a block Schur
   correction;
3. `L-14310/L-14311` reduce the infinite complement to a finite prolate or
   multiband packet plus an explicit coercive tail.

The present branch adds:

4. `L-15301`: an exact source-domain target with form-topology tail control;
5. `T-15301`: no special `Xi` coefficient ratio is required--zeta times any
   nonzero auxiliary factor suffices;
6. `L-15303`: arbitrarily large exact Hermite-radical blocks are available.

## Rejected inference

It is unsafe to argue

```text
small L2 prolate leakage
=> small Weil-form residual.
```

The Weil form is distributional/logarithmic, and the missing continuity norm has
to be proved. `L-15301` avoids that inference by making the Fourier defect tend
to zero in Schwartz topology before applying the arithmetic map.

It is also unsafe to read a shrinking positive prolate eigenvalue or a growing
near-one concentration count as progress toward RH without proving that the
associated packet captures every dangerous arithmetic direction.

## Revised critical path

The remaining positive proof can now be stated in one line:

\[
 \boxed{
 \text{principal angle between the dangerous low packet and an exact repaired
 radical packet tends to zero, with a certified complement floor.}}
\]

More explicitly:

1. choose the low packet from the multiband/prolate symbol bound;
2. choose a same-rank repaired Hermite packet from `L-15303`;
3. certify a directed principal-angle or graph-distance bound;
4. transfer the vanishing radical block and residual estimates through
   `L-14308`;
5. prove the resulting cofinal floor is at least `-epsilon(lambda)` with
   `epsilon(lambda)->0`;
6. invoke `T-14302`.

## Honest conclusion

The source normalization and target-tail problem have a clean repair. The
latest prolate literature makes the finite packet smaller and better organized.
The decisive low-subspace comparison and arithmetic complement coercivity are
not yet proved. Accordingly this audit does not claim RH.