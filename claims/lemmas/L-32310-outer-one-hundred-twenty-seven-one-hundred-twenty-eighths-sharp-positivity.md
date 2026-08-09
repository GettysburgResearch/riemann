# L-32310 — The outer one hundred twenty-seven one hundred twenty-eighths of SHARP are strictly positive

Claim ID: `L-32310`  
Title: Every square-root-hinge average-carry inverse coefficient with `j>T/128` is strictly positive  
Status: **PROPOSED COMPLETE THEOREM — ANALYTIC TAIL + DIRECTED FINITE BASE; INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: `L-32309`; `L-32303/L-32304`; finite multiples-Möbius inversion  
Scope: all endpoints and coefficient indices in the outer one hundred twenty-seven one hundred twenty-eighths; no claim for `j<=T/128` and no RH conclusion

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

and the exact identity

\[
\boxed{
 j c_T(j)
 =(j+2)u_T(j)-j u_T(j+1)
 +\frac{2S_T(j)}{j-1}.
}
\tag{L-32310.1}

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
\tag{L-32310.2}

The new strip uses only the fixed quotient cells `K=64,...,127`.

## 2. Fixed continuum tail through quotient 127

For a quotient cell `K` put

\[
 I_K
 =2A_K\left(\frac1{\sqrt K}-\frac1{\sqrt{K+1}}\right)
 -\frac{M_K}{K(K+1)}.
\tag{L-32310.3}

Use the same exact sum-versus-integral estimate as `L-32309`. The top-half contribution is retained at the safe lower value

\[
 \frac{21}{250}\sqrt T.
\]

`X-32306` evaluates every fixed radical in `K<=127` with directed integer-square intervals and proves

\[
\boxed{
 \frac{21}{250}+\sum_{K=2}^{127}I_K
 >\frac{103}{1000}.
}
\tag{L-32310.4}

The complete discretization-error coefficient in those same cell estimates satisfies

\[
\boxed{
 \sum_{K=2}^{127}E_K<1218.
}
\tag{L-32310.5}

Therefore, if

\[
 J_{128}=\left\lfloor\frac T{128}\right\rfloor+1,
\]

then for `T>=65536`,

\[
\frac{S_T(J_{128})}{\sqrt T}
>\frac{103}{1000}-\frac{1218}{65536}
=\frac{345763}{4096000}
>\boxed{\frac{21}{250}}.
\tag{L-32310.6}

The final strict margin in the last comparison is

\[
 \frac{1699}{4096000}>0.
\]

## 3. The entire new band is locally negative

The same directed fixed-cell proof certifies, for every

\[
64\le K\le127,
\]

that

\[
 A_K<0
 \qquad\text{and}\qquad
 A_K\sqrt K-M_K<0.
\tag{L-32310.7}

Since the scaled state in the complete cell is

\[
 \sqrt T\,u_T(m)=A_K\sqrt{T/m}-M_K
\]

and `A_K<0`, its maximum occurs at the outer cell endpoint `T/m=K`. Hence

\[
\boxed{
 u_T(m)<0
 \quad\text{throughout every complete cell }K=64,...,127.
}
\tag{L-32310.8}

If

\[
\frac{T}{128}<j\le\frac{T}{64},
\]

every summand removed when passing from `S_T(J_128)` to `S_T(j)` lies in this negative band. Removing negative terms only increases the tail, so

\[
\boxed{
 S_T(j)>\frac{21}{250}\sqrt T
 \qquad(T\ge65536,\ T/128<j\le T/64).
}
\tag{L-32310.9}

## 4. One uniform local bound replaces the cell table

Retain

\[
 B_j=\frac{j+2}{\sqrt j}-\frac{j}{\sqrt{j+1}}
 <\frac{5}{2\sqrt j}.
\]

For a same-cell pair in quotient cell `K`,

\[
 (j+2)u_T(j)-ju_T(j+1)
 =A_KB_j-\frac{2M_K}{\sqrt T}.
\]

Since `A_K<0` and `j>T/(K+1)`,

\[
\sqrt T[(j+2)u_T(j)-ju_T(j+1)]
>\frac52A_K\sqrt{K+1}-2M_K.
\tag{L-32310.10}

Rather than retain sixty-four separate constants, `X-32306` certifies the single uniform inequality

\[
\boxed{
 \frac52A_K\sqrt{K+1}-2M_K
 >-\frac{4K}{25}
 \qquad(64\le K\le127).
}
\tag{L-32310.11}

This bound is close to sharp at the worst fixed cell but still leaves a simple rational global margin.

## 5. Same-cell positivity

Because `j-1<T/K`, equation (L-32310.9) gives

\[
\frac{2S_T(j)}{j-1}
>\frac{21K}{125\sqrt T}.
\tag{L-32310.12}

Combining with (L-32310.11),

\[
\begin{aligned}
\sqrt T\,j c_T(j)
&> -\frac{4K}{25}+rac{21K}{125}\\
&=\boxed{\frac{K}{125}}.
\end{aligned}
\tag{L-32310.13}

Thus every same-cell row in the new strip is strictly positive, with a margin increasing linearly in the quotient index.

## 6. Quotient-cell transitions

At a transition from cell `K` to `K-1`, the exact correction is

\[
 \mu(K)\left[
 \frac1{\sqrt T}-\frac1{\sqrt{K(j+1)}}
 \right].
\tag{L-32310.14}

The bracket is positive. Hence `mu(K)<=0` improves the local term.

If `mu(K)=1`, the complete transition loss in (L-32310.1) is, as in `L-32307`--`L-32309`, less than

\[
 \frac1{2\sqrt T}.
\]

Equation (L-32310.13) gives, uniformly for every possible adverse transition,

\[
\sqrt T\,j c_T(j)
>\frac{K}{125}-\frac12
\ge\frac{64}{125}-\frac12
=\boxed{\frac3{250}>0}.
\tag{L-32310.15}

Thus no list of exceptional positive-Möbius transitions is required: the same global inequality pays all of them.

## 7. Cofinal theorem

For `T>=65536`, `L-32309` handles every `j>T/64`. Sections 2--6 handle

\[
\frac{T}{128}<j\le\frac{T}{64}.
\]

Hence

\[
\boxed{
 c_T(j)>0
 \qquad(T\ge65536,\ 2\le j<T,\ j>T/128).
}
\tag{L-32310.16}

## 8. Directed finite base

`X-32306-outer-127-128` uses only exact Möbius integers and directed integer-square inverse-root intervals. It evaluates only the new strip `T/128<j<=T/64`, importing `L-32309` above it.

It certifies every endpoint

\[
3\le T\le65535
\]

and every new-strip coefficient. In total

\[
\boxed{16,777,152}
\]

coefficient rows are checked with no failure.

The same proof object certifies the fixed continuum lower bound (L-32310.4), the error bound (L-32310.5), strict negativity (L-32310.8), and the uniform local inequality (L-32310.11).

Its retained digest is

```text
af9a1a3076f7db5eeb430ed15ecda1ab27d3b4e1350f5902a1146e8843bf7a81
```

Combining the finite replay with (L-32310.16) gives

\[
\boxed{
 c_T(j)>0
 \qquad
 \text{for every }T\ge3,\ 2\le j<T,\ j>\frac{T}{128}.
}
\tag{L-32310.17}

As always, `c_T(T)=0` exactly.

## 9. Significance and exact frontier

The proved progression is now

```text
outer 7/8      L-32304
outer 15/16    L-32307
outer 31/32    L-32308
outer 63/64    L-32309
outer 127/128  L-32310
```

The new proof is simpler than the preceding two layers: one uniform local inequality handles all sixty-four newly entered quotient cells and every adverse transition.

The unresolved region is now

\[
\boxed{j\le T/128.}
\]

`T-32302` identifies the fixed-ratio continuum limit which controls any arbitrary-depth continuation. Therefore this geometric progression is not claimed to be a soft route to infinity; a genuinely uniform all-depth theorem is RH-bearing.

## 10. Proof boundary

Closed here, subject to independent review:

1. fixed quotient data through `K=127`;
2. sharpened continuum tail reserve and directed discretization error;
3. strict negativity of every new quotient cell;
4. one uniform local bound for all new cells;
5. every quotient transition by one universal margin;
6. directed finite new-strip completion through `T=65535`;
7. SHARP positivity for every `j>T/128`.

Open:

1. the inner one hundred twenty-eighth `j<=T/128`;
2. eventual one-sidedness of the continuum scalar `Psi` from `T-32302`;
3. full SHARP;
4. RH.
