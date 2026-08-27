# Higher-derivative beta carriers form a sharp all-support hierarchy

Status: **exact fixed-rung carrier and moment formulas, exact sharp
support-energy and spectral identities, an all-support renormalized
RH equivalence at every fixed rung, a safe growing-rung window, and an
exact critical-width phase diagram; no new beta estimate, proof of RH,
GRH, or unrestricted growing-rung theorem**

Bounded replay:
[ffps_higher_derivative_carrier_hierarchy.py](ffps_higher_derivative_carrier_hierarchy.py).
Canonical summary:
[ffps_higher_derivative_carrier_hierarchy.json](ffps_higher_derivative_carrier_hierarchy.json).

Frozen source: the beta carrier Legendre moment tower at commit
**866b082b7cecdfa03ebbeca369aa8f654a9bad00**. The producer pins all
four source blobs and imports no live predecessor module.

## 0. Outcome

Fix an integer \(m\ge1\) and a width \(S>0\). Define the positive
unit-mass beta carrier

\[
 Q_{m,S}(t)
 =\frac{(2m+1)!}{m!^2S^{2m+1}}
 t^m(S-t)^m\mathbf1_{[0,S]}(t)
\tag{0.1}
\]

and differentiate the zero extension exactly \(m\) times:

\[
 J_{m,S}=D^mQ_{m,S}.
\tag{0.2}
\]

The endpoint zeros in (0.1) prevent delta masses through derivative
order \(m\). Rodrigues' formula gives the exact compact detector

\[
\boxed{
 J_{m,S}(t)
 =(-1)^m\frac{(2m+1)!}{m!S^{m+1}}
 P_m\!\left(\frac{2t}{S}-1\right)\mathbf1_{(0,S)}(t),}
\tag{0.3}
\]

where \(P_m\) is the ordinary Legendre polynomial.

With

\[
 a_n=\frac{\beta(n)}{\sqrt n},\qquad
 \beta(n)=\mu(n)-\mathbf1_{67\mid n}\mu(n/67),
\tag{0.4}
\]

put

\[
 H_{m,S,X}(t)=\sum_{n\le X}a_nJ_{m,S}(t-\log n),\qquad
 \mathcal E_{m,S}(X)=\|H_{m,S,X}\|_2^2.
\tag{0.5}
\]

Let \(B_r(X)=\sum_{n\le X}a_n(\log n)^r\), let
\(q_h=\int t^hQ_{m,S}(t)\,dt\), and let
\(M_k=\int t^kH_{m,S,X}(t)\,dt\). Then

\[
 M_0=\cdots=M_{m-1}=0,\qquad
 M_m=(-1)^m m!B_0(X),
\tag{0.6}
\]

and, for every \(r\ge0\),

\[
\boxed{
 M_{m+r}
 =(-1)^m m!\binom{m+r}{m}
 \sum_{h=0}^{r}\binom rh q_hB_{r-h}(X).}
\tag{0.7}
\]

Thus every fixed rung has \(m\) exact vanishing moments and then a
triangular copy of the complete logarithmic beta-prefix tower.

Write

\[
 L_X=\log X+S,\qquad
 C_m=(m!)^2(2m+1)\binom{2m}{m}^2.
\tag{0.8}
\]

Shifted-Legendre projection gives the sharp identity

\[
\boxed{
 \mathcal E_{m,S}(X)
 =\frac{C_m}{L_X^{2m+1}}|B_0(X)|^2
 +\|\mathcal H_{m,S,X,\perp}\|_2^2.}
\tag{0.9}
\]

The remainder is orthogonal to the degree-\(m\) shifted Legendre mode.
The constant is optimal in the abstract support-and-moment class and
is attained by the one-atom field \(X=1\), whose hull has \(L_X=S\).

The scale-balanced energy is

\[
 \mathcal R_{m,S}(X)=L_X^{2m+1}\mathcal E_{m,S}(X).
\tag{0.10}
\]

For every fixed \(m\) and every prescribed schedule \(S_X\ge1\),

\[
\boxed{
 \mathrm{RH}\quad\Longleftrightarrow\quad
 \mathcal R_{m,S_X}(X)=X^{o(1)}.}
\tag{0.11}
\]

This extends the first-derivative cubic renormalization to an infinite
fixed-rung hierarchy. It does not prove the needed energy estimate:
the forward implication uses RH through the beta Mertens bound, and
the reverse implication is exactly another RH criterion.

## 1. Positive carrier, Legendre detector

The beta integral gives

\[
 \int_0^S t^m(S-t)^m\,dt
 =S^{2m+1}\frac{m!^2}{(2m+1)!},
\tag{1.1}
\]

so (0.1) has mass one. Its first \(m-1\) derivatives vanish at both
endpoints. Consequently differentiating the zero extension \(m\)
times creates an ordinary compactly supported function, not a measure
with boundary atoms.

The shifted Rodrigues identity is

\[
 \frac{d^m}{dt^m}\{t^m(S-t)^m\}
 =(-1)^m m!S^mP_m\!\left(\frac{2t}{S}-1\right).
\tag{1.2}
\]

Combining (1.2) with (0.1) proves (0.3). Orthogonality of \(P_m\)
then gives

\[
\boxed{
 \|J_{m,S}\|_2^2
 =\frac{C_m}{S^{2m+1}}.}
\tag{1.3}
\]

The carrier moments are also closed form:

\[
\boxed{
 q_h
 =\frac{(2m+1)!(m+h)!}{m!(2m+h+1)!}S^h.}
\tag{1.4}
\]

In particular \(q_0=1\).

The beta carrier is forced by a variational theorem. Among all real
unit-mass carriers \(Q\) supported in \([0,S]\) whose zero-extended
\(D^mQ\) lies in \(L^2\),

\[
\boxed{
 \|D^mQ\|_2^2\ge\frac{C_m}{S^{2m+1}},}
\tag{1.5}
\]

with equality only for \(Q=Q_{m,S}\) almost everywhere. Indeed,
\(J=D^mQ\) has moments zero below \(m\) and
\(\int t^mJ=(-1)^m m!\). The sharp degree-\(m\) shifted-Legendre
projection gives (1.5), with equality only when \(J\) is proportional
to \(P_m(2t/S-1)\). Integrating \(m\) times with the compact-support
boundary traces recovers (0.1) uniquely. Thus the optimizer in the
larger signed class is already positive: imposing positivity cannot
lower the detector norm.

## 2. The complete triangular transform

For one translate, integration by parts \(m\) times gives

\[
 \int t^kJ_{m,S}(t-\ell)\,dt=0\qquad(k<m)
\tag{2.1}
\]

and

\[
 \int t^{m+r}J_{m,S}(t-\ell)\,dt
 =(-1)^m m!\binom{m+r}{m}
 \sum_{h=0}^{r}\binom rh q_h\ell^{r-h}.
\tag{2.2}
\]

Summing over \(\ell=\log n\) proves (0.6)--(0.7). Equivalently, the
exponential generating functions satisfy

\[
\boxed{
 \mathscr H_{m,S,X}(z)
 =(-z)^m\mathscr Q_{m,S}(z)\mathscr B_X(z).}
\tag{2.3}
\]

Because \(\mathscr Q_{m,S}(0)=1\), the transform after the \(m\)
forced zero rows is triangular and invertible. Higher derivative order
does not destroy any fixed logarithmic beta moment; it delays the
tower by exactly \(m\) rows.

## 3. Sharp support-energy identity

Every \(H=H_{m,S,X}\) is supported in \([0,L_X]\) and is orthogonal to
all polynomials of degree below \(m\). Let

\[
 \phi_{m,L}(t)
 =\sqrt{\frac{2m+1}{L}}
 P_m\!\left(\frac{2t}{L}-1\right).
\tag{3.1}
\]

This is a unit vector in \(L^2([0,L])\). Since the leading coefficient
of \(P_m(2t/L-1)\) is \(\binom{2m}{m}/L^m\), equations (0.6) and (3.1)
give

\[
 \langle H,\phi_{m,L}\rangle
 =(-1)^m\frac{m!\sqrt{2m+1}\binom{2m}{m}}
 {L^{m+1/2}}B_0(X).
\tag{3.2}
\]

Pythagoras proves (0.9), including the exact residual. In particular,

\[
\boxed{
 |B_0(X)|
 \le\frac{L_X^{m+1/2}}{m!\sqrt{2m+1}\binom{2m}{m}}
 \mathcal E_{m,S}(X)^{1/2}.}
\tag{3.3}
\]

Equality in the abstract moment problem holds precisely when the field
is proportional to the shifted \(P_m\). Formula (0.3) realizes that
extremizer with one source atom and carrier width equal to the support
hull. Therefore no argument using only support length, the first \(m\)
moment constraints, and energy can improve the power
\(L^{m+1/2}\).

The whole higher-rung Legendre tower is also explicit. For \(r\ge0\),
put \(k=m+r\),

\[
\begin{aligned}
 d_{m+r}
 &=\int_0^{L_X}H(t)
 P_{m+r}\!\left(\frac{2t}{L_X}-1\right)\,dt,\\
 A_r^{(m)}
 &=\frac{(-1)^m r!L_X^{m+r}}
 {(m+r)!\binom{2m+2r}{m+r}}d_{m+r}.
\end{aligned}
\tag{3.4}
\]

Then \(A_r^{(m)}\) is a triangular combination of
\(B_0,\ldots,B_r\) with leading coefficient one, and for every
\(R\ge0\),

\[
\boxed{
 \mathcal E_{m,S}(X)
 =
 \sum_{r=0}^{R}
 \frac{(2m+2r+1)
 \left[\dfrac{(m+r)!}{r!}\binom{2m+2r}{m+r}\right]^2}
 {L_X^{2m+2r+1}}
 |A_r^{(m)}(X)|^2
 +\|\mathcal H_{m,S,X,>R}\|_2^2.}
\tag{3.5}
\]

As \(R\to\infty\), the remainder decreases to zero by polynomial
density. The \(r=0\) row is exactly (0.9); subsequent rows resolve the
centered logarithmic drift and curvature of the beta prefix after the
forced spectral notch.

Combining the sharp recovery constant with the variational minimum
gives the scale-free support condition number

\[
\boxed{
 \kappa_m(L,S)
 =\frac{L^{2m+1}}{C_m}\frac{C_m}{S^{2m+1}}
 =\left(\frac LS\right)^{2m+1}.}
\tag{3.6}
\]

Since the physical hull satisfies \(L=S+\log X\ge S\), this condition
number is nondecreasing in \(m\), and strictly increasing when \(X>1\).
Higher derivative order therefore cannot improve support-normalized,
diagonal-normalized recovery. Any gain must use source-specific
cancellation beyond support, mass, positivity, and \(L^2\) energy.

This is a hard diagnostic for inverse detector design: at fixed
integer rung, increasing the number of forced vanishing moments raises
the raw support-loss exponent from \(L^{3/2}\) to \(L^{m+1/2}\). Thus
\(m=1\) uniquely minimizes that exponent among these zero-mean
derivative rungs. This is not a finite-\(L\) numerical optimum: the
factorial constants also vary with \(m\). Growing \(m\), weighted or
Sobolev data, alternate normalizations, and arithmetic cancellation in
the complete beta convolution remain outside the no-go.

## 4. Autocorrelation and spectral jet

Let

\[
 \mathcal C_{m,S,X}(u)
 =\int H_{m,S,X}(v)H_{m,S,X}(v+u)\,dv.
\tag{4.1}
\]

Every autocorrelation moment of order below \(2m\) vanishes. At the
first order not forced to vanish, only the middle term of the moment
convolution remains:

\[
\boxed{
 \int u^{2m}\mathcal C_{m,S,X}(u)\,du
 =(-1)^m(2m)!|B_0(X)|^2.}
\tag{4.2}
\]

With Fourier convention
\(\widehat H(\omega)=\int H(t)e^{-i\omega t}dt\), the positive spectral
density \(\mathcal P=|\widehat H|^2\) therefore satisfies

\[
\boxed{
 \mathcal P^{(2m)}(0)=(2m)!|B_0(X)|^2.}
\tag{4.3}
\]

Thus rung \(m\) moves the first potentially nonzero spectral curvature
to order \(2m\), and its magnitude is exactly the same beta prefix. If
\(B_0=0\), that row also vanishes. The forced lower jet is a frequency
notch, not an arithmetic saving.

## 5. All-support RH equivalence

The reverse implication in (0.11) is immediate from (0.9):

\[
 C_m|B_0(X)|^2\le\mathcal R_{m,S}(X).
\tag{5.1}
\]

Hence a subpower renormalized energy gives the beta Mertens criterion
and therefore RH.

For the forward implication, define

\[
 B_0^*(X)=\sup_{1\le y\le X}|B_0(y)|.
\tag{5.2}
\]

At fixed \(m\), (0.3) gives a constant \(K_m<\infty\), independent of
\(S\), such that

\[
 \|J_{m,S}\|_\infty+\operatorname{Var}(J_{m,S})
 \le K_mS^{-m-1}.
\tag{5.3}
\]

Bounded-variation summation of the beta source, pointwise in \(t\),
gives

\[
 |H_{m,S,X}(t)|\le K_mB_0^*(X)S^{-m-1}.
\tag{5.4}
\]

The field is supported on an interval of length \(L_X\), so

\[
 \mathcal E_{m,S}(X)
 \le K_m^2B_0^*(X)^2\frac{L_X}{S^{2m+2}}.
\tag{5.5}
\]

Under RH, \(B_0^*(X)=O_\varepsilon(X^\varepsilon)\). Since \(S\ge1\),

\[
 \mathcal R_{m,S}(X)
 \le K_m^2B_0^*(X)^2
 \left(\frac{L_X}{S}\right)^{2m+2}
 \le K_m^2B_0^*(X)^2(1+\log X)^{2m+2}.
\tag{5.6}
\]

This is \(X^{o(1)}\), uniformly over every width schedule \(S_X\ge1\),
and proves (0.11).

### A normalized growing-rung theorem

For cross-rung comparison the sharp factorial constant must also be
removed. Define

\[
 \mathfrak E_{m,S}(X)
 =\frac{L_X^{2m+1}}{C_m}\mathcal E_{m,S}(X).
\tag{5.7}
\]

The shifted-Legendre inequality gives, for arbitrary moving integer
\(m=m(X)\ge1\) and any moving unit-mass carrier with
\(D^mQ\in L^2\),

\[
\boxed{\mathfrak E_{m,S}(X)\ge|B_0(X)|^2.}
\tag{5.8}
\]

Thus a subpower normalized energy always implies RH; this direction
does not need a fixed differential operator.

For the beta minimizer, elementary monotonicity intervals of \(P_m\)
give the explicit bounded-variation estimate

\[
 \|J_{m,S}\|_\infty+\operatorname{Var}(J_{m,S})
 \le(2m+3)\frac{(2m+1)!}{m!S^{m+1}}.
\tag{5.9}
\]

Repeating the forward argument and dividing by \(C_m\) yields, under
RH,

\[
\boxed{
 \mathfrak E_{m,S}(X)
 \le(2m+1)(2m+3)^2
 \left(\frac{L_X}{S}\right)^{2m+2}B_0^*(X)^2.}
\tag{5.10}
\]

Consequently RH is equivalent to
\(\mathfrak E_{m(X),S_X}(X)=X^{o(1)}\) throughout the safe window

\[
 \log\!\big((2m+1)(2m+3)^2\big)
 +(2m+2)\log(L_X/S_X)=o(\log X).
\tag{5.11}
\]

For fixed \(S\), this includes

\[
 m=o\!\left(\frac{\log X}{\log\log X}\right).
\tag{5.12}
\]

This is a genuine growing-rung theorem, but not an unrestricted one.
Outside (5.11), the displayed forward bound need not be subpower.

## 6. Critical-width phase diagram

For a real width power \(p\ge0\), define

\[
 \mathcal R_{m,p,S}(X)=L_X^p\mathcal E_{m,S}(X).
\tag{6.1}
\]

The two exact thresholds are:

1. The current RH forward bound pays every \(p\le2m+1\), uniformly for
   all \(S_X\ge1\).
2. The sharp support inequality makes every \(p\ge2m+1\) sufficient in
   the reverse direction.

Thus

\[
\boxed{p_c(m)=2m+1}
\tag{6.2}
\]

is the unique power paid in both directions by the current information,
and it is the unique scale-balanced power because
\(\|J_{m,S}\|_2^2\asymp S^{-(2m+1)}\).

The subcritical side has an exact trivial-dilution warning. Young's
inequality and
\(\sum_{n\le X}|a_n|\le4\sqrt X\) give

\[
 \mathcal E_{m,S}(X)\le16C_m\frac{X}{S^{2m+1}}.
\tag{6.3}
\]

If \(p<2m+1\), the schedule

\[
 S_X=X^{1/(2m+1-p)}
\tag{6.4}
\]

makes \(\mathcal R_{m,p,S_X}(X)=O_{m,p}(1)\) without using beta
cancellation. Therefore a subcritical all-support premise can be made
trivial by dilation.

The supercritical side has a complementary adaptive obstruction. The
sharp lower bound gives

\[
 \mathcal R_{m,p,S}(X)
 \ge C_m|B_0(X)|^2L_X^{p-(2m+1)}.
\tag{6.5}
\]

The prefix \(B_0(X)\) is nonzero at infinitely many integer horizons,
because its source coefficients are nonzero infinitely often. Define
the arithmetic-dependent finite schedule on integer horizons by

\[
 S_X=
 \begin{cases}
 \max\!\left\{1,\,
 X^{1/(p-2m-1)}|B_0(X)|^{-2/(p-2m-1)}\right\},
     &B_0(X)\ne0,\\
 1,  &B_0(X)=0.
 \end{cases}
\tag{6.6}
\]

Along the infinite nonzero subsequence this forces
\(\mathcal R_{m,p,S_X}(X)\ge C_mX\). Thus a literal
every-schedule subpower forward statement is unavailable for
\(p>2m+1\), even though the reverse implication remains valid. The
schedule is deliberately adaptive; this does not rule out useful
restricted schedule classes or a future arithmetic estimate there.

There is a parallel raw-energy wedge. If

\[
 \gamma\ge0,\qquad S_X\le X^{\gamma+o(1)},\qquad
 \mathcal E_{m,S_X}(X)=X^{o(1)},
\tag{6.7}
\]

then (3.3) gives

\[
 |B_0(X)|\le X^{(m+1/2)\gamma+o(1)}.
\tag{6.8}
\]

Consequently the beta Dirichlet series excludes zeta zeros in

\[
 \boxed{\Re\rho>\frac12+\left(m+\frac12\right)\gamma.}
\tag{6.9}
\]

At the trivial escape slope \(\gamma=1/(2m+1)\), this boundary lands
exactly at \(\Re\rho=1\). Higher derivative order therefore rotates the
support wedge and the dilution schedule together; it does not open a
free zero-free region.

## 7. Scope and firewalls

| statement | grade |
|---|---|
| positive unit-mass beta carrier (0.1) | **PROVED EXACT** |
| Rodrigues/Legendre detector formula (0.3) | **PROVED EXACT** |
| unique signed-carrier variational optimum (1.5) | **PROVED EXACT** |
| all-order triangular moment transform (0.7) | **PROVED EXACT** |
| sharp support-energy Pythagorean identity (0.9) | **PROVED EXACT** |
| complete higher-rung Legendre tower (3.5) | **PROVED EXACT** |
| exact support condition number (3.6) | **PROVED EXACT** |
| first available autocorrelation/spectral jet (4.2)--(4.3) | **PROVED EXACT** |
| all-support fixed-\(m\) renormalized RH equivalence (0.11) | **PROVED** |
| normalized safe growing-rung RH equivalence (5.7)--(5.12) | **PROVED** |
| critical width power \(p_c=2m+1\) within current bounds | **PROVED** |
| subcritical trivial-dilution schedule | **PROVED** |
| supercritical adaptive-schedule obstruction | **PROVED** |
| raw-energy zero-exclusion wedge | **PROVED** |
| new unconditional subpower beta-energy estimate | **NOT PROVED** |
| unrestricted growing-rung forward/equivalence theorem | **NOT PROVED** |
| improvement from arithmetic convolution beyond support geometry | **NOT PROVED** |
| RH or GRH | **NOT PROVED** |

The unnormalized criterion (0.11) fixes \(m\) before \(X\) varies.
Width \(S_X\) may vary arbitrarily subject to \(S_X\ge1\). Growing
\(m\) is allowed only after the \(C_m\) normalization and within the
explicit window (5.11).

The equality case in (0.9) is an abstract one-atom field. It proves
sharpness for the stated support/moment information and does not claim
that a long arithmetic beta convolution attains equality.

The criterion remains source-faithful and individual: no family-to-
principal extraction is needed. Its missing forward estimate is still
equivalent to RH after the critical renormalization, so this hierarchy
organizes rather than solves the arithmetic difficulty.

No external novelty or priority is claimed without a dedicated
literature comparison.

## 8. Bounded replay

The producer:

- verifies the frozen moment-tower quartet by full Git blob ID;
- constructs \(Q_{m,S}\) and \(D^mQ_{m,S}\) exactly for \(1\le m\le6\);
- checks Rodrigues' formula, unit mass, endpoint vanishing, detector
  norm, and carrier moments using rational polynomial arithmetic;
- verifies the triangular source/field transform through three rows
  above each forced notch;
- checks the sharp and higher-mode constants, support condition number,
  normalized growing-rung factor, spectral jet, critical exponent,
  trivial schedule, and zero-free boundary exactly;
- performs no beta sum, prime enumeration, zeta evaluation, random
  sampling, quadrature, or curve computation.

~~~text
python -B research/l-families/atlas/function_field/ffps_higher_derivative_carrier_hierarchy.py --check
python -O -B research/l-families/atlas/function_field/ffps_higher_derivative_carrier_hierarchy.py --check
python -B -m unittest tests.test_ffps_higher_derivative_carrier_hierarchy
python -O -B -m unittest tests.test_ffps_higher_derivative_carrier_hierarchy
python -m ruff check research/l-families/atlas/function_field/ffps_higher_derivative_carrier_hierarchy.py tests/test_ffps_higher_derivative_carrier_hierarchy.py
python -m ruff format --check research/l-families/atlas/function_field/ffps_higher_derivative_carrier_hierarchy.py tests/test_ffps_higher_derivative_carrier_hierarchy.py
~~~
