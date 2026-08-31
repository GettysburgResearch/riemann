# Absolute powers on an irrational tempered rank-two orbit

Status: **proposed exact local theorem; external novelty unreviewed**
Issue: [#764](https://github.com/gfreund123/riemann/issues/764)
Claim labels: GLO764.IRRATIONAL_ROTATION_ABSOLUTE_POWER_RATIONALITY,
GLO764.IRRATIONAL_ROTATION_EVEN_POWER_MINIMAL_DENOMINATOR, and
GLO764.DENSE_ORBIT_FINITE_SPECTRUM

## Scientific firewall

This packet treats one determinant-one, unramified, tempered local recurrence
with an **irrational** rotation angle. It classifies ordinary generating
functions of the absolute powers \(|u_r|^\lambda\) for real
\(\lambda\geq0\). Absolute value erases phase, so this is not a construction
or obstruction for a complex nonintegral
\(\operatorname{Sym}^{\lambda}\).

The result does not range uniformly over primes. Rational rotation angles are
excluded and can produce periodic counterexamples. Nothing here supplies
ramified factors, a global Euler product, completion, functional equation,
automorphy, motivic origin, an infinite-dimensional or categorical no-go,
an explicit formula, or a zero theorem. There is no RH or GRH consequence.

## 1. Normalization

Fix

\[
0<\theta<\pi,
\qquad
\frac{\theta}{\pi}\notin\mathbb Q,
\qquad
x=2\cos\theta\in(-2,2).
\]

Let

\[
u_0=1,\qquad
u_1=x,\qquad
u_{r+2}=x u_{r+1}-u_r
\quad(r\geq0).
\]

Then

\[
u_r
=\frac{\sin((r+1)\theta)}{\sin\theta}.
\tag{1.1}
\]

Irrationality implies \(\sin((r+1)\theta)\neq0\) for every \(r\geq0\).
For real \(\lambda\geq0\), define

\[
a_r(\lambda)=|u_r|^\lambda.
\]

When \(\lambda=0\), this means \(a_r(0)=1\); no \(0^0\) ambiguity occurs
because the orbit never hits a zero. Set

\[
G_{\lambda,\theta}(T)
=\sum_{r\geq0}a_r(\lambda)T^r.
\tag{1.2}
\]

Rationality means that the analytic germ (1.2) at \(T=0\) belongs to
\(\mathbb C(T)\).

## 2. Exact classification

**Theorem
(GLO764.IRRATIONAL_ROTATION_ABSOLUTE_POWER_RATIONALITY).** Under the
hypotheses above,

\[
G_{\lambda,\theta}(T)\in\mathbb C(T)
\quad\Longleftrightarrow\quad
\lambda\in2\mathbb Z_{\geq0}.
\tag{2.1}
\]

If \(\lambda=2m\), the reduced denominator is

\[
D_{m,\theta}(T)
=\prod_{k=-m}^{m}
  \left(1-e^{2ik\theta}T\right),
\tag{2.2}
\]

and the minimal constant-coefficient recurrence order is exactly

\[
2m+1.
\tag{2.3}
\]

This includes \(m=0\): \(G_{0,\theta}(T)=(1-T)^{-1}\), with minimal order
\(1\).

## 3. Rational series force finite Fourier spectrum

The necessity proof uses the following elementary gate.

**Lemma (GLO764.DENSE_ORBIT_FINITE_SPECTRUM).** Let
\(f:\mathbb R/\pi\mathbb Z\to\mathbb C\) be continuous, and suppose
\(\theta/\pi\) is irrational. If the sequence

\[
b_r=f((r+1)\theta)
\]

satisfies a nonzero constant-coefficient recurrence for all sufficiently
large \(r\), then \(f\) has finite Fourier support. Equivalently, \(f\) is a
trigonometric polynomial in the frequencies \(e^{2ikt}\).

### Proof

An eventual recurrence can be written

\[
\sum_{j=0}^{d}q_j b_{n-j}=0
\quad(n\geq N),
\tag{3.1}
\]

with \(q_0q_d\neq0\) after deleting zero end coefficients. Put
\(c_\ell=q_{d-\ell}\) and

\[
H(t)=\sum_{\ell=0}^{d}c_\ell f(t+\ell\theta).
\tag{3.2}
\]

Equation (3.1) says that \(H((n-d+1)\theta)=0\) for every sufficiently
large \(n\). The tail of an irrational rotation orbit is dense modulo
\(\pi\). Since \(H\) is continuous,

\[
H(t)=0
\quad\text{for every }t\in\mathbb R/\pi\mathbb Z.
\tag{3.3}
\]

Use the Fourier convention

\[
\widehat f(k)
=\frac1\pi\int_0^\pi f(t)e^{-2ikt}\,dt,
\qquad k\in\mathbb Z.
\tag{3.4}
\]

Taking the \(k\)-th Fourier coefficient of (3.3) gives

\[
P(e^{2ik\theta})\widehat f(k)=0,
\qquad
P(z)=\sum_{\ell=0}^{d}c_\ell z^\ell.
\tag{3.5}
\]

The numbers \(e^{2ik\theta}\), \(k\in\mathbb Z\), are pairwise distinct:
equality for two indices would make \(\theta/\pi\) rational. The nonzero
polynomial \(P\) has only finitely many roots. Therefore
\(\widehat f(k)\neq0\) for only finitely many \(k\).

For completeness, Fejér's theorem says that the Cesàro means of the Fourier
series of a continuous periodic function converge uniformly to that
function. With finite Fourier support, those means converge to the
corresponding finite trigonometric polynomial. Hence \(f\) equals that
polynomial. \(\square\)

A rational ordinary generating function has an eventual
constant-coefficient recurrence: if

\[
G(T)=\frac{A(T)}{Q(T)},
\qquad Q(0)=1,
\]

then the coefficients of \(Q(T)G(T)=A(T)\) vanish beyond
\(\deg A\). Thus the lemma applies directly to a rational
\(G_{\lambda,\theta}\).

## 4. The cusp excludes every other real power

Assume first that \(\lambda>0\), and define the continuous
\(\pi\)-periodic function

\[
f_\lambda(t)=|\sin t|^\lambda.
\tag{4.1}
\]

By (1.1),

\[
a_r(\lambda)
=\frac{f_\lambda((r+1)\theta)}
       {(\sin\theta)^\lambda}.
\tag{4.2}
\]

The nonzero constant factor in (4.2) does not affect rationality. If
\(G_{\lambda,\theta}\) were rational, the lemma would make
\(f_\lambda\) a trigonometric polynomial, hence \(C^\infty\).

Near \(t=0\),

\[
f_\lambda(t)
=|t|^\lambda h_\lambda(t),
\qquad
h_\lambda(t)
=\left|\frac{\sin t}{t}\right|^\lambda,
\qquad
h_\lambda(0)=1.
\tag{4.3}
\]

The factor \(h_\lambda\) is positive and \(C^\infty\) near \(0\), as is its
reciprocal. Therefore \(f_\lambda\) is \(C^\infty\) at \(0\) if and only if
\(|t|^\lambda\) is.

If \(\lambda\) is not an integer, let

\[
n=\lfloor\lambda\rfloor+1.
\]

On \(t>0\), the \(n\)-th derivative of \(t^\lambda\) is

\[
\lambda(\lambda-1)\cdots(\lambda-n+1)t^{\lambda-n},
\tag{4.4}
\]

whose coefficient is nonzero and whose magnitude diverges as
\(t\downarrow0\). Thus \(|t|^\lambda\notin C^n\).

If \(\lambda=n\) is an odd positive integer, the \(n\)-th one-sided
derivatives of \(|t|^n\) at \(0\) are \(n!\) and \(-n!\), so the \(n\)-th
derivative is discontinuous. Finally, if \(\lambda=2m\) is even,

\[
|t|^{2m}=t^{2m}
\]

is smooth. We have proved

\[
|\sin t|^\lambda\in C^\infty(\mathbb R)
\quad\Longleftrightarrow\quad
\lambda\in2\mathbb Z_{\geq0},
\tag{4.5}
\]

with \(\lambda=0\) understood separately as the constant function \(1\).
This proves the nonrational direction of (2.1).

## 5. Even powers and the minimal denominator

For \(m\geq0\), the exact Fourier expansion is

\[
\sin^{2m}t
=2^{-2m}
\sum_{k=-m}^{m}
(-1)^k\binom{2m}{m-k}e^{2ikt}.
\tag{5.1}
\]

Every coefficient in (5.1) is nonzero. Substitution of
\(t=(r+1)\theta\) into (4.2) gives

\[
a_r(2m)
=\sum_{k=-m}^{m}
A_k\left(e^{2ik\theta}\right)^r,
\tag{5.2}
\]

where

\[
A_k
=\frac{2^{-2m}(-1)^k\binom{2m}{m-k}e^{2ik\theta}}
       {\sin^{2m}\theta}
\neq0.
\tag{5.3}
\]

Therefore

\[
G_{2m,\theta}(T)
=\sum_{k=-m}^{m}
\frac{A_k}{1-e^{2ik\theta}T}.
\tag{5.4}
\]

Irrationality makes the \(2m+1\) characteristic roots
\(e^{2ik\theta}\) pairwise distinct. At the pole
\(T=e^{-2ik\theta}\), the corresponding residue is

\[
-A_ke^{-2ik\theta}\neq0,
\tag{5.5}
\]

while all other summands are analytic. No denominator factor cancels.
Equations (2.2) and (2.3) follow, completing the theorem.
\(\square\)

The denominator is the same determinant-one weight product that appears for
the scalar even power \(u_r^{2m}\). This statement remains only a local
scalar recurrence statement; it is not a full symmetric-power Euler-factor
construction.

## 6. Hostile controls and exact replay

The source-lineage base is commit
\(f2f8044fb867fa7f109be92350f3f194479d36c6\). This packet imports the first
local-power packet at its metadata-corrected state
\(6b5fe8f112b38e59bd73ad80b448d52fff2da2d6\), with exact file, payload,
and Git-blob
hashes in the colocated sources manifest.

The adjacent dependency-free producer is reused for canonical hashing,
Dickson/Laurent conversion, and normalized even-power numerator checks. It
declares the repository arithmetic class EXACT_RATIONAL; its method is exact
integer/rational Laurent-polynomial, Fourier, recurrence, cusp-control, and
formal coefficient algebra. The new producer:

1. reconstructs the exact scaled coefficients
   \((-1)^k\binom{2m}{m-k}\) in (5.1);
2. independently forms the Laurent denominator
   \(\prod_{k=-m}^{m}(1-q^kT)\) and matches it to the inherited weight
   product under \(q=e^{2i\theta}\);
3. checks exact tail annihilation through the declared finite bound for
   \(0\leq m\leq6\);
4. records the nonzero roots and minimal orders \(2m+1\);
5. checks rational cusp controls including half-integers and odd integers;
6. treats \(\lambda=0\) separately; and
7. records the hostile rational-angle example
   \(\theta=\pi/2,\lambda=1/2\), for which
   \((|u_r|^\lambda)=(1,0,1,0,\ldots)\) and
   \(G(T)=(1-T^2)^{-1}\).

The last example proves that the irrationality hypothesis cannot simply be dropped.

Replay from the repository root:

    python research/l-families/atlas/generalized/irrational_rotation_absolute_power_rationality.py --check
    python -O research/l-families/atlas/generalized/irrational_rotation_absolute_power_rationality.py --check
    python -m unittest tests.test_irrational_rotation_absolute_power_rationality
    python -O -m unittest tests.test_irrational_rotation_absolute_power_rationality

The replay uses exact integer/rational Laurent and Fourier algebra. It uses
no floating point, random samples, external symbolic engine, or prime, curve,
field, conductor, or zero enumeration. The finite cusp rows are controls;
the all-real classification is the proof in Sections 3--5.

## 7. L0--L9 survival ledger

| Object | L0 | L1 | L2 | L3 | First stop |
|---|---|---|---|---|---|
| \(\lambda=2m\) on an irrational tempered orbit | defined | \(|ab|^{2m}=|a|^{2m}|b|^{2m}\) for multiplicative inputs | formal under L1 | local rational factor of minimal degree \(2m+1\) | L4 |
| \(\lambda\geq0\) not even | defined on the nonzero orbit | \(|ab|^\lambda=|a|^\lambda|b|^\lambda\) for multiplicative inputs | formal under L1 | fails at every irrational-rotation local recurrence | L3 |

Levels L4--L9 respectively ask for weight/determinant/duality and ramified
coherence; completion data; analytic continuation and functional equation;
functorial compatibilities; a realization; and a principled explicit formula
or zero theory. None is established here.

## 8. Nearby prior art and novelty firewall

Oliver Knill and John Lesieutre,
[*Analytic continuation of Dirichlet series with almost periodic
coefficients*](https://abel.math.harvard.edu/~knill/kam/papers/denjoy/index.html),
study series \(\sum g(n\alpha)z^n\) generated by irrational rotations. Their
discussion includes meromorphic continuation for trigonometric-polynomial
\(g\), the Fourier partial-fraction expansion, and stronger natural-boundary
results under additional Diophantine, smoothness, and Fourier-support
hypotheses.

That work is direct nearby prior art. This packet asks a narrower but
different question: exact **rationality**, equivalently eventual recurrence,
for the specific function \(g(t)=|\sin t|^\lambda\), for every irrational
\(\theta/\pi\). Its necessity proof uses a translate identity and finite
Fourier support; it does not assert the natural-boundary conclusions of the
nearby work. Conversely, a meromorphic continuation is not by itself a
rationality classification.

The argument here is built from standard recurrence, irrational-rotation,
Fourier-uniqueness, and cusp-regularity facts. A self-contained proof is not
a priority proof. The exact formulation remains **external novelty
unreviewed**, requires specialist comparison before citation as new, and this
packet makes no novelty claim.

## 9. Known gaps

The theorem excludes rational \(\theta/\pi\), endpoints
\(\theta=0,\pi\), signed or branched noninteger powers, determinant other
than \(1\), ramified factors, and any demand for one degree bound uniform
over a global prime family. It neither constructs nor rules out a global or
infinite-dimensional generalized \(L\)-object.
