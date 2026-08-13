# R-91306 — The positive four-state rough dilation is not total-variation contractive

Claim ID: `R-91306`  
Status: **EXACT MATRIX REFUTATION / SCOPE CORRECTION**  
Created: 2026-08-12  
Depends on: `L-91327`  
RH status: **unproved**

## 1. The claimed ledger

`L-91327` defines, for `0<B<=A<=1` and `d=A-B`,

\[
 \widetilde D(A,B)=
 \begin{pmatrix}
  2A-B&0&0&0\\
  d&B&0&0\\
  0&d&A&0\\
  0&0&0&B
 \end{pmatrix}
\tag{R-91306.1}
\]

and claims that the total positive mass

\[
 \mathfrak m(z)=u+v+z+w
\]

is nonincreasing.

## 2. Exact counterexample

Take the positive input

\[
 e_1=(1,0,0,0)^T.
\]

Then

\[
 \widetilde D(A,B)e_1
 =(2A-B,d,0,0)^T
\]

and hence

\[
 \mathfrak m(\widetilde D e_1)
 =2A-B+d
 =3A-2B.
\tag{R-91306.2}

For one prime put

\[
 r=p^{-1/2},
 \qquad A=1-r^2,
 \qquad B=1-r.
\]

Then

\[
\boxed{
 3A-2B-1
 =2r-3r^2
 =r(2-3r)>0
}
\tag{R-91306.3
}

for every `p>=3`. In particular it is positive for every rough prime
`p>=67`.

Equivalently, the first coefficient in the displayed loss formula of
`L-91327.14` is

\[
 1-3A+2B=r(3r-2)<0,
\]

not nonnegative.

Thus

\[
\boxed{
 \mathfrak m(\widetilde D e_1)>\mathfrak m(e_1).
}
\tag{R-91306.4
}

## 3. What survives

The intertwining identity

\[
 O\widetilde D=M O
\]

and entrywise positivity of `widetilde D` survive. The four-state system remains
a valid positive linear dilation of the signed two-state Euler action.

What fails is the asserted `ell^1` contraction and every argument which derives
from it:

```text
pathwise total-variation loss;
subprobability branch weights;
linear mass telescope based on u+v+z+w;
absence of branch amplification in that norm.
```

## 4. Consequences for descendants

The following uses require repair or an independent ledger:

- the mass-contractive interpretation in `L-91327.5`;
- the nomination of `L-91327` as supplying the weights in `T-91302`;
- any source partition in `L-91325` or later reports which relies on
  `sum theta_b<=1` through this total-variation functional.

The positive-functor and sum-before-quantize theorems are unaffected; they are
linear/ordering statements, not contraction statements.

## 5. Correct next target

A valid branching proof must find a different positive ledger—possibly
scale-weighted, state-dependent or score-neutral—or prove source subprobability
directly from a least-prime disintegration. No fixed unweighted `ell^1` mass is
available from (R-91306.1).

```text
positive four-state dilation                    RETAINED EXACT
fixed observation/intertwining                  RETAINED EXACT
unweighted total-variation contraction          FALSE
subprobability weights from that ledger         BLOCKED
alternative positive ledger                     OPEN
Riemann Hypothesis                              UNPROVEN
```
