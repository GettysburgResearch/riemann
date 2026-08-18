# L-97900 — The rough-product inclusion–exclusion simplex is exactly the positive Dickman function

Claim ID: `L-97900`  
Status: **PROVED EXACT ANALYTIC THEOREM**  
Created: 2026-08-18  
RH status: **not assumed**

For `u>=0`, put

\[
I_0(u)=1,
\]

and, for `k>=1`,

\[
I_k(u)=\frac1{k!}
\int_{\substack{s_1,\ldots,s_k\ge1\\s_1+\cdots+s_k\le u}}
\frac{ds_1\cdots ds_k}{s_1\cdots s_k}.
\tag{L-97900.1}
\]

The integral is zero when `k>u`. Define the finite alternating sum

\[
\mathfrak D(u)=\sum_{k=0}^{\lfloor u\rfloor}(-1)^k I_k(u).
\tag{L-97900.2}
\]

Then `mathfrak D` is the Dickman function: it is the unique continuous function
satisfying

\[
\mathfrak D(u)=1\qquad(0\le u\le1),
\]

\[
\boxed{u\mathfrak D'(u)=-\mathfrak D(u-1)}
\qquad(u>1)
\tag{L-97900.3}
\]

away from the integer knots. Moreover

\[
\boxed{u\mathfrak D(u)=\int_{u-1}^{u}\mathfrak D(v)\,dv}
\qquad(u\ge1),
\tag{L-97900.4}
\]

and therefore

\[
\boxed{\mathfrak D(u)>0\quad\text{for every finite }u\ge0.}
\tag{L-97900.5}
\]

## Proof

Differentiate `I_k` through the moving simplex boundary. Multiplying the
boundary integral by `u=s_1+...+s_k` and using symmetry gives

\[
u I_k'(u)=I_{k-1}(u-1).
\]

Summing with signs proves (L-97900.3). The two sides of (L-97900.4) have the
same derivative, and they agree at `u=1`; hence they agree for every `u>=1`.
Positivity follows inductively from (L-97900.4): it is true on `[0,1]`, and if
it is true through `u`, then its integral over `[u-1,u]` is strictly positive.

## Arithmetic interpretation

Let `z>1`, `Y=z^u`, and attach harmonic weight `1/p` to each prime `p>=z`.
The degree-`k` integral `I_k(u)` is the continuous limit of the total weight of
squarefree `k`-prime products below `Y`. Thus `mathfrak D(u)` is the exact
critical inclusion–exclusion limit of the rough-product source, including the
product activation boundary. It is not the parity-blind full Euler product.
