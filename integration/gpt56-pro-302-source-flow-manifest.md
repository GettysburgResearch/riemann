# Integration handoff — source-flow repair of the eta–Pascal cascade

**Branch:** `research/gpt56-pro-302-source-flow-manifest`  
**Frozen parent:** PR #301 at `1855957a18b7ea43229cde626178920f7a538951`  
**Status:** review/repair; RH unproved

## Canonical review spine

```text
R-30201  exact standalone source/edge mismatch
L-30201  relative replacement and absolute divisor commutator
L-30202  shifted residual Hausdorff invariance
R-30202  source mass is not central-edge capacity
D-30201  fail-closed source-flow certificate
L-30203  exact finite capacity LP and Farkas dual
T-30201  SFC -> triangular eta cascade -> Cycle Debt -> RH
M-30201  adversarial review protocol
X-30201  exact finite regressions
```

## Main correction to PR #301

Retain:

```text
chi_[4k,2k-1]-chi_[4k,2k]
 =1_(q|2k)-1_(q|2k+1).
```

But distinguish:

```text
relative flow replacement:
  A[4k,2k] -> (A-B)[4k,2k]+B[4k,2k-1];

formal paired source:
  A e_(2k)-B e_(2k+1).
```

The first changes the carry vector by the required dipole.  It does not realize
the second unless the incoming central edge of coefficient `A` is present.

The exact `k=1` mutation is mandatory:

```text
source q=2,3,4       1/2, -1/3, 0
edge pair q=2,3,4    1/3,  1/6, 1/2
```

## New durable theorem

For the actual shifted coefficients

```text
A_k=(2kq-1)^(-s)/(2k),
B_k=((2k+1)q)^(-s)/(2k+1),
```

the residual `A_k-B_k` is a Hausdorff moment sequence.  This remains true after
all positive finite-difference jets and exact Euler remainders.  Hence the
boundary source type is stable across generations.

## Correct open theorem

`SFC` must bind those source coefficients to actual edge capacities in the
incoming flow and prove only polylogarithmic weighted defect.  The finite
zero-defect problem is

```text
Bx=r-Ba,
x>=0,
```

with the exact balanced-superadditive Farkas dual in `L-30203`.

## Conditional composition

```text
analytic contraction 6/7
+ boundary source contraction theta<1
+ Hausdorff residual invariance
+ SFC polylog capacity defect
-> triangular polylog cascade
-> Cycle Debt
-> prime ramp 4 sqrt(X)+X^o(1)
-> square-screw/Landau
-> RH.
```

## Exact proof objects

```text
X-30201 source-flow result digest
29e2fda98df6f244f6e13a323652418e6a49824a4e92295401e5ca61c2168a20

X-30202 capacity result digest
3300081ea6a9fc2f0f495549bf189bd7f8807cf0808a17ee2c6ea671cbd26daf
```

They prove finite algebra only.

## Integration warning

Do not merge PR #301 as an RH proof unless an independently reconstructed SFC
manifest is supplied.  The analytic files may be retained separately from the
withdrawn standalone source-flow conclusion.
