## T-106610 — exact Riemann–Siegel-gauge arithmetic endpoint

The adaptive scale is now made explicit:

```text
a_RS(t)=1/theta'(t)
       =2/log(t/2pi)+o(1/log t).
```

Writing

```text
Xi=A exp(i theta) h,
h(t)=zeta(1/2+it),
L=D+A'/A+i theta',
H_k=L^k h,
```

one has exact carrier-cancelled packets

```text
C_k=i/theta' * (D+A'/A) H_k,
R_k=2H_k-C_k,
Xi^(k)+i a_RS Xi^(k+1)=A exp(i theta) C_k,
Xi^(k)-i a_RS Xi^(k+1)=A exp(i theta) R_k.
```

Therefore the fifth-endpoint quotient is the exact arithmetic cross-ratio

```text
U_5=R_0 C_5/(C_0 R_5),
```

and its endpoint difference is

```text
R_0 C_5-C_0 R_5
=2i/theta' * (h D H_5-(D h)H_5).
```

The Xi amplitude connection cancels from the Wronskian. `H_5`, `C_5`, and
`R_5` are finite combinations of `zeta,...,zeta^(6)` with explicit
gamma/digamma coefficients.

The cofinal height theorem remains valid for this scale, so all denominator
charge above height `1/100` is paid by `3/40 N`. The remaining theorem is the
single arithmetic shallow phase mean

```text
RSGAUGE106610 < 11/500 N.
```

It implies more than 90%, but remains open. Ninety percent, density one, and
RH are not claimed.
