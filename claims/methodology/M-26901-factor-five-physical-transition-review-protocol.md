# M-26901 — Fail-closed review protocol for the factor-five physical transition certificate

Claim ID: `M-26901`  
Title: Exact production and adversarial-review schema for the sole remaining physical transference theorem  
Status: **METHODOLOGY / REQUIRED CERTIFICATE CONTRACT**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Dependencies: `L-26204`, `L-26901`--`L-26903`, `R-26901`; PR #241 `L-9518`  
Scope: review protocol only; no transference theorem or RH conclusion

## 1. Frozen mathematical boundary

The following source-side statements are the inputs to a production review:

```text
L-26204  complete fixed-q0=2 two-frequency source matrix;
L-26901  exact pointwise omega2 wavelet and factor-five localization;
L-26902  uniform ordinary-Kummer carry Schur reserve;
L-26903  positive inverse, generalized primes, positive wavelet synthesis,
          and reserve transfer to the actual carry source;
R-26901  signed odd-column load is lower order but the odd target is RH-bearing;
L-26202  DSS/Riesz Mellin consumer;
L-26203  two-charge Green representation.
```

No reviewer should be asked to re-prove these while reviewing the physical
transference. They should be checked first at their declared scopes and then
frozen by exact commit SHA.

The sole production theorem is:

```text
physical independent-frequency quotient cells 2/3/4
-> generalized-prime carry Gram
-> retained strict source reserve
-> DSS or subexponential omega2 shell energy.
```

## 2. Required source manifest

For every production endpoint/block, the certificate must export a
duplicate-free source manifest containing:

1. every original Möbius atom;
2. its `2`-adic siblings at scales `1,2,4` with coefficients
   ```text
   1, -3/2, 1/2;
   ```
3. every reflected copy in the second frequency leg;
4. all quotient-cell labels and transition/cutoff labels;
5. the exact generalized-prime weight
   ```text
   Lambda_omega(q)
    =Lambda(q)+(log2)(1+2^-r)1_(q=2^r);
   ```
6. all endpoint and noncoprime chains;
7. the fixed-ratio `2/3` Mertens mutation.

A source atom may be merged only with another atom having exactly the same
physical destination, frequency phases, cutoff state, and coefficient.

## 3. Physical matrix object

For each factor-five transition cell, the producer must emit a Hermitian matrix

\[
G^{\rm phys}_{J,\tau}
\]

constructed from PR #241's independent-frequency kernel

\[
\Phi_{J,\alpha}(t-s).
\]

It must include the four dyadic translate channels

```text
(m,n), (2m,n), (m,2n), (2m,2n)
```

and the further `omega2` sibling introduced by

```text
I-(1/2)tau_(log2).
```

The matrix must be assembled before interval widening, Schur elimination,
positive parts, or absolute values.

The certificate must also emit the direct arithmetic replay

\[
\sum_{u,v}{\omega_2(u)\omega_2(v)\over\sqrt{uv}}
K_J(\log u,\log v)
\]

and show exact equality with the two-frequency assembly.

## 4. Carry matrix object

For the same source manifest, emit the pointwise carry vectors

\[
Z_{n,m}(j)=g_m(n)-g_m(j)-g_m(n-j)
\]

and the generalized-prime profile

\[
P_n=\sum_{m\le n}a_\omega(m)\log m\,Z_{n,m}.
\]

The complete carry Gram is

\[
G^{\rm car}_{n}(m,r)
={1\over n+1}\sum_{j=0}^{n}Z_{n,m}(j)Z_{n,r}(j).
\]

Every cross term in the positive synthesis must be retained. Rowwise use of
only the diagonal reserves in `L-26902/L-26903` is insufficient unless the
source map proves that the omitted cross sector is nonnegative.

## 5. Exact transference map

The production theorem must provide an explicit linear map

\[
S_{J,\tau}:
\mathcal H_{\rm phys}\longrightarrow\mathcal H_{\rm car}
\]

or its adjoint, with one exact source commutative diagram. At minimum it must
prove, on the licensed source subspace,

\[
\boxed{
S^*G^{\rm car}S
\preceq C_{J,\tau}G^{\rm phys}
}
\tag{M-26901.1}
\]

and a reverse inequality on the retained source coordinate sufficient to
transport the carry Schur reserve:

\[
\boxed{
G^{\rm phys}_{\rm res}
\preceq C'_{J,\tau}S^*G^{\rm car}_{\rm res}S
 +G^{\rm lower}_{J,\tau}.
}
\tag{M-26901.2}

The allowed condition numbers must satisfy the declared recurrence budget. A
fixed power `X^c` is not acceptable. Polylogarithmic conditioning, a uniform
constant, or an explicitly vanishing exponent is acceptable if the final
consumer calculation is written out.

A claim that the two spaces are “morally the same source” is not a map.

## 6. Factor-five partition

Every source row must be assigned before estimation to exactly one of:

```text
inner positive:       m<=n<2m;
transition:           2m<=n<5m;
far nonnegative:      n>=5m;
finite boundary:      n<210;
strict lower delay:   declared consumer scale.
```

The `n>=5m` family may be moved to the positive side only through the exact
Kummer sign theorem of `L-26901`, with its source map intact. It may not be
silently removed from the physical matrix.

The finite boundary is finite in the row variable, but not automatically finite
in every packet coordinate. Its complete source list and direct matrix replay
are required.

## 7. Mandatory Schur reserve

After all declared positive/lower sectors are assembled, the actual physical
transition matrix must be written as

\[
\begin{pmatrix}
G&C^*\\
C&D
\end{pmatrix},
\qquad D\succ0,
\]

and the certificate must prove

\[
\boxed{
G-C^*D^{-1}C
\succeq\kappa_{J,\tau}G_{m source}.
}
\tag{M-26901.3}

The carry-side reserve is absolute. Any loss in the physical transference must
be displayed in `kappa_(J,tau)`. A decomposition which returns the full source
energy to the forcing side and gives only `2E=2E` fails.

## 8. Consumer map

The certificate must finish with one explicit recurrence, not a prose appeal.
Accepted forms include:

### DSS recurrence

\[
|\Pi_2(X)|
\le C\log^A(2X)
 +\sum_\beta\theta_\beta|\Pi_2(Y_\beta)|,
\]

where

\[
Y_\beta\le X^{1-\delta},
\qquad
\sum_\beta\theta_\beta\le1.
\]

### Shell-energy recurrence

\[
E_\omega(J)
\le C(1+J)^A
 +\theta\max_{u\le J-\delta}E_\omega(u),
\qquad\theta<1.
\]

Every normalization and boundary term must be shown. The fixed causal filters
from `omega2` to `b2` and from the dyadic shell to the `2/3` shell must be
applied explicitly.

## 9. Binary rejection mutations

A proof object must be tested against at least the following mutations:

```text
M1  replace independent frequencies (t,s) by t=s;
M2  delete one of the four dyadic translate cross terms;
M3  replace -3/2 or 1/2 in omega2 by a nearby rational;
M4  delete one generalized-prime power-of-two correction;
M5  declare the mixed cell 4m<=n<5m automatically nonnegative;
M6  move n>=5m to the positive side without its exact source map;
M7  take total variation before omega2 recombination;
M8  omit an endpoint, cutoff, or noncoprime row;
M9  use only individual-wavelet diagonal reserves and drop cross terms;
M10 use a condition number X^c with fixed c>0;
M11 omit the n<210 boundary table;
M12 fail the first-cell Mertens mutation;
M13 produce a recurrence with lower destination above the declared scale;
M14 substitute a finite numerical ladder for the cofinal theorem.
```

Every mutation must make the verifier reject.

## 10. Reviewer verdict table

A review should classify the following independently:

```text
source manifest completeness               VERIFIED / FALSE / UNPROVEN
physical two-frequency assembly            VERIFIED / FALSE / UNPROVEN
carry positive synthesis                    imported verified / rejected
the transference map                        VERIFIED / FALSE / UNPROVEN
condition-number budget                     VERIFIED / FALSE / UNPROVEN
physical Schur reserve                      VERIFIED / FALSE / UNPROVEN
finite boundary table                       VERIFIED / FALSE / UNPROVEN
DSS/shell consumer recurrence               VERIFIED / FALSE / UNPROVEN
first-cell Mertens mutation                 VERIFIED / FALSE / UNPROVEN
RH conclusion                               only if every prior row verifies
```

A failure of one construction is not a refutation of every possible physical
transference. `FALSE` requires a hypothesis-matching counterexample to the
exact claimed map or inequality.

## 11. Current status

```text
all source/carry inputs to this protocol     PROPOSED COMPLETE
production physical matrix                   NOT YET EMITTED
exact transference map                       OPEN
physical Schur reserve                       OPEN
consumer recurrence                          OPEN AS PART OF THE SAME OBJECT
Riemann Hypothesis                           UNPROVED
```
