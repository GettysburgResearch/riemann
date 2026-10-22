# R-93020 - Backward Hardy inversion requires the zero-linear boundary mode

Claim ID: `R-93020`  
Status: **EXACT SCOPE FIREWALL FOR `L-93018`**  
Created: 2026-08-15  
Corrects: any use of the infinite backward-Hardy formula without proving \(C(N)=o(N)\) or retaining the finite boundary term  
Scope: the discrete transform boundary only; no objection to the compact-Q4 application, where the PNT supplies the required limit

## 1. The boundary term is load bearing

For an arbitrary coefficient sequence, `L-93018` proves the finite identity

\[
\begin{aligned}
C(N)
={}&
M(N)
-
2(N+1)
\sum_{k=N}^{K}
\frac{M(k)}{(k+1)(k+2)}\\
&+
2(N+1)
\frac{S(K)}{(K+1)(K+2)}.
\end{aligned}
\tag{R-93020.1}
\]

The final term can be removed only when

\[
\frac{S(K)}{(K+1)(K+2)}\longrightarrow0.
\tag{R-93020.2}
\]

The sufficient condition used in `L-93018` is

\[
C(K)=o(K).
\tag{R-93020.3}
\]

## 2. Exact counterexample to boundary-free inversion

Take

\[
c(n)=1
\qquad(n\ge1).
\tag{R-93020.4}
\]

Then

\[
C(N)=N,
\qquad
M(N)=1,
\qquad
S(K)=\frac{K(K+1)}2.
\tag{R-93020.5}
\]

The normalized boundary tends to

\[
\frac{S(K)}{(K+1)(K+2)}
\longrightarrow\frac12.
\tag{R-93020.6}
\]

If the boundary term were incorrectly discarded, the proposed infinite
formula would give

\[
1
-
2(N+1)
\sum_{k=N}^{\infty}
\frac1{(k+1)(k+2)}
=
1-2=-1,
\tag{R-93020.7}
\]

whereas the true prefix is \(C(N)=N\).

Restoring the boundary contributes

\[
2(N+1)\cdot\frac12=N+1,
\]

and recovers \(N\) exactly.

## 3. Correct Q4 scope

For the compact-Q4 source,

\[
C_\circ(N)
=
\psi(N)-4\psi(N/4)+O(\log N).
\]

The unconditional prime number theorem gives

\[
C_\circ(N)=o(N).
\]

Therefore the boundary-free formula of `L-93018` is valid for the actual Q4
application. The firewall rejects only a source-free use of that formula.

## 4. Lifecycle instruction

Any future backward-Hardy application must provide one of:

```text
a retained finite boundary term;
a proof that C(N)=o(N);
a stronger explicit boundary decay.
```

A Chebyshev bound \(C(N)=O(N)\) does not suffice.
