# L-30105 — Factor-five outer Möbius divergence is positive

Claim ID: `L-30105`  
Title: For the critical carry target, every Möbius-divergence coefficient above one fifth of the endpoint is strictly positive  
Status: **PROPOSED COMPLETE ELEMENTARY THEOREM — INDEPENDENT REVIEW REQUESTED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Dependencies: only `mu(1)=1`, `mu(2)=mu(3)=-1`, `mu(4)=0` and elementary calculus  
Scope: exact sign localization for the PR #272 odd-commutator source; no estimate below one fifth and no RH conclusion

## 1. Critical target and Möbius profile

Fix a real endpoint `X>=5` and put

\[
w_X(t)=t^{-1/2}\log(X/t),
\qquad0<t\le X.
\tag{L-30105.1}

For real `m>0`, define the piecewise-smooth Möbius profile

\[
\boxed{
u_X(m)=
\sum_{d\le X/m}\mu(d)w_X(dm).
}
\tag{L-30105.2}

At integer arguments, PR #272's divergence is

\[
r_X(m)=u_X(m)-u_X(m+1).
\tag{L-30105.3}

We prove that `u_X` is strictly decreasing on `(X/5,X)`. It follows immediately that

\[
\boxed{
r_X(m)>0
\qquad\text{for every integer }X/5<m<X.
}
\tag{L-30105.4
}

The closing bracket in the equation tag is typographical only.

## 2. Logarithmic derivative

Put

\[
L=\log(X/m)
\]

and

\[
h_L(c)=c^{-1/2}
\left(1+{L-\log c\over2}\right).
\tag{L-30105.5}

Direct differentiation gives

\[
-m{d\over dm}w_X(cm)=m^{-1/2}h_L(c).
\tag{L-30105.6}

On `(X/5,X)`, the quotient `floor(X/m)` is at most four. Since

\[
\mu(1)=1,
\qquad
\mu(2)=\mu(3)=-1,
\qquad
\mu(4)=0,
\]

there are only three derivative patterns.

## 3. Quotient cells one and two

When `1<=X/m<2`,

\[
u_X(m)=w_X(m)
\]

and the derivative is strictly negative.

When `2<=X/m<3`,

\[
u_X(m)=w_X(m)-w_X(2m).
\]

Equation (L-30105.6) gives

\[
-mu_X'(m)
=m^{-1/2}[h_L(1)-h_L(2)]>0,
\tag{L-30105.7}

because both the factor `c^(-1/2)` and the logarithmic bracket decrease from `c=1` to `c=2`.

## 4. Quotient cells three and four

When `3<=X/m<5`, the `d=4` coefficient vanishes and

\[
u_X(m)=w_X(m)-w_X(2m)-w_X(3m).
\]

Thus

\[
-mu_X'(m)
=m^{-1/2}\Phi(L),
\tag{L-30105.8}

where

\[
\Phi(L)=
1+{L\over2}
-{1\over\sqrt2}
 \left(1+{L-\log2\over2}\right)
-{1\over\sqrt3}
 \left(1+{L-\log3\over2}\right).
\tag{L-30105.9}

Its slope is

\[
\Phi'(L)
={1\over2}
\left(1-{1\over\sqrt2}-{1\over\sqrt3}\right)<0.
\]

Throughout these cells `L<log 5`, so the minimum is bounded below by the value at `log 5`.

The following elementary rational enclosures suffice:

\[
{1\over\sqrt2}<{71\over100},
\qquad
{1\over\sqrt3}<{58\over100},
\tag{L-30105.10}

\[
\log2>{69\over100},
\qquad
\log3>{109\over100},
\qquad
\log5<{161\over100}.
\tag{L-30105.11}

They follow, for example, by squaring the rational square-root bounds and by the alternating/positive exponential series. Substitution gives

\[
\begin{aligned}
\Phi(\log5)
&>
1+{161\over200}\\
&\quad-{71\over100}
 \left(1+{161\over200}-{69\over200}\right)\\
&\quad-{58\over100}
 \left(1+{161\over200}-{109\over200}\right)\\
&={47\over1250}>0.
\end{aligned}
\tag{L-30105.12}

Therefore `u_X'(m)<0` on every quotient-three and quotient-four cell.

## 5. Cell boundaries

When a new divisor term enters at `m=X/d`, its value is

\[
w_X(dm)=w_X(X)=0.
\]

Thus `u_X` is continuous at the quotient boundaries `X/2` and `X/3`. There is no change at `X/4` because `mu(4)=0`.

The strict derivative signs from Sections 3–4 therefore concatenate across the complete interval:

\[
\boxed{
u_X(m)\text{ is strictly decreasing on }(X/5,X).
}
\tag{L-30105.13

The closing brace in the equation tag is typographical only.

Combining (L-30105.3) and (L-30105.13) proves (L-30105.4).

## 6. Consequence for the dyadic commutator normal form

At endpoint `X=2Y`, PR #272 writes the complete odd source as

\[
Q_Y=
\sum_{a=1}^{Y-1}r_X(2a+1)E_{2a}.
\]

The present theorem shows

\[
r_X(2a+1)>0
\qquad
\text{whenever }2a+1>X/5.
\tag{L-30105.14}

Hence every genuinely sign-indefinite odd coefficient is confined to

\[
\boxed{2a+1\le X/5,}
\tag{L-30105.15}

which is a strict factor-five lower scale.

Together with `R-30102/L-30104`, the outer odd source has the exact disposition

```text
X/5 < 2a+1 <= X/2:
    positive coefficient, parent-4a sibling switch lies inside endpoint;

X/2 < 2a+1 < X:
    positive coefficient, escaped switch replaced by legal E_(2a),
    complete family debt O(1);

2a+1 <= X/5:
    sole remaining signed source, already at strict lower scale.
```

This is a source-level factor-five localization. It does not use a bounded-rank, face-count, or positive-Hankel assertion.

## 7. Proof boundary

Closed exactly:

1. the real interpolation of the outer Möbius profile;
2. derivative negativity on quotient cells one through four;
3. rigorous positivity of the quotient-three/four derivative gap;
4. continuity across every active boundary;
5. strict positivity of every integer divergence coefficient above `X/5`;
6. confinement of all signed odd coefficients to strict factor-five scale.

Still open:

- a complete recursive flow/capacity ledger for the inner source `m<=X/5` coupled to the doubled lower flow;
- RH.
