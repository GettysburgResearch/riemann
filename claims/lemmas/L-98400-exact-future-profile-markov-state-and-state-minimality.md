# L-98400 — Exact future-prime quotient state and an \(\Omega(\sqrt N)\) state-minimality theorem

Claim ID: `L-98400`  
Status: **PROVED EXACT FINITE-STATE THEOREM**  
Created: 2026-08-18  
Frozen base: PR #582 at `699f9f119a66823702e96fba95cc8b14b8251c60`  
RH status: **not assumed**

## 1. One quotient DAG supports both live normalizations

Fix a horizon \(N\ge1\) and put

\[
\mathcal Q_N=\left\{\left\lfloor\frac Nm\right\rfloor:1\le m\le N\right\}.
\]

For \(\alpha>0\) and a prime \(p\), define

\[
(T_{p,\alpha}f)(x)
=f(x)-p^{-\alpha}f\!\left(\left\lfloor\frac xp\right\rfloor\right).
\tag{L-98400.1}
\]

The floor identity

\[
\left\lfloor
\frac{\lfloor N/m\rfloor}{p}
\right\rfloor
=
\left\lfloor\frac{N}{mp}\right\rfloor
\tag{L-98400.2}
\]

shows that \(T_{p,\alpha}\) preserves functions on \(\mathcal Q_N\).  Hence the complete quotient profile

\[
\boxed{
\mathbf f_N(m)=f\!\left(\left\lfloor\frac Nm\right\rfloor\right)
}
\tag{L-98400.3}
\]

is an exact finite Markov state.

Two live routes are instances of the same state:

* \(\alpha=\tfrac12\): the reciprocal-Julia boundary update;
* \(\alpha=1\): the square-root-normalized annular/native rough update.

The state has at most \(2\lfloor\sqrt N\rfloor\) distinct coordinates.

## 2. Exact transition words

For an odd squarefree integer \(q\), let

\[
T_{q,\alpha}=\prod_{p\mid q}T_{p,\alpha}.
\]

The floor operators commute, and expansion gives

\[
\boxed{
(T_{q,\alpha}f)(N)
=
\sum_{d\mid q}
\mu(d)d^{-\alpha}
 f\!\left(\left\lfloor\frac Nd\right\rfloor\right).
}
\tag{L-98400.4}
\]

No approximation or source-blind reservoir enters this identity.

## 3. State-minimality theorem

Call a linear realization exact if there are a linear map
\(\Phi: \mathbb R^{\mathcal Q_N}\to\mathbb R^D\), transition matrices
\(M_p\), and an output row \(\ell\) such that

\[
\Phi T_{p,\alpha}=M_p\Phi,
\qquad
f(N)=\ell\Phi f
\tag{L-98400.5}
\]

for every relevant odd prime \(p\) and every state \(f\).

Then

\[
\boxed{
D\ge
\#\{q\le\sqrt N:q\text{ odd and squarefree}\}.
}
\tag{L-98400.6}
\]

### Proof

Every output row \(e_N^*T_{q,\alpha}\) belongs to the row span of \(\Phi\).  By
(L-98400.4), its coefficient at
\(e_{\lfloor N/q\rfloor}^*\) is
\(\mu(q)q^{-\alpha}\ne0\), while every other divisor \(d\mid q\) is smaller
than \(q\).  Ordered by increasing \(q\), these rows form a triangular family
with nonzero diagonal.  Moreover \(q\mapsto\lfloor N/q\rfloor\) is injective
for \(q\le\sqrt N\).  The rows are therefore linearly independent.

Since odd squarefree integers have density \(4/\pi^2\),

\[
\boxed{
D\ge\left(\frac4{\pi^2}+o(1)\right)\sqrt N.
}
\tag{L-98400.7}
\]

At \(N=10^8\), the exact finite lower bound is \(D\ge4056\).

## 4. Consequence

No fixed-dimensional exact linear port can carry arbitrary future-prime
completion.  In particular, none of the following can be an exact all-scale
state by itself:

```text
one boundary number;
boundary plus one child;
a fixed moment list;
a fixed Julia/Schur matrix;
PSD plus logarithmic energy;
any other fixed-dimensional linear summary.
```

This does not prove or refute RJTE.  It proves that a successful all-scale
argument must either retain a growing quotient profile or use a genuinely
nonlinear source-specific invariant.
