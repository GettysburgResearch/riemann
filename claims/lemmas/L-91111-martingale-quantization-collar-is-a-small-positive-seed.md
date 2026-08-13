# L-91111 — The martingale-quantization collar is a small positive seed

Claim ID: `L-91111` (provisional research range)  
Title: The continuum-to-endpoint B-spline discrepancy is coefficientwise nonnegative, has an explicit one-node-per-half-cell formula and \(m^{-3/2}\) decay, and its complete radix-four carry disturbance is \(O((q\sqrt K)^{-1})\) when the reset begins at scale \(K\)  
Status: **PROPOSED COMPLETE EXACT SIGN / QUANTITATIVE COLLAR THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Date: 2026-08-11  
Depends on: `L-91110`; elementary endpoint-state bounds  
Scope: exact collar sign and size; the separate finite equality-target mismatch and terminal annulus remain open

## 1. Cell splitting point

Retain the martingale quantization of `L-91110`. On the endpoint cell
\[
 T-1<s<T,
\]
put
\[
 s_T=r_T^{-2}.
\]
Since
\[
 T^{-1/2}<r_T<(T-1)^{-1/2},
\]
one has
\[
 T-1<s_T<T.
\]

For \(T-1<s<s_T\), the state \(r(s)\) is represented by the pair \(r_{T-1},r_T\). For \(s_T<s<T\), it is represented by \(r_T,r_{T+1}\).

Let
\[
 C(m)=F_{\rm disc}(m)-F_{\rm cont}(m)
\]
be the seed discrepancy.

## 2. Exact positive collar formula

For \(s\in(T-1,s_T)\), every node except \(m=T-1\) is represented exactly. At \(m=T-1\), the affine moment identity uses the virtual old-node value
\[
 \sqrt{T-1}-r_{T-1}(T-1)<0,
\]
whereas the actual entering endpoint atom \(e_{T-1}(T-1)\) is zero. Therefore the quantized seed exceeds the continuous seed by
\[
 a(s)q_{T-1}(s)
 \sqrt{T-1}
 [r_{T-1}\sqrt{T-1}-1]
\]
at node \(T-1\).

For \(s\in(s_T,T)\), every node except \(m=T\) is represented exactly. The continuous atom is still inactive at \(m=T\), whereas \(e_{T+1}(T)\) has the positive old-node value
\[
 \alpha_{T+1}\sqrt T[1-r_{T+1}\sqrt T].
\]
The normalized surplus is
\[
 a(s)q_{T+1}(s)
 \sqrt T[1-r_{T+1}\sqrt T]
\]
at node \(T\).

Consequently
\[
\boxed{
\begin{aligned}
 C(m)={}&
 \sqrt m[r_m\sqrt m-1]
 \int_m^{s_{m+1}}
 \lambda(s)a(s)q_m(s)\,ds\\
 &+\sqrt m[1-r_{m+1}\sqrt m]
 \int_{s_m}^{m}
 \lambda(s)a(s)q_{m+1}(s)\,ds,
\end{aligned}}
\tag{L-91111.1}
\]
with absent/out-of-support integrals interpreted as zero.

Every factor is nonnegative. Hence
\[
\boxed{
 C(m)\ge0
 \qquad\text{for every }m.
}
\tag{L-91111.2}

The martingale quadrature error is therefore a positive boundary seed, not an indefinite discretization error.

## 3. Pointwise decay

Assume
\[
 0\le\lambda(s)\le M.
\]
The endpoint-state bounds give
\[
 \sqrt m[r_m\sqrt m-1]
 <\frac1{\sqrt{m-1}},
\tag{L-91111.3}
\]
\[
 \sqrt m[1-r_{m+1}\sqrt m]
 <\frac1{\sqrt m}.
\tag{L-91111.4}

Moreover \(q_U\le1\), the integration lengths are at most one, and
\[
 a(s)=2/s.
\]
Therefore, for \(m\ge3\),
\[
\begin{aligned}
 C(m)
 &\le
 \frac{2M}{m\sqrt{m-1}}
 +\frac{2M}{(m-1)\sqrt m}\\
 &<\frac{4M}{(m-1)^{3/2}}.
\end{aligned}
\tag{L-91111.5}

Thus
\[
\boxed{
 0\le C(m)<4M(m-1)^{-3/2}.
}
\tag{L-91111.6}

On the factor-\(54.2\) equality window, `X-91102` verifies
\[
 L(x)<1.83<2.
\]
Hence the equality-density collar satisfies
\[
\boxed{
 C(m)<8(m-1)^{-3/2}.
}
\tag{L-91111.7}

## 4. Support localization

If \(\lambda\) is supported on
\[
 K+2\le s\le X-1,
\]
then (L-91111.1) gives
\[
\boxed{
 \operatorname{supp}C\subseteq[K+1,X-1]\cap\mathbb Z.
}
\tag{L-91111.8}

Thus the collar seed is both positive and confined to the outer endpoint annulus.

## 5. Ordinary carry bound

For a nonnegative seed \(C\),
\[
 |v_q(C)|
 \le\sum_{k\ge1}[C(kq)+C(kq+1)].
\tag{L-91111.9}

For \(m\ge4\), (L-91111.7) implies the simpler bound
\[
 C(m)<16m^{-3/2}.
\tag{L-91111.10}

Using
\[
 \sum_{k\ge M}k^{-3/2}\le3M^{-1/2},
\]
and the support restriction \(m\ge K\), a two-case estimate according as \(q\le K\) or \(q>K\) gives
\[
\boxed{
 |v_q(C)|<\frac{128}{q\sqrt K}
 \qquad(K\ge4).
}
\tag{L-91111.11}

The constant is deliberately loose; no optimization is needed.

## 6. Radix-four detail bound

Let
\[
 \mathcal D_4v_q(C)=v_q(C)-2v_{4q}(C).
\]
Equation (L-91111.11) gives
\[
\begin{aligned}
 |\mathcal D_4v_q(C)|
 &\le\frac{128}{q\sqrt K}
 +2\frac{128}{4q\sqrt K}\\
 &<\frac{200}{q\sqrt K}.
\end{aligned}
\]
Therefore
\[
\boxed{
 |\mathcal D_4v_q(C)|
 <\frac{200}{q\sqrt K}.
}
\tag{L-91111.12}

For an interior detail column \(4q\le X\),
\[
 \Omega_X(q)=\frac{\log4}{\sqrt q}.
\]
Hence
\[
\boxed{
 \frac{|\mathcal D_4v_q(C)|}{\Omega_X(q)}
 <\frac{103}{\sqrt K}
 \qquad(q\ge2).
}
\tag{L-91111.13}

Thus multiplying the quantized outer producer by
\[
 1-\frac{103}{\sqrt K}
\]
is more than sufficient to pay the **quantization collar alone** on every interior radix-four column, once \(K>103^2\).

Since \(K\asymp X\) in the reset, the required safety loss is \(O(X^{-1/2})\). The outer producer score is \(O(\sqrt X)\), so this safety factor costs only \(O(1)\) score per generation.

## 7. What remains separate

The estimate above pays only the B-spline quantization collar. Two effects remain to be combined with it:

1. the exact finite target-versus-continuum equality error;
2. the terminal detail annulus \(q>X/4\), where \(\Omega_X(q)\) tapers to zero.

Both are independent of the martingale quantization and have finite quotient depth. They are the remaining local terms in the reset gate of `T-91101`.

## 8. Proof boundary

Closed exactly, subject to review:

1. the explicit collar formula;
2. coefficientwise positivity;
3. \(m^{-3/2}\) decay;
4. outer-annulus support;
5. ordinary carry bound;
6. radix-four detail bound;
7. \(O(X^{-1/2})\) safety factor and \(O(1)\) score cost for the collar.

Still open:

1. the exact finite equality-target mismatch in carry coordinates;
2. terminal-annulus repair;
3. recombination with the parity shadow and inner residual;
4. RH.
