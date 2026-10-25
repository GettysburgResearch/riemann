# Independent source audit: arXiv:2610.20242v1

Date: 2026-10-25. Source: Guangshi Lü, Zhiwei Wang and Jie Wu, *On the Hardy–Littlewood–Chowla conjecture*, arXiv:2610.20242v1, submitted 2026-10-14, 52 pages. Uploaded PDF read locally in full. Primary web record: https://arxiv.org/abs/2610.20242; full HTML: https://arxiv.org/html/2610.20242v1.

## Finding

The paper reports the fixed-shift theorem

\[
\sum_{p\le x}\mu(p+2)=o(\pi(x)),\qquad
\sum_{n\le x}\Lambda(n)\mu(n+2)=o(x).
\]

It does not state a stronger zero-free region, an estimate for the unshifted Mertens sum with a fixed power saving, a power-saving shifted-prime theorem, or a uniform result over polynomially many shifts/moduli. Its strongest new input that looks potentially transferable is the arbitrary-coefficient determinant major-arc replacement in Proposition 4.2. This is a real arithmetic cancellation mechanism, rather than an inequality for just positive majorants. It is nevertheless at logarithmic-saving strength with frozen auxiliary parameters.

I found no concrete counterexample or fatal contradiction in the portions audited below. This is not certification of the complete 52-page proof: the prime-memory operator construction and its global distinctness argument are substantial new components, and should remain explicitly source-qualified if imported. The external paper is not a license to assume a power-strength or differently shaped analogue.

## Dependency map with exact locations

| Input | What it gives | Relevant limitation |
|---|---|---|
| Proposition 2.1, pp. 4–5, (2.2)–(2.4) | Vaughan decomposition after imposing `Z`-roughness, `Z=exp((log x)^0.24)` | Uses all three Vaughan pieces; a Type II estimate alone is not the original sum |
| Proposition 2.2, pp. 5–6, (2.5)–(2.11) | Uniform log-saving for sifted Möbius character–Mellin sums, `D>=x^δ`, modulus at most a fixed log-power, Mellin frequency at most a fixed power of x | Existing classical Möbius cancellation is an input, not a new zero-free conclusion |
| Proposition 2.3, pp. 7–10, (2.16) | Approximate constant function on shifted primes by averaging `b` independent prime-block marks | `b,K` and all band exponents are fixed before `x→∞`; quantitative variance cost does not disappear |
| Proposition 3.1, pp. 10–14, (3.2) | Type I log-saving via Bombieri–Vinogradov for Möbius and truncation of small-prime expansions | Moduli remain below the square-root range after all expansions |
| Proposition 4.2, p. 17, proved pp. 17–39 | `Q_Y-Q_Y^maj = O_A(XY (log x)^(-A))` for arbitrary log-bounded coefficients on sifted integers and `M,N>=x^δ` | `A_0,K` chosen sufficiently large but fixed; this is not a bound `XY x^(-η)` |
| Proposition 4.3, pp. 20–21, (4.21)–(4.26) | Exact parity conjugacy from determinant coefficient −2 to coefficient 1 | Nonzero shift and parity are structural hypotheses |
| Proposition 4.4, pp. 22–24 | Averaging arithmetic roots into independent projective lines over small primes | Residue moduli are `exp(O((log x)^0.98))`, not arbitrary polynomial-degree products |
| Proposition 4.5, pp. 32–35, (4.52) | High trace moment saving, moment order `2R≈sqrt(log x)` | Depends on small dirty-edge norm and global distinctness; high moment alone does not amplify a fixed operator contraction into a power saving after taking its root |
| Lemma 5.2, pp. 40–42, (5.6) | Small-prime polynomial large values occupy `exp(O((log x)^0.91))` unit intervals; arbitrary long Dirichlet polynomial has only polylog energy there | Prime size is subpolynomial; this sparse-frequency argument has a different shape from full character/inverse-moment estimates |
| Proposition 5.3, pp. 42–45, (5.12) | Major arcs small for the specific sifted Möbius coefficient | Arbitrary coefficients are allowed in Proposition 4.2, but not in this major-arc vanishing assertion |
| Theorem 1 proof, pp. 45–46, (5.17)–(5.19) | Weighted log saving, followed by `x→∞` then `b→∞`, proves unweighted `o(x)` | The order of limits provides no explicit unweighted decay rate |

The operator method is adapted from OpenAI, *The Poisson–Dirichlet law for prime predecessors*, September 24, 2026 version, 74 pages, cited as reference [11]. This is distinct from the quasi-RH / zero-free-family source.

## Checks of load-bearing algebra

### Vaughan truncation and Type I

The roughness factor is multiplicative over a product, so inserting it into Vaughan's identity is legitimate. The discarded prime powers have base prime at most `Z`. There is at most one power of a given prime in a dyadic interval, so the claimed `O(Z)` weighted error is compatible with the usual bound for the Chebyshev sum over primes up to `Z`.

The identity (3.4), `μ(dv)=μ(d)∑_{a|v, p|a⇒p|d}μ(v/a)` for squarefree d, is correct prime-by-prime. The proof explicitly retains higher powers in a; truncating a to squarefree values would have been an error, but the paper does not make that truncation. The square-root modulus requirement is respected in the displayed `da<=x^(1/20)` range. The complementary smooth-divisor tail is estimated separately. No contradiction found here.

### Nonzero-shift determinant and parity conjugacy

For coprime selected products a,b, equality `(mn+2)/a=(rs+2)/b` with integer quotient is exactly equivalent to

\[
bmn-ars=2(a-b).
\]

The transform `T(u,v)=(u,(u-v)/2)` is a bijection from odd-odd primitive vectors to primitive integer vectors with odd first coordinate in the transformed parallelogram. It changes determinants by −1/2. The major-arc torus substitution has two preimages, each with Jacobian 1/2, so equation (4.25) has no missing factor two. Complements transform by `(c,d)→(-2c,d-c)`, so `r_{TP}=-2r_P (mod 1)` is correct. The proof properly retains the parallelogram rather than enlarging to a potentially much larger axis-aligned box.

### Root averaging and Appendix A

The elementary fourth-moment argument in Appendix A gives a valid weaker-than-Weil Kloosterman bound. The orbit stabilizer of `(h,k)` under `(h,k)→(hs,ks^{-1})` is controlled by `(h,k,m)`, and the resulting factor in (A.2) is consistent with the fourth-moment count.

The projective line probability is exactly `1/(p+1)`, not `1/p`: each kernel of the first row of an `SL_2(F_p)` matrix occurs `p(p−1)` times among `p(p²−1)` matrices. At p=2, odd-odd first columns account for two of six matrices, giving the density `1/(3ζ(2))` used in Proposition 4.4. The residue and continuous boundary errors remain smaller than the target stretched-exponential log moment because all moduli and all discrete path choices have `exp(o(log x))` size.

### Clean and dirty edges

The clean-edge minor-arc matrix reduces to a tensor product of two rectangular Fourier matrices. The Gram-matrix estimate and the determinant tensor normalization on pp. 29–30 are consistent. The source does not discard the shared-prime congruence when replacing the other divisibility indicators; retaining it is essential to the lattice reduction.

The dirty-edge estimate is qualitatively different. A previously stored prime supplies one endpoint and fixes a projective line; the good-state condition permits at most one admissible tuple of omitted entries. Its saving is the list-symmetrization probability `(J+1)^{-K}`. This is precisely the part that remains only a log saving and blocks a simple polynomial-scale redesign.

The finite local damping expansion on pp. 25–27 is algebraically consistent with independent projective-line averaging. The proof of global distinctness on pp. 33–35 is more substantial than these local checks; I did not establish a complete independent formal reconstruction of that Fock-space calculation. No specific failure was found, so it should not be described as false or disproved.

### Major-arc normalization

The combined scale in Proposition 5.3 is correctly

\[
(YMN)^2\times X^{-1}\times Y^{-1}\asymp XY.
\]

The kernel is separated in a thin difference coordinate before Mellin inversion. The resulting frequency range has length about X, not the short length of one original factor. The paper notices that a naive pointwise Möbius bound followed by mean-square for the other factor loses `T/N≈M`, and uses Lemma 5.2 to avoid this. That distinction matters if one tries to transfer the result to the repository's signed moment estimates.

## Why taking shift zero cannot produce the desired unshifted theorem

For the actual marks of (2.13), `W_j(p)=0` for every sufficiently large prime p: a prime p has no factors in the prescribed small-prime bands. Therefore the analogue of Proposition 2.3 at shift zero fails completely; an average of these marks cannot approximate 1 on primes.

In the sifted Type II sum one likewise has `W(mn)=0`, because m,n have no prime factors in the selected small bands. For coprime a,b the equation `bmn=ars` has no solutions on this support, since every prime of b is coprime to ars. Thus the marked zero-shift estimate would be vacuous, not strong cancellation for the original unweighted sum.

The direct check is

\[
\sum_{n\le x}\Lambda(n)\mu(n)=-\vartheta(x)\sim-x.
\]

All composite prime powers have Möbius value zero, and primes have Möbius value −1. Hence any argument that treats nonzero shift as a removable detail and concludes `o(x)` for this zero-shift sum is false.

If one removes sifting to formulate a different zero-determinant operator, proportional-vector resonances reappear and must be treated explicitly. Simply subtracting `−ϑ(x)` proves nothing new. Subtracting `−x` instead leaves exactly the prime-number-theorem error one is trying to improve.

There is an exact analytic expression for this distinction. For `Re s>1`, let

\[
F_0(s)=\sum_n\frac{\Lambda(n)\mu(n)}{n^s}
      =-\sum_p\frac{\log p}{p^s}
      =\frac{\zeta'}{\zeta}(s)+R(s),
\qquad
R(s)=\sum_p\sum_{k\ge2}\frac{\log p}{p^{ks}}.
\]

The series R is holomorphic for `Re s>1/2`. Consequently holomorphy of `F_0(s)+1/(s−1)` in a fixed half-plane to the right of 1/2 would itself exclude zeros there. The fixed-shift theorem controls a different series `F_2`; the paper supplies no identity that continues `F_0` from `F_2`.

## Why polynomial rescaling does not close the gap

Write `L=log x`. Equations (4.10), (4.48), (4.51), (4.68), and (A.5) display the relevant competing requirements:

\[
J=\lfloor L^{0.01}\rfloor,\qquad 2R\asymp L^{1/2},
\]

\[
\epsilon_K\ll_{K,\rho}L^2(J+1)^{-K}+L^{2K}e^{-cL^{0.1}},
\qquad
\|E_j^{\rm dirty,raw}\|\ll\sqrt{\epsilon_K},
\]

\[
|\langle f,Ag\rangle|
\ll d_0YMN\,L^{-E_0+4C}(d_0Y)^{1/(2R)},
\]

while the projective-root discrepancy is bounded by

\[
S^5\min(d_0YM,N)^{-1/100}.
\]

The original proof makes `log(d_0Y)=O_K(L^0.21)` and all path residue moduli `S=exp(O_K(L^0.96))`. This explains why large R is affordable and why the trace-to-pairing dimension factor is bounded.

Now replace each prime band by primes of size `x^{ε_i}` with fixed positive ε_i. The collision term becomes smaller, but the dirty-edge factor `(J+1)^{-K}` does not improve. With fixed K, a gain `x^{-η}` from that factor requires J to be a fixed positive power of x. Then the auxiliary product of KJ primes has

\[
\log d_0\ge KJ\epsilon_{\min}\log x,
\]

and the necessary residue products are far too large for (A.5). Even keeping J fixed while allowing R to grow produces path moduli containing increasingly many polynomial-size primes; the given discrepancy estimate cannot absorb them. Freezing R and J avoids that specific blowup, but leaves a constant dirty-edge bound and the positive factor `(d_0Y)^{1/(2R)}`, which prevents the required saving.

This is a barrier of the estimates as written, not a theorem that no future arithmetic refinement can succeed. A usable polynomial-strength redesign needs a new estimate for dirty edges or a different way to control arithmetic roots and resonant tuples. Merely knowing a zero-free boundary that strengthens Möbius cancellation on the major arcs does not remove this independent Type II obstruction.

There is a second transparent obstruction to increasing K within the original prime bands. Each band has harmonic prime mass tending to `log 2`, while the whole available range has harmonic mass only

\[
\sum_{\exp(L^{0.1})<p\le\exp(2L^{0.2})}\frac1p
=0.1\log L+\log2+o(1).
\]

Thus only `O(log L)` disjoint bands fit. With `J=L^0.01`, even their best formal combined list saving is `exp(-O((log L)^2))=x^{-o(1)}`, not a fixed power. For disjoint real defining intervals the exact elementary inequality is `(K−1)log2<0.1logL`; for merely disjoint prime sets use harmonic mass rather than claiming exact geometric interval packing.

## Exact mark-variance refinement

The separate note [MARK_VARIANCE.md](MARK_VARIANCE.md) proves the finite CRT identity and its fixed-parameter prime asymptotic, including the precise quantifiers.

## Reproducible finite checks

Run `python3 paper_audit_checks.py` from this packet directory. The script uses only the standard library and checks:

- 762 parity/conjugacy cases for odd primitive vectors with coordinates below 64;
- exact projective probabilities for p=3,5,7,11;
- the elementary fourth-moment root-count inequality for every modulus 2 through 40;
- all 216 local projective configurations for the three-vertex damping identity at p=5;
- the exact zero-shift prime-power identity through 100,000 (floating-point log sums agree to 2e−11).

These finite checks test the cited algebra and the transfer obstruction. They do not verify asymptotic operator estimates or establish a new zero-free region.
