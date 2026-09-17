# 03. Euler generation, prime zeta, and analytic continuation

**Status:** classical identities and proposed deductions with domains stated. Unknown Golomb continuation and the disputed multi-residue theorem are not supplied by density asymptotics. Sources: [SOURCES](SOURCES.md).

## 1. A generator series is not its generated Euler product

For generators A in (1,infinity), define
\[
D_A(s)=\sum_{a\in A}a^{-s},\qquad
Z_A(s)=\prod_{a\in A}(1-a^{-s})^{-1}.
\]
In an absolute-convergence domain,
\[
\log Z_A(s)=\sum_{m\ge1}D_A(ms)/m.
\]
The Euler product enumerates multisets of generators, with numerical collisions counted according to their multiplicity. Ordinary primes give unique factorization and the ordinary integers. Beurling generalized-prime systems provide a broad setting, but do not automatically supply a functional equation or an RH-type critical line.

The sine-product observation that motivated the discussion is different: expanding \(\sin x/x=\prod_{n\ge1}(1-x^2/(n^2\pi^2))\) recovers \(\zeta(2)=\pi^2/6\). It is not an Euler-factor replacement rule.

## 2. All integers as generators

Exclude 1, whose factor would be undefined, and set
\[
Z_{\rm int}(s)=\prod_{n\ge2}(1-n^{-s})^{-1},\quad\Re s>1.
\]
Its coefficient a(m) counts unordered multiplicative partitions of m into factors >1. For instance a(6)=2 (6 and 2*3), whereas a(2)a(3)=1, so these coefficients are not multiplicative.

Exactly,
\[
\log Z_{\rm int}(s)=\sum_{k\ge1}\frac{\zeta(ks)-1}{k}.
\]
On compact subsets of \(\Re s>0\), only finitely many terms require continuation; the tail is exponentially normally convergent. The continued logarithm has simple poles at s=1/k, of residue 1/k^2. Exponentiation gives a zero-free holomorphic continuation away from essential singularities at these points. Their accumulation at zero prevents continuation through a full neighborhood of zero. This argument alone does not classify every point on the imaginary axis; do not promote it to a full natural-boundary theorem without an additional argument.

## 3. Golomb-generated integers

Let \(P_G(s)=\sum_{g\in G}g^{-s}\). Since G consists of ordinary primes,
\[
Z_G(s)=\prod_{g\in G}(1-g^{-s})^{-1}
=\sum_{n\in\mathcal M_G}n^{-s},
\]
where \(\mathcal M_G\) consists of integers all of whose prime divisors are in G. Every coefficient is 1.

Set
\[
E_G=\sum_{g\in G}[-\log(1-1/g)-1/g].
\]
The product asymptotic in Chapter 02 gives, as epsilon decreases to zero,
\[
P_G(1+\epsilon)=\log_2(1/\epsilon)-D_G+o(1),
\]
\[
Z_G(1+\epsilon)\sim C_G\log(1/\epsilon),
\quad
C_G=e^{E_G-D_G}
=\prod_{g\in G}\left(1-\frac1{(g-1)^2}\right)>0.
\]
The handoff's \(C_G\approx0.697327\) is an un-certified historical decimal.

The positive-coefficient Laplace Tauberian theorem, applied in coordinate log n, yields
\[
\sum_{n\le x,\ n\in\mathcal M_G}\frac1n\sim C_G\log_2x.
\]
Thus Golomb primes generate a family at the **ordinary-prime harmonic level**, not ordinary primes themselves. This is a genuine one-rung reversal under multiplicative generation.

The logarithmic divergence of Z_G excludes meromorphic extension to a full neighborhood of 1: it is neither removable nor a finite-order pole. A real-axis asymptotic does not determine its full multivalued continuation around 1 or a natural boundary elsewhere.

The complementary multiplicative indicator from Chapter 02 satisfies
\[
\sum_n a_G(n)n^{-s}=\zeta(s)/Z_G(s),\qquad
P_G(s)=\sum_{p\ge3}a_G(p-1)p^{-s}.
\]
These exact identities preserve the shifted-prime operation missing from a scalar density model.

## 4. Prime zeta and the exact RH connection

For \(P(s)=\sum_p p^{-s}\), initially \(\Re s>1\),
\[
\log\zeta(s)=\sum_{m\ge1}P(ms)/m,
\quad
P(s)=\sum_{m\ge1}\mu(m)\log\zeta(ms)/m.
\]
Let
\[
K(s)=\sum_p\sum_{m\ge2}p^{-ms}/m.
\]
It is holomorphic on \(\Re s>1/2\), and P=log zeta-K on the initial domain. Hence
\[
\boxed{\mathrm{RH}\iff P'(s)+(s-1)^{-1}
\text{ extends holomorphically to }\Re s>1/2.}
\]
The derivative is \(\zeta'/\zeta+(s-1)^{-1}-K'\). The pole at 1 cancels, but a zero in the half-plane leaves a pole with its multiplicity as residue. Conversely, no such zeros and functional-equation symmetry give RH.

Equivalently, the germ \(P(s)+\Log(s-1)\) continues as a single-valued holomorphic function there. This phrasing refers to the regularized germ; it does not define Log(s-1) globally before continuation. Also \(e^{P(s)}=\zeta(s)e^{-K(s)}\) continues meromorphically to that half-plane and has exactly zeta's zeros there.

In the broader Möbius continuation, candidate logarithmic singularities are at scaled zeros rho/m and poles 1/m. At a coincidence s_0, the coefficients must be added:
\[
c(s_0)=\sum_m\frac{\mu(m)}m\operatorname{ord}_{ms_0}\zeta.
\]
Zeros have positive order; the pole at 1 has order -1. A candidate need not survive cancellation. The classical prime-zeta natural-boundary result on the imaginary axis is attributed to the literature [F68]; this packet does not reproduce its full proof.

## 5. Prime-zeta's OWN zeros obstruct iterated logarithms

For a prime subset A with divergent reciprocal sum and smallest member p_0, let sigma_A>1 solve
\[
\sum_{p\in A,\ p>p_0}(p_0/p)^{\sigma_A}=1.
\]
The sum decreases continuously from infinity to zero, so this root is unique. Triangle domination excludes zeros for \(\Re s>\sigma_A\). Equality on the boundary would require simultaneous phase opposition to p_0 from every other prime, which independence of prime logarithms excludes. Thus there are no zeros at or to the right of this boundary.

The twisted series \(-p_0^{-s}+\sum_{p>p_0}p^{-s}\) has a simple real zero there. Independence of the prime logarithms, Kronecker approximation on finitely many primes, uniform tail control on compact subsets of \(\Re s>1\), and Rouché's theorem transfer that zero to vertical translates of D_A. Consequently D_A has infinitely many zeros with real parts approaching sigma_A from below. No RH assumption enters.

For ordinary P, the equation is \(P(\sigma_A)=2^{1-\sigma_A}\); the handoff's value 1.77954465354699 is preserved as an un-recomputed decimal. The same argument applies to P_G with p_0=3. Zeta zeros are singularities of P; these zeros of P are a different phenomenon.

Therefore a global identity \(\log P=P_G+A\) with A holomorphic throughout \(\Re s>1\) is impossible: it would make P an exponential, hence zero-free. The real-axis relation \(P_G(1+\epsilon)-\log P(1+\epsilon)\to-D_G\) is compatible with this obstruction. At large real s, log P(s) behaves like -s log 2 while P_G(s) tends to zero, a second normalization warning.

## 6. Continuing finite Golomb sieve stages

These are infinite prime sets with finitely many residue restrictions, not finite Euler products. For the first residue class,
\[
B(s)=\prod_{p\equiv2\ (3)}(1-p^{-s})^{-1},
\quad
B(s)^2=\frac{(1-3^{-s})\zeta(s)}{L(s,\chi_3)}B(2s).
\]
The square is meromorphic for \(\Re s>1/2\); B itself requires compatible square-root branches.

For a finite Golomb cutoff y let \(Q_y=\prod_{g\le y}g\). On the reduced residue classes modulo Q_y, expand the admissibility indicator in characters. Each local principal coefficient is (g-2)/(g-1); each nonprincipal coefficient is -1/(g-1). Their products give coefficients c_y(chi), whose principal member is
\(\delta_y=\prod_{g\le y}(1-1/(g-1))\sim1/\log_2y\).

After separately treating the finitely many primes dividing the modulus and any initial-prime exclusions,
\[
\log Z_y(s)=R_y(s)+\sum_{\chi\bmod Q_y}c_y(\chi)\log L(s,\chi),
\]
with R_y holomorphic for \(\Re s>1/2\). Since phi(Q_y)c_y(chi) is integral, \(Z_y^{\phi(Q_y)}\) is single-valued meromorphic there. Locally near 1, \(Z_y(s)=(s-1)^{-\delta_y}B_y(s)\), B_y analytic and nonzero.

As y grows, the modulus, number of characters and branch bookkeeping grow. Uniform convergence for \(\Re s>1\) does not prove continuation to the left. Bounds that depend uncontrolledly on Q_y cannot be passed to the infinite Golomb sieve.

A different route subtracts a smooth model \(A_0(x)=\int_{e^e}^xdu/(\log u\log_2u)\). With E_0=G-A_0,
\[
P_G(s)=J_0(s-1)+s\int_1^\infty E_0(x)x^{-s-1}dx,
\quad
J_0(z)=\int_e^\infty\frac{e^{-zt}}{t\log t}dt.
\]
A suitable \(E_0(x)=O(x^\theta)\) would continue the remainder to \(\Re s>\theta\), but deterministic secondary terms may first need to be included in A_0. The leading Golomb asymptotic does not supply this estimate.

If \(\mu_G\) is Möbius restricted to G-generated integers, its transform is 1/Z_G. An uncentered bound \(\sum_{n\le x}\mu_G(n)=O(x^\theta)\), theta<1, would make 1/Z_G analytic near 1, contradicting its \(1/(C_G\log(1/\epsilon))\) behavior. A corresponding cancellation problem needs a nonzero centered main term.

## 7. Digit-selected series have their own boundary

For the S_k of Chapter 02, put \(F_k(s)=\sum_{p\in S_k}p^{-s}\). A proposed detailed mechanism uses the prime block calculation with w=epsilon+it and L=log b:
\[
F_k(1+w)=A(w)\sum_{m\in S_{k-1}}\frac{e^{-wLm}}m+O_t(1),
\quad A(w)=\frac{e^{wL}-1}{wL}.
\]
For each fixed modulus q, PNT in arithmetic progressions on each retained block has summable harmonic errors, giving
\[
\sum_{m\le X,m\in S_j,m\equiv a(q)}1/m
=H_{S_j}(X)/\phi(q)+C_{j,q,a}+o(1)
\]
for reduced a and j>=1. At squarefree q>=2, (a,q)=1, Abel summation then gives, for k>=2,
\[
\frac{F_k(1+\epsilon+2\pi ia/(qL))}{\log_k(1/\epsilon)}
\longrightarrow
\frac{\mu(q)}{\phi(q)}\frac{e^{2\pi ia/q}-1}{2\pi ia/q}\ne0.
\]
Prime denominators provide a dense set of boundary frequencies. The divergence is unbounded but smaller than any pole, obstructing meromorphic continuation across those points and hence across any interval of Re s=1. The associated Euler product differs in its logarithm by a holomorphic prime-power correction on \(\Re s>1/2\). Its logarithm diverges more slowly than |log epsilon|, inconsistent with a nonzero integer-order zero or pole, and is unbounded, inconsistent with a regular nonzero value. This supplies the proposed natural-boundary proof for the products as well.

Example: \(F_2(1+\epsilon+i\pi/\log b)\sim-(2i/\pi)\log_2(1/\epsilon)\). These resonances depend on the base and are not zeta-zero locations. The argument is recorded for independent review, not claimed as an externally refereed new theorem.

## 8. Centered digit masks retain ordinary prime error

For a fixed set of digit lengths define h(x) as its indicator and
\[
R_h(s)=\sum_p h(p)p^{-s}-\int_2^\infty h(x)x^{-s}/\log x\,dx.
\]
Under RH, \(\pi(x)-\operatorname{li}(x)=O(\sqrt x\log x)\). Blockwise integration by parts makes the centered remainder normally convergent for \(\Re s>1/2\), even for an arbitrary fixed digit mask. The corresponding masked counting error is \(O_b(\sqrt x\log x)\), because the sum of geometric block errors is controlled by the final block.

For the complementary mask,
\[
R_h+R_{1-h}=P-J,\quad J(s)=\int_2^\infty x^{-s}/\log x\,dx.
\]
Its derivative is \(\zeta'/\zeta-K'+2^{1-s}/(s-1)\), cancelling the pole at 1 but not zero poles. Therefore RH is equivalent to simultaneous holomorphic continuation of BOTH centered components to \(\Re s>1/2\). A proof for one mask alone does not automatically control its complement.

## 9. Prime chains and martingales: useful structures, not automatic spectra

The graph q→p when q divides p-1 is acyclic. Finite directed adjacency matrices are strictly triangular and nilpotent; det(I-zT)=1. A nontrivial spectral determinant or Ihara-type closed-path interpretation requires additional structure. Pratt trees and prime-chain literature [FKL] are relevant, not a supplied RH operator.

A genuine finite-sieve probability model exists: independent uniform nonzero residues R_g, survival probability a_g=(g-2)/(g-1), and
\[
W_y=\prod_{g\le y}\frac{1_{R_g\ne1}}{a_g}.
\]
It is a mean-one martingale with \(\mathbb E W_y^2=\prod a_g^{-1}\sim\log_2y\). Differences are orthogonal. This is a theorem about the product residue probability space. Transferring it to actual primes or signed Möbius coefficients, including principal terms and growing moduli, is a different estimate. Nested deterministic indicators alone are not a martingale.
