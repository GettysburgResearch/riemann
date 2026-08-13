# L-91900 — A Birman–Schwinger loop detects every bound state and negative direction

Claim ID: `L-91900`  
Status: **EXACT ABSTRACT FEEDBACK/SPECTRAL-FLOW THEOREM**  
Created: 2026-08-13  
Depends on: standard Hilbert-space spectral theory  
RH status: **unproved**

## 1. Positive medium and feedback port

Let `H` and `E` be complex Hilbert spaces.  Let

\[
 A=A^*\succeq cI_{\mathcal H}
 \qquad(c>0)
\]

and let

\[
 G:\mathcal H\longrightarrow\mathcal E
\]

be bounded.  Put

\[
 V=G^*G,
 \qquad
 H=A-V.
 \tag{L-91900.1}
\]

For `kappa>=0` define the Birman--Schwinger return operator

\[
 \boxed{
 K(\kappa)
 =G(A+\kappa I)^{-1}G^*
 \succeq0.
 }
 \tag{L-91900.2}

When `G(A+kappa I)^(-1/2)` is compact, `K(kappa)` is compact.

## 2. Exact eigenvalue correspondence

For `kappa>=0`,

\[
 \boxed{
 -\kappa\in\sigma_{\rm p}(H)
 \quad\Longleftrightarrow\quad
 1\in\sigma_{\rm p}(K(\kappa)).
 }
 \tag{L-91900.3}

The geometric multiplicities agree.

Indeed, if

\[
 (A-G^*G)f=-\kappa f,
\]

then

\[
 f=(A+\kappa)^{-1}G^*Gf.
\]

The vector `y=Gf` is nonzero—otherwise `(A+kappa)f=0`—and satisfies

\[
 K(\kappa)y=y.
\]

Conversely, if `K(kappa)y=y`, then

\[
 f=(A+\kappa)^{-1}G^*y
\]

is nonzero and obeys `(A-G*G)f=-kappa f`.  The two constructions are inverse
on the corresponding eigenspaces.

## 3. Inertia at the threshold

At `kappa=0`, put

\[
 B=GA^{-1/2}.
\]

Then

\[
 \boxed{
 H=A^{1/2}(I-B^*B)A^{1/2}.
 }
 \tag{L-91900.4
}

The nonzero spectra of

\[
 B^*B
 \quad\text{and}\quad
 BB^*=K(0)
\]

agree with multiplicity.  Therefore, whenever the relevant spectrum above one
is discrete,

\[
 \boxed{
 n_-(H)
 =\#\{\lambda(K(0))>1\},
 }
 \tag{L-91900.5}

and

\[
 \ker H\ne\{0\}
 \quad\Longleftrightarrow\quad
 1\in\sigma(K(0)).
 \tag{L-91900.6}

Thus negative directions are precisely feedback gains exceeding one.

## 4. Monotone energy parameter

For `0<=kappa_1<kappa_2`, resolvent monotonicity gives

\[
 \boxed{
 K(\kappa_2)\preceq K(\kappa_1).
 }
 \tag{L-91900.7}

In norm,

\[
 \|K(\kappa_2)-K(\kappa_1)\|
 \le
 \|G\|^2
 \frac{\kappa_2-\kappa_1}
 {(c+\kappa_1)(c+\kappa_2)}.
 \tag{L-91900.8}

Hence every negative eigenvalue of `H` is a unique unit-gain crossing of a
monotone positive return family, counted with multiplicity.

## 5. Schur complement realization

The block operator

\[
 \mathcal M(\kappa)
 =\begin{pmatrix}
  A+\kappa I&G^*\\
  G&I
 \end{pmatrix}
 \tag{L-91900.9}

has Schur complements

\[
 A+\kappa-G^*G=H+\kappa
\]

and

\[
 I-G(A+\kappa)^{-1}G^*=I-K(\kappa).
\]

Consequently

\[
 \boxed{
 H+\kappa\succeq0
 \quad\Longleftrightarrow\quad
 K(\kappa)\preceq I.
 }
 \tag{L-91900.10}

This is the positive-metric small-gain form of the Birman--Schwinger principle.

## 6. Perturbation determinant and feedback entropy

If `K` is positive trace class and `0<=K<I`, then

\[
 \boxed{
 -\log\det(I-K)
 =\int_0^1
  \operatorname{tr}\bigl[K(I-tK)^{-1}\bigr]dt
 =\sum_j-\log(1-\lambda_j(K)).
 }
 \tag{L-91900.11}

Every summand is nonnegative and diverges as a feedback eigenvalue tends to
one.  The proof follows by applying

\[
 -\log(1-x)=\int_0^1\frac{x}{1-tx}dt
\]

to the eigenvalues and using monotone convergence.

For one scalar return `k in [0,1)`, the same expression is the Clark entropy
of a return amplitude of squared modulus `1-k`.

## 7. Relation to the radial firewall

`R-91900` shows that a diffuse source medium can produce a pure-point output
through a nonlocal loop.  The present theorem identifies the exact mechanism:
a feedback return operator reaches gain one.

The two viable conclusion mechanisms are now sharply separated:

```text
locality route:
    prove the completed map is an L-infinity(depth)-module map;

feedback route:
    construct the completed return operator and prove K< I.
```

Neither conclusion follows merely from positivity or diffuseness of the open
source.

## 8. Exact boundary

```text
Birman--Schwinger eigenvalue correspondence       EXACT
negative-index / gain-above-one count             EXACT
Schur-complement small-gain equivalence           EXACT
feedback entropy                                  EXACT
completed zeta feedback operator                  OPEN
strict completed small gain                       OPEN / RH-BEARING
Riemann Hypothesis                                UNPROVED
```
