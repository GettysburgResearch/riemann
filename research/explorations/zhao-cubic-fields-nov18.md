# The cubic fields in Zhao's strict spectral criterion

Assume GRH for the Dedekind zeta functions tested. Exactly **367 cubic fields** satisfy \(B_K=\sum_\gamma(1/4+\gamma^2)^{-1}<2\). They consist of the [seven cyclic cubic fields](zhao-abelian-fields-nov18.md) and **360 non-Galois cubic fields**. Of the latter, 104 are totally real and 256 have one complex place. The extreme signed discriminants in the non-Galois inventory are \(-6551\) and \(7816\). The question about the sign of the actual prime-ideal mean outside this sufficient criterion remains separate. [Complete non-Galois inventory](zhao-cubic-fields-nov18.json) · [Python/Arb and PARI checker](../../scripts/check_zhao_cubic_fields_nov18.py) · [Zhao, §8(3)](https://doi.org/10.1007/s40993-025-00640-y)

## Enumeration and local tests

The finite-support field bound with \(P=4\) and the completely split upper bounds for the two local Euler contributions ensures \(\Delta<96900\) in the real case and \(|\Delta|<55200\) in the complex case; the checker verifies both loose bounds at 96-bit ball precision. PARI/GP 2.17.2's exact \(\mathtt{nflist("S3",[1,B],r2)}\) enumerates 13,818 non-Galois cubic fields up to isomorphism within these bounds. For each prime in a test use \(\mathtt{idealprimedec(nfinit(f),p)}\) for residue degrees, including ramified and index primes. Each entry in the inventory gives the signed maximal-order discriminant and the descending coefficients of a defining polynomial. No polynomial discriminant is substituted for the field discriminant.

| Prime cutoff | Certified below | Certified above | Remaining |
|---:|---:|---:|---:|
| 16 | 43 | 12,363 | 1,412 |
| 64 | 91 | 261 | 1,060 |
| 256 | 45 | 595 | 420 |
| 1,024 | 95 | 165 | 160 |
| 4,096 | 36 | 21 | 103 |
| 16,384 | 19 | 29 | 55 |

For the remaining 55 fields, 31 pass and 24 fail by the independent theta formula below. A separate [full Dedekind contour](../../scripts/check_zhao_dedekind_contour_nov18.py) reproduced overlapping enclosures and the same strict side for every one of those 55 fields. The checker aborts on any overlapping threshold interval. The finite-support comparison uses [the general field-weight checker](../../scripts/check_zhao_field_weight_nov18.py).

## A degree-two theta certificate

Write \(L(s)=\zeta_K(s)/\zeta(s)=\sum a_n n^{-s}\), the standard two-dimensional representation of \(S_3\). It is induced from a nontrivial character of the order-three subgroup, hence has an entire completed Hecke L-function. The root number is one by division of the two Dedekind functional equations. Its coefficient at \(p^j\) has modulus at most \(j+1\) from the two local eigenvalues on inertia invariants, so \(|a_n|\le d(n)\le n\). At finite precision the coefficients are computed exactly by Dirichlet division of PARI's ideal-count coefficients by the all-ones sequence.

Set \(c=2\pi/\sqrt{|\Delta|}>1/64\), and \(\theta(t)=\sum a_n H(cnt)\), where \(H(x)=e^{-x}\) for a negative cubic discriminant and \(H(x)=K_0(x)\) for a positive discriminant. The Mellin transform equals the completed \(\Lambda(s)\) up to a positive constant independent of \(s\), by the Mellin transforms of the exponential and the Bessel function. Mellin inversion and the entire functional equation give \(\theta(1/t)=t\theta(t)\) in the right half-plane (first on the positive axis and then by analytic continuation). Thus
\[
 \frac{\Lambda'(1)}{\Lambda(1)}
 =\frac{\int_{\mathbb R}u e^u\theta(e^u)du}
        {\int_{\mathbb R}e^u\theta(e^u)du},
 \qquad
 B_K=2+\gamma_E-\log(4\pi)+2\Lambda'(1)/\Lambda(1).
\]
The last equality uses GRH and the symmetric completed logarithmic derivative, counting multiplicity at every ordinate. Apply the trapezoid rule on the full real line at spacing \(h=1/20\). Pairing the ordinates \(u=jh\) and \(-u\) gives summands \(u(e^u-1)\theta(e^u)\) in the numerator and \((e^u+1)\theta(e^u)\) in the denominator, with a single denominator term at zero.

Here are explicit absolute error bounds in the normalization above. On \(|\Im u|\le 1/2\), for \(v=|\Re u|\), the theta kernel on the positive real-part side has modulus at most \(12e^{-n e^v/80}\). Indeed \(\Re(cne^u)\ge n e^v/80\) there, and \(|K_0(z)|\le K_0(\Re z)\le \sqrt{\pi/(2\Re z)}e^{-\Re z}\) by its integral representation. Handle the negative half by reciprocity. The sum of the absolute integrals of either integrand on both boundary lines is below \(10^{12}\): use \(e^{-ne^v/80}\le e^{-n/160}e^{-e^v/160}\), \(\sum_{n\ge1} n e^{-n/160}<26000\), \(|u|\le 1+v\), and \(\int_0^\infty (1+v)e^v e^{-e^v/160}dv\le\int_1^\infty(1+w)e^{-w/160}dw<26000\). Strip contour shifting in the Fourier transform and Poisson summation bound the infinite trapezoid error by \(10^{12}/(e^{\pi/h}-1)<10^{-14}\).

Only terms with \(cn e^{jh}>128\) may be dropped from the folded sum. Factor \(e^{-64}\) out of the kernel's exponential decay, and bound its remainder by \(12 e^{-n/256}e^{-e^{jh}/256}\), using \(c>1/64\). The discarded error in either weighted sum is less than \(10^{12} e^{-64}<10^{-15}\), by \(\sum n e^{-n/256}<66000\) and
\[
 h\sum_{j\ge0}(1+jh)(1+e^{jh})e^{-e^{jh}/256}
 \le 2\int_1^\infty(1+w)e^{-w/270}\,dw<150000 .
\]
The last inequality compares each sample with its following mesh cell and uses \(256e^h<270\). The checker adds absolute balls of radius \(10^{-12}\) to numerator and denominator separately and verifies a positive denominator before division. All sampled exponentials, Bessel values and final comparisons use Arb. The GP polynomial list and number-field arithmetic, the standard degree-two Hecke continuation, and GRH are explicit dependencies.

Run from the repository root with python-flint and PARI/GP available:
```sh
python scripts/check_zhao_cubic_fields_nov18.py --output cubic-replay.json
```
The optional environment variable \(\mathtt{PARI\_GP}\) selects the executable.

## An unconditional check at one

The same 367 cubic fields, and no others, satisfy \(2\Xi'_K(1)/\Xi_K(1)<2\) without GRH. The completed entire function here includes the pole-cancelling factor \(s(s-1)\). A separate Euler derivative sieve on all 13,818 non-Galois candidates leaves 928 for a full Dedekind contour. It tests those fields and all 50 cyclic candidates directly. Exactly 360 non-Galois fields pass, identically matching the polynomial inventory above. The seven cyclic passing discriminants are 49, 81, 169, 361, 961, 1849 and 3969. In particular each passing field is unconditionally free of nontrivial real zeros. [Unconditional method and replay](zhao-low-degree-unconditional-nov18.md)
