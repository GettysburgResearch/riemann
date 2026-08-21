# L-32304 — The outer seven eighths of SHARP are strictly positive

Claim ID: `L-32304`  
Title: Every square-root-hinge average-carry inverse coefficient with `j>T/8` is strictly positive  
Status: **PROPOSED COMPLETE THEOREM — ANALYTIC TAIL + DIRECTED FINITE BASE; INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: PR #329 `L-32303`; finite multiples-Mobius inversion  
Scope: all endpoints and coefficient indices in the outer seven eighths; no claim for `j<=T/8` and no RH conclusion

## 1. Hinge, Mobius state, and the exact local criterion

Fix an integer endpoint `T>=3` and put

\[
 h_T(q)=q^{-1/2}-T^{-1/2},\qquad 1\le q\le T.
\]

Let

\[
 u_T(m)=\sum_{k\le T/m}\mu(k)h_T(mk)
\]

be the finite multiples-Mobius inverse and

\[
 S_T(j)=\sum_{m=j}^{T}u_T(m).
\]

The average-carry inverse coefficient `c_T(j)` of PR #329 satisfies the exact adjoint identity

\[
 c_T(j)=\frac{(j+1)[ju_T(j)-(j-2)u_T(j+1)]+2S_T(j+2)}{j(j-1)}.
\]

Using `S_T(j+1)=S_T(j)-u_T(j)` and `S_T(j+2)=S_T(j)-u_T(j)-u_T(j+1)` gives the equivalent form

\[
 \boxed{
 j c_T(j)
 =(j+2)u_T(j)-j u_T(j+1)+\frac{2S_T(j)}{j-1}.
 }
 \tag{L-32304.1}
\]

Thus it is enough to control one local first-difference term plus one positive tail.

## 2. Quotient-cell normal form

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

Then exactly

\[
 \boxed{
 u_T(m)=\frac{A_K}{\sqrt m}-\frac{M_K}{\sqrt T}.
 }
 \tag{L-32304.2}
\]

For `K<=7` the values are

\[
\begin{array}{c|c|c}
K&A_K&M_K\\ \hline
1&1&1\\
2&1-2^{-1/2}&0\\
3,4&1-2^{-1/2}-3^{-1/2}&-1\\
5&1-2^{-1/2}-3^{-1/2}-5^{-1/2}&-2\\
6&A_5+6^{-1/2}&-1\\
7&A_6-7^{-1/2}&-2.
\end{array}
\tag{L-32304.3}
\]

Only these seven cells occur when `m>T/8`.

## 3. Elementary radical bounds

The following strict rational bounds will be used:

\[
 2^{-1/2}<\frac{177}{250},\qquad
 3^{-1/2}<\frac{289}{500},\qquad
 5^{-1/2}<\frac9{20},\qquad
 6^{-1/2}>\frac{20}{49},
\]

\[
 \sqrt5<\frac94,\qquad \sqrt7<\frac83.
\]

For the narrow `K=7` margin we also use

\[
 2^{-1/2}<\frac{7072}{10000},\quad
 3^{-1/2}<\frac{5774}{10000},\quad
 5^{-1/2}<\frac{4473}{10000},
\]

\[
 6^{-1/2}>\frac{4082}{10000},\quad
 7^{-1/2}<\frac{3780}{10000},\quad
 \sqrt8<\frac{2829}{1000}.
\]

Every assertion follows by squaring positive rationals. `X-32302` replays all of these integer-square gates.

Put

\[
 b_{34}=2^{-1/2}+3^{-1/2}-1,
\]

\[
 b_5=2^{-1/2}+3^{-1/2}+5^{-1/2}-1,
\]

\[
 b_6=b_5-6^{-1/2},\qquad b_7=b_6+7^{-1/2}.
\]

The bounds above give

\[
 b_{34}<\frac{143}{500},\qquad
 b_5<\frac{92}{125}<\frac34,\qquad
 b_6<\frac13,
\tag{L-32304.4}
\]

and

\[
 b_7<\frac{351}{500}.
\tag{L-32304.5}
\]

Moreover

\[
 3^{-1/2}+5^{-1/2}+7^{-1/2}-1-6^{-1/2}<0,
\]

so

\[
 \boxed{b_7<2^{-1/2}.}
 \tag{L-32304.6}
\]

## 4. Positivity of every Mobius state above `T/8`

For `K=1`, `u_T(m)=h_T(m)>=0`. For `K=2`,

\[
 u_T(m)=(1-2^{-1/2})m^{-1/2}>0.
\]

For `K=3,4`,

\[
 u_T(m)=T^{-1/2}-b_{34}m^{-1/2}.
\]

Since `m>T/5`, (L-32304.4) and `sqrt(5)<9/4` give

\[
 u_T(m)>T^{-1/2}\left(1-\frac{143}{500}\frac94\right)>0.
\]

For `K=5`,

\[
 u_T(m)=2T^{-1/2}-b_5m^{-1/2}
 >T^{-1/2}\left(2-\frac34\frac52\right)
 =\frac1{8\sqrt T}>0.
\]

For `K=6`,

\[
 u_T(m)=T^{-1/2}-b_6m^{-1/2}
 >T^{-1/2}\left(1-\frac13\frac83\right)
 =\frac1{9\sqrt T}>0.
\]

For `K=7`, `m>T/8`; by (L-32304.6),

\[
 b_7m^{-1/2}<b_7\sqrt8\,T^{-1/2}<2T^{-1/2},
\]

so again `u_T(m)>0`.

Hence

\[
 \boxed{u_T(m)>0\quad(T/8<m<T),}
 \tag{L-32304.7}
\]

with `u_T(T)=0`.

## 5. A fixed positive tail reserve

Let `L=floor(T/2)` and retain only the top-half `K=1` contribution:

\[
 C_T=\sum_{m=L+1}^{T}\left(m^{-1/2}-T^{-1/2}\right).
\]

For `T>=40`,

\[
 \boxed{C_T>\frac3{40}\sqrt T.}
 \tag{L-32304.8}
\]

Indeed, because the summand is positive and decreasing before its endpoint zero,

\[
 C_T\ge
 \int_{L+1}^{T}\left(x^{-1/2}-T^{-1/2}\right)dx.
\]

For even `T`, the resulting normalized lower bound is

\[
 2\left(1-\sqrt{\frac12+\frac1T}\right)-\frac12+\frac1T,
\]

which is increasing in `T`; at `T=40`, `sqrt(21/40)<29/40`, giving a strict value above `3/40`.

For odd `T`, the normalized lower bound is

\[
 2\left(1-\sqrt{\frac12+\frac1{2T}}\right)-\frac12+\frac1{2T},
\]

also increasing; at `T=41`, `sqrt(21/41)<359/500`, leaving the exact margin `49/41000` above `3/40`.

Since every intermediate `K<=7` state is positive by Section 4,

\[
 \boxed{S_T(j)>C_T>\frac3{40}\sqrt T
 \qquad(T>=40,\ j>T/8).}
 \tag{L-32304.9}
\]

## 6. The universal local factor

For every integer `j>=1`, define

\[
 B_j=\frac{j+2}{\sqrt j}-\frac{j}{\sqrt{j+1}}.
\]

Then

\[
 \boxed{B_j<\frac5{2\sqrt j}.}
 \tag{L-32304.10}
\]

Indeed, after multiplying by `sqrt(j)`, this is equivalent to

\[
 j\sqrt{\frac{j}{j+1}}>j-\frac12.
\]

Squaring is legitimate, and after multiplication by `j+1` the difference is `(3j-1)/4>0`.

If `j` and `j+1` remain in the same quotient cell with

\[
 u_T(m)=\frac{C}{\sqrt T}-\frac{b}{\sqrt m},
\]

then the local term in (L-32304.1) is

\[
 (j+2)u_T(j)-ju_T(j+1)
 =\frac{2C}{\sqrt T}-bB_j.
\tag{L-32304.11}
\]

## 7. Cells `K=1,2,3,4`

For `K=1,2`, the sequence `u_T(m)` decreases, so the local term is strictly positive.

For `K=3,4`, use (L-32304.10), `j>T/5`, (L-32304.4), and `sqrt5<9/4`:

\[
 (j+2)u_T(j)-ju_T(j+1)
 >\frac1{\sqrt T}
 \left[2-\frac52\frac{143}{500}\frac94\right]
 =\frac{313}{800\sqrt T}>0.
\tag{L-32304.12}
\]

Thus no tail reserve is needed in the first four cells.

## 8. Cells `K=5,6,7`

For a same-cell pair, (L-32304.9)--(L-32304.11) and `j-1<T/K` give

\[
 \frac{2S_T(j)}{j-1}>\frac{3K}{20\sqrt T}.
 \tag{L-32304.13}
\]

### `K=5`

Using `b_5<3/4` and `sqrt6<5/2`, the complete bracket in (L-32304.1) is larger than

\[
 \frac1{\sqrt T}
 \left[4+\frac{15}{20}
 -\frac52\frac34\frac52\right]
 =\boxed{\frac1{16\sqrt T}}>0.
\tag{L-32304.14}
\]

### `K=6`

Using `b_6<1/3` and `sqrt7<8/3`, the same-cell margin is

\[
 \frac1{\sqrt T}
 \left[2+\frac{18}{20}
 -\frac52\frac13\frac83\right]
 =\boxed{\frac{61}{90\sqrt T}}>0.
\tag{L-32304.15}
\]

### `K=7`

Using `b_7<351/500` and `sqrt8<2829/1000`, the same-cell margin is

\[
 \frac1{\sqrt T}
 \left[4+\frac{21}{20}
 -\frac52\frac{351}{500}\frac{2829}{1000}\right]
 =\boxed{\frac{17021}{200000\sqrt T}}>0.
\tag{L-32304.16}
\]

## 9. Quotient-cell transitions

At a transition from cell `K` to `K-1`, compare the actual `u_T(j+1)` with the value obtained by formally keeping the `K`th Mobius term. Their difference is

\[
 \mu(K)\left[\frac1{\sqrt{K(j+1)}}-\frac1{\sqrt T}\right].
 \tag{L-32304.17}
\]

Because `T<K(j+1)`, the square bracket is negative. Hence transitions with `mu(K)<=0` only **increase** the local margin. This covers `K=2,3,4,5,7`.

The sole adverse transition is `K=6`, where `mu(6)=1`. Write `T=6j+r`, `0<=r<=5`. By the mean-value theorem,

\[
 0<\frac1{\sqrt T}-\frac1{\sqrt{6(j+1)}}
 \le\frac{6}{2T^{3/2}}.
\]

Since `j<T/6`, multiplying by `j` costs less than

\[
 \frac1{2\sqrt T}.
\]

Subtracting this from (L-32304.15) still leaves

\[
 \boxed{
 \frac{61}{90\sqrt T}-\frac1{2\sqrt T}
 =\frac{8}{45\sqrt T}>0.
 }
 \tag{L-32304.18}
\]

Thus every quotient transition is also strictly safe.

## 10. Finite base and theorem

The analytic argument above covers every `T>=40`. `X-32302` uses the same directed integer-square inverse-root enclosures as `X-32301` and certifies every remaining endpoint

\[
 3\le T<40
\]

and every coefficient index `j>T/8`. It checks 655 coefficients with no failure.

Therefore

\[
 \boxed{
 c_T(j)>0
 \qquad
 \text{for every }T\ge3,\ 2\le j<T,\ j>\frac T8.
 }
 \tag{L-32304.19}
\]

The endpoint coefficient `c_T(T)=0` as before.

## 11. Significance and exact frontier

PR #332 had already closed the entire top half `j>T/2`. The present theorem pushes the unconditional square-root-hinge positivity boundary through quotient cells `K=2,3,4,5,6,7`:

\[
 \boxed{
 \text{all possible SHARP failure is confined to }j\le T/8.
 }
\]

This is source-specific. It does not contradict `R-32302`: generic third-Abel targets still have negative average-carry inverse coefficients.

The remaining inner eighth contains quotient indices `K>=8`; already at `K=8` the Mobius state itself can change sign, so the positive-tail argument above reaches its natural first arithmetic wall.

## 12. Proof boundary

Closed here, subject to independent review:

- exact quotient-cell Mobius formulas through `K=7`;
- positivity of every corresponding Mobius state;
- a uniform positive top-tail reserve;
- strict local-plus-tail margins in every same cell;
- every cell transition, including the sole adverse `mu(6)=+1` transition;
- directed finite completion below `T=40`;
- SHARP positivity for every `j>T/8`.

Open:

- the inner eighth `j<=T/8`;
- the zero-safe low-row sign of PR #326;
- full SHARP;
- RH.
