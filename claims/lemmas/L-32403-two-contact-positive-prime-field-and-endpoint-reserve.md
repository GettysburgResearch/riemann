# L-32403 — Two-contact source, positive generalized primes, and a closed endpoint reserve

Claim ID: `L-32403`  
Title: The dyadic two-contact inverse has positive coefficients and generalized primes, a one-crossing continuous carry profile, and an explicit source-complete endpoint Selberg reserve  
Status: **PROPOSED COMPLETE EXACT ANALYTIC/FINITE LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: `L-32401`; PR #297 `L-29001`--`L-29006`  
Scope: exact source, physical field, and endpoint binding; no coupled interior estimate or RH claim

## 1. Positive inverse and generalized primes

Let

\[
 B_2(s)={1-2^{-s}\over\zeta(s)}
\]

be the Dirichlet series of `b_2` from `L-32401`, and let

\[
 A_2(s)=B_2(s)^{-1}
 ={\zeta(s)\over1-2^{-s}}.
\tag{L-32403.1}
\]

Its coefficients are

\[
\boxed{
 a_2(n)=v_2(n)+1>0.
}
\tag{L-32403.2}
\]

Indeed `1/(1-2^-s)` is the Dirichlet series of the powers of two, and convolution with the constant-one coefficients of `zeta` counts the powers of two dividing `n`.

The generalized von Mangoldt sequence of `A_2` is

\[
\boxed{
 \Lambda_2(n)
 =\Lambda(n)
 + (\log2)\mathbf1_{n=2^r,\ r\ge1}
 \ge0.
}
\tag{L-32403.3}
\]

Thus the source has a positive inverse and a nonnegative generalized-prime sequence. The only difference from the ordinary von Mangoldt source is one extra copy of the dyadic prime-power tower.

## 2. Real carry prefix

For real `x>=0`, put

\[
 G_2(x)=\sum_{q\le x}b_2(q)\left\lfloor{x\over q}\right\rfloor.
\]

The finite divisor interchange from `L-32401` remains valid at real `x` and gives

\[
\boxed{
 G_2(x)=\mathbf1_{1\le x<2}.
}
\tag{L-32403.4}
\]

For `0<=theta<=1`, define the scaled carry profile

\[
 Z_2(x,\theta)
 =G_2(x)-G_2(\theta x)-G_2((1-\theta)x).
\tag{L-32403.5}
\]

Then

\[
\boxed{
 Z_2(x,\theta)\ge0\quad(1\le x<2),
}
\tag{L-32403.6}
\]

and

\[
\boxed{
 Z_2(x,\theta)\le0\quad(x\ge2).
}
\tag{L-32403.7}
\]

For (L-32403.6), when `x<2` the two children have sum `x`, so they cannot both belong to `[1,2)`; the parent contributes one. For (L-32403.7), the parent contributes zero. If neither child contributed, both would be below one or at least two. Both below one would force their sum below two, contradicting `x>=2`; if a child is at least two its contribution is already zero but the other child must then supply either a nonnegative indicator or the equality case. Direct inspection gives a child-indicator sum at least zero, so `Z_2` is nonpositive. More simply, for `x>=2`, (L-32403.5) is the negative of the sum of the two child indicators.

Thus the complete continuous carry profile has one exact source-scale sign transition at `x=2`.

At the central position `theta=1/2`,

\[
\boxed{
 Z_2(x,1/2)
 =\begin{cases}
 1,&1\le x<2,\\
 -2,&2\le x<4,\\
 0,&\text{otherwise}.
 \end{cases}}
\tag{L-32403.8}
\]

## 3. Pole-preserving positive-source field

Let `H_theta` be the symmetric Nyman/carry window of PR #297, with

\[
 \widehat H_\theta(z)=\zeta(s)N_\theta(s),
 \qquad s=z+1/2.
\]

Convolving first with the normalized `b_2` source gives the zero-free numerator

\[
 (1-2^{-s})N_\theta(s).
\]

Now convolve with the positive generalized-prime measure `Lambda_2`. The transform is

\[
\boxed{
 (1-2^{-s})N_\theta(s)
 \left[
 -{\zeta'\over\zeta}(s)
 +{(\log2)2^{-s}\over1-2^{-s}}
 \right].
}
\tag{L-32403.9}
\]

The second term is holomorphic in the open critical strip. At a nontrivial zero `rho` of multiplicity `m_rho`, the residue is therefore

\[
\boxed{
 -m_\rho(1-2^{-\rho})N_\theta(\rho).
}
\tag{L-32403.10}
\]

The finite Euler numerator does not vanish at a nontrivial zero, and the balanced `theta` frame of `L-29001` has positive norm at every zero. Hence this positive-source field retains every off-line zeta pole.

## 4. Exact finite Jensen defect

Put

\[
 \psi_2(y)=\sum_{n\le y}\Lambda_2(n)
\]

and

\[
\boxed{
 A_2(y)=\psi_2(y)-\psi_2(y/2).
}
\tag{L-32403.11]
\]

(the closing bracket in the tag is typographical only).

For every real `X>=1`, finite convolution and (L-32403.4) give

\[
\boxed{
 \sqrt X\,\mathfrak P_{2,\theta}(\log X)
 =A_2(X)-A_2(\theta X)-A_2((1-\theta)X).
}
\tag{L-32403.12}
\]

The linear density of `psi_2` is still `y`; the extra dyadic tower is only logarithmic. Hence the linear model of `A_2` is `y/2`, and it cancels exactly in (L-32403.12).

At `theta=1/2`,

\[
\boxed{
 \sqrt X\,\mathfrak P_{2,1/2}(\log X)
 =\psi_2(X)-3\psi_2(X/2)+2\psi_2(X/4).
}
\tag{L-32403.13]
\]

Again the closing bracket in the tag is typographical only.

Equations (L-32403.9)--(L-32403.13) give a particularly small pole-preserving prime-annulus field: one positive top half, one negative second quarter, and no farther source at the central position.

## 5. Endpoint fibers close exactly

Retain the canonical balanced-tree endpoint commutators

\[
 D_n=T_n-T_{n-1}
\]

of PR #297 and their recursion

\[
 D_{2n}=D_n+E_n,
 \qquad
 E_n=[2n,n]-[2n-1,n-1].
\]

For the step `g_m(r)=1_{m<=r<2m}`, define

\[
\boxed{
 V_m=D_m-D_{2m}=-E_m
 =[2m-1,m-1]-[2m,m].
}
\tag{L-32403.14]
\]

Thus the complete filtered endpoint is already a compact two-edge object.

For any finitely supported nonnegative source `x_m`, define

\[
 A_x(r)=\sum_mx_mg_m(r)
\]

and its endpoint chain

\[
 \mathcal E_x
 =\sum_{r\ge2}[A_x(r)-A_x(r-1)]D_r.
\]

The step has only two jumps, so exact finite recombination gives

\[
\boxed{
 \mathcal E_x=\sum_mx_mV_m.
}
\tag{L-32403.15]
\]

For the physical field, `x_m=Lambda_2(m)>=0`; hence this is a nonnegative superposition of complete fibers.

## 6. Strict endpoint Selberg reserve

Let `F` be the ordinary logarithmic Kummer functional and `S` the ordinary complete Selberg forcing functional on split chains. Since `D_n` is carry/entropy equivalent to `[n,1]`,

\[
 F(D_n)=\log n,
 \qquad
 S(D_n)=\log^2n.
\]

Writing `L=log2`, (L-32403.14) gives

\[
\boxed{
 F(V_m)=-L,
}
\tag{L-32403.16]
\]

and

\[
\boxed{
 S(V_m)=-2L\log m-L^2.
}
\tag{L-32403.17]
\]

Therefore every individual fiber has the strict reserve

\[
\boxed{
 F(V_m)^2-S(V_m)=2L\log(2m)>0.
}
\tag{L-32403.18]
\]

For the nonnegative superposition (L-32403.15), put

\[
 X_0=\sum_mx_m,
 \qquad
 X_1=\sum_mx_m\log m.
\]

Then

\[
 F(\mathcal E_x)=-LX_0,
\]

\[
 S(\mathcal E_x)=-2LX_1-L^2X_0,
\]

and hence

\[
\boxed{
 \mathcal Q_{\rm end}(x)
 :=F(\mathcal E_x)^2-S(\mathcal E_x)
 =L^2X_0^2+2LX_1+L^2X_0>0
}
\tag{L-32403.19]
\]

for every nonzero nonnegative source.

## 7. Physical endpoint norm bound

In logarithmic coordinates one fiber is simply

\[
 h(t)=\mathbf1_{[0,L)}(t).
\]

On one dyadic source annulus `M<=m<2M`,

\[
 f_x(t)=\sum_mx_mh(t-\log m)
\]

is supported in an interval of length at most `2L` and satisfies `|f_x|<=X_0`. Hence

\[
 \|f_x\|_2^2\le2LX_0^2.
\]

Equation (L-32403.19) gives

\[
\boxed{
 \|f_x\|_2^2
 \le{2\over\log2}\,\mathcal Q_{\rm end}(x).
}
\tag{L-32403.20]
\]

Dyadic blocks of the same parity have disjoint interiors after this one-step support enlargement. A two-color decomposition therefore gives the global source-complete endpoint bound

\[
\boxed{
 \|f_x\|_2^2
 \le{4\over\log2}
 \sum_k\mathcal Q_{\rm end}(x|_{[2^k,2^{k+1})}).
}
\tag{L-32403.21]
\]

This closes the endpoint source-binding problem for the two-contact positive generalized-prime field with a simpler two-edge fiber and better constant than the factor-four endpoint package on PR #297.

## 8. Exact frontier

The following are now simultaneous properties of one source:

```text
zero-safe reciprocal-zeta numerator;
root-divergence/two-contact invariant;
positive inverse coefficients;
nonnegative generalized primes;
continuous one-crossing carry profile;
compact central prime-annulus field;
strict source-complete endpoint reserve.
```

The remaining physical problem is entirely the coupled **interior** Jensen/carry Gram. No endpoint source theorem remains to be supplied by a reviewer.

## 9. Proof boundary

Closed here:

- positive inverse and generalized-prime formulas;
- real one-crossing carry profile;
- pole-preserving positive-source field;
- finite Jensen-defect and central two-band formula;
- exact two-edge endpoint fiber;
- strict aggregate endpoint reserve;
- source-complete physical endpoint norm bound.

Open:

- a coupled interior Gram estimate for (L-32403.12);
- a recurrence or direct bound for the root scalar of `L-32401`;
- RH.
