# L-105431 — Exact degree-two F1 Hodge decomposition of the unordered pair current

Claim ID: `L-105431`

Status: **PROVED EXACT CODIMENSION-TWO LEFSCHETZ DECOMPOSITION**

Let \(m\ge4\), let \(H\) be a real Hilbert space, and attach a vector
\(v_{ij}=v_{ji}\in H\) to every unordered pair \(1\le i<j\le m\).  In the
application, \(H\) is the two-coordinate block space for the homotopy-coherent
outer current and \(v_{ij}\) is the current owned by the labelled prime pair
\(\{i,j\}\).

Put

\[
S=\sum_{i<j}v_{ij},
\qquad
r_i=\sum_{j\ne i}v_{ij},
\qquad
M=\binom m2.
\]

Define

\[
\mu=\frac{S}{M},
\]

\[
u_i
=
\frac{r_i-\frac2mS}{m-2},
\qquad
\sum_i u_i=0,
\]

and

\[
w_{ij}=v_{ij}-\mu-u_i-u_j.
\]

Then

\[
\sum_{j\ne i}w_{ij}=0
\qquad(1\le i\le m).
\tag{L-105431.1}
\]

## 1. Orthogonal edge decomposition

The constant, star and cycle pieces are mutually orthogonal in
\(\ell^2(\binom{[m]}2;H)\), and

\[
\boxed{
\sum_{i<j}\|v_{ij}\|^2
=
M\|\mu\|^2
+
(m-2)\sum_i\|u_i\|^2
+
\sum_{i<j}\|w_{ij}\|^2.
}
\tag{L-105431.2}
\]

The three pieces are:

```text
constant pair degree:  mu;
shared-owner stars:    u_i+u_j;
four-label cycle:      w_ij with every row sum zero.
```

## 2. Toric codimension-two intersection form

Use the prime-box Chow ring

\[
A^\bullet
=
\mathbb R[x_1,\ldots,x_m]/(x_1^2,\ldots,x_m^2)
\]

and an ample class

\[
\omega=\sum_i a_i x_i,\qquad a_i>0.
\]

After absorbing the \(a_i\) into the coefficient vectors, let

\[
\beta=\sum_{i<j}v_{ij}x_ix_j.
\]

Contract the \(H\)-coefficients with their inner product.  The normalized
degree-two intersection form is

\[
\mathcal Q_2(v)
=
\frac{
\deg\bigl(\langle\beta,\beta\rangle\omega^{m-4}\bigr)
}{
(m-4)!\prod_i a_i
}.
\]

Only disjoint pairs survive \(x_i^2=0\), so

\[
\boxed{
\mathcal Q_2(v)
=
2
\sum_{\substack{\{i,j\}<\{k,\ell\}\\
                 \{i,j\}\cap\{k,\ell\}=\varnothing}}
\langle v_{ij},v_{k\ell}\rangle.
}
\tag{L-105431.3}
\]

A direct expansion gives the physical trace identity

\[
\boxed{
\mathcal Q_2(v)
=
\|S\|^2
+
\sum_{i<j}\|v_{ij}\|^2
-
\sum_i\|r_i\|^2.
}
\tag{L-105431.4}
\]

Equivalently,

\[
\boxed{
\|S\|^2
=
\mathcal Q_2(v)
-
\sum_{i<j}\|v_{ij}\|^2
+
\sum_i\|r_i\|^2.
}
\tag{L-105431.5}
\]

This is the exact decomposition of the one-dimensional physical pair
restriction.

## 3. Lefschetz signatures

In the orthogonal coordinates above,

\[
\boxed{
\mathcal Q_2(v)
=
\frac{(m-2)(m-3)}{m(m-1)}\|S\|^2
-
(m-2)(m-3)\sum_i\|u_i\|^2
+
\sum_{i<j}\|w_{ij}\|^2.
}
\tag{L-105431.6}
\]

Thus degree two has the expected F1 Hodge signature:

```text
Lefschetz degree direction       positive;
L times primitive degree one     negative;
primitive degree-two cycle       positive.
```

The normalized primitive degree-two gap is again exactly one.

## 4. Two-key physical restriction

Let all norms and inner products be taken over one logarithmic block and the
homotopy-recombined source.  The pair diagonal is already subpower on the
frozen PR #719 inputs.  From (L-105431.5),

\[
\|S\|^2
\le
\bigl(\mathcal Q_2(v)\bigr)_+
+
\sum_i\|r_i\|^2.
\tag{L-105431.7}
\]

Therefore the conjunction

```text
F1STAR105431:
  shared-owner star energy sum_i ||r_i||^2 is exp(o(T));

F1CYCLE105431:
  positive part of the four-distinct-label intersection Q_2 is exp(o(T))
```

implies the homotopy-coherent physical trace estimate.

Neither condition is silently identified with the other.  `F1STAR` contains
all correlations between owner pairs sharing a prime label; `F1CYCLE` contains
only four-distinct-label pair interactions.
