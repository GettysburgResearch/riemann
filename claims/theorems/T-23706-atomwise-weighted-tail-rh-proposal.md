# T-23706 — Atomwise weighted-tail order implies RH

Claim ID: `T-23706`  
Title: A finite weighted-tail inequality for every positive parabolic endpoint atom makes every shell charge vanish and proves the Riemann Hypothesis  
Status: **FULL CONDITIONAL PROPOSAL — ONE FINITE ATOM-TAIL THEOREM OPEN**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Dependencies: `L-23717`; PR #265 `L-26201`; PR #276 `T-27501`; source-pinned square-screw/Landau transfer  
Scope: full Riemann Hypothesis

## 1. Atomwise Weighted-Tail Order

Retain the endpoint residual atom `e_T(q)` from `L-23717`.  The proposed theorem is

> **AWTO.** For every integer `T>=3` and every real `z>=2`,
> \[
> \boxed{
> \mathcal A_T(z)
> =
> \sum_{\substack{z\le p<T\\p\ {m prime}}}
> (\log p)e_T(p)
> \le0.
> }
> \tag{AWTO}
> \]

Every object is finite.  In the radical coordinate of `L-23717`, this is exactly

\[
\sum_{m=2}^{T-1}
F_T(m)[L_z(m)-L_z(m-1)]
\le
\ell_T
\sum_{z\le p<T}\frac{\log p}{\sqrt p}.
\tag{T-23706.1}
\]

No zero, contour, limiting operator, or omitted tail occurs in the statement.

## 2. AWTO makes the shell charge identically zero

Let `2<=Y<X`.  The exact endpoint telescope of `L-23717` gives, for every lower cutoff `z`,

\[
\mathcal S_{X,Y}(z)
=
\sum_{T=Y+1}^{X}\mathcal A_T(z).
\tag{T-23706.2}
\]

Under AWTO every summand is nonpositive.  Therefore

\[
\boxed{
\mathcal S_{X,Y}(z)\le0
\qquad(2\le z\le X).
}
\tag{T-23706.3}
\]

In particular the weighted shell-tail charge of PR #276 satisfies the strongest possible estimate

\[
\boxed{\mathcal B_X=0}
\tag{T-23706.4}
\]

for every dyadic endpoint, rather than merely `X^(o(1))`.

## 3. Completion to RH

PR #276 proves, subject to its declared review boundary,

\[
\mathrm{WSTS}
\Longrightarrow
\sum_{p\le X}
\frac{\log p}{\sqrt p}\log\frac Xp
\ge4\sqrt X-X^{o(1)}
\Longrightarrow
\mathrm{RH}.
\tag{T-23706.5}
\]

Equation (T-23706.4) is stronger than `WSTS`.  Consequently

\[
\boxed{\mathrm{AWTO}\Longrightarrow\mathrm{RH}.}
\tag{T-23706.6}
\]

The same conclusion may be read through the positive endpoint-scale frame of PR #265: every endpoint atom is repaired at zero logarithmic objective cost, and the atom entropies telescope to the sharp parabolic `4 sqrt(X)` score.

## 4. Exact progress toward AWTO

`L-23717` proves

\[
e_T(q)\le0
\qquad
\left(\frac{T-1}{2}<q<T\right).
\tag{T-23706.7}
\]

Hence the complete upper half of every atom is already feasible term by term.  The theorem is not a same-scale prime-spacing problem.  Its positive debt is confined to lower quotient layers and must be transported into the explicit upper-half slack.

The full prime-tail inequality also has the source-complete form

\[
\sum_{m=2}^{T-1}
F_T(m)\Delta L_z(m)
-
\ell_T
\sum_{z\le p<T}\frac{\log p}{\sqrt p}
\le0.
\tag{T-23706.8}
\]

This exposes three exact ledgers which a proof must preserve:

```text
neighboring radical increments L_z(m)-L_z(m-1);
the squarefull/digital reserve log(m/rad(m));
the critical target weight p^(-1/2).
```

## 5. Proposed source-specific proof mechanism

A production proof of AWTO should proceed before any absolute value is taken.

### 5.1 Complete quotient layers

Partition the radical increments by

\[
r=\left\lfloor\frac{T-1}{p}\right\rfloor.
\]

On each layer the endpoint profile is the fixed concave function

\[
F_T(m)=2\ell_T\sqrt m+\eta_Tm.
\]

The upper boundary of every layer is retained explicitly.  The `r=1` layer is already nonpositive by `L-23717`.

### 5.2 Pascal/radical decomposition

Use the exact carry identity

\[
\Gamma_T(p)=\sum_n a_T(n)\beta_{np}
\]

with `a_T>=0`.  For a split `j+(n-j)=n`, the prime set counted by the first carry is a divisor of the squarefree kernel of `binom(n,j)`.  The missing proper-power channels are retained as a positive digital reserve, not discarded through `G_n^(prime)<=G_n`.

The required output is an exact decomposition of (T-23706.8) into:

```text
negative upper-layer stop-loss;
nonnegative p-adic digit reserve;
trace-zero neighboring-radical fluctuation;
strictly lower endpoint atoms.
```

### 5.3 Reflected local square only on the trace-zero residue

The final fluctuation is paired with the reviewed two-frequency physical reflected block of PR #241.  Its complete Hermitian square must be written in the endpoint-atom source coordinates.  Aggregate all-line positivity or the old one-frequency block identification is insufficient.

### 5.4 Lower-scale telescope

Every nonboundary output must have endpoint at most `(T-1)/2`.  A valid proof may establish the stronger recurrence

\[
\mathcal A_T(z)
\le
\max_{U\le(T-1)/2}\mathcal A_U(z)
+\mathcal R_T(z),
\tag{T-23706.9}
\]

with a nonpositive or summable boundary ledger `R_T`.  Since the upper half is already negative, iteration then proves AWTO.

## 6. Why this is a full-problem attack

AWTO is not another global norm equivalent to RH.  It asks for a local theorem on one explicit positive endpoint atom.  It would simultaneously close:

```text
WSTS and the weighted shell-tail route;
Greedy Slack/DCRS through the shared prime-ramp consumer;
the endpoint-scale positive frame;
the ordinary-prime carry minorant;
the square-screw rightmost-zero exponent.
```

The proposal is sharply falsifiable.  One endpoint and one prime cutoff with `A_T(z)>0` rejects AWTO while preserving all exact decompositions.

## 7. Mandatory review tests

1. Reconstruct (L-23717.11) directly from both endpoints.
2. Check the entering endpoint `q=T-1` separately.
3. Enumerate all quotient layers, including divisibility boundaries.
4. Preserve ordinary primes rather than silently replacing `log rad(m)` by `log m`.
5. Retain every proper-power/digital correction.
6. Use the two-frequency reflected physical block, not a scalar analytic square.
7. Reproduce the dyadic and `2/3` fixed-ratio Mertens mutations.
8. Do not promote finite scans to AWTO.

## 8. Status boundary

```text
positive endpoint-scale atoms             imported proposed exact
endpoint residual and shell telescope      proposed exact
radical-tail identity                      proposed exact
upper-half endpoint order                  proposed complete
AWTO below half scale                      OPEN / RH-BEARING
AWTO -> B_X=0 -> WSTS -> RH                 proposed complete
Riemann Hypothesis                         unproved
```
