# Free lengths and a class-by-class numerator choice at the current cap

**Status.** A proved scalar obstruction for the explicitly defined estimate
system below. This is not an obstruction to an arithmetic improvement, and
is not a statement about the actual existence of any adverse zero class.
It fills a parameter gap in this packet: unequal total lengths, both sides
of the numerator contour, and a class-by-class choice of pointwise or
averaged numerator are allowed simultaneously. At the fixed input
`kappa = 2 B_flat - 1`, they still cannot produce `B < B_flat`.

The numerical search that suggested the certificate is not the proof.
`check_mixed_numerator.py` verifies the root isolations, three exact
polynomial identities, and six rational duals with their rounding residuals
using only Python's standard-library rational arithmetic. Its generated
`MIXED_NUMERATOR_CHECKS.json` records the certificate. The smallest strict
dual margin exceeds `0.00000179087019` above `B_flat`; the remaining branch
has an exact identity giving `B_flat` itself.

## 1. Sources and precise scope

The imported scalar inputs are Baiying Liu,
[arXiv:2610.26835v1](https://arxiv.org/html/2610.26835v1), equations
(13.16), (14.14)-(14.16), and Sections 14.8 and 15.1-15.3. In particular,
Remark 14.13 explicitly does not cover a class-by-class mixture of the two
numerator estimates or unequal lengths. The proof here uses those stated
upper bounds as inputs; it does not independently validate the analytic
preprint. The ordinary product moment behind the averaged numerator is
also an input to the earlier repository packets, not a new theorem here.

Set

\[
 B_\flat=0.874886647039964\ldots,\qquad
 \kappa_\flat=2B_\flat-1=0.749773294079928\ldots.
 \tag{1}
\]

The exact definition is the indicated root of

\[
 16686\kappa^4-27405\kappa^3+9936\kappa^2+1290\kappa-275=0.
 \tag{2}
\]

This is Liu's quartic in `B` after `B=(1+kappa)/2`. No decimal is used as
an exact mathematical input to the certificate.

We permit a common choice of real lengths

\[
 M=l_x+l_y,\quad b=l_y-l_x,\quad
 h=1-l_x+\ell,\qquad M,l_y,\ell\ge0.
 \tag{3}
\]

In particular, `b` need not be positive, `M` need not equal `1-ell`, and
we do not impose `ell <= 1/5` or `l_x >= ell`. The direct majorant is

\[
\begin{split}
 B_{\rm low}&=\frac56+\frac{l_x}6-\frac\ell6+G+\frac{k}2,\\
 G&=\max(0,b/12,b-l_y/2),\\
 k&=\max\left(0,\frac{1+3\ell-2M}{4},M+\ell-1,
                                      \frac{3\ell-1}{2}\right).
\end{split} \tag{4}
\]

For the high part we keep the source's optimized separate count. Write
`alpha=5/6`, `0<delta<alpha`, `0<=x<=1/2`, and

\[
\begin{split}
 g&=\delta x,& c&=\frac2{3\kappa},\\
 D&=3-(1+c)x,& P&=(2-cx)(1-x),\\
 J&=(\alpha-\delta)D+\delta P,&
 R&=1-\delta+\frac{(\alpha-\delta)\delta P}{2J}.
\end{split} \tag{5}
\]

All these are exponents in supplied **upper** bounds. The theorem concerns
uniform control of the formal classes, as in the source comparison. A proof
that a critical class is absent would be a new analytic input outside it.

For each class, independently, grant the better of the pointwise numerator
and the amplified first-moment numerator. Also grant unlimited supply of
the original prime windows and ignore positive contour margins. Those
relaxations can only help a hypothetical improvement. The theorem proves
that even this relaxed system cannot improve (1) at `kappa=kappa_flat`.

This theorem is **not** a claim of optimality for all conceivable numerator
arguments, joint inverse/numerator moments, signed returns, a fresh
supremum contradiction with another moment parameter, or different direct
Gram estimates.

## 2. The complete numerator envelope in this model

Put

\[
 a=(1+\delta)/2,\qquad
 Q=(3R+1)/4,\qquad u=\frac{g}{6\kappa},\qquad p=\delta/2.
 \tag{6}
\]

For an approximate-functional-equation block of length `U^m`, with
`0<=m<=1/2`, the two supplied first-moment exponents are

\[
 R+pm,\qquad Q-u/2+um.
 \tag{7}
\]

The first is the cardinality bound times the zero-free pointwise block
bound. The second follows from the product moment for two copies of the
plain block, prime length `(1-2m)/(6 kappa)`, and Holder's inequality.
The centrally normalized character polynomials, fixed character labels,
and natural zeros are unchanged. We are not asserting that this bound is
valid with arbitrary row-selected coefficients or a different amplifier.

Let

\[
 A(m)=\min(R+pm,Q-u/2+um),\qquad
 \nu(\theta)=\max_{0\le m\le1/2}(A(m)-\theta m).
 \tag{8}
\]

For the four classes used below, `p>u`, the two affine functions cross
inside `[0,1/2]`, and hence `A` has slope `p` then `u`. Thus
`nu` is affine on each of `[0,u]`, `[u,p]`, and `[p,infinity)`.
Taking the better bound block by block and optimizing any intermediate
contour therefore yields the same two endpoint values at `theta=u,p`.
This is a finite concave-envelope calculation, not an assumption that
one must use the same numerator estimate on every block.

Define the outside exponent

\[
 C=a-\frac h6-\frac{l_y}2-\frac\ell2+g\ell.
 \tag{9}
\]

If `0<=l_y<=h`, optimizing both contour sides gives the following
optimistic high majorant:

\[
\boxed{\quad
 H(\delta,x)=C+
 \min\left\{
 hR+\frac\delta2\min(l_y,h-l_y),\quad
 hQ-\frac u2|h-2l_y|
 \right\}.
 \quad} \tag{10}
\]

For example, at `w=1/2-theta` the functional equation contributes
`h theta`, the original length contributes `-l_y theta`, and the
numerator average contributes `h nu(theta)`. Their sum is
`h nu(theta)+theta(h-l_y)`. On the other side it is
`h nu(theta)+theta l_y`. The smaller distance is at most `h/2`, so the
piecewise-affine minimization is at `theta=u` or `theta=p` and gives
(10). The dual approximate-functional-equation block is no larger than
the corresponding direct block for nonnegative `theta`.

For later notation, on the side `l_y>=h/2` define

\[
 H_P^+=C+hR+p(h-l_y),\qquad
 H_A^+=C+hQ+u(h/2-l_y).
 \tag{11}
\]

On `l_y<=h/2`, define

\[
 H_P^-=C+hR+pl_y,\qquad
 H_A^-=C+hQ+u(l_y-h/2).
 \tag{12}
\]

The subscripts designate pointwise and averaged; the superscripts
designate the sign of `l_y-h/2`. A successful step must satisfy
`B>=min(H_P,H_A)` for each required class, in addition to (4).

The source's averaged theorem is stated on a smaller contour range than
every endpoint allowed here. Granting the optimistic envelope on the
larger range only strengthens the hypothetical competitor. The proof is
a lower bound for this supplied scalar system, not an analytic
continuation theorem on newly enlarged contour boxes.

## 3. Low constraints bound every relevant parameter

Equation (4) implies

\[
\begin{split}
 B&\ge L_0=\frac56+\frac M{12}-\frac\ell6,\\
 B&\ge L_K=\frac13+\frac{7M}{12}+\frac\ell3,\\
 B&\ge L_J=\frac{23}{24}-\frac M6+\frac{5\ell}{24},\\
 B&\ge L_0-b/12,\qquad B\ge L_K-b/12.
\end{split} \tag{13}
\]

The first three use `G>=b/12`; the last two use `G>=0`.
The identity

\[
 \frac{17}{30}L_0+\frac1{30}L_K+\frac25L_J=\frac{13}{15}
 \tag{14}
\]

forces `B>=13/15`. Thus all four zero classes below belong to the
required interval `1/8<=delta<=2B-1`, even if one seeks a much smaller
`B` than (1).

In considering an improvement, assume `B<B_flat<7/8`. Then `L_K<=B`
gives

\[
 14M+8\ell<13,\qquad M<1,\quad \ell<2,
 \quad h-l_y=1-M+\ell>1/14.
 \tag{15}
\]

Since `l_y>=0`, we have `b>=-M>-1`. The branch
`G>=b-l_y/2`, with `k>=0`, also gives

\[
 B\ge\frac56-\frac M6+\frac{2b}3-\frac\ell6,
\]

so `b<1/16+(M+ell)/4<13/16<1`. Consequently

\[
 0\le M\le1,\quad |b|\le1,\quad0\le\ell\le2,
 \qquad 0\le l_y<h.
 \tag{16}
\]

The safe closed box (16) is used to account rigorously for every rounding
residual in the rational duals. No hidden assumption `l_x>=0` is used.

## 4. The critical averaged class gives an exact dual

Fix `kappa=kappa_flat`, and define

\[
 \delta_c=\frac{3\kappa(9\kappa-5)}{5+18\kappa-18\kappa^2}
           =0.469344858698143\ldots,
 \qquad x_c=1/2.
 \tag{17}
\]

At this class, write `g=delta_c/2`, `u=delta_c/(12 kappa)`.
The identities (2), (5), and (17) give

\[
 9R_c-5-\frac{g}{\kappa}=0,
 \qquad R_c=0.590332353526355\ldots,
 \qquad Q_c=\frac23+\frac u2.
 \tag{18}
\]

For example, substituting `delta=N/D`, with
`N=27 kappa^2-15 kappa`, `D=5+18 kappa-18 kappa^2`, into the critical
quadratic gives the exact polynomial identity

\[
\begin{split}
 &(3-324\kappa^2)N^2
 +(756\kappa^2-54\kappa-5)ND
 +(40\kappa-300\kappa^2)D^2\\
 &\hspace{15mm}=-\kappa(5+42\kappa)
 (16686\kappa^4-27405\kappa^3+9936\kappa^2+1290\kappa-275).
\end{split} \tag{19}
\]

Suppose first that `l_y>=h/2` and the averaged estimate is chosen at
this class. By (18), its high constraint reduces to

\[
 B\ge H_{A,c}^+
     =1+g+u-(1/2+u)M+(g+u)\ell.
 \tag{20}
\]

Set `D_*=3+4g+8u` and take the positive weights

\[
 w_0=\frac{4+14g+22u}{3D_*},\qquad
 w_K=\frac{2(1-g+u)}{3D_*},\qquad
 w_H=\frac1{D_*}.
 \tag{21}
\]

They sum to one and exactly cancel the coefficients of `M,ell` in
`w_0 L_0+w_K L_K+w_H H_{A,c}^+`. Hence

\[
 B\ge\frac{7+14g+22u}{3(3+4g+8u)}=B_\flat.
 \tag{22}
\]

The final equality follows directly from (17) and
`B_flat=(1+kappa)/2`; the checker verifies the corresponding polynomial
identity without division by a numerically approximate root.

This single dual already excludes every unbalanced choice in this branch.

## 5. Six strict duals cover every other choice

Define the smaller root

\[
 (216\kappa-18)\xi^2-(468\kappa-57)\xi+150\kappa-20=0,
 \qquad \xi=0.388582767883352\ldots.
 \tag{23}
\]

The three additional classes, all at `x=1/2`, are

\[
 \delta=\xi,\qquad\delta=43/100,\qquad\delta=9/20.
 \tag{24}
\]

Their counts use the same formula (5); in particular `R(xi,1/2)=2/3`.
The strict duals have the following results. Decimal entries below are
rounded for reading; all acceptance inequalities use exact fractions in
the checker and include the full coefficient residual on (16).

| Side and constraints used with the low bounds | Certified lower bound, rounded down |
|---|---:|
| `l_y<=h/2`, pointwise at `delta_c` | 0.88699944436 |
| `l_y<=h/2`, averaged at `delta_c` | 0.88252066719 |
| `l_y>=h/2`, pointwise at `xi` | 0.87495693690 |
| `l_y>=h/2`, averaged at `xi`, pointwise at `43/100` | 0.87489189209 |
| `l_y>=h/2`, averaged at `43/100`, pointwise at `9/20` | 0.87489619098 |
| `l_y>=h/2`, pointwise at `delta_c`, averaged at `9/20` | 0.87488843790 |

Here is the exact case coverage, without assuming any monotonicity of the
row-by-row choice. The two negative-side cases cover either estimate at
`delta_c`. On the positive side, averaged at `delta_c` is already
excluded by (22). If pointwise is used there, either pointwise at `xi`
is excluded by the third row, or averaged must be used at `xi`. Then
pointwise at `43/100` is excluded by the fourth row. With averaged at
`43/100`, pointwise at `9/20` is excluded by the fifth row, and averaged
at `9/20` is excluded by the sixth. These alternatives are exhaustive.

For reproducibility the four positive-side strict duals use `L_0,L_K`
and the listed one or two high constraints, in that order. Their positive
integer weights, divided by their sum, are

```text
xi pointwise:
687392342258, 125043063097, 187564594645

xi averaged; 43/100 pointwise:
675628381548, 125108107905, 76778023559, 122485486988

43/100 averaged; 9/20 pointwise:
664163876107, 125103809010, 138011532368, 72720782515

delta_c pointwise; 9/20 averaged:
655089546038, 125111562089, 36174178547, 183624713326
```

The two negative-side duals use `L_0-b/12,L_K-b/12` and their high
constraint. The pointwise weights are
`461108703518,113000555632,425890740850`; the averaged weights are
`439749746269,117479332804,442770920927`. They also add, respectively,
`28250138908/10^12` and `69774280882/10^12` times the valid inequality

\[
 0\ge 2l_y-h=-1+3M/2+b/2-\ell.
 \tag{25}
\]

To explain why a rounded dual is a proof, write its affine right side as
`c+r_M M+r_b b+r_ell ell`. Since its weights on `B>=...` sum to one,
(16) implies

\[
 B\ge c-|r_M|-|r_b|-2|r_\ell|.
 \tag{26}
\]

The checker encloses every coefficient using rational interval arithmetic
on isolated `kappa,xi` intervals. Every resulting lower endpoint in (26)
strictly exceeds the upper endpoint for `B_flat`. The smallest excess is
greater than `1.79087019*10^-6`; no near-equality is accepted by a numerical
tolerance.

**Theorem.** Under the supplied system (3)-(10), at
`kappa=kappa_flat`, all admissible choices satisfy `B>=B_flat`.

**Proof.** Equations (13)-(16) reduce any proposed improvement to the
closed parameter box and legitimate two contour sides. Equation (22)
handles the positive-side critical averaged choice. The six certified
strict duals and the exhaustive alternatives above handle all remaining
choices. QED.

For the retained classes, `R_kappa` increases with `kappa`. Indeed
`P/D` decreases with `c=2/(3 kappa)`, since

\[
 \partial_c(P/D)=-x(1-x)^2/D^2\le0,
\]

and (5) is increasing in `P/D`. The numerator penalty `u` decreases with
`kappa`, which also makes (10) weaker. Thus taking a larger moment
parameter does not evade this certificate. In particular a finite
sequence of steps using a previously available boundary at least
`B_flat` cannot cross below it through this fixed supplied system.
This does not claim an independent theorem for every possible
supremum-continuation argument using unknown smaller actual family caps.

## 6. Why reusing a plain witness does not sharpen this numerator bound

There is one potentially useful joint estimate that can already be tested
exactly, without asserting an arbitrary-coefficient mixed moment.
Suppose the same detected presentation has a plain witness of length
`U^m`, whose normalized square is at least `U^(delta m)`, with
`0<=m<=1/2`. Pair this witness with a numerator block of length `U^v`,
`0<=v<=1/2`, in the supplied M2 product
moment, and use the remaining prime length `(1-m-v)/(6 kappa)`.
Cauchy-Schwarz gives first-moment exponent

\[
 E_J(v)=\frac{R+1-\delta m}{2}-u(1-m-v).
 \tag{27}
\]

The ordinary four-copy Holder route above gives

\[
 E_4(v)=\frac{3R+1}{4}-\frac u2(1-2v).
 \tag{28}
\]

Their difference is exactly

\[
 E_J(v)-E_4(v)
   =\frac{1-R-2\delta m-2u(1-2m)}4
   =\frac{R_P(m)-R}{4}.
 \tag{29}
\]

The plain witness itself already supplies `R_P(m)`. Whenever the class
count `R` is at least as strong, (29) is nonnegative; at the balancing
split it is exactly zero. Thus this licensed joint use of the same M2
bound does not improve the supplied numerator at the adverse split.
This says nothing against a genuinely stronger joint inverse/plain
estimate, a correlation between the inverse witness and prime amplitudes,
or a signed physical return.

## 7. A quantitative target for a new arithmetic input

At the averaged critical class, the old inverse/ordinary cutoff is

\[
 t_c=1+\frac{\delta_c P}{2J}=1.163953576509010\ldots.
 \tag{30}
\]

The long inverse exponent there is `(1+5 t_c)/6`. A useful new native
input must reach this length, or provide a joint relation that changes
its adverse split. The `r=7/5`, large-prime-amplitude gain in
`SHORT_INVERSE.md` does not do that: its amplitude threshold is `0.37`,
whereas the class in (17) has `g_c=0.234672429349071...`.

For scale, suppose a new, fully licensed long inverse moment saved a
fixed `eta>0` in a neighborhood of this crossing, with all other scalar
inputs unchanged. The decreasing short count and increasing long count
are affine in the cutoff. Their new intersection would move from `t_c`
to

\[
 t_c+\frac{\eta}{(5/6-\delta_c)+\delta_cP/D},
\]

and its count exponent would drop by exactly

\[
 \frac{\delta_cP}{J}\eta=2(t_c-1)\eta
                   =0.32790715301802\ldots\eta.
 \tag{31}
\]

This is a conditional sensitivity calculation, not a sufficient new
zero-free theorem: the gain would have to hold uniformly on a useful
neighborhood, the other classes and margins would have to be rechecked,
and the comparison must still close. It identifies the length and
amplitude where a new estimate can affect the present boundary.
