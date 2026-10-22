# T-26201 — Full RH proposal by dyadic two-contact signed carry contraction

Claim ID: `T-26201`  
Title: The corrected fixed-`q_0=2` normal source, its exact two-contact carry image, and one parity-weighted greedy slack theorem would prove RH  
Status: **FULL PROPOSAL — DYADIC SIGNED SLACK / BOTTOM-CHARGE DESCENT OPEN; RH NOT CLAIMED PROVED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Dependencies: PR #241 `L-9518`; PR #158 `L-15159`; PR #236 `L-23010`--`L-23012`; PR #244 `L-23701`, `L-23705`, `L-23706`; `L-26201`--`L-26203`  
Scope: corrected source-specific proposal after the reflected-normal and high-index carry-transport audits

## 1. Starting point: the corrected coupled normal block

PR #241 replaces the invalid one-frequency localization by the exact
two-frequency identity

\[
\mathcal B_{J,H}
=
{1\over(2\pi)^2}
\iint
F_\alpha(t)\overline{F_\alpha(s)}
\Phi_{J,\alpha}(t-s)\,dt\,ds,
\tag{T-26201.1}
\]

which expands to the physical factor-ratio normal Gram

\[
\mathcal B_{J,H}
=
\sum_{m,n}
{\Lambda(m)\Lambda(n)\over\sqrt{mn}}
K_J^H(\log m,\log n).
\tag{T-26201.2}
\]

Fixing the Heath--Brown logarithmic coordinate at `q_0=2` leaves the exact
Möbius source of `L-15159`. Applying the bounded dyadic shell difference to
that source produces

\[
b_2(n)
=
\mu(n)-\mathbf1_{2\mid n}\mu(n/2).
\tag{T-26201.3}
\]

PR #236 proves that the normalized dyadic Mertens shell is the causal primitive
of this atomic source and that their smoothed Sobolev energies have the same
Hardy abscissa.

Thus the corrected physical block really does contain the dyadic `b_2` source.
No generic Farey vector, arbitrary packet coefficient, or one-frequency global
integral is used.

## 2. Why the direct parity-comb inversion does not close

The positive parity comb `P_2` satisfies an exact first-kind equation

\[
P_2*\beta_2
=
w_\infty
-{3\over\sqrt2}\tau_{\log2}w_\infty
+\tau_{2\log2}w_\infty.
\tag{T-26201.4}
\]

Its transform is

\[
\widehat P_2(z)
=
{\eta(z+1/2)\over z+1/2}.
\]

A generic coercive inverse bound for convolution by `P_2` would itself exclude
the shifted zeta zeros. It is therefore not an independent elementary
contraction theorem.

The route must exploit the actual coefficient `b_2`, not positivity of the
kernel alone.

## 3. New exact source collapse

`L-26201` proves the pointwise identity

\[
\boxed{
\sum_{q=2}^n b_2(q)\chi_{n,q}(j)
=
-\mathbf1_{j=1}
-\mathbf1_{j=n-1}.
}
\tag{T-26201.5}
\]

Thus the complete dyadic Möbius source becomes exactly two carry contacts,
not a growing packet dictionary.

It follows that:

1. its averaged carry image is the harmonic ray
   \[
   \sum_q b_2(q)\beta_{nq}=-{2\over n+1};
   \]
2. its carry-Hermitian energy is explicit;
3. its reflected cross term with the von Mangoldt carry profile is
   \[
   -{2\log n\over n+1};
   \]
4. the orthogonal interior binomial profile supplies a strict positive Schur
   reserve for every `n>=4`.

This is the source-specific reserve which the frozen generic terminal-face
proposals were trying to manufacture indirectly.

## 4. Pivot from broad signed transport

The natural next attempt is to move the two-contact source through the signed
divisor-gradient transport of PR #254. `L-26202` proves an exact obstruction.

For every divisor-gradient coefficient vector `b`,

\[
\boxed{
\sum_q b_2(q)v_q(b)
=
-2b(2)+b(3).
}
\tag{T-26201.6}
\]

Under an adjacent flow correction

\[
b_F(m)=b(m)+F_{m-1}-F_m,
\]

the dyadic projection changes only by

\[
\boxed{3F_2-F_3.}
\tag{T-26201.7}
\]

Every high-index transport move `F_j`, `j>=4`, is invisible.

Therefore the half-scale defect-to-slack mechanism cannot by itself contract
the fixed-`q_0=2` source. It may rearrange the orthogonal constraint ledger,
but the RH-bearing dyadic charge survives at the bottom boundary.

This is the required pivot: the proof target must be a bottom-charge theorem,
not a broad transport-cost theorem.

## 5. Canonical finite object

Let `d_X^gr` be the exact backward greedy carry minorant of PR #244 and let

\[
s_X^{\rm gr}(q)
=
w_X(q)
-\sum_{n=q}^X d_X^{\rm gr}(n)\beta_{nq}
\ge0
\tag{T-26201.8}
\]

be its final residual.

Define

\[
\boxed{
\Pi_2^{\rm gr}(X)
=
\sum_{q=2}^X b_2(q)s_X^{\rm gr}(q).
}
\tag{T-26201.9}
\]

This is a finite, deterministic, source-bound scalar. It has two exact forms:

\[
\Pi_2^{\rm gr}(X)
=
\sum_{n=2}^X
b_2(n){n-1\over n+1}\ell_X(n),
\tag{T-26201.10}
\]

where `ell_X(n)` is the greedy blocker loss, and

\[
\Pi_2^{\rm gr}(X)
=
\sum_{\substack{m\le X\\m\ {m odd}}}
\mu(m)
\left[
s_X^{\rm gr}(m)
-2s_X^{\rm gr}(2m)
+s_X^{\rm gr}(4m)
\right].
\tag{T-26201.11}
\]

The first is a parity-weighted blocker debt. The second is a dyadic curvature
of the final slack.

## 6. Two-charge Green coordinate

Let `Gbar_X` be the full-divisor Dirichlet Gram of `L-26203` and put

\[
T_X=\overline G_X^{-1}s_X^{\rm gr}.
\tag{T-26201.12}
\]

The exact source charge is

\[
\overline G_Xb_2=-3e_2+e_3,
\]

so

\[
\boxed{
\Pi_2^{\rm gr}(X)
=
-3T_X(2)+T_X(3).
}
\tag{T-26201.13}
\]

The complete RH-bearing source has therefore been reduced to two bottom Green
coordinates. No bound for the total slack, every Green coordinate, or the full
Green energy is logically necessary.

## 7. Sole arithmetic theorem

The proposed completion is the following.

> **DSS — Dyadic Signed Slack theorem.** For every `epsilon>0`,
> \[
> \boxed{
> \Pi_2^{\rm gr}(X)
> =
> O_\varepsilon(X^\varepsilon).
> }
> \tag{T-26201.14}
> \]

Equivalent finite formulation:

\[
\boxed{
|-3T_X(2)+T_X(3)|
=
O_\varepsilon(X^\varepsilon).
}
\tag{T-26201.15}
\]

This is strictly weaker than the Greedy Slack theorem, since

\[
|\Pi_2^{\rm gr}(X)|
\le
2\sum_q s_X^{\rm gr}(q),
\]

but not conversely.

### Stronger production certificate

A constructive proof may establish the following fail-closed half-scale form.

> **PBD — Parity Blocker Descent.** There are absolute `A,C` such that the
> canonical blocker forest admits a signed dyadic-chain decomposition with
> every child endpoint `Y<=(X+1)/2` and
> \[
> \boxed{
> |\Pi_2^{\rm gr}(X)|
> \le
> C\log^A(2X)
> +
> \max_{2\le Y\le(X+1)/2}
> |\Pi_2^{\rm gr}(Y)|.
> }
> \tag{T-26201.16}
> \]

Iteration gives

\[
\Pi_2^{\rm gr}(X)=O(\log^{A+1}X)
\]

and hence DSS.

A production PBD proof must emit:

1. the exact blocker forest;
2. complete dyadic chains `m,2m,4m`;
3. every truncated-chain boundary;
4. the same-scale cluster solve;
5. the child endpoint map;
6. the bottom charges `2,3`;
7. equality of the signed parent and child ledgers before absolute values.

Counting blockers, transporting only positive defect, or omitting the bottom
charge does not prove PBD.

## 8. DSS implies RH

`L-26202` proves

\[
\Pi_2^{\rm gr}(X)
=
\mathcal R_2(X)
+
2\sum_{n=2}^X{d_X^{\rm gr}(n)\over n+1}.
\tag{T-26201.17}
\]

Feasibility gives

\[
\sum_{n=2}^X{d_X^{\rm gr}(n)\over n+1}
=
O(\log^2X).
\]

Thus DSS implies

\[
\mathcal R_2(X)
=
O_\varepsilon(X^\varepsilon),
\tag{T-26201.18}
\]

where

\[
\mathcal R_2(X)
=
\sum_{q=2}^X
{b_2(q)\over\sqrt q}\log{X\over q}.
\]

Its Mellin transform is

\[
\int_1^\infty
\mathcal R_2(X)X^{-z-1}\,dX
=
{(1-2^{-z-1/2})/\zeta(z+1/2)-1\over z^2}.
\tag{T-26201.19}
\]

The subpower estimate makes this expression holomorphic for `Re z>0`.
Every zeta zero `rho` with `Re rho>1/2` would create a genuine pole at
`z=rho-1/2`; the dyadic numerator cannot vanish there. Therefore no such
zero exists. Functional-equation symmetry gives

\[
\boxed{\mathrm{RH}.}
\tag{T-26201.20}
\]

## 9. Relationship to the corrected two-frequency normal Gram

The proposal does not discard `L-9518`. It uses it to identify and freeze the
correct physical source before changing coordinates.

A direct normal-Gram proof would require a source-specific map transferring the
strict carry Schur reserve in `L-26201.15` into the localized factor-ratio Gram.
No such map is currently proved. Generic parity-comb coercivity is circular,
and high-index signed transport is exactly invisible by (T-26201.7).

The signed-slack/Riesz pivot is therefore deliberate. It retains the same
fixed-`q_0=2` source but asks only for its two bottom carry charges, a strictly
smaller theorem than a complete coupled normal-Gram contraction.

A future Green-to-normal theorem would provide an independent completion, but
it is not imported as a hidden assumption here.

## 10. Exact evidence and mutation policy

`X-26201` verifies exactly:

- the divisor collapse `1*b_2=epsilon-delta_2`;
- the pointwise two-contact identity;
- the averaged rank-one collapse in 12,879 rows;
- the formal reflected cross term;
- the signed residual pairing;
- the dyadic-chain coefficient formula;
- the unprojected two-charge Green identity and inverse;
- the bottom-flow invisibility algebra.

The floating reconnaissance through `X=5000` finds only diagonal greedy
blockers. This is discovery only and is not promoted to Carry Saturation or RH.

Mandatory mutations for DSS/PBD include:

```text
same-sign Mobius cube
remove q=2 charge
remove q=3 charge
truncate one dyadic chain
route a child above X/2
replace signed debt by total variation
apply a high-index flow and falsely claim the dyadic charge changed
```

## 11. Status

```text
correct two-frequency source trace             EXACT / IMPORTED
dyadic shell and Sobolev source                EXACT / IMPORTED
pointwise two-contact carry theorem            PROPOSED COMPLETE
two-charge Green theorem                       PROPOSED COMPLETE
high-index transport invisibility              PROPOSED COMPLETE
DSS / PBD                                      OPEN, RH-BEARING
DSS => Mellin pole exclusion => RH             PROPOSED COMPLETE
Riemann Hypothesis                             UNPROVED
```

This is a new full proposal, not a repair of the frozen reflected-terminal
proof. It replaces a growing balanced packet theorem and a full unsigned slack
theorem by one explicit parity-weighted blocker scalar.
