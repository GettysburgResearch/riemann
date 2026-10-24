# An A+B bound for a sextic row moment with coefficient μγ₂

24 October 2026. Proposed source-dependent theorem, submitted for
independent review. This note uses the pinned sextic large sieve and the
ordinary Hecke functional equation. It does not use a zero-free
hypothesis. It does not prove the corresponding statement with
coefficient μd₆γ₂, and it does not assert a new global zero-free boundary.

## 1. Exact inputs, conventions, and statement

The arithmetic source is `openai/math` at
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`,
`preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`.
Its byte-exact local source is `arithmetic_lane/ope26a_source.tex`, SHA256
`42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`.
The imported statements are `lem:sextic-large-sieve`,
`lem:fixed-gauss-phase`, the primitive Hecke functional equation and its
fixed-angular version, and the natural-reflection identities
`old-eq:2.1a`--`old-eq:2.1d`. The source's finite-seminorm smooth calculus
is used to separate common profiles and to take logarithmic scale
suprema. These are source premises, not an independent certification of
the source's global claims.

For the fixed-angular Hecke equation and smooth duality, additionally
use the same commit's
`preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/build/sections/angular.tex`,
SHA256
`f14a7c1c4f0b19b70d6705c8a2adcb658bfbc77814edb61cd57edb2465f38510`,
Git blob `e93fbddf626ab532b7e8fbfac830f1b45370b0e3`.
The precise inputs are `lem:angular-hecke`,
`eq:angular-hecke-fe`, and the subsection on smooth duality. These are
the ordinary fixed-infinity Hecke equation and its test-profile
consequence. A finite sextic twist changes its finite conductor and
root number, but not this fixed-angular gamma quotient. This use does
not transfer a cubic metaplectic functional equation to sextic data.

Let O=Z[ω], λ=√−3, and use the unique primary generator congruent to 1
modulo 3 for every ideal prime to 3. All ideal columns are outside a fixed
finite set S containing the primes above 6 and every fixed conductor
prime. Element rows need not be squarefree or prime to S. All residue
symbols keep their original zero values at nonunits, even when a local
exponent is divisible by six.

In this note the additive character and plane measure are exactly

\[
 e_0(z)=\exp(2\pi i\operatorname{Tr}(z/\lambda)),\qquad
 d\mu(z)=\frac2{\sqrt3}\,dx\,dy,
 \qquad
 \widehat W(y)=\int_{\mathbb C}W(z)e_0(-zy)d\mu(z).
 \tag{1}
\]

The lattice O is self-dual. In particular the primary-coset Poisson
formula below contains 3, not 3λ, in its Fourier argument. The cubic
first-moment paper uses a different additive normalization; its Gauss
symbol is not silently substituted here.

Write χ_c for the sextic symbol, and

\[
 \gamma_j(c)=(Nc)^{-1/2}\sum_{x\bmod c}\chi_c(x)^j e_0(x/c),
 \qquad \alpha(c)=c/|c|,
\]

for squarefree good c. The source proves

\[
 \gamma_1(c)\gamma_2(c)=\mu(c)\alpha(c)G(c),\qquad
 G(vw)=G(v)G(w)\mathcal R(v,w),
 \tag{2}
\]

where G is a fixed finite-ray function of modulus one and R is a
symmetric sign-valued fixed-ray bicharacter, defined also on noncoprime
pairs. Moreover

\[
 \chi_b(a)=\mathcal R(a,b)\chi_a(b)\quad((a,b)=1),\qquad
 \mathcal R(c,c)=\chi_c(-1).
 \tag{3}
\]

Fix a unitary completely multiplicative coefficient
θ(c)=α(c)^ℓν(c), where the finite ray character ν and the integer ℓ are
fixed. Equivalently one may take a fixed finite linear combination of
such coefficients of one angular type. Let W be a nonnegative smooth
radial plane weight of fixed annular support, and let V be a smooth
norm-annular weight. Define, for A,B≥1,

\[
 J_{6,\theta}(A,B)=\frac1B
 \sum_{a\equiv1\ (3)}W(a/\sqrt A)
 \left|\sum_b\mu(b)\theta(b)\gamma_2(b)
                      V(Nb/B)\chi_b(a)\right|^2.
 \tag{4}
\]

The columns are squarefree because of μ; the primary rows are
unrestricted. The equivalent central normalization 1/√Nb follows by
replacing the fixed profile V(y) by y^(−1/2)V(y).

**Theorem.** If ℓ+1≠0, then, for every ε>0,

\[
 \boxed{J_{6,\theta}(A,B)\ll_{S,\theta,V,W,\epsilon}
                       (AB)^\epsilon(A+B).}
 \tag{5}
\]

The assertion is uniform on bounded smooth test families and under a
fixed number of their logarithmic scale derivatives. A norm twist in
V is allowed with a fixed polynomial cost in its height. The arithmetic
finite-ray data in θ are fixed; no unpriced moving conductor is part of
this statement. Nonzero angular type ℓ+1 is used at the ordinary
functional equation in Section 3. No statement at ℓ=−1 follows from this
proof.

## 2. An all-row ordinary large-sieve estimate

We first record exactly the unrestricted indices needed after Poisson.
For any fixed divisor bound |b_n|≪ε(Nn)^ε, the source squarefree sextic
sieve implies

\[
 \sum_{\substack{k\ {\rm sf}\\Nk\asymp K}}
 \left|\sum_{Nn\asymp N} b_n\chi_n(k)^{\pm1}\right|^2
 \ll (KN)^\epsilon N\{K+N+(KN)^{2/3}\}.
 \tag{6}
\]

Here n is unrestricted, and its coefficients may include any common
zero mask or fixed unit-modulus phase. To prove (6), write n=sv
uniquely, where s is squarefree, v is powerful, and (s,v)=1: the primes
of s are precisely those of valuation one in n. In a dyad Nv≈T there
are Oε(T^(1/2+ε)) possible v. For each fixed v the factor χ_v(k) is a
bounded row scalar, and the s-polynomial is a legitimate common
coefficient vector in the squarefree sieve. Its squared coefficient
norm is Oε(N^ε N/T), with the divisor exponent chosen arbitrarily
small before the final displayed ε. This retains the dependence on v
also when the remaining s length is bounded. Minkowski followed by the powerful count gives

\[
 (KN)^\epsilon N\{K+N/T+(KN/T)^{2/3}\}
\]

for that dyad. Summation over the logarithmically many T proves (6).
The condition (s,v)=1 is left in that common coefficient vector.

Next write an arbitrary row k=uv with u squarefree, v powerful, and
(u,v)=1. For a fixed v with Nv≈T, use (6) at row length K/T, with
b_nχ_n(v) in place of b_n; the restriction (u,v)=1 only decreases its
positive row sum. Sum over the Oε(T^(1/2+ε)) choices of v. For centrally
normalized polynomials this gives

\[
 \sum_{Nk\asymp K}
 \left|N^{-1/2}\sum_{Nn\asymp N}b_n\chi_n(k)^{\pm1}\right|^2
 \ll (KN)^\epsilon
       \{K+N\sqrt K+(KN)^{2/3}\}.
 \tag{7}
\]

Indeed the three contributions on the T dyad are
K/√T, N√T, and (KN)^(2/3)T^(−1/6), respectively. This proves (7) with
all good primary rows, not merely squarefree rows. A bounded row weight
or a restriction of the row set is allowed.

For arbitrary nonzero element rows, separate their unit and S-supported
parts. The unit and valuations modulo six produce a fixed finite
character family on good columns. For each S-supported part of norm Q
the good row width is K/Q. The final estimate K√F in the next section
sums with the convergent mass Σ_Q Q^(−1). Thus that estimate applies to
all nonzero lattice rows, including every nonsquarefree and ramified
frequency. This passage does not delete a row zero or change a
six-divisible power to the constant one.

## 3. One full ordinary factor and its squarefree restriction

Let f be squarefree, F=Nf, and let v be any fixed element whose good
prime support is contained in f. At every prime of f keep any specified
original zero, whether the local phase is nontrivial or redundant. Let
ζ be a fixed unitary finite-ray/angular character of nonzero angular
order r. Set

\[
 T_k(X)=X^{-1/2}\sum_n\psi_k^0(n)U(Nn/X),\qquad
 \psi_k^0(n)=\zeta(n)\overline{\chi_n(vk)}1_{(n,f)=1}.
 \tag{8}
\]

The variable k lies in a common norm dyad K≥1. Its complete natural
presentation has primitive conductor norm Q_k and redundant natural
radical R_(0,k). Tameness at the good primes, with the fixed bad data
absorbed into the constant, gives

\[
 Q_k N R_{0,k}\ll K F.
 \tag{9}
\]

This is a union bound: a good prime is counted once, either in the
primitive conductor or as a redundant natural zero. A canceled phase
does not remove its prime from the presentation. The powers occurring
in v are immaterial to (9), since they are reduced modulo six on units
and their original zeros remain. Nonzero r guarantees that the
primitive inducing character is never principal.

The natural functional equation gives a sum of conjugate natural
polynomials at scales

\[
 Y=\frac{C_k Nd}{X Nh},\qquad
 d\mid R_{0,k},\quad \operatorname{rad}(h)\mid R_{0,k},
 \qquad Y\ll KF/X,
 \tag{10}
\]

with coefficient
ε_k μ(d)ψ_k^*(d) overline(ψ_k^*(h))/√(Nd Nh). Its total absolute mass
is bounded by

\[
 \prod_{p\mid R_{0,k}}
 \frac{1+(Np)^{-1/2}}{1-(Np)^{-1/2}}
 \ll_\epsilon(KF)^\epsilon.
 \tag{11}
\]

The dual coefficient is exactly overline(ψ_k^0(n)), including the
unchanged natural zeros. It therefore has a common coefficient
overline(ζ(n))χ_n(v)1_(n,f)=1 multiplying χ_n(k), and can be used in
(7). Root numbers, the eligibility of d,h, and conductor phases are
bounded row scalars outside that polynomial.

For completeness, one may apply rowwise weighted Cauchy in (10), then
bound every resulting scale by a common logarithmic scale supremum.
The source smooth calculus bounds this supremum by integrals of the
same polynomial and its scale derivative. The transformed profile is
bounded at zero and rapidly decreasing at infinity, with the same
property for the required derivatives. Its lower annuli have central
normalization coefficients O(2^(−j/2)); its upper annuli have arbitrary
decay. Retained upper scales can be restricted to
(KF/X)(KFX)^ε, with an arbitrarily small power enlargement; scales
below one either are empty for the original annular profile or have
rapid decay for the transformed profile. Thus reflection and (7)
give, in addition to the direct bound, the same bound with X replaced
by max(1,KF/X), up to (KFX)^ε. If KF/X<1 the reflected sum is bounded
by Oε((KFX)^ε K), and may be made smaller by using its tail decay.
All profiles and their derivatives are common to the row mean. No
row-dependent coefficient vector is placed inside the sieve.

Taking the better of the direct and reflected estimates, the effective
column length is at most √(KF), or a fixed bounded scale. Since F≥1,

\[
 \sum_{Nk\asymp K}|T_k(X)|^2
 \ll (KFX)^\epsilon
       \{K+K\sqrt F+K F^{1/3}\}
 \ll (KFX)^\epsilon K\sqrt F.
 \tag{12}
\]

This bound holds for every positive nonempty annular scale X. It is a
one-full-factor assertion. It is not a bound for an arbitrary
divisor-bounded coefficient after reflection: the full multiplicative
character is essential to (10).

### Additional common punctures

Let l be any common squarefree puncture, L=Nl. It need not be included
in F. Exact multiplicativity gives

\[
 X^{-1/2}\sum_{(n,l)=1}\psi_k^0(n)U(Nn/X)
 =\sum_{e\mid l}\frac{\mu(e)\psi_k^0(e)}{\sqrt{Ne}}
                      T_k(X/Ne).
 \tag{13}
\]

There is no new condition (n,e)=1 on the quotient column. The
row-dependent multiplier ψ_k^0(e) has modulus at most one. The sum of
the absolute external coefficients is at most L^ε. Consequently
Minkowski and (12) prove the same estimate with this additional mask,
at cost (KFLX)^ε. Counting L inside the conductor budget instead
would incur an unnecessary √L loss and would not close the later
divisor sum.

### Squarefree ordinary columns

Insert the exact identity μ²(n)=Σ_(d²|n) μ(d). Then

\[
 X^{-1/2}\sum_{(n,l)=1}\mu^2(n)\psi_k^0(n)U(Nn/X)
 =\sum_{(d,l)=1}\frac{\mu(d)\psi_k^0(d^2)}{Nd}
 \left(\frac{X}{(Nd)^2}\right)^{-1/2}
 \sum_{(b,l)=1}\psi_k^0(b)
             U\!\left(\frac{Nb}{X/(Nd)^2}\right).
 \tag{14}
\]

The d sum is supported on Nd≪√X, and Σ_(Nd≪√X)1/Nd≪1+log(2X).
There is no condition (b,d)=1. Again ψ_k^0(d²) is only a bounded row
scalar. Weighted Minkowski, (12), and (13) therefore show that

\[
 \mathcal O_{v,f,l}(K,X):=
 \sum_{Nk\asymp K}
 \left|\sum_{(n,fl)=1}
       \frac{\mu^2(n)\zeta(n)}{\sqrt{Nn}}
       \overline{\chi_n(vk)}U(Nn/X)\right|^2
 \ll (KFLX)^\epsilon K\sqrt F.
 \tag{15}
\]

Here the fixed profile can absorb the factor y^(−1/2) converting
normalizations. Formula (15) also holds with a bounded row restriction,
including (k,l)=1, and for all nonzero lattice k as explained after
(7). All fixed finite-ray expansions with the same nonzero angular
order are permitted. This is the precise ordinary input used below.

## 4. Exact sextic Poisson and the phase cancellation

Write c_b=μ(b)θ(b)γ₂(b)V(Nb/B). The genuine pair diagonal in (4) is

\[
 \mathcal D=\frac1B\sum_b|c_b|^2
      \sum_{\substack{a\equiv1\ (3)\\(a,b)=1}}W(a/\sqrt A)
 \ll A(AB)^\epsilon.
 \tag{16}
\]

For an unequal pair put b_i=fp_i, with f,p₁,p₂ squarefree,
(p₁,p₂)=1, and (f,p₁p₂)=1. Remove the common row zero by

\[
 1_{(a,f)=1}=\sum_{m\mid f}\mu(m)1_{m\mid a},
 \qquad F=Nf,\quad M=Nm.
 \tag{17}
\]

The primary substitution a=mx preserves the primary coset. Radial W
makes the rotation by m harmless. For q=p₁p₂, write x=q+3s. The
period-q character is ψ(x)=χ_(p₁)(x) overline(χ_(p₂)(x)). Its finite
Fourier sum is primitive when q≠1. CRT and (3) give

\[
 \frac{\tau(\psi)}{\sqrt{Nq}}=
 \overline{\mathcal R(p_1,p_2)}\chi_{p_2}(-1)
                  \gamma_1(p_1)\overline{\gamma_1(p_2)}.
 \tag{18}
\]

The identity γ_(−1)(p)=χ_p(−1) overline(γ₁(p)) accounts for the
second factor; it cannot be dropped. The primary shift and ψ(3) give
the fixed finite-ray pair phase

\[
 \rho(p_1,p_2)=\overline{\mathcal R(p_1,p_2)}\chi_{p_2}(-1)
                    \chi_{p_1}(3)\overline{\chi_{p_2}(3)}.
 \tag{19}
\]

The additive factor is e₀(k/3). The exact Fourier argument is
k√A/(3√M p₁p₂), and its Jacobian supplies A/(9M). These claims can
also be checked directly by Fourier transforming
s↦W((q+3s)√(M/A)) with convention (1).

Gauss multiplicativity gives

\[
 \gamma_2(fp)=\gamma_2(f)\gamma_2(p)\chi_p(f)^{-2}.
 \tag{20}
\]

Now use (2) on each remaining column:

\[
 \mu(p)\theta(p)\gamma_2(p)\gamma_1(p)
      =\mu^2(p)\theta_1(p),\qquad
 \theta_1(p)=\alpha(p)G(p)\theta(p).
 \tag{21}
\]

This is the coefficient-level cancellation. The ordinary surviving
angular order is ℓ+1. The factor from (20), combined with the m
substitution and the finite Fourier character, leaves

\[
 \overline{\chi_{p_1}(vk)}\chi_{p_2}(vk),\qquad
 v=f^2/m \quad\hbox{on the actual coprime support}.
 \tag{22}
\]

For an integral presentation one may use v=f²m⁵. These have the same
sextic phase and zero support in every column under consideration.
In particular the moving good support of v is contained in f.

Put s(n)=μ²(n). With the prime on the pair sum indicating all the
coprimalities just stated and exclusion of p₁=p₂=1, the exact
nonzero-frequency expression is

\[
\begin{split}
 J_{6,\theta}-\mathcal D
 ={}&\frac A{9B}\sum_f\sum_{m\mid f}\frac{\mu(m)}M
 \sum_{p_1,p_2}^{\prime}
 \frac{s(p_1)\theta_1(p_1)
       \overline{s(p_2)\theta_1(p_2)}}{\sqrt{Np_1Np_2}}
 \rho(p_1,p_2)\\
 &\quad\times V(FNp_1/B)\overline{V(FNp_2/B)}
 \sum_{k\ne0}e_0(k/3)
 \widehat W\!\left(\frac{k\sqrt A}{3\sqrt M\,p_1p_2}\right)
       \overline{\chi_{p_1}(vk)}\chi_{p_2}(vk).
\end{split}                                                    \tag{23}
\]

Because θ is unitary and f is squarefree and good,
|μ(f)θ(f)γ₂(f)|²=1; this is why there is no missing f weight in
(23). Fixed finite linear combinations follow by Cauchy from the
single-character statement. For every genuine unequal pair the
period-q character is nonprincipal, so its zero-frequency term is
zero. Every nonzero lattice frequency remains in (23). In particular
cube or sixth-power frequencies have not been discarded.

## 5. Exact l inversion and all moving masks

Extend the displayed nonzero-frequency summand formally to all
squarefree p₁,p₂ coprime to f. Enforce (p₁,p₂)=1 with
Σ_(l|(p₁,p₂))μ(l), and put p_i=ln_i, L=Nl. This is an algebraic
extension followed by exact coprimality inversion. It is not an
application of a primitive Gauss formula to an overlapping pair.

The surviving masks include (f,l)=1, (n_i,fl)=1. The common row mask is

\[
 |\chi_l(vk)|^2=1_{(k,l)=1},
 \tag{24}
\]

because (v,l)=1. Crucially, this step adds no l to the phase v.
Indeed, by (2),

\[
 \theta_1(ln)=\theta_1(l)\theta_1(n)\mathcal R(l,n),
\]

and (19) gives

\[
 \rho(ln_1,ln_2)
 =\mathcal R(l,n_1)\mathcal R(l,n_2)\rho(n_1,n_2).
 \tag{25}
\]

The otherwise constant factor is
R(l,l)χ_l(−1)=1. The two R factors in (25) cancel those from the two
θ₁ columns, and |θ₁(l)|²=1. The external weight is therefore exactly

\[
 \frac A{9B}\frac{\mu(m)\mu(l)}{ML},
 \tag{26}
\]

with the row mask (24). Before common profile separation the kernel is

\[
 \widehat W\!\left(
           \frac{k\sqrt A}{3\sqrt M\,l^2n_1n_2}\right).
 \tag{27}
\]

After the separation, the ordinary normalized column has the form

\[
 \sum_{(n,fl)=1}\frac{\mu^2(n)\theta_1(n)}{\sqrt{Nn}}
              \overline{\chi_n(vk)}U(Nn/Y_{fl}),
 \qquad Y_{fl}=\frac B{FL}.
 \tag{28}
\]

The finite pair function ρ(n₁,n₂) in (19) is retained: expand it in a
fixed finite sum of products of finite ray characters, and similarly
expand G in θ₁. Each resulting bilinear pair is bounded by Cauchy using
two moments of type (28). Both retain the angular order ℓ+1. Nothing
here asserts that ρ is positive or that it can be omitted from the
identity.

Define

\[
 K_0=\frac{B^2}A,\qquad K_{fm}=K_0\frac M{F^2}.
 \tag{29}
\]

For a frequency norm dyad Nk≈K, the common separated profiles have
arbitrary decay (1+K/K_(fm))^(−R). Smooth Mellin separation of the two
column norms and the radial transform in (27), with sufficiently many
fixed seminorms, gives a common rapidly decreasing Mellin majorant.
Thus (15) applies uniformly to every separated profile, with F the
phase support and l only an extra puncture. Taking absolute values
and Cauchy is first used for a bound at this point; the signed phases
and all zero masks were retained in (23)--(28).

### The artificial unit pair

The formal extension adds p₁=p₂=1, which must be subtracted exactly.
Its nonzero-frequency contribution is

\[
 U_0=\frac A{9B}\sum_{f\ {\rm sf}}|V(F/B)|^2
       \sum_{m\mid f}\frac{\mu(m)}M
       \sum_{k\ne0}e_0(k/3)
           \widehat W\!\left(\frac{k\sqrt A}{3\sqrt M}\right).
 \tag{30}
\]

For every positive M/A, Schwartz decay and nonzero-lattice counting
bound the absolute frequency sum by O(M/A); this also holds when
M/A<1, by taking a sufficiently strong tail. Since F≈B in (30),

\[
 |U_0|\ll B^{-1}\sum_{F\asymp B}\tau(f)
                 \ll B^\epsilon.
 \tag{31}
\]

This is separate from the genuine diagonal (16). No artificial
zero-frequency unit term is added to (23).

## 6. Sum every divisor and frequency block

Apply (15) to (28), retaining the bounded row mask (24). For K≥1 the
result is (ABK)^ε K√F. Its common frequency tail sums to

\[
 \sum_{K\ge1\ {\rm dyadic}}
 K(1+K/K_{fm})^{-R}\ll_R K_{fm}
 \tag{32}
\]

for every K_(fm)>0. For K_(fm)≥1 this is dyadic counting; for
K_(fm)<1 it follows from the same rapid decay. Choosing R after the
small power losses gives the identical conclusion with those losses
absorbed in (AB)^ε. In particular a subunit nominal row width is not
replaced by a spurious constant row count.

The positive majorant for all nonzero-frequency blocks is at most

\[
\begin{split}
 &(AB)^\epsilon\frac AB
     \sum_{f}\sum_{m\mid f}\sum_{l}
            \frac{K_{fm}\sqrt F}{ML}\\
 &\hspace{1cm}=(AB)^\epsilon B
       \sum_f\frac{\tau(f)}{F^{3/2}}
       \sum_{L\ll B/F}\frac1L
 \ll (AB)^\epsilon B.
\end{split}                                                   \tag{33}
\]

The omitted coprimalities only decrease this positive bound. The f
sum converges with any sufficiently small divisor loss; the l sum is
logarithmic over ideals. The finite-ray expansions, fixed-prime and
unit decompositions, and common Mellin integrals only cost the stated
arbitrarily small power. All column ranges that are empty by the
annular support contribute zero.

Combining (16), (31), and (33) proves (5). This completes the whole
f,m,l sum and all frequency powers; it does not bound only the
common-divisor-free block.

## 7. The signed sixth-moment orientation and its limit

The sixth-dual form in the frozen fourth-pass
`SIXTH_MOMENT_ROOT_NUMBER_REDUCTION.md` (SHA256
`071bf3c7f9d6ec109e92e016f8fbeb8dd0ad75356e538ebb39316eee7ee1c10f`)
contains, on its generic squarefree column part in the principal
squarefree-row sieve branch d=1,

\[
 U\sum_n\frac{d_6(n)}{Nn}\,
       \mu(n)G(n)\alpha(n)^{-1}\overline{\gamma_2(n)}
 \sum_h\overline{\chi_n(h)}\alpha(h)^2
               \mathcal H_2\Phi(Nh\,U/Nn).
 \tag{34}
\]

The whole conjugate has the positive sextic orientation of (4), with
θ(n)=α(n)overline(G(n)) and row angular weight α(h)^(−2). Its
ordinary angular type after (21) is two. This is inside the angular
scope of (5), but the coefficient d₆(n) in (34) is not inside its
coefficient scope.

For a single linear row sum, Poisson has period n, rather than the
pair period n₁n₂. With H=Nn/U, the angular Fourier identity gives

\[
 \sum_h\chi_n(h)\alpha(h)^{-2}\Phi(Nh/H)
 =\frac H{\sqrt{Nn}}\gamma_1(n)\alpha(n)^{-2}
     \sum_{u\ne0}\overline{\chi_n(u)}\alpha(u)^2
                  \mathcal H_2\Phi(HNu/Nn),
 \tag{35}
\]

where a fixed field phase is included in the definition of the angular
Hankel transform. This is the full lattice formula; there is no
primary-coset factor nine. Multiplying its column factors gives

\[
 \mu(n)\gamma_2(n)\,[\alpha(n)\overline{G(n)}]
                    \gamma_1(n)\alpha(n)^{-2}=\mu^2(n).
 \tag{36}
\]

The new row length is Nn/H=U. With the paired smooth kernels this
is the inverse Fourier operation returning that original signed AFE
branch. The full squarefree-row sieve is recovered only by applying
the same inverse operation term by term to every d branch, with its
original outside scalar and zero masks. It is an exact orientation
check, not an additional cancellation estimate.

Even a hypothetical extension of (5) to d₆ would not alone supply the
desired signed sixth-moment bound. At H=U² and B=U³, the direct Cauchy
cost of (34) is

\[
 \frac U{\sqrt B}\sqrt H\sqrt{J_6(H,B)}.
 \tag{37}
\]

The bound J₆≪H+B would give U². Even a row-volume bound J₆≪H would
give U^(3/2). Neither meets the proposed small-loss sixth-moment
consumer. Further cancellation must preserve the coherent signed
angular form, or use more of its factor structure.

There are two other precise scope exclusions. The original raw sextic
inverse has coefficient μ before Poisson, so its post-Poisson Gauss
column lacks the μ factor required in (21). It is not (4). Also the
conjugate coefficient obtained from the single-numerator functional
equation has θ=α^(−1)overline(G); its ordinary angular order is zero,
so the nonprincipal reflection argument in Section 3 does not apply.
Neither family is converted into a proof of a new zero-free boundary
by (5).

For general fixed j, the ordinary coefficient left by replacing μ in
(4) with μd_j is μ²d_j. Its leading Euler decomposition contains j
full factors. The one-full-factor reflection in Section 3 is not a
bound for that product. Establishing such a bound, and then paying the
signed consumer (37), are distinct remaining questions.
