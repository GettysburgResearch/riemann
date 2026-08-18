# T-98050 — The mesoscopic Dickman corridor is a hereditary Bellman corridor

Claim ID: `T-98050`  
Status: **UNCONDITIONAL HEREDITARY POSITIVITY THEOREM; ROOT STILL OPEN**  
Created: 2026-08-18  
Depends on: `L-98042`, `L-98050`  
RH status: **unproved**

Let

\[
U(Y,p)={\mathcal F(Y,p)\over\sqrt Y},
\qquad
u={\log Y\over\log p}.
\]

There is an absolute `c_0>0` such that for all sufficiently large `Y`, whenever

\[
2\le u\le c_0(\log Y)^{3/8}(\log\log Y)^{-3/4},
\tag{T-98050.1}
\]

one has not only `U(Y,p)>0`, but the one-prime Bellman inequality

\[
\boxed{
U(Y,p^+)\ge {1\over p}U(Y/p,p^+).
}
\tag{T-98050.2}
\]

Consequently the exact recurrence of `L-98050` gives

\[
\boxed{U(Y,p)\ge0.}
\tag{T-98050.3}
\]

Moreover the same estimate holds at every descendant obtained by deleting finitely many least primes while the descendant remains in the corridor (T-98050.1). Thus the mesoscopic region is hereditary under the native least-prime recursion.

## Proof

The continuous full-base parent and child profiles differ by

\[
a_*\left[\rho(u)-p^{-1}\rho(u-1)\right].
\]

By `L-98050`, once `p\ge 2C_Du\log(u+2)` this is at least `(a_*/2)rho(u)`. In the corridor (T-98050.1), the relation `p=\exp((\log Y)/u)` makes this condition automatic for sufficiently large `Y`.

Apply the VK comparison from `L-98042` separately to parent and child. The total discrete error in the Bellman difference is

\[
O\!\left(u\exp[-c(\log p)^{3/5}(\log\log p)^{-1/5}]\right),
\]

which is `o(rho(u))` by the same inequality used in `L-98042`. Hence the continuous margin survives and proves (T-98050.2).

## Significance

`L-98042` proves positivity state by state. This theorem proves the stronger source-faithful recursive inequality actually consumed by the Bellman architecture. Therefore every counterexample sequence must eventually leave the mesoscopic corridor before the least-prime recursion can become adverse.

The theorem does not reach fixed least prime. Iteration cannot cross a state where `log p` is too small for the VK discrepancy to be dominated by the Dickman Bellman margin. The remaining root problem is exactly that deep fixed/small-prime regime.

```text
state-wise mesoscopic positivity          PROVED
one-prime Bellman margin in corridor      PROVED
hereditary least-prime recursion there    PROVED
deep fixed/small-prime root               OPEN / RH-BEARING
GPC67 / RH                                UNPROVED
```
