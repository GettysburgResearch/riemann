# Global attack — binary–ternary bottom charge and Euler boundary source

**Agent:** `gpt56-pro`  
**Date:** 2026-08-08  
**Branch:** `research/gpt56-pro-280-binary-ternary-bottom-charge`  
**Frozen parent:** PR #277 at `d5be8262c80a1debcf86922b45a4d00a406803f1`  
**Status:** **FULL CONDITIONAL RH PROPOSAL WITH NEW EXACT SOURCE THEOREMS**  
**RH:** **UNPROVEN**

## 1. Why this pass changed direction

The preceding consolidation reduced the elementary route to WSTS, an exact
RH-equivalent prime-sampling scalar.  That was the correct final status, but not
a proof.  The next live producer proposal attempted to prove positivity by
three cumulative Abel integrations.

An exact extension of its checker found

\[
S^{(3)}(15,520)=-91/256,
\]

and

\[
S^{(4)}(15,3559)=-84,999,795/2048.
\]

Thus the ambient fixed-order Abel hierarchy is not the route.  The present pass
returned to the complete arithmetic source and asked what the binary and ternary
splits do to the Euler-aligned reciprocal-zeta coefficients themselves.

That produces two exact collapses which were not visible in the previous
producer formulation.

## 2. First collapse: the entire producer reduces to two bottom coordinates

For

\[
b_2(q)=\mu(q)-\mathbf1_{2\mid q}\mu(q/2),
\]

one has pointwise

\[
\sum_qb_2(q)\chi_{n,j}(q)
=-\mathbf1_{j=1}-\mathbf1_{j=n-1}.
\]

The declared binary and ternary splits have no unit child once `n>=4`.
Consequently their averaged source image is

```text
n=2   -2
n=3   -1
n>=4   0.
```

For every finite target and its exact producer,

\[
\sum_qb_2(q)w(q)=-2A_w(2)-A_w(3).
\]

For the critical target this gives

\[
\boxed{
\mathcal C_2(X)=2A_X(2)+A_X(3)
=-\sum_{q\le X}\frac{b_2(q)}{\sqrt q}\log(X/q).}
\]

Thus the all-row producer positivity problem was stronger than needed.  The
direct Landau consumer needs only eventual nonnegativity, or a subpower positive
part, of one bottom scalar.

## 3. Second collapse: the source matched to both branching scales is compact

Define

\[
\omega_{2,3}
=\mu*(\varepsilon-\delta_2)*(\varepsilon-\delta_3).
\]

Its floor primitive is the compact box

\[
G(x)=1_{x\ge1}-1_{x\ge2}-1_{x\ge3}+1_{x\ge6}.
\]

At scale `m`, the complete pointwise carry wavelet is

\[
Z_{n,m}(j)=G(n/m)-G(j/m)-G((n-j)/m).
\]

For the binary–ternary splits this vanishes whenever

\[
n\ge18m-2.
\]

The infinite balanced packet has therefore become one finite transition source.
No bounded-rank theorem is used; high source rank can remain inside the finite
ratio band.

The inverse and generalized prime data are positive:

\[
a_{2,3}(n)=(v_2(n)+1)(v_3(n)+1)>0,
\]

\[
\Lambda_{2,3}(q)
=\Lambda(q)+(\log2)1_{q=2^r}+(\log3)1_{q=3^r}\ge0.
\]

The actual generalized-prime carry profile is a positive synthesis of the same
compact wavelets, with every cross term retained.  A constant-run argument gives
an absolute carry-feature Schur reserve.

## 4. New proof spine

```text
critical carry target
-> exact binary–ternary producer
-> dyadic b_2 source
-> two-coordinate bottom charge
-> binary–ternary omega_(2,3) Euler sibling
-> compact factor-eighteen carry source
-> positive inverse/generalized-prime synthesis
-> correct two-frequency physical source map
-> boundary recurrence for R_(2,3)
-> ternary contraction to R_2
-> Landau pole exclusion
-> RH.
```

The sole open theorem is `BTEBC`, a production source-image recurrence.  It is
not an ambient positivity theorem.  Every arithmetic source row outside the
factor-eighteen band already vanishes exactly.

## 5. Why the physical theorem is the remaining issue

The carry side now has:

```text
an exact source;
a positive inverse;
positive generalized prime weights;
a finite transition band;
a positive synthesis;
a strict source-specific reserve;
a direct scalar consumer.
```

What remains is the map from PR #241's independent-frequency physical normal
block to that carry source.  A scalar Kummer projection or a one-frequency
vertical integral cannot substitute for this map.

A successful production object must yield

\[
D_{2,3}(X)
\le C\log^A X+\max_{Y\le X/3+C}D_{2,3}(Y),
\]

where `D_(2,3)` is the positive part of the complete source Riesz signal.  Fixed
scale iteration then gives a polylogarithmic envelope and RH.

## 6. Exact replay

The standard-library verifier checks:

```text
third-Abel exact counterexample                 1
fourth-Abel exact counterexample                1
b_2 pointwise source rows                   5,148
bottom-charge synthetic target identities       20
omega_(2,3) floor identities                    201
scaled source wavelet identities            111,055
positive inverse identities                     200
generalized-prime formal identities              200
```

Retained digest:

```text
c044d774fd7e60a71653064e419c6c3ca6d8825ab1a99e679a90c02307abe393
```

The replay proves no physical recurrence or RH.

## 7. Relationship to the other live fronts

- **WSTS / PR #276:** retained as the exact scalar mutation.  It is not imported
  as proved.
- **Factor-five / PR #269:** supplies the closest physical-transition template.
  The present source is instead aligned to both binary and ternary scales.
- **Parity-paired Euler fiber / PR #263:** supplies a finite reconstruction
  strategy for the physical source.
- **Boundary jets / PR #272:** can be tested on the complete compact source rather
  than cellwise fragments.
- **Binary–ternary producer / PR #277:** supplies the exact finite target
  saturation and the bottom coordinates.

## 8. Exact boundary

```text
third/fourth ambient Abel positivity          false
binary–ternary target/producer algebra        inherited proposed exact
dyadic two-coordinate bottom collapse         proposed complete exact
omega_(2,3) compact source                     proposed complete exact
positive inverse and generalized primes       proposed complete exact
carry-feature reserve                         proposed complete
physical BTEBC recurrence                     OPEN / RH-BEARING
BTEBC -> bottom envelope -> RH                 proposed complete
Riemann Hypothesis                            UNPROVEN
```

The branch is a full-problem attack and a reviewable proposal.  It is not an
accepted proof of RH.
