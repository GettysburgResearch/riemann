# L-32406 — Parity-paired averaged Selberg absorption

Claim ID: `L-32406`  
Title: After parity orthogonalization, the complete mixed odd-prime/dyadic Selberg forcing is absorbed by the normalized paired carry energy on every binomial row  
Status: **PROPOSED COMPLETE EXACT THEOREM — FINITE DIRECTED REPLAY + ELEMENTARY COFINAL TAIL**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: PR #263 `L-26202/L-26205`; `L-32404/L-32405`; elementary carry averaging  
Scope: normalized carry-row Hermitian block; no claim that the RH-bearing unweighted physical boundary has been removed

## 1. Parity source

Let

\[
\lambda(n)=\Lambda_{\mathcal E}^{\#}(n)
\]

be the positive generalized-prime sequence of the Euler-filtered inverse from PR #263. Thus

\[
\lambda(p^a)=\log p\qquad(p\text{ odd}),
\]

and

\[
\boxed{
\lambda(2^k)=(2^{k/2}+1)^2\log2.
}
\tag{L-32406.1}
\]

Split it by the parity of the two-adic exponent:

\[
\lambda_0(n)=\mathbf1_{2\mid v_2(n)}\lambda(n),
\qquad
\lambda_1(n)=\mathbf1_{2\nmid v_2(n)}\lambda(n).
\tag{L-32406.2}
\]

Here odd integers have `v_2=0`, so every odd-prime power lies in `lambda_0`.

Let

\[
C=\lambda\log+\lambda*\lambda,
\qquad
C_0(n)=\mathbf1_{2\mid v_2(n)}C(n).
\tag{L-32406.3}
\]

For a binomial row `n=j+(n-j)` put

\[
\chi_{n,q}(j)
=\left\lfloor{n\over q}\right\rfloor
 -\left\lfloor{j\over q}\right\rfloor
 -\left\lfloor{n-j\over q}\right\rfloor
\in\{0,1\}.
\tag{L-32406.4}
\]

Define

\[
P_\epsilon(n,j)=\sum_{q\le n}\lambda_\epsilon(q)\chi_{n,q}(j),
\qquad \epsilon\in\{0,1\},
\tag{L-32406.5}
\]

and

\[
S_0(n,j)=\sum_{q\le n}C_0(q)\chi_{n,q}(j).
\tag{L-32406.6}
\]

The two original parity channels satisfy

\[
P_+=P_0+P_1,
\qquad
P_-=P_0-P_1,
\tag{L-32406.7}
\]

and, because the complete twist is multiplicative,

\[
C_++C_-=2C_0.
\tag{L-32406.8}
\]

Hence

\[
\boxed{
P_+^2+P_-^2=2(P_0^2+P_1^2).
}
\tag{L-32406.9}
\]

The mixed odd-prime/dyadic terms are therefore already present in the exact quantity below; no source block is deleted.

## 2. The averaged theorem

Use the normalized row average

\[
\langle f\rangle_n={1\over n+1}\sum_{j=0}^n f(j).
\tag{L-32406.10}
\]

Then for every integer `n>=2`,

\[
\boxed{
\left\langle P_0(n,\cdot)^2+P_1(n,\cdot)^2\right\rangle_n
\ge
\left\langle S_0(n,\cdot)\right\rangle_n.
}
\tag{L-32406.11}
\]

Equivalently, in the original two-channel normalization,

\[
\boxed{
\left\langle P_+^2+P_-^2\right\rangle_n
\ge
\left\langle C_++C_-\right\rangle_n.
}
\tag{L-32406.12}
\]

Thus the entire parity-retained Selberg forcing — pure odd, pure dyadic, and every mixed odd-prime/even-dyadic convolution term — is absorbed by the complete paired Hermitian carry energy after the split variable is retained through the square and only then averaged.

This is exactly the order required by the reviewed independent-frequency/carry normal orientation.

## 3. Divisor primitives used by the finite replay

For a positive arithmetic sequence `a`,

\[
\sum_{q\le N}a(q)\left\lfloor{N\over q}\right\rfloor
=\sum_{m\le N}(\mathbf1*a)(m).
\tag{L-32406.13}
\]

For the present parity source, write

\[
m=2^v u,\qquad u\text{ odd},\qquad L=\log2.
\]

Put

\[
e_v=\sum_{\substack{1\le k\le v\\k\text{ even}}}(2^{k/2}+1)^2,
\qquad
o_v=\sum_{\substack{1\le k\le v\\k\text{ odd}}}(2^{k/2}+1)^2.
\tag{L-32406.14}
\]

Let

\[
d_k=(2^{k/2}+1)^2,
\]

\[
c_k=k d_k+\sum_{i=1}^{k-1}d_i d_{k-i},
\tag{L-32406.15}
\]

and

\[
D_v=\sum_{\substack{1\le k\le v\\k\text{ even}}}c_k.
\tag{L-32406.16}
\]

Direct divisor summation gives

\[
\boxed{
(\mathbf1*\lambda_0)(m)=\log u+e_vL,
}
\tag{L-32406.17}
\]

\[
\boxed{
(\mathbf1*\lambda_1)(m)=o_vL,
}
\tag{L-32406.18}
\]

and

\[
\boxed{
(\mathbf1*C_0)(m)
=(\log u)^2+2e_vL\log u+D_vL^2.
}
\tag{L-32406.19}
\]

These formulas include the complete mixed convolution. In particular the term `2e_v L log u` is precisely the cumulative odd-prime/even-dyadic channel.

Let `F_0,F_1,G_0` be the cumulative sums of (L-32406.17)--(L-32406.19). Then

\[
P_\epsilon(n,j)=F_\epsilon(n)-F_\epsilon(j)-F_\epsilon(n-j),
\tag{L-32406.20}
\]

\[
S_0(n,j)=G_0(n)-G_0(j)-G_0(n-j).
\tag{L-32406.21}
\]

The directed verifier evaluates the scalar row means from these three one-dimensional prefix tables. It never expands an `O(n^2)` split/source matrix.

## 4. Small rows

The rows `n=2,3,4,5` are elementary. Write

\[
a=\log2,\qquad b=\log3,\qquad c=\log5,\qquad s=\sqrt2.
\]

Their averaged defects in (L-32406.11) are

\[
\Delta_2={a^2(3+2s)^2\over3}>0,
\tag{L-32406.22}
\]

\[
\boxed{\Delta_3=0,}
\tag{L-32406.23}
\]

\[
\Delta_4={2a\over5}\big[(86-6s)a+9b\big]>0,
\tag{L-32406.24}
\]

and

\[
\Delta_5={2a\over3}\big[(23-6s)a+9c\big]>0.
\tag{L-32406.25}
\]

Thus the only equality among these rows is `n=3`.

For `6<=n<30000`, `X-32402` certifies the stronger Jensen-ready scalar inequality

\[
\boxed{
\overline P_0(n)^2+\overline P_1(n)^2
>\overline S_0(n),
}
\tag{L-32406.26}
\]

where bars denote normalized row averages. Jensen then gives (L-32406.11).

The proof object uses rational atanh enclosures after dyadic range reduction for every logarithm and an integer-square enclosure for `sqrt(2)`. No binary floating-point sign decision is used.

## 5. Cofinal lower bound for the paired energy

It remains to prove the theorem without finite replay for all `n>=30000`.

Let

\[
F_n(j)=\log\binom nj
\]

be the ordinary Kummer profile. Since `lambda>=Lambda` coefficientwise and every carry indicator is nonnegative,

\[
P_0(n,j)+P_1(n,j)\ge F_n(j).
\tag{L-32406.27}
\]

Therefore

\[
P_0(n,j)^2+P_1(n,j)^2
\ge{1\over2}F_n(j)^2.
\tag{L-32406.28}
\]

For `j<=n/2`,

\[
\binom nj\ge\binom{2j}j
=\prod_{r=1}^j{j+r\over r}
\ge2^j,
\]

so

\[
F_n(j)\ge jL.
\tag{L-32406.29}
\]

A direct sum of squares, using symmetry, gives for every `n>=4`

\[
\boxed{
{1\over n+1}\sum_{j=0}^nF_n(j)^2
\ge {n^2L^2\over15}.
}
\tag{L-32406.30}
\]

For odd `n=2m+1` the normalized coefficient of `L^2` is

\[
{m\over6(2m+1)}\ge{1\over15}
\qquad(m\ge2),
\]

and for even `n=2m` it is

\[
{2m^2+1\over12m(2m+1)}>{1\over15}.
\]

Hence

\[
\boxed{
\left\langle P_0^2+P_1^2\right\rangle_n
\ge {n^2L^2\over30}.
}
\tag{L-32406.31}
\]

## 6. Elementary upper bound for the complete forcing

Let

\[
\Psi_{\mathcal E}(x)=\sum_{q\le x}\lambda(q).
\]

The elementary central-binomial Chebyshev estimate already used on the live branches gives

\[
\psi(x)\le4x\log2<3x.
\tag{L-32406.32}
\]

The extra dyadic generalized-prime mass is

\[
L\sum_{2^k\le x}\left(2^k+2^{k/2+1}\right).
\]

For `x>=16`,

\[
\sum_{2^k\le x}2^k<2x,
\]

and

\[
2\sum_{2^k\le x}2^{k/2}
<(4+2\sqrt2)\sqrt x<7\sqrt x\le{7\over4}x.
\]

Using `L<3/4` gives an extra mass below `45x/16`. Together with (L-32406.32),

\[
\Psi_{\mathcal E}(x)<6x
\qquad(x\ge16).
\]

The finite cases `2<=x<16` satisfy the same bound directly. Thus

\[
\boxed{\Psi_{\mathcal E}(x)\le6x\qquad(x\ge2).}
\tag{L-32406.33}
\]

Partial summation yields

\[
\sum_{q\le x}{\lambda(q)\over q}
\le6(1+\log x).
\tag{L-32406.34}
\]

Since

\[
C=\lambda\log+\lambda*\lambda,
\]

positivity and (L-32406.33)--(L-32406.34) give

\[
\begin{aligned}
\sum_{q\le n}C(q)
&\le \log n\,\Psi_{\mathcal E}(n)
 +\sum_{ab\le n}\lambda(a)\lambda(b)\\
&\le6n\log n
 +6n\sum_{a\le n}{\lambda(a)\over a}\\
&\le\boxed{36n+42n\log n}.
\end{aligned}
\tag{L-32406.35}
\]

Because `0<=chi<=1` and `C_0<=C`,

\[
\boxed{
\left\langle S_0\right\rangle_n
\le36n+42n\log n.
}
\tag{L-32406.36}
\]

## 7. Tail comparison

It is enough to show

\[
{n^2L^2\over30}
\ge36n+42n\log n,
\]

i.e.

\[
nL^2\ge1080+1260\log n.
\tag{L-32406.37}
\]

The elementary rational logarithm bounds

\[
\log2>{69\over100},
\qquad
\log2<{7\over10},
\qquad
\log3<{11\over10},
\qquad
\log5<{161\over100}
\tag{L-32406.38}
\]

are replayed exactly by `X-32402`. Since

\[
30000=3\cdot2^4\cdot5^4,
\]

these imply

\[
\log30000<{517\over50}=10.34.
\]

At `n=30000`,

\[
nL^2>14283,
\]

while

\[
1080+1260\log n<14108.4.
\]

Moreover

\[
{d\over dn}\left[nL^2-1080-1260\log n\right]
=L^2-{1260\over n}
>{4761\over10000}-{1260\over30000}>0.
\]

Therefore (L-32406.37) holds for every `n>=30000`, completing the proof.

## 8. What this breakthrough closes

The former open phrase

```text
mixed odd-prime/dyadic paired Kummer block
```

is no longer an open local sign theorem at normalized carry-row scope.

The proof deliberately avoids a false stronger statement. The pointwise inequality in `j` is not needed by this consumer. The split variable is retained through the complete square, exactly as required by the normal-Gram orientation, and only then averaged.

Combined with `L-32405`, this gives two independent checks on the dyadic sector:

```text
coefficientwise pure-dyadic absorption       L-32405;
complete averaged mixed-source absorption    L-32406.
```

## 9. Remaining RH-bearing boundary

This theorem does **not** cancel or estimate away the unweighted inverse-zeta source. The positive logarithmic moments still omit the unit/boundary coordinate, and the direct pure-carry window can still cancel the RH pole as recorded on PR #269.

Thus the remaining physical theorem is narrower:

```text
parity-paired independent-frequency source
-> averaged Selberg/carry interior CLOSED here
-> retain the unweighted physical boundary before zeta cancellation
-> route that boundary to a coefficient-one or strict lower-scale recurrence.
```

The mixed local Selberg source is no longer the reason the parity route is open.

## 10. Proof boundary

Closed here:

1. the exact parity decomposition of the generalized-prime/Selberg source;
2. the complete mixed-source normalized carry inequality;
3. an exact directed finite replay through `n=29999`;
4. an elementary uniform tail proof from `n=30000` onward.

Still open:

1. the RH-sensitive unweighted physical boundary recurrence;
2. a global block recurrence consuming that boundary;
3. RH.
