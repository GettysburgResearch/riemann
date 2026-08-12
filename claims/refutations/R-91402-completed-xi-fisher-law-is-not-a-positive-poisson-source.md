# R-91402 — The completed xi Fisher law is not a positive Poisson source

Claim ID: `R-91402`  
Status: **EXACT PRIMARY-SOURCE FIREWALL / SCOPE CORRECTION**  
Created: 2026-08-12  
Depends on: Nakamura 2015 source lock; `L-91308`, `L-91309`, `L-91312`, `L-91316`  
Corrects: the unqualified common-source reading of `T-91302` and PR #404  
RH status: **unproved**

## 1. Two positive sources that must not be conflated

The ordinary-prime safe Euler ratio has a positive compound-Poisson source.
At the scattering-score line used in `L-91307`, its first chaos is the positive
atomic measure

\[
 d\beta_a(u)
 =a\sum_{n=p^k}\Lambda(n)n^{-a-1/2}
  \delta_{\log n}(du).
\tag{R-91402.1}
\]

Separately, `L-91309` uses the completed positive probability law

\[
 \varphi_a(t)
 =\frac{\xi(1/2+a-it)}{\xi(1/2+a)}.
\tag{R-91402.2}
\]

Its score gives the completed Fisher tangent and the exact Fisher--Hankel
factorization of `L-91312/L-91316`.

Both sources are positive Hilbert-space objects. They are not the same type of
probabilistic source.

## 2. Nakamura's theorem blocks the direct Poisson identification

Put

\[
 \sigma=\frac12+a.
\]

For every unconditional safe scale `a>1/2`, one has `sigma>1`, and
(R-91402.2) is Nakamura's completed characteristic function

\[
 \Xi_\sigma(t)=\frac{\xi(\sigma-it)}{\xi(\sigma)}.
\]

Nakamura's published Theorem 1.4 proves:

\[
 \boxed{
 \Xi_\sigma\text{ is quasi-infinitely divisible but not infinitely
 divisible for every }\sigma>1.
 }
\tag{R-91402.3}
\]

A positive Poisson or general positive-Levy representation would make the law
infinitely divisible. By uniqueness of the Levy--Khintchine triplet, no such
alternative nonnegative Levy measure exists.

Consequently

\[
 \boxed{
 \text{completed xi Fisher law}
 \ne
 \text{positive prime Poisson law}
 }
\tag{R-91402.4}
\]

as convolution sources.

## 3. What this refutes

The following shortcut is false:

```text
ordinary-prime Poisson first chaos
  = completed Fisher score space
  merely because both recover a derivative of Theta_a.
```

Equality of one observed scalar tangent does not identify the source metrics or
their orthogonal complements. In particular, the Fisher auxiliary

\[
 2\mathscr E_a^*\mathscr E_a
\]

cannot yet be declared to be the unused environment of the ordinary-prime
Poisson Julia dilation.

The source-linear chaos reduction of `L-91036` does not alter this conclusion.
It says that an exactly source-linear output uses first chaos once a positive
Poisson product system has been chosen. It does not say that every positive
completed characteristic law is Poisson infinitely divisible.

## 4. Exact statements retained

The following remain exact and compatible:

```text
ordinary prime score -> tail-Hankel Julia dilation        L-91307;
gamma/pole motion -> moving-unitary covariant connection L-91306;
completed xi law -> positive Fisher source               L-91309;
Fisher score -> completed phase tangent                  L-91312;
model-space tangent -> Fisher-Hankel contraction         L-91316.
```

These are two explicit source realizations of compatible observed boundary
objects. What is not yet present is one source-ordered positive map between the
prime Poisson/Julia source and the completed Fisher-Hankel source.

## 5. Correct remaining source theorem

A valid completion must construct explicitly a renormalized contraction or
isometry

\[
 \boxed{
 \mathcal W_a:
 \mathcal H_a^{\rm prime\ Poisson}
 \oplus\mathcal H_a^{\Gamma,\rm pole,\theta}
 \longrightarrow
 L^2(P_a;H^2)
 \oplus\mathcal E_a^{\rm ren}
 }
\tag{R-91402.5}
\]

such that:

1. its visible component is the Fisher--Hankel feature `A_a` of `L-91316`;
2. it intertwines the ordinary-prime tail-Hankel and the gamma/pole connection;
3. it is compatible with the compressed delay colligation of `L-91401`;
4. it includes the two orientations and the bridge;
5. its positive defect is identified, with coefficient one, with the corrected
   delayed screw/Weil Gram.

This is a Julia/Wick/Green renormalization problem, not an identity of Levy
measures.

## 6. Exact boundary

```text
ordinary-prime source is positive compound Poisson      EXACT
completed xi Fisher law is a positive probability law  EXACT
completed xi law is not infinitely divisible at a>1/2  IMPORTED PROVED
completed xi law is quasi-infinitely divisible          IMPORTED PROVED
direct Poisson = Fisher source identification            REFUTED
parallel prime and Fisher Hardy colligations              EXACT
renormalized Poisson/Julia -> Fisher-Hankel map           OPEN
positive renormalized defect = delayed screw Gram         OPEN / RH-BEARING
Riemann Hypothesis                                        UNPROVED
```
