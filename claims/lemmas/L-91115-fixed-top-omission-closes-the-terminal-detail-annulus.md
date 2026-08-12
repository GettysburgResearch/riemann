# L-91115 — A fixed top-endpoint omission closes the complete terminal radix-four annulus at bounded score cost

Claim ID: `L-91115` (provisional research range)  
Status: **PROPOSED COMPLETE ASYMPTOTIC CAPACITY / SCORE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Date: 2026-08-12  
Depends on: `L-91110/L-91111/L-91114`; PR #352 `L-90029`  
Scope: closes the tapering terminal detail annulus while preserving nonnegative endpoint weights and bounded debt; the contracted rough-prime state allocation remains open

## 1. Producer and cutoff

Let

\[
 c_0=0.01844367547104\ldots,
 \qquad
 K=\lceil c_0X\rceil,
\]

and let the positive continuum equality density be

\[
 \lambda_X(s)=L(X/s).
\]

Apply the martingale B-spline quantization of `L-91110`, but truncate its
continuous support at

\[
\boxed{
 S_X=X-W-2,
 \qquad W=10000.
}
\tag{L-91115.1}

Because one continuum cell can place mass only on its two nearest endpoint-state
nodes, every resulting discrete endpoint index is at most

\[
 X-W.
\tag{L-91115.2}

All endpoint weights remain nonnegative.

The interior safety factor from `L-91114` is

\[
 \sigma_K=(1+175/K)^{-1}.
\tag{L-91115.3}

Multiplication by `sigma_K` also preserves nonnegativity.

## 2. Endpoint derivative of one terminal carry column

For real `s` and an integer column `q>s/4`, put

\[
 J=\left\lfloor\frac sq\right\rfloor\in\{1,2,3\}.
\]

The parabolic endpoint derivative is

\[
 \partial_sb_s(m)=\frac{2\sqrt m}{s}-\frac{2m}{s^{3/2}}.
\]

Therefore

\[
\begin{aligned}
 \partial_s v_q(b_s)
 &=\sum_{j=1}^{J}
 \left[\partial_sb_s(jq)-\partial_sb_s(jq+1)\right]\\
 &=\frac{2J}{s^{3/2}}
 -\frac2s\sum_{j=1}^{J}
 \frac1{\sqrt{jq}+\sqrt{jq+1}}.
\end{aligned}
\tag{L-91115.4}

Using

\[
 \frac1{\sqrt{jq}+\sqrt{jq+1}}<\frac1{2\sqrt{jq}}
\]

and `s/q<J+1`,

\[
 s^{3/2}\partial_sv_q(b_s)
 >2J-\sqrt{J+1}\sum_{j=1}^{J}j^{-1/2}.
\tag{L-91115.5}

For `J=1,2,3`, the right side is respectively

\[
 2-\sqrt2,
\]

\[
 4-\sqrt3(1+2^{-1/2}),
\]

and

\[
 6-2(1+2^{-1/2}+3^{-1/2}).
\]

The last two are larger than the first by direct squaring. Hence

\[
\boxed{
 \partial_sv_q(b_s)>(2-\sqrt2)s^{-3/2}
 \qquad(q>s/4).
}
\tag{L-91115.6}

## 3. Response removed by the top omission

Assume

\[
 X>2W+10.
\]

On the omitted interval

\[
 S_X\le s\le X-1
\]

one has `1<=X/s<2`, so the equality density is exactly

\[
 L(X/s)=2\sqrt{X/s}-1\ge1.
\tag{L-91115.7}

Let `Q_X^top` be the B-spline quantization of the omitted density on this
interval.

If

\[
 X/4<q<X-W,
\]

then the active part of the omitted interval has length at least `W`. Equations
(L-91115.6)--(L-91115.7) give the continuum lower bound

\[
 v_q(Q_{X,\mathrm{cont}}^{\mathrm{top}})
 >W(2-\sqrt2)X^{-3/2}.
\tag{L-91115.8}

The quantization error of this top packet is a collar of the type in `L-91111`.
Since its lower endpoint exceeds `X/2`,

\[
 |v_q(C_X^{\mathrm{top}})|
 <\frac{128}{q\sqrt{X/2}}
 <512\sqrt2\,X^{-3/2}
 <800X^{-3/2}.
\tag{L-91115.9}

Thus

\[
\boxed{
 v_q(Q_X^{\mathrm{top}})
 >[W(2-\sqrt2)-800]X^{-3/2}.
}
\tag{L-91115.10}

The elementary bound `sqrt(2)<17/12` gives

\[
 W(2-\sqrt2)-800
 >10000\cdot\frac7{12}-800
 >5033.
\tag{L-91115.11}

## 4. Complete possible terminal overfill

Let `P_X^full` be the unscaled B-spline producer before the top omission. Its
finite target error is the sum of the quantization collar and the
finite/continuum mismatch.

For `q>X/4`, `K>X/55` and `L-91111/L-91114` give

\[
 |v_q(C_X)|<\frac{128}{q\sqrt K}
 <512\sqrt{55}\,X^{-3/2}
 <3840X^{-3/2},
\tag{L-91115.12}

and

\[
 |v_q(E_X)|<\frac{51}{2}q^{-3/2}
 <204X^{-3/2}.
\tag{L-91115.13}

Therefore the possible overfill is strictly below

\[
\boxed{
 [v_q(P_X^{\mathrm{full}})-\Omega_X(q)]_+
 <4044X^{-3/2}.
}
\tag{L-91115.14}

The favorable omission margin in (L-91115.11) is larger.

Hence the top-truncated unscaled producer satisfies

\[
 v_q(P_X^{\mathrm{cut}})<\Omega_X(q)
 \qquad(X/4<q<X-W).
\tag{L-91115.15}

If `q>=X-W`, every retained endpoint index is at most `X-W<=q`, and triangular
support gives

\[
 v_q(P_X^{\mathrm{cut}})=0\le\Omega_X(q).
\tag{L-91115.16}

Thus the entire terminal annulus is feasible.

Since `4q>X` there, the radix-four detail is the ordinary response, so

\[
\boxed{
 \sum_T\Lambda_T^{\mathrm{cut}}\Xi_T(q)
 \le\Omega_X(q)
 \qquad(X/4<q<X).
}
\tag{L-91115.17}

Finally, multiplication by `sigma_K<1` preserves the inequality.

## 5. Interior and terminal synthesis

`L-91114` proves that multiplication by `sigma_K` makes every interior outer
column

\[
 K\le q\le X/4
\]

feasible. The present theorem proves terminal feasibility for

\[
 X/4<q<X.
\]

Consequently the same nonnegative endpoint vector satisfies

\[
\boxed{
 \sum_T\Lambda_T^{\mathrm{reset}}\Xi_T(q)
 \le\Omega_X(q)
 \qquad(K\le q<X).
}
\tag{L-91115.18}

By the positive radix-four telescope of PR #352, it is ordinarily carry-feasible
on every outer column as well.

This completes the recombination of:

```text
finite target/continuum mismatch;
width-three positive quantization collar;
tapering terminal quotient annulus.
```

No terminal finite LP is needed.

## 6. Score debt

The interior factor removes only `O(K^-1)` of a producer of score
`O(sqrt(X)log^2(2X))`, hence costs `O(1)`.

The omitted interval has fixed endpoint width `W`. Differentiating the exact
parabolic score, or summing the endpoint increments directly, gives

\[
 \sum_{T=X-W}^{X}H_T=O(WX^{-1/2}\log^2(2X))=O(1).
\tag{L-91115.19}

Therefore

\[
\boxed{
 E_X^{\mathrm{analytic/discrete}}=O(1)
}
\tag{L-91115.20}

per reset generation.

Endpoint weights remain nonnegative throughout.

## 7. Remaining state transfer

After (L-91115.18), every outer detail column is feasible and all three requested
analytic/discrete effects have bounded score debt. What remains is the exact
inner residual below `K`.

`L-91109/L-91113` identify it with a parity-resolved positive finite forcing plus
delayed rough-prime copies of the contracted `(L,R)` state. The remaining theorem
is the capacity-faithful coefficient-one allocation of those delayed states.

No positivity of the inverse rough-prime renewal is asserted here.

## 8. Proof boundary

```text
terminal endpoint derivative lower bound          PROPOSED COMPLETE EXACT
fixed top omission response >5033 X^-3/2          PROPOSED COMPLETE
all possible terminal overfill <4044 X^-3/2       PROPOSED COMPLETE
complete terminal detail feasibility              PROPOSED COMPLETE
interior+terminal nonnegative endpoint vector      PROPOSED COMPLETE
bounded analytic/discrete debt per reset           PROPOSED COMPLETE
contracted rough-prime (L,R) allocation            OPEN / RH-BEARING
Riemann Hypothesis                                 UNPROVEN
```
