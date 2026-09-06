# L-91328 — The all-prime Jordan inverse exists canonically as a cylinder distribution and has an exact Dirichlet–Hardy threshold

Claim ID: `L-91328`  
Status: **EXACT ALGEBRAIC DISTRIBUTION AND HILBERT-REGULARITY THEOREM**  
Created: 2026-08-12  
Depends on: `L-91311/L-91325/L-91326`  
RH status: **unproved**

## 1. Canonical cylinder distribution

For each prime \(p\), let \(\mathcal P_p=\mathbb C[z_p]\) with vacuum functional

\[
 \varepsilon_p\!\left(\sum_{k\ge0}c_kz_p^k\right)=c_0.
 \tag{L-91328.1}
\]

For a finite prime set \(P\), define

\[
 D_{\omega,P}
 =\prod_{p\in P}
 \frac{1-p^\omega z_p}{1-p^{-\omega}z_p}
 \tag{L-91328.2}
\]

as a formal geometric series in the variables \(z_p\). Every local factor has constant coefficient one.

Let \(\mathcal P_{\rm cyl}\) be the algebraic tensor product of the \(\mathcal P_p\), so every test polynomial depends on only finitely many primes. For \(\Phi\in\mathcal P_{\rm cyl}\), choose a finite set \(S\) containing all primes occurring in \(\Phi\) and put

\[
 \boxed{
 \langle\mathfrak d_\omega^{\rm cyl},\Phi\rangle
 :=
 \left\langle D_{\omega,S},\Phi\right\rangle_S.
 }
 \tag{L-91328.3}
\]

If \(P\supset S\), every new factor is removed by its vacuum functional, so the value is unchanged. Hence (L-91328.3) defines a canonical all-prime cylinder distribution without any limiting choice:

\[
 \boxed{
 \mathfrak d_\omega^{\rm cyl}
 =\underset{P}{\operatorname{proj\!\!\!-lim}}\;D_{\omega,P}.
 }
 \tag{L-91328.4}
\]

The definition of the global Wick input in `T-91306` is therefore algebraically closed; only its topological/Hilbert realization remains open.

## 2. Multiplicative coefficients

Writing

\[
 D_\omega(s)
 =\sum_{n\ge1}\frac{d_\omega(n)}{n^s},
 \tag{L-91328.5}
\]

one has

\[
 d_\omega(1)=1,
 \qquad
 d_\omega(p^k)
 =-(p^{2\omega}-1)p^{-k\omega}
 \quad(k\ge1),
 \tag{L-91328.6}
\]

and multiplicativity over distinct primes.

## 3. Exact weighted Dirichlet–Hardy norm

For a real parameter \(\sigma\), define

\[
 \|D_\omega\|_{\mathscr H^2_\sigma}^2
 :=\sum_{n\ge1}|d_\omega(n)|^2n^{-2\sigma}.
 \tag{L-91328.7}
\]

Formal Euler factorization gives

\[
 \boxed{
 \|D_\omega\|_{\mathscr H^2_\sigma}^2
 =
 \prod_p
 \left[
 1+
 \frac{(p^{2\omega}-1)^2p^{-2(\sigma+\omega)}}
      {1-p^{-2(\sigma+\omega)}}
 \right].
 }
 \tag{L-91328.8}
\]

The local excess is

\[
 p^{-2(\sigma-\omega)}(1+o(1)),
 \tag{L-91328.9}
\]

so

\[
 \boxed{
 D_\omega\in\mathscr H^2_\sigma
 \iff
 \sigma>\frac12+\omega.
 }
 \tag{L-91328.10}
\]

At the useful checks

\[
 \boxed{
 \text{local norm at }\sigma=\omega:
 \quad
 1+\sum_{k\ge1}|d_\omega(p^k)|^2p^{-2k\omega}
 =\frac{2}{1+p^{-2\omega}},
 }
 \tag{L-91328.11}
\]

and

\[
 \boxed{
 \text{local norm at }\sigma=0:
 \quad
 1+\sum_{k\ge1}|d_\omega(p^k)|^2
 =p^{2\omega}.
 }
 \tag{L-91328.12}
\]

Thus the explosive all-detail normalization found in `L-91326` is the exact ordinary Dirichlet–Hardy norm growth.

## 4. Rigged-space consequence

The global inverse is simultaneously:

```text
an exact algebraic cylinder distribution;
a Hilbert vector on every line sigma > 1/2 + omega;
not a Hilbert vector at or left of the threshold;
not a vector in the critical Xi prime product sector.
```

A correct Wick-to-Hardy theorem must therefore specify a rigging and an unbounded sector-changing closure. Treating the cylinder distribution as an ordinary vector is not a harmless abuse of notation.
