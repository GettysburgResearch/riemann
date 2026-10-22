# Final status of the three isolated-line obligations

Date: 2026-08-12  
Branch: `agent/gpt56-pro-09-i/198-square-screw-criterion`  
Scope: continuation of `M-19802` and `2026-08-11-three-obligation-proof-audit.md`  
Scientific status: **RH remains unproved**

## Executive result

The three requested obligations do not survive as three simultaneously valid
theorems in their original form.

1. A complete prime/source-side isolated-line theorem **is proved** for the
   exterior-residual positive pencil (`L-19867`), with exact cofinal residual
   ratio and a simple even target line.
2. A generic non-ground CCM real-zero theorem is **false**, even inside the exact
   divided-difference matrix class (`R-19848`, `R-19849`).
3. The complete moving-Hardy target rate **is proved** for the Xi residual line,
   with explicit support, Fourier-cutoff, alias, endpoint and directed-enclosure
   scheduling (`L-19868`).

The strongest correct replacement for item 2 is `L-19869`: a prescribed positive
source-bound symmetrizer whose normalized CCM commutator defect tends to zero
forces all finite zeros into a shrinking real strip and therefore implies RH by
Hurwitz.

Two further exact firewalls now close the logical audit:

- `L-19870`: minimizing the defect over an unrestricted positive metric gives
  exactly the largest imaginary part of the finite determinant roots.  Free
  metric optimization is spectrally tautological.
- `R-19850`: the tempting isotropic residual complement has an exact parity-area
  defect.  A spectral gap by itself does not approximate the CCM commutator.

Thus the surviving conclusion-producing theorem is one source-specific
anisotropic commutator cancellation.  No current file proves it.

## I. Obligation 1 — isolated line

For the exact residual Gram `D_j` and metric

```text
G_j = diag(1,C_j),  C_j >= I,
```

write the whitened matrix as

```text
[[m_j, u_j*],
 [u_j, I]],
```

where `m_j` is the target residual energy and `||u_j||^2<=m_j`.
The generalized eigenvalues are

```text
1 (multiplicity dim(E_j)-1),
lambda_±=(1+m_j ± sqrt((1-m_j)^2+4||u_j||^2))/2.
```

Hence

```text
0<=lambda_-<=m_j,
lambda_+>=1,
gap>=1-m_j,
```

and the target-line angle is at most

```text
sqrt(m_j)/(1-m_j).
```

With `m_j<=exp(-8L_j)`, the exact cofinal residual ratio tends to zero
exponentially.  This proves the isolated-line geometry without assuming RH and
without excluding lower eigenvalues of the localized Weil matrix.

It does not establish a two-sided moat for the indefinite localized Weil matrix
itself.  The positive residual pencil is the corrected object.

## II. Obligation 2 — exact counterexample and correct replacement

At nodes `-1,0,1`, the exact CCM matrix

```text
A=[[0,1,1],
   [1,2,1],
   [1,1,0]]
```

has eigenvalues `-1,0,3`.  Its simple interior zero eigenvector

```text
xi=(1,-1,1)
```

is even and normalized by the CCM evaluation vector.  Nevertheless its
determinant polynomial is

```text
P_xi(s)=s^2+1.
```

Thus isolation, parity and exact CCM matrix structure do not imply real zeros.
Moreover the parity-preserving positive CCM completion cone with this kernel is
empty.

`L-19869` proves the correct asymptotic substitute.  If `Q_j>=0`,
`ker Q_j=C xi_j`, and

```text
E_j=Q_j T_j-T_j^*Q_j
```

has normalized quotient norm at most `2 epsilon_j`, then every nonuniversal zero
of `hat xi_j` has imaginary part at most `epsilon_j`.  Local uniform convergence
and `epsilon_j->0` imply RH.

`L-19870` proves that the best possible defect over all positive metrics equals
exactly the nonreal spectral radius.  Therefore the only meaningful theorem is
small defect for one metric fixed independently by arithmetic/source geometry.

`R-19850` shows that the identity-complement limit does not provide this metric:
its defect is the area of the even evaluation mismatch and odd scaling
derivative.

## III. Obligation 3 — moving-Hardy rate

Let `r` be the exact Xi source and `L_j=j`.  Analytic continuation of `r` to a
fixed strip and its super-exponential real decay give

```text
periodization/fold alias <= C_A exp(-A L_j),
weighted Fourier tail
 <= C_A exp(tau_j L_j/2-2pi a N_j/L_j).
```

Take

```text
tau_j=1/2-1/j,
N_j=ceil(kappa j^2),
kappa>8/pi^2.
```

Then the complete target rate satisfies

```text
weighted projection + periodization + fold alias
 <= C exp(-c j).
```

For the residual ground line, `m_j<=exp(-8j)` gives

```text
angle <= sqrt(m_j)/(1-m_j) <= 2 exp(-4j).
```

Endpoint and pole channels are exact by construction.  At each finite level all
remaining special-function, prime-power and matrix entries are computable, so
outward dyadic enclosures can be refined until the total directed radius is at
most `2^-j`.

Thus the full moving-Hardy error is bounded by

```text
C exp(-cj)+2 exp(-4j)+2^-j -> 0.
```

No actual-zero selector, horizontal support sieve or unproved alias asymptotic
is used.

## Exact final frontier

The corrected route is now

```text
exact residual isolated line                    PROVED
complete moving-Hardy rate                      PROVED
generic non-ground CCM real-zero theorem        FALSE
unrestricted positive symmetrizer optimization  TAUTOLOGICAL
isotropic complement as symmetrizer             REFUTED
source-bound anisotropic CCM commutator defect   OPEN / RH-BEARING
Riemann Hypothesis                               UNPROVED
```

A future full proof must construct the positive forms `Q_j` from arithmetic
sources and prove

```text
1/2 ||Q_j^(-1/2)(Q_j T_j-T_j^*Q_j)Q_j^(-1/2)|| -> 0
```

on the quotient.  Neither a larger spectral gap nor free choice of metric can
replace this theorem.
