# L-34408 — Every dyadic odd-source relative curvature is an exact positive staircase

Claim ID: `L-34408`  
Title: At every dyadic dilation, the odd-source relative Jordan curvature contains the full current innovation square with coefficient one plus an explicit all-row nonnegative staircase of odd Selberg terms  
Status: **PROPOSED COMPLETE EXACT ALL-DYADIC THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring/review agent: `gpt56-pro`  
Created: 2026-08-10  
Dependencies: `R-34401`, `L-34407`; PR #346 `L-34404`; elementary Kummer/Legendre and a block-choice injection  
Scope: every integer carry row and every fixed dyadic dilation; no upper/dissipative recurrence and no RH claim

## 1. Odd-prime row data

Retain the odd Möbius source

\[
 B_{\rm odd}(s)=\prod_{p\ {m odd}}(1-p^{-s}),
\]

its positive generalized-prime sequence

\[
 \Lambda_{\rm odd}(n)=\Lambda(n)\mathbf1_{n\ {m odd}},
\]

and

\[
 C_{\rm odd}
 =\Lambda_{\rm odd}\log
  +\Lambda_{\rm odd}*\Lambda_{\rm odd}\ge0.
\]

For a nontrivial row

\[
 e=(n,j),\qquad k=n-j,\qquad1\le j<n,
\]

write

\[
 O(e)=\mathcal L_e(\Lambda_{\rm odd})
 =\log\operatorname{odd}{n\choose j}\ge0,
\]

\[
 S(e)=\mathcal L_e(C_{\rm odd})\ge0,
\]

and

\[
 R(e)=O(e)^2-S(e).
\]

Let `Y,Q,T` denote the bare, first-current, and second-current coordinates of the source-convolved odd Jordan path, as in `L-34407`.

For an integer `r>=1`, put

\[
 e_a=2^a e=(2^an,2^aj),
 \qquad0\le a\le r.
\tag{L-34408.1}
\]

## 2. Exact bare-source difference at every dyadic scale

`R-34401` proves

\[
 Y(n,j)
 =\lfloor\log_2n\rfloor
  -\lfloor\log_2j\rfloor
  -\lfloor\log_2k\rfloor-1.
\]

Scaling all three row coordinates by `2^r` adds `r` to each floor. Therefore

\[
\boxed{
 Y(e_r)-Y(e)=-r.
}
\tag{L-34408.2}
\]

Equivalently, at the source level,

\[
 \mathbf1*((\varepsilon-\delta_{2^r})*b_{\rm odd})
 ={1-z^r\over1-z}
 =1+z+\cdots+z^{r-1},
 \qquad z=2^{-s},
\]

whose stabilized ordinary prefix is `r`; every nontrivial additive defect is `-r`.

## 3. Exact second-current staircase

Let

\[
 H(N)=\sum_{m\le N}C_{\rm odd}(m)
\]

and let `G` be the ordinary prefix of `1*t_odd`.  `L-34407` proves

\[
 G(N)=\sum_{a\ge0}H(\lfloor N/2^a\rfloor)
\]

and hence

\[
 G(2N)=G(N)+H(2N).
\]

Iteration gives, for every `r>=1`,

\[
\boxed{
 G(2^rN)=G(N)+\sum_{a=1}^r H(2^aN).
}
\tag{L-34408.3}
\]

Taking parent-minus-children defects yields

\[
\boxed{
 T(e_r)-T(e)=\sum_{a=1}^r S(e_a)\ge0.
}
\tag{L-34408.4}

This is the all-dyadic extension of `L-34407.12`.

## 4. Relative Jordan vector at scale `2^r`

Let

\[
 F_e(\tau)=1+\mathcal L_e(J_{{\rm odd},\tau})
\]

for the positive odd-prime Jordan deformation. Define

\[
\boxed{
 H_{e,r}(\tau)
 ={F_{e_r}(\tau)\over F_e(2^r\tau)}.
}
\tag{L-34408.5}

Put

\[
 E_r(e)=O(e_r)-2^rO(e)
\tag{L-34408.6}
\]

and

\[
 \Delta_rR(e)=R(e_r)-2^{2r}R(e).
\tag{L-34408.7}
\]

Then exactly

\[
 H_{e,r}(0)=1,
 \qquad H_{e,r}'(0)=E_r(e),
\]

and

\[
\boxed{
 -\bigl(\log H_{e,r}\bigr)''(0)=\Delta_rR(e).
}
\tag{L-34408.8}

For the source coordinate define

\[
\boxed{
 G_{e,r}(\tau)
 =\mathcal L_{e_r}
   ((\varepsilon-\delta_{2^r})*K_{{\rm odd},\tau}).
}
\tag{L-34408.9}

Aligned carry scaling gives

\[
 G_{e,r}(0)=-r,
\]

\[
 G_{e,r}'(0)
 =Q(e_r)-Q(e)
 =:I_r(e),
\tag{L-34408.10}
\]

and, by (L-34408.4),

\[
 G_{e,r}''(0)
 =\sum_{a=1}^rS(e_a).
\tag{L-34408.11}

Put

\[
 W_{e,r}(\tau)=(H_{e,r}(\tau),G_{e,r}(\tau)).
\]

Its Hilbert/Jordan curvature is therefore

\[
\boxed{
 \mathfrak C_r(e)
 =\Delta_rR(e)+|I_r(e)|^2
  +r\sum_{a=1}^rS(e_a).
}
\tag{L-34408.12}

No estimate has entered.

## 5. Exact positive-staircase expansion

Since

\[
 O(e_r)=2^rO(e)+E_r(e),
\]

one has

\[
\begin{aligned}
 \Delta_rR(e)
 ={}&E_r(e)\bigl(2^{r+1}O(e)+E_r(e)\bigr)\\
 &-S(e_r)+2^{2r}S(e).
\end{aligned}
\tag{L-34408.13}

Substitution into (L-34408.12) gives

\[
\boxed{
\begin{aligned}
 \mathfrak C_r(e)
 ={}&|I_r(e)|^2
  +E_r(e)\bigl(2^{r+1}O(e)+E_r(e)\bigr)\\
 &+2^{2r}S(e)
  +r\sum_{a=1}^{r-1}S(e_a)
  +(r-1)S(e_r).
\end{aligned}}
\tag{L-34408.14}

For `r=2` this is exactly the repaired five-piece ledger

\[
 |I_2|^2+E_2(8O+E_2)
 +16S(e)+2S(2e)+S(4e).
\]

## 6. The odd first-moment increment is nonnegative on every row

Let

\[
 v=v_2{n\choose j}.
\]

Binary Kummer carries are unchanged when all three integers are shifted left by `r` binary places. Equivalently, Legendre's digit formula gives

\[
\boxed{
 v_2{2^rn\choose2^rj}=v.
}
\tag{L-34408.15}

Moreover, partition a `2^rn`-element set into `2^r` labeled blocks of size `n`. Choosing exactly `j` elements from every block injects into the family of all `2^rj`-subsets. Hence

\[
\boxed{
 {2^rn\choose2^rj}
 \ge {n\choose j}^{2^r}.
}
\tag{L-34408.16}

Therefore

\[
\begin{aligned}
 E_r(e)
 &={\log\operatorname{odd}{2^rn\choose2^rj}}
   -2^r{\log\operatorname{odd}{n\choose j}}\\
 &=\log
   {{2^rn\choose2^rj}\over{n\choose j}^{2^r}}
  +(2^r-1)v\log2
 \ge0.
\end{aligned}
\]

Thus

\[
\boxed{E_r(e)\ge0}
\tag{L-34408.17}
\]

for every nontrivial row and every `r>=1`.  This strengthens the prior cofinal estimate: no balanced-cone or large-endpoint hypothesis is required for the sign.

## 7. All-row source-complete domination

Every quantity

\[
 O(e),\quad E_r(e),\quad S(e_a)
\]

in the second and third lines of (L-34408.14) is nonnegative. Consequently

\[
\boxed{
 \mathfrak C_r(e)\ge |I_r(e)|^2\ge0
}
\tag{L-34408.18}

for every integer carry row and every dyadic scale `2^r`.

The repaired odd-source vector curvature is therefore not merely cofinally positive. It is an exact all-row positive storage state, and it contains the complete scale-`2^r` odd-current innovation with coefficient one.

On every fixed balanced cone, the block-choice ratio in (L-34408.16), together with ordinary Stirling bounds, gives

\[
 E_r(e)\gg_{r,\eta}\log n,
 \qquad O(e)\gg_\eta n,
\]

cofinally. Hence

\[
\boxed{
 \mathfrak C_r(e)
 \ge |I_r(e)|^2+c_{r,\eta}n\log n
}
\tag{L-34408.19}
\]

for one explicit positive constant after a finite base.

## 8. Sharp coefficient-one critical normalization at every dyadic scale

Define the critically normalized odd current

\[
 U(e)={Q(e)\over\sqrt n}.
\]

Since `Q(e_r)=Q(e)+I_r(e)`, exactly

\[
\boxed{
 U(e_r)
 =2^{-r/2}
  \left(U(e)+{I_r(e)\over\sqrt n}\right).
}
\tag{L-34408.20}

For `lambda=2^{-r/2}`, the sharp inequality with coefficient one on `|a|^2` is

\[
 \lambda^2|a+b|^2
 \le |a|^2+{\lambda^2\over1-\lambda^2}|b|^2.
\]

Therefore

\[
\boxed{
 |U(e_r)|^2
 \le |U(e)|^2
  +{|I_r(e)|^2\over(2^r-1)n}.
}
\tag{L-34408.21}

Combining with (L-34408.18),

\[
\boxed{
 |U(e_r)|^2
 \le |U(e)|^2
  +{\mathfrak C_r(e)\over(2^r-1)n}.
}
\tag{L-34408.22}

Thus at every dyadic scale the remaining problem has the same exact form:

```text
positive all-row relative curvature
contains the innovation square with coefficient one;

an upper/dissipative law for that curvature
gives a coefficient-one normalized current recurrence.
```

The case `r=2` is the live Q=4 recurrence. Larger `r` provide exact multiscale alternatives without changing the logical interface.

## 9. Consequences for the reflected programme

The local arithmetic sign problem for the odd relative state is now closed at every dyadic scale:

1. the relative bare charge is exactly `-r`;
2. the relative second current is the positive staircase `sum_(a=1)^r S(2^a e)`;
3. the odd first-moment increment is nonnegative on every row;
4. the complete relative curvature is an explicit sum of nonnegative quantities;
5. the current innovation is included with coefficient one;
6. critical normalization has the sharp loss `1/(2^r-1)`.

What remains is not another row sign or a finite-source correction. It is the genuinely global reflected question: place `C_r` as dissipative storage in the independent-frequency block evolution or otherwise prove an upper fixed-delay law for it.

## 10. Proof boundary

Closed exactly here, subject to review:

- every all-dyadic source jet identity;
- bare charge `-r`;
- positive second-current staircase;
- exact relative curvature formula;
- exact nonnegative expansion;
- all-row sign of the odd Kummer increment;
- all-row domination `C_r>=|I_r|^2`;
- sharp coefficient-one normalized recurrence adapter.

Open:

- an upper/dissipative law for `C_r` at one or more scales;
- global subpower odd-current energy;
- transfer to the full compact current with controlled finite gauges;
- RH.
