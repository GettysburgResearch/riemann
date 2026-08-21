# R-19801 — The outer-zero tail does not close the square-cell sign

Claim ID: `R-19801`  
Title: An `O(log n)` high-zero radius leaves the entire RH obstruction in one fixed-frequency inner block  
Status: `PROVED SCOPE CORRECTION`  
Authoring agent: `gpt56-pro-09-i`  
Created: 2026-08-01  
Dependencies: `L-19802`; `L-19807`; `L-19808`; Suzuki's weighted Chebyshev criterion  
Scope: final statement of PR #202

## 1. Claim being corrected

The beta square-cell stack proves that all centered zeros with

\[
 |\Re\gamma|\ge An
\]

contribute only `O_A(log n)` to the smoothed screw scalar. It is tempting to
interpret this as leaving a finite arithmetic block that should be accessible by
ordinary zero-density, finite verification, or additional endpoint smoothing.

That interpretation is false. The remaining block is finite at each level, but
it contains every fixed zero for all sufficiently large `n`. A single fixed
off-line zero is enough to produce the full polynomial obstruction.

## 2. Exact obstruction

Let `rho` be an ordinary zeta zero with

\[
 \Re\rho={1\over2}+b,
 \qquad b>0,
\]

and let `z=a+ib` be the corresponding centered parameter. By `L-19808`, its
square-cell multiplier satisfies

\[
 J_{n,\beta}(z)
 =n^{-2iz}(1+O_z(n^{-1})),
\]

so its quartet contributes an oscillatory term of size

\[
 \asymp_z n^{2b}.
\]

For every fixed `A>0`, this zero lies in the inner block

\[
 |\Re z|<An
\]

for all sufficiently large `n`. It is therefore never covered by the
`O_A(log n)` outer radius.

## 3. Why standard refinements cannot finish the proof

### Zero density

Any zero-density theorem that permits even one fixed off-line zero is compatible
with an `n^(2b)` term. Counting almost all zeros correctly does not control this
one mode.

### Finite verified height

A proof-grade verification through a fixed height `H` removes every fixed mode
below `H`, but a hypothetical off-line zero immediately above `H` remains fixed
while `n` tends to infinity. Its polynomial growth eventually dominates every
fixed verification-dependent constant.

### More endpoint zeros

Additional integrations by parts improve `J_n(z)` only when `|Re z|` is on or
above the reciprocal cell-width scale `Theta(n)`. They do not change the
fixed-frequency asymptotic `J_n(z)=n^(-2iz)(1+o(1))`.

### Phase-blind prime estimates

The prime-number theorem and its classical zero-free-region errors permit a
fixed off-line zero. Any bound derived solely from those estimates must also
permit its polynomial contribution and cannot establish a subpolynomial
negative part.

## 4. Literature alignment

Suzuki's weighted Chebyshev theorem already proves that eventual one-sidedness of

\[
 \sum_{m\le x}{\Lambda(m)\over\sqrt m}\log{x\over m}
 -4\sqrt x
\]

is equivalent to RH. The square-screw theorem adds a critical discretization and
complete archimedean normalization; it does not turn the sign assertion into a
weaker arithmetic theorem.

The beta-cell theorem is likewise an exact local averaging variant. Its
remaining estimate

\[
 [\mathcal R_\beta(n)-\mathcal B_\beta(n)]_+=n^{o(1)}
\]

is equivalent to the absence of fixed off-line modes by `L-19802` and
`L-19808`.

## 5. Correct strategic conclusion

The high-zero theorem is still useful: it proves that no infinite spectral tail
or matrix compactness issue remains. But it does **not** make the final block a
routine finite estimate. It localizes the RH content to:

\[
 \boxed{
 \text{exclude every fixed off-line centered frequency from the moving inner
 block}.}
\]

A valid next mechanism must be phase-sensitive and must act on a fixed
frequency. Examples include:

1. a genuine positivity identity for the complete finite prime Riesz mean;
2. a fixed-frequency source/cardinal contradiction;
3. a contour or Hardy argument whose multiplier is nonzero at every point of the
open strip;
4. a proof that the relevant prime-side residual has no exponentially growing
mode.

A smaller tail constant, a longer finite zero table, or a stronger density count
cannot substitute for one of these mechanisms.

## 6. Proof boundary

This refutation does not show that the beta-cell programme is false. It shows
that its final sign estimate is the RH-bearing theorem itself and prevents the
outer-tail result from being presented as an asymptotic closure.