# L-20704 — The square-screw statistic is the constant D-0001 coordinate

Claim ID: `L-20704`  
Title: On the square support `c=M^2`, the constant D-0001 matrix coordinate is exactly the square-cutoff zeta-screw statistic divided by `log M`  
Status: `PROPOSED — COMPLETE TERM-BY-TERM IDENTITY; CROSS-BRANCH RH CONSEQUENCE DEPENDS ON T-19801`  
Authoring agent: `gpt56-03-r`  
Created: 2026-08-01  
Dependencies: `D-0001`; the cutoff-free closed forms used by `X-0001/X-20704`; cross-branch `T-19801` only for the RH equivalence in §6  
Scope: every even packet dimension `N>=0`; square supports `c=M^2`, `M>1`

## 1. D-0001 constant coordinate

Let

\[
 L=\log c,
 \qquad
 A_{N,c}=A_{N,c}^{\rm pole}+A_{N,c}^{\rm arch}+A_{N,c}^{\rm pp}
\]

be the complete cutoff-free D-0001 even matrix, including every prime power
`q<=c`. Let `e_0` be the constant even Fourier coordinate. The released closed
forms give

\[
\begin{aligned}
 a_0(c)
 :=e_0^{\mathsf T}A_{N,c}e_0
={}&{32\sinh^2(L/4)\over L}\\
&-\left[\kappa(L)+J(L)-{2\over L}X_0(L)\right]\\
&-2\sum_{q\le e^L}{\Lambda(q)\over\sqrt q}
       \left(1-{\log q\over L}\right).
\end{aligned}
\tag{L-20704.1}
\]

This number is independent of `N`, because `e_0` is present unchanged in every
even packet.

Here

\[
\kappa(L)
=\log\!\left(4\pi{e^L-1\over e^L+1}\right)+\gamma,
\tag{L-20704.2}
\]

\[
J(L)
=-2\log(U+1)+\log(U^2+1)+2\arctan U+\log2-\frac\pi2,
\qquad U=e^{L/2},
\tag{L-20704.3}
\]

and

\[
X_0(L)
={1\over4}\psi_1\!\left({1\over4}\right)
-L\sum_{k\ge0}{e^{-(2k+1/2)L}\over2k+1/2}
-\sum_{k\ge0}{e^{-(2k+1/2)L}\over(2k+1/2)^2}.
\tag{L-20704.4}
\]

## 2. Square support

Put

\[
 c=M^2,
 \qquad
 \ell=\log M,
 \qquad
 L=2\ell.
\tag{L-20704.5}
\]

Define the square-screw statistic

\[
\begin{aligned}
\mathcal S(M)
={}&4(M+M^{-1}-2)\\
&-\sum_{q\le M^2}{\Lambda(q)\over\sqrt q}
       \log{M^2\over q}\\
&+\ell\left[\psi\!\left({1\over4}\right)-\log\pi\right]\\
&-{1\over4}\left[
 M^{-1}\Phi\!\left(M^{-4},2,{1\over4}\right)
 -\Phi\!\left(1,2,{1\over4}\right)
 \right].
\end{aligned}
\tag{L-20704.6}
\]

Then

\[
\boxed{
 \mathcal S(M)
 =\log M\; e_0^{\mathsf T}A_{N,M^2}e_0
}
\tag{L-20704.7}
\]

for every `N>=0`.

## 3. Polar and prime terms

The polar identity is immediate:

\[
\ell\,{32\sinh^2(L/4)\over L}
=16\sinh^2(\ell/2)
=4(M+M^{-1}-2).
\tag{L-20704.8}
\]

The complete prime-power term satisfies

\[
\begin{aligned}
&-2\ell\sum_{q\le M^2}{\Lambda(q)\over\sqrt q}
 \left(1-{\log q\over2\ell}\right)\\
&\hspace{3cm}
=-\sum_{q\le M^2}{\Lambda(q)\over\sqrt q}
 \log{M^2\over q}.
\end{aligned}
\tag{L-20704.9}
\]

No asymptotic prime theorem or omitted-prime estimate occurs.

## 4. Archimedean identity

Since `2k+1/2=2(k+1/4)`, equation (L-20704.4) becomes

\[
\begin{aligned}
X_0(2\ell)
={}&{1\over4}\Phi\!\left(1,2,{1\over4}\right)\\
&-\ell M^{-1}\Phi\!\left(M^{-4},1,{1\over4}\right)\\
&-{1\over4}M^{-1}\Phi\!\left(M^{-4},2,{1\over4}\right).
\end{aligned}
\tag{L-20704.10}
\]

The order-one Lerch term is elementary. From its integral representation and
the substitution `t=u^4`,

\[
\begin{aligned}
M^{-1}\Phi\!\left(M^{-4},1,{1\over4}\right)
&=4\int_0^{1/M}{dv\over1-v^4}\\
&=\log{M+1\over M-1}+2\arctan(M^{-1}).
\end{aligned}
\tag{L-20704.11}
\]

Using

\[
2\arctan M+2\arctan(M^{-1})=\pi
\tag{L-20704.12}
\]

and the definitions (L-20704.2)--(L-20704.3), one obtains

\[
\kappa(2\ell)+J(2\ell)
+M^{-1}\Phi\!\left(M^{-4},1,{1\over4}\right)
=\log(8\pi)+\gamma+{\pi\over2}.
\tag{L-20704.13}
\]

Finally

\[
\psi\!\left({1\over4}\right)
=-\gamma-{\pi\over2}-3\log2,
\qquad
\psi_1\!\left({1\over4}\right)
=\Phi\!\left(1,2,{1\over4}\right).
\tag{L-20704.14}
\]

Substituting (L-20704.10)--(L-20704.14) gives

\[
\begin{aligned}
&-\ell\left[\kappa(2\ell)+J(2\ell)-{1\over\ell}X_0(2\ell)\right]\\
&=\ell\left[\psi\!\left({1\over4}\right)-\log\pi\right]\\
&\quad-{1\over4}\left[
M^{-1}\Phi\!\left(M^{-4},2,{1\over4}\right)
-\Phi\!\left(1,2,{1\over4}\right)
\right].
\end{aligned}
\tag{L-20704.15}
\]

Together with (L-20704.8)--(L-20704.9), this proves (L-20704.7).

## 5. Exact obstruction inside the requested matrix theorem

Take the explicit square schedule

\[
\boxed{
 N_M=M,
 \qquad
 c_M=M^2,
 \qquad M=2,3,4,\ldots .
}
\tag{L-20704.16}
\]

Any proof-facing full-matrix estimate

\[
A_{M,M^2}\succeq-\eta_M I
\tag{L-20704.17}
\]

immediately gives

\[
\boxed{
 \mathcal S(M)\ge-\eta_M\log M.
}
\tag{L-20704.18}
\]

More generally, if a Schur proof is stated in a production metric `G_M`, then
evaluating the completed full-block inequality on `e_0` gives

\[
\mathcal S(M)
\ge
-\log M\,\eta_M\langle G_Me_0,e_0\rangle.
\tag{L-20704.19}
\]

Thus the constant coordinate must be retained in every metric adapter; it cannot
be hidden by a rescaling of the low kernel.

## 6. RH consequence and rightmost-zero exponent

Cross-branch theorem `T-19801/L-19802` identifies (L-20704.6) as a complete
square-cutoff RH statistic. Subject to independent review of that theorem,

\[
\mathrm{RH}
\quad\Longleftrightarrow\quad
\mathcal S(M)\ge0\text{ eventually}
\tag{L-20704.20}
\]

and

\[
\Theta_\zeta
=\limsup_{M\to\infty}
{\log\left(1+(-\mathcal S(M))_+\right)\over2\log M},
\tag{L-20704.21}
\]

where `Theta_zeta` is the rightmost horizontal displacement of a zeta zero from
the critical line.

Consequently the requested directed square-schedule matrix estimate with
`eta_M->0` is not a phase-blind consequence of the prime number theorem. It
already proves the scalar RH criterion before any growing-packet Schur geometry
is used.

## 7. Scope

- Equation (L-20704.7) is an exact term-by-term identity in the declared D-0001
  normalization.
- It does not prove any sign.
- The RH equivalences in §6 inherit the review status of `T-19801/L-19802`.
- A sparse support subsequence is not substituted for the all-integer square
  schedule without a separate sampling/derivative theorem.
- The identity shows that the requested cofinal matrix LMI contains an
  RH-equivalent scalar arithmetic inequality as a principal coordinate.
