# Terminal boundary breakthrough: the large source is one dyadic half-pole shell

## Executive result

The frozen terminal proposal on PR #304 cannot be repaired by correcting its source typing and continuing to sum atomic norms. The correctly inverted complete source has linear atomic norm.

However, after recombination **before** absolute values, the boundary has a much sharper exact form:

```text
complete shifted cutoff boundary
 = analytically regularized dyadic half-pole shell
 + subpower one-step shift source
 + one constant-cost collar atom.
```

The dyadic half-pole shell has a physical Euler renormalization which lowers the safe-window order by exactly one.

This is the first cancellation-preserving replacement for the rejected terminal ledger.

## Exact negative theorem

`R-30404` proves

```text
||sigma_N||_at > N/480
```

for the unique finite divisor source of the complete critical boundary. Every exact decomposition terminated by a sum of atomic norms inherits this lower bound.

Therefore the absolute terminal architecture is false.

## Exact source decomposition

`L-30405` proves

```text
H_N=P_N+E_N+C_N.
```

Here:

```text
P_N(q)=sum_(rq>N)(-1)^r/sqrt(rq),

E_N(q)=sum_(2kq-1>N)
       [(2kq-1)^(-1/2)-(2kq)^(-1/2)],

C_N(q)=-(N+1)^(-1/2)1_(2q|N+1).
```

The collar is a single divisor-source atom of norm `1/sqrt(2)`.

The shift satisfies

```text
sum_(q<=Q)sqrt(q)E_N(q)<3,
```

and its correctly inverted finite source has

```text
||sigma_shift||_at=O_epsilon(N^epsilon).
```

Thus neither the lattice shift nor the parity-cutoff mismatch carries the linear obstruction.

## Exact parity collapse

For `Re(s)>1`, infinite multiple-Möbius inversion of

```text
P_(N,s)(q)=sum_(rq>N)(-1)^r/(rq)^s
```

gives exactly

```text
Sigma_(N,s)(m)
 =m^(-s)[2^(1-s)1_(m>N/2)-1_(m>N)].
```

This follows from

```text
mu*((-1)^n)=-delta_1+2delta_2.
```

At `s=1/2`, the analytically regularized source is

```text
m^(-1/2)[sqrt(2)1_(m>N/2)-1_(m>N)].
```

It is a pure dyadic half-pole shell. It may not be treated as an absolutely summable raw source.

## Physical safe-order descent

For a compact half-pole-null window `W`, define

```text
(R_2W)(y)
 =e^(y/2)[sqrt(2)F_W(y+log2)-F_W(y)],

F_W(y)=int_(-infinity)^y e^(-u/2)W(u)du.
```

`L-30406` proves

```text
S_(N,W)(x)
 =sqrt(N)(R_2W)(x-log N)+O_W(e^(-x/2)),
```

and

```text
widehat(R_2W)(z)
 =(e^(z log2)-1)/(z-1/2) widehat W(z).
```

Therefore:

```text
compact support is preserved;
Euler error on x=log N+O(1) is O(N^-1/2);
half-pole zero order r becomes r-1 exactly.
```

The macroscopic terminal boundary is one lower-complexity physical packet, not a collection of terminal atoms.

## Consequence for the full proof graph

The corrected terminal architecture is now:

```text
high-order source packet
-> exact signed boundary recombination
-> lower-safe-order dyadic packet
   + N^o(1) shift
   + O(1) collar
   + O(N^-1/2) Euler remainder.
```

The remaining base object is the final compact zero-order parity packet. It is the same dyadic source appearing in the central-cascade, DCD, parity-comb, and WSTS routes.

Thus the repository's many surviving elementary paths have converged to one source for a structural reason, not by nomenclature.

## Honest boundary

Proved:

```text
absolute terminal closure is impossible;
all non-parity terminal channels are subpower or constant;
parity source is exactly a dyadic half-pole shell;
physical parity output lowers safe order by one.
```

Still open:

```text
control of the final zero-order parity packet;
a strict signed/lower-scale recurrence;
RH.
```

A reviewer is asked only to verify the completed proofs above. No missing theorem is presented as a reviewer exercise.
