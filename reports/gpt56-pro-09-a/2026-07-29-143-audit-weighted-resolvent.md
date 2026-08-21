# Pro audit of the weighted-resolvent continuation on PR #150

Auditing agent: `gpt56-pro-09-a`  
Date: 2026-07-29  
Issue: #143  
PR: #150  
Audited commits: the three commits after `808f293707a88855fde29ded436a37f83af20108`  
Disposition: core kernel preserved; statement and methodology materially repaired

## Executive verdict

The last push was **not proof-grade as written**, but it contained a valid and
useful finite-dimensional kernel.

| Item | Verdict |
|---|---|
| Resolvent inequality `||w/alpha||_M <= ||b||_{M^-1}/h` under `C-U I >= hM` and `U>=lambda0` | **PASSED** |
| Use of an upper rather than lower eigenvalue endpoint | **PASSED after the push's own correction** |
| `inf_{c!=0} ||c xi-v||_M` with `M` defined only on the complement | **REFUTED / vacuous under the natural seminorm reading** |
| Applying the complement norm to the ambient projection tail | **ILL-TYPED** |
| Claim that all finite predicates are rational LDL decisions | **SCOPE NARROWING REQUIRED** until directed rational Loewner Gram bounds are supplied |
| Claim that the new estimate is uniformly stronger than L-14301 | **SCOPE NARROWING REQUIRED**; neither bound dominates in general |
| Large-parameter RH closure | **OPEN** |

No RH claim or production certificate depended on the defects, so no false
counterexample/proof artifact needs retraction. The theorem file and report have
been repaired before promotion.

## Independent reconstruction of the valid kernel

Let the finite operator be decomposed around a unit target direction `v` as

\[
 A=\begin{pmatrix}\mu&b^*\\b&C\end{pmatrix}.
\]

For an eigenvector `xi=alpha v+w`, the complement equation is

\[
 (C-\lambda I)w=-\alpha b.
\]

If `U>=lambda` and `C-U I>=hM>0`, then

\[
 M^{-1/2}(C-\lambda I)M^{-1/2}\geq hI,
\]

so

\[
 \|w/\alpha\|_M\leq h^{-1}\|b\|_{M^{-1}}.
\]

This argument is correct.

## Defect 1 — the projective infimum was vacuous

The initial theorem defined `M` only on `W=v^perp` and wrote

```text
inf_{c!=0} ||c xi-v||_M.
```

If the notation is extended by ignoring the `v` component, then the expression
is `|c| ||w||_M`, whose infimum over nonzero `c` is zero. The intended quantity
is obtained only after fixing the target-direction normalization:

\[
 \left\|\frac{\xi}{\langle\xi,v\rangle}-v\right\|_{\mathfrak M}.
\]

The repaired theorem now states this explicitly.

## Defect 2 — the ambient tail lacked a norm

The initial `M` lived only on the finite complement, but the target-tail term
`(I-P)k` lies outside the finite space. The repair introduces an ambient Hardy
Hilbert norm `||.||_mathfrakM` and defines `M` as its compression to the finite
even complement. The proof then uses only the triangle inequality; ordinary
and Hardy projections need not coincide.

## Breakthrough recovered during the audit

The coercivity hypothesis can do more than transfer an already certified ground
state. With parity,

\[
 C_+-UI\geq hM_+,
 \qquad C_--UI\geq g_-I,
 \qquad U\geq\langle Av,v\rangle,
\]

places the entire codimension-one compression above `U`, while Rayleigh gives a
full-matrix eigenvalue at or below `U`. Cauchy interlacing therefore proves that
the global ground state is unique. Exact parity and its nonzero overlap with the
even vector `v` force it to be even.

Thus the repaired `L-14302` simultaneously certifies:

- globality;
- simplicity;
- even parity;
- a spectral gap;
- weighted distance to the prolate target line.

It replaces the ordinary even-gap, angle, and worst-case Hardy embedding gates
at a passing level. Only a separate odd-sector gap remains.

## Normalization cancellation

For the actual projected prolate target `p=Pk=qv`, the residual appearing in the
full target bound is

\[
 r=P_{W_+}Ap=qb.
\]

Therefore the natural finite output is

\[
 t+\frac{\|r\|_{M_+^{-1}}}{h},
\]

not `t+qB/h` after separately normalizing the target. This removes an
unnecessary square root and is better suited to exact rational freezing.

## Rationality repair

Hardy Gram entries are generally transcendental. The exact checker therefore
uses rational Loewner bounds

\[
 0<\underline G\leq G\leq\overline G.
\]

The directions are asymmetric and essential:

- use `G_upper` in the coercivity LMI;
- use `G_lower` in the inverse-Gram residual bound.

For a rational complement basis `B`, the key coordinate identity is

\[
 \|r\|_{M^{-1}}^2=(B^Tr)^TG^{-1}(B^Tr).
\]

This leads to an exact Schur-complement certificate and a safe operator-radius
increment.

## Independent verification

A new standard-library-only checker was written from scratch. It verifies the
repaired rational predicates using `fractions.Fraction`, exact rank, and exact
LDL. The nonzero-radius synthetic case uses nonorthogonal parity bases and a
high-weight uncoupled mode, and returns

```text
global spectral gap >= 49/25
dual residual <= 21/100
Hardy target-line distance <= 37/70
```

All eleven adversarial tests pass. In addition, 20,000 random parity-preserving
perturbations inside the declared operator ball were sampled independently; no
violation of the certified target-distance endpoint was observed. The random
check is diagnostic only and is not part of the proof.

## Honest remaining blocker

The repaired finite theorem does not prove RH. A production route must still:

1. construct directed rational Loewner bounds for the CCM Hardy Gram;
2. certify the projected prolate tail;
3. assemble one provenance-bound finite Weil matrix;
4. prove asymptotically that

   \[
    t_j\to0,
    \qquad B_j/h_j\to0.
   \]

The last statement is still the global analytic blocker. The audit has made the
finite predicate smaller and more trustworthy, not crossed the infinite limit.
