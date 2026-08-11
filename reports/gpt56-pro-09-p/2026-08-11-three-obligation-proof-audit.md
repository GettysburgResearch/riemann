# Three-obligation proof audit: isolated line, non-ground real zeros, and moving-Hardy closure

Date: 2026-08-11  
Agent: `gpt56-pro-09-p`  
Branch at completion: `agent/gpt56-pro-09-i/198-square-screw-criterion`  
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
`O(exp(-BL))` at any prescribed exponential rate, one obtains a cofinal isolated
line converging exponentially to the target.  The generalized second eigenvalue
is exactly one.

This is an unconditional source/arithmetic theorem.  It is not an isolated-line
theorem for the indefinite localized Weil matrix.

### Obligation 2 — false as stated

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

and arbitrary allowed even diagonal `(0,2,0)`, so the counterexample lies inside
the finite CCM/Loewner class, not merely among arbitrary Hermitian matrices.

A multiplier `Q(z)` having only real zeros cannot repair the defect, because
every nonreal zero of `F` remains a zero of `QF`.

The correct replacement is an **independent positive CCM completion** for the
same isolated line:

```text
Q_j >= 0,
ker Q_j = C xi_j,
[D0,Q_j] = |beta_j><eta|-|eta><beta_j|.
```

The finite CCM theorem then gives real zeros, but existence of this completion is
not implied by spectral isolation.  It is the sole remaining RH-bearing gate.

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
The audited source-to-strip inequality yields locally uniform convergence of the
finite transforms to a nonzero multiple of Xi on every closed substrip.

## Corrected proof chain

The complete surviving chain is

```text
exact positive residual-Gram isolation        PROVED
complete moving-Hardy convergence              PROVED
positive CCM/Loewner completion for same line OPEN / RH-BEARING
finite real-zero theorem                       then automatic
Hurwitz                                        then automatic
RH                                             UNPROVED
```

The old phrasing as three independent obligations was misleading.  Isolation and
convergence are analytic/linear-algebraic.  The finite real-zero property is not
a generic consequence of either; its positivity completion contains the central
arithmetic sign.

## Files

```text
R-19848  exact isolated-interior counterexample and multiplier firewall
L-19867  exact residual-Gram isolated-line theorem
L-19868  complete moving-Hardy target-rate ledger
M-19802  corrected positive-completion programme
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
