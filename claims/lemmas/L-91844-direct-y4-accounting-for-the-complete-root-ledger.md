# L-91844 — Direct `Y_4` accounting closes the complete root ledger without a benchmark bridge

Claim ID: `L-91844`  
Status: **PROVED DIRECT COST COMPILATION ON THE FROZEN PR #487 ESTIMATES**  
Created: 2026-08-15  
Primary inputs: `L-91378`, `L-19885`, `L-19887`, `L-91756`, `L-91843`  
Forbidden input: any eventual upper bound for `J_Lambda(X)-4sqrt(X)`  
RH status: **unproved**

Let

\[
 \delta_X=\langle Y_4,r_X\rangle.
\]

## 1. Named root-slack classes

The one-shot specialization of `L-91843` gives the disjoint decomposition

\[
 r_X=r_X^{\rm thin}+r_X^{\rm nonterm}
     +r_X^{\rm term}+r_X^{\rm omit}.
\tag{L-91844.1}
\]

There is no unnamed baseline term. Hall, first-owner and causal-colour
operations are exact in the total row. The matrix port is zero in PR #487 and
would have zero `Y_4` coordinate in the portful specialization.

## 2. Exact numerical ledger

For integer `X>=10^12`, the frozen inputs give

\[
\langle Y_4,r_X^{\rm thin}\rangle<12012,
\tag{L-91844.2}
\]

\[
\langle Y_4,r_X^{\rm nonterm}\rangle<4,
\tag{L-91844.3}
\]

\[
\langle Y_4,r_X^{\rm term}\rangle<48972,
\tag{L-91844.4}
\]

and

\[
\langle Y_4,r_X^{\rm omit}\rangle<1.
\tag{L-91844.5}
\]

Therefore

\[
\boxed{
 0\le\delta_X<12012+4+48972+1=60989<61000.
}
\tag{L-91844.6}
\]

## 3. No double charge

Terminal, taper and finite-base rows which are retained in the current packet
are part of `Xi(d_X)` in (L-91843.4). Only their explicitly unused comparison
vectors may occur in (L-91844.1). The same vector cannot be charged both as
current response and as slack.

Any positive port surplus is a matrix coordinate and contributes exactly zero
to the pairing.

## 4. Circularity firewall

The thinning estimate uses the unconditional positive benchmark bound

\[
 J_\Lambda(X)<16(\log2)\sqrt X
\]

from `L-19887`. It never uses

\[
 J_\Lambda(X)-4\sqrt X=O_{\rm upper}(\log X),
\]

which PR #484 correctly identifies as RH-bearing.

## 5. Boundary

```text
root Y4 classes                            explicit and disjoint
square-root thinning                       <12012
nonterminal comparison                     <4
terminal comparison                        <48972
omissions                                  <1
base/port duplicate charge                 absent
complete root slack                        <61000
RH-bearing benchmark bridge                forbidden
Riemann Hypothesis                         unproved
```
