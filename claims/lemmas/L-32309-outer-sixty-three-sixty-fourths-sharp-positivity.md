# L-32309 — The outer sixty-three sixty-fourths of SHARP are strictly positive

Claim ID: `L-32309`  
Title: Every square-root-hinge average-carry inverse coefficient with `j>T/64` is strictly positive  
Status: **PROPOSED COMPLETE THEOREM — ANALYTIC TAIL + DIRECTED FINITE BASE; INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: `L-32308`; `L-32303/L-32304`; finite multiples-Möbius inversion  
Scope: all endpoints and coefficient indices in the outer sixty-three sixty-fourths; no claim for `j<=T/64` and no RH conclusion

## 1. Exact criterion

Retain

\[
 h_T(q)=q^{-1/2}-T^{-1/2},
\]

\[
 u_T(m)=\sum_{k\le T/m}\mu(k)h_T(mk),
 \qquad
 S_T(j)=\sum_{m=j}^{T}u_T(m),
\]

and the exact SHARP identity

\[
\boxed{
 j c_T(j)
 =(j+2)u_T(j)-j u_T(j+1)
 +\frac{2S_T(j)}{j-1}.
}
\tag{L-32309.1}

If

\[
 K=\left\lfloor\frac{T}{m}\right\rfloor,
\]

then

\[
\boxed{
 u_T(m)=\frac{A_K}{\sqrt m}-\frac{M_K}{\sqrt T},
 \qquad
 A_K=\sum_{k\le K}\frac{\mu(k)}{\sqrt k},
 \quad
 M_K=\sum_{k\le K}\mu(k).
}
\tag{L-32309.2}

The new strip uses only the fixed quotient cells `K=32,...,63`.

## 2. A sharper fixed tail estimate

The minimum-per-cell estimate of `L-32308` is deliberately too crude for another doubling. Here we retain the complete inverse-square-root sum in each quotient cell.

For

\[
 a_K=\left\lfloor\frac{T}{K+1}\right\rfloor+1,
 \qquad
 b_K=\left\lfloor\frac TK\right\rfloor,
\]

put

\[
 \Sigma_K=\sum_{m=a_K}^{b_K}m^{-1/2},
 \qquad
 N_K=b_K-a_K+1.
\]

Then the complete normalized contribution of cell `K` is

\[
\frac1{\sqrt T}\sum_{m=a_K}^{b_K}u_T(m)
=A_K\frac{\Sigma_K}{\sqrt T}-M_K\frac{N_K}{T}.
\tag{L-32309.3}

Let

\[
 I_K
 =2A_K\left(\frac1{\sqrt K}-\frac1{\sqrt{K+1}}\right)
 -\frac{M_K}{K(K+1)}.
\tag{L-32309.4}

### Sum-integral error

For decreasing `x^-1/2`,

\[
 \int_{a_K}^{b_K+1}x^{-1/2}dx
 \le\Sigma_K
 \le\int_{a_K-1}^{b_K}x^{-1/2}dx.
\tag{L-32309.5}

For `K=2`, the fixed state has `A_2>0`, and therefore

\[
\frac{\Sigma_2}{\sqrt T}
\ge
2\left(\frac1{\sqrt2}-\frac1{\sqrt3}\right)
-rac{\sqrt3}{T}.
\tag{L-32309.6}

For every `K=3,...,63`, the directed fixed-cell calculation gives `A_K<0`. If `T>=16384`, then `T/(K+1)>=256>2`, and (L-32309.5) gives

\[
\frac{\Sigma_K}{\sqrt T}
\le
2\left(\frac1{\sqrt K}-\frac1{\sqrt{K+1}}\right)
+rac{\sqrt{2(K+1)}}{T}.
\tag{L-32309.7}

Also

\[
\left|\frac{N_K}{T}-\frac1{K(K+1)}\right|<\frac1T.
\tag{L-32309.8}

Consequently every fixed cell satisfies the lower bound

\[
\frac1{\sqrt T}\sum_{m=a_K}^{b_K}u_T(m)
\ge
I_K-rac{E_K}{T},
\tag{L-32309.9}

where

\[
E_2=|A_2|\sqrt3+|M_2|,
\]

and for `K>=3`

\[
E_K=|A_K|\sqrt{2(K+1)}+|M_K|.
\tag{L-32309.10}

## 3. Tail reserve down to `T/64`

The top-half calculation of `L-32304` can be sharpened slightly at large endpoint. Its normalized integral lower bound is increasing in `T`; at the even endpoint `T=256`,

\[
2\left(1-\sqrt{\frac12+\frac1{256}}\right)-\frac12+\frac1{256}
>\frac{21}{250}.
\tag{L-32309.11}

Indeed this is equivalent to

\[
\sqrt{129}<\frac{45437}{4000},
\]

which follows by squaring. For odd `T>=257`, the same expression equals the even formula at endpoint `2T` and is larger. Thus

\[
\boxed{
 C_T>\frac{21}{250}\sqrt T
 \qquad(T\ge256).
}
\tag{L-32309.12}

Now put

\[
 J_{64}=\left\lfloor\frac T{64}\right\rfloor+1.
\]

Combining (L-32309.9) over `K=2,...,63` with (L-32309.12) gives

\[
\frac{S_T(J_{64})}{\sqrt T}
>
\frac{21}{250}
+\sum_{K=2}^{63}I_K
-rac1T\sum_{K=2}^{63}E_K.
\tag{L-32309.13]

(The closing bracket in the tag is typographical only.)

`X-32305` evaluates the two fixed radical sums with directed rational square-root intervals and proves

\[
\boxed{
\frac{21}{250}+\sum_{K=2}^{63}I_K>\frac{69}{500},
}
\tag{L-32309.14

and

\[
\boxed{
\sum_{K=2}^{63}E_K<438.
}
\tag{L-32309.15

Therefore for `T>=16384`,

\[
\frac{S_T(J_{64})}{\sqrt T}
>
\frac{69}{500}-\frac{438}{16384}
=
\frac{11}{100}+rac{1297}{1024000}
>
\boxed{\frac{11}{100}}.
\tag{L-32309.16}

## 4. Every new cell is locally negative

The same directed fixed-cell calculation certifies

\[
\boxed{
 A_K<0,
 \qquad
 A_K\sqrt K-M_K<0
 \qquad(K=32,...,63).
}
\tag{L-32309.17

Hence

\[
 u_T(m)<0
\]

through every complete new quotient cell.

If

\[
\frac{T}{64}<j\le\frac{T}{32},
\]

then every term omitted when passing from `S_T(J_64)` to `S_T(j)` lies in cells `32,...,63` and is negative. Thus

\[
\boxed{
 S_T(j)>\frac{11}{100}\sqrt T
 \qquad(T\ge16384,\ T/64<j\le T/32).
}
\tag{L-32309.18

## 5. Local term in cells thirty-two through sixty-three

Retain

\[
 B_j=\frac{j+2}{\sqrt j}-\frac{j}{\sqrt{j+1}}
 <\frac{5}{2\sqrt j}.
\]

For a same-cell pair in quotient cell `K`,

\[
 (j+2)u_T(j)-j u_T(j+1)
 =A_KB_j-\frac{2M_K}{\sqrt T}.
\]

Since `A_K<0` and `j>T/(K+1)`,

\[
\sqrt T[(j+2)u_T(j)-j u_T(j+1)]
>rac52A_K\sqrt{K+1}-2M_K.
\tag{L-32309.19

`X-32305` certifies the following simple rational lower bounds `C_K` for the right side:

```text
K : C_K
32 -7.0    33 -6.7    34 -6.3    35 -5.9
36 -6.0    37 -6.7    38 -6.3    39 -5.8
40 -5.9    41 -6.5    42 -7.2    43 -7.8
44 -8.0    45 -8.1    46 -7.7    47 -8.4
48 -8.5    49 -8.7    50 -8.8    51 -8.5
52 -8.6    53 -9.2    54 -9.4    55 -9.0
56 -9.1    57 -8.7    58 -8.2    59 -8.8
60 -8.9    61 -9.5    62 -9.1    63 -9.2
```

All entries are terminating rationals with directed radical certificates.

From (L-32309.18) and `j-1<T/K`,

\[
\frac{2S_T(j)}{j-1}
>rac{11K}{50\sqrt T}.
\tag{L-32309.20

Adding the local bounds yields the strict same-cell margins

```text
K : sqrt(T) j c_T(j) lower margin
32  1/25      33 14/25      34 59/50      35 9/5
36 48/25      37 36/25      38 103/50     39 139/50
40 29/10      41 63/25      42 51/25      43 83/50
44 42/25      45 9/5        46 121/50     47 97/50
48 103/50     49 52/25      50 11/5       51 68/25
52 71/25      53 123/50     54 62/25      55 31/10
56 161/50     57 96/25      58 114/25     59 209/50
60 43/10      61 98/25      62 227/50     63 233/50.
```

Thus every same-cell row in the new strip is strictly positive.

## 6. Quotient transitions

At a transition from quotient cell `K` to `K-1`, the exact correction is the one from `L-32307`:

\[
\mu(K)\left[
\frac1{\sqrt T}-\frac1{\sqrt{K(j+1)}}
\right].
\]

Transitions with `mu(K)<=0` improve the local term. The adverse positive-Möbius transitions in `32<=K<=63` are

\[
\boxed{K=33,34,35,38,39,46,51,55,57,58,62.}
\tag{L-32309.21

Their complete loss is less than `1/(2sqrt(T))`. After subtracting that loss from the same-cell margins, the smallest remaining margin is at `K=33`:

\[
\boxed{
\frac{14}{25\sqrt T}-\frac1{2\sqrt T}
=\frac{3}{50\sqrt T}>0.
}
\tag{L-32309.22

All other adverse transitions have larger margin. Every quotient transition is therefore safe.

## 7. Cofinal theorem

For `T>=16384`, `L-32308` handles every `j>T/32`. Sections 3--6 handle

\[
\frac{T}{64}<j\le\frac{T}{32}.
\]

Hence

\[
\boxed{
 c_T(j)>0
 \qquad(T\ge16384,\ 2\le j<T,\ j>T/64).
}
\tag{L-32309.23

## 8. Directed finite base

`X-32305-outer-sixty-three-sixty-fourths` uses exact Möbius integers and directed integer-square inverse-root intervals. Because the theorem only adds the new strip `T/64<j<=T/32`, the finite replay evaluates that strip directly and imports `L-32308` above it.

It checks every endpoint

\[
3\le T\le16383
\]

and every new-strip coefficient: in total

\[
\boxed{2,097,120}
\]

rows, with no failure.

It also independently certifies:

- the fixed continuum tail lower bound (L-32309.14);
- the total discretization error bound (L-32309.15);
- strict negativity of every new quotient cell;
- every local rational bound and same-cell margin;
- every adverse positive-Möbius transition.

The retained proof digest is

```text
ed10807e02062094914b13b8aec848da6305b06bcde50ef6e98360d50ec73c98
```

Combining the finite replay, `L-32308`, and (L-32309.23) proves

\[
\boxed{
 c_T(j)>0
 \qquad
 \text{for every }T\ge3,\ 2\le j<T,\ j>\frac{T}{64}.
}
\tag{L-32309.24

As always, `c_T(T)=0` exactly.

## 9. Significance and frontier

The exact unconditional progression is now

```text
outer 7/8    L-32304
outer 15/16  L-32307
outer 31/32  L-32308
outer 63/64  L-32309
```

The proof has crossed fifty-six consecutive quotient cells after the first local Möbius sign failure. The mechanism remains the same: a positive global tail reserve overcomes locally negative Möbius states and finitely many adverse cell transitions.

The unresolved region is now

\[
\boxed{j\le T/64.}
\]

This region remains RH-bearing. No claim of a uniform all-depth tail theorem is made.

## 10. Proof boundary

Closed here, subject to independent review:

1. fixed quotient data through `K=63`;
2. sum-integral tail control strong enough to retain `11sqrt(T)/100` down to `T/64`;
3. strict local negativity of every new cell `32,...,63`;
4. strict same-cell positivity after tail compensation;
5. every adverse transition;
6. directed new-strip completion through `T=16383`;
7. SHARP positivity for every `j>T/64`.

Open:

1. the inner sixty-fourth `j<=T/64`;
2. a uniform arbitrary-depth version of the tail compensation mechanism;
3. full SHARP;
4. RH.
