# L-32304 — Square-root hinge inverse is positive on the outer four fifths

Claim ID: `L-32304`  
Title: Every square-root hinge average-carry inverse coefficient with `5j>T` is strictly positive; the unresolved SHARP region is confined to the inner fifth  
Status: **PROPOSED COMPLETE ELEMENTARY THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-10  
Dependencies: `L-32303` exact adjoint formula  
Scope: exact all-endpoint theorem for the outer four fifths; no claim for `j<=T/5` and no RH conclusion

## 1. Statement

For an integer endpoint `T>=3`, let

\[
h_T(q)=q^{-1/2}-T^{-1/2},\qquad 2\le q\le T,
\]

and let `c_T(j)` be the unique triangular average-carry inverse from `L-32303`:

\[
h_T(q)=\sum_{n=q}^T c_T(n)\beta_{nq}.
\]

Then

\[
\boxed{
5j>T,\quad 2\le j<T
\quad\Longrightarrow\quad
c_T(j)>0.
}
\tag{L-32304.1}
\]

Thus full SHARP can fail, if at all, only in

\[
\boxed{2\le j\le T/5.}
\tag{L-32304.2}
\]

The endpoint coefficient remains `c_T(T)=0` exactly.

## 2. Multiples-Mobius state and a local positivity criterion

For `m>=2` define

\[
u_T(m)=\sum_{k\le T/m}\mu(k)
\left((mk)^{-1/2}-T^{-1/2}\right)
\tag{L-32304.3}
\]

and the tail

\[
S_T(j)=\sum_{m=j}^T u_T(m).
\tag{L-32304.4}
\]

`L-32303.9` gives

\[
c_T(j)=
\frac{(j+1)[j u_T(j)-(j-2)u_T(j+1)]+2S_T(j+2)}{j(j-1)}.
\]

Using

\[
S_T(j+2)=S_T(j)-u_T(j)-u_T(j+1)
\]

one obtains the exact simplification

\[
\boxed{
jc_T(j)
=(j+2)u_T(j)-j u_T(j+1)
+\frac{2S_T(j)}{j-1}.}
\tag{L-32304.5}
\]

Therefore it is enough to prove, for `5j>T`,

\[
S_T(j)>0
\tag{L-32304.6}
\]

and

\[
L_T(j):=(j+2)u_T(j)-j u_T(j+1)>0.
\tag{L-32304.7}
\]

## 3. Only three formulas occur above `T/5`

If `m>T/5`, then `floor(T/m)<=4`.  Since

\[
\mu(1)=1,\qquad \mu(2)=\mu(3)=-1,\qquad \mu(4)=0,
\]

put

\[
a=1-\frac1{\sqrt2}>0,
\qquad
d=\frac1{\sqrt2}+\frac1{\sqrt3}-1.
\tag{L-32304.8}
\]

Then exactly

\[
\boxed{
u_T(m)=
\begin{cases}
 m^{-1/2}-T^{-1/2},&\lfloor T/m\rfloor=1,\\[1mm]
 a\,m^{-1/2},&\lfloor T/m\rfloor=2,\\[1mm]
 T^{-1/2}-d\,m^{-1/2},&\lfloor T/m\rfloor\in\{3,4\}.
\end{cases}}
\tag{L-32304.9}
\]

The equality of the quotient-three and quotient-four cells is the exact `mu(4)=0` cancellation.

The constants obey the elementary rational bounds

\[
0<d<\frac3{10},\qquad a>\frac14.
\tag{L-32304.10}
\]

Indeed,

\[
\frac1{\sqrt2}<\frac57,
\qquad
\frac1{\sqrt3}<\frac7{12},
\]

so

\[
d<\frac57+\frac7{12}-1=\frac{25}{84}<\frac3{10},
\]

while `1/sqrt(2)<3/4` gives `a>1/4`.  Positivity of `d` follows from `1/sqrt(2)>1/2` and `1/sqrt(3)>1/2`.

For the last line of (L-32304.9), `m>T/5` gives

\[
T^{-1/2}-d m^{-1/2}
>T^{-1/2}(1-d\sqrt5)>0
\]

because `d<3/10` and `sqrt(5)<3`.  The other two lines are visibly nonnegative, and they are strictly positive for every `m<T`.

Hence, whenever `5j>T` and `j<T`, every term in `S_T(j)` is nonnegative and its first term is positive.  Therefore

\[
\boxed{S_T(j)>0.}
\tag{L-32304.11}
\]

## 4. A universal square-root increment bound

Define

\[
R_j=\frac{j+2}{\sqrt j}-\frac{j}{\sqrt{j+1}}.
\tag{L-32304.12}
\]

For every integer `j>=1`,

\[
\boxed{
\frac2{\sqrt{j+1}}<R_j<\frac5{2\sqrt j}.}
\tag{L-32304.13}
\]

The lower bound is immediate:

\[
R_j-\frac2{\sqrt{j+1}}
=(j+2)\left(\frac1{\sqrt j}-\frac1{\sqrt{j+1}}\right)>0.
\]

For the upper bound it is enough to show

\[
j\left(1-\sqrt{\frac j{j+1}}\right)<\frac12.
\]

Equivalently,

\[
\sqrt{\frac j{j+1}}>1-\frac1{2j}.
\]

Both sides are nonnegative, and after squaring the difference is

\[
\frac{3j-1}{4j^2(j+1)}>0.
\]

This proves (L-32304.13).

## 5. Interior of each quotient formula

Suppose first that `u_T(j)` and `u_T(j+1)` are governed by the same line of (L-32304.9).

### Quotient one

Then

\[
L_T(j)=R_j-\frac2{\sqrt T}.
\]

Since `T>=j+1`, (L-32304.13) gives

\[
R_j>\frac2{\sqrt{j+1}}\ge\frac2{\sqrt T},
\]

so `L_T(j)>0`.

### Quotient two

Here

\[
L_T(j)=aR_j>0.
\]

### Quotients three and four

The common formula gives

\[
L_T(j)=\frac2{\sqrt T}-dR_j.
\]

Using (L-32304.10), (L-32304.13), `j>T/5`, and `sqrt(5)<8/3`,

\[
\begin{aligned}
dR_j
&<\frac3{10}\frac5{2\sqrt j}\\
&<\frac3{10}\frac52\frac{\sqrt5}{\sqrt T}\\
&<\frac3{10}\frac52\frac{8}{3\sqrt T}
=\frac2{\sqrt T}.
\end{aligned}
\]

Hence again `L_T(j)>0`.

The quotient-four to quotient-three boundary requires no separate argument because `mu(4)=0` makes the two formulas identical.

## 6. The quotient-three to quotient-two transition

The only remaining transition between the lower formula and quotient two has

\[
\lfloor T/j\rfloor=3,
\qquad
\lfloor T/(j+1)\rfloor=2,
\]

so

\[
T\in\{3j,3j+1,3j+2\}.
\tag{L-32304.14}
\]

Since

\[
d+a=\frac1{\sqrt3},
\]

one gets exactly

\[
L_T(j)
=aR_j+(j+2)\left(\frac1{\sqrt T}-\frac1{\sqrt{3j}}\right).
\tag{L-32304.15}
\]

The second term is nonnegative when `T=3j`.  In the two remaining cases its negative magnitude is at most

\[
E_j=(j+2)
\left(\frac1{\sqrt{3j}}-\frac1{\sqrt{3j+2}}\right).
\]

Using the exact difference-of-square-roots denominator,

\[
E_j<\frac{j+2}{(3j)^{3/2}}.
\]

Here `j>=2`; hence `j+2<=2j`.  Since `sqrt(3)>5/3`,

\[
E_j<\frac2{3\sqrt3\sqrt j}<\frac2{5\sqrt j}.
\tag{L-32304.16}
\]

On the other hand, `a>1/4` and (L-32304.13) give

\[
aR_j>\frac1{2\sqrt{j+1}}.
\]

For `j>=2`,

\[
\frac1{2\sqrt{j+1}}\ge\frac2{5\sqrt j}
\]

because `25j>=16(j+1)`.  Thus `aR_j>E_j` and

\[
\boxed{L_T(j)>0}
\]

also across the `3 -> 2` transition.

## 7. The quotient-two to quotient-one transition

Here

\[
T\in\{2j,2j+1\}.
\tag{L-32304.17}
\]

If `T=2j`, then

\[
L_T(j)=R_j-\frac2{\sqrt{2j}}>0,
\]

because `j>=2` and

\[
R_j>\frac2{\sqrt{j+1}}>\frac2{\sqrt{2j}}.
\]

If `T=2j+1`, write

\[
D_j=\frac{j+2}{\sqrt{2j}}-\frac j{\sqrt{2j+1}}.
\]

Then

\[
L_T(j)=R_j-D_j.
\]

Split

\[
D_j=
\frac2{\sqrt{2j}}
+j\left(\frac1{\sqrt{2j}}-\frac1{\sqrt{2j+1}}\right).
\]

By the mean-value theorem for `x^{-1/2}`,

\[
j\left(\frac1{\sqrt{2j}}-\frac1{\sqrt{2j+1}}\right)
<\frac1{4\sqrt{2j}},
\]

so

\[
D_j<\frac9{4\sqrt{2j}}.
\tag{L-32304.18}
\]

But (L-32304.13) gives

\[
R_j>\frac2{\sqrt{j+1}}
>\frac9{4\sqrt{2j}},
\]

where the final inequality is equivalent after squaring to

\[
128j>81(j+1),
\]

which holds for every `j>=2`.  Hence `L_T(j)>0` across the final transition as well.

## 8. Completion

Sections 5--7 exhaust every possible pair of adjacent quotient cells when `j>T/5`.  Therefore

\[
L_T(j)>0.
\]

Together with the tail positivity (L-32304.11), the exact identity (L-32304.5) gives

\[
jc_T(j)>0.
\]

Thus

\[
\boxed{c_T(j)>0\qquad(5j>T,\ 2\le j<T).}
\]

This proves (L-32304.1).

## 9. Significance and proof boundary

This converts the million-endpoint directed nomination on `X-32301` into a cofinal symbolic theorem over a macroscopic portion of every endpoint:

```text
old unconditional region on the hinge route: top half;
new unconditional region:                  outer four fifths;
remaining possible SHARP obstruction:       inner one fifth.
```

No zero-free region, PNT, Mertens estimate, or numerical scan enters the proof.  The factor five is arithmetic: it is exactly the first quotient at which `mu(5)=-1` introduces a genuinely new formula.

The theorem does **not** prove SHARP or RH.  The inner fifth retains the reciprocal-zeta/Mertens obstruction identified on PR #332 and in `T-32403`.