# L-32423 — The adaptive root-of-unity current bank has only two Fourier modes

Claim ID: `L-32423`  
Title: Arbitrarily many radix-four source channels separate the positive Selberg forcing without increasing the dimension of the RH-sensitive inverse-zeta current; after channel Fourier transform only the principal and one delayed detail mode survive  
Status: **PROPOSED COMPLETE EXACT SOURCE/CURRENT LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: `L-32421`; elementary differentiation of Dirichlet sources  
Scope: finite root-of-unity source bank and its physical current; no RH conclusion

## 1. Source bank

Let

\[
 B_0(s)=\frac1{\zeta(s)},
 \qquad
 a(s)=4^{1-s},
 \qquad
 L=\log4.
\]

For an integer `M>=2` and every `M`th root of unity `omega`, define

\[
\boxed{
 B_\omega(s)=(1-\omega a(s))B_0(s).
}
\tag{L-32423.1}

This is the same finite source bank as `L-32421`.

Write

\[
 q_0=B_0',
 \qquad
 q_\omega=B_\omega'.
\]

In coefficient notation these are the source-convolved logarithmic currents `q=-b log`.

## 2. Exact current decomposition

Since

\[
 a'(s)=-La(s),
\]

differentiating (L-32423.1) gives

\[
\begin{aligned}
 q_\omega
 &=(1-\omega a)q_0+L\omega a B_0\\
 &=\boxed{
 q_0+\omega a\bigl(LB_0-q_0\bigr).
 }
\end{aligned}
\tag{L-32423.2}

Thus the dependence on the channel phase is exactly affine. No higher root-of-unity harmonic occurs in the inverse-source current even though the generalized-prime logarithmic derivative of the separate system contains the complete local four-adic tower.

## 3. Channel Fourier transform

Use normalized discrete Fourier coefficients

\[
 \widehat q_k
 =\frac1M\sum_{\omega^M=1}\omega^{-k}q_\omega,
 \qquad0\le k<M.
\]

Root-of-unity orthogonality and (L-32423.2) give

\[
\boxed{
 \widehat q_0=q_0,
 \qquad
 \widehat q_1=a(LB_0-q_0),
 \qquad
 \widehat q_k=0\quad(2\le k<M).
}
\tag{L-32423.3}

Likewise the bare source itself has only two channel modes:

\[
\boxed{
 \widehat B_0=B_0,
 \qquad
 \widehat B_1=-aB_0,
 \qquad
 \widehat B_k=0\quad(k\ge2).
}
\tag{L-32423.4}

Therefore increasing the channel count to separate arbitrarily many local generalized-prime levels introduces **no new inverse-zeta current species**.

## 4. Exact Parseval current frame

Channel Parseval gives, pointwise on every vertical line,

\[
\boxed{
 \frac1M\sum_{\omega^M=1}|q_\omega|^2
 =|q_0|^2+|a|^2|LB_0-q_0|^2.
}
\tag{L-32423.5}

On the critical line `Re(s)=1/2`,

\[
 |a|=2,
\]

so

\[
\boxed{
 \frac1M\sum_\omega|q_\omega|^2
 =|q_0|^2+4|LB_0-q_0|^2.
}
\tag{L-32423.6}

The first term is the principal RH-sensitive logarithmic-derivative current. The second is one strict radix-four delay of the same current plus the bare inverse-zeta gauge.

## 5. Physical carry localization

Multiply every channel by the common atomized carry factor `zeta(s)N_theta(s)`. Then

\[
 \zeta B_0N_\theta=N_\theta
\]

is deterministic, while

\[
 \zeta q_0N_\theta
 =-\frac{\zeta'}\zeta N_\theta
\]

is the ordinary RH-sensitive pole current.

Consequently the nonprincipal Fourier mode becomes

\[
\boxed{
 a(s)\left[LN_\theta(s)
 -\left(-\frac{\zeta'}\zeta(s)N_\theta(s)\right)\right].
}
\tag{L-32423.7}

In physical logarithmic coordinates multiplication by `a(s)=4^{1-s}` is translation by exactly `log4` with critical amplitude two. Hence the complete multichannel bank consists of

```text
current Fourier mode 0:
    current-scale ordinary reciprocal-zeta pole field;

current Fourier mode 1:
    one log(4)-delayed copy of
      (deterministic carry field - ordinary pole field);

all higher current modes:
    identically zero.
```

No fractional collar is introduced on `log4`-aligned blocks.

## 6. Compatibility with the separated reserve

`L-32421` shows that, when `M` exceeds twice the active four-adic depth, the generalized-prime/Selberg side has as many nonnegative Fourier channels as are needed to separate every local level. `L-32422` then proves the complete Hermitian reserve of that adaptive bank grows by at least sixteen under one radix-four dilation.

The current side, by contrast, remains two-dimensional by (L-32423.3). Thus the endpoint-adaptive construction achieves

```text
arbitrarily fine positive forcing separation;
critical frame constant independent of M;
reserve storage factor >=16;
RH-sensitive current dimension exactly 2.
```

This removes channel proliferation as a possible obstruction to the final reflected recurrence.

## 7. Proof boundary

Closed exactly:

1. affine phase dependence of every source-convolved current;
2. two-mode DFT support for both bare source and current;
3. exact channel Parseval identity;
4. critical-line frame formula;
5. physical interpretation as one principal mode plus one strict radix-four delayed detail;
6. compatibility with the adaptive separated reserve.

Still open:

1. a no-double-spend reflected inequality paying the delayed detail from the newly created reserve while carrying the principal mode with coefficient one;
2. the resulting global recurrence;
3. RH.
