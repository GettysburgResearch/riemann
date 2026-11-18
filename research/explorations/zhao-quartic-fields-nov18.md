# The quartic fields in Zhao's strict spectral condition

Assume GRH for the Dedekind zeta functions tested. Exactly **871 quartic fields** up to isomorphism satisfy \(B_K=\sum_\gamma (1/4+\gamma^2)^{-1}<2\). The count includes 47 [abelian quartics](zhao-abelian-fields-nov18.md) and 824 nonabelian quartics. The following inventory identifies the nonabelian fields by signed maximal-order discriminant, number of complex places, and descending coefficients of PARI's canonical defining polynomial. [Inventory](zhao-quartic-fields-nov18.json) · [Zhao, §8(3)](https://doi.org/10.1007/s40993-025-00640-y)

| Galois closure group | Totally real | Two real places | Totally complex | Total |
|---|---:|---:|---:|---:|
| Abelian | 16 | 0 | 31 | 47 |
| Dihedral of order eight | 40 | 82 | 141 | 263 |
| Alternating of degree four | 0 | 0 | 3 | 3 |
| Symmetric of degree four | 38 | 385 | 135 | 558 |
| All | 94 | 467 | 310 | 871 |

## Complete candidate source

At \(P=3\), use the [finite prime inequality](zhao-field-prime-test-nov18.md) with the completely split Euler bound for both rational primes. The checker proves at 96-bit interval precision that \(B_K\le2\) implies \(|\Delta|<759909,450317,266855\), respectively, in order of increasing complex places. These caps are within the corrected Cohen–Diaz y Diaz–Olivier quartic tables of fields with absolute discriminant below one million. Their three files have 13,073, 90,671, and 81,322 rows respectively. The inventory calculation checks SHA-256 digests of the complete uncompressed files and identifies the Galois groups over the rationals. The table source removes any class-group GRH dependency beyond the stated spectral hypothesis. [Bordeaux corrected tables and errata](https://pari.math.u-bordeaux.fr/pub/pari/packages/nftables/README.txt) · [Data files](https://pari.math.u-bordeaux.fr/pub/pari/packages/nftables/) · [Table extraction](../../scripts/check_zhao_quartic_tables_nov18.py)

| Closure group | Candidate fields | Needed contour evaluation | Passing |
|---|---:|---:|---:|
| Dihedral | 17,209 | 50 | 263 |
| Alternating | 68 | 1 | 3 |
| Symmetric | 49,474 | 135 | 558 |

We additionally compared PARI's independent class-field enumeration to the table by discriminant and group for all dihedral and alternating signatures and totally real symmetric fields, comparing canonical \(\mathtt{polredabs}\) representatives whenever several fields share the same signature, group and discriminant. The three tables supplied the larger mixed and complex symmetric inventories directly.

The [Euler checker](../../scripts/check_zhao_quartic_fields_nov18.py) uses the prime test at \(P=8,32,128,512,2048,8192\). When the prime does not divide the index of the defining order, Dedekind's factorization criterion gives the residue degrees from the distinct factors modulo that prime. At index primes it uses \(\mathtt{idealprimedec(nfinit(F),p)}\). The [contour checker](../../scripts/check_zhao_quartic_contour_nov18.py) resolves the remaining 186 fields. The [full Dedekind contour](../../scripts/check_zhao_dedekind_contour_nov18.py), using truncated Euler logarithms in place of the Artin coefficients, independently reproduced the strict side and overlapping balls in all 186 cases. Direct Bordeaux replays produced identical canonical inventories, decisions and contour balls for the earlier dihedral, alternating and totally real symmetric calculations.

## An independent contour check for close quartic fields

Put \(r=r_2\) and let \(L(s)=\zeta_K(s)/\zeta(s)\), with coefficients \(a_n\). At every prime the Euler polynomial is that of the three-dimensional permutation representation with the trivial summand removed, on inertia invariants. Its eigenvalues have modulus at most one, giving \(|a_n|\le d_3(n)\). The completed function is entire for all three tested groups. In \(D_4\) the representation is a nontrivial linear character plus a plane representation induced from a character of the cyclic group of order four. In \(A_4\) it is induced from a nontrivial character of the Klein four-group. In \(S_4\), restriction to the normal Klein four-group splits into its three nontrivial characters; the group permutes the three eigenlines and the standard representation is induced by the linear action of the stabilizer of one line. These induced one-dimensional representations have entire Hecke completions. The functional-equation sign is one by division of the two Dedekind functional equations.

With \(C=\sqrt{|\Delta|}/\pi^{3/2}\), set
\[
 F(s)=C^s\Gamma(s/2)^{3-r}\Gamma((s+1)/2)^r L(s)
             \exp((s-1/2)^2/36).
\]
The quotient gamma factors follow by duplication, up to a positive constant independent of \(s\). Thus \(F(1-s)=F(s)\). On GRH the symmetric completed logarithmic derivative gives
\[
 B_K=2+\gamma_E-\log(4\pi)+2\big(F'(1)/F(1)-1/36\big).
\]
The residue theorem and symmetry give absolutely convergent vertical integrals on \(s=8+it\) for \(F(1)\) and \(F'(1)\), respectively:
\[
 (2\pi)^{-1}\int_\mathbb R F(8+it)k_j(8+it)\,dt,\quad
 k_0(s)=\frac1{s-1}+\frac1s,\qquad
 k_1(s)=\frac1{(s-1)^2}-\frac1{s^2}.
\]
Indeed reflect the left contour at \(\Re s=-7\) through the functional equation. The Gaussian factor yields decay on the horizontal segments by the standard vertical strip growth bounds for completed Hecke L-functions.

The checker samples \(t=jh\) with \(h=1/4\), \(|j|\le240\), and folds conjugates. Define
\[
 A(\sigma)=2 C^\sigma\Gamma(\sigma/2)^{3-r}
   \Gamma((\sigma+1)/2)^r\zeta(\sigma)^3 e^{(\sigma-1/2)^2/36}.
\]
For each \(\sigma\ge2\) either integrand has modulus at most \(A(\sigma)e^{-t^2/36}\), by the gamma integral and absolute Euler bound. Poisson summation and contour displacement by six in the ordinate variable therefore bound the infinite trapezoid error, after division by \(2\pi\), by
\[
 \frac{6\sqrt\pi\,[A(2)+A(14)]}{2\pi(e^{12\pi/h}-1)} .
\]
For \(T=240h\), comparison with the Gaussian integral bounds the omitted samples by \(36 A(8)e^{-T^2/36}/(2\pi T)\). Truncating the Dirichlet series at \(N\) adds an absolute error at most
\[
 \frac{2C^8\Gamma(4)^{3-r}\Gamma(9/2)^r\, e^{(15/2)^2/36}
       \zeta(5/4)^3\,(h+6\sqrt\pi)}{2\pi N^{27/4}} .
\]
Here \(\sum_{n>N}|a_n|n^{-8}\le N^{-27/4}\zeta(5/4)^3\). All three analytic errors are added to numerator and denominator independently. Exact coefficients come from PARI's ideal counts divided as a Dirichlet series by \(\zeta\). All complex gamma values, phases and comparisons use 160-bit Arb balls. The code requires a strictly positive resulting denominator and a strict separation of \(B_K\) from 2. The integral and error bounds have no GRH dependence; the interpretation as the positive spectral sum uses GRH.

## Replay

Download and decompress T40.gp.gz, T42.gp.gz and T44.gp.gz from the Bordeaux data directory into a local directory named tables. With python-flint and PARI/GP installed, run the following from the repository root. The optional PARI_GP environment variable specifies the GP executable.

```sh
mkdir -p quartic-replay
python scripts/check_zhao_quartic_tables_nov18.py --table-dir tables --output-dir quartic-replay
python scripts/check_zhao_quartic_fields_nov18.py --enumeration-cache quartic-replay --output-dir quartic-replay
python scripts/check_zhao_quartic_contour_nov18.py --input-dir quartic-replay --output quartic-replay/fields.json
```


The same list of 871 fields is the entire unconditional classification of \(2\Xi'_K(1)/\Xi_K(1)<2\), verified separately on all 81,145 candidates using larger discriminant bounds valid throughout the critical strip. Every one of these fields has no nontrivial real zero. [Unconditional classification and replay](zhao-low-degree-unconditional-nov18.md)
