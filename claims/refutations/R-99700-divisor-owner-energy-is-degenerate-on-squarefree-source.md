# R-99700 — Divisor-owner quadratic variation is identically blind on the squarefree Möbius sector

Claim ID: `R-99700`  
Status: **PROVED EXACT MECHANISM REFUTATION**  
Created: 2026-08-20  
Depends on: `L-99701`  
RH status: **not assumed**

A tempting conclusion from `L-99701` is that the logarithmic quadratic variation of the owner martingale should pay the negative mass of the SHARP scalar. That implication is false.

Let `n` be squarefree and not divisible by `67`. Then

\[
g(n)=1,
\qquad
f(n)=\beta(n)=\mu(n)\in\{+1,-1\}.
\]

Every prime-power divisor admitted by the owner kernel is then a prime `p\mid n`, and

\[
f(n/p)=-f(n).
\]

Consequently every summand in the one-step martingale energy vanishes:

\[
\boxed{
D(n)=\sum_{p\mid n}\mathbb P_n(p)
\bigl(f(n/p)+f(n)\bigr)^2=0.
}
\tag{R-99700.1}
\]

The adjusted martingale `(-1)^t f(N_t)` is deterministic along the complete squarefree divisor chain. Its quadratic variation is zero even when `f(n)=-1`.

This is not a negligible exceptional set. The squarefree sector is exactly the main reciprocal-zeta/Möbius source. A source measure supported on any negative squarefree state has

```text
negative signed observation;
zero within-state owner quadratic variation.
```

Therefore no inequality of the form

\[
\text{negative scalar mass}
\le C\times
\text{divisor-owner quadratic variation}
\]

can hold without an additional cross-source transport or prime-birth mechanism.

The valid use of `L-99701` is narrower: it controls repeated-prime uncertainty and supplies the correct source ownership. It cannot manufacture cancellation between distinct squarefree integers.

This firewall rules out a false completion of `OMCE98920` and of the first version of the owner-Green idea. The repaired construction must include edges that **add** prime powers and therefore connect different source integers; `L-99702` supplies that exact reversible network.