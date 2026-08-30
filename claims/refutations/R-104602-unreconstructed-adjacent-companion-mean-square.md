# R-104602 — The advertised adjacent-companion 92.18% transfer is not reconstructed

Claim ID: `R-104602`  
Status: **BINDING PUBLICATION AND IMPORT FIREWALL**  
Created: 2026-08-26  
RH status: **unproved**

## 1. The issue

An earlier response advertised an implication

\[
\alpha_3>0.9873\Longrightarrow \alpha_2>0.9218
\]

through a one-piece mollified mean square for

\[
Q(x)=(1-x)(1-2x)^2.
\]

That statement is not presently a theorem on the live branch.

The actual `T-104600` files on PR #720 concern the persistence--Mellin
reverse-Rolle frontier. They do not contain the advertised adjacent-companion
mean-square theorem, its proof, or a source lock for the asserted `4/7`-length
formula.

## 2. Why the missing import is load-bearing

Conrey's published variational theorem is not an arbitrary-polynomial black
box. Its test polynomial enters through

\[
q_m(x)=\phi(x)(1-2x)^m
\]

with

\[
\phi(0)=1,\qquad \phi'(x)=\phi'(1-x),
\]

and through a separately optimized mollifier. The mean-square functional,
endpoint terms, derivative normalization, mollifier length, and error
uniformity must all be derived for the exact companion being counted.

Merely displaying `Q(x)` does not establish that the proposed companion has
the claimed mean square.

## 3. Binding disposition

```text
advertised 98.73% -> 92.18% implication        UNPUBLISHED / UNVERIFIED
arbitrary-Q short-window mean-square import     NOT RECONSTRUCTED
Conrey's original fixed-order theorem            VALID PRIMARY SOURCE
T-104620 explicit direct certificates            CONTROLLING RECONSTRUCTION
Riemann Hypothesis                               UNPROVED
```

No later integration should cite the 92.18% number unless a separate frozen
line-by-line proof of its precise mean-square theorem is deposited and reviewed.
