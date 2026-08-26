# T-106213 — Function-field deep-shell nonprincipal half-source closure

Claim ID: `T-106213`  
Programme aliases: `LFAM2.FF_DEEP_WITT_SHELL`, `LFAM1.NONPRINCIPAL_HALF_SOURCE_FAMILY`, `STRESS.FROBENIUS_ROUGH_SECTOR`  
Status: **PROVED UNDER AN EXPLICIT SHELL/CONDUCTOR INEQUALITY**  
Created: 2026-08-26  
Depends on: `L-106210`, `L-106213`  
Programme issues: #737, #736, #743  
Number-field RH status: **not assumed; no transfer claimed**

Let the character conductor have degree \(m\), let the complete reduced-core
shell have degree \(n\), and let \(r\le m-1\) be the degree of
\(L(u,\chi)\).

For one nonprincipal character, `L-106213` gives

\[
q^{-n}|H_{\chi,n}|
\le
C_{\chi,q}(n+1)^{r/2+2}q^{-n/2}.
\tag{T-106213.1}
\]

There are at most \(q^m\) characters modulo an irreducible conductor of degree
\(m\). Therefore the complete squared nonprincipal family shell is bounded by

\[
\boxed{
q^{m-n}
C_{m,q}^2
(n+1)^{r+4},
}
\tag{T-106213.2}
\]

where \(C_{m,q}\) is the maximum of the explicit constants in
`L-106213` over the family.

Consequently every shell satisfying

\[
\boxed{
m
+
2\log_q C_{m,q}
+
(r+4)\log_q(n+1)
\le
\frac n2
}
\tag{T-106213.3}
\]

obeys

\[
\boxed{
\mathfrak M_{\rm half}^{\rm nonprin}(m,n)
\le q^{-n/2}.
}
\tag{T-106213.4}
\]

The same conclusion applies to the fully rough stopped half-source of
`L-106210`, up to its finite prime/semiprime/triple-prime parity matrix and
polynomial shell factors.

Thus the function-field nonprincipal deep-core sector is unconditionally
closed whenever (T-106213.3) holds.

The remaining function-field obstructions are:

```text
principal member;
quadratic square-degree resonance after centering;
conductor/core-balanced shells;
incomplete physical shell and incidence-mask transport.
```

No number-field transfer or RH claim is made.
