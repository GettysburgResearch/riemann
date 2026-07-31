# X-15408 — Exact finite Hardy pole-Gram regression

Status: exact Gaussian-rational synthetic regression  
Agent: `gpt56-05-l`  
Claims: `T-15407`, `R-15402`  
Issue: #180

## Purpose

For a finite meromorphic principal-part packet

```text
p(z)=sum_j r_j/(z-a_j),
Re(a_j)<sigma,
```

Laplace Plancherel gives the exact Hardy energy

```text
(1/(2*pi)) integral_R |p(sigma+i t)|^2 dt
 = sum_(j,k) conjugate(r_j) r_k
   /(2 sigma-conjugate(a_j)-a_k).
```

The Cauchy matrix on the right is positive semidefinite. `T-15407` uses this
identity to separate stable poles, critical-boundary poles, and unstable
right-half-plane poles.

`X-15408` verifies the finite algebra using Python integers and
`fractions.Fraction` only.

## Retained packets

### Unstable packet

Two poles have common real part `1/4` and distinct ordinates `3/2,5/2`.
The evaluation line is

```text
sigma=13/50=1/4+1/100.
```

With residues

```text
2-i,
-1+i/2,
```

the exact energy is

```text
1562625/5002,
```

and the sigma-weighted energy is

```text
812565/10004.
```

The diagonal entries of the Cauchy Gram equal `50`, displaying the
`1/(2 epsilon)` unstable pressure.

### Boundary packet

The poles are `i` and `2i`. The exact sigma-weighted energy at `sigma=1/10` is

```text
21/26.
```

The rational fail-safe Abel bound from the residue-coordinate `l1` norm is `2`.
This illustrates that critical-line poles have finite normalized Abel mass.

### Stable packet

The pole is `-1/4+i`. At `sigma=1/10`, the weighted energy is

```text
9/28.
```

It tends to zero as the evaluation line approaches the critical boundary.

## Reproduction

```bash
python verify.py certificates/synthetic.json \
  --output results/synthetic-verification.json
python -m unittest discover -s tests -v
```

Nine adversarial tests pass.

## Mutation coverage

The tests reject:

- a false exact quadratic value;
- a false sigma-weighted value;
- a line through or left of a declared pole;
- duplicate poles;
- a zero residue;
- a nonpositive line parameter;
- Boolean integer fields;
- malformed packet claims.

They also check exact Hermitian conjugacy of the retained Cauchy matrix.

## Proof boundary

This experiment proves finite rational Hardy pole algebra only. It does not
locate any Riemann zero and does not prove that the actual right-half-plane
principal-part packet of `xi'/xi` is empty. That emptiness is precisely the
unclosed RH statement isolated by `T-15407`.
