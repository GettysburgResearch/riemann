# R-91305 — Independent one-prime child partitions overdraw the parent SHARP source

Claim ID: `R-91305`  
Status: **EXACT FINITE OVERDRAW FIREWALL**  
Created: 2026-08-12  
Depends on: `L-91331`  
RH status: **unproved**

## 1. The tempting but invalid parallelization

For one rough prime `p`, `L-91331` proves the positive canonical child term

\[
 C_p(x)
 =(1-p^{-1/2})w_\Psi(x/p,1),
\]

where

\[
 w_\Psi(x,1)=4\sqrt x-3.
\]

It is tempting to allocate `C_p(x)` independently for every active least-prime
branch. This would require

\[
 \sum_p C_p(x)\le w_\Psi(x,1).
\tag{R-91305.1}
\]

That inequality is false by a large exact margin.

## 2. Exact witness at `x=10000`

Take the fifteen primes

\[
 \mathcal P=
 \{67,71,73,79,83,89,97,101,103,107,109,113,127,131,137\}.
\]

For every `p in P`,

\[
 8<\sqrt p<12.
\]

Hence

\[
 1-p^{-1/2}>\frac78
\]

and

\[
 w_\Psi(10000/p,1)
 =\frac{400}{\sqrt p}-3
 >\frac{100}{3}-3
 =\frac{91}{3}.
\]

Therefore each canonical child satisfies

\[
 C_p(10000)>
 \frac78\frac{91}{3}
 =\frac{637}{24}.
\]

Summing only these fifteen branches,

\[
\boxed{
 \sum_{p\in\mathcal P}C_p(10000)
 >15\frac{637}{24}
 =\frac{9555}{24}
 >397
 =w_\Psi(10000,1).
}
\tag{R-91305.2
}

No floating approximation is used.

## 3. Meaning

The one-prime identity is a partition only after the source packet assigned to
that prime has already been separated from the parent source. The same parent
atom cannot be fed independently into every prime branch.

Thus none of the following is valid:

```text
one-prime positivity for every p
-> sum all canonical p-children;
branch-local Schur reserve for every p
-> reuse the same diagonal port for every p;
pathwise coefficient below one
-> parallel child weights sum below one.
```

This is the source-mass analogue of the scalar-port nontensorization in
`R-91303`.

## 4. Correct remaining theorem

A valid global reset must first produce an exact positive disintegration

\[
 \mu^{\rm parent}_\Psi
 =\mu_0+\sum_p\mu_p
\]

with disjoint least-prime source labels. Only then may `L-91331` be applied to
`mu_p` on branch `p`.

The sum-before-quantize theorem `L-91329` and branching consumer `T-91302` are
built for precisely this structure.

```text
one-prime canonical-child identity                RETAINED EXACT
independent parallel application                   REFUTED EXACTLY
parallel source-port reuse                         FORBIDDEN
least-prime positive source disintegration         OPEN / LOAD BEARING
Riemann Hypothesis                                 UNPROVEN
```
