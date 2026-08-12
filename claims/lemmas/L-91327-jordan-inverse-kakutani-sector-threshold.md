# L-91327 — The Jordan inverse has a sharp Kakutani sector threshold and no critical product-translation representation

Claim ID: `L-91327`  
Status: **EXACT PRODUCT-SECTOR THEOREM; INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-12  
Depends on: `L-91325/L-91326`; von Neumann's criterion for incomplete tensor products; the prime number theorem  
RH status: **unproved**

## 1. Local inverse vector on a vertical line

Fix \(0<\omega<1/2\) and a vertical line \(\Re s=\sigma>\omega\). For a prime \(p\), put

\[
 a_p=p^{-(\sigma-\omega)},
 \qquad
 b_p=p^{-(\sigma+\omega)},
 \qquad
 0<b_p<a_p<1.
 \tag{L-91327.1}
\]

With \(z=e^{-it\log p}\), the local factor of the signed Jordan inverse is

\[
 D_{p,\omega,\sigma}(z)
 =\frac{1-a_pz}{1-b_pz}
 =1-(a_p-b_p)\sum_{k\ge1}b_p^{k-1}z^k.
 \tag{L-91327.2}
\]

Regard this as a vector in \(H^2(\mathbb D)\). Its exact norm is

\[
 \boxed{
 N_p^2
 :=\|D_{p,\omega,\sigma}\|_{H^2}^2
 =1+\frac{(a_p-b_p)^2}{1-b_p^2}.
 }
 \tag{L-91327.3}
\]

Let

\[
 \widehat D_p=N_p^{-1}D_{p,\omega,\sigma},
 \qquad
 \Omega_p=1.
 \tag{L-91327.4}
\]

Then the local vacuum overlap is positive and equals

\[
 \langle\Omega_p,\widehat D_p\rangle=N_p^{-1}.
 \tag{L-91327.5}
\]

## 2. Exact incomplete-tensor-product threshold

The product vector \(\bigotimes_p\widehat D_p\) belongs to the incomplete tensor product based at the vacuum \(\bigotimes_p\Omega_p\) exactly when

\[
 \sum_p\left(1-N_p^{-1}\right)<\infty.
 \tag{L-91327.6}
\]

Since

\[
 1-N_p^{-1}
 =\frac12p^{-2(\sigma-\omega)}(1+o(1)),
 \tag{L-91327.7}
\]

we obtain the sharp phase transition

\[
 \boxed{
 \bigotimes_p\widehat D_p
 \text{ is in the vacuum sector}
 \iff
 \sigma>\frac12+\omega.
 }
 \tag{L-91327.8}
\]

At the line used by the completed horizontal Xi quotient, namely \(\sigma=\frac12\), the inverse product sector is disjoint from the safe vacuum for every \(0<\omega<1/2\).

## 3. Exact local translation overlap

Let \(U_{p,t}\) be the prime-log translation

\[
 (U_{p,t}F)(z)=F(e^{-it\log p}z).
 \tag{L-91327.9}
\]

Put

\[
 A_p=(a_p-b_p)^2,
 \qquad
 r_p=b_p^2,
 \qquad
 \vartheta_p=t\log p.
 \tag{L-91327.10}
\]

The normalized overlap is

\[
 \boxed{
 q_p(t)
 :=\langle\widehat D_p,U_{p,t}\widehat D_p\rangle
 =\frac{
 1+A_pe^{-i\vartheta_p}/(1-r_pe^{-i\vartheta_p})
 }{N_p^2}.
 }
 \tag{L-91327.11}
\]

A direct calculation gives

\[
 \boxed{
 1-|q_p(t)|^2
 =
 \frac{
 2A_p(1-\cos\vartheta_p)
 \bigl(1+a_p^2b_p^2-2a_pb_p^3\bigr)
 }{
 (1+a_p^2-2a_pb_p)^2
 \bigl(1-2b_p^2\cos\vartheta_p+b_p^4\bigr)
 }.
 }
 \tag{L-91327.12}
\]

All factors other than \(A_p(1-\cos\vartheta_p)\) tend to one.

## 4. Translation disjointness on the critical line

At \(\sigma=\frac12\),

\[
 A_p=p^{-1+2\omega}(1+o(1)).
 \tag{L-91327.13}
\]

For every fixed \(t\ne0\), the prime number theorem gives

\[
 \sum_p p^{-1+2\omega}
 \bigl(1-\cos(t\log p)\bigr)=\infty.
 \tag{L-91327.14}
\]

Indeed, partial summation gives a nonoscillatory main term of size

\[
 \frac{X^{2\omega}}{2\omega\log X},
\]

whereas the oscillatory term has leading coefficient of modulus
\((4\omega^2+t^2)^{-1/2}<(2\omega)^{-1}\).

By (L-91327.12),

\[
 \sum_p\left(1-|q_p(t)|\right)=\infty
 \qquad(t\ne0).
 \tag{L-91327.15}
\]

Thus the critical inverse product state and its nontrivial translate are not strongly equivalent. In particular there is no strongly continuous product-unitary representation of physical log-translation in that incomplete tensor sector.

## 5. Architectural consequence

A finite-dimensional, prime-independent, or separately tensored gamma/theta reservoir cannot change this conclusion: restriction of any proposed completed representation to the prime tensor algebra would still make the two disjoint prime representations equivalent.

Therefore the critical completion cannot be obtained by

```text
safe prime product in its vacuum sector
+ an independent archimedean tensor factor
+ a strong critical-line limit.
```

A viable construction must entangle the all-prime tail with the gamma/theta channel before Hilbert completion, or work as an unbounded sector-changing map from a rigged cylinder space.
