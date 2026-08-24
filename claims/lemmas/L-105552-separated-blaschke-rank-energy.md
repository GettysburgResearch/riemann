# L-105552 — Separated Blaschke rank from Hankel energy

Claim ID: `L-105552`  
Status: **PROVED EXACT FINITE MODEL-SPACE THEOREM**  
Created: 2026-08-24  
Depends on: `L-105551`; reproducing kernels of a finite model space  
RH status: **not assumed**

Let

\[
u=B_+/B_-
\]

be reduced, with `B_-` having simple zeros `b_1,...,b_m` in the disk.  Let
`e_j` be the normalized Hardy reproducing kernels at `b_j`, and let

\[
G=(\langle e_j,e_k\rangle)_{j,k=1}^m.
\]

Assume

\[
\lambda_{\min}(G)\ge\kappa>0,
\qquad
\lambda_{\max}(G)\le K,
\tag{L-105552.1}
\]

and

\[
|B_+(b_j)|\ge\varepsilon>0
\qquad(1\le j\le m).
\tag{L-105552.2}
\]

Then every nonzero singular value of `H_u` is at least

\[
\varepsilon\sqrt{\kappa/K},
\]

and hence

\[
\boxed{
 m\le
 \frac{K}{\kappa\varepsilon^2}
 \|H_u\|_{\rm HS}^2.
}
\tag{L-105552.3}
\]

## Proof

The nonzero singular values of `H_u` are those of

\[
A=M_{B_+}^*\big|_{K_{B_-}}.
\]

The kernels at the simple zeros form a basis of `K_(B_-)`, and

\[
A e_j=\overline{B_+(b_j)}e_j.
\]

For `v=sum c_j e_j`, with `D=diag(overline{B_+(b_j)})`,

\[
\|Av\|^2=(Dc)^*G(Dc)
\ge\kappa\varepsilon^2\|c\|_2^2,
\]

while

\[
\|v\|^2=c^*Gc\le K\|c\|_2^2.
\]

This gives the singular-value floor.  Summing its square over the `m`
nonzero singular values proves (L-105552.3).

The theorem identifies the two quantities which a source-specific companion
argument must control: conditioning among bad companion zeros and separation
from the reflected/good factor.  An unsigned energy estimate alone is not a
counting theorem.
