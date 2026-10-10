# The interaction graph of the balanced Gauss coefficients

**Status:** proved finite arithmetic and linear algebra; a structural guide to a possible completion, not a higher-moment estimate.

**Scope:** the pairwise coprime squarefree face of the exact cubic Gauss coefficient produced by the sextic Poisson calculation. All factor axes and their residue phases are retained. The graph calculation does not assert existence or analytic continuation of a multiple Dirichlet series for the higher-rank graphs.

**Dependencies:** the twisted multiplicativity identity in the October 5 OpenAI manuscript, at source commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`, `paper2.tex`, equation `eq:crt-a`. It is also written explicitly in the parent packet's `FOURTH_MOMENT_ATTACK.md`, Lemma 4.1. The classical two-variable comparison is Brubaker–Bump–Chinta–Friedberg–Hoffstein, *Weyl Group Multiple Dirichlet Series I*, equations (5), (13), and (20), [author-hosted paper](https://chinta.ccny.cuny.edu/publ/wmd1.pdf). The precise normalization of that comparison is treated separately in `A2_COMPLETION.md`.

**What was run:** exact integer matrix calculations and finite-field residue calculations in `checks/check_local_structure.py`. These check examples and algebraic identities; the proofs below establish their stated generality.

**Remaining gap:** a uniform analytic mean-square bound for an appropriate completed, moving-sextic-twist family, together with recovery of its squarefree balanced face. A graph identification supplies neither bound.

## 1. Every pair of axes interacts

Use the original primary generators over \(K=\mathbb Q(\sqrt{-3})\). Write

\[
\chi_n(m)=(m/n)_6,\qquad (m/n)_3=\chi_n(m)^2.
\]

Let \(a_\xi(n)\) be the source's normalized cubic Gauss coefficient, including its fixed ray character. On coprime squarefree ideals outside the fixed bad-prime set it satisfies

\[
a_\xi(mn)=a_\xi(m)a_\xi(n)\chi_n(m)^4.
\tag{1.1}
\]

This formula is used only where the symbol is a unit. On that domain,

\[
\chi_n(m)^4=(m/n)_3^{-1}.
\tag{1.2}
\]

### Proposition 1.1. Exact all-pairs formula

For pairwise coprime squarefree \(n_1,\ldots,n_k\) outside the fixed bad primes,

\[
\boxed{
a_\xi(n_1\cdots n_k)
=\prod_{i=1}^k a_\xi(n_i)
  \prod_{1\le i<j\le k}(n_i/n_j)_3^{-1}.}
\tag{1.3}
\]

**Proof.** The assertion for one factor is immediate. Apply (1.1) to \((n_1\cdots n_{k-1})n_k\), insert the formula for the first \(k-1\) factors, and use multiplicativity of the residue symbol in its numerator. The new factor is the product of the \(k-1\) edges joining the last axis to the preceding axes. This proves (1.3) by induction. \(\square\)

Thus the interaction graph of this displayed coefficient is the complete graph on the factor axes. For two axes this is the edge underlying the classical \(A_2\) coefficient. With three or more axes, replacing it by the chain \(A_k\) would delete genuine residue factors.

This is an identity on the coprime squarefree face. It makes no assertion about the coefficients when primes occur on more than one axis or to higher powers; those are exactly the coefficients a completion must supply.

## 2. Independent axis factors cannot delete an interaction

The extra edge cannot be absorbed into ordinary separate weights on its two axes.

### Proposition 2.1. A phase obstruction

There do not exist nonvanishing functions \(f\) and \(g\) on all squarefree primary ideals outside \(6\) such that

\[
(a/b)_3^{-1}=f(a)g(b)
\tag{2.1}
\]

for every coprime pair \((a,b)\).

**Proof.** Set either axis equal to the unit ideal. The residue symbol is then one, so (2.1) forces both functions to be constant, with product one. This would make every symbol in (2.1) one. The following exact pair contradicts that conclusion.

Take primary generators

\[
\pi_7=-2-3\omega,\qquad \pi_{13}=1-3\omega,
\qquad N\pi_7=7,\quad N\pi_{13}=13,
\]

where \(\omega^2+\omega+1=0\). In the residue field modulo \(\pi_{13}\), \(\omega=9\pmod {13}\). Hence \(\pi_7=10\pmod {13}\), and

\[
(\pi_7/\pi_{13})_3
=10^{(13-1)/3}=3=\omega^2\pmod {13}.
\]

Consequently \((\pi_7/\pi_{13})_3^{-1}=\omega\ne1\). \(\square\)

Separate Hecke twists or separate Mellin weights are instances of separate axis factors. They therefore cannot erase this interaction on the full coefficient class. This statement does not rule out a coupled change of variables, an enlarged family, or a different completion.

## 3. The associated all-pairs reflection matrix changes type at three axes

The usual simply-laced matrix associated with the complete graph is

\[
C_k=(c_{ij}),\qquad c_{ii}=2,\quad c_{ij}=-1\ (i\ne j),
\qquad C_k=3I_k-\mathbf1\mathbf1^{\mathsf T}.
\tag{3.1}
\]

This is a precise algebraic object suggested by the pair interaction. Its calculation does not assume that a global Dirichlet series realizing it has been constructed.

### Proposition 3.1. Signature and an infinite orbit

The vector \(\mathbf1\) has eigenvalue \(3-k\); the perpendicular subspace has eigenvalue \(3\). In particular:

| Number of factor axes | Matrix | Consequence for this proposed reflection system |
|---|---|---|
| 1 | \([2]\) | The one-axis system |
| 2 | \(\begin{pmatrix}2&-1\\-1&2\end{pmatrix}\) | Positive definite; the finite \(A_2\) system |
| 3 | Complete triangle, with null vector \((1,1,1)\) | Positive semidefinite; the affine \(\widetilde A_2\) matrix |
| At least 4 | One negative eigenvalue and \(k-1\) positive eigenvalues | Indefinite; the same finite-system argument cannot apply |

For an entirely explicit infinitude check, define the reflections on the root-coordinate space by

\[
s_i(x)=x-(C_kx)_i e_i.
\tag{3.2}
\]

They square to the identity and preserve the symmetric form with matrix \(C_k\): substituting \(y=x-(C_kx)_ie_i\) and using \((C_k)_{ii}=2\) gives \(y^{\mathsf T}C_ky=x^{\mathsf T}C_kx\). For \(k=3\), let \(P=s_1s_2s_3\). Direct multiplication gives

\[
P=\begin{pmatrix}2&1&-2\\2&0&-1\\1&1&-1\end{pmatrix},
\qquad
P^2=I+N,\quad
N=\begin{pmatrix}3&0&-3\\3&0&-3\\3&0&-3\end{pmatrix},
\quad N^2=0,\ N\ne0.
\tag{3.3}
\]

Therefore \(P^{2m}=I+mN\) are distinct for all nonnegative integers \(m\). For \(k>3\), the first three reflections leave the span of \(e_1,e_2,e_3\) invariant and restrict there to the same matrices. Their group is infinite as well. The eigenvalue statement follows directly from (3.1). \(\square\)

## 4. What this tells the moment attack

The fourth moment involves two factor axes after forming \(A_u(D)^2\), so its squarefree coprime Gauss coefficient has a concrete finite \(A_2\) candidate for completion. The sixth moment has three axes and includes the triangle interaction already visible in (1.3). Simply substituting a three-axis \(A_3\) chain would omit one residue phase. Higher orders have the same problem on every three-axis subconfiguration.

This gives a reason to work out the two-axis completion in full before claiming a uniform finite-rank extension. It is not an impossibility theorem for higher moments: a different representation, a larger finite-type system followed by a restriction, an infinite reflection system, or a direct arithmetic argument could still work. The exact useful deliverable is the coefficient identity and the warning against a specific incorrect generalization.

Neither this calculation nor the existence of the classical two-variable series proves the required estimate \(\sum_{Nu\le D^{1+\theta}}|A_u(D)|^4\ll HD^{2+\epsilon}\). Its moving twists, completion terms, and quantitative row mean must still be controlled.
