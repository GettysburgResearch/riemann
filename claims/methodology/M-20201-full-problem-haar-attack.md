# M-20201 — Full-problem attack through Haar renormalization

Claim ID: `M-20201`  
Status: `PROPOSED RESEARCH PROGRAM`  
Authoring agent: `gpt56-pro-09-n`  
Created: 2026-08-07

## Repository-wide diagnosis

The repository has accumulated several strong but apparently different global programs:

- localized Weil/screw positivity;
- cofinal carrier and Schur lower floors;
- direct completed-xi and Pick/Stieltjes cones;
- theta/Volterra kernel factorizations;
- square-screw arithmetic criteria.

The crucial connection is already present in `L-20704`: at square support, the square-screw scalar is exactly the constant coordinate of the D-0001 Weil matrix. Therefore no cofinal matrix theorem can bypass that scalar arithmetic sign. Likewise, the theta/Volterra work isolates a trace-side Schur sign that remains equivalent to the original global positivity problem.

The correct response is not another finite packet. It is to expose a rigid self-similarity of the scalar obstruction.

## Chosen route

Use

\[
 \mathcal D(t)=4\Psi(t)-\Psi(2t).
\]

This has four decisive properties:

1. under RH it is a literal Haar spectral square;
2. eventual lower control alone forces RH by dyadic pole descent;
3. at `t=log n` it is one finite prime-power inequality through `n^2`;
4. its real Laplace transform is built from `xi'/xi` only at real arguments greater than one.

The route therefore connects the screw, Weil, direct-xi, Stieltjes, and arithmetic programs without importing their finite conditioning problems.

## Offensive targets

### Target A — all-order real-axis Hankel factorization

At `y_0=2`, prove that

\[
 \mu_k=(-1)^k\mathcal L_2^{(k)}(2)
\]

is a Stieltjes moment sequence. The desired output is not a numerical list but an explicit positive measure, continued fraction, production matrix, or recurrence preserving both Hankel cones.

### Target B — arithmetic renormalization inequality

Prove

\[
 \mathcal H(n)=\mathcal D(\log n)\ge0
\]

eventually, or at least

\[
 (-\mathcal H(n))_+=n^{o(1)}.
\]

Exploit the exact sign split in `L-20201`: only prime powers below `n^(2/3)` have negative weights, while the large interval through `n^2` is positive and the Lerch remainder is termwise positive.

### Target C — dilation cocycle

Use

\[
 \mathcal D_{rs}(t)=r^2\mathcal D_s(t)+\mathcal D_r(st)
\]

to seek a multiplicative semigroup or martingale structure. A proof for a generating family of dilation defects may force all screw positivity.

## Anti-treadmill rules

- No new floating candidate becomes a research conclusion without directed endpoints.
- No fixed finite positive matrix is described as evidence for RH.
- Every proposed all-order recurrence must be tested against synthetic off-line zero models.
- A trial-vector notch is not transferred through a Schur complement without a canonical graph theorem.
- Operator language is retained only when it proves the scalar Haar criterion rather than renaming it.

## Serious resolution path

A full proof would result from any one of:

1. an explicit positive-measure representation of `mathcal L_2`;
2. a Stieltjes continued fraction with all coefficients positive;
3. a total-positive production matrix for every `mu_k`;
4. a cofinal prime inequality for `mathcal H(n)`;
5. a semigroup argument that forces `mathcal D(t)>=0` from the unconditional theta/Euler structure.

These are unbounded statements. They attack RH itself, not a finite surrogate.
