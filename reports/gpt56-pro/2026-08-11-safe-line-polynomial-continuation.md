# Continuation: exact sign geometry of the one-safe-line Euler weights

Date: 2026-08-11  
Parent PR: #389  
RH status: **unproved**

The single-safe-line criterion has prime weights `P_k(log n)`.  Writing

```text
Q_k=2^(k+1) P_k,
```

they satisfy

```text
Q_0(t)=1+t-t^2,
Q_(k+1)(t)=(t+2k+3)Q_k(t)-t Q_k'(t).
```

Every coefficient row has exactly one sign variation.  Hence every `Q_k` has
one simple positive zero `tau_k`, the roots increase strictly, and

```text
sqrt(2k+2) < tau_k < sqrt(2k+3).
```

The weights also have the exact Gamma--Bessel representation

```text
e^-t P_k(t)
 =1/sqrt(pi) int_0^infinity q^(k+1/2)e^(-q-t^2/(4q))
   (1-t^2/(2q)) dq.
```

Thus the derivative order selects one prime-log sign boundary at
`log n=sqrt(2k+O(1))`, exactly matching the heat saddle.  This gives a sharply
structured target for summation by parts or total positivity, but no arithmetic
sign theorem yet.
