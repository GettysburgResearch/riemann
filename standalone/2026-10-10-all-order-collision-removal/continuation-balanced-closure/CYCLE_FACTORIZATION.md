# Primitive-cycle factorization of the actual coloured Euler source

**Status:** a self-contained adaptation of a classical formal identity and a proposed analytic application to the present source. This does not prove the balanced moment estimate. Classical necklace/Witt identities are not claimed as new.

The purpose is to inspect the remaining arithmetic source rather than replacing it by arbitrary coefficients. The factorization identifies all finite-degree corrections, the exact character powers, and the obstruction that persists after completion.

## 1. A classical identity, with its proof

For a nonzero vector a=(a_1,...,a_k) of nonnegative integers, let m=sum a_i and g=gcd(a_1,...,a_k), with zero entries ignored in the gcd. Set

\[
 \ell_k(\mathbf a)=\frac1m\sum_{d\mid g}\mu(d)
       \frac{(m/d)!}{\prod_i(a_i/d)!}.
\tag{1.1}
\]

These are nonnegative integers: the numerator counts primitive words of content a, and rotation partitions those words into orbits of exactly m elements. Indeed every word is a unique repetition of a primitive word; inversion over repetition divisors proves the numerator formula. This also gives ell_k(e_i)=1 and ell_k(m e_i)=0 for m>1.

The formal identity is

\[
 1-\sum_i z_i=\prod_{\mathbf a\ne0}
        (1-\mathbf z^{\mathbf a})^{\ell_k(\mathbf a)}.
\tag{1.2}
\]

For a direct verification, the coefficient of z^b in minus the logarithm of the right side is sum_(d|gcd b) ell_k(b/d)/d. Since |b|=d|b/d|, the primitive-word decomposition makes this multinomial(|b|;b)/|b|. That is the coefficient in -log(1-sum z_i). The constant terms are one, so (1.2) follows. Formal operations are legitimate degree by degree.

Consequently the predecessor's positive kernel has the factorization

\[
 R_k(\mathbf z)=\prod_{|\mathbf a|\ge2}
              (1-\mathbf z^{\mathbf a})^{-\ell_k(\mathbf a)}.
\tag{1.3}
\]

The pair factors are exactly (1-z_i z_j)^(-1), one for each i<j. At degree three there is one factor for each 2e_i+e_j, i!=j, and two for each e_i+e_j+e_l with distinct indices. The full factorization, not only its scalar specialization, keeps the factor-length geometry.

Literature comparison: Blessenohl and Laue, *Algebraic combinatorics related to the free Lie algebra*, Section 1, printed page 3, gives the multivariate Witt dimension/necklace formula. Its formula and interpretation were checked in both parsed text and the page image. The proof above is included to avoid importing an unstated combinatorial theorem. Source: https://radon.mat.univie.ac.at/~slc/s/s29laue.pdf .

## 2. Apply it without discarding row zeros

Fix a row u and write psi_u(n)=nu(n) chi_n(u), with its original zero extension and a finite fixed exclusion S. Define, initially for every Re(s_i)>1,

\[
 Z_{k,u}^S(\mathbf s)=
 \sum_{\substack{n_i\ \mathrm{squarefree},\ (n_i,n_j)=1\ (i\ne j)\\
                 (\prod_i n_i,S)=1}}
 \mu(\prod_i n_i)\psi_u(\prod_i n_i)\prod_i(Nn_i)^{-s_i}
 =\prod_{p\notin S}\left(1-\psi_u(p)\sum_i(Np)^{-s_i}\right).
\tag{2.1}
\]

This is the *joint Dirichlet series* of the same coefficient system used in the balanced polynomial. It is not itself a bound for the smoothed balanced polynomial.

For an integer d>=1 use the literal presentation

\[
 L^S(w,\psi_u^{[d]})=
 \prod_{p\notin S}(1-\psi_u(p)^d(Np)^{-w})^{-1}.
\tag{2.2}
\]

The bracket emphasizes that 0^d=0, including d divisible by six. This agrees with the appropriate finite-order Hecke L-function with its actual omitted Euler factors; those factors must not be restored at row primes.

### Theorem 2.1. Finite-degree analytic factorization

Fix J>=2 and include every prime of norm at most (2k)^(J+1) in S. Then

\[
 \boxed{
 Z_{k,u}^S(\mathbf s)=E_{k,J,u}^S(\mathbf s)
 \prod_{1\le|\mathbf a|\le J}
 L^S(\mathbf a\cdot\mathbf s,\psi_u^{[|\mathbf a|]})^{-\ell_k(\mathbf a)}.
 }
\tag{2.3}
\]

The remainder E and its reciprocal have absolutely convergent multivariate ideal series on min_i Re(s_i)>1/(J+1), locally uniformly there and uniformly in all row phases of modulus at most one. In particular E is holomorphic and nonvanishing there. Formula (2.3) gives a meromorphic continuation on that domain, not a zero-free assertion.

**Proof.** At one prime set z_i=psi_u(p)(Np)^(-s_i), and define

\[
 E_{k,J,p}(\mathbf z)=
 (1-\sum_i z_i)\prod_{1\le|\mathbf a|\le J}
              (1-\mathbf z^{\mathbf a})^{-\ell_k(\mathbf a)}.
\tag{2.4}
\]

Equation (1.2) shows that its Taylor expansion is 1 plus terms of total degree at least J+1. Its inverse has the same property. Both are holomorphic and nonzero when sum_i |z_i|<1. The fixed cutoff puts every local argument inside sum_i|z_i|<1/2 throughout the claimed domain. On each compact subdomain, absolute Taylor estimates therefore give local defects bounded by C_(k,J) (Np)^(-(J+1) sigma), with sigma the minimum real part on that subdomain. Summing over prime ideals converges because (J+1)sigma>1, using the elementary ideal count in BALANCED_CLOSURE.md. Multiplying the absolute local series proves the stated absolute convergence, for E and its reciprocal. Substitution and multiplication of (2.4) prove (2.3) in the initial absolute region, then throughout the indicated domain by meromorphic continuation. At a prime dividing the row all z_i=0, so every factor is exactly one. QED.

## 3. Which character sectors appear?

At J=2 the exact formula is

\[
 Z_{k,u}^S(\mathbf s)=
 \frac{E_{k,2,u}^S(\mathbf s)}
 {\prod_i L^S(s_i,\psi_u)
  \prod_{i<j}L^S(s_i+s_j,\psi_u^{[2]})},
 \qquad \min_i\Re(s_i)>1/3.
\tag{3.1}
\]

The pair correction carries the squared sextic row character, hence a cubic row twist. At degree three the row character is quadratic. Degree six has no nontrivial sixth-root phase at good primes, but it still has the original row-prime zero mask and the fixed factor nu^6. The absolute-convergence claim for the remainder is uniform in these phases; it is not a uniform nonvanishing or growth theorem for the displayed L-functions.

On min_i Re(s_i)>1/2, every pair argument in (3.1) has real part greater than one. Its Euler product is nonzero there. Thus the hard reciprocal factors L(s_i,psi_u)^(-1) have not been cancelled by the completion.

More explicitly, suppose L^S(s,psi_u) has a zero rho with Re(rho)>1/2 and order m. At the point (rho,...,rho), the pair factors and E in (3.1) are finite and nonzero. The coefficient of the leading product singularity is

\[
 \frac{E_{k,2,u}^S(\rho,\ldots,\rho)}
 {[L^{S,(m)}(\rho,\psi_u)/m!]^k
  L^S(2\rho,\psi_u^{[2]})^{\binom{k}{2}}}\ne0.
\tag{3.2}
\]

On the restriction s_1=...=s_k=s, the singularity has order km. That restriction sums by the *product norm*, and is not the same operation as imposing k separate smooth factor windows at a common scale. No bound for the latter is deduced from (3.2).

This calculation rules out a shortcut in this attempted attack: factoring or continuing the joint Euler correction cannot by itself eliminate the target zeros. A useful analytic step still needs cancellation/growth control for the literal smoothed, balanced source. Neither the primitive-cycle identity nor the extension of E to deeper half-planes supplies that estimate.
