# Full-problem attack: reciprocal eta, product six, and the Mersenne boundary

Agent: `gpt56-pro-09-v`  
Date: 2026-08-08  
Parent: PR #280  
Status: **NEW EXACT GLOBAL REDUCTIONS + SERIOUS CONDITIONAL PROPOSAL; RH UNPROVED**

## 1. Why this pass changed direction

The central-cascade route was attractive because one and two positive stages
already recover a large fraction of the sharp carry constant.  Its proposed
all-stage justification, however, treated the continuum cascade as positive and
monotone and assigned every later sign defect to the finite lattice shift.

That diagnosis is false.  The first continuum defect occurs before any lattice
commutator, at the two ordered factorizations of six.

Rather than abandon the cascade, this pass identifies its complete all-stage
source and discovers that the source has an unexpectedly sparse carry image.

## 2. Exact product-six mutation

In logarithmic coordinates the central operator is convolution by

\[
 a(n)=(-1)^n\mathbf1_{n\ge2}.
\]

For

\[
 F(t)=t e^{t/2}\mathbf1_{t\ge0},
\]

the second iterate satisfies, exactly on `log6<t<log8`,

\[
 \mathcal U^2F(t)=F(t-\log4)-2F(t-\log6).
\]

Its right derivative at `log6` is

\[
 \sqrt{3/2}\left(1+\frac12\log(3/2)\right)-2<0.
\]

Thus the continuum residual has already lost monotonicity.  The coefficient
`-2` is the complete ordered ledger

```text
6=2*3=3*2.
```

The one-pass and two-pass finite packings survive.  The all-order monotonicity
argument does not.

## 3. The full cascade is exactly reciprocal eta

The coefficient sequence is

\[
 a=\varepsilon-e,
 \qquad e(n)=(-1)^{n-1},
\]

so its Dirichlet series is `1-eta(s)`.  The coefficientwise Neumann resolvent is
finite at every integer and equals

\[
 \sum_{j\ge0}a^{*j}=e^{-1}.
\]

Hence

\[
 \sum_{n\ge1}{b(n)\over n^s}={1\over\eta(s)}
 ={1\over(1-2^{1-s})\zeta(s)}.
\]

Explicitly, if `n=2^r m` with `m` odd,

\[
 b(n)=
 \begin{cases}
 \mu(m),&r=0,\\
 2^{r-1}\mu(m),&r\ge1.
 \end{cases}
\]

The cascade has therefore not avoided the balanced Möbius obstruction.  It has
chosen the particularly structured reciprocal-eta gauge of it.

## 4. Complete carry collapse

Although the coefficients `b(n)` are signed, their divisor-prefix image is
literal dyadic arithmetic:

\[
 \sum_{q\le x}b(q)\lfloor x/q\rfloor
 =2^{\lfloor\log_2x\rfloor+1}-1.
\]

Therefore the atomized carry image is

\[
 Y_n(j)=D(n)-D(j)-D(n-j),
 \qquad D(x)=2^{\lfloor\log_2x\rfloor+1}-1.
\]

For `P<=n<2P`, it is positive in the central window and negative only on the two
endpoint wings.  The average row is

\[
 \overline Y_{P+r}
 ={(2P-1)((P-1)/3-r)\over P+r+1}.
\]

This exposes the exact ternary transition inside every dyadic block.

## 5. Stronger collapse on the central split

At `j=floor(n/2)`, the complete reciprocal-eta source equals

\[
 y_n=1
\]

for every parent except

\[
 n=2^r-1,
\]

where

\[
 y_n=1-2^{r-1}.
\]

Thus the dense Möbius source sees only a sparse Mersenne boundary.  For the full
finite central cascade,

\[
 \mathcal R_\eta(X)
 =\sum_jr_j(2)
  -\sum_j\sum_{P=2^a}
   P[r_j(2P-1)-r_j(2P)].
\]

The complete RH-bearing Riesz coordinate has been reduced to `O(log^2 X)`
explicit stage/scale boundary rows.

This does not prove the coordinate is small.  It radically changes what a
proof must estimate.

## 6. Reflected eta square

The generalized Selberg identity applies directly to `eta`.  With independent
frequencies `t,u`, subtracting the individual identities from the product
identity gives

\[
 C_\eta(t,-u)-C_\eta(t)-C_\eta(-u)
 =2\Lambda_{\eta,t}*\Lambda_{\eta,-u}.
\]

On the diagonal this is

\[
 2|\eta'/\eta|^2.
\]

The generalized prime coefficients are ordinary `Lambda` away from the powers
of two and equal `(1-2^r)log2` at `2^r`.  The entire discrepancy is a dyadic
boundary source.

The two-frequency physical adapter of PR #241 can therefore be reused without
the false one-frequency/local-block identification.

## 7. New full proposal

`T-28001` defines the Reflected Mersenne Boundary Recurrence (`RMBR`).  Its
production object is required to retain:

- the complete reciprocal-eta source;
- every Mersenne row and exact dyadic charge;
- all ordered binary--ternary overlaps;
- the independent-frequency reflected block;
- high-order Euler closure of rows with a free macroscopic lattice variable;
- signed recombination before norms;
- a nonnegative reflected reserve;
- strict lower-scale destinations;
- the fixed-ratio Mertens mutation.

A recurrence with loss exponent tending to zero gives a subpower bound for the
reciprocal-eta Riesz coordinate, hence RH.

## 8. What is genuinely new

This is not another claim that a generic balanced packet contracts.  The source
has been compressed twice:

```text
complete central cascade
  -> explicit reciprocal-eta coefficient state
  -> exact dyadic carry staircase
  -> only Mersenne boundary rows on central splits.
```

The first product-six failure and every later dyadic boundary are explicit.
The proposal is therefore substantially more falsifiable than the original
DCCS wording.

## 9. Honest boundary

```text
one-pass 4 log(2) theorem                   pushed / proposed exact
product-six continuum refutation            proposed exact
reciprocal-eta resolvent                     proposed exact
dyadic staircase carry image                 proposed exact
Mersenne boundary telescope                  proposed exact
reflected eta Hermitian identity              proposed exact
RMBR sparse boundary recurrence               OPEN / RH-BEARING
RMBR -> RH                                   complete conditional composition
Riemann Hypothesis                           UNPROVED
```

The branch should be reviewed as a corrected global research proposal, not as an
accepted proof of RH.
