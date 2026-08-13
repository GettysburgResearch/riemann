# L-91338 — Every rough prime has a positive canonical return preserving both hidden ledgers

Claim ID: `L-91338`  
Status: **PROVED EXACT POSITIVE-RETURN / BOUNDED-PORT THEOREM**  
Created: 2026-08-12  
Depends on: `L-91335`, `L-91337`, `L-91333`, `L-91334`  
RH status: **unproved**

## 1. Hidden ledgers after one prime

Put

\[
 A=1-p^{-1},
 \qquad
 B=1-p^{-1/2},
 \qquad
 d=A-B>0.
\]

Start from the canonical hidden lift

\[
 I(L,R)=(L,R,L,2R)^T.
\]

After the diagonal hidden action of `L-91335`, the two positive ledgers of
`L-91337` are

\[
\boxed{
 a=m_\Psi(D_pI(L,R))=AL+2BR,
}
\tag{L-91338.1
}

and

\[
\boxed{
 b=m_S(D_pI(L,R))=A(2L+R).
}
\tag{L-91338.2
}

## 2. Unique physical state with both ledgers

Solve

\[
 L'+2R'=a,
 \qquad
 2L'+R'=b.
\]

The unique solution is

\[
\boxed{
 \binom{L'}{R'}
 =C_p\binom LR,
 \qquad
 C_p=
 \begin{pmatrix}
  A&\dfrac{2d}{3}\\[2mm]
  0&\dfrac{4B-A}{3}
 \end{pmatrix}.
}
\tag{L-91338.3
}

Indeed,

\[
 (1,2)C_p=(A,2B),
 \qquad
 (2,1)C_p=(2A,A).
\tag{L-91338.4
}

For every `p>1`,

\[
 4B-A=3-4p^{-1/2}+p^{-1}>0.
\]

Therefore

\[
\boxed{
 C_p\ge0
}
\tag{L-91338.5
}

entrywise. Every positive physical state returns to the positive `(L,R)` cone
after one rough prime while preserving both hidden target and score ledgers
exactly.

The return is canonical because the two ledger equalities determine `(L',R')`
uniquely.

## 3. Sequential rough processing

After returning to `(L',R')`, reapply the canonical injection `I` and process
the next rough prime. Thus no hidden-state distortion accumulates along a prime
path.

At every stage:

```text
least-prime hazards partition positive hidden source mass;
C_p returns each nonzero child to the positive physical cone;
SHARP-target ledger is preserved exactly;
endpoint-score ledger is preserved exactly.
```

Consequently the child coefficients from `L-91336` are the same coefficients in
both conclusion-relevant scalar ledgers.

## 4. Difference from the exact arithmetic Euler state

Let `M_p` be the exact signed arithmetic `(L,R)` matrix. Direct subtraction gives

\[
\boxed{
 C_p-M_p
 =dK,
 \qquad
 K=
 \begin{pmatrix}
  -1&8/3\\
  -1&2/3
 \end{pmatrix}.
}
\tag{L-91338.6
}

This discrepancy is the price of replacing the exact physical state by the
positive two-ledger representative. It is not charged to the inherited child
loss; it is a local observation port.

## 5. Uniform Hilbert-innovation domination

Retain the local innovation

\[
 \Delta_p=H-M_p^THM_p
\]

of `L-91333`. With `r=p^-1/2`,

\[
 \Delta_p
 =S^T\operatorname{diag}(\alpha,\beta)S,
 \qquad
 \alpha=r^2(2-r^2),
 \quad
 \beta=r(2-r).
\]

Since `beta>=alpha`,

\[
 \Delta_p\succeq\alpha H.
\]

The metric `H` has determinant one and trace seven, so

\[
 H\succeq\frac17I_2.
\]

Also

\[
 \alpha>2d^2
\]

because

\[
 2-r^2>2(1-r)^2
\]

for `0<r<1`. Finally

\[
 \|K\|_F^2=\frac{86}{9}.
\]

Therefore

\[
\begin{aligned}
 (C_p-M_p)^T(C_p-M_p)
 &\preceq\frac{86}{9}d^2I_2\\
 &\preceq\frac{301}{9}\Delta_p.
\end{aligned}
\]

Thus

\[
\boxed{
 (C_p-M_p)^T(C_p-M_p)
 \preceq\frac{301}{9}\Delta_p.
}
\tag{L-91338.7
}

The constant is deliberately crude and uniform in `p`.

## 6. One global endpoint port

For an ordered prime cascade, transform every local discrepancy back to the
common initial coordinate. The innovation telescope of `L-91333` gives

\[
\boxed{
 \sum_j E_j^*E_j
 \preceq\frac{301}{9}H,
}
\tag{L-91338.8
}

where `E_j` is the canonical-return discrepancy at stage `j`.

`L-91334` embeds `H/2` into one bounded native endpoint port. Hence the complete
canonical-return cost is still one endpoint-independent `O(1)` port per
factor-54 reset. It is not multiplied by the number of rough primes or branches.

Positive functoriality and sum-before-quantize assembly preserve this global
port domination.

## 7. Consequence

The two formerly separate open interfaces

```text
positive return of a hidden child to the (L,R) cone;
common score coefficient for target and endpoint score;
```

are closed by `C_p`.

The remaining task is now purely measure/source assembly: identify survival and
frontier packets with the resident finite forcing and outer packing, then apply
the hazard partition and canonical return pointwise before one global
quantization.

## 8. Proof boundary

```text
positive two-ledger canonical return C_p             EXACT
target-ledger preservation                            EXACT
score-ledger preservation                             EXACT
sequential recanonicalization                         EXACT
local discrepancy matrix                              EXACT
uniform Hilbert-innovation domination                 EXACT
one bounded global endpoint port                      AVAILABLE
survival/frontier source typing                       OPEN
full reset synthesis                                  NEXT
Riemann Hypothesis                                    UNPROVEN
```
