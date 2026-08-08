# R-24504 — Pure central-Neumann positivity fails

Claim ID: `R-24504`  
Status: **REFUTED — exact hypothesis-matching finite counterexample**  
Scope: pointwise nonnegativity of the pure central producer only  
Issue: #245  
Date: 2026-08-08

## 1. Claim under test

`L-24523` constructs the unique central-split coefficient vector `A_X(n)`
satisfying

\[
\sum_{n=q}^{X}A_X(n)\chi_n^{\rm c}(q)
=q^{-1/2}\log(X/q)
\qquad(2\le q\le X).
\tag{R-24504.1}
\]

A tempting stronger claim is

\[
A_X(n)\ge0
\qquad(2\le n\le X)
\tag{R-24504.2}
\]

for every endpoint. If true, it would give an exact nonnegative central carry
packing and would close the prime-ramp argument immediately.

## 2. Directed counterexample

At the exact integer endpoint

\[
X=10050
\]

the coefficient at

\[
n=11
\]

is strictly negative. The directed 100-decimal enclosure committed in
`X-24504` is

\[
\boxed{
\begin{aligned}
-0.00000338713025281696432847501869049748021797147658759992104422926727976411941085035547786943176233572
\quad\le A_{10050}(11)\\
\le
-0.00000338713025281696432847501869049748021797147658759992104422926727976411941085035547786943176012845
<0.
\end{aligned}}
\tag{R-24504.3}
\]

The interval is obtained by outward-rounded evaluation of the actual critical
target, exact Möbius values, the exact divergence, and the descending central
fragmentation recurrence. It is not a binary64 sign observation.

Therefore the universal pointwise statement (R-24504.2) is false.

## 3. Exact scope

This counterexample rejects:

```text
pure central splitting
+ exact central-Neumann inversion
+ pointwise coefficient positivity at every endpoint.
```

It does **not** reject:

- the exact central saturation algebra of `L-24523`;
- the Haar potential of `L-24525`;
- subpower negative variation `CNVD`;
- dyadic shell variation `CHSS`;
- positivity after Pascal-cycle or signed-dipole deformation;
- another mixed or adaptive balanced fragmentation producer;
- RH.

In particular the negative coefficient is extremely small, and later endpoints
show dyadically organized negative bands rather than a failure of exact
saturation. The correct theorem is a signed-variation or shell-recombination
statement, not pointwise central positivity.

## 4. Relation to the newer repository state

This exact mutation agrees with the independent route-scope correction on the
binary/ternary fragmentation branch: pure halving is not a universal positive
producer. It also explains why finite positivity through thousands of endpoints
cannot be promoted.

The finite Neumann series terminates because of support descent, but finite
nilpotence does not imply preservation of the positive cone. The reciprocal-zeta
firewall in `L-24523` remains active.

## 5. Mandatory mutation

Every future proof using the central cascade must replay

```text
X=10050,
n=11,
A_X(n)<0.
```

A proof that assumes stagewise monotonicity, treats the residual operator as a
positive-cone contraction, or cites only smaller finite tables fails this
mutation.

## Verification

The checker is

```text
experiments/X-24504-central-neumann-haar/verify.py
```

with verdict

```text
PASS_EXACT_HAAR_AND_DIRECTED_CENTRAL_NEGATIVITY.
```

The checker also replays the exact tent, Haar, potential-recursion, saturation,
and dyadic-shell identities on rational finite controls.
