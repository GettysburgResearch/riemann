# A Boolean evaluation restriction exposes the exact Frobenius residue left by the beta band-pass

Status: **exact literal-beta Euler identity, exact incomplete evaluation
projector, all-odd-\(q\) fixed-filter nonannihilation theorem, and exact
Frobenius-energy main term; no owner theorem, incomplete WAVEPRIMCAR,
number-field estimate, RH, or GRH theorem**

Bounded exact replay:
[function_field_beta_boolean_evaluation_bandpass.py](function_field_beta_boolean_evaluation_bandpass.py).
Canonical summary:
[function_field_beta_boolean_evaluation_bandpass.json](function_field_beta_boolean_evaluation_bandpass.json).

The packet is frozen to commit \(070be728e\). It imports the exact beta
source and fixed band-pass conventions from
[FFPS_BANDPASS_BETA_ENERGY_LADDER.md](FFPS_BANDPASS_BETA_ENERGY_LADDER.md)
and
[FFPS_ASSEMBLED_BETA_PERRON_FOURIER_BRIDGE.md](FFPS_ASSEMBLED_BETA_PERRON_FOURIER_BRIDGE.md),
and the complete function-field Euler algebra from
[FUNCTION_FIELD_BASEWAVE_SHADOW.md](FUNCTION_FIELD_BASEWAVE_SHADOW.md)
and
[FUNCTION_FIELD_BASEWAVE_CURVE_EXTENSION.md](FUNCTION_FIELD_BASEWAVE_CURVE_EXTENSION.md).
The producer pins both the Markdown and replay source of all four
dependencies by Git blob.

## 0. Outcome

This packet applies the literal beta source to a genuine incomplete
function-field family.

Let \(q\) be odd, let \(P\) and \(Q\) be distinct monic irreducibles in
\(\mathbf F_q[T]\), and put

\[
 e=\deg P,\qquad d=\deg Q.
\]

For a monic polynomial \(f\), define

\[
 \boxed{\beta_P(f)=\mu(f)-\mathbf 1_{P\mid f}\mu(f/P).}
\tag{0.1}
\]

Let \(\chi_Q(f)\) be the quadratic character of the evaluation
\(f\bmod Q\in\mathbf F_{q^d}\), extended by zero when \(Q\mid f\). For
\(\sigma\in\{+1,-1\}\), impose the hard Boolean restriction

\[
 \boxed{
 \delta_{\sigma,Q}(f)
 =\mathbf 1_{Q\nmid f,\ \chi_Q(f)=\sigma}
 ={1\over2}\mathbf 1_{Q\nmid f}
  +{\sigma\over2}\chi_Q(f).}
\tag{0.2}
\]

This is not the complete monic family and not merely a renamed coefficient
minor. It removes the conductor fibre and then keeps one of its two
evaluation squareclasses.

Let \(\mathcal B(z)\) be any fixed nonzero finite degree-lattice band-pass
polynomial. Define the filtered incomplete beta field by

\[
 \mathcal H_{\sigma,Q}(z)
 =\sum_{n\ge0}h_{\sigma,Q}(n)z^n
 =\mathcal B(z)
 \sum_{f\ {\rm monic}}
 {\beta_P(f)\delta_{\sigma,Q}(f)\over q^{\deg f/2}}
 z^{\deg f}.
\tag{0.3}
\]

Before restriction, the literal affine beta field is the polynomial

\[
 \boxed{
 \mathcal H_{\rm complete}(z)
 =\mathcal B(z)(1-q^{-e/2}z^e)(1-\sqrt q\,z).}
\tag{0.3a}
\]

It therefore vanishes identically beyond a fixed degree. Hard deletion of
\(Q\), without selecting an evaluation sign, changes this to

\[
 \boxed{
 \mathcal H_{Q{\rm -free}}(z)
 ={\mathcal B(z)(1-q^{-e/2}z^e)(1-\sqrt q\,z)
   \over1-q^{-d/2}z^d},}
\tag{0.3b}
\]

whose coefficients still decay exponentially. The genuine Boolean
squareclass selection is the step which changes the analytic boundary.
Its complete answer is

\[
\boxed{
\begin{aligned}
\mathcal H_{\sigma,Q}(z)
={\mathcal B(z)\over2}\bigg[
&{(1-q^{-e/2}z^e)(1-\sqrt q\,z)
  \over1-q^{-d/2}z^d}\\
&+\sigma\,
 {1-\chi_Q(P)q^{-e/2}z^e
  \over L_Q(z/\sqrt q,\chi_Q)}
\bigg].
\end{aligned}}
\tag{0.4}
\]

The first line is the trivial deleted channel. It is analytic on
\(|z|<\sqrt q\). The second line is a genuine inverse-\(L\) channel.

Write

\[
 L_Q(u,\chi_Q)=(1-u)^{\epsilon_Q}P_Q(u),\qquad
 \epsilon_Q=\mathbf 1_{2\mid d},
\tag{0.5}
\]

where

\[
 \deg P_Q=N_Q=d-1-\epsilon_Q,\qquad
 P_Q(z/\sqrt q)
 =\prod_{\lambda}(1-\lambda z)^{m_\lambda},
 \qquad |\lambda|=1.
\tag{0.6}
\]

The modulus statement in (0.6) is function-field RH for this quadratic
character. It is an available theorem in the laboratory, not a number-field
inference.

### Fixed-filter nonannihilation theorem

Put \(D=\deg\mathcal B\). If

\[
 \boxed{N_Q>D,}
\tag{0.7}
\]

then at least one normalized Frobenius mode in (0.6) survives in
\(\mathcal H_{\sigma,Q}\). Consequently:

1. \(\mathcal H_{\sigma,Q}\) has a pole on \(|z|=1\);
2. \(h_{\sigma,Q}(n)\) is not exponentially decaying;
3. the complete affine finite-support law and the deletion-only exponential
   law do not survive this incomplete evaluation restriction;
4. the prefix degree energy has an explicit positive polynomial main term.

This is uniform over **every** irreducible \(Q\) satisfying (0.7), not a
finite census. Since irreducibles exist in every positive degree, every
fixed finite band-pass filter fails to annihilate all sufficiently
high-conductor evaluation families.

The result is consistent with known function-field RH. Polynomial growth in
the degree horizon \(H\) is subpower in the norm horizon \(q^H\). What fails
is the much stronger exponential decay of the complete affine shadow.

## 1. The literal beta Euler identity

It is useful to prove the source identity before imposing any family
restriction.

Let \(C/\mathbf F_q\) be a smooth projective geometrically connected curve,
let \(U\subset C\) be a nonempty open curve, and let
\(P\in|U|\) have degree \(e\). For an effective divisor \(D\) on \(U\), put

\[
 \beta_P(D)=\mu(D)-\mathbf 1_{P\le D}\mu(D-P).
\tag{1.1}
\]

Let \(\psi\) be a multiplicative divisor character on \(U\), including
\(\psi=1\), and define

\[
 L_U(u,\psi)
 =\prod_{v\in|U|}
  (1-\psi(v)u^{\deg v})^{-1}.
\tag{1.2}
\]

Then

\[
\boxed{
 \sum_{D\ge0}\beta_P(D)\psi(D)u^{\deg D}
 ={1-\psi(P)u^e\over L_U(u,\psi)}.}
\tag{1.3}
\]

Indeed,

\[
 \sum_D\mu(D)\psi(D)u^{\deg D}
 ={1\over L_U(u,\psi)}.
\]

In the second term of (1.1), the substitution \(D=P+E\) is a bijection,
and contributes

\[
 {\psi(P)u^e\over L_U(u,\psi)}.
\]

This proves (1.3) without a coefficient truncation.

At the exceptional place itself, the inverse \(L\)-factor already contains
\(1-\psi(P)u^e\). Thus the weighted local beta polynomial is

\[
 \boxed{(1-\psi(P)u^e)^2.}
\tag{1.4}
\]

For \(\psi(P)=1\), its coefficient vector is
\((1,-2,1)\), exactly the duplicate-\(67\) source vector. For
\(\psi(P)=-1\), it is \((1,2,1)\). This is the literal source pushforward,
not an analogy.

## 2. The exact degree-lattice band-pass

Degree is the function-field logarithmic coordinate because

\[
 \log |f|=(\deg f)\log q.
\]

Let

\[
 K(z)=\sum_{m=0}^{M}\kappa_mz^m\ne0
\]

be a fixed finite causal seed. It may be the cell pushforward of a compact
boundary kernel; the theorem uses only its exact finite coefficients.
For fixed integers

\[
 s,r,\ell\ge1,\qquad j\ge0,
\]

define

\[
\boxed{
 \mathcal B(z)
 =K(z)
 \left({1-z^s\over s}\right)^r
 \left({1+z+\cdots+z^{\ell-1}\over\ell}\right)^j.}
\tag{2.1}
\]

The first multiplier is the exact fixed difference of step
\(s\log q\). The second is the exact causal degree-box average. Therefore

\[
 [z^n]\mathcal B(z)A(z)
\]

is precisely the fixed degree convolution of the source coefficient
sequence \(A\) with the chosen band-pass.

On the unit circle \(z=e^{-it}\),

\[
 |1-z^s|^{2r}
\]

is the discrete counterpart of the order-\(2r\) autocorrelation notch.
The word fixed is again load-bearing: all parameters in (2.1) are
independent of the degree horizon and of every Frobenius root.

A pure difference kills a normalized Frobenius mode \(\lambda\) only when

\[
 \lambda^s=1.
\tag{2.2}
\]

The box multiplier can kill further torsion modes. Neither multiplier
annihilates a generic Frobenius angle.

For the filtered coefficient sequence \(h(n)\), the exact prefix Gram is

\[
\boxed{
\sum_{n=0}^{H}|h(n)|^2
=\sum_{D,E}
 {w(D)\over q^{\deg D/2}}
 {\overline{w(E)}\over q^{\deg E/2}}
 \sum_{n=0}^{H}
 b_{n-\deg D}\overline{b_{n-\deg E}},}
\tag{2.3}
\]

where \(w(D)=\beta_P(D)\delta_{\sigma,Q}(D)\),
\(\mathcal B(z)=\sum b_mz^m\), and \(b_m=0\) outside the finite causal
support. Thus the energy used below is the exact degree-lattice band-pass
energy, not a histogram.

## 3. The incomplete evaluation projector

Return to \(A=\mathbf F_q[T]\). Let \(Q\) be monic irreducible of degree
\(d\). Reduction modulo \(Q\) maps \(A\) to \(\mathbf F_{q^d}\), and
\(\chi_Q\) is its quadratic character.

Equation (0.2) is an exact Fourier projector on the two nonzero evaluation
squareclasses. Consequently,

\[
\begin{aligned}
\sum_f\beta_P(f)\delta_{\sigma,Q}(f)u^{\deg f}
={1\over2}\bigg[
&\sum_{Q\nmid f}\beta_P(f)u^{\deg f}\\
&+\sigma\sum_f\beta_P(f)\chi_Q(f)u^{\deg f}
\bigg].
\end{aligned}
\tag{3.1}
\]

The trivial deleted Euler product is

\[
 Z_{\mathbf A^1\setminus\{Q\}}(u)
 ={1-u^d\over1-qu},
\tag{3.2}
\]

so (1.3) gives

\[
 \sum_{Q\nmid f}\beta_P(f)u^{\deg f}
 ={(1-u^e)(1-qu)\over1-u^d}.
\tag{3.3}
\]

Without deleting \(Q\), the same calculation gives (0.3a). Equation (3.3)
gives (0.3b) after normalization and filtering. Thus conductor avoidance
alone has no singularity before \(|z|=\sqrt q\); any uncanceled poles lie
on that larger circle. It does not create the unit-circle obstruction.

The character channel is

\[
 \sum_f\beta_P(f)\chi_Q(f)u^{\deg f}
 ={1-\chi_Q(P)u^e\over L_Q(u,\chi_Q)}.
\tag{3.4}
\]

Insert \(u=z/\sqrt q\), multiply by \(\mathcal B(z)\), and combine
(3.3)--(3.4). This proves (0.4).

The incomplete family is a sum of two Euler products rather than one Euler
product. That distinction is the mechanism. The complete genus-zero inverse
zeta zero remains in the first channel, while the second channel introduces
the reciprocal zeros of a genuine quadratic \(L\)-function.

### 3.1 Positive averaging does not restore the complete source

Let \(t(n)\) and \(c(n)\) be the filtered coefficients of the trivial
deleted and character lines in (0.4). Then

\[
 h_{\sigma,Q}(n)={t(n)+\sigma c(n)\over2}.
\tag{3.5}
\]

Coherent recombination before a norm gives

\[
\boxed{
 h_{+,Q}(n)+h_{-,Q}(n)=t(n),\qquad
 h_{+,Q}(n)-h_{-,Q}(n)=c(n).}
\tag{3.6}
\]

Thus adding the two class amplitudes restores the exponentially decaying
deleted channel. Positive energy averaging behaves differently:

\[
\boxed{
 |h_{+,Q}(n)|^2+|h_{-,Q}(n)|^2
 ={\,|t(n)|^2+|c(n)|^2\over2}.}
\tag{3.7}
\]

After summing over a degree horizon, one half of the inverse-\(L\) energy
survives unchanged. This is an exact family-assembly firewall: orthogonal
positive averaging cannot remove the evaluation Frobenius main term, while
coherent signed assembly can.

## 4. Exact Frobenius pole classification

The restriction of \(\chi_Q\) to \(\mathbf F_q^\times\) is the \(d\)-th
power of the quadratic character of \(\mathbf F_q^\times\). Hence it is even
exactly when \(d\) is even. The standard completed factorization is (0.5),
with

\[
 N_Q=d-1-\mathbf 1_{2\mid d}.
\tag{4.1}
\]

Let

\[
 v_\lambda
 =\operatorname {ord}_{z=\lambda^{-1}}\mathcal B(z).
\tag{4.2}
\]

The beta numerator in the character line of (0.4) cannot vanish on the unit
circle:

\[
 \left|\chi_Q(P)q^{-e/2}z^e\right|=q^{-e/2}<1
 \qquad(|z|=1).
\tag{4.3}
\]

The even factor \(1-z/\sqrt q\) also has no unit-circle zero. The trivial
deleted line is analytic on \(|z|<\sqrt q\), so it cannot cancel a
unit-circle pole from the character line.

Therefore the exact surviving pole order at \(\lambda^{-1}\) is

\[
\boxed{
 M_\lambda=\max(m_\lambda-v_\lambda,0).}
\tag{4.4}
\]

All evaluation Frobenius modes disappear if and only if

\[
 \boxed{P_Q(z/\sqrt q)\mid\mathcal B(z)}
\tag{4.5}
\]

with multiplicities. Since the left side has degree \(N_Q\), condition
\(N_Q>D\) makes (4.5) impossible. This proves the fixed-filter
nonannihilation theorem.

No modulus enumeration is hidden here. The exact irreducible count

\[
 I_q(d)={1\over d}\sum_{m\mid d}\mu(m)q^{d/m}
\tag{4.6}
\]

is positive for every \(q\) and \(d\). The replay evaluates (4.6) only to
certify that the declared bounded control degrees are populated; the proof
is the degree argument (4.5).

## 5. The exact energy main term

Assume at least one \(M_\lambda>0\), and put

\[
 M=\max_\lambda M_\lambda.
\]

For each surviving root, define its leading principal-part coefficient

\[
 A_\lambda
 =\lim_{z\to\lambda^{-1}}
 (1-\lambda z)^{M}\mathcal H_{\sigma,Q}(z)
 \qquad(M_\lambda=M).
\tag{5.1}
\]

This number is nonzero by the definition of the surviving pole order.
When \(\lambda\) is a simple root and
\(\mathcal B(\lambda^{-1})\ne0\), it is explicitly

\[
\boxed{
A_\lambda
={\sigma\,\mathcal B(\lambda^{-1})
 (1-\chi_Q(P)q^{-e/2}\lambda^{-e})
 \over
 2(1-\lambda^{-1}/\sqrt q)^{\epsilon_Q}
 \displaystyle\prod_{\mu\ne\lambda}
 (1-\mu/\lambda)^{m_\mu}}.}
\tag{5.1a}
\]

Partial fractions applied to (0.4) give, for some \(R>1\),

\[
\boxed{
 h_{\sigma,Q}(n)
 =\sum_{M_\lambda>0}
 Q_\lambda(n)\lambda^n+O(R^{-n}),
 \qquad
 \deg Q_\lambda=M_\lambda-1.}
\tag{5.2}
\]

The leading term of \(Q_\lambda\) is

\[
 {A_\lambda\over(M_\lambda-1)!}n^{M_\lambda-1}.
\tag{5.3}
\]

The same coefficients can be generated without factoring a single
polynomial. If

\[
 L_{\rm norm}(z)=1+\ell_1z+\cdots+\ell_Nz^N,\qquad
 {N(z)\over L_{\rm norm}(z)}=\sum_{n\ge0}c_nz^n,
\]

then exact coefficient comparison gives

\[
\boxed{
 c_n=N_n-\sum_{k=1}^{\min(n,N)}\ell_kc_{n-k}.}
\tag{5.3a}
\]

This is the recurrence used by the replay. It needs the symbolic
\(L\)-polynomial only; it enumerates no polynomial modulus, point, or curve.

Distinct normalized roots give bounded oscillatory sums after one discrete
summation by parts; their cross terms have one lower power of \(H\) than the
diagonal. Hence

\[
\boxed{
\sum_{n=0}^{H}|h_{\sigma,Q}(n)|^2
=
{H^{2M-1}\over
 (2M-1)((M-1)!)^2}
\sum_{M_\lambda=M}|A_\lambda|^2
+O(H^{2M-2}).}
\tag{5.4}
\]

In the simple surviving-root case,

\[
 \sum_{n=0}^{H}|h_{\sigma,Q}(n)|^2
 =H\sum_\lambda|A_\lambda|^2+O(1).
\tag{5.5}
\]

If every pole is canceled, the rational function is analytic on a disc of
radius greater than one and the coefficients decay exponentially. Thus
(4.4)--(5.4) are a complete dichotomy for the affine evaluation
restriction.

This is the precise truth-serum replacement for a pretty shell plot:

~~~text
complete affine family
  -> literal beta generating polynomial
  -> finite coefficient support

hard conductor deletion only
  -> possible poles only at radius sqrt(q)
  -> exponential coefficient decay

one hard evaluation Boolean class
  -> trivial deleted inverse-zeta channel
     plus a quadratic inverse-L channel
  -> explicit Frobenius residues
  -> positive polynomial degree-energy main term.
~~~

## 6. Every fixed curve

The Euler identity itself does not require genus zero.

Let \(C/\mathbf F_q\) be fixed, let \(U\subset C\) contain the exceptional
place \(P\), and let \(\chi\) be a nontrivial quadratic divisor or ray-class
character on \(U\). Define

\[
 \delta_{\sigma,\chi}(D)
 ={1+\sigma\chi(D)\over2}
\]

on the divisor monoid where \(\chi(D)\in\{\pm1\}\). If ramified places are
present, remove them from \(U\) first. Equations (1.3) and the projector give

\[
\boxed{
\mathcal H_{\sigma,\chi}(z)
={\mathcal B(z)\over2}
\left[
 {1-q^{-e/2}z^e\over Z_U(z/\sqrt q)}
 +\sigma\,
 {1-\chi(P)q^{-e/2}z^e
  \over L_U(z/\sqrt q,\chi)}
\right].}
\tag{6.1}
\]

This is an exact all-curve identity.

Factor the normalized weight-one pieces of \(Z_U\) and \(L_U(\,\cdot,\chi)\).
Their unit-circle principal parts give the coefficient expansion and energy
main term exactly as in Section 5. On a positive-genus curve the trivial
inverse-zeta and character inverse-\(L\) channels can share a normalized
root, so their residues must be added before declaring a pole. Equation
(6.1) is the exact cancellation algorithm; no universal noncancellation is
claimed in that broader setting.

The affine line is cleaner. Its trivial deleted channel is analytic across
the unit circle, so every uncanceled quadratic evaluation pole survives in
the full Boolean sum. This is why the uniform theorem is stated first on
\(\mathbf F_q[T]\).

## 7. The bounded formal control

The replay includes one exact formal residue control, not an arithmetic
curve census.

Take

\[
 q=9,\qquad d=3,\qquad e=1,\qquad
 \chi_Q(P)=-1,\qquad
 \mathcal B(z)=1-z,
\]

and use the Weil-admissible completed control polynomial

\[
 P_Q(z/\sqrt q)=1+z^2.
\]

The character line is

\[
 {(1-z)(1+z/3)\over1+z^2}.
\tag{7.1}
\]

Its eventual coefficient period is

\[
 \left({2\over3},{4\over3},-{2\over3},-{4\over3}\right),
\]

whose mean square is \(10/9\). The Boolean projector contributes one half
of this amplitude, while the trivial line is exponentially decaying.
Therefore the exact formal energy law is

\[
 \boxed{
 \sum_{n=0}^{H}|h_{+,Q}(n)|^2
 ={5\over18}H+O(1).}
\tag{7.2}
\]

The replay does **not** assert that a particular degree-three modulus over
\(\mathbf F_9\) realizes this polynomial. Its role is to authenticate the
normalization, projector, recurrence, and energy coefficient. The
large-conductor nonannihilation theorem requires no such realization.

## 8. Relation to the predecessor packets

The complete affine shadow proved exponential shell decay because every
local state was summed before a norm and

\[
 \prod_R(1-u^{\deg R})=1-qu.
\]

The all-curve extension showed that positive genus replaces this finite zero
by Frobenius residue channels. The present packet shows a second and
independent way those channels appear:

- the underlying curve may remain \(\mathbf P^1\);
- the literal complete beta field is actually a polynomial, while hard
  conductor deletion by itself retains exponential decay;
- one evaluation Boolean restriction already inserts a nontrivial
  quadratic \(L\)-polynomial;
- no fixed finite degree notch can cancel all sufficiently high-conductor
  versions of that polynomial.

This does not prove or refute an incomplete WAVEPRIMCAR estimate. The degree
energy in (5.4) is still subpower in \(q^H\), as function-field RH predicts.
The theorem identifies the exact main term that such an estimate must
retain or renormalize.

The restriction is evaluation/Boolean, not an owner restriction. Largest
prime ownership is nonmultiplicative and needs a different recursion. No
owner statement is silently inferred from (0.2).

## 9. Proof and scope ledger

| statement | grade |
|---|---|
| literal beta divisor identity (1.3) | **PROVED EXACT FOR EVERY FIXED CURVE AND MULTIPLICATIVE CHARACTER** |
| local beta square (1.4) | **PROVED EXACT** |
| finite degree-band-pass multiplier (2.1) | **EXACT DEFINITION AND CONVOLUTION IDENTITY** |
| Boolean evaluation projector (0.2) | **PROVED EXACT** |
| affine incomplete identity (0.4) | **PROVED BY TWO EULER PRODUCTS** |
| coherent/positive Boolean identities (3.6)--(3.7) | **PROVED EXACT COEFFICIENTWISE** |
| all-curve identity (6.1) | **PROVED EXACT** |
| quadratic completed degree (4.1) | **IMPORTED STANDARD FUNCTION-FIELD CHARACTER ALGEBRA** |
| unit-circle location (0.6) | **IMPORTED FUNCTION-FIELD RH / WEIL** |
| pole order formula (4.4) | **PROVED BY EXACT LOCAL NONVANISHING** |
| fixed-filter no-go for \(N_Q>\deg\mathcal B\) | **PROVED FOR EVERY IRREDUCIBLE \(Q\) IN THAT DEGREE RANGE** |
| symbolic coefficient recurrence (5.3a) | **PROVED EXACT** |
| coefficient expansion and energy main term (5.2)--(5.4) | **PROVED BY PARTIAL FRACTIONS AND GEOMETRIC-SUM ORTHOGONALITY** |
| formal \(5/18\) control | **REPLAYED EXACT; NO MODULUS REALIZATION CLAIM** |
| owner restriction | **NOT INCLUDED** |
| incomplete WAVEPRIMCAR or PRIMCAR | **NOT PROVED** |
| number-field estimate | **NOT INFERRED** |
| RH or GRH | **NOT PROVED** |

## 10. Bounded replay

~~~text
python -B research/l-families/atlas/function_field/function_field_beta_boolean_evaluation_bandpass.py --check
python -B -O research/l-families/atlas/function_field/function_field_beta_boolean_evaluation_bandpass.py --check
python -B -m unittest tests.test_function_field_beta_boolean_evaluation_bandpass
python -B -O -m unittest tests.test_function_field_beta_boolean_evaluation_bandpass
python -B -m ruff check research/l-families/atlas/function_field/function_field_beta_boolean_evaluation_bandpass.py tests/test_function_field_beta_boolean_evaluation_bandpass.py
python -B -m ruff format --check research/l-families/atlas/function_field/function_field_beta_boolean_evaluation_bandpass.py tests/test_function_field_beta_boolean_evaluation_bandpass.py
~~~

The replay uses:

- exact rational polynomial and reciprocal-series arithmetic;
- exact Möbius irreducible-degree counts for \(q=3,5,7\);
- conductor degrees only \(9\) and \(10\);
- one formal coefficient recurrence through degree \(40\);
- no polynomial, curve, point, zero, conductor family, or \(L\)-function
  enumeration;
- no floating-point arithmetic.
