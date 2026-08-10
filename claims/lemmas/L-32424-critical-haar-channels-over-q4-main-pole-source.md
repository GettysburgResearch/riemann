# L-32424 — Critical-Haar root-of-unity channels over the Q=4 main-pole source

Claim ID: `L-32424`  
Title: A finite critical-Haar root-of-unity bank over the Q=4 Euler–Blaschke source preserves main-pole cancellation, separates every active dyadic generalized-prime level into nonnegative Fourier channels, and leaves only two inverse-zeta current modes  
Status: **PROPOSED COMPLETE EXACT SOURCE/FRAME THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: `L-32404`, `L-32405`, `L-32421`, `L-32423`  
Scope: finite endpoint-adaptive source frame; no RH conclusion

## 1. Hybrid source family

Retain the Q=4 Euler–Blaschke source

\[
 B_4(s)=\frac{E_4(s)}{\zeta(s)},
 \qquad
 E_4(s)=\frac{1-4^{1-s}}{1-4^{-s}},
\]

with inverse `A_4=B_4^{-1}`, generalized-prime sequence `Lambda_4>=0`, and strict balanced reserve `R_4` from `L-32405`.

Put

\[
 u(s)=\sqrt2\,2^{-s},
 \qquad
 \ell=\log2.
\]

For an integer `M>=2` and every `M`th root of unity `omega`, define

\[
\boxed{
 B_{4,\omega}(s)=(1-\omega u(s))B_4(s).
}
\tag{L-32424.1}

Its inverse is

\[
 A_{4,\omega}(s)=\frac{A_4(s)}{1-\omega u(s)}.
\]

Individual channel coefficients may be complex when `omega` is nonreal; positivity is asserted only after the exact finite Fourier orthogonalization below.

## 2. Analytic pole geometry

At `s=1`, the common factor `B_4` has the zero which removes the deterministic zeta pole in the physical Q=4 current. The factor `1-omega u(s)` is analytic and finite there.

If `rho` is a nontrivial zeta zero, then `B_4` has the corresponding pole structure described in `L-32404`; multiplication by a finite local factor cannot create a new pole away from the declared local zero set. For an endpoint-adaptive bank one may always retain the complete family rather than divide by an individual channel zero. The DFT principal channel below is exactly the original Q=4 system, so every off-line zeta pole remains explicitly present in the bank.

On the critical line `s=1/2+it`,

\[
 |u(s)|=1.
\]

Thus root-of-unity averaging gives the constant critical analysis frame

\[
\boxed{
 \frac1M\sum_{\omega^M=1}|1-\omega u|^2
 =1+|u|^2=2.
}
\tag{L-32424.2}

The frame constant is independent of the channel count.

## 3. Generalized-prime Fourier channels

The logarithmic derivative of the inverse system is

\[
\begin{aligned}
 L_{4,\omega}(s)
 &:=-\frac{A_{4,\omega}'}{A_{4,\omega}}(s)\\
 &=L_4(s)
   +\ell\frac{\omega u(s)}{1-\omega u(s)}\\
 &=L_4(s)+\ell\sum_{r\ge1}\omega^r u(s)^r
\end{aligned}
\tag{L-32424.3}

initially in the absolute local-Euler domain and then coefficientwise as a formal Dirichlet identity.

Take normalized channel DFTs. Channel zero is exactly the positive Q=4 generalized-prime sequence `Lambda_4`. For `1<=k<M`, the `k`th channel is supported on dyadic powers with exponent `r congruent k mod M` and coefficient

\[
\boxed{
 \ell(\sqrt2)^r>0
 \qquad\text{at }2^r.
}
\tag{L-32424.4}

Every orthogonalized generalized-prime channel is therefore coefficientwise nonnegative.

## 4. Exact finite separation of the complete Selberg forcing

Fix an endpoint `n` and put

\[
 R_2=\lfloor\log_2n\rfloor.
\]

Assume

\[
\boxed{M>2R_2.}
\tag{L-32424.5}

Then every active dyadic exponent `1<=r<=R_2` occupies a distinct nonzero Fourier channel, and no two active nonzero channel indices add to zero modulo `M`.

Consequently, after averaging the separate-system Selberg sources over `omega`, all mixed terms between `Lambda_4` and the new critical-Haar tower disappear from channel zero, and all local-local convolution terms also disappear from channel zero. The complete averaged Selberg forcing is exactly the original Q=4 forcing

\[
\boxed{
 C_4=\Lambda_4\log+\Lambda_4*\Lambda_4.
}
\tag{L-32424.6}

The averaged first-moment Hermitian energy is

\[
\boxed{
 P_4(n,j)^2
 +\sum_{2^r\le n}\ell^2 2^r\,\chi_{n,2^r}(j).
}
\tag{L-32424.7}

Hence the endpoint-adaptive hybrid reserve is

\[
\boxed{
 R_{4,M}^{\rm Haar}(n,j)
 =R_4(n,j)
 +\sum_{2^r\le n}\ell^2 2^r\,\chi_{n,2^r}(j)
 \ge R_4(n,j)>0
}
\tag{L-32424.8}

on every quarter-balanced row where `R_4` is positive.

No mixed new local arithmetic remains after channel separation.

## 5. The inverse-zeta current still has only two channel modes

Let

\[
 q_4=B_4',
 \qquad
 q_{4,\omega}=B_{4,\omega}'.
\]

Since `u'=-ell u`, differentiating (L-32424.1) gives

\[
\boxed{
 q_{4,\omega}
 =q_4+\omega u(\ell B_4-q_4).
}
\tag{L-32424.9}

Therefore the normalized channel DFT satisfies

\[
\boxed{
 \widehat q_0=q_4,
 \qquad
 \widehat q_1=u(\ell B_4-q_4),
 \qquad
 \widehat q_k=0\quad(k\ge2).
}
\tag{L-32424.10}

Channel Parseval yields, on the critical line,

\[
\boxed{
 \frac1M\sum_\omega|q_{4,\omega}|^2
 =|q_4|^2+|\ell B_4-q_4|^2.
}
\tag{L-32424.11}

Thus arbitrarily fine forcing separation does not proliferate the RH-sensitive current state.

## 6. Physical localization

After multiplication by the common atomized carry factor `zeta(s)N_theta(s)`, the principal mode `q_4` is the Q=4 RH-sensitive pole current. The bare `B_4` leg becomes the deterministic Q=4 bare carry field `E_4(s)N_theta(s)`, already controlled in the live Q=4 branches.

Multiplication by `u(s)=sqrt(2)2^{-s}` is an exact delay `log2` with unit critical amplitude. Hence the only nonprincipal current mode is one **strict dyadic predecessor state** of

```text
(deteministic Q=4 bare field - Q=4 pole current).
```

There are no higher current modes and no fractional collars on `log2`-aligned blocks.

## 7. Consequence for the live proof architecture

The hybrid bank simultaneously has

```text
Q=4 main-pole removal and off-line-pole retention;
critical frame constant 2 independent of M;
positive DFT generalized-prime channels;
all new dyadic mixed Selberg terms removed at finite endpoint;
strict Q=4 reserve retained and enlarged by local squares;
RH-sensitive current dimension exactly 2;
nonprincipal current state delayed by one log2 block.
```

This offers a cleaner direct-sum coordinate for the final reflected no-double-spend theorem: the complete arithmetic forcing may be made diagonal without changing the dimension of the principal current recurrence.

The theorem does not itself bound the delayed current mode. That inequality remains RH-bearing.

## 8. Proof boundary

Closed exactly:

1. hybrid source construction;
2. constant critical root-of-unity frame;
3. nonnegative DFT generalized-prime channels;
4. exact finite elimination of every new mixed Selberg term;
5. explicit enlarged reserve;
6. exact two-mode current DFT;
7. physical interpretation as principal Q=4 current plus one dyadic predecessor detail.

Still open:

1. source-convolved reflected no-double-spend control of the delayed detail by newly created reserve;
2. coefficient-one recurrence;
3. RH.
