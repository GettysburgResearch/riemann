# L-4503 — Fixed-vector Pick contraction preserves uncertainty correlation

Claim ID: L-4503  
Title: A Pick Rayleigh witness is one linear functional of sampled `xi'/xi` values  
Status: PROPOSED  
Authoring agent: `gpt56-06-b`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: D-3201 and L-3202 from draft PR #38; L-4502  
Scope: quantitative survival of finite Pick-Rayleigh witnesses  
Related counterexample candidates: future `xi'/xi` passivity witnesses

## Statement

Let

\[
 s_1,\ldots,s_m\in\{s:\operatorname{Re}s>1/2\}
\]

be exact rational or dyadic complex points, let

\[
 F_j=F(s_j),
 \qquad F=\xi'/\xi,
\]

and let the Pick matrix from `L-3202` be

\[
 K_{jk}=\frac{F_j+\overline{F_k}}
 {s_j+\overline{s_k}-1}.
\]

For an exact Gaussian-rational or Gaussian-dyadic vector
\(v\in\mathbb C^m\), define

\[
 c_j=\overline{v_j}
 \sum_{k=1}^m
 \frac{v_k}{s_j+\overline{s_k}-1}.
\]

Then the exact fixed-vector Rayleigh value satisfies

\[
 \boxed{
 v^*Kv=2\operatorname{Re}\sum_{j=1}^m c_jF_j.
 }
\]

Suppose a rigorous evaluator exports independent complex disk enclosures

\[
 F_j\in B(z_j,r_j)
 =\{z:|z-z_j|\le r_j\}
\]

and exact rational bounds \(M_j\ge0\) satisfying

\[
 M_j^2\ge|c_j|^2.
\]

Then every admitted Pick matrix satisfies

\[
 v^*Kv
 \le
 2\operatorname{Re}\sum_jc_jz_j
 +2\sum_jM_jr_j.
\]

Therefore, if the right-hand side is strictly negative, the exact vector remains
a negative Pick direction for every sampled-value realization in the declared
disks.  Conditional on the logical gates in `D-3201/L-3202`, RH is false.

If the `F_j` errors are correlated, replace the independent-disk sum by the
support function of their exact joint uncertainty set as in `L-4502`; the
contraction identity is unchanged.

## Definitions

- The points and vector are exact certificate data.  A floating eigenvector may
  nominate them but does not enter the proof.
- The denominators have strictly positive real part because both sample points
  lie in the open shifted half-plane.
- The disk centers and radii must be exported with exact rational outer data.
- The coefficient bounds \(M_j\) can be checked without square roots through
  \(M_j^2\ge\operatorname{Re}(c_j)^2+\operatorname{Im}(c_j)^2\).

## Motivation

An entrywise interval construction evaluates each uncertain `F_j` many times:
once in every entry of row `j` and once conjugated in every entry of column `j`.
Ordinary interval arithmetic forgets that these repetitions refer to the same
primitive value.  The resulting dependency blowup can make a strict negative
direction appear unresolved.

The correct proof order is:

1. freeze the exact vector;
2. contract the symbolic matrix algebraically;
3. evaluate the resulting linear functional once per primitive `F_j`;
4. maximize that scalar over the joint uncertainty set.

This is the Pick-route instance of “contract before enclose.”

## Proof

Write

\[
 d_{jk}=s_j+\overline{s_k}-1.
\]

The Rayleigh value is

\[
 v^*Kv
 =\sum_{j,k}\overline{v_j}v_k
   \frac{F_j+\overline{F_k}}{d_{jk}}.
\]

Separate the two terms and define

\[
 A=\sum_{j,k}\overline{v_j}v_k\frac{F_j}{d_{jk}}.
\]

Because

\[
 \overline{d_{jk}}=d_{kj},
\]

we have, after conjugating and relabeling `j` and `k`,

\[
 \overline A
 =\sum_{j,k}\overline{v_j}v_k
   \frac{\overline{F_k}}{d_{jk}}.
\]

Hence

\[
 v^*Kv=A+\overline A=2\operatorname{Re}A.
\]

Collecting the terms with the same `F_j`,

\[
 A
 =\sum_j
 \left(
   \overline{v_j}\sum_k\frac{v_k}{d_{jk}}
 \right)F_j
 =\sum_jc_jF_j.
\]

This proves the boxed identity.

Now write

\[
 F_j=z_j+e_j,
 \qquad |e_j|\le r_j.
\]

Then

\[
 v^*Kv
 =2\operatorname{Re}\sum_jc_jz_j
 +2\operatorname{Re}\sum_jc_je_j
\]

and

\[
 2\operatorname{Re}(c_je_j)
 \le2|c_j||e_j|
 \le2M_jr_j.
\]

Summing proves the robust upper bound. ∎

## Certificate reduction

A proof-oriented `pick-disks` certificate needs only:

1. exact points `s_j`;
2. exact vector `v`;
3. one exact outer disk `(z_j,r_j)` for each `F_j`;
4. rational coefficient magnitude bounds `M_j`;
5. an exact rational upper bound for

   \[
   2\operatorname{Re}\sum_jc_jz_j+2\sum_jM_jr_j;
   \]

6. the logical-gate and uncertainty-closure manifests.

The checker reconstructs every denominator and coefficient directly.  It does
not trust matrix entries, an eigensolver, or a claimed Hermitian
symmetrization.

## Analytic domain audit

- Every sample point lies strictly in `Re(s)>1/2`.
- The evaluator must prove `xi(s_j)` excludes zero before forming `F_j`.
- The exact denominator `s_j+conj(s_k)-1` cannot vanish in the open half-plane.
- The lemma does not prove the Lagarias positivity criterion or the
  `D-3201/L-3202` zero expansion; those remain logical dependencies.
- No branch of a logarithm is used by the contraction itself.

## Dependency audit

- `D-3201` fixes `xi` and `F`.
- `L-3202` states that a strict negative exact Pick Rayleigh value contradicts
  RH, conditional on its imported normalization and convergence gates.
- `L-4502` supplies the support-function interpretation and the independent-disk
  robust bound.

The algebraic contraction is self-contained and can be reviewed independently
of the analytic theorem.

## Gap audit

- Midpoint averaging must not be used to manufacture Hermitian symmetry.
- Disk radii from a common evaluator may be correlated.  Treating them as
  independent disks is sound if the product of disks is a proved outer set, but
  may be unnecessarily weak.
- A fitted Loewner, Padé, or passivity model may nominate points and a vector;
  its values cannot replace direct `xi'/xi` balls.
- The exact vector must be nonzero, but it need not be normalized.
- Reusing a disk for a mutated point or changed precision must fail digest and
  provenance checks.
- A negative midpoint with a nonnegative robust upper endpoint is unresolved.

## Adversarial tests

1. Compare the compressed formula with an exact direct matrix contraction on
   rational synthetic data.
2. Change the denominator shift from `-1` to `0`; the equality must fail.
3. Set one `M_j` below `|c_j|`; exact squaring must reject it.
4. Enlarge all radii until the robust upper endpoint becomes positive; the
   checker must return `NOT_CERTIFIED`.
5. Put one sample point on `Re(s)=1/2`; the checker must reject the domain.
6. Duplicate one sample uncertainty channel in the manifest; closure must fail.

## Remaining uncertainty

The compression theorem is exact.  Its practical strength depends on tight,
proof-grade `F_j` disks and on whether the search discovers a vector with a moat
large enough to survive rationalization and evaluation error.  Joint affine or
Taylor-model enclosures may be substantially sharper than independent disks.

## Suggested next attack

Integrate the X-4501 `pick-disks` checker into Issue #39.  The Arb producer should
export exact rational outer disks for `F_j`, while the checker reconstructs the
fixed-vector contraction independently.  Extend the same “contract before
enclose” principle to the derivative-jet localizers in draft PR #43.
