# Complete theta-integral enclosure for one four-by-four trace-Hankel matrix

**Proposed finite certificate; independent code and mathematical review pending.** The calculation uses the literal theta density in PROOF.md (1), not a finite theta truncation as a substitute function. It is not an RH proof or a zero census.

The exact output is `moments.json`. Every interval is a pair of decimal strings representing integer endpoints in units $2^{-512}$. Human-readable decimal fields are outward displays only. The accepting command reconstructs the entire output before comparing strict types and values:

```sh
python -I -S -B theta_moments.py --check moments.json
python -I -S -B -O theta_moments.py --check moments.json
```

## 1. Arithmetic primitives

Integer division uses floor and ceiling toward the indicated infinite direction, including for negative numerators. Interval multiplication considers all four endpoint products. Reciprocal operations reject a denominator interval containing zero. Integer powers correctly handle an even power of an interval crossing zero. Rational scaling rounds both endpoints outward. No floating-point number is accepted in the receipt.

Pi is enclosed by the classical Machin identity $\pi=16\arctan(1/5)-4\arctan(1/239)$. Each arctangent uses 192 alternating terms. This ends on a negative term, and the omitted remainder is between zero and $1/(385n^{385})$ for inverse argument $1/n$. Arithmetic rounding widens the interval further.

For an exact nonnegative rational $x$, scale by a power of two until $0\le u\le1/16$. Sum the exponential series through degree 128, with omitted remainder at most $2u^{129}/129!$. Repeated outward squaring reconstructs $e^x$. Negative arguments use the reciprocal of the positive enclosure. Interval exponential evaluation uses monotonicity at both rational endpoints.

Independent bounded arithmetic tests use a different pi identity, $\pi=4(\arctan(1/2)+\arctan(1/3))$, with 512 terms per arctangent. Exponential controls use unreduced exact rational Taylor sums through degree 256. These test the implementation at declared finite inputs; they do not substitute for the written primitive remainder proofs.

## 2. Cell Taylor integration

Even raw moments through degree 14 are twice the integrals on $t\ge0$. On $[0,3]$ take 96 cells of width $1/32$, with centers $c=(2j+1)/64$, half-width $h=1/64$. Retain the first eight literal positive-time theta terms explicitly and enclose all subsequent terms analytically.

For one term put $q=\pi n^2e^{2c}$ and

$$f(v)=\exp(5v/2-qe^{2v})=\sum_{k\ge0}f_kv^k.$$

Then, exactly,

$$k f_k=\tfrac52f_{k-1}-2q\sum_{j=0}^{k-1}\frac{2^j}{j!}f_{k-1-j},\qquad f_0=e^{-q}.$$

The theta coefficient of order $j$ at $c$ is

$$\pi n^2e^{5c/2}\bigl[-f_j-2(j+1)f_{j+1}\bigr].$$

This follows from $-f-2f'=(4qe^{2v}-6)f$ and agrees with both terms of the defining density. The program computes $f$ through degree 97, builds the theta coefficients through degree 96, multiplies by $(c+v)^k$, and integrates every retained monomial of **total degree at most 96**. Odd monomials integrate to zero; an even degree $j$ has exact integral $2h^{j+1}/(j+1)$. Pi, exponential and coefficient errors remain interval-valued throughout.

A cell-term is skipped only when the lower enclosure of $\pi n^2e^{2(c-h)}$ is at least 300; Section 5 bounds all those skipped real integrals. The frozen run has 247 explicitly computed and 521 analytically bounded cell-terms. Their sum is $96\cdot8$.

## 3. Uniform bound for every complex Taylor remainder

Use a complex circle of radius $r=1/8$ around every center. It lies in $|\Re z|<25/8$, $|z|<4$, $|\Im z|\le1/8$. Hence $\Re(e^{2z})=e^{2\Re z}\cos(2\Im z)>0$ and

$$|e^{-\pi n^2 e^{2z}}|\le1.$$

Uniformly for any subset of $1\le n\le8$, the sum of the absolute prefactors is less than $2^{50}$. For example, use $\pi<4$, $\sum_{n\le8}n^4\le8^5$, $\sum n^2\le8^3$, and $e^{15}<3^{15}$. Multiplication by $z^k$, $k\le14$, gives a bound $2^{78}$.

The Cauchy coefficient bound therefore gives the complete remainder after total degree 96 on $|v|\le h$:

$$|\mathrm{remainder}|\le 2^{78}\frac{(h/r)^{97}}{1-h/r}<2^{-212}.$$

Total integration length 3 and the reflection factor 2 make the total raw-moment Taylor error less than $2^{-209}$. This applies to the actual subset of unskipped terms in each cell. It does not require the two individually divergent full-line Volterra pieces or any asymptotic quadrature assertion.

## 4. All omitted theta indices

For $n\ge9$ and $t\ge0$, discard the negative theta prefactor for an upper bound and use $e^{2t}\ge1+2t$. The reflected raw moment tail is at most

$$8\pi^2k!\sum_{n\ge9}\frac{n^4e^{-\pi n^2}}{(2\pi n^2-9/2)^{k+1}},\qquad 0\le k\le14.$$

Since $2\pi n^2-9/2>5n^2$, and $k!\le(5n^2)^k$ in this range, this is below $26\sum_{n\ge9}n^2e^{-3n^2}$. The successive term ratio is below $1/2$, so it is below $4212e^{-243}<2^{-311}$. Here $e^3>16$, already implied by its first five positive Taylor terms. In particular the entire missing index tail is less than $2^{-300}$.

This bounds those indices over **all positive time**, including the time beyond 3. No numerical extrapolation in the theta index is used.

## 5. The complete remaining time tail and skipped cells

For $t=3+u$, $u\ge0$, $e^6>400$. This follows from $\sum_{j=0}^{8}3^j/j!=89641/4480>20$. Thus $q_n=\pi n^2e^6>1200n^2$. Also

$$t^k\le3^ke^{ku/3},\qquad e^{2t}\ge e^6(1+2u).$$

For $1\le n\le8$, the reflected positive raw integrand is bounded by

$$8\pi^2n^4 3^k e^{27/2-q_n}\exp[-(2q_n-9/2-k/3)u].$$

Integrating and summing gives a bound below $2^{68}e^{-1200}<2^{-1500}$, using the same elementary integer and exponential estimates. This is the **entire** $t>3$ tail of the first eight terms.

On a skipped cell $\pi n^2e^{2t}\ge300$. On $[0,3]$, all prefactors together are bounded by $2^{50}$ and $t^k\le3^{14}<2^{23}$. The complete union of skipped-cell integrals, including reflection, is consequently below $2^{76}e^{-300}<2^{-324}$.

Combining Taylor remainder, omitted index tail, time tail and skipped-cell bounds gives an absolute analytic error below $2^{-208}$ for every selected raw moment. The program deliberately adds the much larger symmetric error $[-2^{-190},2^{-190}]$ to each already outward-rounded raw integral. No rounding budget is being counted twice as an analytic bound; all numerical arithmetic errors have stayed in the interval operations.

## 6. Normalization, cumulants and positive definiteness

The raw zeroth moment interval is strictly positive and encloses

$$Z\in[0.497120778188314109912773739685397719807293609557,
0.497120778188314109912773739685397719807293609558].$$

Divide all raw moments by this interval; set $\mu_0=1$ exactly and odd moments to zero by full-source symmetry. Apply the full cumulant recurrence (19) of PROOF.md with outward arithmetic, and then the exact factorial factors (18) to obtain $s_1,\ldots,s_7$.

The program applies interval LDL to the **entire** $4\times4$ matrix $(s_{i+j+1})_{0\le i,j\le3}$. Each pivot interval has strictly positive lower endpoint. Dependency overestimation only widens these enclosures; no independence of repeated moment occurrences is presumed. By induction the exact pivots of the exact source matrix lie in the computed pivot intervals, so all divisions are justified and positive definiteness follows.

The exact accepting pivot and determinant endpoints are in `moments.json`. Coarse display bounds appear in PROOF.md. The leading determinant lies between $1.1775\cdot10^{-41}$ and $1.1777\cdot10^{-41}$. Its smallness is not loss of rigor: the source moment intervals and all subtractions are outward enclosed.

## 7. Acceptance contract and limitations

`--emit` is a producer operation. `--check` parses a finite, strict JSON schema, rejects duplicate keys, floating/nonfinite numbers and Boolean/integer aliases, checks the fixed coverage, regenerates the entire computation, then performs recursively type-strict equality. A changed numerical endpoint fails a fresh full reconstruction. A self-consistent false receipt is not accepted by rehashing alone.

The optional `verify_packet.py` separately checks the exact published regular-file inventory and byte hashes before invoking this numerical reconstruction. Integrity and arithmetic reconstruction are different checks. Neither claims an independently authored referee or a machine proof of the analytic tail lemmas.

No actual zero ordinate, zeta/gamma oracle, truncated zero sum, heuristic prime model, ordinary floating quadrature, Lean build or repository-wide validation enters acceptance. The one certified finite Hankel matrix is not the unbounded positivity tower required for RH.
