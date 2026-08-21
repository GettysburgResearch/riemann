# L-32307 — The outer fifteen sixteenths of SHARP are strictly positive

Claim ID: `L-32307`  
Title: Every square-root-hinge average-carry inverse coefficient with `j>T/16` is strictly positive  
Status: **PROPOSED COMPLETE THEOREM — ANALYTIC TAIL + DIRECTED FINITE BASE; INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: `L-32304`; PR #329 `L-32303`; finite multiples-Möbius inversion  
Scope: all endpoints and coefficient indices in the outer fifteen sixteenths; no claim for `j<=T/16` and no RH conclusion

## 1. Exact SHARP criterion

Fix `T>=3` and write

\[
 h_T(q)=q^{-1/2}-T^{-1/2},
 \qquad
 u_T(m)=\sum_{k\le T/m}\mu(k)h_T(mk),
\]

\[
 S_T(j)=\sum_{m=j}^{T}u_T(m).
\]

For the unique average-carry inverse coefficient `c_T(j)`, `L-32304` proves exactly

\[
\boxed{
 j c_T(j)
 =(j+2)u_T(j)-j u_T(j+1)
 +\frac{2S_T(j)}{j-1}.
}
\tag{L-32307.1}
\]

The first term is local in one quotient cell. The second is a normalized Möbius tail.

## 2. Quotient-cell form

If

\[
 K=\left\lfloor\frac{T}{m}\right\rfloor,
\]

put

\[
 A_K=\sum_{k\le K}\frac{\mu(k)}{\sqrt k},
 \qquad
 M_K=\sum_{k\le K}\mu(k).
\]

Then

\[
\boxed{
 u_T(m)=\frac{A_K}{\sqrt m}-\frac{M_K}{\sqrt T}.
}
\tag{L-32307.2}
\]

The present theorem needs only the fixed quotient cells `K<=15`.

`X-32303` uses directed rational intervals for every inverse square root and exact integer-square comparisons to certify the following fixed inequalities.

### Positive outer states

Throughout cells `K=2,...,6`, uniformly over the complete ratio interval of the cell,

\[
\boxed{
\begin{array}{c|ccccc}
K&2&3&4&5&6\\ \hline
\sqrt T\,u_T(m)>&2/5&2/5&1/3&1/5&1/8.
\end{array}}
\tag{L-32307.3}
\]

Cell `K=7` is positive as already proved in `L-32304`; its mass will simply be discarded below.

### Inner-cell state floor

For every `K=8,...,15`,

\[
\boxed{
 u_T(m)>-\frac{4}{5\sqrt T}
 \qquad\left(K=\left\lfloor T/m\right\rfloor\right).
}
\tag{L-32307.4}
\]

These are eight fixed radical inequalities; no endpoint-dependent finite scan enters their proof.

## 3. A tail reserve already present above `T/8`

Let

\[
 J_8=\left\lfloor\frac T8\right\rfloor+1.
\]

`L-32304` proves that the top-half `K=1` tail contributes more than

\[
 \frac3{40}\sqrt T
\tag{L-32307.5}
\]

once `T>=40`.

For a quotient cell `K`, the number of integers in

\[
 \frac{T}{K+1}<m\le\frac TK
\]

is at least

\[
 \frac{T}{K(K+1)}-2.
\tag{L-32307.6}
\]

Using only the positive cells `K=2,...,6` from (L-32307.3), and dropping the entire positive `K=7` cell, gives

\[
\begin{aligned}
\frac{S_T(J_8)}{\sqrt T}
>&
\frac3{40}
+\frac25\left(\frac16+\frac1{12}\right)
+\frac13\frac1{20}
+\frac15\frac1{30}
+\frac18\frac1{42}
-\frac{35}{12T}\\
&=
\boxed{
\frac{1691}{8400}-\frac{35}{12T}.
}
\end{aligned}
\tag{L-32307.7}
\]

The error `35/(12T)` deliberately uses two lost integer points per cell; it is weaker than the exact floor error.

## 4. Push the tail reserve down to `T/16`

Now let

\[
 j>\frac{T}{16}.
\]

If `j>=J_8`, no additional argument is needed. Otherwise every newly included index

\[
 j\le m<J_8
\]

belongs to one of the quotient cells `K=8,...,15`. By (L-32307.4), each contributes more than `-4/(5sqrt T)`.

The number of such indices is at most

\[
 \frac{T}{16}+2.
\]

Hence

\[
\begin{aligned}
\frac{S_T(j)}{\sqrt T}
&>
\frac{1691}{8400}-\frac{35}{12T}
-\frac1{20}-\frac{8}{5T}\\
&=
\boxed{
\frac{1271}{8400}-\frac{271}{60T}.
}
\end{aligned}
\tag{L-32307.8}
\]

At `T=256`, the right side exceeds `13/100` by exactly

\[
 \frac{657}{179200}>0,
\]

and it increases with `T`. Therefore

\[
\boxed{
S_T(j)>\frac{13}{100}\sqrt T
\qquad(T\ge256,\ j>T/16).
}
\tag{L-32307.9}

This is the reserve which compensates the first genuinely negative local Möbius states.

## 5. Uniform local factor

Retain

\[
 B_j=\frac{j+2}{\sqrt j}-\frac{j}{\sqrt{j+1}}.
\]

`L-32304` proves

\[
\boxed{B_j<\frac{5}{2\sqrt j}.}
\tag{L-32307.10}

If `j,j+1` stay in the same quotient cell `K`, (L-32307.2) gives

\[
 (j+2)u_T(j)-j u_T(j+1)
 =A_KB_j-\frac{2M_K}{\sqrt T}.
\tag{L-32307.11}

For `K=8,...,15`, all `A_K<0`. Since `j>T/(K+1)`, the fixed radical certificate `X-32303` yields

\[
\boxed{
\begin{array}{c|cccccccc}
K&8&9&10&11&12&13&14&15\\ \hline
\sqrt T\,[(j+2)u(j)-ju(j+1)]>
&-13/10&-8/5&-6/5&-2&-9/4&-31/10&-14/5&-12/5.
\end{array}}
\tag{L-32307.12}
\]

Again these are eight fixed exact radical inequalities, not endpoint reconnaissance.

## 6. Same-cell positivity in every new quotient cell

If `K=floor(T/j)`, then `j-1<T/K`. Equation (L-32307.9) therefore gives

\[
\boxed{
\frac{2S_T(j)}{j-1}
>\frac{13K}{50\sqrt T}.
}
\tag{L-32307.13}

Adding (L-32307.12) gives the following strict lower margins for the complete right side of (L-32307.1):

\[
\boxed{
\begin{array}{c|cccccccc}
K&8&9&10&11&12&13&14&15\\ \hline
\sqrt T\,j c_T(j)>&
39/50&37/50&7/5&43/50&87/100&7/25&21/25&3/2.
\end{array}}
\tag{L-32307.14}

Thus every same-cell pair in the new region is strictly safe.

## 7. Quotient-cell transitions

Suppose `j` is in quotient cell `K` and `j+1` enters cell `K-1`. The actual value `u_T(j+1)` differs from the formal same-`K` continuation by

\[
 \mu(K)
 \left[
 \frac1{\sqrt T}-\frac1{\sqrt{K(j+1)}}
 \right].
\tag{L-32307.15}

The bracket is positive because `K(j+1)>T`. Therefore transitions with `mu(K)<=0` can only improve the local term in (L-32307.1).

For `8<=K<=15`, the only adverse transitions have

\[
 \mu(10)=\mu(14)=\mu(15)=1.
\]

Write `T=Kj+r`, `0<=r<K`. Then

\[
0<\frac1{\sqrt T}-\frac1{\sqrt{K(j+1)}}
<\frac{K}{2T^{3/2}}.
\]

Since `j<T/K`, the complete transition loss in (L-32307.1) is less than

\[
\frac1{2\sqrt T}.
\tag{L-32307.16}

Subtracting this from the corresponding same-cell margins in (L-32307.14) leaves

\[
\boxed{
K=10:\ \frac9{10\sqrt T},
\qquad
K=14:\ \frac{17}{50\sqrt T},
\qquad
K=15:\ \frac1{\sqrt T}.
}
\tag{L-32307.17}

Every quotient transition is therefore strictly positive.

## 8. Cofinal theorem

For `T>=256`, `L-32304` already handles every `j>T/8`. Sections 3--7 handle the entire remaining strip

\[
\frac{T}{16}<j\le\frac{T}{8}.
\]

Hence

\[
\boxed{
 c_T(j)>0
 \qquad
 (T\ge256,\ 2\le j<T,\ j>T/16).
}
\tag{L-32307.18}

## 9. Directed finite base

`X-32303` uses only the Python standard library, exact Möbius integers, and directed rational inverse-square-root intervals certified by integer squares.

It checks every endpoint

\[
3\le T\le255
\]

and every coefficient index `j>T/16`, a total of

\[
\boxed{30,451}
\]

coefficient rows, with no failure.

The same proof object independently certifies:

- the five positive-state constants in (L-32307.3);
- the eight inner-state floors in (L-32307.4);
- the eight local lower bounds in (L-32307.12);
- the tail arithmetic at `T=256`;
- all same-cell and adverse-transition rational margins.

Combining the finite base with (L-32307.18) proves

\[
\boxed{
 c_T(j)>0
 \qquad
 \text{for every }T\ge3,\ 2\le j<T,\ j>\frac{T}{16}.
}
\tag{L-32307.19}

As before, `c_T(T)=0` exactly.

## 10. Significance and new frontier

`L-32304` confined every possible SHARP failure to the inner eighth. The present theorem halves the unresolved region again:

\[
\boxed{
\text{every possible SHARP failure is confined to }j\le T/16.
}
\]

The proof has crossed the first quotient cells where the local Möbius state itself becomes negative. Positivity now comes from a **global positive tail reserve compensating a negative local state**, not from local Möbius positivity.

This is the mechanism any deeper SHARP proof must preserve. It is source-specific and does not imply generic Abel or average-carry positivity.

## 11. Proof boundary

Closed here, subject to independent review:

- exact fixed quotient inequalities through `K=15`;
- a uniform positive tail reserve down to `T/16`;
- strict same-cell margins in all new quotient cells;
- every quotient transition, including all three adverse positive-Möbius transitions;
- directed finite completion through `T=255`;
- SHARP positivity for every `j>T/16`.

Open:

- the inner sixteenth `j<=T/16`;
- full SHARP;
- the zero-safe low-row sign of PR #326;
- RH.
