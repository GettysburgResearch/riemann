# L-90028 — The positive factor-four block is stochastically dominated by the exact capped-Gamma target

Claim ID: `L-90028` (provisional range; branch-qualified)  
Title: The radix-four detail target is a probability law `H`; the positive endpoint block law `Y` satisfies `Y <=_st H`, so two block atoms admit a lossless state-dependent monotone transport to the complete continuum target  
Status: **PROPOSED COMPLETE EXACT STOCHASTIC-ORDER / TRANSPORT THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Date: 2026-08-10  
Depends on: `L-90025/L-90026`; the endpoint law of PR #353 `L-90022`; elementary trapezoidal bounds  
Scope: closes the continuum state-dependent radix-four transport; no finite arithmetic lift and no RH conclusion

## 1. The capped-Gamma target law

Put

\[
 L=\log4.
\]

Define a nonnegative density

\[
\boxed{
 f_H(t)={1\over2}\min(t,L)e^{-t/2},
 \qquad t\ge0.
}
\tag{L-90028.1}
\]

It has total mass one. Its Laplace transform is

\[
\boxed{
 \phi_H(s)
 ={2-4^{-s}\over(1+2s)^2}.
}
\tag{L-90028.2}
\]

Equivalently, if

\[
 G\sim\operatorname{Gamma}(2,1/2),
 \qquad
 f_G(t)={t\over4}e^{-t/2},
\]

then, with causal zero extension,

\[
\boxed{
 f_H(t)=2f_G(t)-f_G(t-L).
}
\tag{L-90028.3}
\]

Thus `H` is the positive factor-four detail of the sharp Gamma target. Its survival function is

\[
\boxed{
 \overline F_H(t)=
 \begin{cases}
 (t+2)e^{-t/2}-1,&0\le t<L,\\
 Le^{-t/2},&t\ge L.
 \end{cases}}
\tag{L-90028.4}
\]

The critically normalized radix-four column target is

\[
 \ell(t)=t-(t-L)_+=\min(t,L).
\]

Hence

\[
\boxed{
 e^{-t/2}\ell(t)=2f_H(t).
}
\tag{L-90028.5}
\]

The complete continuum detail target is exactly two units of the law `H`.

## 2. Exact tail of the endpoint atom

Let `V` be the critical endpoint atom of PR #353. Its density is

\[
 f_V(t)={1\over2}e^{-t/2}\varrho(t).
\]

For

\[
 x=e^t,\qquad n=\lfloor x\rfloor,
\]

`L-90025` gives

\[
 f_V(t)=ne^{-t}-{S_n\over2}e^{-t/2}.
\tag{L-90028.6}
\]

Integration on one logarithmic cell, followed by telescoping at the knots, yields

\[
\boxed{
 \overline F_V(t)
 =1+{n\over x}-{S_n\over\sqrt x}.
}
\tag{L-90028.7}
\]

Indeed the right side differentiates to `-f_V` on every cell, tends to zero at infinity by the square-root-sum asymptotic, and has value one at zero.

## 3. Exact tail of the positive block law

`L-90026` proves

\[
 f_Y(t)=2f_V(t)-f_V(t-L).
\]

Therefore, with `overline F_V(s)=1` for `s<0`,

\[
\boxed{
 \overline F_Y(t)
 =2\overline F_V(t)-\overline F_V(t-L).
}
\tag{L-90028.8}

For `0<=t<L`, this is

\[
\boxed{
 \overline F_Y(t)
 =1+{2n\over x}-{2S_n\over\sqrt x}.
}
\tag{L-90028.9}

For `t>=L`, put

\[
 m=\left\lfloor{x\over4}\right\rfloor.
\]

Then

\[
\boxed{
 \overline F_Y(t)
 =1+{2n-4m\over x}
  -{2(S_n-S_m)\over\sqrt x}.
}
\tag{L-90028.10}

## 4. The first factor-four block

We prove

\[
\boxed{
 \overline F_Y(t)<\overline F_H(t)
 \qquad(t>0).
}
\tag{L-90028.11}

### 4.1 The first block `1<=x<4`

Here `n` is one of `1,2,3`. Multiplying the desired inequality by `sqrt(x)` gives

\[
 F_n(x):=\log x+2-2\sqrt x-{2n\over\sqrt x}+2S_n\ge0.
\tag{L-90028.12}

On `n<=x<n+1`,

\[
 F_n'(x)={n+\sqrt x-x\over x^{3/2}}>0,
\]

because `x-n<1<=sqrt(x)`. It is therefore enough to inspect the three left endpoints.

For `n=1`, `F_1(1)=0`. For `n=2`,

\[
 F_2(2)=\log2+4-3\sqrt2>{1\over6}>0
\]

using `log2>2/3` and `sqrt2<3/2`. For `n=3`,

\[
 F_3(3)=\log3+4+\sqrt2+{2\over\sqrt3}-4\sqrt3>0
\]

from the elementary bounds

\[
 \log3>1,\quad \sqrt2>{7\over5},\quad
 \sqrt3<{7\over4}.
\]

Thus (L-90028.11) holds on the first factor-four block, strictly away from zero.

### 4.2 All later blocks

Let `x>=4` and write

\[
 n=4m+r,\qquad r\in\{0,1,2,3\}.
\]

The trapezoidal inequality for the convex function `u^{-1/2}` gives

\[
\boxed{
 S_n-S_m
 \ge2(\sqrt n-\sqrt m)
 -{1\over2\sqrt m}+{1\over2\sqrt n}.
}
\tag{L-90028.13}

The function

\[
 g(x)=\sqrt x+{2n-4m\over\sqrt x}
\]

is maximized on `[n,n+1]` at `x=n+1` when `r=0`, and at `x=n` when `r>=1`. Combining this with (L-90028.13), the normalized tail margin

\[
 \sqrt x[\overline F_H(t)-\overline F_Y(t)]
\]

is bounded below by the following four quantities.

For `r=0`,

\[
 M_0=L+4\sqrt m-{1\over2\sqrt m}
 -{8m+1\over\sqrt{4m+1}}.
\]

The exact identity

\[
 {8m+1\over\sqrt{4m+1}}-4\sqrt m
 ={1\over
 \sqrt{4m+1}[(8m+1)+4\sqrt{m(4m+1)}]}
 <{1\over9\sqrt5}
\]

gives

\[
 M_0>{4\over3}-{1\over2}-{1\over18}={7\over9}>0.
\]

For `r=1`,

\[
 M_1=L+2\sqrt{4m+1}-4\sqrt m-{1\over\sqrt m}
 >L-1>{1\over3}.
\]

For `r=2` and `m>=2`,

\[
 M_2>L-{1\over\sqrt m}-{1\over\sqrt{4m+2}}
 >{4\over3}-{5\over7}-{1\over3}={2\over7}.
\]

At `m=1`,

\[
 M_2>{4\over3}+{24\over5}-5-{5\over12}
 ={43\over60}>0.
\]

For `r=3` and `m>=2`,

\[
 M_3>L-{1\over\sqrt m}-{2\over\sqrt{4m+3}}
 >{4\over3}-{5\over7}-{20\over33}={1\over77}.
\]

At `m=1`,

\[
 M_3>{4\over3}+{26\over5}-5-{10\over13}
 ={149\over195}>0.
\]

This proves (L-90028.11) globally.

## 5. Monotone state-dependent transport

Equation (L-90028.11) is exactly

\[
\boxed{Y\le_{\rm st}H.}
\tag{L-90028.14}

By the one-dimensional quantile characterization, there exists a coupling

\[
\boxed{
 H=Y+D,
 \qquad D\ge0\quad\text{almost surely},
}
\tag{L-90028.15}

where the delay `D` may depend on the state `Y`.

This is stronger than the centered convex-order theorem of `L-90026`: no centering and no negative movement are required.

Because the complete detail target is `2 Law(H)`, two units of the positive block atom can be transported state-dependently, only toward larger logarithmic scale, to saturate the target exactly. In measure form there is a positive kernel `K(y,dh)` supported on `h>=y` such that

\[
\boxed{
 2f_H(h)dh
 =2\int K(y,dh)f_Y(y)dy.
}
\tag{L-90028.16}

Thus the continuum radix-four endpoint-packing problem has a lossless positive state-dependent solution.

## 6. Why this is not yet the finite RH proof

An independent scale convolution would require a positive deconvolution factor and remains reciprocal-zeta sensitive. The coupling above is state-dependent; that is precisely why it can exist without proving RH.

The remaining task is to lift `K` to the finite endpoint/carry packets. `L-90027` supplies the matching positive finite radix-four column details, and PR #355 supplies positive Stieltjes/path packets for the fragmentation consumer. A completion must show that the quantile delay can be implemented by those finite packets with signed seed-score loss `o(log^2 X)`.

No such finite loss theorem is asserted here.

## 7. Proof boundary

Closed exactly, subject to independent review:

1. the capped-Gamma target law and transform;
2. the exact endpoint and block survival functions;
3. strict stochastic domination `Y<_st H`;
4. the monotone state-dependent coupling;
5. lossless continuum saturation of the complete radix-four target.

Still open:

1. a finite packet realization of the monotone coupling;
2. a subquadratic signed score-loss bound;
3. the factor-64 endpoint inequality;
4. RH.
