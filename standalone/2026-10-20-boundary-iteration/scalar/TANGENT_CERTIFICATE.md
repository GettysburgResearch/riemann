# An independent rational certificate for the tangent continuation

20 October 2026. Status: exact scalar verification, not an analytic
zero-free proof. This independently reconstructs the part of Liu's
arXiv:2610.26835v1 Lemmas 14.8--14.10 needed after the bound 7/8.
The source HTML is pinned at SHA256
5b128f3cedb4d6ecfe3a3d57b1290cb576cac03092cf0b807c6f8092abf864c6.
The source estimates which feed these formulas remain assumptions.

Run `python -I -S -B verify_tangent.py`. Python's standard library is
sufficient. Every acceptance calculation uses exact rational numbers;
the 64 intervals are a cover, not sample points. The output is
TANGENT_CHECK.json. An independent source and implementation review is
recorded separately.

## 1. Primitive scalar formulas

Put c=1/(3 kappa), and write

\[
 D=3-(1+2c)x,\quad P=(2-2cx)(1-x),\quad
 J=(5/6-\delta)D+\delta P,
 \quad R=1-\delta+\frac{(5/6-\delta)\delta P}{2J}.
\]

For the rectangle \(1/8\le\delta\le5/6\),
\(0\le x\le1/2\), all D, P, J are positive. The identity
\(2D-3P=2x(2+c-3cx)\ge0\) implies
\(1-\delta\le R\le1-2\delta/3\).
The source endpoint is

\[
 E=C_0+\delta/2+\delta x V-\frac{3h}{4}(1-R),
\quad C_0=-1/4+b/6+5\ell/4,
\quad V=\ell+c(h/4-l_y/2),
\]

where \(h=(1+b+3\ell)/2\) and \(l_y=(1+b-\ell)/2\).

At x=1/2 introduce polynomial numerators

\[
 \begin{split}
 \bar D&=15\kappa-2,& \bar P&=6\kappa-1,\\
 \bar J&=(5/6-\delta)\bar D+\delta\bar P,&
 \bar R&=2(1-\delta)\bar J+(5/6-\delta)\delta\bar P,\\
 Z&=96\kappa\bar J.
 \end{split}
\]

Thus \(\bar J=6\kappa J\), \(R=\bar R/(2\bar J)\), and

\[
 E=(N_0+\ell N_\ell+bN_b)/Z,
\]

with the following literal polynomials, constructed independently in
the checker's two-variable rational polynomial ring:

\[
 \begin{split}
 N_0&=(-1/4+\delta/2)Z-2\delta\bar J
                              -18\kappa(2\bar J-\bar R),\\
 N_\ell&=(5/4+\delta/2)Z+10\delta\bar J
                              -54\kappa(2\bar J-\bar R),\\
 N_b&=16\kappa\bar J-2\delta\bar J
                              -18\kappa(2\bar J-\bar R).
 \end{split}
\tag{1}
\]

Coefficientwise arithmetic verifies

\[
 3N_b+2\operatorname{cr}(\delta,\kappa)=0,
\quad
 \operatorname{cr}=(3-324\kappa^2)\delta^2
 +(756\kappa^2-54\kappa-5)\delta+40\kappa-300\kappa^2.
\tag{2}
\]

For each kappa in the certified interval, exact signs at 23/50 and
12/25, together with a strictly positive delta derivative there,
give a unique root delta_c. Define

\[
 \ell^*=-N_0/N_\ell,\qquad
 b^*=-\frac{N_{0,\delta}N_\ell-N_0N_{\ell,\delta}}
                    {N_\ell N_{b,\delta}},
 \qquad \delta=\delta_c.
\tag{3}
\]

All denominators are proved nonzero by interval division and strict
sign checks. Equations (1)--(3) give exactly E=E_delta=E_b=0 at
(delta_c,1/2); the derivative numerator cancellation is also checked
coefficientwise. This exact algebra, rather than an interval containing
zero, proves the double root used below.

## 2. A certificate over the entire rectangle

Set y=1/2-x. Then

\[
 D=5/2-c+(1+2c)y,\qquad P=1-c/2+2y+2cy^2,
 \qquad U=1/2+(1/2-y)V.
\]

Expanding the primitive formula gives

\[
 -2JE=A(y)\delta^2+B(y)\delta+C(y),
\tag{4}
\]

where

\[
 \begin{split}
 A&=-2(P-D)U+9hP/4-3hD/2,\\
 B&=-2C_0(P-D)-5DU/3+5hD/4-5hP/8,\\
 C&=-5C_0D/3.
 \end{split}
\tag{5}
\]

The exact double root at y=0 makes the constant coefficient of
4AC-B squared equal to zero. The checker does not test an interval
approximation of that zero. Instead, it proves every coefficient of A
and every coefficient of

\[
                     (4AC-B^2)/y
\]

strictly positive on each kappa box. Therefore A>0 and 4AC-B squared
is positive for y>0. The elementary identity

\[
 4A(A\delta^2+B\delta+C)=(2A\delta+B)^2+(4AC-B^2)
\]

proves the quadratic in (4) strictly positive whenever y>0, for all real
delta. Since J>0 on the source rectangle, E<0 there. At y=0,
the right side of (4) is A(0)(delta-delta_c) squared. Thus on the
source rectangle E is nonpositive, with its unique zero at
(delta_c,1/2). There is no mesh in delta or x.

The checker also verifies every strict side condition in Remark 14.1,
including its three small-row inequalities (14.10). The kappa range is

\[
          [7497732940799/10^{13},\ 3/4],
\tag{6}
\]

partitioned into 64 exactly adjacent closed rational intervals. On each
interval, two rational bisections give a delta enclosure with certified
signs at both ends, valid for every kappa in that interval. Ordinary
interval operations then enclose b and ell, the coefficients in (5),
the discriminant coefficients, and the side margins. There are no
floating-point acceptance values and no omitted gaps between boxes.

To make the endpoint strict, decrease ell while holding b and kappa
fixed. On the whole source rectangle,

\[
 E_\ell=5/4+\delta x(1+5c/8)-9(1-R)/8
                  \ge5/4-9\delta/8\ge5/16>1/8.
\tag{7}
\]

Hence lowering ell by tau lowers E by at least tau/8 uniformly.
The other strict inequalities persist by continuity. Equation (7)
is an analytic algebraic bound over the full rectangle, not a claim
inferred from the code's derivative value at the critical point.

## 3. The self-consistent endpoint and its exact bracket

The checker differentiates (3) along the critical root using
delta_c prime = -cr_kappa/cr_delta, with exact interval arithmetic.
It proves

\[
 G'(\kappa)>0,\qquad
 G(\kappa)=(1+\kappa)/2-11/12+\ell^*(\kappa)/4,
\]

throughout (6). A separate, finer exact root enclosure proves opposite
signs of G at

\[
 \kappa_-=749773294079928/10^{15},\quad
 \kappa_+=749773294079929/10^{15}.
\tag{8}
\]

Thus G has exactly one zero in (6), lying strictly between (8).
This sign is what the source continuation needs for
kappa greater than kappa_flat.

For the polynomial identity, the code independently constructs the
four-by-four Sylvester determinant in delta of cr and
N0+(5/3-2 kappa) N_ell. Coefficientwise comparison gives

\[
 -\frac{1600}{3}\kappa^2(6\kappa-1)^2(15\kappa-2)(42\kappa+5)
 (16686\kappa^4-27405\kappa^3+9936\kappa^2+1290\kappa-275).
\tag{9}
\]

The prefactors are nonzero on (6). At the unique zero of G,
ell=5/3-2 kappa, so the resultant vanishes. Exact endpoint signs and
a nonzero derivative also isolate the quartic's root within (8).
This identifies the correct branch, rather than accepting an arbitrary
root of a resultant. Substitution kappa=2B-1 gives the inherited
quartic for B_flat and its exact bracket in TANGENT_CHECK.json.

## 4. Scope and negative controls

The certificate covers the narrow tangent family, all its continuous
delta/x domain, strict side margins, and the required endpoint root.
It does not replay the initial analytic improvement to 7/8, the
canonical recursion, product moments, contour shifts, or the physical
probe. It does not check the larger kappa interval in the full source
Lemma 14.9, which is unnecessary for this closing step.

Two algebraic negative controls reject a changed critical source
coefficient and a reversed tangent sign. These are tests of the
primitive identity checks, not an end-to-end mutation suite for the
whole analytic argument. Reported positive margins are rounded down
to rational multiples of 10 to the minus ninth using integer division;
acceptance uses the original exact interval endpoints. Python's
optimized mode cannot remove any check.
