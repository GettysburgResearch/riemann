# L-28003 — Quarter-balanced extraction and dual scale rigidity

Claim ID: `L-28003`  
Title: Every distant integer leaf can be extracted by a quarter-balanced tree, forcing all balanced-superadditive dual obstructions to be scale-rigid  
Status: **PROPOSED COMPLETE ELEMENTARY LEMMA**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: `L-23810` balanced Farkas dual  
Scope: global geometry of the full quarter-balanced fragmentation cone; no source estimate

## 1. Quarter-balanced trees

A split

\[
p=a+(p-a)
\]

is quarter balanced when

\[
\frac p4\le a,p-a\le\frac{3p}{4}.
\tag{L-28003.1}
\]

Fix integers `n,m` with `n>=2m`. Let `k` be the largest power of two satisfying

\[
2mk\le n.
\tag{L-28003.2}
\]

Then

\[
\boxed{k\ge n/(4m).}
\tag{L-28003.3}
\]

Repeated near-halving splits partition `n` into exactly `k` leaves whose sizes differ by at most one. Every such leaf `p` satisfies

\[
2m\le p\le4m.
\tag{L-28003.4}
\]

For each leaf, make the final split

\[
p=m+(p-m).
\]

Because of (L-28003.4), both children lie between `p/4` and `3p/4`. Thus every split in the tree is quarter balanced, and the terminal forest contains at least `k` copies of the prescribed leaf `m`.

This construction is explicit and deterministic.

## 2. Nonnegativity of dual potentials

Let `phi(1)=0` and assume quarter-balanced superadditivity:

\[
\phi(p)\ge\phi(a)+\phi(p-a)
\tag{L-28003.5}
\]

for every retained split. Near-halving induction gives

\[
\boxed{\phi(n)\ge0\qquad(n\ge1).}
\tag{L-28003.6}
\]

Applying (L-28003.5) down the extraction tree and using (L-28003.6) on every unmarked leaf yields

\[
\boxed{
\phi(n)\ge k\phi(m)
\ge\frac{n}{4m}\phi(m)
\qquad(n\ge2m).}
\tag{L-28003.7}

Equivalently, for the normalized potential

\[
\psi(t)=\phi(t)/t,
\]

\[
\boxed{
\psi(m)\le4\psi(n)
\qquad(n\ge2m).}
\tag{L-28003.8}

## 3. Exact interpretation

`L-23810` says that failure of a nonnegative quarter-balanced fragmentation flow is witnessed by such a superadditive `phi`. Equation (L-28003.8) proves that no dual witness can be concentrated at a remote lower scale while remaining invisible at all doubled ancestors.

Thus every genuine obstruction has two parts:

```text
long-range scale component:
    rigid under repeated doubling and testable by shell tails;

transition component:
    oscillation inside one factor-two annulus.
```

This is the dual counterpart of the first-entrance identity in `L-28001`. Both locate the nontrivial arithmetic in one finite-ratio transition band after all distant generations are recombined.

## 4. Dyadic shell consequence

For a fixed endpoint `X`, put

\[
M_j=\max_{X/2^{j+1}<m\le X/2^j}\frac{\phi(m)}m.
\]

Whenever both shells are nonempty, (L-28003.8), applied to `m` and `2m`, gives

\[
\boxed{M_{j+1}\le4M_j.}
\tag{L-28003.9}
\]

A completion may therefore treat the scale baseline by a dyadic shell telescope and reserve a separate transition certificate for intra-shell oscillation. It may not posit an arbitrary independent obstruction on every scale.

## 5. Relation to factor-five work

PR #269 localizes every negative logarithmic coupling of the opposite-parity source to the ratio band `2m<=n<5m`. The present lemma is independent finite fragmentation geometry and gives a compatible conclusion: all genuinely new dual behavior is finite-ratio. Long-range source transport is not where an unconstrained obstruction can hide.

This does not import the physical Kummer sign into the fragmentation cone. A source-bound transition theorem is still required.

## 6. Exact replay

`X-28001` constructs every extraction tree for

\[
4\le n\le256,\qquad1\le m\le n/2,
\]

and verifies `16,382` exact tree instances, every balance inequality, the marked-leaf count, and (L-28003.3).

## 7. Proof boundary

Closed:

- explicit quarter-balanced extraction trees;
- nonnegativity of balanced-superadditive potentials;
- normalized factor-two scale rigidity;
- dyadic shell consequence.

Open:

- source pairing of the transition component;
- FEP/BCT for the critical source;
- RH.
