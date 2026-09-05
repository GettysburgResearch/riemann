# L-106451 — Endpoint Hermite--Bézout form has an exact CRT signature

Claim ID: `L-106451`  
Status: **PROVED EXACT FOR COPRIME SIMPLE REAL POLYNOMIALS; CONFLUENT PASSAGE BY CONTINUITY**  
Created: 2026-08-25  
Depends on: classical Hermite--Bézout inertia theorem; `L-106440`; `R-106450`  
RH status: **not assumed**

Let `p,q in R[x]` be monic, coprime and square-free.  Put

\[
A=pq,
\qquad
W=p'q-pq'.
\]

For a real polynomial pair `(f,g)` define

\[
\operatorname{Bez}(f,g)(x,y)
 ={f(x)g(y)-g(x)f(y)\over x-y}.
\]

## 1. Exact endpoint decomposition

Let

\[
\mathcal B_f(x,y)
 ={f(x)f'(y)-f'(x)f(y)\over x-y}.
\]

Direct expansion gives

\[
\boxed{
\operatorname{Bez}(A,W)(x,y)
 =q(x)q(y)\mathcal B_p(x,y)
  -p(x)p(y)\mathcal B_q(x,y).
}
\tag{L-106451.1}

This is the denominator-free leading Hermite form of the endpoint companion

\[
(p+i\lambda p')(q-i\lambda q').
\]

Indeed its real and imaginary parts are

\[
A_\lambda=pq+\lambda^2p'q',
\qquad
B_\lambda=\lambda W,
\]

so

\[
\lambda^{-1}\operatorname{Bez}(A_\lambda,B_\lambda)
 =\operatorname{Bez}(A,W)
  +\lambda^2\operatorname{Bez}(p'q',W).
\tag{L-106451.2}

When no common real event occurs, the Hermite signature is constant for
`lambda>0`; the confluent limit retains the standard multiplicity ledger.

## 2. CRT diagonalization

At a root `alpha` of `p`,

\[
{W(\alpha)\over A'(\alpha)}=+1,
\]

whereas at a root `beta` of `q`,

\[
{W(\beta)\over A'(\beta)}=-1.
\]

The Lagrange/CRT diagonalization of the Bézout form therefore assigns the
literal label

```text
+1 to the p-root fibre;
-1 to the q-root fibre.
```

Let

\[
r_p=N_\mathbb R(p),\qquad
c_p={\deg p-r_p\over2},
\]

and define `r_q,c_q` similarly.  Every real root contributes its displayed
sign.  Every nonreal conjugate pair contributes one positive and one negative
direction.  Consequently

\[
\boxed{
\begin{aligned}
n_+\bigl(\operatorname{Bez}(A,W)\bigr)
 &=r_p+c_p+c_q,\\
n_-\bigl(\operatorname{Bez}(A,W)\bigr)
 &=r_q+c_p+c_q,
\end{aligned}
}
\tag{L-106451.3}

and hence

\[
\boxed{
\operatorname{sig}\operatorname{Bez}(A,W)
 =r_p-r_q.
}
\tag{L-106451.4
}

For `q=p^(K)`, this is exactly the endpoint companion winding
`R_0-R_K`.

## 3. Relation to the resolvent frontier

The resolvent Hankel form of `T-106450` and the Hermite--Bézout form in this
lemma have the same finite half-plane index, but they are not norm-equivalent:

```text
resolvent coordinate:
  explicit pole principal parts and Cauchy Gram;

full-signature coordinate:
  polynomial coefficient matrix with literal +/- CRT fibres.
```

The second coordinate removes the invalid denominator-multiplied Hardy source.
It is the natural input for a rank--trace or Gram compression theorem.

## 4. Xi fourth endpoint

For a symmetric canonical-product truncation `p=Xi_T` and `q=p^(4)`, the
signature is

\[
\operatorname{sig}\operatorname{Bez}
 (p p^{(4)},p'p^{(4)}-p p^{(5)})
 =R_0(T)-R_4(T).
\tag{L-106451.5}

Thus the exact ninety-percent requirement is the lower signature bound

\[
\boxed{
\operatorname{sig}\operatorname{Bez}
 (p p^{(4)},p'p^{(4)}-p p^{(5)})
 >-{237\over2500}N(T)+o(N(T)).
}
\tag{L-106451.6
}

No denominator resolvent appears in this statement.

## 5. Scope

The lemma proves the signature identity, not a favorable source-basis estimate
of that signature.  Coefficientwise smallness of `W` cannot orient the form,
because positive scaling leaves its signature unchanged.  A successful proof
must construct a source-owned congruence or rank--trace estimate for the
literal matrix.