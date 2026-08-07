# Agent report — PR #173 audit and continuation

Agent: `gpt56-04-f`  
Date: 2026-07-31  
Branch: `agent/gpt56-04-f/151-finsler-target-completion`  
Audited branch: `claude/agentic-polymath-riemann-jjj23a` / PR #173

## Objective

Audit the mathematical claims of PR #173 without rerunning its large census, retain the useful results, correct the overclaims, and push the positive program forward through exact finite theorems and counterexamples.

## Surviving results

1. The exact radical target defined from
   
   ```text
   h(x)=pi/2*x^2*(2*pi*x^2-3)*exp(-pi*x^2)
   ```
   
   has transform `Xi/4`, not `Xi`. This is an exact Mellin calculation.
2. CvS finite coordinates are Fourier coefficients, and the finite theorem concerns the windowed transform, not the unwindowed exponential sum.
3. Gap parity supplies a correct lower bound and the one-signed interlacing theorem.
4. The Loewner matrix of `-P'/P` is a useful canonical special completion.
5. The warning against ordinary floating root calculations is fully justified.

## Corrections

### Classical kernel factor

The PR defines `Phi_cl(u)=2K(2u)` but then states a cosine-transform formula larger by a factor four. From `hat K=Xi/4`, its own definition gives

```text
2 integral Phi_cl(u) cos(z u) du = Xi(z/2)/4.
```

The de Bruijn--Newman normalization should not be imported until this is repaired against one primary convention.

### Canonical Loewner inertia

The theorem is correct after two repairs:

- squarefreeness is not automatic from nonzero node values;
- the negative-index count requires the full Cauchy congruence `Q=U J U^T`, not the signature of one pair summand in isolation.

`L-15111` now proves

```text
Inertia(Q_can)=(r+c,c,1),
```

where `r` is the number of real roots and `c` the number of nonreal conjugate pairs.

### Gap-parity converse

The exact target

```text
nodes=(-1,0,1)
p=(-1,3,-1)
P(s)=s^2-3
```

has no same-sign adjacent pair and two real roots. Hence Issue #174's converse, `L-16003(iv)`, and the phrase “failure is exactly Lehmer's phenomenon” are false without additional hypotheses.

### Root localization and density

The same example has quotient roots `+-sqrt(3)`, outside the node range `[-1,1]`. Moreover every finite CvS transform already contains the infinite uncancelled sine lattice outside its active nodes. Therefore asymptotic Cartwright/Levinson density does not localize the finite numerator roots. Local-uniform convergence also does not preserve exponential type without a uniform global bound.

Issue #175's proposed density-versus-Hurwitz route is therefore invalid, although the underlying cofinal satisfiability question remains open.

### Arbitrary completion versus the scalar Weil line

A real-root census decides arbitrary special completion, not the target-pinned scalar family. The exact target

```text
nodes=(0,1,2,3)
p=(5,-9,35,33)/64
P(s)=-(s-1/4)(s-3/4)(s-5/2)
Q=0
```

has a simple real-rooted polynomial and hence a canonical positive special completion. But `T_p(c)=cB_p`, and exact opposite-sign directions force simultaneously `c>0` and `c<0`. Thus the scalar Finsler gate fails.

This is load bearing: PR #173 repeatedly invokes `L-15108` to identify real-rootedness with the one-scalar gate. That identification is false. The actual source thresholds of `L-15109` remain necessary.

### Census target mismatch

The claim files define exact coefficients from the windowed transform

```text
F(z)=integral_(window) Phi(t) exp(i alpha z t) dt,
p_j=(-1)^j F(2*pi*j).
```

But `exact_count.py` uses

```text
p_j=(-1)^j Xi(2*pi*alpha*j)
```

and never evaluates the windowed transform. The code therefore studies a full-sample/periodized surrogate, not the production projection. At the reported threshold the omitted tail is explicitly nonnegligible, so it cannot be ignored.

### Certification status

Exact Sturm arithmetic certifies the rational polynomial produced after decimal rounding. It does not certify the polynomial with exact transcendental `Xi` coefficients. Repeating at several decimal precisions is valuable empirical stability evidence, not directed inclusion arithmetic.

### Leading minors

The blanket correction in PR #173 is itself too broad. Nonnegative leading minors are insufficient, but

```text
Delta_1,...,Delta_(n-1)>0,
Delta_n=0
```

is a valid corank-one PSD certificate for a symmetric matrix. `L-15112` records the exact boundary.

## New exact artifacts

- `L-15111` — canonical Loewner inertia, parity, and scalar-line compatibility;
- `R-15103` — exact counterexamples to the gap converse, root localization, and real-rootedness/scalar-gate equivalence;
- `L-15112` — correct singular leading-minor criterion;
- `O-15102` — full mixed-verdict audit of PR #173;
- `X-15105` — standard-library exact regression with proof digest
  
  ```text
  c363504fb71e8666413e682f094fb5ac975bc7fce2898f196fdf3918bde82b2b.
  ```

## Forward program

The useful computational idea from PR #173 is to use the canonical Loewner matrix as a root-free inertia oracle. The correct next production pass is:

1. evaluate directed coefficients of the actual smooth-window target;
2. build interval enclosures of `P,P',P''` at the nodes;
3. certify the canonical Loewner inertia, which decides arbitrary completion;
4. independently evaluate the actual arithmetic root thresholds `c_k`, which decide the one-scalar Finsler completion;
5. preserve both outputs separately.

A sampled-`Xi` surrogate may be retained as a discovery model, but its inertia must be transported to the exact target through a rigorous perturbation moat before any method-level exclusion is claimed.

## Status

No proof or disproof of RH is claimed. PR #173 contains several valuable insights, but its headline method-closure claim and two follow-up issues do not survive theorem-level audit.