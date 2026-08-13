# L-91114 — The finite/continuum equality mismatch gains one full power after the carry difference

Claim ID: `L-91114` (provisional research range)  
Status: **PROPOSED COMPLETE EXACT MISMATCH / INTERIOR-CAPACITY THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Date: 2026-08-12  
Depends on: `R-91102`; `L-91110/L-91111`; PR #352 `L-90029`  
Scope: exact adjacent mismatch identity, explicit outer carry/detail bounds, and bounded-cost interior safety factor; terminal quotient collars and rough-prime state allocation remain separate

## 1. Finite and continuum equality seeds

For real `t>=1`, define the continuous equality divergence

\[
 d_X^\star(t)
 =\sum_{k\le X/t}\frac{\mu(k)}{\sqrt{kt}}
   \log\frac{X}{kt},
\tag{L-91114.1}
\]

with causal cutoff. The entering summand at `t=X/k` is zero, so
`d_X^star` is continuous at every activation point.

The exact finite and continuum seeds are

\[
 b_X^\star(n)=\sum_{m=n}^{X}d_X^\star(m),
\tag{L-91114.2}
\]

and

\[
 \overline b_X^\star(n)=\int_n^Xd_X^\star(t)dt
 =\sqrt X\,\mathscr B^\star(n/X).
\tag{L-91114.3}
\]

Put

\[
 E_X(n)=b_X^\star(n)-\overline b_X^\star(n).
\tag{L-91114.4}
\]

`R-91102` proves that `E_X` is not identically zero.

## 2. Exact adjacent-difference identity

Telescoping the sum and the integral separately gives

\[
\boxed{
 E_X(n)-E_X(n+1)
 =d_X^\star(n)-\int_n^{n+1}d_X^\star(t)dt.
}
\tag{L-91114.5}

Thus the carry operator does not see the macroscopic accumulated Riemann-sum
error. It sees one local quadrature error.

## 3. Uniform derivative bound on the reset window

Assume

\[
 n\ge X/55.
\]

On every smooth subinterval of `[n,n+1]`, at most the terms `k<=55` are active,
and

\[
 \left|\frac d{dt}
 \left[t^{-1/2}\log\frac{X}{kt}\right]\right|
 =t^{-3/2}\left(1+\frac12\log\frac{X}{kt}\right).
\tag{L-91114.6}
\]

Define the finite constant

\[
 C_{55}
 =\sum_{k\le55}\frac{|\mu(k)|}{\sqrt k}
 \left(1+\frac12\log\frac{55}{k}\right).
\tag{L-91114.7}
\]

The directed standard-library checker `X-91105` proves

\[
\boxed{C_{55}<17.}
\tag{L-91114.8}
\]

The piecewise derivative bound and continuity at activation points make
`d_X^star` globally Lipschitz on `[n,n+1]`. Therefore

\[
\begin{aligned}
 |E_X(n)-E_X(n+1)|
 &\le\int_n^{n+1}|d_X^\star(n)-d_X^\star(t)|dt\\
 &<\frac{17}{2}n^{-3/2}.
\end{aligned}
\]

Hence

\[
\boxed{
 |\Delta E_X(n)|<\frac{17}{2}n^{-3/2}
 \qquad(n\ge X/55).
}
\tag{L-91114.9}

This is one full power smaller than the accumulated seed-level corridor.

## 4. Ordinary carry and radix-four detail bounds

For a zero-extended seed,

\[
 v_q(E_X)=\sum_{j\ge1}[E_X(jq)-E_X(jq+1)].
\]

If `q>=X/55`, every active node lies in the range of (L-91114.9). Since

\[
 \sum_{j\ge1}j^{-3/2}<3,
\]

one obtains

\[
\boxed{
 |v_q(E_X)|<\frac{51}{2}q^{-3/2}.
}
\tag{L-91114.10}

For the radix-four detail

\[
 \mathcal D_4v_q(E_X)=v_q(E_X)-2v_{4q}(E_X),
\]

\[
\begin{aligned}
 |\mathcal D_4v_q(E_X)|
 &<\frac{51}{2}q^{-3/2}
 +51(4q)^{-3/2}\\
 &=\frac{255}{8}q^{-3/2}
 <32q^{-3/2}.
\end{aligned}
\]

Thus

\[
\boxed{
 |\mathcal D_4v_q(E_X)|<32q^{-3/2}.
}
\tag{L-91114.11}

## 5. Combination with the positive B-spline collar

Let `C_X` be the positive martingale-quantization collar of `L-91111`, with
reset scale `K`. That theorem gives

\[
 |\mathcal D_4v_q(C_X)|<\frac{200}{q\sqrt K}.
\tag{L-91114.12}

The quantized continuum equality producer differs from the exact equality target
by the signed seed `C_X-E_X`. Hence, on an interior radix-four column

\[
 K\le q\le X/4,
\]

\[
\boxed{
 \left|
 \mathcal D_4v_q(C_X-E_X)
 \right|
 <32q^{-3/2}+\frac{200}{q\sqrt K}.
}
\tag{L-91114.13}

There

\[
 \Omega_X(q)=\frac{\log4}{\sqrt q}.
\]

Using `q>=K` and the elementary bound `log4>4/3`,

\[
\boxed{
 \frac{|\mathcal D_4v_q(C_X-E_X)|}{\Omega_X(q)}
 <\frac{174}{K}.
}
\tag{L-91114.14}

Consequently, when `K>175`, multiplying every nonnegative quantized endpoint
weight by

\[
\boxed{
 \sigma_K=\frac1{1+175/K}
}
\tag{L-91114.15}

makes every interior detail column feasible. Endpoint weights remain
nonnegative.

## 6. Score cost of the interior safety factor

A crude all-integer majorant gives the score of the outer producer as

\[
 O(\sqrt X\log^2(2X)).
\]

For the factor-54 reset, `K\asymp X`. Therefore the score removed by
(L-91114.15) is

\[
 O\left(\frac{\log^2(2X)}{\sqrt X}\right)=O(1).
\tag{L-91114.16}
\]

The sharper expected cost tends to zero, but boundedness is all that is required
by the reset consumer.

Thus the finite target/continuum mismatch and the positive width-three
quantization collar are fully paid on every interior outer column with
nonnegative endpoint weights and bounded score debt.

## 7. Terminal annulus and parity state

The estimate (L-91114.11) also places the finite mismatch at the natural
`X^-3/2` terminal scale. `L-91306` proves that the quantization contribution has
two extra powers away from four bounded quotient collars and that the last-column
ratio tends to `1/16`.

Therefore the only terminal work left is a bounded-dimensional taper/capacity
certificate. It is not a macroscopic safety-factor problem.

After those finite collars, the unresolved state is the parity-resolved
contracted `(L,R)` renewal of `L-91109/L-91113`. This lemma does not assert the
positive inverse of that rough-prime renewal.

## 8. Proof boundary

```text
exact adjacent finite/continuum mismatch identity   PROPOSED COMPLETE
explicit constant C55<17                            DIRECTED EXACT
ordinary mismatch carry O(q^-3/2)                  PROPOSED COMPLETE
radix-four mismatch O(q^-3/2)                      PROPOSED COMPLETE
interior mismatch+collar relative <174/K           PROPOSED COMPLETE
nonnegative 1/(1+175/K) safety scaling             PROPOSED COMPLETE
bounded interior score debt                         PROPOSED COMPLETE
bounded terminal quotient certificate               OPEN
rough-prime coefficient-one allocation               OPEN / RH-BEARING
Riemann Hypothesis                                  UNPROVEN
```
