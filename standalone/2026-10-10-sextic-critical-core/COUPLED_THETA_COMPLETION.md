# Coupled theta completion: exact cancellation and quantitative component bounds

Status: proposed reviewable deductions from the imported theta transformation and classical quadratic/cubic large sieves. The complete balanced fourth moment remains open. The main new facts are an exact coupled reflection, bounds for its individual Ramanujan components, and a stronger estimate on the explicit standard infinity-cusp face.

Scope: squarefree primary dual rows, outside a fixed finite bad set. These results concern a completed balanced divisor polynomial and specified components of its reflected expansion. They do not assert the canonical estimate for arbitrary dual rows, nor the initial adverse range of the fourth moment.

Source: OpenAI October 5 `paper2.tex`, pinned at `adc7f1241b42e322a6451854ab7e4b4c146bf78a`, in the October 7 import. Load-bearing identities are `eq:crt-a` (around line 850), `eq:T` and `eq:completed-twist` (1289–1310), `eq:intro-theta-coefficients` (363), `eq:theta-local-factors` (1730), `eq:reflection` (1809), `lem:reflection-uniformity`, `lem:theta-bounds`, `eq:ray-local-transform` (3230 onward), and the full scalar immediately after `eq:dual-cusp-mellin-series` (3418 onward). The scalar is independently derived in `REFLECTION_SCALAR_AUDIT.md`. All prior packets remain unchanged.

No Lean build, zero computation, or numerical asymptotic inference is used. Statements below retain the imported transformation as an analytic input; they are not a new verification of its automorphy proof.

## 1. Exact object and conventions

Work in K=Q(omega), O=Z[omega]. All arithmetic indices denote primary ideal generators. The original divisor and row indices a,k, and their factors e,f,g, are outside a fixed set S containing primes over 6. Reflected theta indices n,b,n',b' are allowed to meet S unless a restriction is explicitly displayed; this retains the full source theta support. Put N(a)=|a|^2, alpha(a)=a/|a|, and chi_a(k)=(k/a)_6, with its literal zero extension. Fix a ray character xi supported at S and set

\[
a_\xi(a)=\overline{\alpha(a)}\gamma_2(a)\xi(a).
\]

The imported CRT formula is

\[
a_\xi(ab)=a_\xi(a)a_\xi(b)\chi_b(a)^4
\quad ((a,b)=1,\ a,b\text{ squarefree}).                 \tag{1.1}
\]

Let A,B,H>=1 be polynomially bounded in an auxiliary D. Fix smooth compactly supported norm weights W_1,W_2. Let T(B;k,a) be the source's completed theta sum with twist

\[
\Psi_{k,a}(n)=\xi(n)\chi_n(k)\chi_n(a)^4,
\]

using W_2. Define the balanced completion

\[
\mathcal C_{A,B}(k)=\frac1{\sqrt A}
 \sum_{a\ \mathrm{squarefree}}a_\xi(a)\chi_a(k)
 W_1(Na/A)T(B;k,a).                                    \tag{1.2}
\]

The outside factor chi_a(k) makes every term with (a,k)>1 zero. Its cube-free face is exactly

\[
\frac1{\sqrt{AB}}
\sum_{a,n\ \mathrm{squarefree}}a_\xi(an)\chi_{an}(k)
W_1(Na/A)W_2(Nn/B)\mathbf1_{(a,n)=1}.                    \tag{1.3}
\]

This follows from (1.1); the inner character chi_n(a)^4 supplies the coprimality mask. Thus (1.2) is an actual completion of the balanced squarefree divisor column, not an invented coefficient class.

Theorems below average over squarefree k with H<=Nk<2H. A bounded initial range can be included by finitely many dyads. Symbols such as D^epsilon allow constants depending on epsilon, fixed polynomial scale ceilings, fixed S/xi, and finitely many smooth seminorms.

## 2. The scalar cancellation makes the coupled character quadratic

Take a,k squarefree, coprime, and outside S. At primes of k the source's local exponent is j=1, while at primes of a it is j=4. All these primes are active. In a fixed term of the finite bad-ray decomposition, write c=c_0ka, with c_0 supported at S, and put t=lambda^2c_0.

The explicit scalar computation in the companion audit, using the source's full scalar including bar(alpha(c))^2, gives

\[
a_\xi(a)\,C(k,a)
 =R(k)\,\eta(a)\,\overline{\alpha(a)}^{3}
   \chi_a(k)^2.                                         \tag{2.1}
\]

Exactly, the companion scalar audit defines F_0, Gamma(k), and Xi(a) with R(k)=F_0 Gamma(k) and eta(a)=Xi(a); the different notation F_0 here distinguishes that scalar from the norm scale F below. Here R(k) has bounded modulus, and eta is a fixed ray character, with bounded fixed scalars absorbed; after finitely many fixed ray-class splits, the cusp coefficient, additive character, c_0, and eta are independent of the varying a,k. Exact fixed factors are recorded in the scalar audit; no variable Gauss factor is hidden in eta. The root-number part depending on k alone may be placed outside its row norm.

Two arithmetic identities are responsible:

\[
\gamma_2(a)\gamma_4(a)=1,
\qquad
\gamma_4(ka)=\gamma_4(k)\gamma_4(a)\chi_a(k)^2.             \tag{2.2}
\]

The first uses chi_a(-1)^2=1; the second is normalized Gauss CRT plus reciprocity to an even exponent. The source's angular scalar is why the surviving angular power in (2.1) is bar(alpha(a))^3, not bar(alpha(a)).

Multiplying (2.1) by the outside chi_a(k) in (1.2) makes its dependence chi_a(k)^3. The primes of k contribute the transformed factor chi_k(lambda^4 ell)^3. By quadratic reciprocity and a further fixed ray split, their product is the quadratic character of a times the dual index. In particular, the a sum can remain coupled to the theta sum throughout reflection.

For clarity, on a theta support term ell=u lambda^m n b^3, n squarefree, the variable character becomes

\[
\chi_k(a n b)^3,                                        \tag{2.3}
\]

up to fixed unit/bad-ray factors. The a-prime factor is the exact normalized Ramanujan product

\[
B_{a,4}(u\lambda^{m+4}nb^3)
 =\prod_{p\mid a}(Np)^{-1/2}
    \bigl(-1+Np\,\mathbf1_{p\mid nb}\bigr).              \tag{2.4}
\]

The dependence on u,lambda has disappeared from its divisibility test because a is outside S. Equations (2.1)–(2.4), inserted into the source's absolutely convergent reflected expansion, are the coupled reflection identity. It does not take Cauchy over a.

There is no omitted polar term: this is a linear combination of the source's completed transforms, whose horizontal derivative removes the constant modes at every cusp. The finite a sum commutes with that identity. This uses the source's analyticity argument, not a new assertion that arbitrary divisor-weighted theta functions are automorphic.

## 3. Exact local decomposition and normalizations

At each p|a use the three-term identity

\[
(Np)^{-1/2}(-1+Np\mathbf1_{p\mid nb})
=-(Np)^{-1/2}
 +(Np)^{1/2}\mathbf1_{p\mid n}
 +(Np)^{1/2}\mathbf1_{p\nmid n,\ p\mid b}.                \tag{3.1}
\]

Allocate the prime to g,e,f, respectively. Thus a=efg with e,f,g pairwise coprime and squarefree. Reindex n=e n' and b=f b'. Preserve n' squarefree, (e,n')=1, and (f,en')=1. There is no restriction that g be coprime to n'b': its negative term in (3.1) exists also at divisibility points. Forgetting this would change the expansion.

The product of the local amplitudes is mu(g) sqrt(N(ef)/Ng). Against the source's denominator sqrt(Nn) Nb it leaves

\[
\frac{\mu(g)}{\sqrt{Nf\,Ng}\sqrt{Nn'}\,Nb'}.             \tag{3.2}
\]

The source's normalized theta coefficient remains bounded after this reindexing, since its numerator grows at most by sqrt(Nf) when b is replaced by fb'. The quadratic character in (2.3) becomes

\[
\chi_k(g n'b')^3\,\mathbf1_{(k,ef)=1}.                  \tag{3.3}
\]

The zero mask is compulsory. The square factors e^2 f^2 do not yield one when a prime divides k. The g mask remains inside chi_k(g).

Take dyadic scales Ne~E, Nf~F, Ng~G, with EFG comparable to A. On a fixed m and cube dyad Nb'~C, the squarefree n' scale is

\[
U\asymp\frac{H^2EG^2}{BF\,3^m C^3}.
\tag{3.4}
\]

For sums over all m and C, use the common scale

\[
Y:=\frac{H^2EG^2}{BF}.                                  \tag{3.5}
\]

The normalization outside the n',b' sums is comparable to (AFG)^(-1/2). Norm ratios of e,f,g,k in their dyads appear in a common smooth kernel. Its Mellin separation has a uniform integrable majorant, by the imported transformed-weight bounds. The character phases have modulus at most one and the theta coefficient after normalization is bounded. The dependence on a,k through fixed ray classes was fixed before this separation.

A component below means the sum from precisely these allocations and norm blocks, with the retained masks, the original signs, and the original reflected coefficient. The three components at one prime are algebraic summands; they are not a disjoint partition of dual frequencies.

## 4. A quadratic product-column lemma with every repeated-prime mask

Let k range over squarefree primary indices with Nk<=H. Suppose c_{g,n} is independent of k, bounded by one, and supported on squarefree g,n with Ng~G, Nn~U. Then

\[
\sum_k^*\left|\sum_{g,n}^*
 \frac{c_{g,n}}{\sqrt{Nn}}\chi_k(gn)^3\right|^2
\ll(HGU)^\epsilon G(H+GU).                              \tag{4.1}
\]

**Proof.** Write h=gcd(g,n), g=h g_1,n=h n_1. Then g_1 n_1 is squarefree and \(\chi_k(gn)^3=\mathbf1_{(k,h)=1}\chi_k(g_1n_1)^3\). Fix h, drop this row mask only as a contraction in the norm, and group by r=g_1n_1. Each r has divisor-boundedly many such factorizations. Its coefficient energy is at most

\[
(GU)^\epsilon\frac{G}{(Nh)^2},
\]

because there are O(GU/(Nh)^2) pairs and 1/Nn=O(1/U). The quadratic large sieve gives, for this fixed h,

\[
\ll(HGU)^\epsilon\frac G{(Nh)^2}
 \left(H+\frac{GU}{(Nh)^2}\right).
\]

Minkowski over h costs sums of 1/Nh and 1/(Nh)^2, respectively. The first is logarithmic and the second converges by ideal counting. This proves (4.1). If a scale is bounded, include it in a fixed unit-sized annulus; empty supports are zero. \(\square\)

## 5. Universal bounds for each reflected allocation block

### Theorem 5.1

For every E,F,G block of the coupled reflection, at every cusp, the mean square of its contribution over squarefree rows k~H satisfies

\[
\boxed{\sum_k^*|\mathcal C_{E,F,G}(k)|^2
 \ll D^\epsilon
 \left(\frac{HE}{G}+\frac{H^2A^2}{BF^3}\right).}           \tag{5.1}
\]

The finite bad-ray decomposition and all theta units/ramified valuations are included. The statement assumes the source's coefficient and transformed-weight estimates.

**Proof.** First fix e,f,b' and a theta unit/ramified valuation. The squarefree reflected n' may contain primes of S. Split its S-part first: there are finitely many squarefree patterns, and each changes the norm scale by a fixed factor and contributes a fixed bounded row phase. Apply (4.1) to its remaining squarefree part outside S. The cube index b' remains unrestricted at S; its row character is simply a contraction for each fixed b'. No reflected bad-prime powers are deleted. The mask (k,ef)=1 is a fixed row contraction. The factor chi_k(b')^3 is another contraction. Separate the common smooth kernel before applying (4.1) to g,n'. By (3.2), (3.4), and the outer A^(-1/2), the square norm on an n' dyad is

\[
\ll D^\epsilon\frac1{AF}\,(H+GU),
\]

times the source's ramified-decay and smooth tail factors. There are O(EF) choices of e,f. Minkowski gives

\[
D^\epsilon\frac{E^2F}{A}(H+GU).
\tag{5.2}
\]

On a fixed cube dyad, sum b' with weight 1/Nb'; its total mass is O(1), so this causes no positive power of C. Summing n' and cube dyads costs only logarithms until 3^m U C^3 reaches Y; beyond it the transformed weight decays faster than any power. Its factor 3^(-m/3), m>=-4, makes the ramified sum convergent up to a subpower. Thus replace U by O(Y) in the second term of (5.2), and keep H in the first. If Y<1, the same statement follows from the rapidly decreasing nonzero tail; no sieve is applied at length below one.

Finally, EFG~A and Y=H^2EG^2/(BF) give E^2F/A~E/G and E^2F GY/A~H^2A^2/(BF^3). This proves (5.1). \(\square\)

Two exact extremes illustrate a real gain over the factorwise-Cauchy estimate A(H+H^2A/B):

- All divisor primes allocated to the dual cube part: F~A, E=G=1. Its energy is O(D^epsilon[H+H^2/(AB)]), the ideal completed length AB.
- All divisor primes allocated to the negative terms: G~A, E=F=1. Its energy is O(D^epsilon[H/A+H^2A^2/B]). The first term improves by A^2, but its long-dual term remains.

The all-squarefree-divisibility component E~A, F=G=1 has the old bound A H+H^2A^2/B from (5.1). Section 6 improves that component on the explicit standard cusp face.

## 6. A second sieve improves the standard infinity-cusp face

Restrict the reflected coefficients to the explicitly known face

\[
\ell=\lambda^{-3}n b^3,\qquad (nb,S)=1,
\qquad d_0(\ell)=3^{5/2}|b|\overline{\chi_n(\lambda)^2}\gamma_2(n).
\tag{6.1}
\]

This is a precisely specified component, not a claim that every cusp sequence has this form. Under n=e n', b=f b', Gauss CRT gives

\[
\gamma_2(en')=\gamma_2(e)\gamma_2(n')\chi_{n'}(e)^4.
\tag{6.2}
\]

The supplementary factor overline(chi_(en')(lambda)^2) factors multiplicatively into fixed-ray factors of e and n'. After combining alpha(ell) with bar(alpha(a))^3 from (2.1), the arithmetic dependence in e,n' factors into bounded separate coefficients times chi_{n'}(e)^4. All remaining fixed-ray additive phases are periodic modulo a fixed S-supported ideal; splitting e,n',b' into those finitely many classes preserves this separation. Restrictions involving fixed f,g go into the separate coefficient vectors. The variable coprimality of e,n' is already the zero of chi_{n'}(e)^4.

### Lemma 6.1: a quadratic–cubic composition with its row mask

Let |u_e|,|v_n|<=1, supported on squarefree e~E,n~U outside S. For squarefree k~H put

\[
Q_k=\frac1{\sqrt{EU}}\sum_{e,n}^*
 u_e v_n\,\mathbf1_{(k,e)=1}\chi_k(n)^3\chi_n(e)^4.
\]

Then

\[
\boxed{\sum_k^*|Q_k|^2
 \ll(HEU)^\epsilon\frac{H+U}{U}
 \left[E+U+(EU)^{2/3}\right].}                           \tag{6.3}
\]

Bounded smooth norm kernels may be included by uniform Mellin separation, before either sieve.

**Proof.** Expand the mask as sum_(d|k,e) mu(d). For each fixed k use divisor-Cauchy, at cost tau(k), rather than Minkowski across d. Write e=d e',k=d k'. The remaining ranges are E/Nd and H/Nd. Multiplicativity puts every d character factor into v_n; it has modulus at most one. The coefficient u_(de') remains bounded. Retain squarefreeness and the masks (e',d)=(k',d)=1, dropping only the latter after it has become a fixed row restriction.

For fixed d, the quadratic large sieve in k' first gives (H/Nd+U) times the n-coefficient energy divided by EU. The cubic large sieve in e',n bounds that coefficient energy by

\[
(HEU)^\epsilon\frac E{Nd}
\left[\frac E{Nd}+U+\left(\frac{EU}{Nd}\right)^{2/3}\right].
\]

Consequently the fixed-d bound is

\[
(HEU)^\epsilon\frac{H/Nd+U}{(Nd)U}
\left[\frac E{Nd}+U+\left(\frac{EU}{Nd}\right)^{2/3}\right].
\tag{6.4}
\]

Its six expanded terms involve sums of (Nd)^(-3), (Nd)^(-2), (Nd)^(-8/3), (Nd)^(-2), (Nd)^(-1), and (Nd)^(-5/3). All converge except the explicitly logarithmic fifth one. After reassigning epsilon, their sum is bounded by the right side of (6.3). This proves the lemma with the moving zero mask intact. \(\square\)

### Theorem 6.2: component estimate and a quantitative range gain

For the face (6.1), the E,F,G component satisfies

\[
\boxed{\sum_k^*|\mathcal C^{(0)}_{E,F,G}(k)|^2
 \ll D^\epsilon\left[HE+Y+(EY)^{2/3}\right],
 \qquad Y=\frac{H^2EG^2}{BF}.}                            \tag{6.5}
\]

It also satisfies (5.1), so the minimum of these two proved bounds is available.

**Proof.** First fix f,g,b'. Use (6.2) and separate the smooth norm kernel. The row factor chi_k(gb')^3 and mask (k,f)=1 are contractions. The remaining sum is Lemma 6.1 with the necessary mask (k,e)=1 retained. The actual prefactor in (3.2) gives the factor E/(AFG) relative to that lemma. Minkowski over the O(FG) frozen f,g labels exactly costs (FG)^2; since EFG~A their total product is O(1). This proves (6.3)'s bound with e-scale E and n'-scale U, on each cube dyad.

Again sum b' with weight 1/Nb', giving bounded mass on its dyad. For 1<=U bounded by a fixed multiple of Y, expand (6.3)'s right side as

\[
H+U+HE/U+E+HE^{2/3}U^{-1/3}+E^{2/3}U^{2/3}.
\]

Since H,E>=1, this is at most a constant times HE+Y+(EY)^(2/3). Dyadic summation costs only a subpower; the tails are controlled by the same smooth-decay argument as in Theorem 5.1. This proves (6.5). \(\square\)

In particular the all-squarefree-divisibility component E~A,F=G=1 has

\[
\sum_k^*|\mathcal C^{(0)}_{A,1,1}(k)|^2
\ll D^\epsilon\left[HA+\frac{H^2A}{B}
 +\left(\frac{H^2A^2}{B}\right)^{2/3}\right].              \tag{6.6}
\]

For A=B=D and 1<=H<=D, this is O(D^(2+epsilon)). The previous factorwise-Cauchy estimate is O(D^epsilon[D H+D H^2]) and reaches D^2 only up to H<=D^(1/2). Thus the particular standard-cusp component has a rigorously larger admissible dual-row range. It is not an improvement of the full canonical domain, since other components and row valuations remain.

## 7. What remains after these deductions

The exact reflection exposes two different useful structures. The Ramanujan component assigned to dual cubes has the completed bound at total length AB. On the explicit infinity-cusp face, the component assigned to the squarefree theta index gains from a composition of cubic and quadratic large sieves, with a full treatment of the moving row mask.

The all-negative component G~A,F=E=1 retains the long-dual term H^2A^2/B. At A=B=D this is H^2D. Neither (5.1) nor (6.5) brings it to D^2 beyond H~D^(1/2). The fourth-moment initialization needs H of order D^(3-theta), so a very large gap remains. Summing improved bounds on some algebraic components does not suppress this one.

The coefficient in this difficult component is particularly explicit: mu(g)bar(alpha(g))^3 times a fixed ray factor, coupled to the theta index through a quadratic character and the ratio N(theta index)/Ng^2. A future argument can target that exact Möbius–angular sum or its joint Dirichlet series. Replacing it by bounded arbitrary coefficients forfeits the remaining arithmetic cancellation. None of the estimates above proves that such cancellation is impossible.
