# T-101220 — Every adverse double-owner interval has a subpower least endpoint

Claim ID: `T-101220`  
Status: **PROVED UNCONDITIONAL LOCALIZATION THEOREM; RESIDUAL ROW ESTIMATE OPEN**  
Created: 2026-08-21  
Depends on: `L-101221`

For each integer `k>=2`, let `P_k` be large enough that `L-101221` applies with exponent `A=k`. Define a nondecreasing function

\[
\mathcal A(p)=
\max\{k\ge2:p\ge P_k\},
\]

with any fixed value before `P_2`. Then

\[
\mathcal A(p)\longrightarrow\infty
\]

and every endpoint interval satisfying

\[
q\le p^{\mathcal A(p)}
\]

is pointwise nonnegative.

Consequently, if an interval with `q<=X` can contribute negatively, then

\[
q>p^{\mathcal A(p)}.
\tag{T-101220.1}
\]

For every fixed `epsilon>0`, choose `P` such that

\[
\mathcal A(p)>1/\epsilon\qquad(p>P).
\]

If also `p>=X^epsilon`, then

\[
q\le X\le p^{1/\epsilon}<p^{\mathcal A(p)},
\]

contradicting (T-101220.1). Therefore

\[
\boxed{
\max\{p:\text{an adverse interval }(p,q),\ q\le X\}
=X^{o(1)}.
}
\tag{T-101220.2}
\]

Thus the unresolved double-owner matrix is confined to subpower-many least-prime rows. Every row with a polynomial-sized least endpoint is closed pointwise.

The theorem does not estimate the remaining small-least-owner rows. Their carrier-preserving Hardy/near-collision packing remains open.

```text
all fixed-exponent intervals positive        PROVED
adverse least endpoint X^o(1)                PROVED
remaining small-owner row packing             OPEN / RH-BEARING
Riemann Hypothesis                            UNPROVEN
```
