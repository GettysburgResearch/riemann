# L-93023 - The positive scale-four Q4 transfer is source-owned and locally capacity-faithful modulo one principal channel

Claim ID: `L-93023`  
Status: **PROPOSED COMPLETE EXACT FINITE TRANSFER THEOREM - INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-16  
Depends on: `L-93022`; `R-93022`; the complete endpoint normalization of `T-93010`  
Scope: source ownership, orthogonal principal/transverse decomposition, and atomwise capacity; no aggregate critical estimate and no RH conclusion

## 1. Positive source measure

Use the nonnegative generalized-prime source

\[
 \Lambda_+
 =
 (\varepsilon+2\delta_2)*\Lambda_4
 \ge0
\]

from `L-93022`, and its exact physical fibres

\[
 Z_{m,N}(j)
 =
 h_m(N)-h_m(j)-h_m(N-j-1),
 \tag{L-93023.1}
\]

where

\[
 h_m(x)
 =
 \mathbf1_{m\le x}
 -
 2\mathbf1_{2m\le x}.
\]

The complete row is

\[
 R_N=\sum_{m\le N}\Lambda_+(m)Z_{m,N}.
 \tag{L-93023.2}
\]

The sum is finite. Each source atom occurs exactly once.

## 2. Canonical orthogonal split of one fibre

Define

\[
 \kappa_{m,N}
 =
 \frac1N\sum_{j=0}^{N-1}Z_{m,N}(j)
 \tag{L-93023.3}
\]

and

\[
 Z_{m,N}^{\perp}
 =
 Z_{m,N}-\kappa_{m,N}\mathbf1.
 \tag{L-93023.4}
\]

Then

\[
 \langle Z_{m,N}^{\perp},\mathbf1\rangle=0
 \tag{L-93023.5}
\]

and

\[
 \boxed{
 Z_{m,N}
 =
 \kappa_{m,N}\mathbf1+Z_{m,N}^{\perp}
 }
 \tag{L-93023.6}
\]

is the unique orthogonal principal/transverse split.

The scalar is explicit. Reversing the finite prefix sum gives

\[
 \boxed{
 \kappa_{m,N}
 =
 \mathbf1_{m\le N}\left(\frac{2m}{N}-1\right)
 -
 2\mathbf1_{2m\le N}
 \left(\frac{4m}{N}-1\right).
 }
 \tag{L-93023.7}
\]

Thus

\[
 \kappa_{m,N}
 =
 \begin{cases}
 1-6m/N,&m\le N/2,\\
 2m/N-1,&N/2<m\le N,\\
 0,&m>N.
 \end{cases}
 \tag{L-93023.8}
\]

No limiting argument enters this formula.

## 3. Exact aggregate principal channel

Summing (L-93023.6) with the positive source weights gives

\[
 \boxed{
 R_N
 =
 M_\circ(N)\mathbf1+R_N^\perp,
 }
 \tag{L-93023.9}
\]

where

\[
 \boxed{
 M_\circ(N)
 =
 \sum_{m\le N}\Lambda_+(m)\kappa_{m,N},
 }
 \tag{L-93023.10}
\]

and

\[
 R_N^\perp
 =
 \sum_{m\le N}\Lambda_+(m)Z_{m,N}^{\perp}.
 \tag{L-93023.11}
\]

The two outputs are orthogonal:

\[
 \langle R_N^\perp,\mathbf1\rangle=0.
 \tag{L-93023.12}
\]

Consequently the complete positive energy splits exactly:

\[
 \boxed{
 \mathscr P_\circ(N)
 =
 \frac{|M_\circ(N)|^2}{N}
 +
 \frac{\|R_N^\perp\|_2^2}{N^2}.
 }
 \tag{L-93023.13}
\]

This is the positive-source version of the variance identity in `T-93010`.

## 4. Atomwise transverse capacity

The fibres are step functions with at most four interior breakpoints. The
firewall `R-93022` proves the uniform estimate

\[
 \boxed{
 \|Z_{m,N}^{\perp}\|_2^2\le144m
 \qquad(1\le m\le N).
 }
 \tag{L-93023.14}
\]

When \(N\ge4m\), the sharper source-local decomposition is

\[
 Z_{m,N}
 =
 \mathbf1+E_{m,N},
 \tag{L-93023.15}
\]

with

\[
 |\operatorname{supp}E_{m,N}|\le4m,
 \qquad
 \|E_{m,N}\|_2^2\le64m.
 \tag{L-93023.16}
\]

Thus every atom enters the physical row through:

```text
one scalar principal port;
one mean-zero finite boundary packet;
one explicit local capacity <=144m.
```

This is a genuine capacity-faithful source interface. It is not a claim that
the sum of all local capacities is the optimal aggregate Gram capacity.

## 5. One-use provenance

The transfer may be implemented with the following immutable labels:

```text
source index m;
positive mass Lambda_+(m);
principal coefficient kappa_(m,N);
transverse vector Z_(m,N)^perp.
```

The two outputs are linear projections of the same atom. They are not two
independent copies of its mass. The exact ledger is

\[
 \Lambda_+(m)Z_{m,N}
 =
 \Lambda_+(m)\kappa_{m,N}\mathbf1
 +
 \Lambda_+(m)Z_{m,N}^{\perp}.
 \tag{L-93023.17}
\]

Summing (L-93023.17) once gives (L-93023.9). No prime tower, four-adic gauge,
Hardy boundary, or endpoint row is spent twice.

## 6. The remaining aggregate theorem

The local theorem closes the source/provenance and one-atom capacity
interfaces. The all-scale aggregate statement still required is a
source-specific bound of the form

\[
 \left\|
 \sum_{m\le N}\Lambda_+(m)Z_{m,N}^{\perp}
 \right\|_2^2
 \ll N^2\log^A N.
 \tag{L-93023.18}
\]

A source-blind Bessel estimate from (L-93023.14) is too weak because the
boundary fibres are nested. A proof must retain arithmetic cancellation,
a Carleson/martingale structure, or a coupling to the Cycle-Debt transverse
cone.

Independently, the principal output requires

\[
 M_\circ(N)\ll\sqrt N\log^B N.
 \tag{L-93023.19}
\]

By `T-93011`, (L-93023.19) is RH-bearing. The present theorem does not rename
it as a completed capacity estimate.

## 7. Cross-route opportunity

The two fifth-strike decompositions now have matching type signatures:

```text
Cycle Debt:
    irreducible dyadic root face
    + positive transverse carry cone;

Q4:
    irreducible scalar principal mean
    + positive-source transverse boundary Gram.
```

A legitimate cross-route closure would construct one source-owned map between
the two transverse objects and one separate conservative pairing of the two
principal outputs. It must not infer the principal pairing from positivity
alone.

This is a concrete synthesis target, not an asserted theorem.

## 8. Proof boundary

Established exactly:

1. the positive finite source measure;
2. the unique atomwise orthogonal split;
3. the explicit principal coefficient;
4. the complete aggregate principal/transverse identity;
5. exact energy orthogonality;
6. the atomwise capacity bounds;
7. a one-use provenance ledger.

Open:

1. the aggregate transverse Gram estimate;
2. the principal Q4 mean estimate;
3. a source-owned cross-route coupling;
4. RH.
