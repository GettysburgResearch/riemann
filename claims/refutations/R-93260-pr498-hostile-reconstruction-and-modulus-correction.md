# R-93260 — Hostile reconstruction of PR #498 and the corrected large-modulus line

Claim ID: `R-93260`  
Status: **INDEPENDENT RECONSTRUCTION / ONE NON-LOAD-BEARING CORRECTION**  
Created: 2026-08-16  
Frozen object: PR #498 at exact head `6cc0da2fa5711017e260ebdcea4ba8c22e453288`  
Scope: reconstruction only; PR #498 is not modified

## 1. Verdict

The following load-bearing interfaces of PR #498 survive an independent
reconstruction:

1. the open-cell predecessor is `N-j-1`;
2. the centered normalization is
   \[
   \mathscr V_\circ(N)=N^{-2}\sum_j|R_N(j)-M_N|^2;
   \]
3. for
   \[
   w(\theta)=\theta(1-\theta)-1/6,
   \]
   one has `int w=0` and `int w^2=1/180`;
4. the exact projection kernel is
   \[
   K(x)=x(1-x)(2x-1)/3;
   \]
5. the Mellin multiplier is
   \[
   \widehat K(s)=(s-1)/[3(s+1)(s+2)(s+3)];
   \]
6. the Q4 source multiplier and `Khat` do not cancel a nontrivial zeta zero;
7. the integer-to-real interpolation error is `O(1)`;
8. the implication
   \[
   \mathscr V_\circ(N)\ll\log^A N\Longrightarrow RH
   \]
   follows from the resulting holomorphic Mellin integral in `Re s>1/2`;
9. `RH => V_circ(N)=O(log^4 N)` follows from the von-Koch Chebyshev bound.

No macroscopic Selberg estimate, factor-67 theorem, or unreviewed positivity
producer is needed for those implications.

## 2. Exact correction to `T-93253.11`

`T-93253.11` states, for every surviving two-sided Fourier mode,

\[
q={N\over(a,N)}\ge {N\over a}>\sqrt N.
\]

This display is false when `a` lies near `N`. For example, `a=N-1` gives
`N/a` close to one.

The correct statement uses

\[
d_N(a)=\min(a,N-a).
\]

Because

\[
(a,N)=(N-a,N)=(d_N(a),N),
\]

every mode satisfying `d_N(a)<sqrt(N)` obeys

\[
\boxed{
q={N\over(a,N)}={N\over(d_N(a),N)}
\ge {N\over d_N(a)}>\sqrt N.
}
\tag{R-93260.1}
\]

The corrected conclusion is exactly the one used by the character-modulus
reindexing. This is a wording/display correction, not a failure of the
mean-free major-arc reduction.

## 3. Pole audit

At a nontrivial zero `rho`, the residue multiplier in the cubic transform is

\[
{\rho-1\over3(\rho+1)(\rho+2)(\rho+3)}
(1-4^{1-\rho}).
\]

For `0<Re rho<1`, none of its factors vanishes. The four-adic rational gauge is
analytic there. Thus every open-strip zero remains a genuine pole.

## 4. Interpolation audit

For `N<=X<N+1`, the endpoint set is unchanged and

\[
|K(m/X)-K(m/N)|
\le \|K'\|_\infty {m\over N^2}.
\]

The elementary estimate

\[
\sum_{m\le N}m|c_\circ(m)|=O(N^2)
\]

gives

\[
\mathcal A_\circ(X)-\mathcal A_\circ(N)=O(1).
\]

No square-root estimate is used in this interpolation.

## 5. Boundary

```text
centered cubic identity and normalization    RECONSTRUCTED
Mellin pole survival                         RECONSTRUCTED
integer-to-real interpolation                RECONSTRUCTED
centered-energy equivalence                  SURVIVES
T-93253.11 as printed                        FALSE NEAR a=N
correct d_N(a) large-modulus statement       EXACT
CPBD / arithmetic square-root estimate       STILL OPEN
RH                                           UNPROVED
```
