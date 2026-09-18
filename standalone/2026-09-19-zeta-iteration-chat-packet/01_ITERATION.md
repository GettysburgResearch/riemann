# 01 — Literal composition, exponential feedback, and inverse trees

Source turn: U1/A1, with the spiral correction from U2/A2. Status: elementary
analytic deductions, numerical examples, and explicitly experimental literature.
This chapter is not an RH proof. References are keyed in [SOURCES](SOURCES.md).

## The original object

The question was about

$$
\zeta^{\circ n}(s)=\zeta(\zeta(\cdots\zeta(s)\cdots)),
$$

on the domain where all required intermediate evaluations exist. This is not
zeta(s)^n. Woon [W98] investigated Julia/Mandelbrot-type pictures; Brent [BR17]
investigated inverse orbits. Their dynamical pictures motivate questions, not
zero-location theorems.

## Pairwise pole/exponential feedback

As sigma=Re(s) tends to +infinity, uniformly in Im(s),

$$
\zeta(s)-1=2^{-s}(1+O((2/3)^\sigma)),\qquad
\zeta(1+\epsilon)=\epsilon^{-1}+\gamma_E+O(\epsilon).
$$

Substitution gives

$$
\zeta^{\circ2}(s)=2^s(1+O((2/3)^\sigma))+\gamma_E+O(2^{-\sigma}).
$$

The mechanism is simple: the pole at 1 inverts the leading small term 2^{-s}.
On a sufficiently large positive real orbit, a pair of iterations therefore
acts like an exponential, while the intervening iterate is very close to 1.

The original response displayed

    x -> 1+2^{-x} -> 2^x -> 1+2^{-2^x} -> 2^{2^x} -> ...

as intuition. It must remain SCHEMATIC. In particular, the relative asymptotic
F(x)~2^x, where F=zeta^{circ2}, cannot be substituted repeatedly into an
exponent to conclude F(F(x))~2^{2^x}. Already

$$
F(x)=2^x-(4/3)^x+\gamma_E-1+o(1)
$$

on the positive real axis. The correction -(4/3)^x tends to minus infinity,
so F(F(x))/2^{2^x} tends to zero, not one. This refinement follows by retaining
the n=3 and n=4 terms in zeta(x)-1, expanding its reciprocal, and using the
Laurent series at 1. It is an editorial clarification of the original heuristic,
not a claimed tetration conjugacy or a new RH result.

## Numerical real dynamics

The original orbit from 2 was recomputed at 40 decimal working precision:

| n | zeta^{circ n}(2), rounded |
|---|---:|
| 0 | 2 |
| 1 | 1.64493406684822644 |
| 2 | 2.17263205728576287 |
| 3 | 1.50833785176723590 |
| 4 | 2.58013558949369127 |
| 5 | 1.31221954912844035 |
| 6 | 3.80234276107712621 |
| 7 | 1.09731513411320105 |
| 8 | 10.8601495286369168 |
| 9 | 1.00054488586213795 |
| 10 | 1835.82399137424159 |

Two numerically computed real fixed points and multipliers are

$$
p_-\approx-0.29590500557521395565,\quad \zeta'(p_-)\approx-0.51273791545496933533;
$$
$$
p_+\approx1.83377265168027139625,\quad \zeta'(p_+)\approx-1.37425243024718990618.
$$

Their local types are attracting and repelling, respectively. These values are
ordinary high-precision numerical calculations, not directed root certificates.
The initial response also mentioned later papers counting fixed points; no
specific counting asymptotic from them is used in this research packet.

## Backward zero trees and the singularity tree

Let Z be all zeta zeros, trivial and nontrivial. Wherever the composition is
well-defined,

$$
\zeta^{\circ n}(s)=0
\iff \zeta^{\circ(n-1)}(s)\in Z.
$$

Thus the zeros of iterates are iterated preimages of the original zero set.
The notation zeta^{-j} here means a set of preimages, not a global inverse.
Different inverse branches may have different limits or fail to continue.

Ordinary zeta has its pole at 1. The second iterate has an isolated essential
singularity at 1: near that point the inner zeta maps into a neighborhood of
infinity, where transcendental zeta has an essential singularity. At any regular
point with zeta(s)=1, the second iterate has a pole whose order is the
multiplicity of the inner 1-point. Higher iterates have further prepoles and
may have non-isolated singular behavior. Do not claim that every iterate is a
meromorphic function on all of C or assign every deeper singularity the same
local type. The organizing sets are preimages of 0 and 1, not two identical
trees of ordinary zeros and simple poles.

Even assuming RH, descendants of the original zeros need not stay in the
critical strip. The a-point literature [APS22] records zeta's nonzero value
attainment in Re(s)>1. RH concerns the original nontrivial zeros, not all their
inverse descendants.

## Why the nearly logarithmic spirals were not enough

At a repelling fixed point p with lambda=zeta'(p), |lambda|>1, a local inverse
branch g has multiplier lambda^{-1}. Koenigs linearization [KOENIGS] gives a
coordinate h in which h(g(z))=lambda^{-1}h(z). Once an orbit stays in that local
branch,

$$
z_n=p+c\lambda^{-n}+O(|\lambda|^{-2n}).
$$

Contraction and rotation explain the spiral. The complex constant c still
carries two real degrees of freedom; the phenomenon holds for arbitrary nearby
seeds, not only zeta zeros. Rescaling recovers the information contraction hid.
Brent's proposed RH use of intersecting spiral bands was explicitly experimental;
bands built using known zero locations risk circularity [BR17].

The original log/exponential hierarchy analogy remains a motivation. No link
from that analogy to Li(x), R(x), or RH was established here. The actual next
step was to design a DIFFERENT flow that detects horizontal displacement from
the critical line; that is Chapter 02.
