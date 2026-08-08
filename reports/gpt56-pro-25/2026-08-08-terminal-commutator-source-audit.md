# Terminal-commutator source audit — 2026-08-08

Status: `LOAD-BEARING REFUTATION / RELATIVE REPAIR OPEN`  
Issue: #245  
PRs: #248 and #304  
Reviewed PR #304 head: `78b75fc17e27334a9950018528c1c6e083d74820`

## Executive conclusion

PR #304 contributes a useful exact lemma:

```text
E_h=T_(h+1)-T_h,
L_q(E_h)=1_(q|h+1),
||E_h||_(omega,1)<<sqrt(h+1).
```

Thus an already-isolated complete divisor source has an exact balanced split-flow
lift with controlled negative capacity.

The proposed full composition nevertheless fails. The complete first-generation
stopped-power boundary is not a polylogarithmic divisor source. It is the
macroscopic term which almost cancels the infinite analytic bank. On the prime
band

```text
X/3 < p <= X/2
```

its value is at least

```text
c log(X)/sqrt(p).
```

At the strict next half endpoint every such prime is an isolated divisor-source
coordinate. The declared atomic norm is therefore `Omega(X)`, not polylogarithmic.

The exact proof is `R-24505`; the directed mutation is `X-24505`.

## Exact stopped-power identity

For

```text
p(q)=q^(-1/2),
p_Y=p 1_(q<=Y),
ell_Y=log((Y+1)/Y),
```

the critical target is

```text
w_X=sum_(Y<X) ell_Y p_Y.
```

Let `C` be the infinite shifted central operator and `C_Y` its finite stopped
restriction. The complete first boundary is

```text
B_X
 =sum_(Y<X) ell_Y(Cp-C_Yp_Y)
 =log(X)Cp-C_Xw_X.
```

This is the source which PR #304 proposes to terminate independently.

For a prime `p` in `(X/3,X/2]`,

```text
C_Xw_X(p)=w_X(2p-1)
```

and

```text
Cp(p)
 >=(2p-1)^(-1/2)-(3p)^(-1/2)
 >(1/sqrt(2)-1/sqrt(3))/sqrt(p).
```

Hence

```text
B_X(p)>=c log(X)/sqrt(p).
```

If

```text
B_X(q)=sum_(q|m,m<=floor((X+1)/2)) sigma_m,
```

then `sigma_p=B_X(p)` on this band. Summing over primes and using the PNT gives

```text
sum_m sqrt(m)|sigma_m|=Omega(X).
```

## Why the divisor-switch estimate was misapplied

PR #286's divisor-switch estimate applies to the small finite jet/collar **after
the leading analytic and boundary channels have been kept in one relative
ledger**. It does not identify the whole boundary `B_X` with a small atomic
source.

The relation

```text
finite residual = analytic bulk - complete boundary
```

contains a large cancellation. Measuring the negative capacity of the complete
boundary before recombination destroys it.

This is the same logical distinction previously exposed by PR #303:

```text
formal/source coefficient
!=
available relative edge capacity.
```

PR #304's absolute commutator lift does not bypass that issue for the leading
boundary.

## Corrected possible repairs

The following remain logically possible.

### 1. Relative descendant-capacity matching

Bind the leading boundary source to the actual expanded central-tree capacity
of the analytic bank, and use the terminal commutator only on the unmatched
remainder.

### 2. Edgewise recombination

Construct both analytic and boundary flows first, add their coefficients on
common edges, and take negative capacity only afterward.

### 3. Leading-source subtraction

Split

```text
B_X=B_X^lead+B_X^jet
```

where `B_X^lead` is canceled exactly against the analytic bank and only
`B_X^jet` has polylog atomic norm.

### 4. Direct finite shell/cycle theorem

Avoid the separate analytic decomposition and prove the signed finite residual
or its completed dyadic shell has subpower optimized Cycle Debt.

All four repairs preserve the logarithmic/von-Mangoldt and fixed-ratio Mertens
firewalls. None is proved by PR #304.

## Relation to the central-Haar continuation

`L-24525` writes the exact finite central saturation as

```text
A_X(n)=G_X(n)-G_X(n+1)
```

for one binary-tree Haar potential. That construction performs the
analytic/boundary cancellation automatically before signs are measured. Its
remaining `CHSS` theorem is therefore a valid relative formulation, but it
remains RH-bearing and unproved.

The failed PR #304 shortcut cannot be used to declare `CHSS`, `DCCS`, `CDT`, or
WSTS routine.

## Additional positive avenue

PR #295 proves that the critical target is an exact positive mixture of
square-root hinges

```text
h_T(q)=q^(-1/2)-T^(-1/2).
```

On PR #248, the exact average-binomial-row inverse of `h_T` has been checked in
ordinary high-precision reconnaissance through `T=5,000,000` with no negative
coefficient. If the all-scale hinge positivity theorem were proved, positive
superposition would give a complete nonnegative carry certificate and RH.

This observation is not proof. The inverse formula contains the same coherent
Möbius channel, so finite positivity cannot be extrapolated.

## Exact status

```text
adjacent commutator atom                    proposed exact
single-atom O(sqrt m) capacity bound        proposed exact
complete stopped boundary polylog norm      refuted
PR #304 full composition                    blocked/rejected at current head
relative analytic-boundary repair           open / RH-bearing
central-Haar shell theorem                   open / RH-bearing
square-root hinge saturation                 open / stronger alternative
Riemann Hypothesis                           unproved
```
