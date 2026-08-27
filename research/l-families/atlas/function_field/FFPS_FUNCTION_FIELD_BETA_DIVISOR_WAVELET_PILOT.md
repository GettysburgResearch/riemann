# A twisted function-field beta wavelet exposes its surviving Frobenius mode

Status: **exact beta/color adapter, exact twisted Witt--\(L\)
factorization, exact \(q=5\) low-degree replay, and a proved zero-frequency
Frobenius energy main term; no near-square, maximal-height, growing-sieve,
number-field WAVEPRIMCAR, RH, or GRH estimate**

Bounded producer:
[ffps_function_field_beta_divisor_wavelet_pilot.py](ffps_function_field_beta_divisor_wavelet_pilot.py).
Canonical output:
[ffps_function_field_beta_divisor_wavelet_pilot.json](ffps_function_field_beta_divisor_wavelet_pilot.json).

Frozen provenance: commit **3658d4c31**. The replay pins the complete
function-field divisor-Witt quartet, the complete beta/evaluation quartet,
and the elementary finite-field pilot used for the bounded polynomial
arithmetic.

## 0. Outcome

The complete untwisted function-field divisor wavelet has unusually strong
cancellation because every primitive binary color word collapses against
the affine polynomial zeta function. This packet asks what survives after
the same two-color wavelet is attached to:

1. the literal three-channel beta source at one exceptional place; and
2. a genuine quadratic evaluation character.

Let \(U\) be the affine line with the ramified places of a multiplicative
character \(\chi\) removed. Fix an unramified place \(\Pi\) of degree
\(e\), and put

\[
 (c_0,c_1,c_2)=(1,-2,1).
\tag{0.1}
\]

For a squarefree divisor \(M\) of \(U\), with \(\Pi\nmid M\), define the
source-faithful beta/color series

\[
\boxed{
\begin{aligned}
\mathscr B_{\Pi,\chi}(u,z)
=\sum_{\alpha=0}^{2}
&c_\alpha\chi(\Pi)^\alpha
 u^{\alpha e}z^{\alpha e}\\
&\times
\sum_{\substack{M\ {\rm squarefree}\\\Pi\nmid M}}
\mu(M)\chi(M)u^{\deg M}
\sum_{A\mid M}z^{\,2\deg A-\deg M}.
\end{aligned}}
\tag{0.2}
\]

The exponent \(\alpha e\) places the exceptional beta power on the left
color. This is the degree-lattice analogue of the three exceptional
orientations in the integer divisor wavelet. It is not an arbitrary
symmetrization.

At each ordinary place there are three coherent states: absent, assigned
left, or assigned right. Therefore

\[
\boxed{
\mathscr B_{\Pi,\chi}(u,z)
=
\bigl(1-\chi(\Pi)(uz)^e\bigr)^2
\prod_{R\neq\Pi}
\left(
1-\chi(R)(uz)^{\deg R}
 -\chi(R)(u/z)^{\deg R}
\right).}
\tag{0.3}
\]

The line break in (0.3) is typographical: the local factor is

\[
 1-\chi(R)(uz)^{\deg R}-\chi(R)(u/z)^{\deg R}.
\tag{0.4}
\]

Let

\[
 M(a,b)=
\frac1{a+b}
\sum_{d\mid\gcd(a,b)}
\mu(d)\binom{(a+b)/d}{a/d}
\tag{0.5}
\]

be the number of primitive binary necklaces of content \((a,b)\). Applying
the content-refined Witt identity at every place gives the exact formal
factorization

\[
\boxed{
\begin{aligned}
\mathscr B_{\Pi,\chi}(u,z)
=&
\frac{\bigl(1-\chi(\Pi)(uz)^e\bigr)^2}
 {1-\chi(\Pi)(uz)^e-\chi(\Pi)(u/z)^e}\\
&\times
\prod_{\substack{a,b\geq0\\a+b>0}}
L_U\!\left(
 u^{a+b}z^{a-b},\chi^{a+b}
\right)^{-M(a,b)}.
\end{aligned}}
\tag{0.6}
\]

This is the theorem-quality adapter. Primitive color-word length selects
the geometric channel:

\[
\boxed{
\text{word length }k
\quad\longmapsto\quad
L_U(v,\chi^k)^{-1}.}
\tag{0.7}
\]

For a quadratic character:

- odd word lengths retain the inverse quadratic \(L\)-function;
- even word lengths retain the inverse deleted-principal zeta channel.

The complete zero Fourier mode is obtained by setting \(z=1\). If

\[
 L_k(2)=\sum_{a+b=k}M(a,b),
\tag{0.8}
\]

then

\[
\boxed{
\mathscr B_{\Pi,\chi}(u,1)
=
\frac{(1-\chi(\Pi)u^e)^2}{1-2\chi(\Pi)u^e}
\prod_{k\geq1}
L_U(u^k,\chi^k)^{-L_k(2)}.}
\tag{0.9}
\]

Thus the zero mode is not automatically erased by coherent coloring. It is
a spectrum of inverse \(L\)-channels indexed by primitive color words.

## 1. Why the beta local vector is exactly \((1,-2,1)\)

For an effective divisor \(D=\alpha\Pi+M\), with \(\Pi\nmid M\), define

\[
 \beta_\Pi(D)=
 \mu(D)-\mathbf1_{\Pi\leq D}\mu(D-\Pi).
\tag{1.1}
\]

If \(M\) is squarefree, direct evaluation gives

\[
\begin{array}{c|ccc}
\alpha&0&1&2\\ \hline
\beta_\Pi(\alpha\Pi+M)/\mu(M)&1&-2&1.
\end{array}
\tag{1.2}
\]

For \(\alpha>2\), or when the core has a repeated place, the value is zero.
After twisting by \(\chi(D)\), the local exceptional polynomial is

\[
 1-2\chi(\Pi)(uz)^e+\chi(\Pi)^2(uz)^{2e}
 =\bigl(1-\chi(\Pi)(uz)^e\bigr)^2.
\tag{1.3}
\]

This proves that (0.2) is the literal beta pushforward, not merely a
three-term filter with the same coefficients.

## 2. Proof of the twisted Witt--\(L\) factorization

Put

\[
 X=uz,\qquad Y=u/z.
\tag{2.1}
\]

At a place \(R\), apply the two-letter Witt identity to
\(\chi(R)X^{\deg R}\) and \(\chi(R)Y^{\deg R}\):

\[
\begin{aligned}
1-\chi(R)X^{\deg R}-\chi(R)Y^{\deg R}
=\prod_{a,b}
\left(
1-\chi(R)^{a+b}
 X^{a\deg R}Y^{b\deg R}
\right)^{M(a,b)}.
\end{aligned}
\tag{2.2}
\]

Multiplying over all unramified \(R\) gives

\[
 \prod_R
 \left(1-\chi(R)^k v^{\deg R}\right)
 =L_U(v,\chi^k)^{-1}.
\tag{2.3}
\]

The product in (0.3) omits \(\Pi\). Restoring it inside every
\(L\)-factor divides by

\[
\prod_{a,b}
\left(
1-\chi(\Pi)^{a+b}
 X^{ae}Y^{be}
\right)^{M(a,b)}
=1-\chi(\Pi)X^e-\chi(\Pi)Y^e.
\tag{2.4}
\]

Multiplication by the exceptional beta square (1.3) proves (0.6). Every
step is a formal coefficient identity: a fixed coefficient of \(u^n\)
sees only finitely many word lengths and place degrees.

At \(z=1\), all contents of a fixed length \(k\) have the same argument
\(u^k\). Grouping their multiplicities gives (0.9).

## 3. A fully explicit \(q=5\) arithmetic fiber

The bounded arithmetic control uses

\[
 q=5,\qquad
 Q=T^3+T+1,\qquad
 \Pi=T.
\tag{3.1}
\]

The cubic \(Q\) has no root in \(\mathbf F_5\), hence it is irreducible.
Let

\[
 \chi(f)=\left(\frac{f}{Q}\right).
\tag{3.2}
\]

Euler's criterion in \(\mathbf F_{5^3}\) gives

\[
 \chi(\Pi)=1.
\tag{3.3}
\]

Complete sums over monic residue representatives of degrees zero, one,
and two give

\[
\boxed{
 L_Q(v,\chi)=1+3v+5v^2.}
\tag{3.4}
\]

For every degree \(n\geq3\), every residue class modulo \(Q\) occurs
equally often among monic degree-\(n\) polynomials. The nontrivial
character sum of the residue field is zero, so all later coefficients
vanish. Thus (3.4) is an exact \(L\)-polynomial, not an interpolation.

Its Frobenius eigenvalues are

\[
 \alpha,\beta=\frac{-3\pm\sqrt{-11}}2,
\qquad
 \alpha+\beta=-3,\qquad
 \alpha\beta=5.
\tag{3.5}
\]

In particular,

\[
 |\alpha|=|\beta|=\sqrt5.
\tag{3.6}
\]

No general function-field RH theorem is needed for this modulus; the
modulus follows directly from the exact quadratic polynomial.

The principal character on
\(\mathbf A^1\setminus\{Q\}\) has

\[
 L_U(v,1)=\frac{1-v^3}{1-5v},
\qquad
 L_U(v,1)^{-1}=\frac{1-5v}{1-v^3}.
\tag{3.7}
\]

Since

\[
 L_1(2)=2,\qquad L_2(2)=1,
\tag{3.8}
\]

the first two color lengths in the zero mode are

\[
 (1+3u+5u^2)^{-2}
 \frac{1-5u^2}{1-u^6}.
\tag{3.9}
\]

This already displays the mechanism: the two one-letter colors double the
quadratic Frobenius pole, while the balanced length-two word contributes a
principal-zeta zero.

## 4. The zero-mode main term is exact

For the fiber (3.1), equation (0.9) becomes

\[
\begin{aligned}
\mathscr B(u,1)
=&
\frac{(1-u)^2}{1-2u}
(1+3u+5u^2)^{-2}
\frac{1-5u^2}{1-u^6}
\mathcal H(u),
\end{aligned}
\tag{4.1}
\]

where the displayed line denotes a product and

\[
\boxed{
\begin{aligned}
\mathcal H(u)=&
\prod_{\substack{k\geq3\\k\ {\rm odd}}}
(1+3u^k+5u^{2k})^{-L_k(2)}\\
&\times
\prod_{\substack{k\geq4\\k\ {\rm even}}}
\left(\frac{1-5u^k}{1-u^{3k}}\right)^{L_k(2)}.
\end{aligned}}
\tag{4.2}
\]

The primitive-word bound

\[
 0\leq L_k(2)\leq\frac{2^k}{k}
\tag{4.3}
\]

shows that (4.2) converges normally on every closed disk
\(|u|\leq r<1/2\). For odd \(k\geq3\), the first possible
quadratic-\(L\) pole has radius

\[
 5^{-1/(2k)}>1/2.
\tag{4.4}
\]

For even \(k\geq4\), the first principal zero has radius
\(5^{-1/k}>1/2\), and the deleted-place denominators have radius one.
Therefore \(\mathcal H\) is holomorphic and nonzero throughout
\(|u|<1/2\).

The two roots of (3.4) have modulus \(5^{-1/2}<1/2\) in the \(u\)-plane.
Neither is canceled by:

- the exceptional factor, whose first denominator zero is \(u=1/2\);
- the length-two zero \(1-5u^2\), because the roots of
  \(1+3u+5u^2\) are nonreal;
- the nonvanishing tail (4.2).

Hence:

\[
\boxed{
\mathscr B(u,1)
\text{ has an exact double pole at }
u=\alpha^{-1},\beta^{-1}.}
\tag{4.5}
\]

Define the nonzero principal amplitudes

\[
\begin{aligned}
A_\alpha&=
\lim_{u\to\alpha^{-1}}
(1-\alpha u)^2\mathscr B(u,1),\\
A_\beta&=
\lim_{u\to\beta^{-1}}
(1-\beta u)^2\mathscr B(u,1)
=\overline{A_\alpha}.
\end{aligned}
\tag{4.6}
\]

If

\[
 b_n=[u^n]\mathscr B(u,1),
\tag{4.7}
\]

partial fractions on any disk

\[
 5^{-1/2}<r<1/2
\tag{4.8}
\]

give

\[
\boxed{
b_n=
n\bigl(A_\alpha\alpha^n+A_\beta\beta^n\bigr)
+O(5^{n/2}).}
\tag{4.9}
\]

The error includes the simple parts at the same two poles; the remainder
after removing both full principal parts is \(O_r(r^{-n})\), which is
exponentially smaller than \(5^{n/2}\).

Since \(\alpha/\beta\neq1\), summation of the oscillatory cross term loses
one power of the horizon. Consequently

\[
\boxed{
\sum_{n=0}^{H}
\left|5^{-n/2}b_n\right|^2
=
\frac{|A_\alpha|^2+|A_\beta|^2}{3}H^3
+O(H^2).}
\tag{4.10}
\]

The leading coefficient is strictly positive.

This is the surviving geometric constituent requested by the laboratory:
coherent divisor colors do not erase the quadratic Frobenius channel at
zero Fourier frequency. They square its inverse \(L\)-factor.

The polynomial growth in \(H\) remains subpower in the norm horizon
\(5^H\). Equation (4.10) is compatible with function-field RH and does not
imply an integer RH estimate.

## 5. Exact low-degree coefficient identities

Through total degree four, the bounded replay obtains the same Laurent
series in four independent ways:

1. enumerate the literal beta value
   \(\mu(F)-\mathbf1_{\Pi\mid F}\mu(F/\Pi)\);
2. split \(F=\Pi^\alpha M\) into the three beta channels and all divisor
   orientations of the squarefree core;
3. multiply the two-color Euler factors (0.3);
4. multiply the content-refined twisted Witt/\(L\) factors.

The zero-frequency coefficients are

\[
\boxed{
[u^n]\mathscr B(u,1)
=
1,-6,13,2,-120
\quad(0\leq n\leq4).}
\tag{5.1}
\]

The complete nonzero Laurent rows are:

| degree | phase \(j\) | coefficient of \(u^nz^j\) |
|---:|---:|---:|
| 0 | 0 | 1 |
| 1 | -1, 1 | -2, -4 |
| 2 | -2, 0, 2 | 2, 4, 7 |
| 3 | -3, -1, 3 | 5, -2, -1 |
| 4 | -4, -2, 0, 2, 4 | -24, -28, -14, -22, -32 |

These rows authenticate the adapter. The all-degree statements in Sections
2 and 4 are proved algebraically; they are not inferred from five
coefficients.

## 6. What this does and does not say about the divisor-wavelet gate

The exact mechanism is:

    literal beta orientations
      -> exceptional square (1-chi(Pi)X^e)^2;

    coherent divisor colors
      -> local state 1-chi(R)X^deg(R)-chi(R)Y^deg(R);

    primitive binary words
      -> inverse L(v,chi^word_length);

    quadratic twist
      -> odd lengths retain Frobenius;
      -> even lengths retain the principal deleted-zeta channel.

This tells a future number-field or sheaf argument what must be removed
before square-root cancellation is even plausible. At zero frequency, the
geometric mode is an explicit main term, not random error.

But \(z=1\) is the complete orientation sum. A sampled near-square kernel
is a Fourier integral or a finite phase functional of the full Laurent
series. A band-pass multiplier may vanish at zero. A maximal-height
supremum, a fixed nontrivial core, a harmonic sieve variable, and an
incomplete owner restriction all change the assembly. No conclusion about
those gates follows from (4.10) alone.

The next rigorous experiment should insert one finite degree-lattice
kernel \(\kappa(2\deg A-\deg M+\alpha e)\) and calculate its values on the
two length-one Frobenius channels. Only after those residues are subtracted
should growing-degree cancellation be conjectured.

## 7. Proof and scope ledger

| statement | grade |
|---|---|
| three-channel beta adapter | **PROVED EXACT** |
| literal beta/core/Euler equality | **PROVED EXACT** |
| twisted Witt--\(L\) factorization | **PROVED AS A FORMAL IDENTITY** |
| quadratic odd/even word selection | **PROVED EXACT** |
| \(L_Q(v,\chi)=1+3v+5v^2\) | **PROVED BY COMPLETE RESIDUE-CLASS SUMS** |
| Frobenius modulus in the frozen example | **PROVED FROM THE QUADRATIC DISCRIMINANT** |
| zero-mode continuation to \(|u|<1/2\) | **PROVED BY NORMAL CONVERGENCE** |
| exact double poles and coefficient law | **PROVED** |
| critical zero-mode energy main term | **PROVED** |
| finite near-square kernel theorem | **NOT INCLUDED** |
| maximal-height or growing-sieve estimate | **NOT PROVED** |
| number-field WAVEPRIMCAR | **NOT PROVED** |
| RH or GRH | **NOT PROVED** |

No external novelty claim is made without a dedicated literature search.

## 8. Bounded replay

The producer uses \(q=5\), one degree-three conductor, one degree-one
exceptional place, and total degree at most four. Each complete monic scan
contains only

\[
 1+5+5^2+5^3+5^4=781
\tag{8.1}
\]

polynomials. It replays 205 irreducibles and primitive words of length at
most four. It evaluates no zeta zero, numerical \(L\)-zero, curve, point,
random sample, floating-point fit, or large-degree family.

    python -B research/l-families/atlas/function_field/ffps_function_field_beta_divisor_wavelet_pilot.py --check
    python -B -O research/l-families/atlas/function_field/ffps_function_field_beta_divisor_wavelet_pilot.py --check
    python -B -m unittest tests.test_ffps_function_field_beta_divisor_wavelet_pilot
    python -B -O -m unittest tests.test_ffps_function_field_beta_divisor_wavelet_pilot
    python -B -m ruff check research/l-families/atlas/function_field/ffps_function_field_beta_divisor_wavelet_pilot.py tests/test_ffps_function_field_beta_divisor_wavelet_pilot.py
    python -B -m ruff format --check research/l-families/atlas/function_field/ffps_function_field_beta_divisor_wavelet_pilot.py tests/test_ffps_function_field_beta_divisor_wavelet_pilot.py
