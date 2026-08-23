# R-105203 — Order-three Pick positivity does not bootstrap the boundary Loewner gate

Claim ID: `R-105203`  
Status: **PROVED EXACT ABSTRACT SCOPE REFUTATION**  
Created: 2026-08-23  
Depends on: `L-105214`, `T-105220`; canonical actual-Xi Pick order-three result  
RH status: **not assumed**

The reviewed repository proves positivity of the actual-Xi infinitesimal safe
Pick matrices through packet size three, with the stated normalization and
source repairs. `BRP105220`, however, asks for positive semidefiniteness of an
explicit boundary Cauchy–Loewner kernel on **every** finite real packet.
There is no abstract bootstrap from the former packet size to the latter.

## Exact four-point separator

Consider the symmetric matrix

\[
M_4=
\begin{pmatrix}
1&-2/5&-2/5&-2/5\\
-2/5&1&-2/5&-2/5\\
-2/5&-2/5&1&-2/5\\
-2/5&-2/5&-2/5&1
\end{pmatrix}.
\tag{R-105203.1}
\]

Every one- and two-point principal submatrix is positive definite. Every
three-point principal submatrix has eigenvalues

\[
{7\over5},\quad {7\over5},\quad {1\over5},
\]

and is positive definite. But the complete four-point matrix has eigenvalues

\[
{7\over5},\quad {7\over5},\quad {7\over5},\quad -{1\over5}.
\]

Therefore

\[
\boxed{
\text{all principal packets of size }\le3	ext{ are positive}
\centernot\Longrightarrow M_4\succeq0.
}
\tag{R-105203.2}

Equivalently, the three-point principal determinants are

\[
\det M_3={49\over125}>0,
\]

while

\[
\det M_4=-{343\over625}<0.
\]

## Consequence for the Xi programme

The canonical order-three theorem remains valuable unconditional Xi
structure. It cannot, by matrix theory alone, establish either:

```text
BRP105220: all-packet positivity of the boundary Cauchy-Loewner remainder;
OPEN.OPERATOR.XI.PICK_ORDER4_PLUS: the reviewed all-order actual-Xi Pick gate.
```

Moreover, the safe-axis Pick coordinate and the finite-window remainder
`H_(F,Omega)` have different constructions. A future identification between
them must prove the exact normalization, domain and exhaustion map before any
order-three result is imported.

The correct use of the reviewed low-order Pick theorems is therefore as a
finite principal-minor check and source of candidate curvature identities, not
as an automatic proof of `BRP105220`.

## Scope

The matrix above is an abstract separator, not a counterexample built from Xi.
It proves only that no source-free packet-size bootstrap is available. Special
Xi structure could still prove all-order positivity, but that would be a new
theorem—the exact remaining burden rather than a consequence of the
three-node result.