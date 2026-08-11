# L-90411 — Exact Fourier and inverse-Laplacian form of a carry field

Claim ID: `L-90411`  
Title: Every integer carry field has an exact sine-transform expansion, and its complete position energy is a finite inverse-discrete-Laplacian quadratic form  
Status: **PROPOSED COMPLETE EXACT FINITE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Dependencies: elementary divisor switching, Fourier integration, and the cosecant partial-fraction identity  
Scope: any finite arithmetic source; no arithmetic estimate or RH conclusion

## 1. Prefix and carry coordinates

Let \(f\) be supported on \(\{1,\ldots,N\}\), put

\[
c=\mathbf1*f,
\qquad
C(x)=\sum_{m\le x}c(m),
\]

and define, for \(0<\theta<1\),

\[
Q_{f,N}(\theta)
=
\sum_{d\le N}f(d)
\left(
\left\lfloor\frac Nd\right\rfloor
-\left\lfloor\frac{N\theta}d\right\rfloor
-\left\lfloor\frac{N(1-\theta)}d\right\rfloor
\right).
\tag{L-90411.1}
\]

Finite divisor switching gives exactly

\[
\boxed{
Q_{f,N}(\theta)
=
C(N)-C(N\theta)-C(N(1-\theta)).
}
\tag{L-90411.2}
\]

The field is constant on each open cell
\((j/N,(j+1)/N)\).

## 2. Exact Fourier coefficients

Use the convention

\[
\widehat Q(k)=\int_0^1Q(\theta)e^{-2\pi ik\theta}\,d\theta.
\]

For \(k\ne0\), integrating the two step functions in (L-90411.2) gives

\[
\boxed{
\widehat Q(k)
=
\frac1{\pi k}
\sum_{m=1}^{N-1}
c(m)\sin\frac{2\pi km}{N}.
}
\tag{L-90411.3}
\]

The mean is

\[
\boxed{
\widehat Q(0)
=
-C(N)+\frac2N\sum_{m=1}^{N}m\,c(m).
}
\tag{L-90411.4}
\]

Thus the carry-position problem is a finite additive sine transform of the
ordinary prefix coefficient \(c=\mathbf1*f\), not of the raw source \(f\).

## 3. Finite inverse-Laplacian identity

For \(1\le a<N\), put

\[
S_a
=
\sum_{m=1}^{N-1}
c(m)\sin\frac{2\pi am}{N}.
\tag{L-90411.5}
\]

Since \(S_k\) depends only on \(k\bmod N\), Parseval and

\[
\sum_{r\in\mathbb Z}\frac1{(a+rN)^2}
=
\frac{\pi^2}{N^2\sin^2(\pi a/N)}
\tag{L-90411.6}
\]

give

\[
\boxed{
\int_0^1|Q_{f,N}(\theta)-\widehat Q(0)|^2\,d\theta
=
\frac1{N^2}
\sum_{a=1}^{N-1}
\frac{|S_a|^2}{\sin^2(\pi a/N)}.
}
\tag{L-90411.7}
\]

Including the mean,

\[
\boxed{
\int_0^1|Q_{f,N}(\theta)|^2\,d\theta
=
|\widehat Q(0)|^2
+
\frac1{N^2}
\sum_{a=1}^{N-1}
\frac{|S_a|^2}{\sin^2(\pi a/N)}.
}
\tag{L-90411.8}
\]

Equivalently, if \(Q_j\) is the value on the \(j\)-th cell,

\[
\boxed{
\frac1N\sum_{j=0}^{N-1}|Q_j|^2
=
|\widehat Q(0)|^2
+
\frac1{N^2}
\sum_{a=1}^{N-1}
\frac{|S_a|^2}{\sin^2(\pi a/N)}.
}
\tag{L-90411.9}
\]

The multiplier \(\sin^{-2}(\pi a/N)\) is the Green kernel of the
discrete circle Laplacian. Hence the positive innovation Gram has an exact
finite Green-energy realization.

## 4. Why this coordinate matters for PIG

The singular weights occur only near additive residues \(a=0\) and \(a=N\).
Away from those residues, ordinary coefficient energy is enough. Therefore
PIG is not an undifferentiated \(N\)-dimensional Gram problem: it is a
major-residue problem plus an elementary bulk.

No sign or cancellation has been asserted. In particular, (L-90411.8) does
not by itself prove PIG; it gives an exact coordinate in which the remaining
arithmetic obstruction can be isolated.
