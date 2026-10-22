# L-90021 — The factor-64 filter is a two-state cyclotomic decrement with an explicit radical/ramp kernel

Claim ID: `L-90021` (provisional range; branch-qualified)  
Title: The cyclotomic factorization reduces the seven-scale endpoint to a factor-eight decrement of one factor-four critical state, and its entire finite arithmetic content is one explicit radical kernel minus one signed prime-ramp spline  
Status: **PROPOSED COMPLETE EXACT STATE/FINITE-NORMAL-FORM LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Date: 2026-08-10  
Depends on: `L-90004`, `L-90018`, `L-90019`  
Scope: exact state and finite annular formulas; no sign theorem or RH claim

## 1. Cyclotomic factorization

The filter of `L-90019` satisfies

\[
\boxed{
 P_{64}(y)
 =(1-y^2)(1-y^3)(1-y/\sqrt2).
}
\tag{L-90021.1}

Indeed

\[
 (1-y^2)(1-y^3)
 =(1-y)^2(1+y)(1+y+y^2).
\]

Let the scale-shift operator be

\[
 (\mathcal Sf)(X)=f(X/2).
\]

Define the critical state

\[
\boxed{
 C(X)=(I-2^{-1/2}\mathcal S)A(X)
 =A(X)-2^{-1/2}A(X/2),
}
\tag{L-90021.2}

and its factor-four shell

\[
\boxed{
 G(X)=(I-\mathcal S^2)C(X)
 =C(X)-C(X/4).
}
\tag{L-90021.3}

Then

\[
\boxed{
 \mathcal U_{64}(X)
 =(I-\mathcal S^3)G(X)
 =G(X)-G(X/8).
}
\tag{L-90021.4}

Thus the factor-64 conclusion is the single scale monotonicity statement

\[
\boxed{G(X)<G(X/8)}
\tag{L-90021.5}

for all sufficiently large `X`.

By `T-90014`, eventual strict inequality (L-90021.5), or eventual one-sidedness of its difference, is equivalent to RH.

## 2. The factor-64 ramp spline

Put

\[
 q=1/\sqrt2,
 \qquad
 u=\log_2(X/m).
\]

The compact spline of `L-90018` for `P_64` is

\[
\boxed{
\Phi_{64}(u)=
\begin{cases}
 u,&0\le u\le1,\\
 (1-q)u+q,&1\le u\le2,\\
 2+q-qu,&2\le u\le3,\\
 5-2q-u,&3\le u\le4,\\
 5-6q+(q-1)u,&4\le u\le5,\\
 q(u-6),&5\le u\le6,\\
 0,&\text{otherwise}.
\end{cases}}
\tag{L-90021.6}

It has one interior sign change:

\[
\boxed{
 u_*=5-\sqrt2.
}
\tag{L-90021.7}

Hence

\[
 \Phi_{64}(u)>0\quad(0<u<u_*),
 \qquad
 \Phi_{64}(u)<0\quad(u_*<u<6).
\tag{L-90021.8}

The critical moment is exactly

\[
 \int_0^6\Phi_{64}(u)2^{u/2}\,du=0.
\tag{L-90021.9}

## 3. The critical seed step function

For the coefficients `a_j=[y^j]P_64(y)`, define

\[
 \Psi_{64}(u)
 =\sum_{0\le j\le u}a_j2^{j/2}.
\]

Exact summation gives

\[
\boxed{
\Psi_{64}(u)=
\begin{cases}
 1,&0\le u<1,\\
 0,&1\le u<2,\\
 -2,&2\le u<3,\\
 -2\sqrt2,&3\le u<4,\\
 0,&4\le u<5,\\
 4\sqrt2,&5\le u<6,\\
 0,&\text{otherwise}.
\end{cases}}
\tag{L-90021.10}

The final zero is precisely the critical seed cancellation

\[
 P_{64}(\sqrt2)=0.
\]

## 4. Complete finite radical/ramp normal form

Let

\[
 d(m)=\log\operatorname{rad}(m)-\log\operatorname{rad}(m-1)
\]

as in `L-90004`, and set

\[
 u_m=\log_2(X/m).
\]

For every `X/64<m<=X`, direct substitution of the parabolic seed at the seven scales gives

\[
\boxed{
 \beta_{64,X}(m)
 =2\sqrt m(\log2)\Phi_{64}(u_m)
 +{4m\over\sqrt X}\Psi_{64}(u_m).
}
\tag{L-90021.11}

For `m<=X/64` the same expression is zero because both compact coordinates have returned to zero.

The exact radical switching and ramp formula therefore give

\[
\boxed{
\begin{aligned}
 \mathcal U_{64}(X)
 ={}&\sum_{X/64<m\le X}
 \beta_{64,X}(m)d(m)\\
 &-(\log2)
 \sum_{X/64<p\le X}
 {\log p\over\sqrt p}
 \Phi_{64}(\log_2(X/p)).
\end{aligned}}
\tag{L-90021.12}

Equation (L-90021.12) is the complete finite conclusion-producing coordinate. Nothing outside the factor-64 annulus remains.

## 5. Exact two-sector ramp split

The prime-ramp term in (L-90021.12) is the difference of two nonnegative sector masses:

\[
 \mathcal R_+(X)
 =\sum_{X/2^{u_*}<p\le X}
 {\log p\over\sqrt p}\Phi_{64}(u_p),
\]

and

\[
 \mathcal R_-(X)
 =\sum_{X/64<p<X/2^{u_*}}
 {\log p\over\sqrt p}[-\Phi_{64}(u_p)].
\]

Thus

\[
\boxed{
 \mathcal F_{64}P_{\mathbb P}(X)
 =\log2\,[\mathcal R_+(X)-\mathcal R_-(X)].
}
\tag{L-90021.13}

The endpoint inequality is not a termwise sign statement: the radical seed term in (L-90021.12) must pay the signed difference (L-90021.13), together with the explicit prime-power moat.

## 6. Strategic consequence

The preferred arithmetic attack is now one of the equivalent formulations:

```text
factor-eight monotonicity of the factor-four critical state G;

or

annular radical seed
    <= signed two-sector prime ramp
       with the fixed RH-side moat.
```

The first is a one-state recurrence. The second is a finite factorization problem on `[X/64,X]`. Both retain every off-line zero and are exactly equivalent to the factor-64 endpoint sign.

## 7. Proof boundary

Closed exactly:

1. cyclotomic operator factorization;
2. reduction to one factor-eight state decrement;
3. the compact ramp spline and unique sign change;
4. the critical seed step function;
5. the complete finite radical/ramp formula;
6. the two-sector ramp decomposition.

Still open:

1. monotonicity of `G`;
2. the annular radical-versus-ramp inequality;
3. RH.
