## T-106670 — regularized source-Pick free-energy frontier

Remote audit before this packet:

```text
PR:       #731
branch:   research/gpt56-pro/105210-simple-zero-record-and-descent
parent:   433490c133b26bce4163f4edf7ad04aeda9d33e3
state:    open, draft, mergeable
T-106610: present
T-106650: present with retained proof object
```

T-106650 identifies the exact endpoint charge as numerator values plus
truncated-Toeplitz nonnormality.  T-106670 packages that complete charge into
one positive scalar determinant.

For every mesoscopic window, cutoff `eta`, and `tau_T -> 0`, define

```text
Z_(j,eta)(tau)
  = det(G_(j,eta)-tau V_(j,eta)* G_(j,eta) V_(j,eta))
    / det G_(j,eta),

F_(T,eta) = -log prod_j Z_(j,eta)(tau_T) / tau_T.
```

Then exactly

```text
cutoff canonical charge
  <= F_(T,eta)
  <= [-log(1-tau_T)/tau_T] cutoff canonical charge.
```

The node values are literal source samples:

```text
(V_j)_rr
= B_(+,j)(b_(j,r))
= 2 i lambda_j (h D H_5-(D h) H_5)(b_(j,r)) / O_j(b_(j,r)).
```

The full determinant gate has allowance `97/1000`.  The height-paid cutoff
family has allowance

```text
97/1000 - 3/(4000 eta).
```

Hence

```text
eta=1/100 -> 11/500
eta=1/10  -> 179/2000
eta=1     -> 77/800
eta=inf   -> 97/1000.
```

The former `11/500` target is only the conservative `eta=0.01`
specialization.  The complete source-Pick determinant can use the full
`97/1000` budget.

```text
regularized determinant reduction       PROVED EXACT
source-Pick node formula                 PROVED EXACT
conditional pivot factorization          PROVED EXACT
full and cutoff gate equivalences         PROVED EXACT
Xi determinant lower bound               OPEN / 90%-BEARING
90% / density one / RH                   UNPROVED
```

Replay:

```text
PASS_T106670_REGULARIZED_PICK_FREE_ENERGY
```
