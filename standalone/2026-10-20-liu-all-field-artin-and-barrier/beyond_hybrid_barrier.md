# Classwise hybrid numerator bounds cannot cross Liu's boundary

**Status:** Proposed exact scalar theorem, with a standard-library rational checker.
**Scope:** Balanced lengths, the fixed counting estimates in Liu's paper, and a classwise choice of pointwise or averaged numerator bounds. The companion `beyond_free_length_barrier.md` extends the conclusion to free total length and either sign of the asymmetry. The theorem concerns this estimate system; it does not assert that formal worst classes occur among actual characters.
**Source:** Baiying Liu, [arXiv:2610.26835v1](https://arxiv.org/html/2610.26835v1), equations (2.3), (14.3), (14.7), (14.8), Lemma 14.9, Theorem 14.12, and Remark 14.13. The last remark explicitly leaves the classwise hybrid system outside its optimality theorem.
**Prior repo work:** [PR #1005, frozen commit d3b3d19573b8dc47ac6e37abd108d54982e9e5f1](https://github.com/GettysburgResearch/riemann/pull/1005), `JOINT_NUMERATOR_CLOSURE.md`, already proves that the licensed intermediate-contour envelope reduces to the minimum of the two endpoints. The new result here is the global barrier for that minimum over all balanced length choices.
**Smallest analytic gap remaining:** A genuinely stronger estimate, or a justified geometry outside this system. This result supplies neither a new zero-free half-plane nor an estimate for an actual signed character sum.

## 1. The theorem

Let \(\kappa_0\) be the unique root in

\[
\frac{749773294079928}{10^{15}}<\kappa_0<
\frac{749773294079929}{10^{15}}
\]

of

\[
Q(\kappa)=16686\kappa^4-27405\kappa^3+9936\kappa^2+1290\kappa-275.
\]

Set

\[
B_0=\frac{1+\kappa_0}{2},\qquad
\ell_0=\frac53-2\kappa_0=4\left(\frac{11}{12}-B_0\right).
\]

Thus \(B_0\) is Liu's \(B_{\flat}\), approximately 0.874886647039964, and
\(\ell_0\) is approximately 0.16712007850681.

For balanced lengths, write

\[
h=\frac{1+b+3\ell}{2},\qquad
l_y=\frac{1+b-\ell}{2},\qquad
C_0=-\frac14+\frac b6+\frac{5\ell}{4},\qquad
B(\ell)=\frac{11}{12}-\frac\ell4.
\]

For \(c=1/(3\kappa)\), put

\[
D=3-(1+2c)x,\qquad P=(2-2cx)(1-x),\qquad
J=(5/6-\delta)D+\delta P,
\]

\[
R=1-\delta+\frac{(5/6-\delta)\delta P}{2J}.
\]

The pointwise and averaged endpoint exponents are

\[
E_{\rm pt}=C_0+(1/2+\ell)\delta+\ell\delta x-h(1-R),
\]

\[
E_{\rm av}=C_0+\delta/2+
\delta x\{\ell+c(h/4-l_y/2)\}-\frac{3h}{4}(1-R).
\]

**Theorem.** Suppose \(b>0\), \(0<\ell\le1/5\), and
\(\kappa_0\le\kappa\le1\). If \(B(\ell)<B_0\), then there is a
formal class with \(x=1/2\) and

\[
\frac18\le\delta\le2B(\ell)-1
\]

at which **both** \(E_{\rm pt}>0\) and \(E_{\rm av}>0\).
If \(B(\ell)=B_0\) and \(\kappa>\kappa_0\), the same conclusion holds.

Consequently, a uniform estimate that is allowed to select the better numerator
bound independently for each class still cannot prove a boundary below \(B_0\).
Starting from a strictly larger justifying bound, no finite chain of such steps
attains \(B_0\). This extends the stated scalar optimality in Liu's Theorem
14.12 to the classwise hybrid system excluded in his Remark 14.13.

## 2. Monotonicity reduces the proof to one algebraic point

Both exponents strictly increase with \(\ell\) in the stated domain.
Indeed, using \(1-R\le\delta\),

\[
\partial_\ell E_{\rm pt}
=\frac54+\delta(1+x)-\frac32(1-R)
\ge\frac54-\frac\delta2\ge\frac56,
\]

while

\[
\partial_\ell E_{\rm av}
=\frac54+\delta x\left(1+\frac{5c}{8}\right)
-\frac98(1-R)\ge\frac18.
\]

They are also nondecreasing in \(\kappa\), and strictly increasing at all the
witnesses below. To see this without differentiating the large rational formula,
let \(r=P/D\) and \(A=5/6-\delta\). Then

\[
R=1-\delta+\frac{A\delta r}{2(A+\delta r)},
\qquad
\frac{\partial r}{\partial c}
=-\frac{2x(1-x)^2}{D^2}<0\quad(0<x\le1/2).
\]

Since \(c\) decreases as \(\kappa\) increases, \(R\) increases. This worsens
both exponents. The additional \(c\)-coefficient in \(E_{\rm av}\) is

\[
\delta x(h/4-l_y/2)=\frac{\delta x}{8}(5\ell-1-b)<0,
\]

so decreasing \(c\) worsens it as well. The witnesses have
\(0<\delta<5/6\) and \(x=1/2\), making this increase strict.

It therefore suffices to prove that for every \(b>0\), some class has both
exponents nonnegative at \((\ell,\kappa)=(\ell_0,\kappa_0)\). A strict
increase in either parameter makes both exponents positive at that same class.

## 3. Four classes cover every positive length asymmetry

Let \(\delta_0=\delta_c(\kappa_0)\), in Liu's notation. In particular,

\[
\delta_0=0.469344858698\ldots,
\qquad E_{\rm av}(\delta_0,1/2)=0
\quad\text{for every }b.
\]

The critical-class identity is also checked directly from the original
endpoint expression in the exact algebraic quotient ring, as explained below.
The full tangent-family inequality and its 4000-box computation are not needed.
At \(x=1/2\), the slopes in \(b\) are

\[
\partial_bE_{\rm av}=\frac16-\frac{c\delta}{16}
-\frac38(1-R),\qquad
\partial_bE_{\rm pt}=\frac16-\frac12(1-R).
\]

Every number and inequality in the following table is checked by enclosing
rational interval arithmetic at the algebraic point. The lower bounds are
deliberately rounded **down** to rational numbers with positive margins.

| Range of \(b\) | Class \(\delta\), with \(x=1/2\) | Averaged exponent | Pointwise exponent |
|---|---:|---:|---:|
| \(0<b\le969/10000\) | \(\delta_0\) | exactly 0 | \(>19/10^8\) |
| \(969/10000\le b\le273/2500\) | \(9/20\) | \(>97/10^7\) | \(>96/10^8\) |
| \(273/2500\le b\le13/100\) | \(21/50\) | \(>16/10^7\) | \(>8/10^5\) |
| \(b\ge13/100\) | \(3/8\) | \(>65/10^6\) | \(>38/10^5\) |

For the first row, the pointwise slope is negative, so its value at
\(b=969/10000\) is a lower bound for the entire interval. In the second and
third rows the averaged slope is positive and the pointwise slope is negative;
only their left and right endpoints, respectively, need evaluation. In the last
row both slopes are positive, so evaluation at \(b=13/100\) covers the whole
unbounded ray. These are exact affine statements, not a grid over \(b\).

All four witnesses lie below \(12/25\). Since \(\ell\le1/5\) gives
\(2B(\ell)-1\ge11/15>12/25\), every witness is inside the class range a
purported step must control. Together with Section 2, this proves the theorem.

## 4. An independent algebraic certificate for the critical class

The checker does not need a floating approximation to \(\delta_0\). Define

\[
U(k)=2200-26220k-49500k^2+1086480k^3-1263600k^4,
\]

\[
V(k)=2220-25272k-30672k^2+917568k^3-1026432k^4.
\]

Then \(\delta_0=U(\kappa_0)/V(\kappa_0)\). The checker verifies that the
numerators of both

\[
\operatorname{cr}(U/V,k),\qquad
(5/3-2k)D_*(U/V,k)-N_*(U/V,k)
\]

are divisible by \(Q(k)\) over the rationals. Here \(\operatorname{cr}\),
\(N_*\), and \(D_*\) are the displayed critical quadratic and numerator and
denominator of \(\ell_*(\delta,k)\) in Lemma 14.9. It also checks that
\(V\) and \(D_*\) do not vanish in the isolating box. These identities
recover \(\operatorname{cr}(\delta_0,\kappa_0)=0\) and
\(\ell_*(\delta_0,\kappa_0)=\ell_0\) exactly.

Separately, the checker substitutes \(k\), \(U(k)/V(k)\), and
\(\ell=5/3-2k\) into the original rational formula for \(E_{\rm av}\).
It computes in the exact quotient ring \(\mathbb Q[k]/(Q(k))\), checking
that each inverted polynomial is coprime to \(Q\). The resulting numerator
is the zero polynomial at both \(b=0\) and \(b=1\). Since the displayed
endpoint is affine in \(b\), this proves its vanishing for every \(b\)
without assuming the algebraic conclusion of Lemma 14.9.

The quartic's endpoint signs and a derivative enclosure prove that its isolating
interval contains exactly one real root. No branch choice or numerical root
finder enters acceptance. The final receipts display decimals only for human
readability; all decisions use `fractions.Fraction`.

Run:

```sh
python -I -S -B beyond_hybrid_barrier.py
python -I -S -B -O beyond_hybrid_barrier.py
python -I -S -B -O run_barrier_mutations.py
```

This certifies the finite polynomial identities and sign cover. It is not a
replay of the analytic moment theorems in Liu's 136-page preprint.
The last command replays exactly three negative controls: a changed quartic,
a broken witness-interval overlap, and a reversed unequal-length coefficient.
Its receipt binds the checked source by SHA-256; the source itself is unchanged.

## 5. Implications for further work

The previously available intermediate-contour analysis in PR #1005 takes the
pointwise polynomial bound, the amplified fourth moment, all allowable block
lengths, and the physical prime-supply condition into account. It proves that
the optimized endpoint is exactly

\[
\min(E_{\rm pt},E_{\rm av}).
\]

Under its stated hypotheses, the theorem above therefore also rules out a gain
from choosing an arbitrary intermediate reflected-numerator contour separately
for each class. Merely checking that the two methods have different worst
classes does not create a gain: the four-class cover exhibits the shared
obstruction for every balanced value of \(b\).

The finite-chain assertion follows because a bound \(B_{\rm prev}\ge B_0\)
justifies only \(\kappa\ge2B_{\rm prev}-1\ge\kappa_0\) in this system;
the \(\kappa=1\) case is covered as well. A strictly larger previous bound
forces strictness at \(\kappa>\kappa_0\), preventing endpoint attainment.
Whole steps of Liu's earlier pointwise system cannot help, by the separate
pointwise optimality already established there. The exact boundary itself is
obtained by Liu's limiting contradiction argument, not by a finite chain from
above.

A stronger actual mixed moment, a smaller critical-class count, increased
prime amplification, or a new direct bound could change this conclusion.
Unequal total lengths are outside the balanced theorem above; the companion
`beyond_free_length_barrier.md` treats them using the full direct majorant and
four explicit numerator endpoints. Other analytic possibilities must be
analyzed with their full source hypotheses; these scalar obstructions do not
assert impossibility for the underlying number theory.
