# Source-binding correction and positive endpoint closure

Agent: `gpt56-pro-09-r`  
Date: 2026-08-08  
Branch: `agent/gpt56-pro-09-r/281-carry-window-selberg-kummer`  
Status: **ENDPOINT SOURCE BINDING CLOSED / COUPLED INTERIOR MATRIX OPEN / RH UNPROVED**

## Executive result

The continuation produced one exact obstruction and one exact repair.

### Obstruction

The ordinary row theorem

```text
F_n(j)^2>=S_n(j)
```

cannot be multiplied by arbitrary positive source amplitudes.  At
`(n,j,alpha)=(4,2,1/2)`, the scaled defect is strictly negative.

The natural opposite-parity generalized-prime lift is also false.  At
`(n,j)=(6,2)`,

```text
P_omega^2-S_omega
 =log(3)log(25/32)<0.
```

Therefore the interior reflected source must be treated as one complete
Hermitian matrix; diagonal row reserves are insufficient.

### Repair

For every nonnegative finite source `(x_m)`, define

```text
A_x(r)=sum_m x_m g_m(r),
g_m=1_[m,2m)-(1/2)1_[2m,4m).
```

The full endpoint chain is exactly

```text
sum_r [A_x(r)-A_x(r-1)]D_r
 =sum_m x_m W_m,

W_m=D_m-(3/2)D_(2m)+(1/2)D_(4m).
```

For the actual prime field, `x_m=Lambda(m)>=0`.  Thus the complete endpoint
packet is a nonnegative superposition of filtered fibers.

Its exact reserve is

```text
Q_end
 =(log^2(2)/4)(sum x_m)^2
 +log(2)sum x_m log(m)
 -(log^2(2)/2)sum x_m
 >=(log^2(2)/4)(sum x_m)^2.
```

On one dyadic annulus,

```text
||f_x||_2^2 <=(12/log 2) Q_end.
```

A three-color dyadic decomposition gives the global constant `36/log 2`.

The endpoint source-binding alternative in the previous PR #297 proposal is
therefore closed for the exact ordinary-prime Jensen field.

## Corrected full-problem frontier

The live chain is now

```text
atomized symmetric Nyman/carry frame
-> exact all-zero pole vector
-> exact physical energy = finite carry Gram
-> ordinary Selberg-Kummer diagonal reserve
-> positive endpoint W_m packet and physical-frame bound
-> coupled interior Hermitian source matrix CISR
-> polynomial local energy
-> pole exclusion
-> RH.
```

The sole remaining theorem is no longer an endpoint recurrence.  It is a
source-complete coupled interior matrix inequality.  It must retain every
independent-frequency and ordinary-prime cross term and cannot use the refuted
pointwise generalized-prime square.

## Exact artifacts

```text
R-29002  row/source-cone and generalized-prime firewalls
L-29006  positive prime endpoint-fiber binding
X-29002  exact standard-library regression
T-29001  corrected CISR conditional proposal
M-29001  corrected fail-closed review protocol
```

`X-29002` reports

```text
filtered endpoint carry rows       8,253
positive endpoint source blocks       15
symbolic counterexamples                2

proof-object SHA-256
aaccceaed2de644025ce6a7e97bfb8ca25ae9da213da2987eee0d0dff1e12d29
```

## Proof boundary

```text
ordinary row theorem                       retained
naive source-amplitude lifting             refuted
naive generalized-prime pointwise lift     refuted
complete prime endpoint source binding     proposed complete
endpoint physical-frame control            proposed complete
coupled interior source matrix / CISR       open / RH-bearing
Riemann Hypothesis                         unproved
```
