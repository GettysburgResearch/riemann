# L-32311 — The outer two hundred fifty-five two hundred fifty-sixths of SHARP are strictly positive

Claim ID: `L-32311`  
Title: Every square-root-hinge average-carry inverse coefficient with `j>T/256` is strictly positive  
Status: **PROPOSED COMPLETE THEOREM — ANALYTIC TAIL + DIRECTED FINITE TAIL GATE; INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: `L-32310`; `L-32303/L-32304`; finite multiples-Möbius inversion  
Scope: all endpoints and coefficient indices in the outer two hundred fifty-five two hundred fifty-sixths; no claim for `j<=T/256` and no RH conclusion

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

and

\[
\boxed{
jc_T(j)
=(j+2)u_T(j)-ju_T(j+1)+\frac{2S_T(j)}{j-1}.
}
\tag{L-32311.1}
\]

On quotient cell

\[
K=\left\lfloor\frac{T}{m}\right\rfloor,
\]

one has exactly

\[
\boxed{
u_T(m)=\frac{A_K}{\sqrt m}-\frac{M_K}{\sqrt T},
\qquad
A_K=\sum_{k\le K}\frac{\mu(k)}{\sqrt k},
\quad
M_K=\sum_{k\le K}\mu(k).
}
\tag{L-32311.2}

The new strip uses only `K=128,...,255`.

## 2. Tail reserve through quotient 255

For each fixed quotient cell define, as in `L-32309/L-32310`,

\[
I_K
=2A_K\left(\frac1{\sqrt K}-\frac1{\sqrt{K+1}}\right)
-\frac{M_K}{K(K+1)},
\tag{L-32311.3}
\]

and the sum-integral error coefficient

\[
E_2=|A_2|\sqrt3+|M_2|,
\qquad
E_K=|A_K|\sqrt{2(K+1)}+|M_K|\quad(K\ge3).
\tag{L-32311.4}
\]

For a complete quotient cell the exact sum-versus-integral estimate gives

\[
\frac1{\sqrt T}\sum_{m\in\text{cell }K}u_T(m)
\ge I_K-\frac{E_K}{T}.
\tag{L-32311.5}
\]

The directed fixed-radical checker `X-32307` proves

\[
\boxed{
\frac{21}{250}+\sum_{K=2}^{255}I_K>\frac3{40},
}
\tag{L-32311.6}
\]

and

\[
\boxed{
\sum_{K=2}^{255}E_K<3162.
}
\tag{L-32311.7}
\]

Let

\[
J_{256}=\left\lfloor\frac T{256}\right\rfloor+1.
\]

For `T>=262144`, (L-32311.5)--(L-32311.7) give

\[
\begin{aligned}
\frac{S_T(J_{256})}{\sqrt T}
&>\frac3{40}-\frac{3162}{262144}\\
&=\frac1{16}+\frac{287}{655360}\\
&>\boxed{\frac1{16}}.
\end{aligned}
\tag{L-32311.8}
\]

For the finite interval

\[
256\le T\le262143,
\]

`X-32307` evaluates exactly the one required tail per endpoint by quotient-cell grouping and directed inverse-square-root prefix sums. All

\[
\boxed{261888}
\]

endpoint gates satisfy

\[
\boxed{
S_T(J_{256})>\frac1{16}\sqrt T.
}
\tag{L-32311.9}
\]

The smallest directed margin over the finite tail gate occurs at `T=511` and remains strictly positive.

For `T<256`, every nontrivial integer row `j>=2` already lies in `j>T/128`, so `L-32310` covers it.

## 3. The new cells are all locally negative

The fixed-cell checker proves for every

\[
128\le K\le255
\]

that

\[
\boxed{
A_K<0,
\qquad
A_K\sqrt K-M_K<0.
}
\tag{L-32311.10}
\]

Hence

\[
\boxed{
u_T(m)<0}
\tag{L-32311.11}
\]

through every complete new quotient cell.

If

\[
\frac{T}{256}<j\le\frac{T}{128},
\]

every term removed when passing from `S_T(J_256)` to `S_T(j)` is negative, so the tail only increases. Therefore the finite and analytic gates combine to give

\[
\boxed{
S_T(j)>\frac1{16}\sqrt T
\qquad
\left(\frac{T}{256}<j\le\frac{T}{128}\right).
}
\tag{L-32311.12}
\]

## 4. Same-cell local gate

Retain

\[
B_j=\frac{j+2}{\sqrt j}-\frac{j}{\sqrt{j+1}}
<\frac{5}{2\sqrt j}.
\]

For a same-cell pair,

\[
(j+2)u_T(j)-ju_T(j+1)
=A_KB_j-\frac{2M_K}{\sqrt T},
\]

and since `A_K<0` and `j>T/(K+1)`,

\[
\sqrt T[(j+2)u_T(j)-ju_T(j+1)]
> L_K,
\qquad
L_K:=\frac52A_K\sqrt{K+1}-2M_K.
\tag{L-32311.13}
\]

Equation (L-32311.12), together with `j-1<T/K`, gives

\[
\frac{2S_T(j)}{j-1}>rac{K}{8\sqrt T}.
\tag{L-32311.14}
\]

The directed fixed-cell proof checks directly that

\[
\boxed{
L_K+\frac K8>0
\qquad(128\le K\le255).
}
\tag{L-32311.15}
\]

Thus every same-cell row in the new strip is strictly positive. The smallest directed lower margin occurs at

\[
\boxed{K=139}
\]

and is approximately `0.0136568699845/sqrt(T)` for orientation only; the proof uses the exact directed integer certificate.

## 5. Quotient transitions

At a transition from cell `K` to `K-1`, the exact correction is

\[
\mu(K)\left[
\frac1{\sqrt T}-\frac1{\sqrt{K(j+1)}}
\right].
\tag{L-32311.16}
\]

If `mu(K)<=0`, this improves the local term. If `mu(K)=1`, the complete adverse loss is less than `1/(2sqrt(T))`.

The same fixed-cell checker proves, for every positive-Möbius transition in `128<=K<=255`,

\[
\boxed{
L_K+\frac K8-\frac12>0.
}
\tag{L-32311.17}
\]

The smallest adverse-transition margin occurs at

\[
\boxed{K=141}
\]

and is approximately `0.0919963969070/sqrt(T)` for orientation only. Hence every quotient transition is safe.

## 6. The outer 255/256 theorem

`L-32310` handles every `j>T/128`. Sections 2--5 handle

\[
\frac{T}{256}<j\le\frac{T}{128}.
\]

Therefore

\[
\boxed{
 c_T(j)>0
 \qquad
 \text{for every }T\ge3,\ 2\le j<T,\ j>\frac{T}{256}.
}
\tag{L-32311.18}
\]

As always, `c_T(T)=0` exactly.

## 7. Exact replay

`experiments/X-32307-outer-two-hundred-fifty-five-two-hundred-fifty-sixths/verify.py` uses only the Python standard library, exact Möbius integers, and directed integer-square intervals.

It certifies:

1. the fixed continuum tail gate (L-32311.6);
2. the complete error bound (L-32311.7);
3. all 261,888 finite endpoint tail gates in (L-32311.9);
4. strict negativity of every new cell `128,...,255`;
5. every same-cell gate (L-32311.15);
6. every adverse-transition gate (L-32311.17).

Retained result digest:

```text
ac03ded24611dfcb9cca0af6a647cd261b2434406f49b896d16eb27aabeba485
```

The replay proves only the finite and fixed-radical statements above. It does not certify the inner `1/256` or RH.

## 8. Significance and exact frontier

The exact progression is now

```text
outer 7/8       L-32304
outer 15/16     L-32307
outer 31/32     L-32308
outer 63/64     L-32309
outer 127/128   L-32310
outer 255/256   L-32311
```

The quotient-cell arithmetic is no longer the visible obstacle. The new band is controlled by a single tail threshold and fixed local inequalities, while the continuum theorem `T-32302` proves that taking the depth to infinity exposes the zero-safe reciprocal-zeta scalar `Psi`.

The unresolved region is now

\[
\boxed{j\le T/256.}
\]

No arbitrary-depth extrapolation is claimed.

## 9. Proof boundary

Closed here, subject to independent review:

- fixed quotient data through `K=255`;
- a uniform tail reserve `>sqrt(T)/16` down to `T/256`;
- strict local negativity of all cells `128,...,255`;
- every same-cell and quotient-transition margin;
- directed finite tail completion through `T=262143`;
- SHARP positivity for every `j>T/256`.

Open:

- the inner one two-hundred-fifty-sixth `j<=T/256`;
- eventual one-sidedness of the continuum scalar `Psi`;
- full SHARP;
- RH.
