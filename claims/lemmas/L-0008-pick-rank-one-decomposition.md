```text
Claim ID:       L-0008
Title:          Exact rank-one decomposition of the Pick matrix of xi'/xi, and
                a citation-free proof of the refutation direction of T-0005
Status:         PROVED
Authoring agent: claude-02 (second agent; written while independently auditing
                claude-01's T-0005)
Reviewing agents: (none yet)
Created:        2026-07-26
Last updated:   2026-07-26
Dependencies:   Hadamard factorisation of xi (order 1: CITATION FLAG below);
                the functional equation xi(s) = xi(1-s)
Used by:        T-0005 (replaces its appeal to the Nevanlinna-Pick theorem for
                the refutation direction)
```

## Context

T-0005 rests on: *a certified NOT-PSD Pick matrix of `F = xi'/xi` refutes RH.*
As written by claude-01 that soundness came from the Nevanlinna-Pick theorem,
quoted from memory -- a citation flag sitting under the repository's most
load-bearing new claim, with the risk pointing in the dangerous direction (a
misremembered theorem could manufacture a false counterexample).  This lemma
removes the citation: the direction T-0005 actually needs follows from an
exact algebraic identity plus a Gram-matrix argument, both proved here in
full.  The deep direction of Pick's theorem (PSD data ⟹ a Herglotz
interpolant exists) is **never used** anywhere in this repository.

## Statement

Fix probe points `a_1, ..., a_N` with `Re a_j > 1/2`, write `a_j' = a_j - 1/2`,
and for a zero `rho` (with `a_j != rho` for all `j`) set

```
    u_j = 1/(a_j - rho),        beta = Re rho - 1/2 .
```

Let `G(rho)` be the contribution of the single term `1/(s - rho)` to the Pick
matrix of `F`:

```
    G(rho)_jk = ( 1/(a_j - rho) + conj(1/(a_k - rho)) ) / ( a_j' + conj(a_k') ).
```

**(i) Exact decomposition.**

```
    G(rho)  =  u u*  -  2 beta * D_u C D_u* ,
```

where `D_u = diag(u_1..u_N)` and `C_jk = 1/(a_j' + conj(a_k'))`.

**(ii) `C` is a Gram matrix, hence PSD** (positive definite when the `a_j` are
pairwise distinct).

**(iii) Consequences.**
  a. If `beta <= 0` then `G(rho) >= 0` (a sum of two PSD matrices).
  b. If every nontrivial zero has `Re rho = 1/2`, the full Pick matrix
     `P = sum_rho G(rho)` (symmetric pairing) is PSD, being a limit of sums of
     PSD matrices.
  c. Contrapositive -- **the T-0005 refutation direction**: a certified
     non-PSD `P` implies a zero with `Re rho > 1/2`, hence by the functional
     equation a zero off the critical line.
  d. Quantitative form: if `lambda_min(P) <= -eps < 0` then
     `sum_{beta_rho > 0} 2 beta_rho * lambda_max(D_{u_rho} C D_{u_rho}*) >= eps`:
     the off-line zeros must jointly carry at least `eps` of negative mass, so
     a large certified negative pivot forces either a deep zero or one close to
     the probes.

## Proofs

**(i).**  Compute the numerator of `G(rho)_jk`:

```
    1/(a_j - rho) + conj(1/(a_k - rho))
        = [ conj(a_k - rho) + (a_j - rho) ] * u_j conj(u_k)
        = [ a_j' + conj(a_k') - (rho - 1/2) - conj(rho - 1/2) ] * u_j conj(u_k)
        = [ (a_j' + conj(a_k')) - 2 beta ] * u_j conj(u_k) .
```

Dividing by `a_j' + conj(a_k')`:

```
    G(rho)_jk = u_j conj(u_k) - 2 beta * u_j conj(u_k) / (a_j' + conj(a_k'))
              = (u u*)_jk - 2 beta * (D_u C D_u*)_jk .                      []
```

**(ii).**  Since `Re a_j' > 0`,

```
    C_jk = 1/(a_j' + conj(a_k')) = INT_0^inf e^{-a_j' t} conj(e^{-a_k' t}) dt ,
```

so `C` is the Gram matrix of the functions `e^{-a_j' t}` in `L^2(0, inf)`:
for any vector `w`, `w* C w = INT_0^inf | sum_j conj(w_j) e^{-a_j' t} |^2 dt
>= 0`.  When the `a_j'` are pairwise distinct the exponentials are linearly
independent, so the integral vanishes only at `w = 0` and `C` is PD.  []

**(iii)a** is immediate from (i) + (ii): `-2 beta >= 0`, `D_u C D_u* >= 0`
(congruence preserves PSD), `u u* >= 0`.

**(iii)b.**  With all zeros at `Re rho = 1/2`, pair `rho = 1/2 + i gamma` with
`conj(rho)`; each partial sum of `P = sum G(rho)` is PSD by a., partial sums
converge entrywise (the paired tails decay like `1/gamma^2`, see the Hadamard
identity below), and the PSD cone is closed.  []

**(iii)c** is the contrapositive of b., using the zero symmetry
`rho <-> 1 - rho` (functional equation): "some zero has `Re rho > 1/2`" and
"some zero is off the line" are equivalent.  []

**(iii)d.**  `P = sum_{beta<=0} G(rho) + sum_{beta>0} [u u* - 2 beta D_u C D_u*]
>= - sum_{beta>0} 2 beta D_{u} C D_{u}*`, so
`lambda_min(P) >= - sum_{beta>0} 2 beta lambda_max(D_u C D_u*)`.  []

## The prerequisite, made explicit: `F = sum_rho 1/(s - rho)`

Everything above concerns the function `sum_rho 1/(s - rho)`.  T-0005 computes
`F = xi'/xi` from the Euler-Maclaurin machinery, so the two must agree:

  1. `xi` is entire of **order 1** and `xi(0) != 0`.
     [CITATION FLAG (M-0004): standard, quoted from memory, not re-derived
     here.  Direction of risk analysed below.]
  2. Hadamard for order 1:  `xi(s) = e^{A + Bs} prod_rho (1 - s/rho) e^{s/rho}`,
     so `F(s) = B + sum_rho [ 1/(s - rho) + 1/rho ]`.
  3. The functional equation gives `F(s) = -F(1-s)`, and the zero set is
     invariant under `rho -> 1 - rho`.  Adding the two expressions for
     `F(s) + F(1-s) = 0` and using the substitution `rho -> 1 - rho` in the
     second sum cancels the `1/(s-rho)` terms pairwise and leaves
     `2B + 2 sum_rho 1/rho = 0` (symmetric pairing), i.e. `B = -sum 1/rho`.
  4. Substituting back: `F(s) = sum_rho 1/(s - rho)` with symmetric pairing. []

**Direction of risk.**  If step 1 were wrong (order > 1), `F` would carry an
extra polynomial term `c(s)` and the Pick matrix would be `sum G(rho) +
Pick(c)`.  A NOT-PSD verdict could then be caused by `Pick(c)` rather than by
an off-line zero -- a FALSE POSITIVE, the dangerous direction.  This is why
X-0013 validates the identity *numerically* against the certified zero list:
`F` computed by claude-01's `xi_logderiv` (no zeros anywhere in that code path)
is compared with `sum 1/(s-rho)` over the 4520 certified ordinates, and the
residual must match the predicted tail of the truncated sum in sign, size, and
decay.  A constant or polynomial discrepancy would be flagged loudly there.

## What this changes for T-0005

* The refutation direction of T-0005 is now **PROVED inside the repository**,
  modulo one low-risk, numerically-cross-checked citation (order of `xi`),
  instead of resting on the full Nevanlinna-Pick interpolation theorem quoted
  from memory.
* The rank-one structure explains the baseline floor (T-0005's rank argument
  is the special case `beta = 0` of (i), where `G(rho) = u u*` exactly).
* The exact split for an off-line pair `rho_± = 1/2 ± delta + i gamma`,

  ```
      G(rho_+) + G(rho_-) = u_+ u_+* + u_- u_-* - 2 delta [ S_+ - S_- ],
      S_± = D_{u_±} C D_{u_±}* ,
  ```

  is the starting point for deriving the measured `|min pivot| ~ delta^p` law
  (Q-0016a): the negative-capable part is `2 delta (S_- - S_+)`, itself of size
  `O(delta)` in the `sigma`-derivative of the PSD family `S`, giving a leading
  `O(delta^2)` indefinite perturbation -- consistent with the drift of the
  measured slopes (3.8 -> 2.4 over ten decades) toward an asymptotic exponent
  of **2**, not 3.  X-0014 measures this.

## Verification

`tests/test_pick.py::test_rank_one_decomposition_identity` checks (i)
entrywise in ball arithmetic at asymmetric probe/zero configurations, and
`test_gram_matrix_C_is_PD` checks (ii) via interval LDL.  X-0013 validates the
Hadamard prerequisite against the certified zeros.
