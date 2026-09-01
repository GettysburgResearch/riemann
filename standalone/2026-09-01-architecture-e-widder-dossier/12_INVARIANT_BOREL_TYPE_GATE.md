# Invariant Borel transform and the exponential-type gate

Status: **PROPOSED EXACT THEOREMS; INDEPENDENT REVIEW REQUIRED; THE TYPE-ONE SOURCE BOUND, THE ALL-ORDER E--WIDDER INEQUALITY, AND RH REMAIN UNPROVED.**

The radial order product in
[`09_INVARIANT_ORDER_PRODUCT_AND_COUNT_LAW.md`](09_INVARIANT_ORDER_PRODUCT_AND_COUNT_LAW.md)
has a finite radius whenever an off-line invariant zero is present.  This note
removes that finite-radius obstruction by factorial summation.

The resulting Borel transform is entire for every invariant scale.  Its
exponential type is exactly the largest modulus of the transformed invariant
zero atoms.  RH is therefore equivalent to a type-one theorem.  The published
zero-height verification already proves that the type exceeds one, if at all,
by less than `5.56e-26`.

This is a different completion target from coefficientwise Widder positivity:

```text
E--Widder front: every normalized power trace is nonnegative;
Borel front:     one entire source transform has exponential type at most one.
```

Either theorem implies RH.

## 1. Normalized power traces

Retain

\[
 C_k(u)
 =\frac{(4u)^k}{2(2k-1)!}\mathcal W_k(u)
 =\sum_a\lambda_u(a)^k,
\]

where

\[
 \lambda_u(a)=\frac{4ua}{(u+a)^2}.
 \tag{1.1}
\]

The invariant zero multiset satisfies

\[
 \sum_a\frac1{|a|}<\infty.
\]

For each fixed `u>0`,

\[
 \lambda_u(a)=O_u(1/a),
\]

and hence

\[
 \sum_a|\lambda_u(a)|<\infty.
 \tag{1.2}
\]

## 2. Entire factorial summation

Define

\[
 \boxed{
 \mathcal E_u(\tau)
 =\sum_{k\ge1}\frac{C_k(u)}{k!}\tau^k.
 }
 \tag{2.1}
\]

Using (1.2), the zero-side series

\[
 \boxed{
 \mathcal E_u(\tau)
 =\sum_a\left(e^{\tau\lambda_u(a)}-1\right)
 }
 \tag{2.2}
\]

converges locally uniformly in `tau`.  Indeed, outside a finite set of atoms,

\[
 |e^{\tau\lambda}-1|
 \le C_T|\lambda|
 \qquad(|\tau|\le T).
\]

Thus `mathcal E_u` is entire.

The ordinary generator and the Borel transform are related by exact
Borel--Laplace summation.  Wherever the integral converges,

\[
 \boxed{
 w\mathscr C_u(w)
 =\int_0^\infty e^{-t}\mathcal E_u(wt)\,dt.
 }
 \tag{2.3}
\]

This follows termwise from

\[
 \int_0^\infty e^{-t}t^k\,dt=k!.
\]

Consequently the first real pole of the ordinary generator is the reciprocal
of the Borel growth rate.

## 3. Exact exponential type

Let

\[
 L(u)=\sup_a|\lambda_u(a)|.
 \tag{3.1}
\]

Because `lambda_u(a)->0`, the supremum is attained by a finite peripheral
set.

### Theorem 3.1

\[
 \boxed{
 \operatorname{type}(\mathcal E_u)=L(u).
 }
 \tag{3.2}
\]

#### Upper bound

For every `epsilon>0`, split the atom set into the finite subset with
`|lambda|>epsilon` and its complement.  Equation (2.2) gives

\[
 |\mathcal E_u(\tau)|
 \le A_{\epsilon,u}(1+|\tau|)
 e^{L(u)|\tau|}.
\]

Hence the type is at most `L(u)`.

#### Lower bound

Choose a peripheral atom `lambda_*` with

\[
 |\lambda_*|=L(u)
\]

and evaluate on the ray

\[
 \tau=t\,e^{-i\arg\lambda_*}.
\]

The atoms having maximal real exponent on this ray form a finite set.  Their
leading coefficient is a nonzero finite trigonometric polynomial.  Its mean
square is positive, so its modulus has a positive limsup.  All remaining
atoms have strictly smaller exponential rate after first removing the
infinite tail `lambda->0`.  Therefore

\[
 \limsup_{t\to\infty}
 \frac1t\log|\mathcal E_u(te^{-i\arg\lambda_*})|
 \ge L(u).
\]

This proves (3.2). `square`

Equivalently, the coefficient formula for an exponential generating function
gives

\[
 \boxed{
 \operatorname{type}(\mathcal E_u)
 =\limsup_{k\to\infty}|C_k(u)|^{1/k}.
 }
 \tag{3.3}
\]

## 4. Type one is equivalent to RH

Under RH every invariant atom is positive real.  The arithmetic--geometric
mean inequality gives

\[
 0<\lambda_u(a)=\frac{4ua}{(u+a)^2}\le1,
\]

so

\[
 L(u)\le1
\]

for every `u>0`.

Conversely, let

\[
 a=Re^{i\alpha},
 \qquad \alpha\ne0,
\]

be an off-line invariant atom.  At its canonical matching scale `u=R`,

\[
 \lambda_R(a)=\sec^2(\alpha/2)>1.
\]

Hence

\[
 L(R)>1.
\]

Theorem 3.1 yields the exact criterion

\[
 \boxed{
 {\rm RH}
 \iff
 \operatorname{type}(\mathcal E_u)\le1
 \quad\text{for every }u>0.
 }
 \tag{4.1}
\]

A single off-line orbit raises the type at one explicitly determined scale.

This proof does not use sign cancellation among Widder coefficients.  The
matching transformed atom is positive real and lies outside the type-one
disk.

## 5. Exact angle and modulus formula

Write

\[
 a=Re^{i\alpha},
 \qquad
 u=Re^v.
\]

The shifted hyperbolic formula is

\[
 \lambda_u(a)
 =\operatorname{sech}^2\left(\frac{v-i\alpha}{2}\right).
\]

Therefore

\[
 \boxed{
 |\lambda_u(a)|
 =
 \frac1{
  \cosh^2(v/2)-\sin^2(\alpha/2)
 }.
 }
 \tag{5.1}
\]

The maximum over `u>0` is attained at `v=0`:

\[
 \boxed{
 \sup_{u>0}|\lambda_u(a)|
 =\sec^2(\alpha/2).
 }
 \tag{5.2}
\]

Thus the Borel type measures invariant zero angle exactly.

## 6. Verified height gives a near-type-one theorem

Assume every zero through height `H` is critical.  The invariant angle theorem
in `08_FINITE_HEIGHT_WIDDER_CONE.md` gives, for every hypothetical off-line
zero above `H`,

\[
 |\alpha|<\alpha_H:=\arctan(1/H).
\]

Critical atoms have `alpha=0`.  Equations (3.2) and (5.2) therefore imply,
uniformly for every `u>0`,

\[
 \boxed{
 \operatorname{type}(\mathcal E_u)
 \le
 \sec^2(\alpha_H/2)
 =
 \frac1{w_H},
 }
 \tag{6.1}
\]

where

\[
 w_H
 =\cos^2(\alpha_H/2)
 =\frac12\left(1+\frac{H}{\sqrt{H^2+1}}\right).
\]

Since `w_H>1/2`,

\[
 \frac1{w_H}-1
 =\frac{1-w_H}{w_H}
 <2(1-w_H)
 <\frac1{2H^2}.
 \tag{6.2}
\]

For the imported verified height

\[
 H=3\cdot10^{12},
\]

this gives

\[
 \boxed{
 \operatorname{type}(\mathcal E_u)
 <1+5.56\cdot10^{-26}
 \qquad(u>0).
 }
 \tag{6.3}
\]

The external zero computation is imported through the existing exact source
lock and is not rerun.

Thus the remaining all-order theorem can be stated as removal of a possible
excess exponential type below `5.56e-26`.

## 7. Source-side Borel transform

Every coefficient in (2.1) has the Euler-safe expression

\[
 C_k(u)
 =
 \frac{(4u)^k}{2(2k-1)!}
 \left[
  \mathcal G_k(u)
  -\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
   \mathcal L_k(u,\log n)
 \right].
 \tag{7.1}
\]

Consequently the formal source transform is

\[
 \boxed{
 \begin{aligned}
 \mathcal E_u^{\rm src}(\tau)
 =\sum_{k\ge1}
 \frac{(4u\tau)^k}{2k!(2k-1)!}
 \Bigg[
  \mathcal G_k(u)
  -\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
   \mathcal L_k(u,\log n)
 \Bigg].
 \end{aligned}
 }
 \tag{7.2}
\]

Each fixed-order prime series is absolutely convergent at

\[
 s=\frac12+\sqrt{u+\frac14}>1.
\]

The zero-side theorem proves that the completed expression (7.2), when
assembled before any absolute envelope, is entire and equals (2.2).

The independent source theorem to prove is the type-one estimate

\[
 \boxed{
 \forall\epsilon>0\quad
 |\mathcal E_u^{\rm src}(\tau)|
 \le A_{u,\epsilon}
 e^{(1+\epsilon)|\tau|}
 \qquad(\tau\in\mathbb C).
 }
 \tag{7.3}
\]

It is essential that the gamma and prime labels be assembled before taking
absolute values.  A coefficientwise absolute bound can easily create type
strictly larger than one and would erase the RH-bearing cancellation.

## 8. Why this is new leverage

The ordinary order generator has an exact direct-Euler barrier and possible
interior poles.  The Borel transform is entire regardless of RH.

The conclusion-bearing distinction is now only growth:

```text
critical invariant divisor:
    every transformed exponent has modulus <=1;

off-line invariant divisor:
    one matching exponent has modulus >1.
```

There is no sign choice at the matching scale and no need to locate the
negative Widder coefficient.  An off-line zero changes a positive real
exponential rate.

The source attack may therefore use:

1. factorially weighted derivative estimates;
2. Bessel/Laguerre summation of the prime filters;
3. entire-function indicator bounds;
4. the theta--Darboux exterior-current representation;
5. the quasi-free determinant gate.

A successful type estimate at one scale family closes RH through (4.1).

## 9. Exact boundary

```text
local uniform Borel summation                  PROPOSED COMPLETE / REVIEW
Borel--Laplace relation                        PROPOSED COMPLETE / REVIEW
type equals maximal transformed-atom modulus   PROPOSED COMPLETE / REVIEW
RH iff type <=1 at every invariant scale       PROPOSED COMPLETE / REVIEW
verified-height type <1+5.56e-26               PROPOSED COMPLETE / REVIEW
independent source-side type-one bound         OPEN / RH-EQUIVALENT
all-order E--Widder source inequality          OPEN / RH-EQUIVALENT
Riemann Hypothesis                             UNPROVED
```

## 10. Review checklist

1. local uniform convergence in (2.2);
2. the Borel--Laplace factor `w` in (2.3);
3. the lower exponential-type bound for a finite peripheral exponent set;
4. the coefficient formula (3.3);
5. the matching-scale value `sec^2(alpha/2)`;
6. the modulus identity (5.1);
7. the finite-height uniform type bound;
8. the distinction between zero-side equality and an independent source-side
   proof of (7.3).
