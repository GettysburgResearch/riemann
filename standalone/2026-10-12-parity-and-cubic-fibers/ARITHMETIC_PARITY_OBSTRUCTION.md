# Arithmetic parity obstruction: prime faces and the isolated Möbius parameter

Status: proposed research mathematics, with complete proofs below. These are asymptotic obstructions to enlarged coefficient classes and to positive subdivision of the native moment. They do not refute, prove, or supply a new zero-free region for the full Möbius moment.

Scope: the principal coefficient twist over K = Q(sqrt(-3)); all nonzero element rows, including sixth powers; one fixed, nonnegative, nonzero smooth compactly supported norm test; every fixed integer k >= 1. No hypothesis about zeros of an L-function is used. The lower bounds are subsequential growth statements, not prime-number-theorem asymptotics.

Exact repository dependencies: the native ideal-column/element-row convention in PR 926, commit 086bf0560c0c2679a1fe41418f583d2c5ca743c3, standalone/2026-10-10-mobius-overlaps-and-sampled-moments/SAMPLED_MOMENT_CRITERION.md, equations (1.1)-(1.2). For comparison, PR 911, commit 2f8b6a3898a722d0602a91dea73bac344a3bb7dd, research/exploratory/2026-10-10-four-hour-wave/literature/SIGNED_BALANCED_NATIVE_WITNESS.md, supplies a finite native singleton witness; its two-hour-continuation/literature/PRIME_SLOT_ROUTE_STATUS.md keeps the full prime-slot complement open. Neither source is being promoted to an asymptotic theorem here.

Classical context: the singularity of a nonintegral power of zeta is the mechanism behind the Selberg-Delange method. See R. de la Breteche and G. Tenenbaum, *Remarks on the Selberg-Delange method*, arXiv:2010.12929v8, introduction and equation (1.10). That paper explicitly records the vanishing of all expansion coefficients at nonpositive integral zeta exponents. We use only an elementary Mellin noncontinuation argument, proved here, and do not import a uniform Selberg-Delange estimate. Ideal counting and its zeta-pole consequence can also be compared with A. Sutherland, MIT 18.785 (Fall 2021), Lecture 19, Theorem 19.12; the needed special case is proved below by lattice counting.

What was actually done: exact ideal/element counting, coprimality inclusion-exclusion, Euler factorization, a complex-analytic noncontinuation proof, and Holder amplification on actual sixth-power rows. No finite experiment is used to infer an infinite assertion.

Smallest remaining gap: these results identify cancellation that a proof must retain. They give no bound for the signed quadratic/cubic Walsh remainder of the complete original coefficient sequence.

## 1. Native convention and elementary counting

Put O = Z[omega], omega = exp(2 pi i/3), and N(a) = |a|^2. The index n below is a nonzero integral ideal. Let S be a fixed finite set of prime ideals containing the primes above 2 and 3. For squarefree n coprime to S, let

\[
\chi_n(u)=(u/n)_6
\]

be the native multiplicative sextic residue symbol, extended by zero if (u,n) != 1. In particular,

\[
\chi_n(v^6)=\mathbf 1_{(v,n)=1}.                         \tag{1.1}
\]

There is no squarefree restriction on the nonzero element row u or on v.

Fix once and for all W in C_c^infinity((0,infinity)), W >= 0, W not identically zero, with support contained in [a,b], 0 < a < b < infinity. Write

\[
\widehat W(s)=\int_0^\infty W(y)y^{s-1}\,dy;
\qquad \widehat W(1)>0.                                  \tag{1.2}
\]

The Eisenstein integers are norm-Euclidean: every complex number is within distance at most 1/sqrt(3) < 1 of a lattice point, so division with smaller norm remainder is possible. Thus every ideal is principal. The lattice O has covolume sqrt(3)/2 and six units. Covering a disk by fundamental parallelograms, the discrepancy is supported in a boundary annulus of bounded width. Consequently

\[
I(X):=\#\{\mathfrak a:N\mathfrak a\le X\}
=\kappa X+O(\sqrt X),\qquad
\kappa=\frac{\pi}{3\sqrt3},\quad X\ge1.                    \tag{1.3}
\]

The same estimate with O(sqrt(X)) remains valid for 0 < X < 1, since I(X)=0 and X <= sqrt(X). Partial summation gives, initially for Re s > 1,

\[
\zeta_K(s)=s\int_1^\infty I(x)x^{-s-1}\,dx
=\frac{\kappa s}{s-1}
 +s\int_1^\infty (I(x)-\kappa x)x^{-s-1}\,dx.              \tag{1.4}
\]

The last integral is holomorphic for Re s > 1/2. In particular zeta_K has a simple pole of residue kappa at 1. This is the only zeta fact used below, in addition to its absolutely convergent Euler product for Re s > 1.

For every nonzero ideal a, a generator v is determined up to a sixth root of unity. Therefore v^6 is independent of that choice, and

\[
\mathfrak a\longmapsto v^6
\]

is an injection from ideals of norm at most V to actual nonzero element rows of norm at most V^6. Indeed v^6=w^6 implies v/w is a unit. It follows that the native row family contains exactly I(V) distinct rows of this form; no artificial row multiplicity is being inserted.

For a squarefree ideal n, define

\[
g(n)=\prod_{p\mid n}\left(1-\frac1{Np}\right).
\]

Inclusion-exclusion and (1.3), including its small-X version, give the uniform estimate

\[
\begin{aligned}
I_n(V)&:=\#\{\mathfrak a:N\mathfrak a\le V,(\mathfrak a,n)=1\}\\
 &=\sum_{d\mid n}\mu_K(d)I(V/Nd)\\
 &=\kappa Vg(n)+O\!\left(\sqrt V\sum_{d\mid n}(Nd)^{-1/2}\right)\\
 &=\kappa Vg(n)+O(\sqrt V\,\tau_K(n)).                    \tag{1.5}
\end{aligned}
\]

The constant is independent of n and V. In particular divisors with Nd > V have not been silently deleted from the main term.

We will also use the elementary fixed-weight bound

\[
C^{\omega(n)}\tau_K(n)(1+\omega(n))^j\ll_{C,j,\epsilon}(Nn)^\epsilon
                                                               \tag{1.6}
\]

for squarefree n, fixed C,j and every epsilon > 0. To prove it, absorb each factor at a sufficiently large prime into (Np)^epsilon, and absorb the finitely many smaller primes into the constant; reduce a fixed polynomial in omega to another fixed exponential. Together with (1.3), this bounds the sum of the left side over Nn <= bD by O(D^{1+epsilon}).

## 2. A Mellin growth lemma

### Lemma 2.1 (a nonremovable singularity forces full exponent)

Let a(n) be ideal coefficients satisfying |a(n)| <<_epsilon (Nn)^epsilon. Suppose their Dirichlet series F(s) is absolutely convergent for Re s > 1 and admits no holomorphic extension through s=1. Put

\[
C(D)=\sum_n a(n)W(Nn/D).
\]

If the germ of F(s)\widehat W(s) also has no holomorphic extension through 1, then

\[
\limsup_{D\to\infty}\frac{\log(1+|C(D)|)}{\log D}=1.       \tag{2.1}
\]

Here W is as in Section 1, so its nonzero value at 1 preserves every nonremovable singularity of F there.

**Proof.** The upper bound follows from (1.3) and the coefficient bound. For Re s > 1, absolute convergence and the substitution y=Nn/D give the exact Mellin identity

\[
\int_0^\infty C(D)D^{-s}\,\frac{dD}{D}
=\widehat W(s)F(s).                                     \tag{2.2}
\]

The integrand is identically zero for D < 1/b. If C(D)=O(D^{1-delta}) for some delta > 0, the left side defines a holomorphic function for Re s > 1-delta, contradicting the assumed singularity. Therefore there is no such power saving. This proves (2.1). Equivalently, for each eta > 0 there are arbitrarily large D with |C(D)| >= D^{1-eta}. The subsequence may depend on eta. No sign or Tauberian hypothesis on a(n) is required. QED.

## 3. The actual all-distinct prime face is too large to pay separately

Define the prime-column polynomial and its moment

\[
P_u(D)=\sum_{p\notin S}\chi_p(u)W(Np/D),\qquad
\mathcal P_{2k}(D,H)=\sum_{0<Nu\le H}|P_u(D)|^{2k}.         \tag{3.1}
\]

For principal nu, the native Möbius polynomial restricted to primes is -P_u(D). Its even moment is exactly (3.1).

In its finite 2k-column expansion let S_dist(D,H) be the sum over ordered tuples

\[
(p_1,\ldots,p_k,q_1,\ldots,q_k)
\]

whose 2k prime ideals are all distinct, retaining the original Hermitian phases and then summing all rows 0 < Nu <= H. This is a real signed sector: swapping the two k-tuples conjugates each summand and preserves the sector. It is not declared positive term by term.

### Theorem 3.1 (asymptotic singleton prime-face obstruction)

Fix an integer k >= 1 and 0 < h < 6/5. For every eta > 0, there are arbitrarily large D such that

\[
S_{\rm dist}(D,D^h)\ge D^{2k+h/6-\eta}.                  \tag{3.2}
\]

For k >= 2 and 1 < h < 6/5, this excludes a bound

\[
|S_{\rm dist}(D,D^h)|\ll_\epsilon D^{h+k+\epsilon}
\quad\hbox{for every epsilon > 0}.                       \tag{3.3}
\]

More generally, any all-epsilon estimate with exponent h+k+e must have e >= k-5h/6.

**Proof.** Let Q(s)=sum_{p notin S}(Np)^{-s}. For Re s > 1,

\[
Q(s)=\log\zeta_K(s)-E_2(s),
\]

where E_2 consists of finitely many excluded first-prime terms and the terms of degree >= 2 in the Euler logarithm. It is holomorphic in a neighborhood of 1 because the latter sum converges absolutely for Re s > 1/2. By (1.4), Q(s) has a logarithmic singularity at 1. Apply Lemma 2.1 to the prime-indicator coefficient. Thus, for every delta > 0, the nonnegative sum

\[
P_1(D)=\sum_{p\notin S}W(Np/D)
\]

is at least D^{1-delta} for arbitrarily large D.

Set H=D^h and V=H^{1/6}. For all sufficiently large D, V < aD, because h < 6. A prime ideal p with W(Np/D) != 0 has Np >= aD and cannot divide any nonzero ideal of norm at most V. Thus every one of the I(V) actual rows indexed by v^6 satisfies, exactly,

\[
P_{v^6}(D)=P_1(D).
\]

It follows that

\[
\mathcal P_{2k}(D,D^h)\ge I(V)|P_1(D)|^{2k}
\gg D^{h/6+2k(1-delta)}                                 \tag{3.4}
\]

on those arbitrarily large scales.

Every tuple omitted from S_dist has a coincident pair among its 2k positions. There are at most binom(2k,2) choices of such a pair and O(D^{2k-1}) assignments of the remaining prime-ideal positions, by (1.3). Each weight/character product is bounded in modulus by a constant depending only on W,k, and the number of all element rows is O(H). Hence

\[
|\mathcal P_{2k}(D,H)-S_{\rm dist}(D,H)|
\ll_{W,k,K}H D^{2k-1}.                                  \tag{3.5}
\]

Choose delta > 0 so small that 2k delta < 1-5h/6 and 2k delta < eta. The exponent of (3.4) strictly exceeds that of (3.5), so their difference is eventually positive on the chosen subsequence. By decreasing delta once more, the fixed positive constant is absorbed into the requested eta. This proves (3.2). Comparing exponents proves the final assertions. QED.

### What this theorem does and does not say

Every tuple in S_dist lies in the completely singleton incidence pattern: no prime ideal is shared between any two columns, and the original equal-product diagonal is absent. All 2k Möbius signs multiply to +1. Its odd-parity conductor is the product of all 2k primes, of norm comparable to D^{2k}; the source's shared-divisor correction variables are trivial on this face.

The theorem is an obstruction to estimating this *selected prime face* independently and then summing positive bounds. Selection by primality depends on the free singleton ideals. It is outside the selector scope of a theorem that allows arbitrary choices only among already frozen shared incidences. In particular it does not contradict PR 928's shared-graph sector results.

The complete native singleton sector also contains composite squarefree columns. It can cancel the prime face after the signed expansion is reunited. No lower bound for that complete sector or for the full Möbius moment follows from (3.2). The asymptotic statement is a strengthening of the lesson from the finite native witnesses, not a conversion of those witnesses into a global proof.

## 4. The Möbius parameter is isolated under prime-count deformation

For a fixed complex z with |z-1| < 1/4, define the deformed coefficient family

\[
A_{z,u}(D)=\sum_{(n,S)=1}\mu_K(n)z^{\omega(n)}
                  \chi_n(u)W(Nn/D),
\qquad
M_{2k,z}(D,H)=\sum_{0<Nu\le H}|A_{z,u}(D)|^{2k}.           \tag{4.1}
\]

Since mu_K vanishes outside the squarefree ideals, omega can equivalently be replaced by the total number Omega of prime factors with multiplicity. At z=1 this is exactly the principal member of the original family.

Let

\[
B_u(D)=\left.\partial_z A_{z,u}(D)\right|_{z=1}
=\sum_{(n,S)=1}\mu_K(n)\omega(n)\chi_n(u)W(Nn/D).           \tag{4.2}
\]

### Theorem 4.1 (native sixth-power amplification of the branch)

For every fixed z in the indicated disk with z != 1, every fixed h > 0, and every fixed integer k >= 1,

\[
\limsup_{D\to\infty}
\frac{\log(1+M_{2k,z}(D,D^h))}{\log D}
\ge 2k+\frac h6.                                        \tag{4.3}
\]

The same assertion holds with sum_{0<Nu<=D^h}|B_u(D)|^{2k} in place of M_{2k,z}.

Thus an estimate M_{2k,z}(D,D^h) <<_epsilon D^{h+k+e+epsilon} for every epsilon > 0 necessarily has

\[
e\ge k-\frac{5h}{6}.                                   \tag{4.4}
\]

No assertion (4.3) is made for z=1.

**Proof, Euler factorization.** Put

\[
C_z(D)=\sum_{(n,S)=1}\mu_K(n)z^{\omega(n)}g(n)W(Nn/D).
\]

For Re s > 1 its Dirichlet series is

\[
F_z(s)=\prod_{p\notin S}
\left(1-z(1-(Np)^{-1})(Np)^{-s}\right)
=\zeta_K(s)^{-z}E_z(s),                                 \tag{4.5}
\]

where

\[
E_z(s)=
\prod_{p\in S}(1-(Np)^{-s})^{-z}
\prod_{p\notin S}
\frac{1-z(1-(Np)^{-1})(Np)^{-s}}{(1-(Np)^{-s})^z}.         \tag{4.6}
\]

Powers and logarithms on the right are fixed by their Euler-series branches. The logarithm of a good-prime factor is

\[
z(Np)^{-s-1}+O_z((Np)^{-2\Re s}).
\]

Its prime sum converges locally uniformly for Re s > 1/2, uniformly for z in compact subsets of the displayed disk. At good primes Np >= 7, all local numerators are nonzero there: |z|(1-1/Np)(Np)^{-Re s} < (5/4)/sqrt(7) < 1. The fixed excluded-prime factors are nonzero for Re s > 0. Consequently E_z(s) is holomorphic and nonzero for Re s > 1/2, jointly with z in that disk.

By (1.4), on a slit neighborhood of s=1,

\[
F_z(s)=(s-1)^zG_z(s),\qquad G_z(1)\ne0,                 \tag{4.7}
\]

where G_z is holomorphic jointly in s,z. For z != 1 in the disk, z is nonintegral, so (4.7) has no holomorphic continuation through 1. One can see this without a choice of a closed continuation path: a nonzero holomorphic function has integral order of vanishing at 1, whereas (s-1)^zG_z(s) has nonintegral order or a nontrivial oscillating argument on the positive real approach. Equivalently its local monodromy is exp(2 pi i z) != 1. Lemma 2.1 therefore gives

\[
\limsup_{D\to\infty}\frac{\log(1+|C_z(D)|)}{\log D}=1.    \tag{4.8}
\]

Differentiating (4.7) at z=1 yields

\[
\left.\partial_zF_z(s)\right|_{z=1}
=(s-1)G_1(s)\log(s-1)+(s-1)\left.\partial_zG_z(s)\right|_{z=1}.
                                                               \tag{4.9}
\]

Its logarithmic singularity is nonremovable because G_1(1) != 0. Its Dirichlet coefficients are mu_K(n)omega(n)g(n) on (n,S)=1. Applying Lemma 2.1 again proves (4.8) for C'_1 as well.

**Proof, physical rows and error control.** Write a(n) for either mu_K(n)z^{omega(n)} or mu_K(n)omega(n), with the fixed S exclusion, and write C(D)=sum a(n)g(n)W(Nn/D). Take V=D^{h/6}. Summing (1.1) over the I(V) distinct sixth-power rows, then using (1.5)-(1.6), gives

\[
\sum_{N\mathfrak a\le V} A_{v_{\mathfrak a}^6}(D)
=\kappa V C(D)+O_{\epsilon,z,W}(\sqrt V D^{1+\epsilon}).  \tag{4.10}
\]

There is no positivity assumption on the coefficients in this interchange: all sums are finite. For any delta > 0, (4.8) supplies arbitrarily large D with |C(D)| >= D^{1-delta}. Choose epsilon,delta > 0 with epsilon+delta < h/12. The error in (4.10) is then smaller than one half of the main term for sufficiently large D along this subsequence. Holder on these actual rows gives

\[
\begin{aligned}
\sum_{0<Nu\le D^h}|A_u(D)|^{2k}
&\ge I(V)^{1-2k}
  \left|\sum_{N\mathfrak a\le V} A_{v_{\mathfrak a}^6}(D)\right|^{2k}\\
&\gg V |C(D)|^{2k}
\gg D^{h/6+2k(1-delta)}.                                \tag{4.11}
\end{aligned}
\]

Let delta tend to zero, choosing a corresponding positive epsilon each time. This is a limsup statement, so the subsequences need not agree. Equations (4.3)-(4.4) follow. QED.

### Corollary 4.2 (cofinal coefficient-generalization barrier)

Suppose k runs through any cofinal sequence, h_k=o(k), and a proposed argument asks for the diagonal-size hierarchy throughout any fixed complex neighborhood of z=1, or even at one fixed nonintegral z in that neighborhood. Then (4.4) forces

\[
\liminf_{k\to\infty}\frac{e_k}{k}\ge1.                  \tag{4.12}
\]

The same is true if the argument requires this hierarchy for the prime-count derivative B. Constants may depend arbitrarily on each fixed k and z; that does not avoid the exponent obstruction. This is stronger than a failure of uniformity as z approaches 1: each fixed neighboring parameter already fails.

### Why this matters for the full coefficient sequence

The factors z^{omega(n)} have only subpower size at every fixed z, but they alter the first-prime Euler coefficient. The principal zeta pole is converted into a branch for all neighboring nonintegral z; at the integer z=1 it becomes an ordinary zero. The theorem detects this exact cancellation point. It does not predict the magnitude of the native Möbius sum there.

Accordingly, scale differentiation of the fixed smooth W and differentiation in the prime-count parameter are very different operations. The former only changes the fixed test and is used legitimately in PR 926; the latter produces (4.9) and is obstructed. A proof cannot justify coefficient differentiation by appealing to the already proved scale-derivative bounds.

## 5. Two admissible conclusions, and one unresolved route

1. **Keep the complete Möbius parity.** A proof that pays every primality or prime-count class separately is ruled out by Theorem 3.1. The full signed union can still satisfy the target. The quadratic/cubic Walsh expansion in the companion note retains exactly this missing parity information.

2. **Random signs are a comparison problem, not a coefficient perturbation bound.** The independent-sign hierarchy can be small while every fixed nonintegral global prime-count perturbation is large. A random-sign theorem therefore needs an explicit comparison with the actual arithmetic row measure; it cannot be converted to the deterministic Möbius estimate by local continuity in z.

3. **Centering needs a row-specific, noncircular definition.** Multiplying every twisted Dirichlet series by zeta_K(s)^{z-1} cancels the principal branch at 1, but introduces one at 1 for a nonprincipal twist whose L-function is regular and nonzero there. Subtracting a full local Hankel contribution only on truly principal twists is a possible exploratory construction, but no uniform conductor estimate or moment comparison for that construction is proved here. A finite logarithmic asymptotic subtraction would also leave terms of power exponent 1. We do not use such a centering as an established input.

The successful generalized moment proof still has to estimate a signed, coefficient-specific remainder. These theorems make two broad replacements of that task mathematically unavailable, while leaving the intended Möbius hypothesis intact.

## References

- R. de la Breteche and G. Tenenbaum, *Remarks on the Selberg-Delange method*, arXiv:2010.12929v8: https://arxiv.org/abs/2010.12929v8 . Classical context only; no asymptotic theorem from it is used in the proofs.
- A. V. Sutherland, *18.785 Number Theory I, Lecture 19: The analytic class number formula*, Fall 2021: https://math.mit.edu/classes/18.785/2021fa/LectureNotes19.pdf . Comparison for (1.3)-(1.4); their Eisenstein special case was proved above.
- PR 926 fixed native family and sampled criterion: https://github.com/GettysburgResearch/riemann/blob/086bf0560c0c2679a1fe41418f583d2c5ca743c3/standalone/2026-10-10-mobius-overlaps-and-sampled-moments/SAMPLED_MOMENT_CRITERION.md .
- PR 911 finite native singleton witness: https://github.com/GettysburgResearch/riemann/blob/2f8b6a3898a722d0602a91dea73bac344a3bb7dd/research/exploratory/2026-10-10-four-hour-wave/literature/SIGNED_BALANCED_NATIVE_WITNESS.md .
- PR 928 shared-graph selector scope: https://github.com/GettysburgResearch/riemann/blob/ab98878279cd5614fe79bb94aa916e97c9ee50b4/standalone/2026-10-10-signed-graph-and-joint-descent/ARBITRARY_GRAPH_SECTORS.md .
