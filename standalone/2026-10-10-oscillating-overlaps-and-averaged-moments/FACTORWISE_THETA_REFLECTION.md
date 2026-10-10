# Factorwise theta reflection: exact Gauss cancellation and a reciprocal angular Hecke L-factor

Status: proposed research mathematics. The identities below are proved deductions from the explicitly pinned October 5 theta-reflection formula. They preserve an individual factor of a balanced divisor column, including its scalar phase. The fixed-frequency quadratic estimate is also proved from the imported quadratic large sieve. The required coupled-frequency mean square, the desired fourth moment, and the generalized diagonal-size moments remain unproved.

Scope: K = Q(sqrt(-3)), O = Z[omega], lambda = 1 + 2 omega, N(z) = |z|^2. All ideal-indexed variables use the source's multiplicative primary generators. The fixed set S contains the primes above 2 and 3 and the conductors of the fixed finite-order twists. The general transformation below allows every primary row k prime to S, including nonsquarefree k and positive multiples of six in its prime valuations. Its clean quadratic-on-both-axes specialization and the large-sieve proposition explicitly restrict k to squarefree rows. No claim is made here that this squarefree specialization alone controls the full original row family.

Exact imported source: OpenAI, October 5 manuscript, paper2.tex at commit adc7f1241b42e322a6451854ab7e4b4c146bf78a, imported in standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex. The load-bearing interfaces are eq:crt-a (line 850), eq:T (1288), eq:completed-twist (1305), eq:theta-local-factors (1736), eq:theta-weight (1755), eq:reflection (1809), lem:theta-bounds (1859), eq:Q (1892), and the full scalar calculation in eq:ray-multiplier, eq:ray-additive-crt, eq:ray-local-transform, and the displayed scalar C (3179–3426). The proof below uses those exact normalizations; it does not independently re-prove the automorphy theorem behind eq:reflection.

What is new here: the outer factor's normalized cubic Gauss sum cancels the reflected j = 4 Gauss phase exactly. After retaining the phase formerly bounded only by its modulus, the surviving outer coefficient is a quadratic row character times an angular Hecke character and an ideal Ramanujan sum. For each fixed reflected frequency, its Dirichlet series is an explicit finite Euler correction times the reciprocal of a Hecke L-function of infinity type -3.

## 1. A completion that retains the outer factor

Write

\[
a_\xi(n)=\overline{\alpha(n)}\gamma_2(n)\xi(n),\qquad
\alpha(n)=n/|n|,
\]

for squarefree n prime to S. Fix smooth compactly supported W_1 and W_2 on positive norm intervals, and let T(B;k,a) be the source's completed sum with test W_2 and auxiliary factor a. Define

\[
\mathcal C_2(A,B;k)=
\frac1{\sqrt A}\sum_{\substack{a\ {\rm squarefree}\\(a,S)=1}}
a_\xi(a)\chi_a(k)W_1(Na/A)\,T(B;k,a).
\tag{1.1}
\]

Only the outer a is squarefree by definition here; the theta-completion cube index is unrestricted. Every term with (a,k) nontrivial is zero. The cube-index-one part of (1.1) is exactly

\[
\mathcal P_2(A,B;k)=
\frac1{\sqrt{AB}}
\sum_{\substack{ab\ {\rm squarefree}\\(ab,S)=1}}
a_\xi(ab)\chi_{ab}(k)W_1(Na/A)W_2(Nb/B).
\tag{1.2}
\]

Indeed, the source identity

\[
a_\xi(ab)=a_\xi(a)a_\xi(b)\chi_b(a)^4
\]

includes the cross-factor phase needed in T(B;k,a). The zero of that cross factor enforces (a,b)=1.

There is also an exact one-axis cube inversion. Let a superscript (h) on either C_2 or P_2 impose the additional outer restriction (a,h)=1, and put

\[
\vartheta_k(h)=\overline{\alpha(h)}^3\xi(h)^3\chi_h(k)^3.
\]

Then

\[
\mathcal P_2(A,B;k)=
\sum_{\substack{h\ {\rm primary}\\(h,S)=1}}
\frac{\mu(h)\vartheta_k(h)}{Nh}\,
\mathcal C_2^{(h)}(A,B/(Nh)^3;k).
\tag{1.3}
\]

This sum is finite on the supports of the tests. To prove it, expand the cube index b in the definition of T. Its extra twist at a is chi_b(a)^12, exactly the indicator (a,b)=1, including its zero on nonunits. The normalized cube coefficient is vartheta_k(b)/Nb. After substituting this expansion in the right side of (1.3), combine h and b into c = hb. Complete multiplicativity leaves the coefficient sum over h | c of mu(h), while the two outer exclusions combine to (a,c)=1. Only c = 1 survives. This is an algebraic inversion; estimating its tails remains a separate task.

## 2. Retain the exact scalar before taking any norm

First let k be any primary row prime to S. For p | k write j_p = v_p(k) mod 6, with j_p in {0,...,5}. The local character with j_p = 0 is still extended by zero at multiples of p. It is not an absent prime.

Let R be an active subset of the prime support of k:

\[
\{p\mid k:j_p\ne0\}\ \subseteq R\ \subseteq\{p:p\mid k\},
\qquad r=\prod_{p\in R}p.
\tag{2.1}
\]

For a nonzero outer summand, a is squarefree and coprime to kS. Every prime of a has local exponent 4 and is active. Thus the denominator in the source reflection has the exact form

\[
c=c_0ra.
\tag{2.2}
\]

The fixed element c_0 is supported on S. Its unit choice is retained, not replaced by its norm.

Here is the finite-ray bookkeeping required as a varies. Reciprocity writes the inner twist as

\[
\Psi_{k,a}(n)=\Psi_{0,[k]}(n)
\prod_{p\mid k}\chi_p^{j_p}(n)\prod_{p\mid a}\chi_p^4(n),
\]

where the finite-order character Psi_{0,[k]} depends on k only through a fixed ray class. In the source's construction, fix h_0 modulo its fixed L and put M = lambda^12 L^4. The active Fourier residues may be chosen congruent to zero modulo M^2. The cusp numerator modulo Mc_0, the reduced denominator's unit, the cusp index, the S-part of the Kubota multiplier, and the additive character then depend only on h_0 and ra modulo M^2. This follows directly from the displayed numerator formula in the source's reduced-denominator calculation. In particular the dependency does not require holding the individual primes of a fixed.

Consequently, after partitioning k, r, and a into finitely many fixed ray classes, the data

\[
(c_0,d,\psi,\widehat\phi(h_0),\kappa_0)
\tag{2.3}
\]

are fixed on each component. Here d is one of the three exact cusp coefficient sequences d_0, d_+, d_-, psi is the source's additive character, and |kappa_0| = 1. Below, h denotes such a finite component, including its outer ray restriction. No scalar in (2.3) is discarded.

For p | r define the row-only quantities in O/(p)

\[
\sigma_p^0=\lambda^2c_0r/p,\qquad
\epsilon_p^0=-[\lambda^5(c_0r/p)^2]^{-1}.
\tag{2.4}
\]

Both are nonzero. For a general admissible denominator c define

\[
\begin{aligned}
\omega_{p,j}(c)
&=
\begin{cases}
\chi_p(-1)^j\gamma_j(p)\gamma_{j+2}(p)
 \chi_p(\epsilon_p(c))^{-j-2},&j\ne0,4,\\
\gamma_4(p),&j=4,\\
-\gamma_2(p)\chi_p(\epsilon_p(c))^{-2},&j=0\ {\rm active},
\end{cases}\\
\Xi_{p,j}(c)&=\chi_p(\lambda^2c/p)^{-2}\omega_{p,j}(c),\\
\epsilon_p(c)&=-[\lambda^5(c/p)^2]^{-1}.
\end{aligned}
\tag{2.5}
\]

These are precisely the source factors, with gamma indices reduced modulo six. Set

\[
\boxed{
Z_{h,R}(k)=
-\frac{i}{81}\,\overline{\alpha(c_0r)}^2\,
\widehat\phi(h_0)\overline{\kappa_0}
\prod_{\substack{p\mid k\\p\notin R}}(1-(Np)^{-1})
\prod_{p\in R}\Xi_{p,j_p}(c_0r).
}
\tag{2.6}
\]

Thus |Z_{h,R}(k)| <= 1/81 before any subsequent finite character expansion. Formula (2.6) retains the global factor -i/81, the unit and angular phase of c_0r, the ramified Fourier coefficient, the Kubota factor, and every inactive local density.

### Lemma 2.1: exact cancellation of the outer Gauss phase

Let C_h(k,a) be the source scalar for the denominator c_0ra and the chosen component. For every squarefree a coprime to kS in that component,

\[
\boxed{
a_\xi(a)\chi_a(k)\,C_h(k,a)
=Z_{h,R}(k)\,
\overline{\alpha(a)}^3\xi(a)
\chi_a(\lambda^2c_0)^4\chi_a(k)^3.
}
\tag{2.7}
\]

**Proof.** At a row prime p in R, multiplication of c by a multiplies sigma_p by a and epsilon_p by a^(-2). Inspection of each of the three cases of (2.5) gives

\[
\Xi_{p,j}(c_0ra)=
\Xi_{p,j}(c_0r)\chi_p(a)^{2j+2}.
\tag{2.8}
\]

For j = 4 the exponent is -2, which equals 2j+2 modulo six. For active j = 0 it is -2+4 = 2. Thus no exceptional case has been suppressed.

The product of the factors at primes dividing a is

\[
\begin{aligned}
\prod_{p\mid a}\chi_p(\lambda^2c_0ra/p)^{-2}\gamma_4(p)
&=\chi_a(\lambda^2c_0r)^4
\prod_{p\mid a}\chi_p(a/p)^{-2}\gamma_4(p)\\
&=\chi_a(\lambda^2c_0r)^4\gamma_4(a).
\end{aligned}
\tag{2.9}
\]

The last equality is the exact CRT Gauss identity

\[
\gamma_j(ab)=\gamma_j(a)\gamma_j(b)
\chi_a(b)^j\chi_b(a)^j\qquad((a,b)=1),
\]

with j = 4. In particular the cross-prime phases in (2.9) are necessary.

The conjugate Gauss identity for the primitive cubic character gives

\[
\gamma_2(a)\gamma_4(a)=\chi_a(-1)^2=1.
\tag{2.10}
\]

There is no residual Mobius sign: the cubic character takes value one at -1. The angular contribution from a_xi(a) and the factor bar-alpha(c_0ra)^2 is exactly bar-alpha(a)^3.

Finally, every exponent 2j+2 in (2.8) is even, so the sign in sextic reciprocity disappears:

\[
\chi_p(a)^{2j+2}=\chi_a(p)^{2j+2}.
\]

At each active row prime the total exponent of chi_a(p) is

\[
j_p+4+(2j_p+2)=3j_p+6\equiv3j_p\pmod6.
\tag{2.11}
\]

At an inactive prime j_p = 0 and (a,k)=1; it contributes no phase, while its exact scalar density remains in (2.6). Combining these statements proves (2.7). The original exclusion (a,k)=1 has been retained throughout. In particular a row prime whose valuation is a positive multiple of six never loses its zero convention. \(\square\)

For reference, the entire local transformation is:

| j | scalar exponent on a, modulo 6 | reflected B_{p,j}(x) | final outer exponent |
|---|---:|---|---:|
| 0 active | 2 | q^(-1/2) chi_p(x)^4 | 0, with the row mask |
| 1 | 4 | chi_p(x)^3 | 3 |
| 2 | 0 | chi_p(x)^2 | 0, with the row mask |
| 3 | 2 | chi_p(x) | 3 |
| 4 | 4 | q^(-1/2)(q 1_(p divides x) - 1) | 0, with the row mask |
| 5 | 0 | chi_p(x)^5 | 3 |

Here q = Np. The inactive j = 0 option instead contributes 1-q^(-1) in Z and no factor B.

## 3. The exact factorwise reflected formula

For squarefree a put

\[
c_a(x)=\sum_{d\mid(a,x)}Nd\,\mu(a/d),\qquad
R_a(x)=\frac{c_a(x)}{\sqrt{Na}}.
\tag{3.1}
\]

This is the ideal Ramanujan sum and its square-root normalization. Multiplicatively,

\[
R_a(x)=\prod_{p\mid a}(Np)^{-1/2}
\bigl(Np\,\mathbf1_{p\mid x}-1\bigr)
=\prod_{p\mid a}B_{p,4}(x).
\tag{3.2}
\]

For the fixed test W_2, put V_*(y)=sqrt(y) W_2(y), and retain the exact transformed test

\[
V_*^\sharp(y)=\frac1{2\pi i}\int_{(0)}
\widehat V_*(-t)
\frac{\Gamma(7/6+t)\Gamma(5/6+t)}
{\Gamma(7/6-t)\Gamma(5/6-t)}
\left(\frac{(2\pi)^4y}{27}\right)^{-t}\,dt.
\tag{3.3}
\]

Write x = lambda^4 ell, so x is integral and N(x)=81 N(ell). Applying the source reflection separately for each a, followed by Lemma 2.1, gives the following exact identity:

\[
\begin{aligned}
\mathcal C_2(A,B;k)
={}&\frac1{\sqrt A}\sum_R\sum_h Z_{h,R}(k)
\sum_{0\ne\ell\in\lambda^{-4}O}
\frac{d_h(\ell)\alpha(\ell)}{\sqrt{N\ell}}\,
\psi_h(x)\prod_{p\in R}B_{p,j_p}(x)\\
&\quad\times
\sum_{\substack{a\ {\rm squarefree}\\(a,kS)=1\\a\ {\rm in\ the\ ray\ class}\ h}}
\overline{\alpha(a)}^3\xi(a)\chi_a(\lambda^2c_{0,h})^4
\chi_a(k)^3W_1(Na/A)R_a(x)\\
&\qquad\qquad\times
V_*^\sharp\left(
\frac{N\ell\,B}{N(c_{0,h})^2\,N(r)^2\,N(a)^2}
\right).
\end{aligned}
\tag{3.4}
\]

The notation h also fixes the required row and active-product ray classes, as described in Section 2. Thus d_h, psi_h, and c_{0,h} come from a finite fixed list. Zero coefficients may be inserted for inapplicable components. All inactive choices R are actually summed.

Every outer a sum is finite. The reflected frequency sums converge absolutely for fixed scales and row, by the source's coefficient support and rapid large-argument decay of V_*^sharp. Thus summing the source identities and changing these orders is legitimate. Formula (3.4), rather than a bound on its summands, is the main result.

When k is squarefree, R is uniquely the prime support of k, r=k, and

\[
\prod_{p\mid k}B_{p,1}(x)=\chi_k(x)^3.
\tag{3.5}
\]

After expanding the outer ray indicator in finite ray characters and using quadratic reciprocity, each component's a- and x-dependent row phase can therefore be written

\[
\overline{\alpha(a)}^3\rho_h(a)\,\chi_k(ax)^3.
\tag{3.6}
\]

The finite-order character rho_h includes xi, chi_a(lambda^2 c_0)^4, the chosen ray character, and the fixed-row-class reciprocity sign. Each is supported at S, after one fixed enlargement of the modulus. Finite expansion coefficients are placed in Z. Equation (3.6) does not discard either zero: it vanishes when (k,ax) is nontrivial.

For nonsquarefree k, the a-dependent character is still quadratic, but the x-dependent product in (3.4) is generally not quadratic. The table in Section 2 states the exact surviving local factors. Thus the squarefree-row simplification (3.5) cannot be asserted for the general family.

## 4. The outer Dirichlet series is an inverse angular L-function

Fix one genuine finite-character component from the preceding ray expansion, a row k, and x != 0. Define the imprimitive Hecke character

\[
\tau_k(a)=\overline{\alpha(a)}^3\rho(a)\chi_a(k)^3
\]

away from kS, and set it to zero on ideals divisible by a prime of kS. If reciprocity has been used to put the character in denominator-k form, its finite ray sign is included in rho. Let

\[
L_{\tau_k}^{S}(w)=\prod_{p\notin S}
\left(1-\frac{\tau_k(p)}{(Np)^w}\right)^{-1}.
\tag{4.1}
\]

Its displayed zero values already omit the primes of k. Then, for Re w > 1,

\[
\boxed{
\sum_{\substack{a\ {\rm squarefree}\\(a,S)=1}}
\frac{\tau_k(a)c_a(x)}{(Na)^w}
=\frac1{L_{\tau_k}^{S}(w)}
\prod_{\substack{p\mid x\\p\notin S}}
\frac{1+(Np-1)\tau_k(p)(Np)^{-w}}
{1-\tau_k(p)(Np)^{-w}}.
}
\tag{4.2}
\]

**Proof.** Absolute convergence holds because x is fixed. At a prime not dividing x, the squarefree local Ramanujan coefficient is -1, so its factor is 1-tau_k(p)(Np)^(-w). Multiplying these factors proves (4.2), with 1+(Np-1)tau_k(p)(Np)^(-w) at each prime dividing x. If p | k, then tau_k(p)=0 and the correction factor is exactly one. \(\square\)

This is a reciprocal, not a positive divisor series. When x has no prime divisor outside S, the finite correction is empty and the fiber is exactly 1/L_tau^S(w). The character bar-alpha^3 has nonzero infinity type -3 in the source's primary-generator convention. Multiplying it by any finite-order ray character leaves that infinity type unchanged. It is therefore outside the finite-order Hecke-character family asserted in the imported September 30 and October 5 zero-free theorems.

The classical meromorphic continuation of the right side of (4.2) is separate from its Euler-product proof on Re w > 1. In Re w > 0 its displayed finite denominators do not vanish, since |tau_k(p)| <= 1. Zeros of the angular L-function can nevertheless give poles of its reciprocal; in an individual fiber one cannot shift a contour through those poles by citing the finite-order 7/8 theorem. A subsequent sum over x might cancel them, but such cancellation is not established by (4.2).

There is a useful exact check on the Mellin exponents. Let s be the Mellin variable for the outer W_1 and let u be the original completed Dirichlet-series variable in eq:theta-mellin-functional-equation. The reflection contributes (Na)^(1-2u), and the Ramanujan normalization contributes (Na)^(-1/2). Hence the exponent in (4.2) is

\[
\boxed{w=s+2u-\tfrac12.}
\tag{4.3}
\]

Equivalently, using the reflected kernel variable t = 1/2-u from (3.3), it is w=s+1/2-2t. For a fixed frequency the Euler identity needs Re w>1. A sufficient initial region for absolute interchange of the outer Dirichlet series with the reflected coefficient series is Re u<0 and Re w>2: use |c_a(x)|<=Na and the source's absolute convergence of the dual theta series at 1-u. These domain statements do not assert joint continuation past angular-L poles.

## 5. The original factor length really is available to the quadratic sieve, frequency by frequency

This proposition records what the phase cancellation allows before recombining the dual frequencies. It does not estimate the recombined expression (3.4).

Fix a component of the squarefree-row formula, a nonzero x, and A,K>=1. Rows satisfy K<=Nk<=2K and lie in a fixed ray class. Let U_1 be supported in a fixed interval [a_0,a_1] contained in the positive reals. For z>0 put

\[
F_x(k)=
\sum_{\substack{a\ {\rm squarefree}\\(a,S)=1}}
\overline{\alpha(a)}^3\rho(a)\chi_k(a)^3 R_a(x)
U_1(Na/A)
V_*^\sharp\left(\frac{z}{(Na/A)^2(Nk/K)^2}\right).
\tag{5.1}
\]

For every epsilon>0 and M>0, with a sufficiently large fixed number of test derivatives,

\[
\boxed{
\sum_{\substack{K\le Nk\le2K\\k\ {\rm squarefree}}}|F_x(k)|^2
\ll (KA)^\epsilon(K+A)\,E_x(A)\,
\min(z^{1/4},z^{-M})^2,
}
\tag{5.2}
\]

where

\[
E_x(A)=
\sum_{\substack{a\ {\rm squarefree}\\(a,S)=1\\a_0A\le Na\le a_1A}}
|R_a(x)|^2.
\tag{5.3}
\]

The constants depend on the fixed supports, the required test norms, epsilon, M, and S; they do not depend on x. Fixed additional ray restrictions are permitted.

**Proof.** On the two compact ratio intervals, all derivatives of the two-variable test in (5.1) are bounded by a fixed multiple of min(z^(1/4),z^(-M)), using the source's theta-weight derivative estimate with sufficiently large decay exponent. Apply its smooth Fourier separation, retaining the rapid decay of the separation coefficients. Each separated k-factor has bounded modulus. Each a-coefficient has the original support Na comparable to A and squared norm bounded by a constant times E_x(A). Apply the imported quadratic sieve eq:Q on this original squarefree a range, followed by Minkowski for the absolutely convergent separation integral. No a-times-x product modulus is used in this fixed-frequency application. \(\square\)

The coefficient energy also has an exact arithmetic description. Write d = gcd(a,rad x) and a=de. Then

\[
c_a(x)=\mu(e)\varphi_K(d),\qquad
\varphi_K(d)=\prod_{p\mid d}(Np-1).
\]

Consequently

\[
\begin{aligned}
E_x(A)
={}&\sum_{\substack{d\mid{\rm rad}(x)\\(d,S)=1}}
\frac{\varphi_K(d)^2}{Nd}
\sum_{\substack{e\ {\rm squarefree}\\(e,dxS)=1\\
a_0A/Nd\le Ne\le a_1A/Nd}}\frac1{Ne}\\
\ll{}&
\sum_{\substack{d\mid{\rm rad}(x)\\(d,S)=1\\Nd\le a_1A}}Nd.
\end{aligned}
\tag{5.4}
\]

The inner annular harmonic sum is uniformly bounded, including its nonempty bounded-size ranges, by ideal counting. This proves the last inequality. If x has no prime factor outside S, then E_x(A) is bounded independently of A. In general the exceptional divisibility frequencies have the much larger energy displayed in (5.4).

For (3.4), the argument z is exactly N(ell)B/(N(c_0)^2K^2A^2). Thus (5.2) is usable at the original factor length A for each ell. It does not justify taking the squared norm through the ell sum. Those coefficients share the same row character and the Ramanujan divisibility constraints; the needed cancellation is in that coupled sum.

## 6. The exact common-divisor channel and the remaining coupled estimate

In the squarefree-row specialization, expand

\[
c_a(x)=\sum_{\substack{d\mid a\\d\mid x}}Nd\,\mu(a/d)
\]

and substitute a=de, x=dm. The outer squarefreeness gives d and e squarefree with (d,e)=1. There is no imposed coprimality between m and d or e in this divisor expansion. Retain all restrictions inherited from (3.4).

The quadratic phase and the transformed scale are then exactly

\[
\chi_k(ax)^3
=\chi_k(d^2em)^3
=\mathbf1_{(d,k)=1}\chi_k(em)^3,
\tag{6.1}
\]

\[
\frac{N\ell B}{N(c_0)^2(Nk)^2(Na)^2}
=\frac{Nm\,B}
{81N(c_0)^2(Nk)^2Nd\,(Ne)^2}.
\tag{6.2}
\]

In particular, the square d^2 disappears from the quadratic character while retaining its nonunit mask. On a dyadic channel Nd comparable to R and Ne comparable to E, with A comparable to RE, the frequency m has norm scale

\[
\frac{K^2RE^2}{B},
\qquad
N(em)\ {\rm has\ scale}\ \frac{K^2AE^2}{B}.
\tag{6.3}
\]

The large-d channels shorten e. At A=B, however, even E comparable to one leaves product scale K^2. Thus this exact substitution alone does not supply the desired short-row norm. Neither (6.1) nor the individual-frequency estimate (5.2) can be promoted to a diagonal-size moment by positivity or by discarding the signs mu(e).

The smallest new analytic gap can now be stated without an unspecified phase. One must estimate the coupled Ramanujan-theta expression in (3.4), with the exact scalar (2.6), square-root normalization (3.1), and the scale (3.3), strongly enough to bound its outer completed norm at the required initial conductor ratio. The Mobius sign is explicit in each divisor channel and the angular reciprocal-L structure is explicit in each frequency fiber. No estimate accomplishing that coupling is proved in this note.

## 7. Verification boundary

The finite companion checker uses actual split Eisenstein prime ideals and exact cyclotomic arithmetic to check the conjugate Gauss cancellation, its CRT cross phases, the local scalar scaling for every j, the Ramanujan identity on complete residue systems, and the preservation of positive-sixth-power zero masks. It does not authenticate the imported automorphy theorem, estimate an infinite theta sum, prove an angular zero-free region, or validate any short-row moment bound. The checker and its execution evidence are recorded separately so that those finite checks remain distinguishable from the mathematical source dependencies.
