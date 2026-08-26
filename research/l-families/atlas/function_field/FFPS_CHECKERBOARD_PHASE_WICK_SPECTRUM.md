# The checkerboard phase-Gram Wick spectrum

Status: **exact formal product-Gram theorem; no growing-source realization,
global moment, CYSEL, RH, or GRH claim**

Exact replay:
[ffps_checkerboard_phase_wick_spectrum.py](ffps_checkerboard_phase_wick_spectrum.py)

## 0. Outcome

The global parity mask has two very different Wick ledgers.

1. Its selected covariance contains one rank-one character and needs the
   constant sharp diagonal repair 1.
2. The *restricted additive phase Gram* retains almost its entire native
   atomic diagonal after Wick centering.

The second statement is exact and asymptotically sharp.  Let
\(p_1,\ldots,p_d\) be distinct primes congruent to \(1\bmod4\), and put

\[
 m_i={p_i-1\over2},\qquad q_i={p_i+1\over2},
\]

\[
 M=\prod_i m_i,\qquad Q=\prod_iq_i,\qquad
 P=\prod_ip_i,\qquad D_0=\prod_i(p_i-1)=2^dM.
\tag{0.1}
\]

On the complete square-phase tensor the Gram is

\[
 G=\bigotimes_{i=1}^d(p_iI-J).
\tag{0.2}
\]

Restrict it to one global checkerboard half
\(A=\ker(\tau_1\cdots\tau_d)\), where \(\tau_i\) is the unique quadratic
character of the sign-pair group.  Its constant row sum and sharp hard
leverage are

\[
 \mu_{\rm pr}={P+Q\over2},\qquad
 L_{\rm cb}={4M\over P+Q}.
\tag{0.3}
\]

The smallest eigenvalue of the restricted Gram is

\[
 \boxed{
 \mu_{\min}
 =\min_{S\subseteq[d]}
 {1\over2}\left(
 \prod_{i\in S}p_i\prod_{i\notin S}q_i+
 \prod_{i\in S}q_i\prod_{i\notin S}p_i
 \right).}
\tag{0.4}
\]

Therefore the exact smallest scalar which makes the phase-Wick matrix
positive is

\[
 \boxed{
 r_{\rm phase}
 =\max\{0,D_0-\mu_{\min}\},\qquad
 G_A-D_0I+r_{\rm phase}I\succeq0.}
\tag{0.5}
\]

For every growing distinct-prime panel,

\[
 \boxed{
 {r_{\rm phase}\over D_0}\longrightarrow1.}
\tag{0.6}
\]

More explicitly,

\[
 {L_{\rm cb}\over L_{\rm full}}
 ={4Q\over P+Q}
 \le4\left({3\over5}\right)^d,
\tag{0.7}
\]

whereas

\[
 \boxed{
 {r_{\rm phase}\over D_0}
 \ge
 1-{d+2\over2}
 \left({3\over5}\right)^{\lfloor d/2\rfloor}.}
\tag{0.8}
\]

Thus the formal leverage improvement is exponential while the normalized
phase-diagonal repair tends to one.  This is the precise **Wick--leverage separation theorem**:

> A one-line selected sheaf and an excellent uncentered restricted frame do
> not make the native additive phase energy cheap after Wick subtraction.

At the smallest two-prime physical control \((5,13)\),

\[
 \operatorname{Spec}(G_A)=\{37,43,52,52,52,52\},
\quad D_0=48,
\quad r_{\rm phase}=11.
\tag{0.9}
\]

The restricted leverage is \(24/43<4/7\), but the centered phase form already
has a negative eigenvalue \(-11\).

## 1. Frozen dependencies

| source | commit | blob | role |
|---|---|---|---|
| FFPS_CORRELATED_MASK_AMPLIFIER.md | 6e4609dfe | 4569c521e99e8c591f1694126605f8abee8a75f8 | product Gram and checkerboard leverage |
| FFPS_FINITE_ABELIAN_SUBGROUP_MASK_COMPRESSION.md | 9e116ec41 | 19d0ce572fcd70e68b1618462bea29a2958b7f9e | one-line selected covariance and direct (5,13) control |
| FFPS_WICK_CENTERED_DOMINATION_BOUNDARY.md | e2d8ded9e | 47ff1430d4d0a55580ade3d36489ef3cd5cee7a7 | selected-covariance repair 1 |

The theorem below concerns the formal tensor Gram (0.2).  The frozen FFPS
source realizes only the bilateral two-prime checkerboard.  In particular,
(0.6)--(0.8) are not claims that a growing-\(d\) native number-field source
has already been constructed.

## 2. Complete and restricted spectra

Write \(H_i=\mathbf F_{p_i}^{\times}/\{\pm1\}\).  Fourier characters
diagonalize \(p_iI-J\).  The local eigenvalue is

\[
 \lambda_i(\chi_i)=
 \begin{cases}
 q_i,&\chi_i=\mathbf1,\\
 p_i,&\chi_i\ne\mathbf1.
 \end{cases}
\tag{2.1}
\]

Hence \(G\) has eigenvalue
\(\lambda_\chi=\prod_i\lambda_i(\chi_i)\).
Characters of the index-two subgroup \(A\) are the pairs
\(\{\chi,\chi\tau\}\), with
\(\tau=\tau_1\cdots\tau_d\).  Restricting the convolution kernel to \(A\)
gives the exact eigenvalue

\[
 \boxed{\mu_{\{\chi,\chi\tau\}}
 ={1\over2}(\lambda_\chi+\lambda_{\chi\tau}).}
\tag{2.2}
\]

The principal/top pair gives (0.3).  To minimize (2.2), no coordinate needs
to have \(\chi_i\notin\{\mathbf1,\tau_i\}\).  Indeed such a coordinate
contributes the common factor \(p_i\).  Replacing it by either
\(\mathbf1\) or \(\tau_i\), and choosing the better of the two orientations,
does no worse because the average of those two candidate values replaces
\(2p_i\) by \(p_i+q_i<2p_i\).

It remains only to decide, for every coordinate, whether \(\chi_i\) is
principal or top.  Calling the top set \(S\) gives (0.4).  The two
complementary subsets describe the same restricted character.

The literal diagonal of every principal submatrix of \(G\) is \(D_0\).
Subtracting it translates every eigenvalue by \(-D_0\), proving (0.5).
This repair belongs to the *phase Gram*.  It is not the repair of the
selected covariance identity, whose sharp coefficient remains exactly one.

## 3. The asymptotic separation

Because \(p_i\ge5\),

\[
 {q_i\over p_i}={p_i+1\over2p_i}\le{3\over5}.
\tag{3.1}
\]

Choose any subset \(S\) of size \(\lfloor d/2\rfloor\) in (0.4).  Factoring
out \(P\) yields

\[
 \mu_{\min}
 \le {P\over2}\left[
 \left({3\over5}\right)^{|S|}
 +\left({3\over5}\right)^{d-|S|}
 \right]
 \le P\left({3\over5}\right)^{\lfloor d/2\rfloor}.
\tag{3.2}
\]

After ordering the distinct primes, \(p_i\ge i+2\).  Therefore

\[
 {D_0\over P}
 =\prod_i\left(1-{1\over p_i}\right)
 \ge\prod_{i=1}^d{i+1\over i+2}
 ={2\over d+2}.
\tag{3.3}
\]

Equations (3.2)--(3.3) prove (0.8), hence (0.6).  Separately,
\(Q/P\le(3/5)^d\), which proves (0.7).

No prime number theorem or unproved distribution statement is used.

## 4. Why this matters for the source programme

The formal checkerboard has an unusually favorable triple:

\[
 (\text{selected rank},\text{selected mass},
 \text{selected-covariance repair})=(1,1,1).
\]

The telescoping curve model further shows that this one line can have small
maximally extended Betti cost.  Equation (0.6) identifies a different
obstruction: the additive phase frame being used to dominate the hard
observation becomes almost maximally indefinite after its native atomic
diagonal is removed.

This explains why three previously tempting statements do not combine:

1. hard restriction improves the uncentered inverse Gram;
2. the selected quotient is a single rank-one sheaf;
3. literal Wick atoms can be removed from the final principal identity.

All three are true, but the phase-Gram inequality pays (0.5) when it is
centered.  A successful global argument must therefore use signed
source-level recombination, a new off-diagonal estimate, or an arithmetic
identity which cancels the phase repair.  Positivity of the restricted Gram
alone cannot do this.

The theorem does not rule out the hard-mask route.  It rules out one specific
shortcut: applying the uncentered restricted-frame constant after Wick
subtraction while retaining only the constant selected-covariance repair.

## 5. Proof ledger

| statement | grade |
|---|---|
| complete product spectrum (2.1) | **PROVED EXACT** |
| restricted checkerboard spectrum (2.2) | **PROVED EXACT** |
| subset formula for \(\mu_{\min}\) (0.4) | **PROVED EXACT** |
| sharp phase-Wick repair (0.5) | **PROVED EXACT FORMAL GRAM** |
| asymptotic separation (0.6)--(0.8) | **PROVED EXACT/INEQUALITY** |
| direct (5,13) spectrum (0.9) | **REPLAYED EXACT** |
| growing-\(d\) physical FFPS source | **OPEN** |
| cancellation of the phase repair in the native source | **OPEN / CENTRAL** |
| WCADD, WCKUM, CYSEL, RH, or GRH | **OPEN / UNPROVED** |

No external novelty or priority claim is made.

## 6. Reproduction

The replay uses exact integers and rational numbers.  It scans the subset
formula for eight small prime-prefix panels and explicitly diagonalizes the
restricted character spectrum only on tiny controls.  It enumerates no
conductor family, curve, L-function, or zero.

~~~powershell
python research/l-families/atlas/function_field/ffps_checkerboard_phase_wick_spectrum.py --check
python -O research/l-families/atlas/function_field/ffps_checkerboard_phase_wick_spectrum.py --check
python -m unittest tests.test_ffps_checkerboard_phase_wick_spectrum
python -O -m unittest tests.test_ffps_checkerboard_phase_wick_spectrum
python -m ruff check research/l-families/atlas/function_field/ffps_checkerboard_phase_wick_spectrum.py tests/test_ffps_checkerboard_phase_wick_spectrum.py
python -m ruff format --check research/l-families/atlas/function_field/ffps_checkerboard_phase_wick_spectrum.py tests/test_ffps_checkerboard_phase_wick_spectrum.py
~~~
