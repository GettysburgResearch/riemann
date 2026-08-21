# M-26201 — Review protocol for the dyadic two-contact signed-slack proposal

Methodology ID: `M-26201`  
Title: Fail-closed review of the fixed-`q_0=2` source trace, two-contact carry collapse, and bottom-charge descent  
Status: **REVIEW PROTOCOL**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Primary claims: `L-26201`--`L-26203`, `T-26201`  
Scope: exact finite replay and adversarial review of DSS/PBD

## 1. Freeze all imported interfaces

Record exact heads for:

```text
PR #241   L-9518 two-frequency physical block
PR #158   L-15159 fixed-logarithm Möbius source
PR #236   dyadic shell, binary digit kernel, parity comb
PR #244   greedy carry, blocker loss, digital freeze
PR #248   divisor-gradient and Green calculus
PR #254   signed constraint-dipole transport
current proposal branch/head
```

Do not silently consume later repairs.

## 2. Exact source gates

### Gate A — fixed-log source

Verify that fixing `q_0=2` in the complete signed Heath--Brown packet gives the
finite Möbius signal with all endpoint conditions satisfied on the selected
block.

### Gate B — dyadic shell

Apply the exact dyadic difference and recover

\[
b_2(n)=\mu(n)-\mathbf1_{2\mid n}\mu(n/2).
\]

Check that the bounded causal filters used in the source change do not alter
the upper exponential abscissa.

### Gate C — pointwise carry collapse

Independently reconstruct

\[
\sum_{q=2}^n b_2(q)\chi_{n,q}(j)
=
-\mathbf1_{j=1}-\mathbf1_{j=n-1}
\]

for every finite row. A review must verify the floor convention at:

```text
j=0
j=1
j=n-1
j=n
n=2
q=1 insertion/removal
```

### Gate D — reflected cross and reserve

Verify the generalized Kummer identity for a formal completely additive
derivation. Confirm:

\[
\langle Y_n,\Lambda_L\text{-carry}\rangle
=-2L(n)/(n+1)
\]

and that the remaining binomial-square term is a positive orthogonal reserve,
not a deleted diagonal.

## 3. Carry residual gates

### Gate E — signed slack

For an arbitrary finite vector `d`, check exactly

\[
\Pi_2=\mathcal R_2+2\sum_n d(n)/(n+1).
\]

For the greedy vector, independently verify

\[
s_X(n)=\beta_{nn}\ell_X(n)
\]

before substituting it into the parity-weighted blocker formula.

### Gate F — dyadic-chain ledger

Verify

\[
\Pi_2
=
\sum_{m\ {\rm odd}}\mu(m)
[s(m)-2s(2m)+s(4m)]
\]

with every truncated chain and the `m=1` boundary represented.

Mutations:

```text
replace -2 by -1
drop the 4m layer
identify m and 2m signs
discard the m=1 chain
extend a chain beyond X without zero padding
```

Every mutation must fail.

## 4. Green gates

### Gate G — full-divisor Gram

Use all divisor coordinates `2,...,X`, not only prime powers. Verify positive
definiteness and the exact inverse

\[
\overline G_X^{-1}(a,b)
=
\sum_{d\mid a,e\mid b}\mu(a/d)\mu(b/e)\min(d,e).
\]

### Gate H — two charges

Verify

\[
\overline G_Xb_2=-3e_2+e_3,
\qquad
b_2^T\overline G_Xb_2=5.
\]

Mandatory mutations:

```text
-2 e_2 + e_3
-3 e_2
-3 e_2 + e_4
endpoint-projected Gram substituted for the unprojected Gram
prime-power-only coordinates substituted for all divisors
```

### Gate I — source-specific target

Check that DSS is exactly

\[
|-3T_X(2)+T_X(3)|=X^{o(1)},
\quad
T_X=\overline G_X^{-1}s_X^{gr}.
\]

A proof of a different Green energy does not automatically imply this unless
the map is explicit.

## 5. Transport no-go gate

For the divisor-gradient coordinate verify

\[
\sum_q b_2(q)v_q(b)=-2b(2)+b(3)
\]

and

\[
\Delta_F=3F_2-F_3.
\]

Reject any proof claiming that a flow supported entirely at `j>=4` changes the
dyadic scalar.

A valid transport proof must route its charge all the way to the bottom
boundary and retain the complete accumulated coefficient.

## 6. PBD production gate

A production Parity Blocker Descent certificate must emit machine-readable
records:

```text
parent endpoint X
every blocker edge
every dyadic chain
all chain truncations
same-scale cluster solve
signed child coefficients
child endpoints
bottom-charge contribution
boundary forcing
exact parent-child equality
```

Required inequality:

\[
|\Pi_2(X)|
\le C\log^A(2X)
+\max_{Y\le(X+1)/2}|\Pi_2(Y)|.
\]

Reject:

- a sum over exponentially many children without a mass bound;
- an unsigned replacement of the Möbius chain;
- a child above half scale;
- a statement of acyclicity without a source equality;
- omission of charges at `2` or `3`;
- a finite numerical ladder promoted to all `X`.

## 7. Analytic gate

From DSS, verify:

1. the automatic `O(log^2 X)` harmonic carry term;
2. normal convergence of the Riesz Mellin integral in `Re z>0`;
3. noncancellation of a zeta-zero pole by `1-2^{-s}`;
4. functional-equation symmetry.

No physical-normal-Gram estimate is required for this implication.

## 8. Classification

```text
VERIFIED
  every exact gate and a production DSS/PBD proof pass;

VERIFIED WITH FIXES
  only notation, finite endpoint conventions, or checker binding need repair;

GAP/BLOCKED
  exact algebra passes but DSS/PBD is not proved;

REJECTED
  source trace, two-contact identity, parent-child equality, or Mellin
  noncancellation fails.
```

A proof of the generic parity-comb inverse, total greedy slack, or full Green
energy may imply DSS, but it is stronger and must be reviewed at its own
declared scope.
