# M-99610 — Scale-sensitive Owner Carleson Embedding (`SOCE99610`)

## Objective

Use the exact lifted state of `L-99610--L-99612`, not a collapsed prefix or an
unsigned source norm.

The conclusion-facing scalar is

\[
\mathfrak H_{67}(x)
=
\sqrt x\sum_{n\le x}\frac{g_{67}(n)}n
f_{67}(n)q(x/n).
\]

Define the integrated lifted source energy

\[
\mathscr E(X)=
\int_1^X
\sum_{n\le x}\frac{g_{67}(n)}n\mathcal V_x(n)
\frac{dx}{x}.
\]

By `L-99611`, `mathscr E(X)=O((log(2X))^2)`.  The proposed final theorem is
the source-specific boundary Carleson embedding

\[
\boxed{
\int_1^X|\mathfrak H_{67}(x)|^2\frac{dx}{x}
\le C\,[1+\mathscr E(X)]^C.
}
\tag{SOCE99610}
\]

Cauchy--Schwarz then gives

\[
\int_1^X\mathfrak H_{67}(x)^-\frac{dx}{x}
\le (\log X)^{1/2}
\left(\int_1^X|\mathfrak H_{67}(x)|^2\frac{dx}{x}\right)^{1/2}
=(\log X)^{O(1)}.
\]

Thus `SOCE99610`, via `L-99614`, implies RH.

## Why this is now a sharply typed theorem

Every input is exact and unconditional:

```text
source coefficients beta_67                         exact;
positive reciprocal trace g_67                      exact;
owner probabilities P_n                             exact;
SHARP scale q(x/n)                                  exact;
RN child source from PR #653                        exact;
outgoing owner mass <1/2                            exact;
augmented lifted energy O(log x)                    exact;
finite Harnack range below 10^8+1                   exact.
```

The missing step is solely the *incoming* Carleson embedding that prevents
many larger descendants from overdrawing one smaller owner after source
indices are summed.

## Mandatory firewalls

A valid proof may not use:

1. the alpha-child identity as the native Möbius source (PR #652 `R-99600`);
2. coefficient-only martingale variation (`R-99610`);
3. source-blind renewal `l1` contraction, whose prime mass contains
   `sum 1/p`;
4. ordinary prefix Cauchy--Schwarz, which loses a power of `X`;
5. a trace-bearing positive Julia observable;
6. the desired Harnack sign as an invariant or denominator assumption.

## Recommended attack

Work on the directed divisibility DAG with edge weights `a_x(n,d)` from
`L-99611`.  The outgoing row sum is below one half.  Seek a scale-adapted dual
potential `W_x(n)` satisfying

\[
\sum_{\substack{d\ge2\\nd\le x}}
W_x(nd)a_x(nd,d)
\le W_x(n)+\mathrm{polylogarithmic\ boundary\ deposit},
\]

with the deposit supported only where `x/n<10^8+1`, already certified positive.
A successful potential gives the required incoming Carleson estimate by
finite DAG induction.

The potential must depend on the product-boundary coordinate `x/n`; a function
of `n` alone cannot absorb the critical prime-harmonic saddle.
