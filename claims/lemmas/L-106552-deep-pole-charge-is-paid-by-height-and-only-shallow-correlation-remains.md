# L-106552 — Deep companion charge is paid by height; only shallow correlation remains

Claim ID: `L-106552`  
Status: **PROVED EXACT FOR FINITE INNER FACTORS**  
Created: 2026-08-25  
Depends on: `L-106512`, `L-106551`, finite model-space factorization  
RH status: **not assumed**

Let a reduced finite endpoint all-pass symbol be

\[
U=\omega B_+\overline{B_-},
\]

where `B_+` and `B_-` are finite inner functions in the upper-half-plane
normalization. Let the zeros of `B_-` be `b_j=a_j+i y_j`, including
multiplicity, and put

\[
\mathfrak h_-(U)=\sum_j y_j.
\tag{L-106552.1}
\]

The exact adverse charge is

\[
\boxed{
\|H_U\|_{\mathcal S_2}^2
 =\operatorname{tr}
  \left(T_{B_+}^*P_{K_{B_-}}T_{B_+}\right).
}
\tag{L-106552.2}

## 1. Exact shallow/deep orthogonal split

Fix `eta>0` and factor

\[
B_-=B_{\le\eta}B_{>\eta},
\]

where the first factor contains exactly the zeros with `0<y_j<=eta` and the
second exactly those with `y_j>eta`. Scalar inner factors commute, and the
standard model-space decomposition is orthogonal:

\[
\boxed{
K_{B_-}
 =K_{B_{\le\eta}}
  \oplus B_{\le\eta}K_{B_{>\eta}}.
}
\tag{L-106552.3}

Let `Q_sh` and `Q_deep` be the two projections. Substitution in
(L-106552.2) gives the exact sum

\[
\boxed{
\|H_U\|_{\mathcal S_2}^2
 =\mathcal C_{\le\eta}(U)
  +\mathcal C_{>\eta}(U),
}
\tag{L-106552.4}

where

\[
\mathcal C_{\le\eta}(U)
 =\|Q_{\rm sh}T_{B_+}\|_{\mathcal S_2}^2,
\qquad
\mathcal C_{>\eta}(U)
 =\|Q_{\rm deep}T_{B_+}\|_{\mathcal S_2}^2.
\]

There is no cross term: the two model-space ranges are orthogonal.

## 2. Height pays every deep direction

Toeplitz multiplication by `B_+` is an isometry and each model-space
direction costs at most one. Therefore

\[
\mathcal C_{>\eta}(U)
 \le\deg B_{>\eta}.
\]

Every zero in `B_(>eta)` contributes more than `eta` to (L-106552.1), so

\[
\boxed{
\mathcal C_{>\eta}(U)
 \le\deg B_{>\eta}
 \le{\mathfrak h_-(U)\over\eta}.
}
\tag{L-106552.5}

Consequently

\[
\boxed{
\|H_U\|_{\mathcal S_2}^2
 \le
 \mathcal C_{\le\eta}(U)
 +{\mathfrak h_-(U)\over\eta}.
}
\tag{L-106552.6}

The shallow term is an explicit canonical-correlation defect. In the
normalized Cauchy-kernel bases of `L-106512`, it is the trace of the shallow
denominator identity minus the squared cross-Gram overlap with `B_+`, with all
confluent jets retained.

## 3. Cofinal consequence

Let `U_T` be a cofinal family and let `n_T` be its zero-count scale. If

\[
\mathfrak h_-(U_T)=o(n_T),
\tag{L-106552.7}
\]

choose, for example,

\[
\eta_T=
 \sqrt{\max\!\left({\mathfrak h_-(U_T)\over n_T},n_T^{-2}\right)}.
\]

Then `eta_T->0` and

\[
{\mathfrak h_-(U_T)\over\eta_T}=o(n_T).
\]

Hence

\[
\boxed{
\|H_{U_T}\|_{\mathcal S_2}^2
 \le
 \mathcal C_{\le\eta_T}(U_T)+o(n_T).
}
\tag{L-106552.8}

Thus every macroscopic or mesoscopic denominator pole is paid
unconditionally by first-moment height. The only possible power-sized adverse
charge is supported on a vanishing-height companion model space.

## 4. Xi interface

`L-106550` proves an `o(N)` height theorem for the literal Xi divisor, and
`L-106551` proves the exact finite derivative/companion transfer. Once the
cofinal endpoint localization `ENDLOC106550` identifies those finite objects
with the literal fifth-endpoint companion, (L-106552.8) applies with
`n_T=N(T,2T)`.

The remaining term is named `SHALLOWCORR106550`. The firewall `R-106550`
shows that it cannot be bounded from height mass alone.