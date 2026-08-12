# L-91331 — The critical Jordan inverse has a finite harmonic superselection tower and a vacuum-sector remainder

Claim ID: `L-91331`  
Status: **EXACT HARMONIC-SECTOR DECOMPOSITION; INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-12  
Depends on: `L-91327/L-91328`; elementary Hardy-space estimates and the prime number theorem  
RH status: **unproved**

## 1. Local logarithm

Fix

\[
0<\omega<\frac12
\]

and work on the critical vertical line \(\Re s=\frac12\). For a prime \(p\), put

\[
a_p=p^{-1/2+\omega},
\qquad
b_p=p^{-1/2-\omega},
\qquad
0<b_p<a_p<1.
\tag{L-91331.1}
\]

With \(z=e^{-it\log p}\), the local factor of the signed Jordan inverse is

\[
D_{p,\omega}(z)
=
\frac{1-a_pz}{1-b_pz}.
\tag{L-91331.2}
\]

Its logarithm in the unit disk is

\[
\boxed{
\log D_{p,\omega}(z)
=
-\sum_{k\ge1}h_{p,k}z^k,
\qquad
h_{p,k}
=
\frac{a_p^k-b_p^k}{k}>0.
}
\tag{L-91331.3}
\]

The \(k\)-th harmonic therefore has prime-space square mass

\[
\sum_p h_{p,k}^2.
\tag{L-91331.4}
\]

Since

\[
h_{p,k}
=
\frac1k p^{-k(1/2-\omega)}
\left(1-p^{-2k\omega}\right),
\tag{L-91331.5}
\]

the prime number theorem gives the sharp criterion

\[
\boxed{
\sum_p h_{p,k}^2<\infty
\iff
k(1-2\omega)>1.
}
\tag{L-91331.6}
\]

Equality belongs to the divergent side because \(\sum_p p^{-1}=\infty\).

## 2. Finite number of non-Fock harmonics

Define

\[
\boxed{
K_\omega
=
\left\lfloor\frac1{1-2\omega}\right\rfloor.
}
\tag{L-91331.7}
\]

Then precisely the harmonics

\[
1\le k\le K_\omega
\tag{L-91331.8}
\]

fail the square-summability test, while all \(k>K_\omega\) are square summable.

Consequences:

\[
0<\omega<\frac14
\quad\Longrightarrow\quad
K_\omega=1,
\tag{L-91331.9}
\]

and

\[
\omega=\frac14
\quad\Longrightarrow\quad
K_\omega=2.
\tag{L-91331.10}
\]

Thus the critical representation change is never an uncontrolled infinity of independent infrared species. At each fixed \(\omega\) it is a finite harmonic charge tower.

## 3. Exact charge extraction

Put

\[
C_{p,K}(z)
=
\exp\left(
-\sum_{k=1}^{K}h_{p,k}z^k
\right)
\tag{L-91331.11}
\]

and

\[
R_{p,K}(z)
=
D_{p,\omega}(z)C_{p,K}(z)^{-1}
=
\exp\left(
-\sum_{k>K}h_{p,k}z^k
\right).
\tag{L-91331.12}
\]

For \(K=K_\omega\),

\[
\boxed{
D_{p,\omega}=C_{p,K_\omega}R_{p,K_\omega}.
}
\tag{L-91331.13}
\]

The first factor contains every non-square-summable harmonic. The second is a vacuum-sector perturbation.

## 4. Vacuum-sector estimate for the remainder

Let

\[
q_{p,K}(z)
=
-\sum_{k>K}h_{p,k}z^k.
\]

For large \(p\),

\[
\|q_{p,K}\|_{H^2}^2
=
\sum_{k>K}h_{p,k}^2
\ll_{\omega,K}
p^{-2(K+1)(1/2-\omega)}
\tag{L-91331.14}
\]

and

\[
\|q_{p,K}\|_{H^\infty}
\le
\sum_{k>K}h_{p,k}
\ll_{\omega,K}
p^{-(K+1)(1/2-\omega)}.
\tag{L-91331.15}
\]

Since

\[
e^q-1=q\int_0^1e^{tq}\,dt,
\]

\[
\|R_{p,K}-1\|_{H^2}
\le
e^{\|q_{p,K}\|_\infty}\|q_{p,K}\|_{H^2}.
\tag{L-91331.16}
\]

For \(K=K_\omega\),

\[
(K_\omega+1)(1-2\omega)>1,
\]

and therefore

\[
\boxed{
\sum_p
\|R_{p,K_\omega}-1\|_{H^2}^2
<\infty.
}
\tag{L-91331.17}
\]

The constant coefficient of every \(R_{p,K}\) is one. If
\(\widehat R_{p,K}=R_{p,K}/\|R_{p,K}\|_{H^2}\), then

\[
1-\langle1,\widehat R_{p,K}\rangle
=
1-\|R_{p,K}\|_{H^2}^{-1}
\le
\frac12\|R_{p,K}-1\|_{H^2}^2.
\tag{L-91331.18}
\]

Hence

\[
\boxed{
\bigotimes_p\widehat R_{p,K_\omega}
}
\]

belongs to the ordinary vacuum incomplete tensor product.

## 5. Prime-zeta form on a safe half-plane

Let

\[
P(s)=\sum_p p^{-s}
\]

denote the prime zeta function in \(\Re s>1\). There,

\[
\boxed{
\log\frac{\zeta(s+\omega)}{\zeta(s-\omega)}
=
-\sum_{k\ge1}
\frac{
P(k(s-\omega))-P(k(s+\omega))
}{k}.
}
\tag{L-91331.19}
\]

The first \(K_\omega\) summands are exactly the global harmonic charges of
(L-91331.3), and the tail defines the vacuum-sector remainder before analytic continuation.

Equation (L-91331.19) is used only in its absolutely convergent region. Continuing it termwise through prime-zeta singularities is not justified and is not part of this theorem.

## 6. Preferred cofinal sequence

For a proof of RH it is enough to establish innerness on any predetermined sequence
\(\omega_j\downarrow0\). Choose

\[
\boxed{
\omega_j=2^{-j-3},
\qquad j=0,1,2,\ldots.
}
\tag{L-91331.20}
\]

Then \(0<\omega_j\le1/8<1/4\), so

\[
\boxed{
K_{\omega_j}=1
\quad\text{for every }j.
}
\tag{L-91331.21}
\]

Thus the full cofinal RH proposal may be formulated with one divergent prime harmonic species at every scale, plus an ordinary Fock remainder.

## 7. Architectural consequence

The phrase “one pole bridge” in `T-91307` concerns the single physical Mellin pole of the free endpoint. The present theorem identifies a different object: the superselection charge of the prime inverse representation.

For the preferred cofinal sequence, the corrected source geometry is

```text
one non-Fock first-harmonic prime charge field;
one ordinary vacuum-sector prime remainder;
one physical archimedean pole bridge;
the theta/Brownian/Poisson/p=2 positive reserves.
```

A finite-dimensional bridge cannot by itself erase the prime superselection charge. The completion must either use the sector bundle of `L-91332` or construct an equivalent infravacuum/rigged representation.
