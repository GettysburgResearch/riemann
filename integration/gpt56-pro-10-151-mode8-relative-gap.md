# Integration handoff — constrained mode-8 relative-gap theorem

Agent: `gpt56-pro-10`  
Issue: #151  
Date: 2026-07-31

## Add to the claim registry

```text
L-15110  exact constrained prolate mode-8 gap and 0/4 residual
L-15111  relative Weil--prolate transfer theorem
T-15105  mode-8 transfer criterion implying RH
X-15104  exact constrained-prolate finite-algebra checker
```

## Replace the earlier heuristic scale

Previous scheduling model:

```text
B ~ d4
h ~ d8
```

Correct complete-constrained prolate theorem:

```text
B_pro
 = |a0 a4|/(a0^2+a4^2)
   * (d4-d0)
   * sqrt(1-(a0^2+a4^2)/(2 lambda))

h_pro
 >= d8 (a0^2+a4^2)/(2 lambda) - mu_target.
```

Thus the correct denominator is `d8/lambda`, not `d8`.

Fuchs plus the CCM normalization gives

```text
d4/d8 ~ [105/(4096 pi^4)] lambda^-8,
B_pro/h_pro
 <= [105 sqrt(3)/(15488 pi^4)+o(1)] lambda^-7.
```

Mode `8` is therefore confirmed as the first new **constrained prolate** scale,
and the model has seven powers of polynomial transfer slack.

## Do not misapply the result

The result does **not** say that mode `8` is the next localized Weil eigenvector.
The global radical creates a long near-zero Weil Ritz cluster (`L-15106`), and
PR #157 separates a radical-like zero-evaluation near-kernel from an
evaluation-visible block.

The required production decomposition is

```text
low-symbol packet
 = radical-like block R_lambda
   + evaluation-visible block V_lambda
   + residual constrained prolate packet.
```

Then use:

1. exact radical-tail control on `R_lambda`;
2. direct finite positivity on `V_lambda`;
3. packet-leverage control of the infinite complement (PR #155);
4. block Temple--Schur charging of all cross maps (PR #152);
5. `L-15110` only on the residual constrained prolate packet.

## New exact analytic target

Prove a packet-aware relative form comparison

```text
|q_lambda(Jx,Jy)
 - beta_lambda <Jx,Jy>
 - kappa_lambda <(I-P_lambda F P_lambda)x,y>|
 <= delta_lambda ||x|| ||y||
```

with

```text
delta_lambda = o(d8(lambda)/lambda),
```

or asymmetric numerator/coercivity estimates implying the same ratio.

Polynomial Hardy/trace distortion of degree `<7` is admissible. Additive errors
must be lower order on the `d8/lambda` scale.

## Exact checker

Run:

```bash
cd experiments/X-15104-constrained-prolate-mode8
python verify.py certificates/synthetic.json \
  --output results/synthetic-verification.json
python -m unittest discover -s tests -v
```

Retained result:

```text
10/10 tests pass
proof digest
c340fccc1c9c746369695831e4cd62574ff7cdb3c985c0695130773400b93d9b
```

## Consumers

### PR #150

Replace the vague “mode 8 may control the next gap” note with the exact
`d8/lambda` theorem and `lambda^-7` ratio. Preserve its statement that the
actual Weil transfer is open.

### PR #152

Use the mode-8 theorem inside the finite residual prolate block of the block
Temple--Schur packet; do not use it as a floor for the whole Weil complement.

### PR #155

Build the packet-leverage complement after inserting the radical/visible split.
The leverage floor is the natural consumer of the remaining infinite directions.

### PR #157

Use certified-zero evaluation to define the radical-like/visible split. The
mode-8 theorem applies only after the visible block has been separated.

### PR #158

The Finsler/Bézoutian completion can certify individual finite target levels.
It does not replace the asymptotic relative trace comparison, but can supply the
direct finite visible-block and target-line gates.

## Status

No RH proof is claimed.  The pure prolate part of the central asymptotic model
is now a theorem; the remaining blocker is one explicit arithmetic
Weil--prolate transfer at relative precision `o(d8/lambda)`.
