# Bounded audit of the all-order collision kernel

Audit date: 2026-10-10. Reviewed source: PR #916 at exact commit `dabd6da99fb92eead7c99f941331ed9cbd2ec4ad`, `standalone/2026-10-10-all-order-collision-removal/PROOF.md` and `MOMENT_FRONTIER.md`. Comparison sources: PR #912 at `6afd64e042ce7b59d550c3d76e9e2cca8b2c7379`, `MASKS_AND_EULER_FACTORS.md`, Sections 3–4; PR #915 at `9959364671f89b86f3992ec5ed5e19f804eb607b`, `ANISOTROPIC_SINGLETON_CORES.md`, Section 2; and the exact A2/coupled-theta interface in the adjacent `conductor-combination/INTERFACE_COMPARISON.md`.

Verdict: the collision-kernel identities, the logarithmic mass theorem, and the positive norm transfers pass this mathematical audit with their stated fixed-order, enlarged-exclusion, and full-rectangle hypotheses. The moment-defect implications also pass the direct check below. These are reductions and conditional implications, not a new fourth moment, a sublinear moment-defect theorem, or a zero-free improvement. This is an AI-agent source audit, not human peer review or proof-assistant verification. No published file was changed.

## 1. The small-prime hypothesis is explicit and sufficient

The source first fixes the order k and enlarges its fixed finite set S to contain every prime ideal of norm at most (2k)^3. S is then unchanged throughout every row and scale in the identities and norm estimates. Thus its phrase "same fixed S" does not assert validity of the positive-kernel mass theorem for an arbitrary smaller pre-existing set.

Let r=binom(k,2). The two local series are

\[
R_k(\mathbf z)=\frac{\prod_i(1-z_i)}{1-\sum_i z_i}
=\sum_{\mathbf a}c_k(\mathbf a)\mathbf z^{\mathbf a},
\qquad
Q_k(\mathbf z)=R_k(\mathbf z)^{-1}.
\tag{1.1}
\]

The source proves c_k>=0 by its recurrence: on a binary multi-index of support size s the coefficient is the derangement number !s; on a nonbinary multi-index the numerator contributes zero and the coefficient is a sum of preceding coefficients. This induction is valid, including single-coordinate coefficients, which all vanish. The nonconstant coefficient of Q_k is exactly 1-|supp(a)|, and hence is nonpositive. Both absolute kernels first occur at degree two, with exactly r monomials of coefficient one.

At equal arguments t the collapsed absolute local series are therefore exactly

\[
F_k^+(t)=\frac{(1-t)^k}{1-kt},\qquad
F_k^-(t)=2-\frac{1-kt}{(1-t)^k}
=1+r t^2+O_k(t^3),
\tag{1.2}
\]

where the last expansion also holds for F_k^+. The pole 1-kt=0 is a real concern for the positive kernel, but the source's hypothesis removes it: for p outside S and sigma>1/3,

\[
(Np)^{-\sigma}<\frac1{2k}<\frac1k.
\tag{1.3}
\]

All local absolute series used in the proof converge uniformly inside this radius. There is no division by a possibly zero row character: theta_u(prod d_i) is factored only after a formal coefficient identity and is used as a norm contraction.

## 2. Verification of the critical logarithmic mass

Put E_(k,p)^±(t)=(1-t^2)^r F_k^±(t). Its degree-one and degree-two coefficients vanish. The preceding radius bound shows that the absolute local remainder is O_k(|t|^3), uniformly at every allowed prime. Consequently

\[
E_k^\pm(s)=\prod_{p\notin S}E_{k,p}^\pm((Np)^{-s})
\tag{2.1}
\]

has an absolutely convergent ideal Dirichlet series for Re(s)>1/3. At s=1/2 every local factor is positive; it differs from one by a summable O_k((Np)^(-3/2)) quantity. Thus E_k^±(1/2)>0.

Group a tuple d by the product ideal n=prod_i d_i. Writing f_k^±(n) for its total absolute coefficient, exact coefficient multiplication gives

\[
\sum_n f_k^\pm(n)(Nn)^{-s}
=\zeta_K^S(2s)^rE_k^\pm(s),\qquad
f_k^\pm(n)=\sum_{a^2b=n}d_{r,S}(a)e_k^\pm(b).
\tag{2.2}
\]

This is an ordinary multiplicative coefficient identity for the correction kernel itself. It makes no ordinary-Euler-product claim about the later twisted Gauss coefficients.

The ideal harmonic convolution in this fixed class-number-one imaginary quadratic field satisfies

\[
\sum_{Na\le X}\frac{d_{r,S}(a)}{Na}
=\frac{\kappa_S^r}{r!}(\log X)^r
+O_{r,S}((1+\log X)^{r-1}).
\tag{2.3}
\]

The source derives this from lattice-point counting, partial summation and induction; its displayed induction has the correct leading factor and error order. Insert (2.3) into the weighted convolution (2.2). Absolute convergence of E at any fixed number between 1/3 and 1/2 allows every required logarithmic moment of |e(b)|/sqrt(Nb), and bounds the omitted tail by a negative power. This proves the claimed sharper asymptotic

\[
\boxed{
K_k^\pm(Z)=
\frac{\kappa_S^rE_k^\pm(1/2)}{2^r r!}(\log Z)^r
+O_{k,S}((1+\log Z)^{r-1}).}
\tag{2.4}
\]

The factor 2^(-r) is required because a is truncated at sqrt(Z/Nb). In particular the weaker bound O((1+log Z)^r) is valid. Constants are allowed to depend on the fixed k,S; no uniformity in growing k is proved or needed for the later cofinal-order criterion.

There is a simpler upper-bound proof already in PR #912, Proposition 4.1: restrict to primes of norm at most the product horizon, enlarge to their full local absolute series, and use the prime harmonic sum. Thus #916's upper logarithmic norm exponent is compatible with and substantially overlaps the earlier packet. Its explicit total-product asymptotic additionally records the positive leading constant.

### Why one cannot drop the exclusion hypothesis

This is a scope check, not a flaw in the source, which states the exclusion. Suppose an allowed prime p has norm q<k^2. The coefficient of t^m in F_k^+(t), for m>=k, is

\[
[t^m]F_k^+(t)=k^m(1-1/k)^k.
\tag{2.5}
\]

Indeed expand (1-t)^k and sum the finite binomial series against k^(m-j). Tuples supported only at p with total exponent m contribute

\[
k^m(1-1/k)^k q^{-m/2}
=(1-1/k)^k(k/\sqrt q)^m
\tag{2.6}
\]

to the positive weighted mass. Taking m=floor(log_q Z) proves

\[
K_k^+(Z)\gg_{k,q} Z^{\log_q k-1/2}
\quad\text{for all sufficiently large }Z.
\tag{2.7}
\]

For example, k=3 and an allowed Eisenstein prime of norm 7 give power growth, since 3>sqrt(7). The finite set containing only the conventional primes over 6 would not remove this example. The source's enlarged set does remove it. By contrast the absolute Q_k kernel has only single-coordinate denominators 1-t; its local series converges at t=q^(-1/2) for every q>1. The small-prime geometric obstruction belongs to the positive R_k direction.

## 3. What the exact norm equivalence says

The finite coefficient identities are valid for arbitrary completely multiplicative theta_u with |theta_u|<=1, including its zero extension. At each allowed prime the independent Möbius product has local polynomial prod_i(1-z_i), while its pairwise-coprime part has 1-sum_i z_i. Convolution by R_k or Q_k therefore gives both smooth identities at unchanged S, with separately shortened scales X_i/Nd_i. They do not discard signed terms or change any row.

Minkowski, contraction by theta_u(prod_i d_i), and (2.4) give a logarithmic norm loss of r and an energy loss of 2r=k(k-1). Reverse transfer from equal-test moments to arbitrary shorter rectangles uses Hölder at the same row set; its normalization is exactly sqrt(H prod_i X_i). These steps check.

The essential quantifier is the fixed physical row range H over the entire rectangle of smaller scales. A theorem only on H=X^(1+theta) for each individual X is not by itself this envelope. The source explicitly records this distinction. Its moving-exclusion adapter also checks: after the fixed enlargement of S,

\[
\prod_{p\mid c,\ p\notin S}(1-k/\sqrt{Np})^{-1}
\ll_{k,S,\epsilon}(Nc)^\epsilon.
\tag{3.1}
\]

The full geometric local series is finite at every allowed prime; sufficiently large prime factors have logarithm at most epsilon log Np, while the finitely many smaller factors contribute a fixed constant. This estimate is uniform in the moving ideal c, but still needs the full rectangular analytic hypothesis.

## 4. Comparison with the direct anisotropic result and the A2 interface

PR #915's anisotropic proof uses Q_k, with the moving exclusion merged directly into its local factors. At positive weights alpha_i satisfying alpha_i+alpha_j>1 for every distinct pair, its absolute coefficient norm converges. In its application one axis has weight 1/2 and the others have weight b>1/2. It needs no small-prime enlargement, since its denominators are only 1-z_i. It establishes a conditional component estimate from a second moment and pointwise bounds; it does not rely on the positive inverse kernel.

PR #916 uses both directions at the critical symmetric weights alpha_i=1/2. Pair collisions are then harmonic instead of summable, producing the logarithmic mass. These two statements agree exactly at the coefficient level, but have different analytic uses. Passing to the critical symmetric weight does not manufacture the missing rectangular moment estimate from the existing anisotropic component estimate.

The collision kernel does **not** directly remove the exclusions in the A2/coupled-theta mixed family. Its proof requires a common completely multiplicative theta_u and the local Möbius polynomial 1-sum_i z_i. The Poisson-generated Gauss coefficient instead obeys

\[
a_\xi(pn)=a_\xi(p)a_\xi(n)\chi_n(p)^4
\qquad(p\nmid n,\ pn\text{ squarefree}).
\tag{4.1}
\]

A prime shift changes the character of the remaining column, rather than multiplying it only by a row scalar. In the literal A2 projection it changes the auxiliary from f to ef and the exclusion from q_0 to q_0cde. The two labels may overlap. The mixed completion's theta twist then contains af_t as well as a moving exclusion on its inner squarefree and cube indices. The simple factors in (1.1) are not the coefficient system of that family.

Thus #916 can eliminate moving exclusions as a separate premise when formulating an **original Möbius collision-free rectangular target**. It does not automatically solve the moving-conductor reflected estimate generated by a proposed proof of that target. The exact A2-to-coupled-theta composition remains useful, with its precisely stated mixed children; its analytic requirements are not removed by relabeling the Möbius kernel.

## 5. Defect-aware extraction and fixed exclusions at cofinal orders

The source's conditional implication is

\[
\sum_{0<Nu\le D^h}|A_u(D;W)|^{2k}
\ll D^{h+k+\lambda+\epsilon}
\quad\Longrightarrow\quad
A_1(D;W)\ll D^{1/2+(\lambda+5h/6)/(2k)+\eta}.
\tag{5.1}
\]

Its normalization checks: averaging over prime sixth powers with Np comparable to D^(h/6) divides the moment by D^(h/6), up to a logarithm. The exponent after the 2k-th root is (k+lambda+5h/6)/(2k). The exact recurrence removes the p-exclusion in the coefficient without assuming conductor-uniform estimates at a changing p. All smaller arguments lie below D/2 for large D, and the geometric sum over their powers is O(D^beta D^(-h beta/6)) for any fixed beta above the claimed exponent, closing the stated induction. The proof works for each fixed h>0.

For nonvanishing, the estimate must hold for each needed smooth test; after fixing a hypothetical zero, choose a test whose Mellin transform is nonzero there. The holomorphic Mellin integral then rules out that zero in the open half-plane. This test quantifier is present in the source. No critical boundary-line assertion follows at a single fixed order.

At an unbounded sequence of orders k_j, the sufficient condition is

\[
\frac{\lambda_j+5h_j/6}{k_j}\longrightarrow0.
\tag{5.2}
\]

The fixed set S may depend on j. This causes no logical loss in the nonvanishing deduction: choose one finite j after fixing a putative zero, and use that all its finitely deleted Euler factors are nonzero for Re(s)>0. Constants may depend arbitrarily on this selected order and its finite S. The conditional norm-factorization transfer to Dirichlet L-functions and the functional-equation step do not require a uniform-in-j constant.

This supplies a legitimate weaker research target: sublinear defects at cofinal orders can suffice, rather than ideal moments at every order. It does not prove even one new defect estimate for the genuine family. In particular the useful fourth-moment threshold lambda<2/3 at h arbitrarily close to 1 is a target, not a consequence of collision removal. No new numerical zero-free boundary is established by the combination audited here.

## 6. The literal combination with the existing anisotropic estimate

There is a precise useful limitation on this combination. Use PR #915's imported second-moment input at H=D^h, h=1+theta>1, and its stated row-uniform pointwise input with exponent b>1/2. Its anisotropic theorem gives

\[
\frac{\|B_{1,\cdot}(\mathbf X)\|_2^2}{H\prod_iX_i}
\ll D^\epsilon\left(\frac{\prod_iX_i}{\max_iX_i}\right)^{2b-1}
\le D^{(k-1)(2b-1)+\epsilon}
\tag{6.1}
\]

on the full rectangle X_i<=D. Apply #916's norm comparison, allowing its fixed order-dependent exclusion set. The resulting moment defect is

\[
\lambda_k=(k-1)(2b-1).
\tag{6.2}
\]

This agrees with the simpler estimate using one second moment and k-1 pointwise factors. Its defect-aware extraction exponent is exactly

\[
\alpha_k
=b+\frac{5h/6-(2b-1)}{2k}.
\tag{6.3}
\]

For the relevant b near 7/8 and h>1, the last correction is positive and tends to zero as k grows. Thus these currently proved inputs approach their existing pointwise boundary b from above; they do not give the sublinear-defect hypothesis or a new boundary below b. This is a limitation of the displayed estimates and their combination, not a theorem limiting the genuine moments or future cancellation. It identifies why the cofinal-order criterion still needs an additional arithmetic gain.
