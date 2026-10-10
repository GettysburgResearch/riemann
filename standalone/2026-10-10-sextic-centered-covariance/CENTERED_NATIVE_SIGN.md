# A genuine finite-order sign obstruction to a positive centered A2 bootstrap

**Status:** proved finite counterexample to positivity of the correctly product-diagonal-centered A2 covariance. Both signs occur with the exact normalized cubic Gauss coefficients, the trivial finite-order ray character, all six unit rows, and a fixed nonnegative smooth factor weight. The full arithmetic completion equals its coprime squarefree face in this example. This is not a counterexample to a conjectural asymptotic centered-covariance upper bound and gives no new zero-free exponent.

**Scope:** the Eisenstein field, the literal A2 families P and Q in PR #914. No arbitrary coefficient sequence, nonunitary Euler datum, moving test function in an asymptotic limit, omitted unit rows, or replacement of the correct product diagonal is used.

**Exact dependencies:** PR #914 head 0cc0428fedbbfc340044c7451b3d392c1da9a103, standalone/2026-10-10-sextic-moment-conductor-core/A2_COMPLETION.md, Sections 1–4 and 7; the original Gauss normalization at OpenAI/math commit adc7f1241b42e322a6451854ab7e4b4c146bf78a, preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex, definitions of primary generators, alpha, gamma_2 and a_xi, and eq:crt-a. The local finite-field proof below directly computes the required Gauss sums; it does not use a new analytic theorem.

**Smallest remaining analytic gap:** the strict off-diagonal after the exact signed first-Poisson diagonal cancellation remains a signed quantity. A power saving for it needs an estimate that preserves its signs, coupled kernel, masks, and cross-correction terms. Positivity of its product-diagonal-centered completed pieces is unavailable even for genuine source coefficients.

## 1. Exact coefficient convention

Let K=Q(omega), where omega^2+omega+1=0, and let O=Z[omega]. Outside the primes above 2 and 3, an ideal is represented by its unique primary generator congruent to 1 modulo 3. Write

\[
\alpha(n)=n/|n|,\qquad
\chi_n(x)=(x/n)_6,\qquad
e(z)=\exp(4\pi i\,\operatorname{Im}(z)/\sqrt3).
\]

Every character is extended by zero at nonunits. Put

\[
\gamma_2(n)=\frac1{\sqrt{Nn}}\sum_{x\bmod n}\chi_n(x)^2e(x/n),
\qquad
a_1(n)=\overline{\alpha(n)}\gamma_2(n).
\tag{1.1}
\]

Thus the finite-order ray character xi is exactly the trivial character. The source twisted multiplicativity is

\[
a_1(ab)=a_1(a)a_1(b)\chi_b(a)^4
\quad\text{if }ab\text{ is squarefree}.
\tag{1.2}
\]

For squarefree n, this is the genuine cubic Gauss coefficient of the source. Let P and Q have exactly the meaning of A2_COMPLETION.md, equations (4.1) and (4.2). In particular, the normalized completed coefficient has zero local value at the exponent pair (1,1). At disjoint squarefree n_1,n_2 it equals a_1(n_1n_2).

If several ordered factor pairs have the same product ideal n, their coefficients must be combined before forming the product diagonal. For any finite row polynomial

\[
P(k)=\sum_n z_n\chi_n(k),
\]

its product-diagonal-centered covariance over a row set U is

\[
\mathcal C_U(P)=
\sum_{k\in U}\left(
\left|\sum_n z_n\chi_n(k)\right|^2
-\sum_n|z_n\chi_n(k)|^2
\right).
\tag{1.3}
\]

The second term subtracts equality of product ideals n, not equality of ordered factor pairs. Both conventions agree only when the factor-to-product map is injective.

## 2. An exact evaluation on inert rational primes

### Lemma 2.1

Let p>3 be a rational prime with p congruent to 2 modulo 3, and let p_K=(p) be the inert prime ideal. Then

\[
\gamma_2(p_K)=1,\qquad a_1(p_K)=-1.
\tag{2.1}
\]

For distinct such primes p and q,

\[
\chi_{q_K}(p_K)^4=1.
\tag{2.2}
\]

Consequently, on every squarefree product of these inert prime ideals,

\[
a_1(n)=\mu_K(n).
\tag{2.3}
\]

### Proof

The primary generator of p_K is -p, so alpha(p_K)=-1 and Np_K=p^2. The residue field is F_{p^2}=F_p[omega]. Its cubic character kappa=chi_{p_K}^2 is nontrivial and is trivial on F_p^*: the exponent (p^2-1)/3 is divisible by p-1 because 3 divides p+1.

Write a residue as a+b omega, with a,b in F_p. The additive character in (1.1), using the primary denominator -p, is

\[
e((a+b\omega)/(-p))=\exp(-2\pi i b/p).
\tag{2.4}
\]

For b=0, the cubic-character sum over a is p-1. For each nonzero b, its sum over a is the same value T, since

\[
\kappa(a+b\omega)=\kappa(b)\kappa(a/b+\omega)
=\kappa(a/b+\omega).
\]

The sum of a nontrivial multiplicative character over F_{p^2} is zero. Hence (p-1)+(p-1)T=0, so T=-1. It follows exactly that

\[
\begin{aligned}
\sum_{x\bmod p_K}\kappa(x)e(x/(-p))
&=(p-1)-\sum_{b=1}^{p-1}\exp(-2\pi i b/p)\\
&=p.
\end{aligned}
\tag{2.5}
\]

Division by sqrt(Np_K)=p gives gamma_2=1 and then a_1=-1. A primary generator of the other rational inert prime ideal is a nonzero element of F_q, so its cubic symbol modulo q_K equals one. Squaring that cubic symbol proves (2.2). Formula (1.2) now proves (2.3) inductively. This argument uses the exact source additive character and the exact primary generators. Square.

## 3. A fixed smooth three-column window

Consider the three ideals

\[
n_1=(53),\qquad n_2=(71),\qquad n_3=(55)=(5)(11).
\tag{3.1}
\]

The rational primes 5, 11, 53 and 71 are all inert in K. These three ideals are squarefree and pairwise coprime. Their norms are

\[
Nn_1=2809,\qquad Nn_2=5041,\qquad Nn_3=3025.
\tag{3.2}
\]

For each displayed integer norm there is exactly one ideal of that norm. Indeed, every prime ideal dividing an ideal of rational prime-power norm lies over that rational prime; here the rational primes are inert and their unique prime ideals have norms p^2. Unique ideal factorization gives the assertion for 55^2 as well.

Fix A=B=2600. Let rho be any fixed nonnegative smooth function supported in (-1/3,1/3), with rho(0)=1. For a fixed real t>0 define

\[
\begin{aligned}
W_t(x)={}&\rho(2600x-2809)
+\rho(2600x-5041)\\
&+t\rho(2600x-3025),\\
V_t(x,y)={}&W_t(x)W_t(y).
\end{aligned}
\tag{3.3}
\]

Thus W_t belongs to C_c^\infty((1,2)) and is nonnegative. Since ideal norms are integers, W_t(Nn/2600) is supported on exactly the three ideals in (3.1), where its values are respectively 1,1,t. This is one fixed smooth test at one specified finite scale; it is not a family of shrinking tests along an unbounded sequence of scales.

Take q_0=1, f=1, xi=1, and S consisting of the primes above 2 and 3. Lemma 2.1 gives

\[
a_1(n_1)=a_1(n_2)=-1,\qquad a_1(n_3)=1,
\]

and therefore

\[
a_1(n_1n_2)=1,\qquad
a_1(n_1n_3)=a_1(n_2n_3)=-1.
\tag{3.4}
\]

In P, the identical-factor pairs (n_i,n_i) are excluded because their products are not squarefree. Every distinct-factor pair is allowed. Combining the two ordered pairs with each product gives

\[
P(k)=2\chi_{n_1n_2}(k)
-2t\chi_{n_1n_3}(k)
-2t\chi_{n_2n_3}(k).
\tag{3.5}
\]

All three product ideals are distinct.

### Lemma 3.1. The completion makes no change in this window

For every row k, the literal full completion with the same data satisfies

\[
Q(k)=P(k).
\tag{3.6}
\]

### Proof

Each factor ideal selected by V_t is one of the three squarefree ideals n_i. If the selected pair is identical, each prime in that ideal has the local exponent pair (1,1), whose completed coefficient is zero. If the selected pair is distinct, its two ideals are coprime and squarefree, and the completed coefficient is the face coefficient a_1(n_i n_j). There are no other selected factor ideals and hence no correction terms supported at nonsquarefree factors. This proves (3.6) without applying a norm comparison or dropping any character zero. Square.

## 4. All unit rows and the two signs

Let U={k in O:0<Nk<=1}, the full row ball of radius one in norm. It consists of all six units. For a unit epsilon and an inert rational prime ideal (p), the sextic Euler criterion gives

\[
\chi_{(p)}(\varepsilon)
=\varepsilon^{(p^2-1)/6}.
\tag{4.1}
\]

For p=53 and 71 the exponent is divisible by 6, since p^2 is congruent to 1 modulo 36. For p=5 and 11 the exponents are respectively 4 and 20; their sum is 24, again divisible by 6. Therefore

\[
\chi_{n_i}(\varepsilon)=1
\quad(i=1,2,3,\ \varepsilon\in U).
\tag{4.2}
\]

There is no choice of one preferred unit row in this calculation: all six are included with their literal sextic symbols.

By (3.5), P(epsilon)=Q(epsilon)=2-4t at every such row. The genuine product diagonal at each row is

\[
|2|^2+|-2t|^2+|-2t|^2=4+8t^2.
\tag{4.3}
\]

Consequently the correctly centered covariance is

\[
\boxed{\mathcal C_U(P)=\mathcal C_U(Q)
=6\big((2-4t)^2-(4+8t^2)\big)
=48t(t-2).}
\tag{4.4}
\]

In particular:

| Fixed parameter t | Full positive energy | Product diagonal | Centered covariance |
| --- | ---: | ---: | ---: |
| 1/2 | 0 | 36 | -36 |
| 3 | 600 | 456 | 144 |

The energy normalization 1/(ABF), with F=1, divides every entry by 2600^2 and does not change either sign. The auxiliary annulus 1<=Nf<2 contains only the unit ideal, so it introduces no omitted auxiliary terms.

## 5. What is ruled out, and what remains open

The assertions that the correctly product-diagonal-centered covariance of every such P is nonnegative, or that completion restores that positivity for every Q, are false even with the exact finite-order source data and a nonnegative product test. The completion and its inverse are the identity on this example. Accordingly, the failure cannot be assigned to arbitrary coefficient phases, a nonunitary datum, a missing correction term, or an incomplete unit average.

Likewise, the full positive norm comparison between P and Q in PR #914 cannot by itself be read as a positivity statement after product-diagonal centering. That interpretation would already fail where Q=P exactly. Any positive argument that decomposes into these centered blocks requires additional cross-block identities or estimates; positivity of the individual blocks is not available.

This finite theorem does not disprove a bound of the form |C_U(Q)|<<D^epsilon H, because the test is fixed at one finite scale and the implicit constant may depend on that test. It does not prove that the entire signed first-Poisson expression is negative, nor that every one of its fixed ray components has a nonzero coefficient for an arbitrarily specified original nu. It establishes the precise narrower fact needed to reject a generic positivity-based centered-completion bootstrap.

The power-saving question remains the one identified by the signed diagonal identity: control the strict off-diagonal with the exact Möbius signs and coupled smooth kernel, or find an analytic transformation that does so. No new moment exponent or zero-free boundary is claimed here.
