# Growing-prime raw-frame no-go

Status: complete analytic proof; no numerical search and no RH conclusion.

The target was frozen before the proof at `1434cd8d2`.

Authoring parent: `df712b8a8`.  The literal observation and unchanged
physical measure are those of `NATIVE_PHYSICAL_COERCIVITY_PASS4.md`.

## Frozen target

For a finite prime set `S`, put

\[
 A(z)=\sqrt{1-z^2},\qquad C(z)=\sqrt{1-z},\qquad
 x_q(t)=q^{-1/2+it},\quad y_q(t)=\overline{x_q(t)}.
\]

Let `O_S` be the complete A/C-coordinate observation map into the original
`L2(nu)` physical space.  If `P` is a distinguished prime in `S`, freeze the
two-entry coefficient matrix `M_{S,P}` which has one fixed all-A column,
all-A rows at every prime except P, and row coefficients `+1,-1` on the
local C/A choices at P.  Thus `||M_{S,P}||_F^2=2` and its literal field is

\[
 (C(x_P)-A(x_P))A(y_P)
 \prod_{q\in S\setminus\{P\}}A(x_q)A(y_q).          \tag{NG1}
\]

Prove the explicit upper bound

\[
 \frac{\|O_SM_{S,P}\|_{L^2(\nu)}^2}{\|M_{S,P}\|_F^2}
 \le {2\nu(\mathbb R)\over P}
       \prod_{q\in S\setminus\{P\}}(1+q^{-1})^2.   \tag{NG2}
\]

Consequences to prove:

1. singleton panels already rule out a lower frame constant uniform over
   all finite prime sets in the raw A/C coefficient norm;
2. for the nested panel of every prime `q<=P`, the classical Mertens product
   estimate makes the right side `O((log P)^2/P)`, so its smallest singular
   value is `O((log P)/sqrt(P))`;
3. any coordinate normalization which makes this direction order one must
   charge the inverse source map by at least the reciprocal scale.  This is
   a conditioning statement, not a claim that normalized frames cannot
   exist.

The proof must use the exact branch identity

\[
 A(z)=C(z)\sqrt{1+z},\qquad
 C(z)-A(z)=-{C(z)z\over1+\sqrt{1+z}},               \tag{NG3}
\]

with all square roots on their value-one unit-disk branches.  It must retain
the unchanged physical measure and all arithmetic aliases; no point-mass
replacement, coefficient truncation, or path-attainability assertion is
allowed.

## Stop conditions

- If the constant in NG2 is wrong, replace it by the sharp bound proved
  directly from NG1--NG3 and preserve this preregistered target as failed.
- Do not infer a no-go in an adaptively weighted source norm.
- Do not infer failure of fixed-prime coercivity.
- Do not call an arbitrary tensor direction path-attainable.

## Proof

Put `z=x_P(t)`.  Since `|z|=P^{-1/2}<1`, the value-one branches obey

\[
 A(z)^2=C(z)^2(1+z),\qquad A(z)=C(z)\sqrt{1+z}.
\]

The square root in the last display has positive real part.  Consequently
`|1+sqrt(1+z)|>=1`, and rationalizing gives the preregistered identity and
bound

\[
 |C(z)-A(z)|
 ={|C(z)z|\over|1+\sqrt{1+z}|}
 \le \sqrt{1+P^{-1/2}}P^{-1/2}<\sqrt{2/P}.           \tag{NG4}
\]

Also

\[
 |A(y_P)|^2=|1-y_P^2|\le1+P^{-1}<2.                \tag{NG5}
\]

For every other prime q, conjugacy of `x_q,y_q` yields

\[
 |A(x_q)A(y_q)|^2
 =|1-x_q^2|^2\le(1+q^{-1})^2.                      \tag{NG6}
\]

Squaring NG1 and applying NG4--NG6 therefore gives, pointwise for every
real t,

\[
 |(O_SM_{S,P})(t)|^2
 \le {4\over P}\prod_{q\in S\setminus\{P\}}(1+q^{-1})^2.
\]

The physical measure is positive and finite.  Integrating it, then dividing
by `||M_{S,P}||_F^2=2`, proves NG2 without changing that measure or expanding
away any equal-ratio aliases.

For `S={P}`, NG2 tends to zero.  Hence no positive lower frame constant can
hold simultaneously for all finite prime sets in the raw A/C norm.  If S
contains every prime at most P, the classical Mertens product estimate

\[
 \prod_{q\le P}(1-q^{-1})^{-1}=O(\log P)
\]

and `1+q^{-1}<=(1-q^{-1})^{-1}` give

\[
 \sigma_{\min}(O_S)
 \le {\|O_SM_{S,P}\|\over\|M_{S,P}\|_F}
 =O\!\left({\log P\over\sqrt P}\right).            \tag{NG7}
\]

This is the promised nested-panel result.  It is an upper bound on the
best possible raw lower-frame constant, not a lower bound on a source
energy.

Finally let `R_S` be any invertible change from raw coefficients to a new
coordinate norm, and suppose the reparameterized observation has lower
bound c:

\[
 \|O_SR_S^{-1}n\|\ge c\|n\|.
\]

Taking `n=R_SM_{S,P}` gives

\[
 \|R_SM_{S,P}\|\le c^{-1}\|O_SM_{S,P}\|,
\quad
 \|R_S^{-1}\|\ge
 {c\|M_{S,P}\|\over\|O_SM_{S,P}\|}.               \tag{NG8}
\]

Thus a coordinate system with a uniform positive observation bound must
pay an inverse source-map norm of order at least `sqrt(P)/log(P)` on the
nested panels (and `sqrt(P)` on singleton panels), up to the fixed physical
mass constants.  NG8 does not prohibit such a weighted source topology;
it shows that the renormalization cannot be treated as a free algebraic
change of coordinates.

## Trust boundary

The only imported asymptotic input is the classical Mertens product bound,
used solely for NG7.  NG2 and the singleton no-go are elementary and exact.
No arbitrary tensor matrix is asserted to arise from a monotone native path;
the theorem concerns the ambient raw observation frame in which earlier
coercivity and reconstruction statements are formulated.  Fixed-prime
coercivity, including the certified `(2,3,5)` result, is unaffected.
