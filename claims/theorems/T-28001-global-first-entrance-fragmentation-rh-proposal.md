# T-28001 — Global first-entrance fragmentation proposal for RH

Claim ID: `T-28001`  
Title: First-entrance positivity of the complete critical Möbius source would produce a sharp nonnegative balanced carry flow and prove RH  
Status: **SERIOUS FULL CONDITIONAL RH PROPOSAL — ONE GLOBAL TRANSITION THEOREM OPEN**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Parent: PR #277 at `d5be8262c80a1debcf86922b45a4d00a406803f1`  
Dependencies: `L-28001`--`L-28003`, `R-28001`; PR #277 `L-23814/T-23804`; source-pinned square-screw/Landau transfer  
Scope: full elementary carry/fragmentation route

## 1. Step back: the common global obstruction

The live repository has developed several gauges of the same reciprocal-zeta arithmetic:

```text
critical carry target and Möbius divergence;
binary–ternary balanced fragmentation;
cycle-optimized capacity debt;
weighted shell-tail stability;
opposite-parity factor-five source;
bottom charge and boundary commutator;
source-specific reflected normal Gram.
```

The exact failures have a common cause: they take a sign before complete generations are recombined.

```text
generic cluster norm                 false;
bounded face rank                    false;
monotone positive-part cover         false;
conditional-Hankel kernel            false;
fixed Abel orders 1,2,3,4            false.
```

The present proposal changes the order of operations. It retains the full critical source, propagates every higher generation through a conservative fragmentation ancestry, stops only on a finite-ratio transition annulus, and takes the first sign there.

## 2. Critical source and frozen ancestry

Let

\[
w_X(q)=q^{-1/2}\log(X/q),
\]

and let `R_X` be its exact multiple-Möbius node divergence from `L-23810`. Use the frozen half-binary/half-ternary producer of PR #277.

`L-28001` turns this producer into a descending Markov chain `Z_t` and proves

\[
nA_X(n)=\sum_{m=n}^{X}mR_X(m)h_n(m).
\tag{T-28001.1}
\]

For the first entrance below `2n`, define

\[
\Sigma_{X,n}(p)
=\sum_{m=n}^{X}mR_X(m)
\mathbb P_m(Z_{\tau_n}=p),
\qquad n\le p<\min(2n,X+1).
\tag{T-28001.2}
\]

Then exactly

\[
\boxed{
nA_X(n)=
\sum_{p=n}^{\min(2n-1,X)}
\Sigma_{X,n}(p)h_n(p).}
\tag{T-28001.3}
\]

No source term from scale `m>=2n` remains outside `Sigma`.

## 3. Sole proposed theorem — Global First-Entrance Positivity (`GFEP`)

The required theorem is

\[
\boxed{
\operatorname{GFEP}:
\quad
\Sigma_{X,n}(p)\ge0
\quad
\text{for every }X\ge2,
\ 2\le n\le p<\min(2n,X+1).
}
\tag{T-28001.4}

This is an all-scale, source-specific theorem. It is not a finite scan, an ambient operator inequality, or a termwise Möbius estimate.

`L-28002` proves GFEP unconditionally on the full top fifth:

\[
n\ge\lceil X/5\rceil.
\tag{T-28001.5}
\]

Thus the open theorem begins strictly below the first factor-five boundary. Every higher source generation entering that region has already been coupled to its descendants.

## 4. GFEP gives a nonnegative exact flow

Every hitting probability in (T-28001.3) is nonnegative. Therefore GFEP gives

\[
A_X(n)\ge0
\qquad(2\le n\le X).
\tag{T-28001.6}

The split coefficients

\[
d_{n,a_2(n)}=d_{n,a_3(n)}=A_X(n)/2
\]

are then a nonnegative quarter-balanced flow with the exact critical carry loads. No positive-part repair, boundary oversupport, or generic Farkas existence step remains.

PR #277 `L-23814` proves from the exact terminal carry interval that

\[
\sum_{n=2}^{X}A_X(n)\sqrt n=O((\log X)^2).
\tag{T-28001.7}
\]

Hence the complete prime-power ramp satisfies

\[
\boxed{
\sum_{p^a\le X}\frac{\Lambda(p^a)}{\sqrt{p^a}}
\log\frac{X}{p^a}
\ge4\sqrt X-O((\log X)^C).
}
\tag{T-28001.8}

The exact cycle-debt of PR #272 is zero; the profit/debt and half-moment firewalls of PR #277 are automatically controlled.

## 5. Prime ramp to RH

At `X=N^2`, the source-pinned square-screw identity converts (T-28001.8) into a subpolynomial one-sided envelope for the screw statistic. The reviewed square-mesh interpolation and Landau pole-exclusion mechanism then rule out every zeta zero with real part greater than `1/2`. Functional-equation symmetry gives RH.

Thus

```text
GFEP
-> nonnegative exact balanced fragmentation
-> O(log^2 X) capacity variation
-> sharp complete prime-power ramp
-> square-screw/Landau
-> RH.
```

No RH claim is made while GFEP remains open.

## 6. Why GFEP attacks the full problem rather than a shrinking lemma

GFEP is a global recombination theorem. For each target node it includes:

- every Möbius quotient layer through the endpoint `X`;
- every binary and ternary ancestor;
- every repeated central child;
- every path that skips below the target;
- all long-range shell interactions;
- the complete reciprocal-zeta phase.

Only after those objects are summed does the theorem ask for a sign in `[n,2n)`. It therefore avoids every exact counterfamily used against finite face counting, fixed Abel kernels, and monotone covers.

The factor-two annulus is not an arbitrary narrowing. `L-28003` proves independently that every dual obstruction to the full quarter-balanced fragmentation cone is scale-rigid outside a doubled transition band.

## 7. Concrete attack on GFEP

A proof object should use three layers.

### Layer A — positive base

Use `L-28002`:

\[
R_X(m)\ge0\quad(m\ge X/5).
\]

This supplies a strict positive starting measure before recursion.

### Layer B — complete first-entrance transport

For `n<X/5`, propagate the signed size source from every `m>=2n` through the exact stochastic kernel before splitting positive and negative parts. The proof should seek a recursion

\[
\Sigma_{X,n}
=\mathcal P_{X,n}
+\sum_\beta T_\beta\Sigma_{Y_\beta,n_\beta},
\tag{T-28001.9}
\]

with `mathcal P>=0`, lower endpoints `Y_beta<X`, and no total variation before recombination.

### Layer C — transition certificate

The remaining ratio band is where the strongest parallel work meets:

- PR #269 localizes every negative opposite-parity logarithmic coupling to a finite factor-five transition band;
- PR #272 supplies the complete Pascal-cycle basis and exact negative-capacity dual;
- PR #274 supplies proper-power-neutral squarefree collector atoms;
- PR #240 supplies the weighted shell-tail scalar firewall;
- PR #241 supplies the correct independent-frequency physical block if a reflected energy certificate is used.

A valid proof may combine these, but it must emit the exact map into `Sigma`; correspondence of positive Grams is insufficient.

## 8. Stronger and weaker acceptable forms

Pointwise GFEP is sufficient, not logically necessary. An acceptable weaker certificate may prove directly

\[
\sum_p\Sigma_{X,n}(p)h_n(p)\ge0
\tag{T-28001.10}
\]

provided it retains the exact first-entrance source and does not simply rename `A_X(n)>=0`.

A stronger certificate may construct a coupling that sends every negative entrance parcel to a positive top-fifth ancestor while preserving the sibling constraint of the fragmentation flow.

## 9. Exact reconnaissance

The exact checker proves the stochastic, Green, cut, entrance, and balanced-extraction identities. Separate floating reconnaissance found

```text
Sigma_(X,n)(p)>0
for every tested n,p at every endpoint through X=10,000.
```

The minimum in those scans occurs at the final top-band cells and is of the expected order `X^-1/2`. This is discovery evidence only and is not promoted to GFEP.

## 10. Automatic rejection

Reject a claimed completion if it:

- takes positive parts before first-entrance recombination;
- replaces the four-child sibling-coupled kernel by an arbitrary Markov chain;
- omits paths that jump below `n`;
- uses fixed-order Abel positivity;
- treats finite GFEP scans as an all-scale theorem;
- loses the `2/3` Mertens or same-sign Möbius-cube mutation;
- substitutes one-frequency `H(z)^2` for the independent-frequency normal block;
- assumes the weighted shell-tail theorem, producer positivity, or RH under another name.

## 11. Exact boundary

```text
size-biased Markov/Green algebra             PROPOSED COMPLETE EXACT
first-entrance factor-two localization       PROPOSED COMPLETE EXACT
critical source top-fifth positivity         PROPOSED COMPLETE
quarter-balanced dual scale rigidity         PROPOSED COMPLETE
fixed Abel orders 1--4                       REFUTED EXACTLY
GFEP on top fifth                            PROVED CONDITIONALLY ON L-28002 REVIEW
GFEP below top fifth                         OPEN / RH-BEARING
GFEP -> sharp prime ramp -> RH               COMPLETE CONDITIONAL PROPOSAL
Riemann Hypothesis                           UNPROVED
```
