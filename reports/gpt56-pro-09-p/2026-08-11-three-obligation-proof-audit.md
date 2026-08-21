# Three-obligation proof audit: isolated line, non-ground real zeros, and moving-Hardy closure

Date: 2026-08-11  
Agent: `gpt56-pro-09-p`  
Branch: `agent/gpt56-pro-09-i/198-square-screw-criterion`  
Scientific status: **RH remains unproved**

## Requested obligations

1. establish a two-sided isolated-line moat and residual ratio on one cofinal sequence;
2. extend the finite CCM real-zero theorem to a non-ground isolated line, or groundify it by Darboux without hiding the ground hypothesis;
3. prove the moving-Hardy rate with endpoint, periodization, alias and directed-enclosure losses.

## Exact outcome

### Obligation 1 — proved in the corrected positive residual model

`L-19867` applies the exact exterior-cardinal residual geometry of `L-19862`.
For

```text
D = [[m,b*],[b,C]],  C >= I,
G = diag(1,C),
```

it proves exactly

```text
||Dw||_(G^-1) >= ||w||_G       on p-perp,
||Dp||_(G^-1)^2 <= m+m^2.
```

Thus `g=1` and `b/g<=sqrt(m+m^2)`.  Since the Xi target residual can be made
`O(exp(-BL))` at any prescribed exponential rate, one obtains a cofinal even
isolated line converging exponentially to the target.  The generalized second
eigenvalue is at least one and is exactly one in the actual complement
dimensions.

This is an unconditional source/arithmetic theorem.  It is not an
isolated-line theorem for the indefinite localized Weil matrix.

### Obligation 2a — the generic exact statement is false

`R-19848` gives the exact parity-invariant CCM matrix

```text
A = [[0,1,1],
     [1,2,1],
     [1,1,0]].
```

It has eigenvalues `-1,0,3`; the simple even interior eigenvector
`xi=(1,-1,1)` has residual zero and orthogonal singular moat one.  Nevertheless
its CCM transform numerator is

```text
P_xi(z)=z^2+1,
```

with zeros `+i,-i`.

The matrix has the exact divided-difference form

```text
A_ij=(b_i-b_j)/(i-j), b=(-1,0,1),
```

and allowed even diagonal `(0,2,0)`, so the counterexample lies inside the
finite CCM/Loewner class.  `R-19849` proves more: every parity-invariant CCM
matrix with this vector in its kernel is a scalar multiple of `A`, so its
positive-completion cone is empty except for the zero matrix.

A multiplier having only real zeros cannot repair the defect, because every
nonreal zero of `F` remains a zero of `QF`.

### Obligation 2b — a genuine asymptotic non-ground theorem is proved

`L-19869` associates to a finite target `xi` the companion operator

```text
T_xi = Lambda-|Lambda xi><eta|,
```

whose nonzero characteristic factor is exactly the finite CCM polynomial.  For
any positive semidefinite `Q` with `ker Q=C xi`, define

```text
epsilon(Q,xi)
 =1/2 || Q_quot^(-1/2)(Q T_xi-T_xi^*Q)_quot Q_quot^(-1/2) ||.
```

Every finite polynomial root then satisfies

```text
|Im z| <= epsilon(Q,xi).
```

Therefore, if the finite transforms converge locally uniformly and
`epsilon_j->0`, every zero of the limit is real.  This is a true non-ground
extension: finite transforms may have nonreal zeros, but they are squeezed into
a vanishing strip.

For the residual pencil, the positive symmetrizer is already available:

```text
Q_j=D_j-lambda_(j,-)G_j >=0,
ker Q_j=C xi_j.
```

The sole remaining gate is the explicit normalized rank-two commutator defect

```text
1/2 ||Q_j^(-1/2)[
 Q_j Lambda_j-Lambda_j Q_j
 -|alpha_j><eta_j|+|eta_j><alpha_j|
]Q_j^(-1/2)||_quot ->0,
alpha_j=Q_j Lambda_j xi_j.
```

Exact positive CCM completion is the special case where this defect is zero.

### Obligation 3 — proved for the residual-Gram line

`L-19868` proves the full target-side estimate

```text
||iota_L xi_tilde_(L,N)-r_Xi||_tau
 <= C[
   exterior/alias tail
   + exp(tau L/2-2 pi a N/L)
   + exp(tau L/2)sqrt(m)/(1-m)
   + exp(tau L/2)delta_interval
 ].
```

Periodization includes every noncentral alias.  Its endpoint values and all
endpoint derivatives agree exactly, so the periodic endpoint mismatch is zero.
Normalization is charged to the alias and Fourier-cutoff terms.  The directed
interval radius is selected afresh at every level.

For

```text
tau_L = 1/2-L^(-1/2),
N_L = ceil(kappa L^2),
m_L <= exp(-8L),
delta_L <= exp(-4L),
```

with sufficiently large fixed `kappa`, the complete error is `O(exp(-cL))`.
The audited source-to-strip inequality yields locally uniform convergence to a
nonzero multiple of Xi on every closed substrip.

## Corrected proof chain

```text
exact positive residual-Gram isolation          PROVED
complete moving-Hardy convergence                PROVED
asymptotic positive-symmetrizer theorem          PROVED
normalized rank-two commutator defect -> 0        OPEN / RH-BEARING
finite zeros enter a shrinking real strip         then automatic
Hurwitz                                            then automatic
RH                                                 UNPROVED
```

The original three obligations were not independent.  Isolation and convergence
are analytic/linear-algebraic.  The generic exact non-ground statement is false.
The surviving conclusion-producing datum is now one explicit commutator defect,
not a hidden ground-state hypothesis.

## Files

```text
R-19848  exact isolated-interior counterexample and multiplier firewall
R-19849  exact empty positive-completion cone
L-19867  exact residual-Gram isolated-line theorem
L-19868  complete moving-Hardy target-rate ledger
L-19869  asymptotic non-ground symmetrizer theorem
M-19802  corrected commutator-defect programme
X-19843  exact Fraction-only replay
```

## Verification

```bash
cd experiments/X-19843-isolated-line-firewall
python3 verify.py > /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Retained verdict:

```text
PASS_ISOLATED_INTERIOR_CCM_FIREWALL
```
