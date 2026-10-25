# Internal review of the growing-band HLC extension

Reviewed object: `UNIFORM_HLC_AUDIT.md`, 21,382 bytes,
SHA256 `b346256f95beffb0bb8416cc292533370e9203e92bdacc6e923ce351e4cb0b6b`.
The finite projection used by this version is `TWO_SIGN_HLC.md`,
10,547 bytes, SHA256
`da49263ae36f47cf1162fd96859a700b9075e8211743d68fdc476d0cc939d73e`.
Remote-commit authentication is a separate publication step.

Reviewer: `native_gain`, a different research agent from the author of
these notes. I did not develop the projection or the growing-band
parameter choice. This is an internal analytic review, not external
peer review or formal verification. My assessment below is relative
to the explicitly imported source lemmas and identities, not an
independent certification of the entire 52-page HLC preprint.

## Material read and scope

I read the two complete notes above and the supplied source's extracted
text at the following printed page ranges: pp. 7--13 (mark expansion,
CRT comparison and Type I), pp. 17--35 (lists, good states, root
replacement, Fock operators, clean/dirty edges and global distinctness),
pp. 35--38 (pairings and removal of restrictions), and pp. 39--45
(major-arc normalization, sparse frequencies and completion).
The source PDF's exact version and digest are recorded in the parent
`SOURCES.md`. I checked the source formulas, not only the author's
paraphrase of their O_K notation.

## 1. The fixed-gap issue is explicitly repaired

The source's fixed-parameter estimate for the number of distinct DZ
values would not by itself allow K to grow. The explicit geometric
spacing supplies a replacement: the previous-band logarithms sum to
at most A_i/15. After squaring the count, the exceptional-set exponent
is -(11/15-o(1))A_i; Markov at e^(-A_i/4) leaves
-(29/60-o(1))A_i. I recomputed both constants. The additional union
over 2^K tests costs only a power of L and does not use a fixed
positive gap between the moving exponents a_i.

The first good-state test costs at most
2 exp(K log(J+1)-(log Y)/2), also exponentially small in L^(.11).
The same bounds hold for a selected subset of the geometric bands.

## 2. One-edge constants have the stated exponential dependence

This is the load-bearing uniformity check. At the reviewed rational
choice theta=9/10, v_0=24, rho=1/2, both endpoint and internal damping
factors obey

    sqrt(rho)/theta^2 + 1/(theta v_0) < 35/36 < 1.

The two displayed weighted Schur formulas on source p. 28 therefore
have factors at most one from the old memory coordinates. Their
remaining exponent per group is bounded by an absolute constant
smaller than 64, using V_i<=1 and s_i<=2. Multiplication over groups
gives e^(64K), including the square-root endpoint damping.

For edge operators I checked the following sources of dependence.

- There are four choices per group for whether its departing entry
  is appended and whether its incoming entry comes from memory.
  Summing them costs 4^K.
- A transfer changes the Schur weight by at most a fixed power of
  v_0 and contributes at most a factor 1/V_i<=2. Harmonic prime
  masses have uniformly bounded sum. These are fixed costs per band.
- In the raw dirty estimate the separated DZ condition permits a
  single omitted list tuple. The normalized omission mass is
  (J+1)^(-K), not its reciprocal. Repeated eligible coordinates are
  controlled by sup_(h>=1) h theta^(h-1), once per affected band.
  The exceptional-coordinate count is at most ceil(L^2)^K.
- The column estimate is the reversed transfer count. The resulting
  dirty norm uses the Schur square root, giving
  L(J+1)^(-K/2)+L^K exp(-cL^(.11)). This agrees with the corrected
  source formula (4.48), including its square root.
- In the clean measure conversion, nu_i(p)<=4/p implies
  m(a)<=4^K/a. The two endpoint square-root multipliers therefore
  cost at most a fixed constant times 4^K. All endpoint restrictions
  are contractions. The determinant Fourier matrix is planar and
  has no band index; its smooth derivative loss occurs once.
- The dirty comparison count (4.49), major-arc measure L^(3A_0)/Y,
  and the opposite absolute row bound give the last line of U14.
  The only memory-coordinate count there is the displayed L^(2K).
- List symmetrization is an average. Band labels are not permuted.
  I found no additional K! or exp(cK log K) factor in these local
  one-edge bounds, nor an A_0-dependent smooth estimate applied once
  per band.

Thus the C(A_0)e^(C_1 K) form in U14 is supported by the explicit
source construction, with C_1 independent of A_0. This is a review of
the dependence in those formulas, not an assumption that every
unspecified O_K constant in the paper has that dependence.

## 3. Global paths and distinctness remain within their budgets

The logarithms of d_0Y, the absolute path mass, and every retained
root modulus are bounded respectively by O(L^(.15)), O(L^(.66)),
and O(L^(.90)). All are o(log x). The original fixed-power arithmetic
root-counting remainder therefore remains smaller than the required
L^(-2AR). The Bonferroni tail at order L^(.76) has the additional
log L in its negative exponent and absorbs the path mass.

In the distinctness calculation the absolute edge exponent is allowed
to grow like K. The adjusted rank cutoff satisfies
r_0/R=O((K+1)log L/L^(.11))=o(1), uniformly in K<=log L/100.
The changes to at most 2r edges and the collection counts together
cost o(R log L). The product of the G_j norms costs at most
L^(1.3R), rather than a hidden constant independent of K. The stated
G>E_0+10 leaves enough margin for that cost. The large-rank prescribed
prime factor is still exponentially small in L^(.11).

The memory-cap tail, endpoint norm, harmonic collisions, bad-state
removal and dimension factor are retained. In particular
(d_0Y)^(1/(2R))=1+o(1); no spurious constant Fourier frequency or
factorial from auxiliary-list averaging appears.

## 4. Analytic parts keep fixed precision parameters

At rho=1/2 the exact binomial coefficient
l(rho-1)^(l-1) has absolute value at most one. Thus the truncated
mark coefficient is bounded by C^K, whereas the source's cruder
R_1^(2K) estimate would be inadequate at this growing K. The harmonic
coefficient mass has the same exponential-in-K form. The factorial
tail and the rough-sieve tail can absorb it at a larger fixed Type I
precision; mark and rough-sieve moduli remain x^(o(1)).

The character-modulus exponent A_0 remains fixed. In the major-arc
energy proof, extracting one band leaves a product of normalized
harmonic factors each of modulus at most one. The extracted band's
prime sizes stay in a common interior subrange of the allowed
endpoint inequalities. The Mellin cutoff is applied to the product
variable once. These observations support the asserted uniformity of
the fixed logarithmic major-arc saving. They do not extend the
character estimate to polynomial conductor or to growing A_0.

## 5. The growing-dimensional moment comparison is justified separately

I checked the coefficient U21 by differentiating z^n:

    n^2 z^(n-1) = z (d/dz)^2 z^n + (d/dz)z^n.

At z=rho^2=1/4 this gives exactly the stated coefficients of
binom(n,l); their absolute values are uniformly bounded. The
normalizers F_i'(1/2) stay uniformly bounded above and away from zero.
Hence every coefficient in any of the 3^N required moment products
is at most C^N.

For the integer and CRT tails, counting multiples with 3x/d and using
the band sums of 1/p or 1/(p-1), both eventually less than one, gives
the claimed N C^N/R_2! estimate. The extra prime logarithm contributes
only L. Retained divisors have norm x^(o(1)); their class -2 is
reduced. A single larger fixed Bombieri--Vinogradov precision absorbs
the coefficient bound. Thus U20 is a growing-dimensional divisor
argument, not an unjustified exchange of a fixed-dimensional Poisson
limit with N tending to infinity.

The CRT second moments converge uniformly to the stated r(1/2)<3.
The exact projection has coefficient mass at most N^(k-1)2^N/(k-1)!.
Its squared-error expansion uses only the moment products in U20,
and the coefficient mass is included. The Bernoulli lower-tail
comparison gives rate exponent log(3/2)/200, strictly larger than
1/1000. I found no unpriced normalization when passing from the
x-normalized prime sum to its prime probability measure. Dyadic
summation, partial summation, and the prime-power error then give U6.

## 6. Liouville appendix

The appendix is correctly labeled as an explicit version of an
extension anticipated by the source. Its small-square-divisor
Bombieri--Vinogradov transfer keeps the reduced progression condition;
the large-divisor tail is bounded by x log x/D+Q sqrt(x), with D and Q
chosen to supply the requested fixed logarithmic saving. In Type II,
the extra removal of selected-prime square divisibility is necessary
for the damping count even though lambda itself is completely
multiplicative. All selected moduli there remain x^(o(1)), and the
reciprocal-square prime mass makes that error negligible. The surviving
major-arc Möbius coefficient is the one from Vaughan's decomposition,
not a newly asserted Liouville character estimate.

## Assessment and limits

I found no gap in the proposed uniform extension at the explicitly
imported-source scope. The logarithmic HLC consequence is supported
by this extension and the finite projection; it is not already a
consequence of the paper's fixed-parameter theorem alone.

The weakest load-bearing boundary remains the imported determinant
root replacement/Fock identities and the one-edge dependence audit
U14. This review checks the latter against the source formulas but
does not certify the entire original paper or its external references.
The conclusion is a fixed-shift logarithmic saving. It does not imply
a power saving for the full shift average, hypothesis (H) for the
native inverse, or a new zero-free region.

## Exact remote authentication (2026-10-25)

I independently fetched `UNIFORM_HLC_AUDIT.md` and `MANIFEST.json` from
`GettysburgResearch/riemann` at the exact final mathematical commit
`5c7f4aa542ea2112b7f95fce984a35dfe454cfd6`, under
`standalone/2026-10-25-hlc-zero-free-transfer/second-pass/`.
For the fetched note, I recomputed both SHA256 and Git blob SHA-1
(including the `blob <byte-length>\0` header), compared the reported
GitHub blob, checked the manifest entry, and compared the local bytes.
All four checks agree:

- Byte length: `21382`.
- SHA256: `b346256f95beffb0bb8416cc292533370e9203e92bdacc6e923ce351e4cb0b6b`.
- Git blob: `6db6de522955e032e9d49a1a012f45bbade37871`.

The manifest itself is 2963 bytes, SHA256
`68f69ad289a722a358b113cdec20db41cf54755bffb2c1bce73cecdf045e3536`,
Git blob `ca948bb86211998ad92e2c147bfb6e9b4b945f8f`; its fetched bytes also match the
local manifest, and its Git blob was independently recomputed.

These are exactly the mathematical bytes reviewed above, also fetched
unchanged at the preceding mathematical commit
`3b47783a7c775bc8133f6601cb9bb97b1b38678a`.

This appendix authenticates this note and its manifest entry. It does
not extend the analytic assessment, authorship independence, imported
source certification, or claim scope stated above.
