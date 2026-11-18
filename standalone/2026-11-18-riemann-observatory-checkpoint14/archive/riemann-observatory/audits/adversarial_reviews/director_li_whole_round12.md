# Li 1997: complete-work adjudication and local normalization repairs

18 November 2026. The director read all nine printed pages 325–333 of Xian-Jin Li, *The Positivity of a Sequence of Numbers and the Riemann Hypothesis*, Journal of Number Theory 65 (1997), and the two independent complete reconstructions linked below. The pinned PDF is the journal-typeset manifestation recovered from the public Paperzz viewer, SHA-256 `8f5719751f869d71907c9da75270cb8c012b54f1453f54179461dbc331d255a1`, 706,759 bytes. The exact registered version is `1997 journal-typeset manifestation, pp. 325–333, recovered from Paperzz mirror`. The publisher record confirms identity, but the current publisher PDF was inaccessible; byte identity with that server is unverified. The original degraded text reproduction remains in the source history. The director also visually checked printed p. 330 to settle its differential, kernel, and coefficient conventions.

Both main theorems withstand reconstruction. This is a whole-work Level 3 promotion for the pinned manifestation, including the explicit local repairs below. It does not claim a proof of RH, novelty of Li's criterion, exhaustive correction history, or complete re-audit of the four cited reference works.

## Exact theorems and common proof

For the classical completion

```text
Xi(s) = s(s−1) π^(−s/2) Γ(s/2) ζ(s),   Xi(0) = Xi(1) = 1,
lambda_n = D^n[s^(n−1) log Xi(s)]_(s=1)/(n−1)!, n ≥ 1,
```

Theorem 1 says RH is equivalent to `lambda_n ≥ 0` for **every** positive integer n. Theorem 2 has the same quantifiers for one specified number field k and its normalized entire Dedekind completion. Neither theorem assumes simple zeros. A branch of the logarithm is initially needed only near 1; changing its branch adds a constant whose contribution is killed by the nth derivative.

Write `phi(z)=Xi(1/(1−z))`. This is analytic in the open unit disk, even without RH. The inverse map `z=1−1/s` sends that disk exactly to `Re s>1/2`. With reflected zero pairs rho and 1−rho, the product factors are

```text
(1−s/rho)(1−s/(1−rho)) = 1 + s(s−1)/[rho(1−rho)].
```

Order at most one gives summable inverse-square zeros, and hence normal convergence of this paired product. Any residual Hadamard exponential has zero slope by reflection and multiplier one by normalization at zero. A central zero, if present, has even multiplicity and can be paired. The local logarithmic derivative gives

```text
phi'(z)/phi(z) = sum_(n≥1) lambda_n z^(n−1),
lambda_n = sum_(rho paired) [1−(1−1/rho)^n].
```

The paired fixed-n summands are O_n(|rho|^−2). Individual summands are not absolutely reorderable. Differentiating a single factor at s=1 initially produces the inverse nth power; reflection within each pair turns it into the displayed positive power. This is legitimate paired relabeling. Critical-line pairs contribute `2−2 cos(n arg(1−1/rho)) ≥ 0`.

For the converse, the source's positive theta representation gives `phi(z)=1+sum a_j z^j` with a_j>0. The local identity implies

```text
lambda_n = n a_n − sum_(1≤j<n) lambda_j a_(n−j).
```

If all lambda_j are nonnegative, then `0≤lambda_n≤n a_n` for each n. On every closed disk of radius r<1, the logarithmic derivative series is absolutely dominated by phi'(r). It therefore extends analytically to the full disk. The identity `phi'=phi L` extends there by the identity theorem and excludes zeros by their orders of vanishing. Reflection completes both equivalences. A finite nonnegative prefix supplies no such global extension.

## Classical kernel, coefficient centers, and analytic details

With `psi(x)=sum_(m≥1) exp(−πm²x)`, the kernel

```text
W(x) = [x^(3/2) psi'(x)]'
     = π x^(1/2) sum_(m≥1) m²(πm²x−3/2) exp(−πm²x)
```

is positive on x≥1. Gaussian Poisson inversion, a Mellin split at 1, and two integrations by parts establish equation (1.2), including its factor 4 and endpoint constant. In particular `psi'(1)=−(1+2psi(1))/8`. Exponential decay permits all fixed derivatives and coefficient extractions uniformly on compact subdisks. Setting `u=z/(1−z)` and `L=(log x)/2`, the integrand becomes `exp(Lu)+x^(−1/2)exp(−Lu)`. For j≥1 its coefficient is

```text
sum_(l=1)^j binom(j−1,l−1) L^l/l! [1+(−1)^l x^(−1/2)] > 0, x>1.
```

The apparently different bracket in the initial infinite expansion (1.6) is correct: that expansion is at s=0, whereas the later finite formula is recentered at s=1. The same explanation applies to (3.6). An early apparent sign objection is withdrawn and is retained as negative audit knowledge, with no source-error flag.

The numerical initial radius 1/4 in the classical proof needs no empirical zero table. For |s−1|≤1/3 one has Re s≥2/3 and Euler summation gives

```text
(s−1) zeta(s)/s = 1 − (s−1) integral_1^infty {x} x^(−s−1) dx.
```

The subtracted term has modulus at most 1/2, so the expression is nonzero. The other completion factors are nonzero there. The map from |z|<1/4 lies inside this s-disk. A merely sufficiently small radius would also suffice for the proof.

## Dedekind conventions and two local false assertions

Read the source's definitions literally:

```text
G1(s)=π^(−s/2)Γ(s/2), G2(s)=(2π)^(1−s)Γ(s),
Z_k=G1^r1 G2^r2 zeta_k,
c_k=2^r1 (2π)^r2 h R/e,
Xi_k(s)=c_k^−1 s(s−1)|d|^(s/2) Z_k(s).
```

The standard Dedekind functional equation and residue formula give Xi_k(0)=Xi_k(1)=1 and reflection. Their exact uses, including all gamma factors, are independently checked in the two reports.

First, the sentence before (3.3), p. 329, says zeta_k is nonvanishing at zero. In fact `ord_0 zeta_k=r1+r2−1`. For a real quadratic field this is one. For example, `zeta_(Q(sqrt5))=zeta L(s,chi5)` and `L(0,chi5)=−(1−2−3+4)/5=0`. The proof needs the already established `Xi_k(0)=1`, so replacing the symbol repairs the sentence.

Second, the printed multiplier c_k^−1 in (3.4), p. 330, is inconsistent with its own complex gamma factor, kernel and product differential. Let epsilon_v=1 or 2 and `|x|=prod x_v^epsilon_v` as printed. Direct gamma integration gives, absolutely for Re s>1,

```text
integral_(positive orthant) Theta_k(x)|x|^(s/2) prod_v dx_v/x_v
  = (2π)^−r2 |d|^(s/2) Z_k(s).
```

A real place gives G1; a complex place gives `(2π)^−s Γ(s)`, which is G2/(2π). Thus (3.4)'s multiplier must be `(2π)^r2/c_k`, with the displayed kernel unchanged. The same factor repairs the normalized coefficient relation (3.7).

An exact one-dimensional witness removes any possibility of a hidden multi-coordinate measure convention. For k=Q(i), `r1=0,r2=1,|d|=4,h=R=1,e=4,c_k=π/2`. With the ordinary Jacobi theta function,

```text
Theta_k(x) = [theta(x)^2−1]/4 = sum_(nonzero integral ideals b) exp(−π N(b) x),
|x|=x²,
F(s)=integral_0^infty Theta_k(x)x^(s−1) dx = π^−s Γ(s) zeta_k(s).
```

Jacobi inversion gives `Theta_k(x)=x^−1 Theta_k(1/x)+(x^−1−1)/4`. Splitting at 1 yields

```text
F(s)=1/[4s(s−1)]+K(s),
K(s)=integral_1^infty Theta_k(x)(x^s+x^(1−s)) dx/x,
Xi_k(s)=4s(s−1)F(s)=1+4s(s−1)K(s).
```

Equation (3.4) instead gives coefficient 2/π. At s=2 the integral K(2) is strictly positive, so these formulas disagree exactly. The repair is a positive scalar and preserves the positivity needed in Lemma 3.2. This witness does not rely on floating-point agreement, RH, or the exact measure in an inaccessible edition of Lang.

For the general repaired split, push the positive kernel and logarithmic measure to `u=(log|x|)/2`. Its bilateral Mellin transform is the preceding F, with residues ±A_k where `A_k=c_k/(2π)^r2`. Fixed-strip polynomial bounds for Dedekind zeta and gamma decay justify Fourier inversion and a contour shift across 0 and 1. This gives `g(u)=A_k(e^−u−1)+e^−u g(−u)`, and hence the split with prefactor A_k^−1. The positive-side integral is entire by domination with a larger positive real Mellin exponent; fixed logarithmic derivatives are dominated in the same way. Expanding at s=1 gives the positive brackets `|x|^(1/2)+(−1)^l`. Multiplication by `s(s−1)=z/(1−z)^2` preserves positive Taylor coefficients. This reconstructs every step of Lemma 3.2 and the closing theorem and remark with corrected normalization.

## Dependency and coverage ledger

All definitions, equations, both lemmas, both implications of both theorems, the finite composition identity, coefficient interchanges, initial radius, endpoint normalizations, final remark, acknowledgments and four reference roles were checked. The local issues above do not invalidate either main criterion.

Barner's original GDZ journal pages, especially p. 142 Theorem 2, were read by both agents; the paired Hadamard proof also supplies the required product independently. Edwards's exact 1974 manifestation was not obtained; the classical product and grouping were independently derived. Weil's matching theorem was read in a later primary edition, with the original-edition identity limitation retained. The skeptic read Lang's full second-edition Chapter XIII §3, pp. 259–260, whose residue convention matches A_k; the exact cited 1970 measure was not obtained. The independent Mellin reconstruction and Q(i) witness avoid inferring it. The accepted classical functional equation, residue, growth, Gaussian Poisson and Hadamard inputs are matched at their use; their complete proof ancestry is not collectively audited. Bounded correction searches located no verified separate corrigendum and do not establish that none exists.

[Advocate reconstruction](uniform74_li_whole_advocate.md) · [Independent skeptic](prime74_li_whole_skeptic.md) · [DOI record](https://doi.org/10.1006/jnth.1997.2137) · [Public mirror identity](https://paperzz.com/doc/7086946/--science-direct)
