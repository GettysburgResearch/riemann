# A degree-six tensor / symmetric-fifth spectral intersection

## Status

This packet proves an exact local theorem.  Two apparently different
degree-six constructions have the same **complete** normalized Frobenius
spectrum on two explicit Chebyshev graph families:

\[
 H^1(E_A)\otimes\operatorname{Sym}^2H^1(E_B)
 \quad\hbox{and}\quad
 \operatorname{Sym}^5H^1(E_C).
\]

It also proves that these two graphs exhaust all rational coefficient
solutions, identifies the finite algebraic residuals at torus orders
\(7,12,14\), counts every integral Hasse-lattice solution over an odd prime
power, and places the result in an exact all-symmetric-power torus ladder.

The calculation is deliberately light.  It transforms five locked trace
histograms, uses a small sparse polynomial engine over `Fraction`, and never
enumerates a field, curve, model, or database row.  There are no floats,
random samples, or runtime symbolic packages.

## 1. Sign, weight, and dilation conventions

All three elliptic inputs use geometric traces:

\[
 P_t(T)=1-tT+qT^2,
 \qquad t\in\{A,B,C\}.
 \tag{1}
\]

Choose \(s\) in an algebraic closure with \(s^2=q\), and put

\[
 x=A/s,\qquad y=B/s,\qquad z=C/s.
 \tag{2}
\]

The tensor construction
\(\operatorname{Std}(E_A)\otimes\operatorname{Sym}^2(E_B)\) has degree six
and weight three.  The target \(\operatorname{Sym}^5(E_C)\) has degree six
and weight five.  Thus the correctly typed raw comparison is

\[
 \boxed{
 P_{A\otimes\operatorname{Sym}^2B}(qT)
 =P_{\operatorname{Sym}^5C}(T).}
 \tag{3}
\]

Equation (3) is not an equality of the two unscaled factors.  Replacing
\(B\) by \(-B\) does not change \(\operatorname{Sym}^2(E_B)\); that is the
source of the two signs on each graph below.  The signs of \(A\) and \(C\)
retain their ordinary geometric-trace meaning.

## 2. Three exact coefficients determine each factor

At a normalized torus element, the tensor eigenvalues are

\[
 u^{\pm1}v^2,\quad u^{\pm1},\quad u^{\pm1}v^{-2},
 \qquad x=u+u^{-1},\quad y=v+v^{-1}.
\]

The first three elementary symmetric functions are

\[
\begin{aligned}
 e_1^{\rm ten}&=x(y^2-1),\\
 e_2^{\rm ten}&=(y^2-1)(x^2+y^2-3),\\
 e_3^{\rm ten}&=x(x^2+y^4-2y^2-2).
\end{aligned}
\tag{4}
\]

For \(\operatorname{Sym}^5\), whose weights are
\(w^{\pm1},w^{\pm3},w^{\pm5}\), they are

\[
\begin{aligned}
 e_1^{(5)}&=z(z^2-1)(z^2-3),\\
 e_2^{(5)}&=(z^2-1)(z^2-3)(z^2-z-1)(z^2+z-1),\\
 e_3^{(5)}&=z(z^2-3)(z^2-2)(z^2-z-1)(z^2+z-1).
\end{aligned}
\tag{5}
\]

The producer derives (4) and (5) independently from the first three power
sums and Newton identities.  It does not import the displayed formulas as
unchecked premises.

Before dilation, the tensor elementary coefficients are

\[
\begin{aligned}
 a_1&=A(B^2-q),\\
 a_2&=q(B^2-q)(A^2+B^2-3q),\\
 a_3&=q^2A(qA^2+B^4-2qB^2-2q^2),
\end{aligned}
\tag{6}
\]

and its factor is

\[
 [1,-a_1,a_2,-a_3,q^3a_2,-q^6a_1,q^9].
 \tag{7}
\]

After \(T\mapsto qT\), set

\[
\begin{aligned}
 d_1&=qA(B^2-q),\\
 d_2&=q^3(B^2-q)(A^2+B^2-3q),\\
 d_3&=q^5A(qA^2+B^4-2qB^2-2q^2).
\end{aligned}
\tag{8}
\]

Then (7) becomes

\[
 [1,-d_1,d_2,-d_3,q^5d_2,-q^{10}d_1,q^{15}],
 \tag{9}
\]

the same reciprocal shape as \(\operatorname{Sym}^5\).  The independent
plethystic cross-check from the locked predecessor is

\[
 e_2^{(5)}=qE_8+q^3E_4+q^5,
 \qquad
 e_3^{(5)}=q^3E_9+q^5E_5+q^6E_3.
 \tag{10}
\]

Thus equality of the three displayed coefficients is equality of the full
degree-six factors.

## 3. Complete rational intersection theorem

### The theorem

For \(A,B,C,q\in\mathbb Q\) with \(q\ne0\), equation (3) holds if and only
if one of the following alternatives holds:

\[
 \boxed{B^2=C^2,\qquad qA=C(C^2-3q),}
 \tag{11}
\]

or

\[
 \boxed{A=C,\qquad qB^2=(C^2-2q)^2.}
 \tag{12}
\]

In normalized coordinates these are precisely four signed graphs:

\[
 \boxed{x=z^3-3z,\quad y=\pm z,}
 \tag{13}
\]

and

\[
 \boxed{x=z,\quad y=\pm(z^2-2).}
 \tag{14}
\]

The sufficiency is visible at the level of weights.  On (13), take
\(u=w^3\) and \(v=\pm w\).  On (14), take \(u=w\) and \(v^2=w^4\).
In either case

\[
 \{u^{\pm1}v^2,u^{\pm1},u^{\pm1}v^{-2}\}
 =\{w^{\pm1},w^{\pm3},w^{\pm5}\}
 \tag{15}
\]

with multiplicity.

### Exact necessity certificate

Let \(f_i=e_i^{\rm ten}-e_i^{(5)}\), and let
\(I=(f_1,f_2,f_3)\subset\mathbb Q[x,y,z]\).  A deterministic exact
Buchberger replay, with lexicographic order \(x>y>z\), produces a five-row
reduced basis.  Two load-bearing rows factor as

\[
\begin{aligned}
 &(y^2-z^2)\bigl(y^2-(z^2-2)^2\bigr)
   (y^2+z^4-3z^2-1),\\
 &(y^2-z^2)\bigl(y^2-(z^2-2)^2\bigr)
   p_7^+(z)p_7^-(z),
\end{aligned}
\tag{16}
\]

where

\[
 p_7^+(z)=z^3+z^2-2z-1,
 \qquad
 p_7^-(z)=z^3-z^2-2z+1.
 \tag{17}
\]

The fixture stores every term of the reduced basis.  The producer recomputes
it from the three input differences, interreduces it, and checks all ten
S-polynomial remainders exactly.  Thus (16) is an ideal certificate, not a
sampled factorization.

Both cubics in (17) are monic and have neither \(+1\) nor \(-1\) as a root;
the rational-root theorem makes them irreducible over \(\mathbb Q\).  For
rational raw data, \(z=C/s\) lies in \(\mathbb Q(s)\), whose degree over
\(\mathbb Q\) is at most two.  It therefore cannot satisfy either irreducible
cubic.  Every rational raw-trace solution must consequently lie on

\[
 y^2=z^2
 \quad\hbox{or}\quad
 y^2=(z^2-2)^2.
 \tag{18}
\]

Substituting \(y=\pm z\) gives

\[
\begin{aligned}
 f_1&=(z^2-1)(x-z^3+3z),\\
 f_2&=(z^2-1)(x-z^3+3z)(x+z^3-3z),
\end{aligned}
\tag{19}
\]

and \(f_3\) has the factor \(x-z^3+3z\).  Away from \(z^2=1\), this is
(13).  At \(z^2=1\), the only second value is \(x=z\), already on (14).

Substituting \(y=\pm(z^2-2)\) gives

\[
\begin{aligned}
 f_1&=(x-z)(z^2-1)(z^2-3),\\
 f_2&=(x-z)(x+z)(z^2-1)(z^2-3),
\end{aligned}
\tag{20}
\]

and \(f_3\) has the factor \(x-z\).  Away from \(z^2=1,3\), this is (14).
The case \(z^2=1\) contributes only (13) and (14); \(z^2=3\) is the
order-12 algebraic residual treated next.  It supplies no rational raw-trace
solution.  This completes the necessity proof without using the finite
replay.

## 4. The finite algebraic residuals

The intersection over \(\overline{\mathbb Q}\) has extra zero-dimensional
pieces.  They are exactly cyclotomic.

### Order 12

Adjoining \(z^2-3\) to \(I\) gives the exact reduced basis

\[
 x(x^2-3),\qquad x(y^2-1),\qquad
 (y^2-1)(y^2-3),\qquad z^2-3.
 \tag{21}
\]

The \(y^2=3,x=0\) points lie on (13), and \(y^2=1,x=z\) lies on (14).
The additional points are

\[
 \boxed{z^2=3,\quad y^2=1,\quad x=0\text{ or }x=-z.}
 \tag{22}
\]

These are the primitive-order-12 trace stratum.  If the raw traces and
\(q\) were rational, then \(C^2=3q\) and \(B^2=q\), so
\((C/B)^2=3\), impossible in \(\mathbb Q\).

### Orders 7 and 14

The exact trace identities

\[
 C_7(z)-2=(z-2)p_7^+(z)^2,
 \qquad
 C_7(z)+2=(z+2)p_7^-(z)^2
 \tag{23}
\]

identify (17) with primitive order-seven and order-fourteen trace classes.
The restricted ideals reduce to

\[
\begin{array}{ll}
 p_7^+(z)=0:&p_7^+(y)p_7^-(y)=0,\quad x=C_4(y),\\
 p_7^-(z)=0:&p_7^+(y)p_7^-(y)=0,\quad x=-C_4(y),
\end{array}
\tag{24}
\]

where \(C_4(y)=y^4-4y^2+2\).  Each line in (24) is stored and recomputed as a
complete reduced restricted basis.  Since the target trace has degree three,
it cannot equal \(C/s\) with \(C,q\in\mathbb Q\): the latter lies in the
extension \(\mathbb Q(s)\) of degree at most two.  Hence (22)--(24) do not
alter the rational theorem.

The order labels are statements about normalized semisimple torus spectra.
They do not assert an elliptic curve, coefficient field, or compatible
global family realizing those algebraic points.

## 5. Integral Hasse-lattice theorem

Let \(q=p^e\), where \(p\) is an odd prime and \(e\ge1\), and restrict
\(A,B,C\) to the integral Hasse interval.

For (11), integrality of \(A\) is equivalent to

\[
 q\mid C(C^2-3q)
 \quad\Longleftrightarrow\quad
 q\mid C^3
 \quad\Longleftrightarrow\quad
 p^{\lceil e/3\rceil}\mid C.
 \tag{25}
\]

No extra Hasse condition is needed for \(A\), since
\(A/s=T_3(C/s)\) and \(T_3(2\cos\theta)=2\cos3\theta\).  Put

\[
 H=\lfloor2\sqrt q\rfloor,\qquad
 d=\lceil e/3\rceil,\qquad
 h=\left\lfloor H/p^d\right\rfloor.
\]

There are \(2h+1\) possible values of \(C\).  Every nonzero one has two
choices \(B=\pm C\), while \(C=0\) has only one distinct choice.  Thus the
first branch contains

\[
 \boxed{4h+1}
 \tag{26}
\]

distinct ordered triples.

For (12), if \(e\) is odd and the two sides are nonzero, their
\(p\)-adic valuations have opposite parity:

\[
 e+2v_p(B)
 \quad\hbox{versus}\quad
 2v_p(C^2-2q).
\]

The zero fallback would require \(C^2=2q\), impossible for odd \(q\).
Therefore branch two is empty at every nonsquare odd prime power.

If \(e=2k\), write \(s=p^k\).  Branch two becomes

\[
 A=C,\qquad sB=\pm(C^2-2q).
 \tag{27}
\]

Its integrality condition is \(s\mid C^2\), so

\[
 C=p^{\lceil k/2\rceil}m,\qquad
 |m|\le2p^{\lfloor k/2\rfloor}.
\]

The right side of (27) never vanishes.  Hence branch two has

\[
 \boxed{8p^{\lfloor k/2\rfloor}+2}
 \tag{28}
\]

triples.  The two branches overlap exactly at
\(A=C=\pm2p^k\), \(B=\pm2p^k\), four triples.  Combining (26)--(28), and
using \(h=2p^{\lfloor k/3\rfloor}\), gives the closed square-field count

\[
 \boxed{
 N\bigl(p^{2k}\bigr)
 =8p^{\lfloor k/3\rfloor}
  +8p^{\lfloor k/2\rfloor}-1.}
 \tag{29}
\]

For example, \(q=9\) has exactly 15 Hasse-lattice triples.

Equations (25)--(29) classify coefficient-lattice points.  This packet does
not import Waterhouse realization, construct three curves, or relate their
isogeny classes.

## 6. An exact all-\(r\) spectral ladder

The two degree-six graphs are the \(r=2\) rung of a universal normalized
torus identity.  For every integer \(r\ge1\),

\[
 \operatorname{Std}(w^{r+1})\otimes\operatorname{Sym}^r(w)
 \sim_{\rm spectrum}
 \operatorname{Sym}^{2r+1}(w),
 \tag{30}
\]

and

\[
 \operatorname{Std}(w)\otimes\operatorname{Sym}^r(w^2)
 \sim_{\rm spectrum}
 \operatorname{Sym}^{2r+1}(w).
 \tag{31}
\]

This needs no computation.  In (30), the positive translate is

\[
 (r+1)+\{r,r-2,\ldots,-r\}=\{2r+1,2r-1,\ldots,1\},
\]

and the negative translate supplies all negative odd weights.  In (31),
the two sets

\[
 +1+2\{r,r-2,\ldots,-r\},
 \qquad
 -1+2\{r,r-2,\ldots,-r\}
\]

interlace to the same complete odd interval
\(\{-(2r+1),\ldots,-1,1,\ldots,2r+1\}\).

The tensor side has weight \(r+1\), while the target has weight \(2r+1\).
The raw dilation is therefore \(T\mapsto q^{r/2}T\).  For odd \(r\), this
requires a chosen square root of \(q\), exactly as in the predecessor
\(SO(4)/\operatorname{Sym}^3\) packet.  At \(r=2\), it is the clean
integer dilation \(T\mapsto qT\) in (3).

The producer checks the weight unions through \(r=12\), but the proof is the
two displayed interval decompositions.  Only \(r=2\) receives a complete
rational converse here; (30)--(31) are universal sufficient loci, not a
claim that no other cyclotomic intersections occur for general \(r\).

## 7. A moment detector misses the distinction until degree six

Clebsch--Gordan recursion gives

| moment degree | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| independent `Std x Sym2` product | 1 | 0 | 1 | 0 | 6 | 0 | 75 | 0 | 1274 |
| `Sym5` principal slice | 1 | 0 | 1 | 0 | 6 | 0 | 111 | 0 | 2666 |

Thus the two thin compact families agree through the fourth trace moment and
first separate at degree six.  Generic \(USp(6)\) standard trace has moments

\[
 1,0,1,0,3,0,15
\]

through degree six, so both thin constructions already separate from generic
\(USp(6)\) at degree four.  Complete coefficient support sees the two graph
intersections directly; trace moments alone do not distinguish their compact
origins before degree six.

## 8. Locked replay and resource boundary

The complete trace supports in `genus1_cubic_family_laws.json` give

\[
 7^3+9^3+11^3+13^3+15^3=7{,}975
\]

ordered trace triples.  Every one is compared by complete degree-six factor,
and every equality is checked against (11)--(12):

| \(q\) | factor-equal support triples | represented ordered marked-model triples |
|---:|---:|---:|
| 3 | 5 | 80 |
| 5 | 1 | 8,000 |
| 7 | 1 | 74,088 |
| 11 | 1 | 10,648,000 |
| 13 | 1 | 3,796,416 |

At \(q=3\), the five support triples are \((0,0,0)\) and
\((0,\pm3,\pm3)\).  In each other locked prime field only \((0,0,0)\)
survives.  The separate synthetic \(q=9\) Hasse replay has exactly 15
triples and exercises both graph orientations.

The total declared ledger is below the strict exclusive 20,000-unit cap.  It
includes the 7,975 locked triples, 2,197 synthetic triples, every exact
leading-term reduction, and every Buchberger S-pair.  The five upstream JSON
payloads and producers, together with this producer, note, and test, are
LF-normalized SHA-256 locked.

Replay from the repository root:

```text
python -B research/l-families/atlas/function_field/elliptic_tensor_sym2_sym5_spectral_intersection.py --check
python -B -O research/l-families/atlas/function_field/elliptic_tensor_sym2_sym5_spectral_intersection.py --check
python -B -m unittest tests.test_elliptic_tensor_sym2_sym5_spectral_intersection
python -B -O -m unittest tests.test_elliptic_tensor_sym2_sym5_spectral_intersection
```

## 9. Interpretation firewall

What is proved is local and exact: coefficient formulas, complete-factor
intersection, algebraic residual ideals, Hasse-lattice counts, weight-union
identities, moments, and locked finite replays.

What is not proved:

- an equality of the unscaled factors of different weights;
- a representation homomorphism identifying the two source constructions;
- elliptic realization of every Hasse-lattice trace;
- a curve correspondence, isogeny among three curves, or family-wide
  geometric relation;
- a compatible system, global Euler product, automorphic transfer, or
  cross-prime identity;
- a literature-priority claim for the Chebyshev identities or their exact
  rigidity packaging; or
- any analytic continuation, zero-free region, RH, or GRH consequence.

The useful conclusion is narrower and sharper: even a complete local factor
can fail to recover its functorial origin, and this failure propagates along
an exact all-symmetric-power torus ladder.
