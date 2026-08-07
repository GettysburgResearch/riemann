# T-23004 — Full RH proposal by finite-prefix parity–Green coercivity

Claim ID: `T-23004`  
Title: A polylogarithmically conditioned finite digital prefix, certified by the two-frequency reflected block and the canonical carry Green correction, forces the dyadic shell energy to be subexponential and proves RH  
Status: **FULL PROPOSAL WITH ONE EXPLICIT SOURCE-SPECIFIC COERCIVITY THEOREM OPEN**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-08  
Frozen parent: PR #236 at `1c9a749a1648c4772509eb3b056598c7044f4393`  
Dependencies: PR #234 `T-23401`; PR #236 `L-23008`--`L-23012`; `L-23013`--`L-23016`; PR #241 `L-9518`; PR #248 `L-24509/L-24510`; PR #254 `L-25301`  
Scope: complete conditional deduction with one named finite-prefix theorem; RH is not claimed proved

## 1. The source and a harmless smoothing

Let

\[
B_2(x)=M(x)-M(x/2),
\qquad
q(t)=e^{-t/2}B_2(e^t).
\tag{T-23004.1}

Fix one real compact smooth multiplier `H` whose Laplace transform is nonzero in
`0<Re z<1/2`, and put

\[
q_H=H*q.
\tag{T-23004.2}

The safe-filter Hardy transfer gives

\[
\boxed{
\Theta_\zeta
=
\limsup_{J\to\infty}
\frac{\log(1+\|q_H\|_{H^1(0,J)}^2)}{2J}.
}
\tag{T-23004.3}

The first derivative is included only to use the exact Sobolev tail in
`L-23016`; any fixed finite graph norm has the same rightmost-pole exponent.

## 2. The exact digital finite-prefix equation

For `R>=3`, define

\[
\mathcal A_R
=I+
\sum_{3\le k<R}
\frac{1-v_2(k)}{\sqrt k}\tau_{\log k},
\tag{T-23004.4}

and the complementary tail `mathcal T_R` from `L-23016`. Since all convolutions
commute with the fixed smoothing,

\[
\boxed{
\mathcal A_Rq_H
=-H*e^{-t/2}-\mathcal T_Rq_H.
}
\tag{T-23004.5}

Every term of the tail is evaluated at logarithmic scale at least `log R` below
the output scale, and

\[
\boxed{
\|\mathcal T_Rf\|_2
\le
\varepsilon_R\|f\|_{H^1},
\qquad
\varepsilon_R=O((\log R)/\sqrt R).
}
\tag{T-23004.6}

## 3. The finite-prefix parity–Green theorem `PGC(R)`

The sole new theorem required by this proposal is the following.

> **`PGC(R)` — finite-prefix parity–Green coercivity.** There are an absolute
> exponent `A` and an unbounded sequence of integers `R` such that, for every
> source block of the actual Euler-aligned dyadic Möbius field and every `J`,
> the complete two-frequency reflected normal block, after the exact dyadic
> Green projection and canonical signed carry correction, proves
> \[
> \boxed{
> \|q_H\|_{H^1(0,J)}^2
> \le
> C(\log R)^A
> \left[
> 1+
> \|\mathcal A_Rq_H\|_{L^2(0,J+C_H)}^2
> \right].
> }
> \tag{T-23004.7}
> \]
> The proof object must retain all cross terms of the independent-frequency
> reflected identity `L-9518`. The dyadic prime-power sector must be eliminated
> through the explicit path Gram `L-23015`, and the remaining odd/mixed carry
> correction must be a positivity-preserving signed deformation of the exact
> Green solve, with total Dirichlet energy bounded by the right side of
> (T-23004.7).

This is not a generic multiplier inequality. `R-23007` proves that generic bulk
parity/carry coercivity is impossible. `PGC(R)` is a finite, source-specific
boundary Schur theorem.

## 4. Why the condition number must be polylogarithmic

Insert (T-23004.5) into (T-23004.7). Causality and (T-23004.6) give

\[
\begin{aligned}
\|q_H\|_{H^1(0,J)}^2
\le C(\log R)^A\bigl[
1+\varepsilon_R^2
\|q_H\|_{H^1(0,J-\log R+O_H(1))}^2
\bigr].
\end{aligned}
\tag{T-23004.8}

Since

\[
(\log R)^A\varepsilon_R^2
=O((\log R)^{A+2}/R),
\]

choose one retained `R` so large that this coefficient is less than `1/2`.
Iteration of (T-23004.8) then gives a bound polynomial in `J`; in particular,

\[
\boxed{
\|q_H\|_{H^1(0,J)}^2=e^{o(J)}.
}
\tag{T-23004.9}

Even the weaker recurrence with coefficient `C_R=(log R)^A` and no small tail
factor would give exponent at most

\[
\frac{A\log\log R+O(1)}{\log R},
\]

which tends to zero along the retained sequence.

## 5. Deduction of RH

Equation (T-23004.3) and (T-23004.9) give

\[
\Theta_\zeta=0.
\]

Functional-equation symmetry gives

\[
\boxed{\mathrm{RH}.}
\tag{T-23004.10}

Independently, `L-23008/T-23003` transfer the dyadic shell estimate to the
`2/3` first Farey cell, producing

\[
M(D)-M(2D/3)=O_\varepsilon(D^{1/2+\varepsilon}),
\]

and the geometric telescoping theorem `T-23002` again gives RH. Thus the final
proposal passes the mandatory first-cell mutation by an exact causal filter.

## 6. Proof-facing construction of `PGC(R)`

A production certificate must contain the following exact layers.

### 6.1 Two-frequency normal block

Use independent frequencies `(t,s)` and the block kernel
`Phi_(J,alpha)(t-s)` of PR #241. A single vertical integral is rejected.

### 6.2 Digital finite prefix

Bind every coefficient

\[
(1-v_2(k))/\sqrt k,
\qquad3\le k<R,
\]

and every delay `log k`. No tail term below `R` may be omitted.

### 6.3 Exact dyadic Green projection

At dyadic endpoint `2^N`, use the closed matrix and inverse in `L-23015`, not a
numerical pseudoinverse. This pays the complete power-of-two carry sector.

### 6.4 Odd/mixed signed correction

Start from the exact Green equality solve. Deform it by adjacent or plateau
flows, retaining both positive defect and negative slack, until the coefficient
minorant is nonnegative and all carry inequalities are satisfied. The
Dirichlet-energy cost is the Schur correction in (T-23004.7).

### 6.5 Strict scale ledger

Every unresolved tail source must begin at dilation `R`; same-scale
prime-power clusters must be solved jointly and all remaining children must be
routed to the declared lower scale.

## 7. Mandatory adversarial tests

A review must reject any certificate which:

1. replaces the two-frequency block by a diagonal `t=s` integral;
2. uses the rank-one bulk pair as a strict frame;
3. takes absolute values before digital Abel summation;
4. drops the negative carry slack;
5. omits the exact power-of-two Green block;
6. has condition number `R^c` with fixed `c>0` on every retained order;
7. fails the exact `2/3` shell transfer;
8. promotes finitely many successful prefixes to an all-order theorem.

## 8. Exact status

```text
positive p-adic combs and aligned contractions       PROPOSED COMPLETE
parity/carry compact dipole                           PROPOSED COMPLETE
finite-horizon output inequality                     PROPOSED COMPLETE
dyadic Green path block                              PROPOSED COMPLETE
digital H1 tail compactness                           PROPOSED COMPLETE
bulk two-channel source coercivity                    REFUTED
finite-prefix parity-Green coercivity PGC(R)          OPEN
conditional PGC(R) -> shell energy -> RH             COMPLETE
Riemann Hypothesis                                    NOT PROVED
```

This is a serious full proposal with one finite, source-specific theorem. It is
not represented as a completed proof until `PGC(R)` is constructed on an
unbounded prefix sequence with the stated polylogarithmic conditioning.
