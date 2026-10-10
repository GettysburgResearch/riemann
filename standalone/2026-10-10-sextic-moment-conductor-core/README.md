# Sextic moments: conductor sectors, A2 completion, and signed diagonal cancellation

**Research status: component proofs and an explicit remaining estimate. The full short-row fourth moment, the generalized moment hierarchy, and RH remain open.** This packet does not claim a new zero-free boundary. It is stacked on [PR #913](https://github.com/GettysburgResearch/riemann/pull/913), exact parent `6498d6cc2eded03159c7332b25fd224ad07f89c1`. It has not been promoted to the integrated record or formalized in Lean.

The main advance is an explicit arithmetic completion of the balanced two-factor cubic Gauss coefficient, with an exact inverse and controlled norm cost. Separately, the large diagonal in the signed initial Poisson formula is proved to cancel down to a uniformly bounded lattice discrepancy. These statements remove specific arithmetic and diagonal obstacles; the remaining signed off-diagonal cancellation has not been established.

## 1. The target and its consequence

Let $K=\mathbb Q(\sqrt{-3})$, let $S$ contain the fixed bad primes, and fix a finite-order Hecke character $\nu$. For a smooth compactly supported test $W$, retain the literal sextic residue symbols, including their zero values on nonunits:

$$
A_u(D)=\sum_{(n,S)=1}\mu_K(n)\nu(n)\chi_n(u)W(Nn/D),
\qquad \chi_n(u)=(u/n)_6.
$$

The desired estimate is

$$
\boxed{\displaystyle
\sum_{0<Nu\le H}|A_u(D)|^{2k}
\ll_{k,\nu,S,W,\theta,\epsilon}HD^{k+\epsilon},
\qquad H=D^{1+\theta}.
} \tag{T}
$$

Rows are nonzero Eisenstein **elements**, not squarefree ideals. The parameter $H$ is the arithmetic row norm, not a zero height. The requirement is an all-scale estimate for each fixed $k$, with arbitrarily small fixed positive $\theta$ and the test quantifiers needed by the Mellin argument.

The exact sixth-power extraction in the parent packet, sharpened here to tolerate $o(H^{1/6})$ missing rows, turns (T) into the limiting boundary

$$
\beta_k=\frac12+\frac5{12k}.
$$

| Moment that would have to be proved | Resulting limiting zero-free boundary |
| --- | --- |
| Fourth, $k=2$ | $17/24$ |
| Sixth, $k=3$ | $23/36$ |
| Eighth, $k=4$ | $29/48$ |
| Cofinal fixed orders $k\to\infty$ | $1/2$ for the associated twist family |

These are implications, not newly attained boundaries. In particular, the final row is strong enough to imply RH when the principal datum is included. The finite-order Hecke condition is essential to the intended theorem.

## 2. New component theorems

### A. A large, explicit part of every fixed moment is controlled

For a $2k$-tuple in the Hermitian expansion, let $g_1$ be the product of primes occurring exactly once. Let $g_2$ contain the nonprincipal primes occurring exactly twice; these are the same-side double occurrences with cubic residual characters. In dyadic ranges $L\le Ng_1<2L$, $C\le Ng_2<2C$, the absolute sum of the **completed nonprincipal tuple contributions** satisfies

$$
\mathcal Q^\Phi_{L,C}
\ll D^{k+\epsilon}\min\{H\sqrt L,\ L\sqrt C\}. \tag{2.1}
$$

This proves the target contribution whenever $(Ng_1)\sqrt{Ng_2}\le H$. Independently, every tuple with **no singleton prime** is controlled at $HD^{k+\epsilon}$, for every fixed $k$ and every $H\ge1$, even with sharp rows. The primitive-conductor range $1<Nf\le F$ has completed absolute contribution $O(D^{k+\epsilon}F)$.

The precise remainder is the signed sum over tuples with $g_1\ne1$ and $(Ng_1)\sqrt{Ng_2}>H$. Positivity majorizes only the full moment; it is never applied to an individual signed sector. See [CONDUCTOR_SECTORS.md](CONDUCTOR_SECTORS.md) for the statements and proofs.

### B. The balanced Gauss coefficient has an exact cubic A2 completion

Write $a_\xi(n)=\lambda(n)\gamma_2(n)$, where $\lambda(n)=\overline{\alpha(n)}\xi(n)$. Its squarefree multiplication law is

$$
a_\xi(ab)=a_\xi(a)a_\xi(b)(a/b)_3^{-1}.
$$

The rigorous local table and twisted multiplicativity of the classical cubic A2 coefficient system give the following normalized local polynomial:

$$
1+a_p(x+y)+b_p(xy^2+x^2y)+b_pa_px^2y^2,
\qquad b_p=\sqrt{Np}\,\lambda(p)^3.
$$

Every nonzero full coefficient has unique disjoint squarefree labels

$$
n_1=acd^2e^2,\qquad n_2=bc^2de^2,
$$

and the exact global formula

$$
\boxed{\mathfrak a_\xi(n_1,n_2)
=\sqrt{N(cde)}\,\lambda(cde)^3a_\xi(abe).} \tag{2.2}
$$

This yields a completion of the literal two-factor row polynomial and a signed inverse removing all correction primes. For $C=cde$, the child maps are

$$
A'=\frac A{Nc(Nd)^2(Ne)^2},\quad
B'=\frac B{(Nc)^2Nd(Ne)^2},\quad
F'=FNe,\quad q_0'=q_0C,
$$

so $A'B'F'=ABF/(NC)^3$. The normalized Hilbert norm cost is exactly $1/(NC)$ in **both** directions, hence at most a logarithmic cube after summation. The child auxiliary $ef$ may share primes with the child exclusion $q_0C$; the identities retain that overlap.

Using the parent's refined all-row sieve, the completion and the original squarefree face both satisfy

$$
\mathcal E\ll D^\epsilon\bigl[\mathcal H+
\mathcal H^{1/6}L+(\mathcal HL)^{2/3}\bigr],\qquad L=AB.
$$

The completion or projection tail $NC\ge R$ improves to

$$
\mathcal E_{\ge R}\ll D^\epsilon
\bigl[\mathcal H+\mathcal H^{1/6}LR^{-3}
 +(\mathcal HL)^{2/3}R^{-2}\bigr]. \tag{2.3}
$$

It reaches row-diagonal size once $R\ge\max(1,(L^2/\mathcal H)^{1/6})$. These are bounds actually deduced here. A sharper completed mean square and a conductor-uniform functional equation for the literal moving twists remain unproved. The source identification does not assert those extensions. See [A2_COMPLETION.md](A2_COMPLETION.md), Sections 1–5 and 7.

### C. The entire signed dual diagonal reduces to a bounded discrepancy

Carry any squarefree column coefficient $v(n)$, supported at norm $L$ with $\sum|v(n)|^2\ll LD^\epsilon$, and $L\ll D^B$ for a fixed $B$, through the exact initial Poisson formula. Let $\mathcal D[v]$ denote its entire dual product-column diagonal, retaining the outer $\mu_K(f)$ weights. Undoing the exact coprimality expansion proves

$$
\boxed{
\mathcal D[v]=\frac1L\sum_g|v(g)|^2
\left[\sum_{(u,g)=1}\Phi(Nu/H)
-H\widehat\Phi(0)\prod_{p\mid g}(1-(Np)^{-1})\right].
} \tag{2.4}
$$

The full-lattice smooth discrepancy is uniformly $O_\Phi(1)$ for every positive scale. Inclusion–exclusion therefore gives

$$
|\mathcal D[v]|\ll\frac1L\sum_g|v(g)|^2\tau_K(g)
\ll D^\epsilon,
\qquad H>0. \tag{2.5}
$$

This is uniform in the original row/column ratio, including the longest fourth-moment case $L=D^2$, $H=D^{1+\theta}$. It explains exactly why taking absolute values of the outer Möbius weights creates an artificial large positive diagonal.

The remaining sufficient estimate is for the **strict** dual off-diagonal $m_1\ne m_2$, with its original signs, masks, and coupled smooth transform, at size $HD^\epsilon$ in the same $1/L$ normalization. It is not proved. Positive norm transfer does not automatically transfer a centered sesquilinear estimate. See [A2_COMPLETION.md](A2_COMPLETION.md), Section 6.

### D. Extraction is stable under rough averaging, but finitely many moments do not bootstrap

Exact Euler removal makes the average over sufficiently rough sixth-power lifts an invertible perturbation of the identity on every positive Mellin-weighted $L^p$ line, for each fixed integer $p\ge1$. This remains true for an arbitrary measurable moving row range and every truncated scale interval. The inverse is bounded independently of that range.

Positive-density rough replicas also remove a prime-counting logarithm from the prior tail criterion: an exceptional set of $o(H^{1/6})$ rows can be omitted without changing the moment-to-zero-free implication.

Two explicit examples delimit the inference. One satisfies the full removal algebra; another uses the actual periodic sextic character kernel with bounded multiplicative coefficients and has the correct moments through any specified finite order but fails at every higher order. The latter deliberately violates the **finite-order Hecke** hypothesis and is not a counterexample to (T). See [REPLICA_AVERAGES.md](REPLICA_AVERAGES.md).

## 3. Why the A2 construction does not settle all orders

The exact $k$-factor Gauss interaction has an edge between every pair of factors. Its associated symmetric matrix is $3I-\mathbf1\mathbf1^T$, with eigenvalues (3-k) and (3). Thus this particular reflection system is finite A2 at two factors, affine at three, and indefinite at four or more. An explicit infinite reflection orbit and an actual nontrivial cubic residue symbol verify the obstruction to simply reusing a finite chain of A2 reflections. This does not rule out another representation or a different proof. See [INTERACTION_GRAPH.md](INTERACTION_GRAPH.md).

The productive remaining task is a native signed estimate on the singleton core, or on the strict Poisson off-diagonal, using the finite-order Hecke/Möbius coefficient structure. A proof based only on bounded coefficient norms, positive completion energies, or a finite ladder of moments would miss an essential hypothesis.

## 4. Validation and exact scope

There are two standard-library exact checkers. The conductor checker executes **222,127** explicit predicates and reconstructs five full small Eisenstein norm-ball moments independently of its tuple expansion. The A2 checker executes **167,052** predicates, gluing the six-point local table by the unreduced twisted law and checking completion/projection with genuine norm-7, norm-13, and norm-19 residue symbols. It includes nonunit zeros and auxiliary/exclusion overlaps. Both retain their acceptance checks under `python -O`.

These are finite algebra checks. The A2 local table is an input to its checker; its Gauss normalization is proved in the note. Neither program verifies a functional equation or an infinite moment estimate. Independent scoped reviews, source hashes, and exact commands are recorded in [VALIDATION.md](VALIDATION.md) and [PROVENANCE.json](PROVENANCE.json).

The classical A2 coefficient system is credited to Brubaker, Bump, Chinta, Friedberg, and Hoffstein, [*Weyl Group Multiple Dirichlet Series I*](https://chinta.ccny.cuny.edu/publ/wmd1.pdf), specifically its rigorous table (13) and twisted multiplicativity (20). No claim of external novelty is made for the classical system or for standard lattice, divisor, and Poisson facts. The contribution here is the exact adaptation, projection, scale bookkeeping, signed diagonal identification, and stated partial moment bounds for this research program.
