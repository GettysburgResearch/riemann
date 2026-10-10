# A sextic off-diagonal Gram bound from the bounded-coefficient inner sieve

Status: proved deduction, subject to the stated classical sieve and Poisson inputs, from a bounded-coefficient sextic inner extension, lattice Poisson summation, primitive Gauss evaluation, and smooth separation. No full fourth-moment estimate or new zero-free half-plane is claimed.

Scope: all primary squarefree character moduli in a fixed norm annulus, with the literal nonunit zero extensions. The inner sum is an unrestricted primary-element sum with a fixed smooth radial weight. The off-diagonal restriction is essential.

Exact source connection: OpenAI family 023, *An unconditional first moment for cubic Gauss sums*, September 25, 2026, `preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/build/sections/dual.tex`, lines 149–240, label `lem:character-gram`, at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`; blob `8dcddce96894146ca745b8227c922c34f5990dcf`. The fetched local file is `patterson-dual.tex`. That source is Apache-2.0. Its cubic Gram proof motivates the argument below; the character family and sieve input here are sextic, and the proof is supplied explicitly.

Analytic input: the squarefree sextic large sieve of Blomer–Goldmakher–Louvel, *L-functions with n-th order twists*, Theorem 1.3, also stated in `REFINED_ALL_ROW_SIEVE.md`, Section 1. The unrestricted-inner adapter below follows the cubic argument in the same Patterson source's `build/sections/background.tex`, lines 234–276, label `lem:cubic-extensions`, blob `3d31d5791ef3cf55c9608066997f9dc6c6bb861a` at the same commit, but uses the complete six-adic valuation decomposition. No use of the Patterson manuscript's exceptional-moment conclusion is made. The refined all-row sieve was an initial route to a weaker Gram bound; the bounded Fourier coefficients allow the sharper input proved here.

## 1. Statement and normalization

Work in O=Z[omega], omega=exp(2*pi*i/3), with lambda=sqrt(-3), N(z)=|z|^2 and e(t)=exp(2*pi*i*t). A primary element is congruent to 1 modulo 3, and represents its ideal uniquely away from 3. Let S be a fixed finite set of column-modulus primes containing those above 2 and 3. For primary squarefree p outside S, chi_p(n)=(n/p)_6, with its zero when (n,p) is nontrivial.

Fix W in C_c^infinity((0,infinity)), possibly complex-valued. Its support and smoothness norms are fixed. Let P,Z>=1, and fix p squarefree outside S with P<=Np<2P. For p' in the same squarefree primary annulus put

\[
T_{p,p'}(Z)=\sum_{n\equiv1\ (3)}
W(Nn/Z)\chi_p(n)\overline{\chi_{p'}(n)}.
\tag{1.1}
\]

The sum runs over all such n, without a squarefree restriction. Since the support excludes zero, its terms are finite and n=0 never contributes.

### Theorem 1.1

For every epsilon>0,

\[
\boxed{\sum_{\substack{P\le Np'<2P\\p'\ \mathrm{squarefree}\\(p',S)=1,\ p'\ne p}}
|T_{p,p'}(Z)|^2
\ll_{S,W,\epsilon}(PZ)^\epsilon
\left(PZ+P^2Z^{1/3}\right).}
\tag{1.2}
\]

The same upper bound holds on every subset of the p' range. An additional fixed inner exclusion (n,S_0)=1 is permitted, with a constant depending on S_0, by the finite inclusion–exclusion adapter in Section 5.

## 2. A bounded-coefficient unrestricted-inner sextic sieve

### Lemma 2.1

Let B,J>=1. For every coefficient sequence supported on nonzero lattice elements with Nh<=J and |c_h|<=1,

\[
\boxed{\sum_{\substack{b\ \mathrm{primary\ squarefree}\\Nb\le B,\ (b,S)=1}}
\left|\sum_{0<Nh\le J}c_h\chi_b(h)\right|^2
\ll_{S,\epsilon}(BJ)^\epsilon
J\left[B+J+(BJ)^{2/3}\right].}
\tag{2.1}
\]

There is no squarefree, unit, or fixed-bad-prime restriction on h. The same assertion holds with a subpower coefficient bound |c_h|<=C_delta(Nh)^delta for every delta>0, after reassigning epsilon; the constant then depends on the needed C_delta. A uniformly bounded additional norm cutoff or phase is allowed.

**Proof.** Choose generators multiplicatively, and factor each nonzero h uniquely as

\[
h=\varepsilon v^6a_1a_2^2a_3^3a_4^4a_5^5,
\tag{2.2}
\]

where epsilon is one of the six units, each a_j is squarefree, the a_j are pairwise coprime, and v is unrestricted. The ideal v may overlap any a_j. This is just division of every prime valuation by six with its remainder in {0,...,5}; the unit completes the unique representation of lattice elements.

Partition Nv and Na_j into dyadic blocks V and A_j, respectively. A nonempty block has

\[
V^6A_1A_2^2A_3^3A_4^4A_5^5\le J.
\tag{2.3}
\]

Freeze epsilon,v,a_2,...,a_5. The exact factor outside the a_1 character is

\[
\chi_b(\varepsilon)\mathbf1_{(b,v)=1}
\prod_{j=2}^5\chi_b(a_j)^j,
\]

whose modulus is at most one, including every zero caused by a repeated prime. Thus it is a contraction in the b norm, not a factor to be replaced by a primitive-character convention. The remaining coefficients are c_h as functions of a_1, multiplied by the exact squarefree, dyadic, norm, and mutual-coprimality indicators. They remain bounded by one. If a_1 has a factor at the fixed bad primes, freeze that squarefree factor first; there are only O_S(1) choices, and its character is another bounded row multiplier. The varying part of a_1 is then squarefree outside S.

The squarefree sextic large sieve, with reciprocity's finite fixed-ray splitting if required by its indexing convention, bounds the squared b norm for one frozen tuple by

\[
\ll(BJ)^\epsilon A_1
\left[B+A_1+(BA_1)^{2/3}\right].
\tag{2.4}
\]

Its coefficient energy is O(A_1), by ideal counting. There are O(V A_2A_3A_4A_5) frozen tuples. Minkowski in the b norm therefore bounds the whole block by

\[
\ll(BJ)^\epsilon (V A_2A_3A_4A_5)^2 A_1
\left[B+A_1+(BA_1)^{2/3}\right].
\tag{2.5}
\]

The exact elementary comparison is

\[
\frac{(V A_2A_3A_4A_5)^2 A_1}
 {V^6A_1A_2^2A_3^3A_4^4A_5^5}
=\frac1{V^4A_3A_4^2A_5^3}\le1.
\tag{2.6}
\]

Also A_1<=J. This proves (2.1) for a block; there are only O((1+log J)^6) blocks, whose squared Minkowski cost is absorbed by reassigning epsilon. The six units and the fixed bad-prime factors cause only fixed multiplicative constants. Divisor-bounded coefficients are handled by choosing their preliminary subpower exponent sufficiently small. \(\square\)

This is a bound for **bounded coefficients**, not an arbitrary-vector operator bound with J replaced by sum_h |c_h|^2. It makes essential use of the coefficient bound after each frozen factorization. The Gram proof below establishes exactly that hypothesis after smooth separation. In contrast, the arbitrary-vector dual of `REFINED_ALL_ROW_SIEVE.md`, Theorem 3.4, has bracket J+(BJ)^(2/3)+J^(1/6)B; that different norm-sensitive statement is not being strengthened here.

## 3. Common modulus, exact masks, and Poisson

Partition the p' sum by k=gcd(p,p'), and write

\[
p=ka,\qquad p'=kb,\qquad K=Nk,\qquad B=P/K.
\]

All k,a,b are squarefree; (a,b)=(a,k)=(b,k)=1. We have Na,Nb comparable to B. In particular B>=1/2, so all small-length uses of the sieve can harmlessly use max(1,B).

The product of characters in (1.1) is exactly

\[
\mathbf1_{(n,k)=1}\,\psi(n),\qquad
\psi=\chi_a\overline{\chi_b}.
\]

The character psi is primitive modulo c=ab. It is nonprincipal unless a=b=1: at each prime of a or b the local character is a nontrivial sextic character or its conjugate, and the two sets of primes are disjoint. The excluded case a=b=1 is exactly p'=p.

Remove the common-prime mask by the finite identity

\[
\mathbf1_{(n,k)=1}=\sum_{m\mid k,\ m\mid n}\mu_K(m).
\]

Put M=Nm and n=mx. Since m is chosen primary, n primary is equivalent to x primary. Also (m,ab)=1, so psi(m) is a scalar of modulus one. The resulting sum is

\[
\psi(m)\sum_{x\equiv1\ (3)}W(Nx/Y)\psi(x),
\qquad Y=Z/M.
\tag{3.1}
\]

If W is supported on [w_0,w_1], a nonempty sum requires Y>=1/w_1. If Y<1, only O_W(1) ideals can occur. For fixed k,m its squared sum over b is therefore O_W(B), which is at most O_W(P^2), and hence is covered by (1.2). Thus it suffices to prove the asserted bound when Y>=1.

Apply lattice Poisson summation on the primary coset modulo 3ab. Since psi is nonprincipal, the zero frequency vanishes: the primary residue classes project bijectively to the residue classes modulo ab, and the complete psi-sum is zero. The primitive Gauss evaluation has magnitude sqrt(N(ab)), including its vanishing at nonunit frequencies. The resulting sum has amplitude, up to fixed field constants,

\[
\mathcal A=\frac{Y}{\sqrt{N(ab)}}\asymp\frac{ZK}{MP},
\]

and actual frequency norm scale N(ab)/Y. Define the common comparison scale, fixed throughout the b sum, by

\[
J_0:=\frac{P^2M}{K^2Z}=\frac{B^2}{Y},
\qquad \frac{N(ab)}Y\asymp J_0.
\tag{3.2}
\]

The shape and uniformity of the frequency coefficients matter. In the same Fourier convention as the cited Gram lemma, the complete coefficient at h is

\[
e\!\left(\operatorname{Tr}\frac h{3\lambda}\right)
\psi(3\lambda)\overline{\psi(h)}g(\psi),
\qquad
g(\psi)=\sum_{x\bmod ab}\psi(x)
e\!\left(\operatorname{Tr}\frac{x}{ab}\right).
\tag{3.3}
\]

For sextic psi, **psi(3lambda) must not be replaced by one**. It has modulus one because (3lambda,ab)=1, and is a scalar for the row b. The normalized Gauss factor g(psi)/sqrt(N(ab)) and psi(m) are also row scalars of modulus one. Meanwhile

\[
\overline{\psi(h)}=\overline{\chi_a(h)}\chi_b(h).
\]

Thus the only variable character inside the frequency polynomial is chi_b(h). The factor overline(chi_a(h)) and the bounded-modulus phase in (3.3) belong to its frequency coefficients, independently of b. This remains valid at every nonunit frequency, where the appropriate character zero is retained.

The Fourier transform of x -> W(Nx/Y) is radial. Write its radial profile, with the fixed field normalizations absorbed, as W_hat. It is smooth at zero and decreases with all derivatives faster than every power at infinity. After extracting the displayed amplitude, its argument is a fixed multiple of Y Nh/N(ab). Thus the remaining dependence on b is solely through Nb/B. No angular direction of b enters the test.

## 4. Uniform smooth separation and summation of all frequency dyads

Take a nonzero frequency dyad Nh comparable to J, J>=1. Use a fixed smooth partition of unity. In the scaled variables x=Nh/J and y=Nb/B, the remaining kernel has the form

\[
y^{-1/2}V(x)\widehat W\left(c\frac{J}{J_0}\frac{x}{y}\right),
\]

where c stays in a fixed compact interval because a is fixed and Na/B is comparable to one. Its support in x,y is fixed. For every prescribed decay A and every fixed derivative order, its smooth norm is

\[
O_{A,W}((1+J/J_0)^{-A}).
\tag{4.1}
\]

Mellin separation on this compact rectangle gives polynomials in h whose coefficients are independent of b, integrated against a common integrable majorant. The majorant and the finitely many derivatives required for it satisfy (4.1), after increasing the Schwartz order. The factors y^(it) are row scalars of modulus one. Each separated frequency coefficient has modulus bounded by a fixed compact-support cutoff, since the character and phase factors have modulus at most one. Its squared coefficient norm is O_W(J), by lattice counting.

Apply Lemma 2.1 with squarefree-modulus scale comparable to B, and use Minkowski against the **uniform** Mellin majorant before taking the b norm. The squared row norm of this frequency dyad is at most

\[
(PZ)^\epsilon
\left(\frac{ZK}{MP}\right)^2
J\left[B+J+(JB)^{2/3}\right]
(1+J/J_0)^{-A}.
\tag{4.2}
\]

The sieve's factor (BJ)^epsilon is harmless here: J_0 is polynomially bounded in P,Z, and the rapid tail absorbs any extra power of J outside that range. Rechoose the preliminary epsilon to get the displayed final loss.

To recombine dyads, take square roots and use Minkowski. For every r>0 and sufficiently large A,

\[
\sum_{J\in\{1,2,4,\ldots\}}
J^{r/2}(1+J/J_0)^{-A/2}\ll_{r,A}J_0^{r/2}.
\tag{4.3}
\]

For J_0>=1 this follows by splitting at J_0 into two geometric series. For J_0<1 use (1+J/J_0)^(-A/2)<=J_0^(A/2)J^(-A/2), then A>r; this gives an even stronger bound. Thus no large-sieve theorem is applied with a row length below one, and no nonzero small-frequency term is silently discarded.

The three values of r in (4.2) are 1, 2, and 5/3. Substituting (3.2) after (4.3) bounds the squared row norm for fixed k,m by a subpower times

\[
\frac{PZ}{KM},\qquad
\frac{P^2}{K^2},\qquad
\frac{P^2Z^{1/3}}{K^2M^{1/3}}.
\tag{4.4}
\]

Since K,M,Z>=1, their sum is at most a fixed multiple of the right side in (1.2). For fixed k, Cauchy–Schwarz over the divisors m|k costs tau(k). The p' ranges for different k are disjoint; summing them and their divisor bounds costs a fixed power of tau(p), which is P^epsilon after rechoosing epsilon. This also covers the bounded Y<1 cases handled earlier. Dropping remaining restrictions on b occurs only in a nonnegative square-sum bound. Theorem 1.1 follows. \(\square\)

## 5. Fixed masks and a large-values corollary

An additional fixed exclusion (n,S_0)=1 is handled by finite inclusion–exclusion over the product of the primes in S_0 outside 3. The n-primary condition already excludes the prime above 3. Take each divisor d in its primary convention and write n=dx. The scale changes to Z/Nd and a character scalar of modulus at most one is introduced. These norms are fixed, so Theorem 1.1 and its bounded-small-scale treatment apply with only a constant depending on S_0. This adapter is for fixed S_0; it does not assert uniformity under arbitrarily growing masks.

For a Gram-matrix consequence, now assume W>=0. Define

\[
v_p(n)=W(Nn/Z)^{1/2}\chi_p(n),
\qquad
S_p=\sum_n c_n v_p(n),
\qquad A_2=\sum_n|c_n|^2.
\]

The n indices are primary, and c is any finitely supported vector. The diagonal satisfies ||v_p||_2^2=O_W(Z). For any selected set of R character rows, the sum of absolute off-diagonal Gram entries in one row is at most

\[
\sqrt R\left(\sum_{p'\ne p}|T_{p,p'}(Z)|^2\right)^{1/2}.
\]

The Hermitian Gram matrix therefore has operator norm at most

\[
\ll(PZ)^\epsilon\left[Z+\sqrt R\sqrt{G(P,Z)}\right],
\quad G(P,Z)=PZ+P^2Z^{1/3}.
\]

Hilbert-space duality gives the precisely normalized Bombieri–Halász–Montgomery consequence

\[
\boxed{\sum_{p\in\mathcal R}|S_p|^2
\ll(PZ)^\epsilon A_2
\left[Z+\sqrt R\sqrt{G(P,Z)}\right].}
\tag{5.1}
\]

In particular, if every selected row satisfies |S_p|>=V_amp,

\[
R V_{\rm amp}^2
\ll(PZ)^\epsilon A_2
\left[Z+\sqrt R\sqrt{G(P,Z)}\right].
\tag{5.2}
\]

There is no extra normalization by Z in this statement: A_2 is the displayed coefficient energy. For coefficients originally supported in an interval where W is bounded below, divide them by sqrt(W) to use this form, with their corresponding weighted A_2. Young's inequality also yields

\[
R\ll(PZ)^\epsilon\left(
\frac{A_2Z}{V_{\rm amp}^2}
+\frac{A_2^2G(P,Z)}{V_{\rm amp}^4}\right),
\tag{5.3}
\]

after reassigning epsilon.

The signed off-diagonal correlations have been estimated before the final Gram norm is bounded. This is more source-specific information than a count of algebraic diagonals, but it does not by itself establish a fourth moment for the balanced Möbius product or the Patterson source's exceptional-moment power saving for this different sextic family.
