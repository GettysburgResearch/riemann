# L-91661 — The `P_61` finite-Euler response agrees with native capacity exactly before the first rough activation

Claim ID: `L-91661`  
Status: **PROVED EXACT CAPACITY FIREWALL**  
Created: 2026-08-13  
Depends on: `L-91363`  
RH status: **unproved**

Let

\[
P_{61}=\prod_{p\le 61}p
\]

and retain the exact ordinary response of the canonical finite-Euler row from
`L-91363`:

\[
C_{P,X}(q)=q^{-1/2}H_P(X/q),
\]

where, with the zero convention below one,

\[
H_P(Z)=
\sum_{\substack{n\le Z\\(n,P_{61})=1}}
 n^{-1/2}\log(Z/n).
\tag{L-91661.1}
\]

The native ordinary allowance is

\[
w_X(q)=q^{-1/2}h(X/q),
\qquad
h(Z)=\log Z\,\mathbf 1_{Z\ge1}.
\tag{L-91661.2}
\]

The native radix-four allowance and the canonical detail response are

\[
\Omega_X(q)=q^{-1/2}[h(Z)-h(Z/4)],
\]

\[
\Theta_{P,X}(q)=q^{-1/2}[H_P(Z)-H_P(Z/4)],
\qquad Z=X/q.
\tag{L-91661.3}
\]

## 1. Exact compact equality range

Every integer `2<=n<=66` has a prime factor at most `61`. Therefore the only
integer coprime to `P_61` below `67` is `1`. At `Z=67`, the additional coprime
integer `67` enters with zero logarithmic weight. Hence

\[
\boxed{H_P(Z)=h(Z)\qquad(0<Z\le67).}
\tag{L-91661.4}
\]

Consequently, on every physical column satisfying `X/q<=67`,

\[
\boxed{C_{P,X}(q)=w_X(q)}
\tag{L-91661.5}
\]

and, because also `X/(4q)<=67`,

\[
\boxed{\Theta_{P,X}(q)=\Omega_X(q).}
\tag{L-91661.6}
\]

This is the exact finite-window scope in which the canonical row has the native
ordinary and detail dictionary.

## 2. Immediate strict overfill after `67`

For every `Z>67`, the term `n=67` in (L-91661.1) is strictly positive, while
all other new terms are nonnegative. Thus

\[
\boxed{
H_P(Z)-h(Z)
\ge 67^{-1/2}\log(Z/67)>0
\qquad(Z>67).
}
\tag{L-91661.7}
\]

Therefore

\[
\boxed{
C_{P,X}(q)>w_X(q)
\quad\Longleftrightarrow\quad X/q>67.
}
\tag{L-91661.8}
\]

If

\[
67<X/q\le268,
\]

then `X/(4q)<=67`, so the lower endpoint in the radix-four difference still
lies in the equality range. Hence

\[
\boxed{
\Theta_{P,X}(q)-\Omega_X(q)
=C_{P,X}(q)-w_X(q)>0.
}
\tag{L-91661.9}
\]

## 3. First integer-endpoint witness

Take

\[
X=135,
\qquad q=2,
\qquad Z=135/2.
\]

Then `67<Z<68`, and the only active coprime integers are `1` and `67`. Thus

\[
H_P(135/2)
=\log(135/2)+67^{-1/2}\log(135/134).
\]

It follows exactly that

\[
\boxed{
C_{P,135}(2)-w_{135}(2)
=rac1{\sqrt{134}}\log\frac{135}{134}>0.
}
\tag{L-91661.10}
\]

Since `135/8<67`, the same quantity is the detail overfill:

\[
\boxed{
\Theta_{P,135}(2)-\Omega_{135}(2)
=rac1{\sqrt{134}}\log\frac{135}{134}>0.
}
\tag{L-91661.11}
\]

The witness has a simple rational lower bound. From

\[
\log(1+x)>\frac{x}{1+x}
\qquad(x>0)
\]

with `x=1/134`, and from `sqrt(134)<12`,

\[
\boxed{
\frac1{\sqrt{134}}\log\frac{135}{134}
>rac1{135\sqrt{134}}
>rac1{1620}.
}
\tag{L-91661.12}
\]

## 4. Consequence

The canonical `P_61` row has an exact native capacity dictionary only on the
compact quotient window `X/q<=67`. Global coefficientwise positivity of that
row does **not** imply global feasibility against the native allowances
`(w_X,Omega_X)`.

Any valid all-scale use must therefore do one of the following before physical
packing:

1. stop at the first rough activation and recurse on the rough contribution;
2. prove a coordinatewise allowance decomposition subtracting that contribution;
3. replace the global row by a genuinely native-feasible current row.

```text
ordinary response formula                         IMPORTED EXACT
native equality through quotient 67               EXACT
strict ordinary overfill after quotient 67        EXACT
strict detail overfill on 67<Z<=268               EXACT
first integer witness X=135,q=2                   EXACT
canonical row globally native-feasible             FALSE
Riemann Hypothesis                                 UNPROVED
```
