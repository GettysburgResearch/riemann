# A quantitative limitation of the rectangular cubic size estimates

Status: proved feasibility statement for an explicitly specified system of
exponent inequalities; this is not a counterexample to a character-sum
estimate. No new zero-free boundary is claimed.

Scope: the ordinary cubic character means obtained after the second
Poisson step in a cubic raw inverse consumer. The calculation includes
every fixed copied product, the imported off-diagonal Gram inequality,
the current pointwise Möbius bound, and functional-equation reflection of
full smooth factors. It does not include cancellation between convolution
terms or between signed Poisson rows.

Dependencies: `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`,
the cubic first-moment paper, `sections/background-type1.tex`, Lemma
`lem:cubic-extensions`, and `sections/dual.tex`, Lemma
`lem:character-gram` and the copied-product argument. The exact source
hashes are recorded in the frozen third-pass `SOURCES.json` at
`GettysburgResearch/riemann@f11e86684905c6417683a9f45ac75c223da6a162`.

What was run: the displayed inequalities were derived algebraically from
the source estimates. No finite arithmetic experiment is being used as
evidence for an asymptotic assertion.

## 1. The diagonal target and the higher identity

Write the column length as $Y$, the primitive squarefree row-conductor
length as $P=Y^p$, and a large-value set size as $R=Y^r$. In the main
common-factor block of the cubic raw inverse consumer, $p$ is the exponent
of its original row range $H=Y^p$. Its required ordinary second-moment
exponent is $p+1$. The generic cubic sieve gives $(2p+5)/3$ when
$1/2\le p\le2$; its loss over the diagonal is $(2-p)/3$.

For every fixed integer $k\ge2$, let
$m=\mu 1_{N\le Y_0^{1/k}}$, with $Y_0$ exceeding the support endpoint.
Convolution is over ideals. The function $E=\delta_1-m*1$ vanishes up to
$Y_0^{1/k}$, so $E^{*k}$ vanishes up to $Y_0$. Convolving its binomial
expansion with $\mu$ proves the exact identity

\[
\mu=\sum_{j=1}^k(-1)^{j-1}\binom{k}{j}
             m^{*j}*1^{*(j-1)}\qquad(Nn\le Y_0).                 \tag{1}
\]

Characters including their original zeros, punctures, and fixed angular
twists distribute across (1). After a common smooth partition and Mellin
separation, its factors have lengths $Y^{a_i}$, with
$\sum_i a_i=1+o(1)$ and each Möbius factor at most $1/k+o(1)$.
The $j=k$ branch allows all $k$ Möbius factors to have exponent $1/k$
and every full factor to have exponent zero. Therefore replacing the
two-factor identity by arbitrarily high fixed order does not force a
positive-length full factor.

## 2. The complete size-inequality system used here

Let factor $i$ have absolute value $Y^{v_i+o(1)}$ on the selected rows.
A copied product of total length $Y^z$ and value $Y^w$ obeys the cubic
sieve inequality

\[
r+2w\le z+\max\{p,z,2(p+z)/3\}.                              \tag{2}
\]

The ordinary large sieve gives
$r+2w\le z+\max(2p,z)$, which is weaker than (2). Trivial size gives
$v_i\le a_i$, cardinality gives $r\le p$, and the current uniform
reciprocal-Hecke input permits $v_i\le\beta a_i$ for a Möbius factor.

The source's off-diagonal row bound is

\[
\sum_{p'\ne p}|T_{p,p'}|^2
 \ll (PZ)^\epsilon Z\{P+P^2Z^{-2/3}\}.
\]

The Bombieri--Halász--Montgomery step gives
$R Y^{2w}\ll Y^{o(1)}Z\{Z+R^{1/2}[Z(P+P^2Z^{-2/3})]^{1/2}\}$.
Consequently at least one of its diagonal and off-diagonal terms must
have adequate size. In exponents this is exactly

\[
r\le\max\{2z-2w,
      3z+\max(p,2p-2z/3)-4w\}.                               \tag{3}
\]

Using (3) as a simultaneous pair of upper bounds would be invalid: its
right side is a maximum, since either summand can support the inequality.

## 3. A feasible model for every real multiplicity

Put

\[
\rho=\frac{3-\sqrt2}{2},\qquad
r=\frac p{\sqrt2},\qquad v_i=\rho a_i.                       \tag{4}
\]

Assume $0<p<2$, $\sum_i a_i=1$, and $a_i\le p/2$ for every positive
factor. Taking $k\ge2/p$ in the branch described above supplies such a
length pattern. Since $\rho=0.792893\ldots<\beta$ at the currently used
boundary, the pointwise Möbius estimate and all trivial constraints allow
(4).

In fact (2)--(3) hold for **every real $z\ge0$** with $w=\rho z$.
This is stronger than checking the integer multiplicities obtainable
from any one fixed identity.

For (2), if $z\le p/2$, its right side minus its left side is
$p-r-(2\rho-1)z$, which is nonnegative and vanishes at $z=p/2$.
If $p/2\le z\le2p$, the difference has slope
$5/3-2\rho=\sqrt2-4/3>0$ and is zero at the left endpoint.
For $z\ge2p$, it is $2(1-\rho)z-r\ge0$.

For (3), the diagonal alternative is

\[
D(z)=(\sqrt2-1)z.
\]

For $z\le3p/2$, its off-diagonal alternative is
$O_0(z)=2p+(2\sqrt2-11/3)z$. This decreases to
$(3\sqrt2-7/2)p$, which is strictly greater than $p/\sqrt2$.
For $z\ge3p/2$, that alternative is
$O_1(z)=p+(2\sqrt2-3)z$. The increasing $D$ and decreasing $O_1$
cross at

\[
z_*=(1+1/\sqrt2)p,
\qquad D(z_*)=O_1(z_*)=p/\sqrt2.
\]

Their maximum is therefore always at least $r$. This proves (3).

## 4. Full-factor functional equations do not exclude this model

At bounded height, reflection of a full smooth factor of length exponent
$a\le p/2$ has dual length $a^*=p-a$ and value exponent
$v^*=p/2+(\rho-1)a$. The conductor-dependent root number has modulus one
and stays outside the polynomial. Directly,

\[
v^*-\rho a^*=(2\rho-1)(a-p/2)\le0.                          \tag{5}
\]

Any mixture of original and reflected copied factors thus has
$w\le\rho z$. Decreasing $w$ only weakens the necessary inequalities
(2)--(3), so all remain valid. The all-full-factors-subpower branch of
(1) already avoids the need for any such reflection.

This calculation concerns the loss-free, bounded-height reflection.
Conductor and height losses cannot improve the inequalities.

## 5. Quantitative consequence and remaining input

The feasible original second moment has exponent

\[
E=r+2\sum_i v_i=3-\sqrt2+p/\sqrt2.
\]

Its excess over the required $p+1$ is

\[
E-(p+1)=(2-p)(1-1/\sqrt2)>0\qquad(p<2).                     \tag{6}
\]

For the concrete proposed cubic raw target $p=28/25$, which would yield
the boundary $1/2+p/3=131/150$, the remaining permitted loss is

\[
\frac{22}{25}(1-1/\sqrt2)=0.2577460326\ldots.
\]

Thus a fixed saving below the generic cubic sieve ceiling does not reach
the necessary diagonal estimate. Even arbitrarily high fixed short
identities, every real copied length, the present Gram estimate, the
current uniform Möbius pointwise bound, and full-factor functional
equations together do not imply that estimate through these size
inequalities.

This is a limitation of this explicitly listed argument, not an
arithmetic counterexample. New information could exclude the model:
for example a genuinely stronger structured high-moment estimate,
cancellation among the signed terms of (1), a sharper Gram estimate
retaining the arithmetic large-value set, or cancellation in the signed
Poisson kernel before taking absolute values. An ordinary cubic fourth
moment would address the branch with two half-length full factors; it
does not by itself eliminate the branch with only positive-length
Möbius factors.
