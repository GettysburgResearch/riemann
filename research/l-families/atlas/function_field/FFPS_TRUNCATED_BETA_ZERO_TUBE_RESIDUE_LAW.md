# The truncated beta boundary has an exact zero-tube residue law

Status: **exact local distributional law at critical-line zeros, exact
multiplicity and fixed-notch constants, and exact real-\(c\) Perron
normalization on a fixed guarded height window; no infinite-height bound,
contour displacement, RH, or GRH result**

Bounded symbolic replay:
[ffps_truncated_beta_zero_tube_residue_law.py](ffps_truncated_beta_zero_tube_residue_law.py).
Canonical summary:
[ffps_truncated_beta_zero_tube_residue_law.json](ffps_truncated_beta_zero_tube_residue_law.json).

Frozen predecessor: band-pass assembled Perron leakage at commit
`3dbf13f6d1c49e573a5b9cd8355d9c124273062b`.  The replay pins its complete
quartet by Git blob ID.

## 0. Outcome

Put

\[
 A(s)=1-67^{-s},
 \qquad
 B_\beta(s)={A(s)\over\zeta(s)}.
\tag{0.1}
\]

Fix \(T>0\) such that neither endpoint \(1/2\pm iT\) is a zeta zero.
Choose a thin right tube

\[
 \mathcal T_{T,\eta}=
 \{1/2\le\Re s\le1/2+\eta, |\Im s|\le T\}
\tag{0.2}
\]

whose zeros on its left boundary are isolated from every other zero in the
tube.  At fixed height this is a local compactness hypothesis, not RH: one
may shrink \(\eta\) below the positive distance to the finitely many
off-line zeros in a larger compact rectangle.

Let

\[
 \rho={1\over2}+i\gamma
\tag{0.3}
\]

be one critical-line zero of multiplicity \(m\), and put

\[
 a_\rho={\zeta^{(m)}(\rho)\over m!},
 \qquad
 Q_\rho=\left|{1-67^{-\rho}\over a_\rho}\right|^2.
\tag{0.4}
\]

The exceptional numerator never removes such a zero:

\[
 |1-67^{-\rho}|\ge1-67^{-1/2}>0.
\tag{0.5}
\]

Define

\[
 I_m=\int_{\mathbf R}{du\over(1+u^2)^m}
 =\sqrt\pi{\Gamma(m-1/2)\over\Gamma(m)}
 =\pi{\binom{2m-2}{m-1}\over4^{m-1}}.
\tag{0.6}
\]

Then, locally in distributions at \(t=\gamma\),

\[
\boxed{
 \delta^{2m-1}
 \left|B_\beta\!\left({1\over2}+\delta+it\right)\right|^2dt
 \ \Longrightarrow\ 
 I_mQ_\rho\,\delta_\gamma.}
\tag{0.7}
\]

In particular, if every critical-line zero in \((-T,T)\) is simple, then

\[
\boxed{
 \delta
 \left|B_\beta\!\left({1\over2}+\delta+it\right)\right|^2dt
 \ \Longrightarrow\ 
 \pi\sum_{|\gamma|<T}Q_\rho\,\delta_\gamma.}
\tag{0.8}
\]

This is the truncated beta zero-tube law.  A multiple zero does not produce
a finite measure under the simple scaling: if \(m\ge2\), its local mass in
(0.8) diverges like \(\delta^{2-2m}\).

Now let \(K\) be one fixed real compact band-pass kernel, let

\[
 \mathcal R(x)=\int K(u)K(u+x)du,
 \qquad
 w(t)=\widehat{\mathcal R}(t)=|\widehat K(t)|^2\ge0,
\tag{0.9}
\]

and define the max-tilted Perron weight

\[
 w_c(t)=
 \widehat{\mathcal R(\cdot)e^{-c|\cdot|/2}}(t).
\tag{0.10}
\]

The real-\(c\), height-truncated inner integral from the one-variable sharp
Perron coordinate is

\[
\boxed{
 \mathfrak P_T(c)=
 {1\over2\pi}\int_{-T}^T
 w_c(t)
 B_\beta\!\left({1+c\over2}-it\right)
 B_\beta\!\left({1+c\over2}+it\right)dt.}
\tag{0.11}
\]

For real \(c>0\), the beta product is the absolute square. Since
\(w_c\to w\) uniformly on every fixed height window, a zero with
\(w(\gamma)>0\) contributes

\[
\boxed{
 \mathfrak P_{\rho}(c)
 \sim
 \binom{2m-2}{m-1}
 Q_\rho w(\gamma)c^{1-2m}.}
\tag{0.12}
\]

The central binomial coefficient is the complete normalization: the
substitution \(\delta=c/2\), the Cauchy mass (0.6), and the Perron Fourier
factor \(1/(2\pi)\) cancel every remaining power of two and \(\pi\).

Under the local simplicity and nonalignment hypotheses

\[
 m_\rho=1,
 \qquad
 w(\gamma)>0
 \quad(|\gamma|<T),
\tag{0.13}
\]

one obtains the exact boundary residue limit

\[
\boxed{
 \lim_{c\downarrow0}c\,\mathfrak P_T(c)
 =\sum_{|\gamma|<T}Q_\rho w(\gamma).}
\tag{0.14}
\]

Consequently, on a window where the autocorrelation weight is positive at
every critical zero, the conditional estimate

\[
 \mathfrak P_T(c)=O_T(1/c)
\tag{0.15}
\]

would force every critical-line zero in that window to be simple.  It would
not prove that those zeros lie on the critical line, rule out off-line
zeros elsewhere, control \(T\to\infty\), or prove RH.

## 1. Local Laurent proof

At a zero of multiplicity \(m\), write \(z=s-\rho\). The local Taylor
expansion is

\[
 \zeta(\rho+z)=a_\rho z^m(1+O_\rho(z)),
\tag{1.1}
\]

so

\[
 B_\beta(\rho+z)
 ={1-67^{-\rho}\over a_\rho}z^{-m}(1+O_\rho(z)).
\tag{1.2}
\]

On the right line, take \(z=\delta+ix\), where \(x=t-\gamma\). Hence

\[
 \left|B_\beta\!\left({1\over2}+\delta+i(\gamma+x)\right)\right|^2
 =Q_\rho(\delta^2+x^2)^{-m}
 \left(1+O_\rho\!\left(\sqrt{\delta^2+x^2}\right)\right).
\tag{1.3}
\]

For a continuous test function \(\varphi\) supported in an isolating
neighborhood of \(\gamma\), substitute \(x=\delta u\). The main term is

\[
 Q_\rho\int_{\mathbf R}{\varphi(\gamma+\delta u)\over(1+u^2)^m}du,
\tag{1.4}
\]

which tends to \(I_mQ_\rho\varphi(\gamma)\). Splitting the integral into a
fixed core and its tail controls the error in (1.3). This proves (0.7).

On the complement of the isolating neighborhoods, \(1/\zeta\) is uniformly
bounded in a sufficiently thin closed right tube.  Multiplication by any
positive power of \(\delta\) sends that complement to zero. Summing (0.7)
over the finitely many simple zeros proves (0.8).

No global zero-free region is used.  The proof is a local meromorphic
calculation on one fixed compact window.

## 2. Translation into the real-\(c\) Perron inner

The frozen Perron formula uses

\[
 z=c,
 \qquad
 s={1+z\over2}={1\over2}+{c\over2}.
\tag{2.1}
\]

Thus \(\delta=c/2\). If a smooth local cutoff isolates \(\rho\) and
\(w(\gamma)>0\), equations (0.7) and (0.10) give

\[
\begin{aligned}
 \mathfrak P_\rho(c)
 &\sim {Q_\rho w(\gamma)\over2\pi}
 I_m\left({c\over2}\right)^{1-2m}\\
 &=Q_\rho w(\gamma)
 {2^{2m-2}I_m\over\pi}c^{1-2m}.
\end{aligned}
\tag{2.2}
\]

But

\[
 {2^{2m-2}I_m\over\pi}
 =\binom{2m-2}{m-1},
\tag{2.3}
\]

which proves (0.12).

The tilt changes no leading coefficient at a positive-weight zero.  Compact
support gives, uniformly for fixed \(T\),

\[
 w_c(t)=w(t)+O_{K,T}(c).
\tag{2.4}
\]

Inside a zero tube, the error in (2.4) is a relative \(O(c)\) correction
to (2.2); away from every zero it contributes \(O(c)\). Therefore, if all
zeros are simple and \(w(\gamma)>0\), summing (2.2) gives (0.14).

For example, the first multiplicities have the exact local laws

\[
\begin{array}{c|c}
 m&\mathfrak P_\rho(c)/(Q_\rho w(\gamma))\\ \hline
 1&c^{-1}(1+o(1)),\\
 2&2c^{-3}(1+o(1)),\\
 3&6c^{-5}(1+o(1)),\\
 4&20c^{-7}(1+o(1)).
\end{array}
\tag{2.5}
\]

This explains the force of (0.15).  At a positive-weight multiple zero the
integrand is locally positive and grows faster than \(1/c\); bounded
contributions away from the zero cannot cancel it.

## 3. Fixed autocorrelation notches and multiplicity

Suppose now that the untwisted autocorrelation weight has a zero at the
same ordinate:

\[
 w(\gamma+x)=\kappa_\gamma x^{2r}
 +O_\gamma(|x|^{2r+1}),
 \qquad
 \kappa_\gamma>0.
\tag{3.1}
\]

The even order is forced by \(w=|\widehat K|^2\ge0\). For
\(0\le r\le m-1\),

\[
 \int_{\mathbf R}{u^{2r}\over(1+u^2)^m}du
 =\mathrm B\!\left(r+{1\over2},m-r-{1\over2}\right).
\tag{3.2}
\]

The un-tilted local Perron inner therefore satisfies

\[
\boxed{
 \mathfrak J_\rho(c)
 \sim
 C_{m,r}Q_\rho\kappa_\gamma
 c^{2r+1-2m},}
\tag{3.3}
\]

where

\[
 C_{m,r}={2^{2m-2r-2}\over\pi}
 \mathrm B\!\left(r+{1\over2},m-r-{1\over2}\right).
\tag{3.4}
\]

If \(r\ge m\), the local integral is bounded as \(c\downarrow0\). Hence an
un-tilted \(O(1/c)\) bound at a fixed notch forces exactly

\[
\boxed{m\le r+1.}
\tag{3.5}
\]

For \(r=m-1\), the zero is reduced precisely to the \(1/c\) boundary:

\[
 C_{m,m-1}
 ={1\over4^{m-1}}\binom{2m-2}{m-1}.
\tag{3.6}
\]

For a finite-difference kernel of order \(r_0\), the standard factor

\[
 |1-e^{-i\varepsilon t}|^{2r_0}
\tag{3.7}
\]

creates zeros of order \(2r_0\) only at the fixed lattice
\(2\pi\mathbf Z/\varepsilon\). Thus a fixed notch suppresses a zeta tube
only under exact ordinate alignment. Away from that lattice this
finite-difference factor is nonzero, but the remaining factors in
\(\widehat K(\gamma)\) must still be checked: the unnotched law (0.12)
applies only when the full weight satisfies \(w(\gamma)>0\). No adaptive,
zero-dependent notch is introduced.

## 4. The physical max tilt refills a notch

The actual one-variable Perron inner uses \(w_c\), not \(w\). Compact
support gives the expansion

\[
 w_c(t)=w(t)+c\ell(t)+O_K(c^2),
 \qquad
 \ell(t)=-{1\over2}\widehat{|x|\mathcal R(x)}(t).
\tag{4.1}
\]

At zero frequency, for a nonzero mean-zero kernel with cumulative
\(F(x)=\int_{-\infty}^xK(u)du\), the frozen absolute-lag identity gives

\[
 \ell(0)=\|F\|_2^2>0.
\tag{4.2}
\]

More generally, at a fixed notch ordinate with \(\ell(\gamma)\ne0\), the
linear leakage contributes

\[
\boxed{
 \ell(\gamma)Q_\rho
 \binom{2m-2}{m-1}c^{2-2m}}
\tag{4.3}
\]

to the local tilted inner. For every \(r\ge1\), this dominates the native
notch term in (3.3). A simple aligned zero contributes only \(O(1)\), but a
double aligned zero with positive leakage contributes \(\asymp c^{-2}\),
already larger than \(1/c\).

Thus fixed notching does not silently remove the multiple-zero obstruction
from the physical max coordinate.  At zero frequency the leakage
coefficient is strictly positive; at other notch ordinates its sign and
possible vanishing must be checked rather than assumed.

This is still only a local tube diagnosis. The signed tilted weight need
not be globally positive, so an \(O(1/c)\) consequence at notched ordinates
requires either a localized estimate or an explicit noncancellation/sign
hypothesis.  The positive un-tilted statement (3.5) has no such ambiguity.

## 5. What an \(O(1/c)\) boundary theorem would and would not say

On a fixed guarded window, the hierarchy is exact:

~~~text
simple positive-weight zero
  -> one beta Cauchy tube
  -> Q_rho*w(gamma)/c;

multiple positive-weight zero of order m
  -> higher beta tube
  -> binomial(2m-2,m-1)*Q_rho*w(gamma)/c^(2m-1);

fixed notch of order 2r
  -> multiplicity allowance m<=r+1 in the untwisted weight;

physical max tilt
  -> linear notch refill and a c^(2-2m) leakage channel.
~~~

Therefore a truncated \(O_T(1/c)\) theorem with positive weight at all
critical zeros would imply simplicity in that window.  It would also
identify its leading constant as the finite negative-second-moment sum

\[
 \sum_{|\gamma|<T}
 |1-67^{-\rho}|^2
 {w(\gamma)\over|\zeta'(\rho)|^2}.
\tag{5.1}
\]

At fixed \(T\), this is a finite local statement. The hard ASMPERRON
problem requires much more:

* a contour displacement that reaches \(c\downarrow0\);
* control uniform in a height window which eventually becomes unbounded;
* treatment of every zero tube and the complement simultaneously;
* the infinite-\(t\) tail of the reciprocal-zeta product;
* preservation of the signed max-tilted integral and the outer Perron
  endpoint limit.

None of those steps follows from (0.7)--(0.14).  In particular, this packet
does not establish (0.15), does not prove simplicity of any actual zeta
zero, does not rule out off-line zeros, and does not prove RH.

## 6. Claim ledger

| statement | grade |
|---|---|
| beta numerator nonvanishing at critical zeros | **PROVED EXACT** |
| local multiplicity law (0.7) | **PROVED BY LAURENT EXPANSION AND CAUCHY SCALING** |
| simple distributional law (0.8) | **PROVED ON A FIXED ZERO-ISOLATING WINDOW** |
| real-\(c\) central-binomial normalization (0.12) | **PROVED EXACT** |
| simple residue limit (0.14) | **PROVED UNDER LOCAL SIMPLICITY AND WEIGHT NONALIGNMENT** |
| \(O(1/c)\) forces simplicity at positive-weight zeros | **PROVED CONDITIONALLY FROM POSITIVITY** |
| fixed-notch law (3.3)--(3.6) | **PROVED EXACT** |
| max-tilt refill (4.1)--(4.3) | **PROVED FROM THE FROZEN ABSOLUTE-LAG IDENTITY** |
| infinite-height negative moment or tail estimate | **NOT PROVED** |
| ASMPERRON contour displacement | **NOT PROVED** |
| RH or GRH | **NOT PROVED** |

## 7. Bounded replay

The replay derives \(I_m/\pi\), the real-\(c\) central binomial constants,
and every fixed-notch beta constant through multiplicity six using exact
integer and rational arithmetic.  Its three-term second-difference toy
checks the autocorrelation notch, the absolute-lag identity, and the
strictly positive linear max-tilt coefficient.  It computes no zeta zero,
zeta value, prime interval, contour integral, or floating-point fit.

~~~text
python -B research/l-families/atlas/function_field/ffps_truncated_beta_zero_tube_residue_law.py --check
python -B -O research/l-families/atlas/function_field/ffps_truncated_beta_zero_tube_residue_law.py --check
python -B -m unittest tests.test_ffps_truncated_beta_zero_tube_residue_law
python -B -O -m unittest tests.test_ffps_truncated_beta_zero_tube_residue_law
python -B -m ruff check research/l-families/atlas/function_field/ffps_truncated_beta_zero_tube_residue_law.py tests/test_ffps_truncated_beta_zero_tube_residue_law.py
python -B -m ruff format --check research/l-families/atlas/function_field/ffps_truncated_beta_zero_tube_residue_law.py tests/test_ffps_truncated_beta_zero_tube_residue_law.py
~~~
