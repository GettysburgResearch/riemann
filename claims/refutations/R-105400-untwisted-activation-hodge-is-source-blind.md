# R-105400 — The untwisted activation polymatroid alone cannot encode the native source

Claim ID: `R-105400`  
Status: **PROVED EXACT SOURCE-TYPING SEPARATOR**  
Created: 2026-08-23  
RH status: **not assumed**

The activation function

\[
\rho_T(A)=\min\left(T,\sum_{e\in A}\log p_e\right)
\]

depends only on the logarithmic lengths. It does not remember the native
coefficients, their signs, duplicate occurrence labels, or the distinction
between \(p^{-1/2}\) and \(p^{-1}\).

Already for one label, the two operators

\[
I-rS_\lambda
\qquad\text{and}\qquad
I+rS_\lambda
\]

have the same activation interval and the same untwisted toric fan. Applied to
a causal test function at \(t=\lambda\), they give

\[
f(\lambda)-rf(0)
\qquad\text{and}\qquad
f(\lambda)+rf(0),
\]

which are distinct and can have different signs.

Therefore no theorem about the untwisted activation fan, volume polynomial, or
Chow ring can by itself identify the native arithmetic source. The source must
enter as a twisted coefficient module or K-class. `L-105400` and `L-105401`
supply that repair.

A second separator is also binding: a finite Hodge sign does not imply a
cofinal physical trace estimate. The labelled primitive norm and its physical
observation are different objects. The arithmetic trace/occupancy statement
`F1PE105403` remains load bearing.
