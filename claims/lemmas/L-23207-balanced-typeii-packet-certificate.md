# L-23207 — Source-specific balanced Type-II packet certificate

Claim ID: `L-23207`  
Title: The corrected proposal reduces RH to a signed balanced Type-II recurrence on the actual finite Heath--Brown packet vector  
Status: **PROPOSED CERTIFICATE INTERFACE — `BTP(K)` OPEN**  
Authoring agent: `gpt56-pro-21`  
Created: 2026-08-07  
Issue: #232  
Dependencies: PR #158 `L-15151/L-15153/L-15155/L-15156/L-15157`; `L-23206`  
Scope: the sole open arithmetic family in the corrected proposal

## 1. Exact balanced sources

Fix `K>=6`, the safe window

\[
H_K=H^{[K+1]},
\]

and the reserve

\[
\delta=\frac15.
\]

Apply the exact finite Heath--Brown identity of `L-15156` to the complete
von-Mangoldt signal on block `[J,J+1]`.  Retain every tuple coefficient,
truncation, support boundary, and transition source.

Use the corrected source reduction `L-23206`.  All rows assigned to the same
balanced destination `tau` are recombined with their exact signed binomial and
Möbius coefficients before any absolute value.  The resulting source function
has the form

\[
Q_{K,\tau,J}(x)
=
\sum_{(a,b)\in\mathcal M_{K,\tau,J}}
\frac{c_{K,\tau,J}(a,b)}{\sqrt{ab}}
H_K(x-\log(ab)),
\tag{L-23207.1}
\]

where the finite manifest is source bound and

\[
e^{\delta J-O_K(1)}
\le a,b\le
e^{(1-\delta)J+O_K(1)}.
\tag{L-23207.2}
\]

The packet energy is

\[
\boxed{
E_{K,\tau}(J)
=
\int_J^{J+1}|Q_{K,\tau,J}(x)|^2dx.
}
\tag{L-23207.3}
\]

This is the adjoint/normal factor-ratio Gram orientation.  It may not be
replaced by a product-dilation form or by the total variation of the tuple
coefficients.

## 2. Complete balanced vector

Let `mathfrak B_K` be the finite dictionary of balanced destination types at
order `K`, including

```text
identity indices and signed binomial vector
ordered factor words
first-crossing position
factor-scale intervals
Möbius/divisor/logarithmic coefficient words
all truncation and transition boundaries
null companions, if independently certified
auxiliary energy destination
```

and put

\[
M_K(X)
=
1+\max_{\tau\in\mathfrak B_K}
  \max_{0\le J\le X}E_{K,\tau}(J).
\tag{L-23207.4}
\]

`L-23206` proves that every nonbalanced row is either an exponentially small
terminal row or a finite same-scale source reduction into this dictionary and
strictly lower complexity.  It does not estimate any member of
`mathfrak B_K`.

## 3. The balanced packet theorem `BTP(K)`

A **linear balanced Type-II certificate** proves, for every balanced type,

\[
\boxed{
E_{K,\tau}(J)
\le
\exp\{(\varepsilon_K+o_K(1))J\}
\left[
1+
\max_{\upsilon\in\mathfrak B_K}
\max_{u\le(1-\delta)J+O_K(1)}
E_{K,\upsilon}(u)
\right].
}
\tag{L-23207.5}
\]

A tensor certificate may instead prove

\[
E_{K,\tau}(J)
\le
\exp\{(\varepsilon_K+o_K(1))J\}
\prod_s
\left[1+M_K(\alpha_{K,s}J+O_K(1))\right]^{\theta_{K,s}},
\tag{L-23207.6}
\]

with

\[
\kappa_K
=
\sum_s\theta_{K,s}\alpha_{K,s}<1.
\tag{L-23207.7}
\]

The all-order theorem `BTP` is:

\[
\boxed{
\varepsilon_K\longrightarrow0
}
\tag{L-23207.8}
\]

along an unbounded sequence of orders in the linear system, or

\[
\boxed{
\frac{\varepsilon_K}{1-\kappa_K}\longrightarrow0
}
\tag{L-23207.9}
\]

in the tensor system.

No estimate of this strength is proved in the present branch.

## 4. Production certificate

For each retained order and block, a fail-closed proof object must include:

```text
safe-window and normalization digests
complete Heath--Brown tuple manifest
all exact tuple coefficients and multiplicities
signed destination recombination digest
factor intervals and product-support checks
complete cutoff and transition ledger
normal-Gram packet matrices or exact source contractions
all auxiliary energy identifiers
linear/tensor recurrence coefficients
strict scale destinations
epsilon_K and, if applicable, kappa_K
```

A consumer must reject:

- absolute values before signed destination recombination;
- omission of a tuple, prime-power layer, cutoff, or transition source;
- a product-dilation/factor-ratio substitution;
- a generic operator estimate unrelated to the actual coefficient vector;
- a lower-scale destination above `(1-delta)J+O_K(1)`;
- inference from finitely many orders to (L-23207.8).

## 5. Permitted analytic mechanisms

A proof of `BTP(K)` may use, provided every source map is explicit:

1. a signed common-cell Type-II dispersion inequality;
2. multiplicative large-sieve estimates after complete signed recombination;
3. a coupled vector/matrix Selberg equation retaining all packet cross terms;
4. Ramanujan or Farey orthogonality for the actual Möbius/divisor vectors;
5. another source-specific bilinear contraction.

The scalar Selberg identity for the aggregate prime measure does not, by itself,
control the sum of packet self-energies.

## 6. Mertens audit

The first Farey cell of PR #229 is exactly a fixed complex multiple of

\[
M(D)-M(\lfloor2D/3\rfloor),
\]

and `L-23202` proves that its finite geometric differences remain
RH-equivalent.  This is a human and theorem-level audit of `BTP`: a proposed
balanced contraction that forgets the coherent Möbius vector cannot be valid.

A machine-checkable first-cell mutation is required only when an explicit
source map from the balanced proof object to that scalar coordinate is exported.
The corrected proposal does not pretend that such a decoder already exists.

## 7. Why this is the sole remaining arithmetic hinge

`L-23206` supplies exact source routing for all reduced Type-I rows and closes
the terminal family by Euler cancellation.  The high-order null quotient and
prime/full-von-Mangoldt normal bridge are inherited from PR #158.  Therefore,
after exact packet assembly, every unresolved source lies in
`mathfrak B_K`.

The final scale-contraction implication from `BTP` to RH is stated in
`T-23202`.

## 8. Proof boundary

Closed here:

- the source-specific balanced packet definition;
- the complete certificate schema;
- the exact rate needed by scale contraction;
- the distinction between valid coupled mechanisms and the rejected generic
  operator/aggregate-Selberg shortcuts.

Open:

- construction of `BTP(K)` for any unbounded sequence of orders;
- the vanishing coefficient rate;
- RH.