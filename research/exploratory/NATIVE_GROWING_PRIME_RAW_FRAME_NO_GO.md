# Growing-prime raw-frame no-go

Status: preregistered theorem target; proof to be completed without a
numerical search.  No RH conclusion.

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
