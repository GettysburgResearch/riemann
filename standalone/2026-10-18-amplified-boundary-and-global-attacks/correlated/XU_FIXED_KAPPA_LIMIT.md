# An exact limit of parameter tuning in the unchanged Xu--Sang endpoint

Status: a necessary condition for the source's endpoint inequality at fixed
\(\kappa\). It is not a limit on the underlying mathematics or on a new
mixed-moment estimate.

Use the endpoint \(E_{b,\ell,\kappa}(\delta,x)\) of equation (28) in
Xu--Sang, arXiv:2610.15291v2. Set

\[
 \kappa=\frac{29991}{40000},\qquad c=\frac1{3\kappa}=\frac{40000}{89973},
\]

and let \(\delta_*\) be the smaller root of

\[
 (9c^2-108)\delta^2+(252-54c-15c^2)\delta+(40c-100)=0.             \tag{1}
\]

For an explicit root selection, write the three coefficients in (1) as
\(a_2,a_1,a_0\), in descending order. They satisfy
\(a_2<0\), \(a_1>0\), \(a_0<0\), and

\[
 \delta_*=\frac{-a_1+\sqrt{a_1^2-4a_2a_0}}{2a_2}.              \tag{1a}
\]

The polynomial is negative at \(23/50\), positive at \(12/25\), and its
derivative is positive at \(12/25\). Since its second derivative is
negative, it is strictly increasing throughout that interval. These
rational comparisons prove that \(\delta_*\in(23/50,12/25)\); the other
root is larger, since a concave quadratic positive at \(12/25\) eventually
becomes negative. They also establish positivity of the radical in (1a).
In particular \(\delta_*\) lies inside the source's required rectangle.
The exact three comparisons, writing \(p\) for the left side of (1), are

\[
 p(23/50)=-\frac{1990692592919}{1686487651875}<0,
 \quad p(12/25)=\frac{743867881388}{562162550625}>0,
 \quad p'(12/25)=\frac{8301279941044}{67459506075}>0.
\]

**Proposition.** If some \(b,\ell\) and \(g>0\) satisfy the unchanged
endpoint condition \(E_{b,\ell,\kappa}(\delta,x)\le-g\) throughout
\(1/8\le\delta\le5/6\), \(0\le x\le1/2\), then

\[
 \ell<\ell_*:=\frac{5-6\delta_*}{9+6(1+c)\delta_*},
 \qquad
 B(\ell)>B_*:=\frac{11}{12}-\frac{\ell_*}{4}.                    \tag{2}
\]

More precisely,

\[
 B(\ell)\ge B_*+
   \frac{g}{4\{3/4+(1+c)\delta_*/2\}}.                          \tag{3}
\]

## Proof

At \(x=1/2\), put \(T=1-R_\kappa(\delta,1/2)\). The count formula
(21) gives

\[
 T=\frac{\delta\{(5/6)(8-3c)+(c-4)\delta\}}
           {4\{(5/6)(5/2-c)-((3-c)/2)\delta\}}.                 \tag{4}
\]

The denominator here is positive for \(0\le\delta\le5/6\): it is
\(4J\), with
\(J=(5/6-\delta)(5/2-c)+\delta(1-c/2)\). Both fixed factors are
positive because \(0<c<1/2\), and the two nonnegative weights cannot
both vanish. All denominator clearings below are therefore valid at
\(\delta_*\).

Using \(h=(1+b+3\ell)/2\) and \(l_y=(1+b-\ell)/2\), the coefficient
of \(b\) in \(E(\delta,1/2)\) is

\[
 \frac16-\frac{c\delta}{16}-\frac{3T}{8}.                       \tag{5}
\]

It vanishes exactly when \(T=4/9-c\delta/6\). Substituting (4) and
clearing its positive denominator gives (1). Thus at \(\delta_*\),
all dependence on \(b\) cancels and direct simplification yields

\[
 E_{b,\ell,\kappa}(\delta_*,1/2)
   =\frac{\delta_*}{2}-\frac5{12}
      +\ell\left\{\frac34+\frac{(1+c)\delta_*}{2}\right\}.
                                                                    \tag{6}
\]

The coefficient of \(\ell\) is positive. Applying the endpoint
requirement at this single point proves (2)--(3).

For orientation, evaluating the exact expressions gives

\[
 \delta_*\approx0.4693449406921990775,
 \quad \ell_*\approx0.1671200682001409903,
 \quad B_*\approx0.8748866496166314191.
\]

These decimal displays are not used in the proof. The proposition follows
from the exact root and algebraic identities above. It explains why the
certified boundary \(0.87488666\) leaves little room for a larger gain by
changing \(b\) or \(\ell\) while retaining the same \(\kappa\) and
endpoint estimate. A stronger arithmetic estimate can change (6), and is
outside this restriction.

Source: <https://arxiv.org/html/2610.15291v2>, equations (21) and (28).
