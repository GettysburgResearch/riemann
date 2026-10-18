# What the proposed joint numerator optimization actually proves

**Status.** Exact exponent comparison for a proposed analytic improvement.
It proves that two tempting uses of the existing moments do not improve
the current comparison. No new zero-free boundary is claimed. This is a
failed-closure diagnosis, not a numerical optimization certificate.

**Sources.** The notation and imported moments are those of
[Xu–Sang, arXiv:2610.15291v2, Sections 2, 4–6 and Appendix B](https://arxiv.org/html/2610.15291v2).
The pointwise polynomial bound is the original September 30 source's
lemma headed “Pointwise dyadic estimates”; it includes the natural
character masks, smooth profiles and the common buffered height budget.
The source's theorem is conditional on its recorded analytic inputs.
No independent proof of those inputs is asserted here.

## 1. The twist-safe joint estimate is already dominated

Fix a physical row class of size at most $U^{R+\varepsilon}$, with
detector parameter $\delta>0$, physical mean prime amplitude $q\ge0$,
available prime length $\mathscr L$, and plain moment parameter

\[
 C=\frac1{6\kappa},\qquad
 z(v)=\min\{\mathscr L,C(1-2v)_+\}.
\]

Suppose its plain detector has length $m$ and satisfies
$|S_m|\ge U^{\delta m/2-\varepsilon}$. The amplified plain fourth
moment gives the available count bound

\[
 R\le P_m:=1-2\delta m-2qz(m).                         \tag{1}
\]

Here and below exponents are understood with the arbitrarily small
positive losses required by the source. One can intersect this bound
with the inverse-witness estimate; (1) still holds.

The physical numerator character need not be the detector's character.
Even for a principal target, the buffered family retains the finite ray
twists needed for the physical prime pool. Cauchy–Schwarz between two
licensed fourth moments gives a joint second moment only with capacity

\[
 z_J=\min\{z(m),z(v)\}.
\]

After dividing by the detector and prime lower bounds and using the row
count, this proposed first moment of a numerator block of length $v$
has exponent

\[
 J=\frac{R+1-\delta m}{2}-q\min\{z(m),z(v)\}.          \tag{2}
\]

By contrast, the numerator's own fourth moment, followed by Hölder, gives

\[
 K=\frac{3R+1}{4}-\frac q2z(v).                       \tag{3}
\]

The comparison is exact:

\[
 \boxed{J-K=\frac{P_m-R}{4}
                    +\frac q2|z(m)-z(v)|\ge0.}        \tag{4}
\]

Both expressions acquire the same additional coefficient exponent
$-\vartheta v$ in the numerator approximate functional equation, so
(4) is unchanged after that coefficient, reflection, and the outside
Mellin scales are restored. Thus the twist-safe joint proposal never
improves the estimate already available from (3) and the same count.

If the characters happen to agree, the direct mixed plain moment has
capacity $\min\{\mathscr L,C(1-m-v)_+\}$. When neither individual
capacity is cut by the physical supply, and $0\le m,v\le1/2$, that
capacity is $(z(m)+z(v))/2$; the difference is then simply
$(P_m-R)/4\ge0$. Physical supply cuts can change this comparison for
very short blocks, but character agreement is not globally guaranteed.
It cannot be imposed on all detector bins by selecting a principal
target.

## 2. Intermediate numerator contours reduce to the two known endpoints

We now allow the pointwise numerator bound as well. The buffered
polynomial lemma gives

\[
 |S_v|^2\ll U^{\delta\min(v,1-v)+\varepsilon}.
\]

For $0\le v\le1/2$, the first-moment exponent obtained from the
pointwise estimate and (3) is therefore

\[
 V_R(v)=\min\left\{R+\frac{\delta v}{2},
                 \frac{3R+1}{4}-\frac q2z(v)\right\}. \tag{5}
\]

The two AFE profiles, conductor parameters, original zero masks and fixed
excluded Euler factors are retained exactly as in Xu–Sang Appendix B.
The pointwise lemma applies uniformly to those profiles with the same
single cumulative added-height allowance. For $v\ge1/2$, the reflected
pointwise bound and the unmarked fourth moment are both nonincreasing
after a coefficient $U^{-\vartheta v}$, $\vartheta\ge0$. Thus the
maximization of these block bounds occurs in $0\le v\le1/2$.

Assume the actual comparison range

\[
 \frac{13}{18}\le\kappa\le1,\qquad
 0\le q\le\delta/2,\qquad
 1-\delta\le R\le1-2\delta/3,\qquad
 \mathscr L\ge\frac{21}{100}.                         \tag{6}
\]

Write

\[
 s_0=qC,\qquad K_R=\frac{3R+1}{4},\qquad
 v_c=\frac{1-R-2s_0}{2\delta-4s_0}.                   \tag{7}
\]

Then the supply cut in (5) never controls the crossing: throughout the
relevant block range,

\[
 V_R(v)=
 \begin{cases}
 R+\delta v/2,&0\le v\le v_c,\\
 K_R-s_0/2+s_0v,&v_c\le v\le1/2.
 \end{cases}                                         \tag{8}
\]

Here is a verification of the supply issue. If $\mathscr L<C$, its
transition is $v_0=1/2-3\kappa\mathscr L$. At that point the fourth
moment minus the pointwise exponent is

\[
 \frac{1-R}{4}-\frac{q\mathscr L}{2}
                         -\frac{\delta v_0}{2}
 \ge \frac\delta4
                \left[-\frac13+(6\kappa-1)\mathscr L\right]>0,
\]

by (6). It is larger for $0\le v<v_0$. Above $v_0$, the two affine
functions have their unique intersection at (7), since
$0\le s_0<\delta/2$. At $v=1/2$, their difference is
$(1-R-\delta)/4\le0$. If $\mathscr L\ge C$, there is no supply
cut, and the same calculation applies directly. These statements also
cover $q=0$.

At numerator line $1/2+\vartheta$, define the exponent furnished by
these AFE block bounds to be

\[
 M_R(\vartheta)=\max_{0\le v\le1/2}
                         \{V_R(v)-\vartheta v\}.
\]

Equation (8) gives, without numerical minimization,

\[
 M_R(\vartheta)=
 \begin{cases}
 K_R-\vartheta/2,&0\le\vartheta\le s_0,\\
 R+(\delta/2-\vartheta)v_c,&s_0\le\vartheta\le\delta/2,\\
 R,&\vartheta\ge\delta/2.
 \end{cases}                                         \tag{9}
\]

At the critical row scale $U=Z^h$, reflection contributes
$U^{\vartheta}$, and the outside numerator scale contributes
$Y^{-\vartheta}=Z^{-l_y\vartheta}$. The entire contour-dependent
exponent is consequently

\[
                  hM_R(\vartheta)+(h-l_y)\vartheta.   \tag{10}
\]

In the source geometry $h=l_y+2\ell$ and $h/2<l_y<h$. Its slope
on the first interval in (9) is $h/2-l_y<0$, its slope on the middle
interval is the constant $h-l_y-hv_c$, and its slope on the last is
$h-l_y>0$. Therefore its minimum is attained at

\[
                  \boxed{\vartheta=s_0
                         \quad\hbox{or}\quad\vartheta=\delta/2.} \tag{11}
\]

The first is the Xu–Sang contour; the second is the old pointwise
contour. Even granting the whole displacement interval to the proposed
interpolation does not improve their minimum. This is an optimization
of the stated bounds, not an assertion that every intermediate contour
automatically satisfies all local Euler-factor conditions. Relaxing those
conditions only enlarges the proposed optimization domain; (11) already
rules out an improvement in that enlarged domain.

For clarity, putting

\[
 C_0=-\frac14+\frac b6+\frac{5\ell}{4}
\]

and restoring all the remaining endpoint factors gives exactly

\[
 E_{\mathrm{old}}=C_0+(1/2+\ell)\delta+\ell q-h(1-R),
\]

\[
 E_{\mathrm{Xu}}=C_0+\delta/2+\ell q
          -\frac{3h}{4}(1-R)+(h/2-l_y)\frac{q}{6\kappa}.
\]

Thus the complete upper envelope available from this attempt is
$\min(E_{\mathrm{old}},E_{\mathrm{Xu}})$, with every reflection
and outside-scale cost included.

## 3. Why retuning the detector does not rescue this attempt

Once (4) has removed the proposed twist-safe joint improvement, all these
numerator bounds depend on a detector subdivision only through its count
exponent $R$. The pointwise and fourth-moment bounds are nondecreasing
in $R$; taking their minimum, the maximum over block lengths, and the
minimum over contours preserves that monotonicity. Therefore optimizing
the detector parameter for this numerator bound gives the same minimax
count optimization as Section 4 of Xu–Sang. It cannot improve merely by
balancing the numerator after, instead of before, the count.

There is a more precise explanation at the short balancing subdivision.
There $R=P_m$, its plain capacity is not supply-limited, and (1) becomes

\[
 1-R-2s_0=2(\delta-2s_0)m.
\]

Comparison with (7) proves

\[
                              v_c=m.                 \tag{12}
\]

The numerator block controlling the interpolated estimate has exactly
the length of the plain polynomial already forced to be large by the
detector. A joint plain/plain fourth moment at that length repeats the
same binding information. On such a subdivision even aligned characters
give equality in the comparison at that block.

The original saturated-witness argument already uses
$\sum_{d\mid n}\mu(d)=0$ for $n>1$ to build the capped inverse
detector before it extracts an individual product. Obtaining a further
saving would require a stronger estimate that retains additional signed
information from that convolution or a genuinely stronger mixed
inverse/plain moment. The proposed combination of existing marginal
moments and intermediate contours does not provide it.
