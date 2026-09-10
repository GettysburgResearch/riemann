# 2. Primary Target A — generalized-Schur zero-index theorem

## 2.1 Negative squares

For a Hermitian kernel \(K\) on a set \(\Omega\), write \(\nu_-(K)=\kappa\) if every finite Gram matrix

\[
[K(z_i,z_j)]_{i,j=1}^n
\]

has at most \(\kappa\) negative eigenvalues and some finite Gram matrix has exactly \(\kappa\). The value may be \(+\infty\).

Let \(f\) be real entire, \(\lambda>0\), and put

\[
A=f-i\lambda f',\qquad B=f+i\lambda f',\qquad
\Theta=A/B.
\]

Cancel common local factors and let \(\Omega\) be the upper half-plane with the genuine poles of the reduced \(\Theta\) removed.

Define

\[
K_\Theta(z,w)=
\frac{1-\Theta(z)\overline{\Theta(w)}}
     {-i(z-\overline w)}.
\]

## 2.2 The congruence identity

On the dense set where \(f(z)B(z)\ne0\), set

\[
m(z)=-\frac{f'(z)}{f(z)},\qquad
u(z)=\frac{f(z)}{B(z)}.
\]

A direct expansion gives

\[
\boxed{
K_\Theta(z,w)
=
2\lambda\,u(z)\overline{u(w)}
\frac{m(z)-\overline{m(w)}}{z-\overline w}.
}
\tag{A.1}
\]

Indeed,

\[
B(z)\overline{B(w)}-A(z)\overline{A(w)}
=
2i\lambda\bigl(f'(z)\overline{f(w)}
-f(z)\overline{f'(w)}\bigr).
\]

Multiplication of a Gram matrix by the nonsingular diagonal matrix
\(\operatorname{diag}u(z_j)\) preserves inertia. Points at zeros of \(f\)
are recovered by continuity. Hence

\[
\boxed{\nu_-(K_\Theta)=\nu_-(N_m)},\qquad
N_m(z,w)=\frac{m(z)-\overline{m(w)}}{z-\overline w}.
\tag{A.2}
\]

In particular the index is independent of \(\lambda>0\).

## 2.3 Polynomial theorem

### Theorem A1

Let \(f\) be a nonzero real polynomial. Let

* \(x_1,\dots,x_r\) be its distinct real zeros;
* \(a_1,\dots,a_q\) be its distinct upper-half-plane zeros.

Multiplicities may be arbitrary. Then

\[
\boxed{\nu_-(K_{\Theta_\lambda})=q.}
\tag{A.3}
\]

Thus the index equals the number of **distinct** upper-half-plane zeros.
It equals the algebraic zero count precisely when all upper-half-plane
zeros are simple.

### Proof

Write the multiplicities as \(\mu_j\) and \(\nu_j\). Since

\[
-\frac{f'}f
=
\sum_{j=1}^r\frac{\mu_j}{x_j-z}
+
\sum_{j=1}^q\nu_j
\left(\frac1{a_j-z}+\frac1{\overline{a_j}-z}\right),
\]

and \(\phi_\alpha(z)=(\alpha-z)^{-1}\),

\[
N_m(z,w)
=
\sum_{j=1}^r\mu_j
 \phi_{x_j}(z)\overline{\phi_{x_j}(w)}
\]
\[
\quad+
\sum_{j=1}^q\nu_j\left(
 \phi_{a_j}(z)\overline{\phi_{\overline{a_j}}(w)}
+\phi_{\overline{a_j}}(z)\overline{\phi_{a_j}(w)}
\right).
\tag{A.4}
\]

This is a finite feature representation with coefficient form

\[
J=
\operatorname{diag}(\mu_1,\dots,\mu_r)
\oplus
\bigoplus_{j=1}^q
\nu_j
\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\tag{A.5}
\]

Every \(2\times2\) block has one positive and one negative eigenvalue.
The Cauchy functions associated with distinct poles are linearly
independent. Consequently one can choose as many sample points as there
are feature functions so that their evaluation matrix is invertible.
The resulting Gram matrix is congruent to \(J\). Therefore its negative
inertia is exactly \(q\). Equation (A.2) transfers the result to
\(K_\Theta\). ∎

## 2.4 Finite-order entire theorem

Let \(E_1(\zeta)=(1-\zeta)e^\zeta\).

### Theorem A2

Suppose \(f\) is a nonzero real entire function with a genus-at-most-one
canonical product

\[
f(z)=e^{az+b}z^{m_0}
\prod_{\rho\ne0}E_1(z/\rho)^{m_\rho},
\qquad a,b\in\mathbb R,
\tag{A.6}
\]

where the zero multiset is conjugation-invariant and

\[
\sum_{\rho\ne0}\frac{m_\rho}{|\rho|^2}<\infty.
\tag{A.7}
\]

Let \(q\) be the number of distinct upper-half-plane zeros, possibly
infinite. Then

\[
\boxed{\nu_-(K_{\Theta_\lambda})=q.}
\tag{A.8}
\]

This class includes real entire functions of order at most one with
their standard genus-one product, in particular the centered Xi
function.

### Proof

The constant terms in the logarithmic derivative disappear from
\(N_m\). The kernel has the locally uniformly convergent expansion

\[
N_m=
m_0\,\phi_0\phi_0^*
+\sum_{x\in Z(f)\cap\mathbb R}
m_x\,\phi_x\phi_x^*
\]
\[
\quad+
\sum_{a\in Z(f)\cap\mathbb C_+}
m_a\bigl(\phi_a\phi_{\overline a}^*
+\phi_{\overline a}\phi_a^*\bigr).
\tag{A.9}
\]

Convergence on compact subsets follows from (A.7). If \(q<\infty\),
(A.9) is a pullback of a Hermitian coefficient form with exactly \(q\)
negative directions, so \(\nu_-(N_m)\le q\).

For the reverse inequality, use the following pole lemma.

### Pole lemma

If a meromorphic \(m\) has \(q\) distinct simple poles
\(a_1,\dots,a_q\in\mathbb C_+\) with residues \(-\mu_j<0\), then
\(N_m\) has at least \(q\) negative squares.

Choose disjoint small circles \(C_j\) around the poles and define

\[
L_j h=\frac1{2\pi i}\int_{C_j}h(z)\,dz.
\]

Choose finite point-evaluation combinations \(P_j\) satisfying

\[
P_j\!\left[(\overline{a_k}-z)^{-1}\right]=\delta_{jk}.
\]

This is possible because those \(q\) analytic Cauchy functions are
linearly independent. Residue calculation gives

\[
L_j\overline{P_k}N_m=-\mu_j\delta_{jk},\qquad
P_j\overline{L_k}N_m=-\mu_j\delta_{jk},\qquad
L_j\overline{L_k}N_m=0.
\]

For \(T_j=tL_j+P_j\), the induced \(q\times q\) matrix is

\[
-2t\,\operatorname{diag}(\mu_1,\dots,\mu_q)+O(1),
\]

hence negative definite for large \(t\). The contour functionals are
limits of finite Riemann sums of point evaluations, so a genuine finite
Gram matrix has at least \(q\) negative eigenvalues.

Each zero of \(f\), regardless of its multiplicity, produces a simple
pole of \(-f'/f\) with residue equal to minus the multiplicity. The pole
lemma gives \(\nu_-(N_m)\ge q\). If \(q=\infty\), applying the lemma to
arbitrarily large finite subsets gives infinite index. Equation (A.2)
finishes the proof. ∎

## 2.5 Denominator zeros, cancellation, and boundary zeros

If \(b\) is a zero of \(f\) of multiplicity \(m\), write

\[
f(z)=(z-b)^m a(z),\qquad a(b)\ne0.
\]

Both \(A\) and \(B\) have the common factor \((z-b)^{m-1}\). After
cancellation,

\[
\Theta(b)=-1,\qquad
\Theta'(b)=-\frac{2i}{\lambda m}.
\tag{A.10}
\]

There are no other common zeros: \(A=B=0\) implies \(f=f'=0\).

A genuine zero of the reduced denominator \(B\) is a pole of
\(\Theta\). Such poles are excluded from the sampling domain but do
not add a separate term to (A.8); their behavior is already encoded by
the generalized-Schur index. Their locations may depend on \(\lambda\),
whereas the index does not.

The reduced denominator has no real zero. On the real axis
\(B(x)=f(x)+i\lambda f'(x)\), so \(B(x)=0\) forces \(f(x)=f'(x)=0\),
which is precisely a canceled multiple zero.

A distinct real zero of \(f\) contributes one positive rank-one term
to \(N_m\). Its multiplicity changes the coefficient of that term but
not its rank. Boundary zeros therefore contribute no negative square.

## 2.6 Multiplicity no-go theorem

No theorem equating \(\nu_-(K_\Theta)\) to the algebraic upper-half-plane
zero count can hold for this kernel without a simplicity hypothesis.

For

\[
f_m(z)=(z^2+1)^m
\]

the upper-half-plane zero \(i\) has multiplicity \(m\), but Theorems A1
and A2 give

\[
\nu_-(K_{\Theta_\lambda})=1
\quad\text{for every }m\ge1.
\]

After cancellation,

\[
\Theta_\lambda(z)
=
\frac{z^2+1-2i\lambda m z}
     {z^2+1+2i\lambda m z},
\]

whose degree is independent of \(m\). The lost \(m-1\) copies are
exactly the common-factor cancellation. The correct universal statement
is therefore

\[
\nu_-(K_\Theta)
=
N_+^{\mathrm{distinct}}(f)
\le
N_+^{\mathrm{multiplicity}}(f),
\tag{A.11}
\]

with equality on the right if and only if all upper-half-plane zeros
are simple.

## 2.7 Xi consequence

For centered Xi,

\[
\boxed{
\nu_-(K_{\Theta_\lambda})
=
\#\{z\in\mathbb C_+:\Xi(z)=0\text{, counted distinctly}\}.
}
\tag{A.12}
\]

Thus:

* RH is equivalent to index \(0\);
* finitely many distinct off-axis Xi zeros give the same finite index;
* infinitely many distinct off-axis Xi zeros give infinite index;
* the count is independent of \(\lambda>0\);
* a generic off-critical zeta quartet contributes two upper-half-plane
  zeros in the centered \(z\)-variable and hence two negative squares.

No assertion is made that any such off-axis Xi zero exists.

## 2.8 Finite and truncated certificates

For any finite nodes \(z_1,\dots,z_n\) avoiding genuine denominator
poles,

\[
n_-\!\left([K_\Theta(z_i,z_j)]\right)
\le N_+^{\mathrm{distinct}}(f).
\tag{A.13}
\]

Therefore a rigorously certified negative eigenvalue for Xi would be an
unconditional RH counterexample. A positive finite Pick matrix gives no
upper bound and no RH evidence.

The Bezoutian form

\[
K_\Theta(z,w)=
\frac{2\lambda\,
\bigl(f(z)\overline{f'(w)}-f'(z)\overline{f(w)}\bigr)}
{(z-\overline w)
 (f(z)+i\lambda f'(z))
 \overline{(f(w)+i\lambda f'(w))}}
\tag{A.14}
\]

is preferable for interval evaluation because it keeps cancellation
explicit.

If a rectangle contains \(q\) certified, disjoint upper-half-plane
zero discs, the pole-lemma construction gives \(q\) negative directions
using points arbitrarily close to those discs. The converse localization
is false without an exterior factorization: zeros outside a rectangle
can influence Pick matrices sampled inside it. A rectangle-level equality
therefore requires either an argument-principle zero census plus simplicity
or a proved positive/exterior remainder decomposition.

The committed #765 transport data concern fifth-companion zeros, not
off-axis Xi zeros, and do not presently instantiate such a certificate.

---
