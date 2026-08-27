# The complete genus-zero base-wavelet shadow has an exact cubic Euler notch

Status: **exact all-degree theorem for the complete \(u=1\) polynomial-norm
shadow over \(\mathbf F_q[T]\); exact bivariate coefficient recurrence and
bounded replay; no incomplete-family, positive-genus, WAVEPRIMCAR, RH, or
number-field theorem**

Bounded exact replay:
[function_field_basewave_shadow.py](function_field_basewave_shadow.py).
Canonical summary:
[function_field_basewave_shadow.json](function_field_basewave_shadow.json).

Frozen dependencies at b870366141fe8d5f43d5b81f6e50a67d2a888070:

| source | git blob | role |
|---|---|---|
| FFPS_PRIMITIVE_RHO_TILT_CONVOLUTION_ISOMORPHISM.md | 31311893b8a7ba708ae7a2813b9c44b920b788a9 | the \(u=1\) divisor wavelet and its exceptional-prime-free cofactor sum |
| FFPS_BOUNDARY_FIELD_NEAR_CORRELATION_CRITERION.md | 105837343b6b8ef148488f492c66da8feae0334a | compact autocorrelation and ratio support |
| ffps_boundary_field_near_correlation_criterion.py | 53b5a710cb2f6b918958ff7e96801d81e2a0a79c | finite autocorrelation conventions |

## 0. Outcome

The most literal complete \(\mathbf F_q[T]\) shadow of the \(u=1\) divisor
wavelet is not merely subpower. It decays exponentially in the degree height.

Fix a monic irreducible polynomial \(\pi\) of degree \(e\), an exceptional
orientation \(\alpha\geq0\), and a finitely supported sampled ratio kernel
\(r_k\). For \(h\geq0\), define

\[
 \mathcal S_h^{\alpha}
 =\sum_{\substack{A,B\ {\rm monic\ squarefree}\\
                   (A,B)=1,\ \pi\nmid AB\\
                   \max(\alpha e+\deg A,\deg B)=h}}
 {\mu(A)\mu(B)\over q^{(\deg A+\deg B)/2}}
 r_{\alpha e+\deg A-\deg B}.
\tag{0.1}
\]

This is exactly what results from writing the squarefree product \(N=AB\),
summing all divisor orientations \(A\mid N\), taking \(u=1\), and replacing
integer absolute value by polynomial norm. Because \(q\geq3\), a
multiplicative interval \((H,2H]\) contains at most one polynomial norm
\(q^h\); hence (0.1) is the native complete norm shell rather than a further
smoothing.

### Theorem

For fixed \(q,e,\alpha\) and \(r_k\), and every \(\varepsilon>0\),

\[
 \boxed{
 \mathcal S_h^\alpha
 =O_{q,e,\alpha,r,\varepsilon}
 \left(q^{-(1/3-\varepsilon)h}\right).}
\tag{0.2}
\]

The meaningful range is \(0<\varepsilon<1/3\); larger values follow after
enlarging the constant. In particular,

\[
 \sum_{h\geq0}|\mathcal S_h^\alpha|^2<\infty.
\tag{0.3}
\]

Thus the complete genus-zero base-wavelet shadow satisfies every subpower
shell bound. This does **not** prove WAVEPRIMCAR: it omits nontrivial cores,
the harmonic \(d\)-average, incomplete Boolean/owner restrictions, and every
nonzero incidence mode.

The mechanism is exact. The two one-sided Möbius channels and their shared
diagonal produce the three Euler zeros

\[
 (1-\sqrt qX)(1-\sqrt qY)(1-XY).
\tag{0.4}
\]

In particular, the degree-zero Fourier channel is a notch \(1-XY\), not a
main-term pole.

## 1. Exact oriented Euler product

Let

\[
 c_{i,j}
 =\sum_{\substack{A,B\ {\rm monic\ squarefree}\\
                   (A,B)=1,\ \pi\nmid AB\\
                   \deg A=i,\ \deg B=j}}
 {\mu(A)\mu(B)\over q^{(i+j)/2}}.
\tag{1.1}
\]

At every irreducible \(P\neq\pi\), there are three choices: absent, assigned
to \(A\), or assigned to \(B\). Therefore

\[
 \boxed{
 F_{q,e}(X,Y)
 :=\sum_{i,j\geq0}c_{i,j}X^iY^j
 =\prod_{P\neq\pi}
 \left(1-q^{-\deg P/2}X^{\deg P}
         -q^{-\deg P/2}Y^{\deg P}\right).}
\tag{1.2}
\]

No polynomial enumeration is needed. If

\[
 I_q(d)={1\over d}\sum_{m\mid d}\mu(m)q^{d/m},
 \qquad
 J_{q,e}(d)=I_q(d)-\mathbf 1_{d=e},
\tag{1.3}
\]

then the unweighted product

\[
 G_{q,e}(x,y)=
 \prod_{d\geq1}(1-x^d-y^d)^{J_{q,e}(d)}
 =\sum b_{i,j}x^iy^j
\tag{1.4}
\]

has \(c_{i,j}=q^{-(i+j)/2}b_{i,j}\).

For \(r+s>0\), its logarithmic coefficient is

\[
 \lambda_{r,s}
 =-\sum_{d\mid\gcd(r,s)}
 {J_{q,e}(d)\over (r+s)/d}
 \binom{(r+s)/d}{r/d},
\tag{1.5}
\]

where \(\gcd(r,0)=r\). Applying the total Euler operator to
\(G=\exp(\log G)\) gives the exact triangular recurrence

\[
 \boxed{
 (i+j)b_{i,j}
 =\sum_{\substack{0\leq r\leq i,\ 0\leq s\leq j\\r+s>0}}
 (r+s)\lambda_{r,s}b_{i-r,j-s}.}
\tag{1.6}
\]

The replay computes (1.6) through bidegree \(35\) for \(q=3,5,7\) and
checks it independently against the truncated product (1.4) through
bidegree \(8\). Every coefficient produced by the rational recurrence is
integral. On an axis, the product collapses exactly to

\[
 G_{q,e}(x,0)={1-qx\over1-x^e},
\tag{1.7}
\]

which supplies a second all-degree check.

## 2. Exact factorization and the diagonal notch

For one irreducible of degree \(d\), put

\[
 a=q^{-d/2}X^d,
 \qquad b=q^{-d/2}Y^d.
\]

The elementary identity

\[
 (1-a)(1-b)(1-ab)-(1-a-b)=ab(a+b-ab)
\tag{2.1}
\]

shows that

\[
 1-a-b=(1-a)(1-b)(1-ab)\mathcal J_d(a,b),
\tag{2.2}
\]

where

\[
 \mathcal J_d(a,b)
 ={1-a-b\over(1-a)(1-b)(1-ab)}
 =1+O(a^2b+ab^2).
\tag{2.3}
\]

The monic-prime Euler identity

\[
 \prod_P(1-z^{\deg P})=1-qz
\tag{2.4}
\]

then gives

\[
 \boxed{
 F_{q,e}(X,Y)=
 { (1-\sqrt qX)(1-\sqrt qY)(1-XY)
  \over
   (1-q^{-e/2}X^e)(1-q^{-e/2}Y^e)
   (1-q^{-e}(XY)^e)}
 \mathcal J_{q,e}(X,Y),}
\tag{2.5}
\]

with

\[
 \mathcal J_{q,e}(X,Y)=
 \prod_{P\neq\pi}\mathcal J_{\deg P}
 \left(q^{-\deg P/2}X^{\deg P},
       q^{-\deg P/2}Y^{\deg P}\right).
\tag{2.6}
\]

Equation (2.5) identifies the complete diagonal channel. The mixed local
term \(ab\), which might have generated a diagonal pole after the orientation
sum, instead contributes the exact inverse-zeta zero \(1-XY\). Removing one
exceptional prime divides by \(1-q^{-e}(XY)^e\), which is nonzero at
\(XY=1\); the notch survives.

## 3. Convergence and proof of the shell theorem

Fix \(r<q^{1/6}\) and \(|X|,|Y|\leq r\). For an irreducible of degree \(d\),

\[
 |a|,|b|\leq (r/\sqrt q)^d.
\]

By (2.3), on every smaller closed bidisc there is a constant \(C\) with

\[
 |\mathcal J_d-1|
 \leq C\left({r^3\over q^{3/2}}\right)^d.
\tag{3.1}
\]

Using \(I_q(d)\leq q^d/d\),

\[
 \sum_{d\geq1}I_q(d)|\mathcal J_d-1|
 \ll\sum_{d\geq1}{1\over d}
 \left({r^3\over\sqrt q}\right)^d<\infty.
\tag{3.2}
\]

Thus \(\mathcal J_{q,e}\), and hence \(F_{q,e}\), is analytic on every closed
bidisc with radius \(r<q^{1/6}\). Cauchy's estimate gives

\[
 |c_{i,j}|\leq C_{q,e,r}r^{-(i+j)}.
\tag{3.3}
\]

Let the sampled kernel be supported on \(|k|\leq K\). On the degree-\(h\)
shell, a surviving pair obeys

\[
 \max(\alpha e+i,j)=h,
 \qquad |\alpha e+i-j|\leq K,
\]

and therefore

\[
 i+j\geq2h-K-\alpha e.
\tag{3.4}
\]

There are at most \(2K+1\) such bidegrees. Equations (3.3)--(3.4) yield

\[
 |\mathcal S_h^\alpha|
 \ll r^{-2h+K+\alpha e}.
\tag{3.5}
\]

Taking \(r=q^{1/6-\delta}\) proves (0.2).

## 4. What is special about this shadow

The theorem is useful precisely because its strength diagnoses a degeneracy.

1. Polynomial norm ratios retain only the integer
   \(\deg A-\deg B\). The archimedean continuum inside an integer ratio shell
   has disappeared.
2. The complete monic genus-zero family has inverse zeta polynomial
   \(1-qu\). This makes all three factors in (0.4) exact finite zeros.
3. All monic polynomials of the permitted degrees are summed before a norm is
   taken. Owner restrictions, Boolean incidence, fixed cores, and source
   truncations can destroy (1.2).

For a positive-genus curve \(C\),

\[
 \prod_{x\in|C|}(1-u^{\deg x})={1\over Z_C(u)}
 ={(1-u)(1-qu)\over P_C(u)},
\tag{4.1}
\]

and the Frobenius polynomial \(P_C\) adds genuine reciprocal-root channels.
The residual factorization then requires a new pole/zero audit. Nothing in
(0.2) predicts that those channels cancel. Likewise, this packet gives no
number-field estimate: integer ratios vary within each logarithmic shell,
and the integer Euler product does not collapse to (2.4).

The correct next function-field experiment is therefore not another
genus-zero coefficient row. It is one of:

- insert a positive-genus Frobenius numerator into (2.5) and classify the
  first surviving reciprocal-root channel;
- retain one exact owner/Boolean restriction and determine which of the
  three zeros in (0.4) it destroys;
- add the harmonic sieve variable \(d\) and prove a uniform Euler deletion
  bound before summing cores.

## 5. Proof ledger

| statement | grade |
|---|---|
| orientation Euler product (1.2) | **PROVED EXACT** |
| irreducible-degree recurrence (1.5)--(1.6) | **PROVED EXACT** |
| recurrence/product agreement through bidegree \(8\) | **REPLAYED EXACT FOR \(q=3,5,7\)** |
| local cubic factorization (2.1)--(2.3) | **PROVED EXACT** |
| global three-zero factorization (2.5) | **PROVED EXACT FROM THE MONIC PRIME EULER IDENTITY** |
| residual convergence for \(r^3<\sqrt q\) | **PROVED BY ABSOLUTE EULER-PRODUCT MAJORIZATION** |
| complete-shell decay (0.2) | **PROVED BY CAUCHY** |
| finite control amplitudes through degree \(35\) | **REPLAYED EXACT IN \(\mathbf Q(\sqrt q)\)** |
| positive-genus analogue | **OPEN / NOT INFERRED** |
| incomplete owner/Boolean analogue | **OPEN / NOT INFERRED** |
| WAVEPRIMCAR, PRIMCAR, RH, or GRH | **NOT PROVED** |

The finite control kernel in the replay is the degree-lattice autocorrelation
\((1,2,3,2,1)\). It is not asserted to equal the sampled analytic kernel.
The theorem itself is uniform over every fixed finite sampled kernel, so no
numerical value of the analytic autocorrelation enters the proof.

## 6. Bounded replay

~~~text
python -B research/l-families/atlas/function_field/function_field_basewave_shadow.py --check
python -B -O research/l-families/atlas/function_field/function_field_basewave_shadow.py --check
python -B -m unittest tests.test_function_field_basewave_shadow
python -B -O -m unittest tests.test_function_field_basewave_shadow
python -B -m ruff check research/l-families/atlas/function_field/function_field_basewave_shadow.py tests/test_function_field_basewave_shadow.py
python -B -m ruff format --check research/l-families/atlas/function_field/function_field_basewave_shadow.py tests/test_function_field_basewave_shadow.py
~~~

The replay uses irreducible-degree counts and bivariate dynamic programming
only. It enumerates no polynomial, point, curve, zero, or \(L\)-function.
