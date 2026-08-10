# R-90227 — A bandwidth-one two-trace Weil certificate cannot close RH

Claim ID: `R-90227`  
Status: **IMPORTED-RESULT ROUTE FIREWALL / PROPOSED EXACT SCOPE SYNTHESIS — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Depends on: Claude Zeta23 Theorem D and §7.5; Zeta23 Lean `PairCeiling`; `L-90228` finite-channel nonamplification  
External sources: `https://www.anthropic.com/research/riemann-zeta`, `https://github.com/anthropics/zeta-23-lean`  
Scope: first two trace moments, bandwidth-one prime-side input, and configuration-by-configuration inertia certificates; no refutation of higher, nonlinear, longer-support, or source-specific methods

## 1. The successful certificate

Claude's finite Gabor compression has, after normalization,

\[
 \operatorname{tr}G_T=(1+o(1))N_T,
\]

and

\[
 \|G_T\|_F^2
 =\left(\frac1{c_1^*}+o(1)\right)N_T,
\]

for the optimal Montgomery--Taylor window, where

\[
 c_1^*=0.753296067856\ldots .
\]

The rank--trace inequality and exact hyperbolic block count then give

\[
 N_0^s(T,2T)
 \ge\left(2-\frac1{c_1^*}-o(1)\right)N_T
 =(0.672500703679\ldots-o(1))N_T.
\]

This is a genuine unconditional theorem.

## 2. Tightness of the linear-algebra seam

The Zeta23 paper and Lean artifact prove that the multiplicity-aware rank--trace
inequality is tight for the data it consumes. Equality is attained by an
orthogonal configuration of on-line atoms and hyperbolic pair blocks at the
relevant scalar equality values.

Therefore no improvement can come from rearranging the same inequality while
retaining only

```text
trace;
Frobenius norm / second trace;
rank of the on-line positive part;
positive index of the off-line part.
```

The missing information is not another Cauchy--Schwarz or Schur manipulation.

## 3. Optimal scalar window at support one

Within the paper's nonnegative scalar-window functional, the variational
problem is solved exactly by

\[
 v_*(s)=\cos(\sqrt2s),
 \qquad |s|\le1/2.
\]

It yields the constant `0.6725007...`; no scalar window using the same
bandwidth-one trace law does better.

The formal artifact additionally contains a `PairCeiling` theorem. For the
specified class of bandwidth-one configuration-by-configuration row
certificates, an explicit near-CUE law limits the certifiable simple-on-line
proportion to approximately

\[
 0.6818287
\]

plus the declared edge-regularity penalty. Thus even a more general row
certificate of that formalized class remains bounded away from one.

## 4. Why merely adding finite channels does not evade the wall

By `L-90228`, one actual off-line pair is represented by one true hyperbolic
zero-coordinate block. Any finite collection of carriers, windows, source
filters, or linear test channels is a pullback of that same block and has
negative index at most one.

Moreover, as the pair approaches the critical line, its unique negative
finite-compression eigenvalue can tend to zero. Hence a larger finite matrix
does not assign a uniform macroscopic spectral cost to the final pair.

Consequently the strategy

```text
add more finite carrier coordinates;
compute only tr and tr^2 with support <=1;
apply a sharper inertia/count inequality;
force the negative index to vanish
```

cannot close RH.

## 5. Arithmetic bandwidth wall

The prime-side diagonal evaluation is unconditional for support parameter
`lambda<=1`. Beyond that range, the off-diagonal prime sums are no longer lower
order under Montgomery--Vaughan alone. Their asymptotic evaluation requires
prime-pair information of Hardy--Littlewood / full pair-correlation strength.

Therefore extending the same moment mechanism past the `67.25%` result is not
a free test-function optimization. It asks for new arithmetic information.
Even full improvement of a proportion is logically weaker than excluding the
last off-line pair.

## 6. Exact impact on live repository routes

### Carrier and finite-Weil packets (`PR #30/#91`)

Claude's theorem validates the power of critical-density Gabor/carrier
compressions. It also proves that their first two aggregate moments are a
proportion certificate, not a full positivity theorem.

### Xi-cardinal kernel (`PR #179/#199`)

The exact global cardinal block detects one off-line pair with fixed value
`-2m`. That direction lies precisely outside what the two-trace proportion
certificate can eliminate. Complete cardinal localization remains a distinct
RH-bearing theorem.

### Critical-neutral scalar (`T-90206/L-90225`)

`CN3` is sensitive to a single off-line zero through a reciprocal-zeta pole.
Knowing that `67.25%`, `99%`, or all but `o(N)` zeros lie on the line does not
control that scalar: one rightmost off-line zero is enough to destroy eventual
one-sign behavior.

## 7. Routes not ruled out

This firewall does not apply to:

1. a direct proof of `CN3` or the adjacent-dyadic Mertens-flux bound;
2. a complete globally conditioned Xi-cardinal synthesis theorem;
3. genuinely nonlinear/tensor observables;
4. cross-moments carrying information not reducible to the first two traces;
5. support beyond one together with a new unconditional prime-correlation
   theorem;
6. an arithmetic theorem that aligns the specific dangerous source with the
   small residual negative sector.

## 8. Correct conclusion

Claude's theorem is a major unconditional advance and a powerful import for
the repository. It does not supply the final RH sign, and its own sharpness
results explain why.

The live problem after import is not

```text
find a slightly better finite trace inequality.
```

It is one of

```text
break bandwidth one with new prime correlations;
localize the exact global off-line cardinal direction uniformly;
prove the one-sided critical-neutral arithmetic scalar directly;
introduce genuinely new non-two-trace information.
```
