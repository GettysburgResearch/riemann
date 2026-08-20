# T-100101 — Finite-completion pole-exposure route is rejected in its QPET form

Claim ID: `T-100101`  
Status: **REJECTED AS A CLOSURE ROUTE; CORRIDOR RESULTS RETAINED**  
Created: 2026-08-20  
Corrected: 2026-08-20 by `R-100103`  
Depends on: `L-100101--L-100104`; `R-100103`  
RH status: **unproved**

Let

\[
\mathcal C_{3;Z,k}=\mathscr A_{Z,k}\mathcal C_3
\]

and

\[
N_{Z,k}=\inf\{X\ge1:\mathcal C_{3;Z,k}(X)<0\},
\]

with `N_(Z,k)=infinity` if no negative point exists.

The valid retained theorems are:

1. every finite completion multiplier is zero-free in `Re z>0`;
2. every hypothetical off-line reciprocal-zeta pole survives;
3. for each fixed `k` and every `A<A_k^*`,

   \[
   \mathcal C_{3;Z,k}(X)>0
   \qquad(1\le X\le Z^A)
   \]

   for all sufficiently large `Z`;
4. selected pole residues are alternately amplified and suppressed as `Z`
   varies.

However the proposed gate

\[
\exists k\ge2:\quad
\liminf_{Z\to\infty}
\frac{\log N_{Z,k}}{\log Z}<A_k^*
\tag{QPET100101}
\]

is incompatible with item 3. Indeed item 3 implies, for every `A<A_k^*`,

\[
N_{Z,k}>Z^A
\]

for all sufficiently large `Z`, and hence

\[
\boxed{
\liminf_{Z\to\infty}
\frac{\log N_{Z,k}}{\log Z}\ge A_k^*.
}
\]

Therefore

\[
\boxed{\mathrm{QPET100101}\text{ is false as stated}.}
\]

The amplified-residue mechanism does not evade the contradiction. Throughout
the positive corridor, the level-mass upper bound keeps the complete physical
scalar of ordinary carrier size. Consequently all other pole and contour terms
must cancel any superpolynomial selected residue at the same scale; a one-pole
dominance theorem inside the corridor is false.

```text
finite completion source identity        PROVED
positive corridor to A_k^*               PROVED
finite multiplier zero-free              PROVED
residue amplification/suppression        PROVED
QPET100101 strict-liminf gate             REFUTED
inside-corridor one-pole UPE              REFUTED
Riemann Hypothesis                        UNPROVED
```

The finite-completion programme remains a useful positivity corridor and
spectral stress test, but it no longer appears in the normative closure graph
through QPET100101.
