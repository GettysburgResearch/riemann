# Deep review of the post-Farey replacement: terminal repair and exact balanced frontier

Date: 2026-08-07  
Reviewer: `gpt56-sol`  
Repository: `gfreund123/riemann`  
Frozen replacement head reviewed: `13d32ea7a694acf64f5e55b4a41b9b632cd22dd0`  
Primary files reviewed: `R-15407`, `L-15449`, `L-15450`, `T-15415`, `M-15410`, `X-15416`  
Pinned dependencies inspected: PR #158 exact Heath–Brown packet and Möbius-core decoder; PR #233 finite Möbius resolvent

## Executive verdict

The replacement architecture is materially stronger and more honest than the rejected Farey proposal. The single-row Euler theorem `L-15449` is valid and supplies a genuine unconditional terminal estimate. However the recursive Type-I routing in `L-15450` is not valid on its full stated reserve range because its internal split omits the already-exposed small packet.

The terminal conclusion is nonetheless recoverable. This review adds:

1. `R-15408`, an exact scale counterexample to the frozen Section-3 inference and a minimal `delta<=1/3` repair;
2. `L-15451`, a cleaner direct full-tuple partition that removes same-scale Type-I recursion entirely and closes Heath–Brown terminal rows;
3. an explicit residual divisor expansion that also puts Möbius-resolvent terminal rows into the free-lattice normal form;
4. `O-15403`, showing that after terminal closure at least one balanced destination retains the full fixed-`q_0` Möbius exponent.

The corrected architecture is therefore genuinely reduced to the balanced signed packet problem, but that problem remains RH-bearing and no production BTP(K) inequality is yet supplied.

## Classification

```text
R-15407 frozen Farey refutation                 VERIFIED
surviving analytic-totient/Jordan/Mellin spine VERIFIED at prior scopes
L-15449 one-row terminal Euler theorem          VERIFIED
L-15450 recursive routing as written            REJECTED
terminal conclusion after L-15451 repair        VERIFIED WITH FIXES
Möbius-resolvent terminal closure as written    GAP/BLOCKED
Möbius-resolvent closure after divisor expansion VERIFIED WITH FIXES
X-15416 narrow finite regression                VERIFIED WITH FIXES
BTP(K)                                          GAP/BLOCKED; RH-bearing
BTP(K) => scale contraction => RH               VERIFIED CONDITIONALLY
T-15415 as a completed proof                    GAP/BLOCKED
RH                                              UNPROVED
```

## 1. `L-15449` independently checked

For

\[
F_{A,x}(t)=
{P(\log t)\over\sqrt{At}}W(x-\log(At)),
\]

set

\[
u=x-\log(At),
\qquad
t=e^{x-u}/A.
\]

Then

\[
\int_0^\infty F_{A,x}(t)dt
={e^{x/2}\over A}
\int e^{-u/2}P(x-\log A-u)W(u)du.
\]

If `deg P<=R`, the last polynomial has degree at most `R` in `u`, so the half-pole moments of the high-order safe window annihilate the continuous lattice term exactly.

Differentiation gives

\[
F'_{A,x}(t)=
{1\over\sqrt A t^{3/2}}
\left[P'(\log t)W(u)-{1\over2}P(\log t)W(u)-P(\log t)W'(u)\right].
\]

After the same substitution, the factor `A` cancels from the leading remainder:

\[
\int|F'_{A,x}(t)|dt
\ll_W e^{-x/2}
\max_u(|P(x-\log A-u)|+|P'(x-\log A-u)|).
\]

Euler summation therefore gives the claimed `e^(-x/2)` row bound. The `e^(delta J)` loss appears only when one sums absolutely over all possible small products `A`; it is not intrinsic to one row.

## 2. Exact obstruction in `L-15450`

The frozen recursive argument starts with

\[
N=AUV,
\qquad A\le e^{\delta J+O(1)},
\]

then declares an internal split balanced if `U,V<=e^((1-delta)J)`.

At the allowed reserve

\[
\delta=2/5,
\]

take

\[
(\log A,\log U,\log V)/J=(2/5,3/10,3/10).
\]

Both internal groups pass the frozen test, but the only complete factor splits have scales `(7/10,3/10)` or `(3/10,7/10)`, while `1-delta=3/5`. Hence neither is a legitimate balanced destination.

This is recorded as `R-15408`.

For the repository's preferred `delta=1/5`, a local recursive repair exists: attach `A` to the smaller internal group. More generally this works for `delta<=1/3`. A cleaner replacement is the direct partition below.

## 3. Direct full-tuple repair

Fix `eta in (0,1/2)`, for example `eta=1/4`.

For a complete tuple product

\[
N=w_1\cdots w_r\asymp e^J,
\]

declare an unrestricted coordinate `w_i` terminal iff

\[
N/w_i\le e^{\eta J+O_K(1)}.
\]

There is at most one such coordinate for large `J` because `2eta<1`.

If no terminal coordinate exists, every unrestricted coordinate is at most `e^((1-eta)J+O(1))`; truncated coordinates satisfy the same bound when `1/K<1-eta`. Traverse the full tuple until the first prefix reaches `e^(eta J/2)`. Then both that prefix and its complement are at most

\[
e^{(1-eta/2)J+O_K(1)}.
\]

Thus every source tuple is assigned directly to either:

```text
terminal: one free unrestricted coordinate, complement <= exp(eta J),
or
balanced: both whole-product factors <= exp((1-eta/2)J).
```

No same-scale Type-I complexity recursion is needed. Because the partition is deterministic before estimates, exact signed recombination remains available.

This is `L-15451`.

## 4. Terminal Heath–Brown closure

In the exact Heath–Brown tuple the `d_i` are truncated and `q,r_i` are unrestricted. A terminal coordinate has size at least `e^((1-eta)J)`, so for fixed `K` it cannot be one of the truncated `d_i`.

If the terminal coordinate is `q`, the coefficient is linear in `log q`. If it is an `r_i`, the logarithmic variable `q` lies in the frozen complement and the terminal coefficient is constant. Therefore every terminal row satisfies `L-15449`.

Fixed-order divisor multiplicity and the number of possible complements below `e^(eta J)` give

\[
\sum_A|c_A|\mathcal P_{A,x}
\le e^{(\eta+o_K(1))J}.
\]

Hence

\[
E_{K,term}(J)
\le
\exp[-(1-2\eta-o_K(1))J].
\]

At `eta=1/4`, terminal energy is `e^(-(1/2-o_K(1))J)`.

## 5. Möbius-resolvent terminal repair

The raw PR #233 residual variable is not a unit-weight free coordinate: it carries

\[
r_V(n)=-\sum_{d|n,\,d\le V}\mu(d).
\]

Expand each residual exactly as

\[
n_i=a_i b_i,
\qquad a_i\le V.
\]

Then all `a_i` join the truncated word and every `b_i` is an unrestricted positive integer with exact Möbius sign on `a_i`. A terminal `b_i` satisfies `b_i>>e^((1-eta)J)`, so the residual support condition `a_i b_i>V` is automatic when `1-eta>1/K`. Thus no hidden terminal cutoff remains and `L-15449` applies.

This expansion should be explicit in any promoted terminal theorem.

## 6. Balanced sector retains the RH-bearing source

PR #158's exact decoder shows that fixing the logarithmic Heath–Brown variable at `q_0` leaves exactly `mu(m) log q_0`. At `q_0=2` this is a translated scalar Möbius safe signal.

After terminal closure write

\[
h_{\mu,q_0}=h_{term}+\sum_{\tau\in\mathfrak B_K}h_\tau.
\]

Then

\[
\max_{\tau\in\mathfrak B_K}E_{K,\tau}(J)
\ge
{(\sqrt{E_{\mu,q_0}(J)}-\sqrt{E_{term}(J)})_+^2
\over |\mathfrak B_K|^2}.
\]

Because terminal energy decays exponentially, any positive rightmost-zero exponent must survive in at least one balanced destination. This is `O-15403`.

Consequently BTP(K) is not a routine residual estimate. Somewhere in the balanced system lies the full RH-equivalent Möbius mode.

## 7. Why the current named mechanisms do not yet prove BTP(K)

### Naive tensor factorization

For balanced factor scales `alpha J` and `beta J` with `alpha+beta approximately 1`, a product energy estimate

\[
E_{parent}(J)\lesssim e^{o(J)}E_1(\alpha J)E_2(\beta J)
\]

has tensor exponent `kappa=alpha+beta=1`, not a strict contraction.

### Reusing terminal Euler after absolute values

A fixed complement gets `e^(-J/2)`, but absolute summation over complements of scale `e^(alpha J)` costs `e^(alpha J)`. This is contracting only for `alpha<1/2`; balanced packets necessarily reach the critical half-scale and beyond.

### Product-coordinate versus factor-ratio coordinate

The centered Selberg square lives naturally in an additive/product Hankel coordinate. The target physical Gram is a normal/factor-ratio coordinate. The repository's positive exponential Hankel adjoints do not yet provide a bounded conversion for arbitrary compact signed safe-window packets. Thus listing Selberg square, positive Hankel adjoints, and factor-ratio Gram does not yet constitute the needed intertwiner.

### First-cell mutation

The first positive critical Farey cell is a fixed-ratio Mertens increment. Any claimed BTP proof must imply its square-root scale; otherwise it has spent the actual Möbius cancellation.

## 8. Sharp next target

Do not attack all balanced packet types generically first. Instead:

1. freeze one packet order `K`;
2. trace the exact `q_0=2` Möbius slice through the deterministic full-tuple balanced partition;
3. write its signed normal Gram without total variation;
4. identify the exact lower-scale destination terms and every cutoff/factor-boundary residual;
5. attempt one production recurrence with a strict exponent reserve;
6. mutate the resulting recurrence against the fixed-ratio Mertens first cell.

A success on this packet defeats the hardest scalar obstruction. A failure exposes the exact missing arithmetic mechanism more sharply than a generic BTP formulation.

## 9. Durable status after review

```text
frozen Farey proof                         REJECTED
R-15407 scope correction                   VERIFIED
single terminal Euler row                  VERIFIED
L-15450 recursive routing as written       REJECTED
terminal family after L-15451 repair       VERIFIED WITH FIXES
balanced signed packet theorem BTP(K)      OPEN / RH-BEARING
BTP(K) => rightmost-zero exponent zero     VERIFIED CONDITIONALLY
Riemann Hypothesis                         UNPROVED
```
