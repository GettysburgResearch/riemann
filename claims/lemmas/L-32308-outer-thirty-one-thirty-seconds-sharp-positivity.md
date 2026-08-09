# L-32308 — The outer thirty-one thirty-seconds of SHARP are strictly positive

Claim ID: `L-32308`  
Title: Every square-root-hinge average-carry inverse coefficient with `j>T/32` is strictly positive  
Status: **PROPOSED COMPLETE THEOREM — ANALYTIC TAIL + DIRECTED FINITE BASE; INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: `L-32307`; PR #329 `L-32303/L-32304`; finite multiples-Möbius inversion  
Scope: all endpoints and coefficient indices in the outer thirty-one thirty-seconds; no claim for `j<=T/32` and no RH conclusion

## 1. Exact SHARP criterion

For

\[
 h_T(q)=q^{-1/2}-T^{-1/2},
\]

put

\[
 u_T(m)=\sum_{k\le T/m}\mu(k)h_T(mk),
 \qquad
 S_T(j)=\sum_{m=j}^{T}u_T(m).
\]

For the unique average-carry inverse coefficient `c_T(j)`, `L-32304/L-32307` prove exactly

\[
\boxed{
 j c_T(j)
 =(j+2)u_T(j)-j u_T(j+1)
 +\frac{2S_T(j)}{j-1}.
}
\tag{L-32308.1}

If

\[
 K=\left\lfloor\frac{T}{m}\right\rfloor,
\]

write

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
\tag{L-32308.2}

The new theorem needs only the fixed quotient cells `K<=31`.

## 2. Fixed cell lower bounds through quotient thirty-one

`X-32304` uses exact Möbius integers and directed rational enclosures for every square root. It certifies the following lower bounds for the complete scaled cell state

\[
 \sqrt T\,u_T(m)>L_K,
 \qquad
 K=\lfloor T/m\rfloor,
\]

with

\[
\boxed{
\begin{array}{c|rrrrrrrrrrrrrrr}
K&2&3&4&5&6&7&8&9&10&11&12&13&14&15\\ \hline
L_K&.41&.43&.36&.20&.14&.01&-.11&-.22&-.28&-.38&-.48&-.61&-.70&-.76
\end{array}}
\tag{L-32308.3}

and

\[
\boxed{
\begin{array}{c|rrrrrrrrrrrrrrrr}
K&16&17&18&19&20&21&22&23&24&25&26&27&28&29&30&31\\ \hline
L_K&-.81&-.89&-.97&-1.08&-1.18&-1.25&-1.30&-1.37&-1.44&-1.51&-1.56&-1.61&-1.65&-1.71&-1.79&-1.88
\end{array}}
\tag{L-32308.4}

All decimals in the two tables are terminating rationals, not floating approximations.

The same directed proof object certifies the stronger sign fact

\[
\boxed{
 u_T(m)<0
 \quad\text{throughout every complete quotient cell }K=16,\ldots,31.
}
\tag{L-32308.5}

Thus the entire newly entered band is genuinely negative at the local Möbius-state level. The theorem below is driven by the positive global tail in (L-32308.1), not by local positivity.

## 3. Tail reserve down to `T/32`

Put

\[
 J_{32}=\left\lfloor\frac T{32}\right\rfloor+1.
\]

`L-32304` supplies the top-half contribution

\[
 S_{K=1}>\frac3{40}\sqrt T
\tag{L-32308.6}

for `T>=40`.

For each quotient cell `K>=2`, the number of integers in

\[
 \frac{T}{K+1}<m\le\frac TK
\]

is

\[
 N_K=\left\lfloor\frac TK\right\rfloor
      -\left\lfloor\frac{T}{K+1}\right\rfloor
\]

and therefore

\[
\left|N_K-\frac{T}{K(K+1)}\right|<1.
\tag{L-32308.7}

Using the directed lower bounds `L_K` from (L-32308.3)--(L-32308.4), with the floor error oriented according to the sign of `L_K`, gives

\[
\frac{S_T(J_{32})}{\sqrt T}
>
\frac3{40}
+
\sum_{K=2}^{31}\frac{L_K}{K(K+1)}
-
\frac1T\sum_{K=2}^{31}|L_K|.
\tag{L-32308.8}

The two finite rational sums are

\[
\frac3{40}
+
\sum_{K=2}^{31}\frac{L_K}{K(K+1)}
=
\frac{1054123104558031}{7220177644680000}
>
\frac{29}{200},
\tag{L-32308.9}

and

\[
\sum_{K=2}^{31}|L_K|=\frac{2709}{100}.
\tag{L-32308.10}

Hence for `T>=2048`,

\[
\frac{S_T(J_{32})}{\sqrt T}
>
\frac{29}{200}-\frac{2709}{204800}
=
\frac18+rac{1387}{204800}
>
\boxed{\frac18}.
\tag{L-32308.11}

Now suppose

\[
\frac{T}{32}<j\le\frac{T}{16}.
\]

Every index removed when passing from `S_T(J_32)` to `S_T(j)` lies in one of the cells `16,...,31`, and every such state is negative by (L-32308.5). Removing negative summands can only increase the tail. Therefore

\[
\boxed{
 S_T(j)>\frac18\sqrt T
 \qquad(T\ge2048,\ T/32<j\le T/16).
}
\tag{L-32308.12}

Together with `L-32307`, this is the tail reserve available throughout the new region.

## 4. Uniform local lower bounds in cells sixteen through thirty-one

Retain

\[
 B_j=\frac{j+2}{\sqrt j}-\frac{j}{\sqrt{j+1}}.
\]

`L-32304` proves

\[
 B_j<\frac{5}{2\sqrt j}.
\tag{L-32308.13}

For every `K=16,...,31`, the directed cell data give `A_K<0`. If `j,j+1` remain in the same quotient cell `K`, then

\[
 (j+2)u_T(j)-j u_T(j+1)
 =A_KB_j-\frac{2M_K}{\sqrt T}.
\tag{L-32308.14}

Since `j>T/(K+1)`, equations (L-32308.13)--(L-32308.14) yield

\[
 \sqrt T\,[(j+2)u_T(j)-j u_T(j+1)]
 >\frac52A_K\sqrt{K+1}-2M_K.
\tag{L-32308.15}

`X-32304` certifies the following simpler rational lower bounds for the right side:

\[
\boxed{
\begin{array}{c|rrrrrrrr}
K&16&17&18&19&20&21&22&23\\ \hline
C_K&-2.6&-3.3&-3.5&-4.2&-4.5&-4.2&-3.8&-4.5
\end{array}}
\tag{L-32308.16}

\[
\boxed{
\begin{array}{c|rrrrrrrr}
K&24&25&26&27&28&29&30&31\\ \hline
C_K&-4.6&-4.8&-4.4&-4.6&-4.7&-5.3&-6.0&-6.7
\end{array}}
\tag{L-32308.17}

Again these are terminating rationals with directed radical certificates.

## 5. Same-cell SHARP positivity in the new band

If `K=floor(T/j)`, then `j-1<T/K`. From (L-32308.12),

\[
\frac{2S_T(j)}{j-1}
>\frac{K}{4\sqrt T}.
\tag{L-32308.18}

Combining with (L-32308.16)--(L-32308.17), the complete right side of (L-32308.1) has the following scaled lower margins:

\[
\boxed{
\begin{array}{c|rrrrrrrr}
K&16&17&18&19&20&21&22&23\\ \hline
\sqrt T\,j c_T(j)>&7/5&19/20&1&11/20&1/2&21/20&17/10&5/4
\end{array}}
\tag{L-32308.19}

and

\[
\boxed{
\begin{array}{c|rrrrrrrr}
K&24&25&26&27&28&29&30&31\\ \hline
\sqrt T\,j c_T(j)>&7/5&29/20&21/10&43/20&23/10&39/20&3/2&21/20.
\end{array}}
\tag{L-32308.20}

Every same-cell coefficient in the new strip is therefore strictly positive.

## 6. Quotient-cell transitions

When `j` is in cell `K` and `j+1` enters `K-1`, `L-32307` gives the exact transition correction

\[
 \mu(K)\left[
 \frac1{\sqrt T}-\frac1{\sqrt{K(j+1)}}
 \right].
\tag{L-32308.21}

The bracket is positive. Thus transitions with `mu(K)<=0` improve the local term. Among `K=16,...,31`, the only adverse positive-Möbius transitions are

\[
\boxed{K=21,22,26.}
\tag{L-32308.22}

As in `L-32307`, their complete loss in (L-32308.1) is less than

\[
\frac1{2\sqrt T}.
\tag{L-32308.23}

Subtracting this from the same-cell margins leaves respectively

\[
\boxed{
 K=21:\frac{11}{20\sqrt T},
 \qquad
 K=22:\frac{6}{5\sqrt T},
 \qquad
 K=26:\frac{8}{5\sqrt T}.
}
\tag{L-32308.24}

Every quotient transition is therefore strictly positive.

## 7. Cofinal theorem

For `T>=2048`, `L-32307` already handles every `j>T/16`. Sections 3--6 handle the complete new strip

\[
\frac{T}{32}<j\le\frac{T}{16}.
\]

Hence

\[
\boxed{
 c_T(j)>0
 \qquad
 (T\ge2048,\ 2\le j<T,\ j>T/32).
}
\tag{L-32308.25}

## 8. Directed finite base

`X-32304-outer-thirty-one-thirty-seconds` uses only the Python standard library, exact Möbius integers, integer-square directed enclosures for inverse square roots, and the exact adjoint numerator in (L-32308.1).

It certifies every endpoint

\[
3\le T\le2047
\]

and every coefficient index `j>T/32`: in total

\[
\boxed{2,029,539}
\]

coefficient rows, with no failure.

The same proof object independently certifies:

- every cell-state lower bound in (L-32308.3)--(L-32308.4);
- strict negativity of every new cell `16,...,31`;
- every local lower bound in (L-32308.16)--(L-32308.17);
- the exact tail arithmetic at `T=2048`;
- every same-cell and adverse-transition rational margin.

Its retained proof digest is

```text
64619c8fd5f1d4cf01c58a93a1421148c97675a05d0aa4d785d7464d5c8927c4
```

Combining the finite base with (L-32308.25) proves

\[
\boxed{
 c_T(j)>0
 \qquad
 \text{for every }T\ge3,\ 2\le j<T,\ j>\frac{T}{32}.
}
\tag{L-32308.26]

(The closing bracket in the tag is typographical only.) As always, `c_T(T)=0` exactly.

## 9. Significance and new frontier

The successive exact theorems now read

```text
L-32304: every possible SHARP failure lies in j<=T/8;
L-32307: every possible SHARP failure lies in j<=T/16;
L-32308: every possible SHARP failure lies in j<=T/32.
```

The proof has crossed sixteen consecutive quotient cells in which the local Möbius state is strictly negative. The mechanism is a global positive tail reserve overwhelming a negative local state, with only three adverse quotient transitions.

The unresolved region is now

\[
\boxed{j\le T/32.}
\]

This remains RH-bearing. No extrapolation of the geometric pattern to arbitrary depth is claimed.

## 10. Proof boundary

Closed here, subject to independent review:

1. fixed quotient-cell state gates through `K=31`;
2. a uniform tail reserve `>sqrt(T)/8` down to `T/32`;
3. strict same-cell margins on every new cell `16,...,31`;
4. every quotient transition, including all three adverse positive-Möbius transitions;
5. directed finite completion through `T=2047`;
6. SHARP positivity for every `j>T/32`.

Open:

1. the inner thirty-second `j<=T/32`;
2. full SHARP;
3. the fixed low-row zero-safe sign;
4. RH.
