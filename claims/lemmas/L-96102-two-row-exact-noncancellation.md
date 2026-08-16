# L-96102 — Rows two and three cannot simultaneously cancel any right-half-strip zero

Claim ID: `L-96102`  
Status: **PROVED EXACT ALGEBRAIC NONCANCELLATION**  
Created: 2026-08-16  
Depends on: `L-96101`  
RH status: **not assumed**

The two cancellation polynomials are

\[
 P_2(z)=-1+2\,2^{-z}-3^{-z},
\tag{L-96102.1}
\]

and

\[
 3P_3(z)=-1-2^{-z}+5\,3^{-z}-3\,4^{-z}.
\tag{L-96102.2}
\]

Suppose both vanish and put

\[
 a=2^{-z},\qquad b=3^{-z}.
\]

Equation (L-96102.1) gives `b=2a-1`. Substitution into (L-96102.2) gives

\[
 0=-1-a+5(2a-1)-3a^2
   =-3(a-1)(a-2).
\tag{L-96102.3}
\]

If `Re(z)>0`, then `|a|=2^{-Re(z)}<1`, so neither `a=1` nor `a=2` is possible. Hence

\[
 \boxed{
 \Re z>0\quad\Longrightarrow\quad
 (P_2(z),P_3(z))\ne(0,0).
 }
\tag{L-96102.4}
\]

This exact two-row argument replaces the large-row Euler--Maclaurin noncancellation used in PR #542. No asymptotic expansion, effective row bound, or choice of a large component is required.
