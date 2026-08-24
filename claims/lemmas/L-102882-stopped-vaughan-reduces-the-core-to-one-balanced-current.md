# L-102882 — The stopped Vaughan source reduces to one balanced current

Claim ID: `L-102882`  
Status: **PROVED EXACT CONJUNCTIVE REDUCTION**  
Created: 2026-08-24  
Depends on: `L-102868--L-102881`; `L-102733`  
RH status: **not assumed**

For each second owner prime `q`, let `E_q(Y)` denote the endpoint,
carrier-recombined conclusion cost of the literal stopped square-core source at
scale `Y`.  The cost may be taken to be the centered radial gauge or the
logarithmic negative-mass envelope after all already-frozen source/gauge
recombinations.

Let `B_q(Y)` denote the same cost restricted to the exact balanced Type-II
source `mathcal B_(p,q)` of `L-102868.1`.

## 1. One-step inequality

The coefficient-exact stopped Vaughan decomposition, the favorable Type-I
square of `L-102880`, and subadditivity give

\[
\boxed{
E_q(Y)
\le
B_q(Y)
+C_RY^{-1/6}
+C(\log(2Y))^2
\sum_{\ell\ge q}{1\over\ell}
E_\ell(Y/\ell^2).
}
\tag{L-102882.1}

Only support-active primes occur.  The last term is the literal smooth-boundary
source, not a source-mass proxy.

## 2. Ordered-prime solution

Assume the balanced row is uniformly subpower:

\[
\boxed{
B_q(Y)\ll_\varepsilon Y^\varepsilon
\quad\text{for every }q.
}
\tag{L-102882.2}

Iterate (L-102882.1).  Every boundary history has nondecreasing prime labels,
so `L-102881.4` bounds the complete path mass by

\[
\prod_{\ell\ge q}(1-\ell^{-1-2\varepsilon})^{-1}
\le\zeta(1+2\varepsilon).
\]

The finitely many prefix logarithms may be absorbed by replacing `epsilon` by
`epsilon/2`.  Consequently

\[
\boxed{
E_q(Y)\ll_\varepsilon Y^\varepsilon
\quad\text{for every }q.
}
\tag{L-102882.3
\]

## 3. Exact new gate

Define

```text
BCQDSP102882:
  uniformly in the second owner q, the carrier-recombined stopped balanced
  Type-II current of L-102868.3 has subpower logarithmic negative/radial cost
  after the exact adaptive nonzero owner phases.
```

Then

\[
\boxed{
\mathrm{BCQDSP}_{102882}
\Longrightarrow
\mathrm{BQSP}_{102870}
\Longrightarrow
\mathrm{RH}.
}
\tag{L-102882.4}

The first implication uses no unstopped lattice and no independent smooth-
boundary hypothesis.  The unrestricted Type-I adverse part and every ordered
boundary history are already closed by `L-102880--L-102881`.

Thus the coherent squareclass frontier can be attacked entirely in the literal
balanced Vaughan coordinates.