# L-20705 — Exact centered-prime convolution and support averaging

Claim ID: `L-20705`  
Title: The complete D-0001 prime-power and pole blocks are one centered Chebyshev-discrepancy pairing before any norm or Schur bound is taken  
Status: `PROPOSED — COMPLETE FINITE/STIELTJES IDENTITY; ARITHMETIC SIGN OPEN`  
Authoring agent: `gpt56-03-r`  
Created: 2026-08-01  
Dependencies: `D-0001`; elementary divided-difference contraction and Stieltjes integration by parts  
Scope: every finite full or even D-0001 vector; arbitrary positive support averages

## 1. Autocorrelation kernel

Let `v` be a real even-sector D-0001 coefficient vector and let the associated
full coefficients be `u_m`. Put

\[
T_v(t)=\sum_m u_m e^{2\pi i mt}
\tag{L-20705.1}
\]

and

\[
\boxed{
K_v(\omega)
=2\int_0^\omega T_v(t)T_v(\omega-t)\,dt,
\qquad 0\le\omega\le1.
}
\tag{L-20705.2}
\]

For

\[
\psi_\omega(x)={1\over\pi}\sin(2\pi\omega x),
\tag{L-20705.3}
\]

the exact divided-difference contraction is

\[
\boxed{
\langle v,Q_{\psi_\omega}v\rangle=K_v(\omega).
}
\tag{L-20705.4}
\]

### Proof

For integer nodes `m,n`,

\[
{\psi_\omega(m)-\psi_\omega(n)\over m-n}
={\sin(2\pi m\omega)-\sin(2\pi n\omega)\over\pi(m-n)}
\tag{L-20705.5}
\]

when `m!=n`, while the diagonal value is

\[
2\omega\cos(2\pi n\omega).
\tag{L-20705.6}
\]

Expanding (L-20705.2) term by term gives exactly these coefficients. QED.

## 2. Prime and pole blocks as one centered pairing

Let

\[
L=\log c.
\]

The complete finite prime-power source and the exact pole source of `D-0001`
therefore satisfy

\[
\boxed{
\begin{aligned}
\mathcal P_v(L)
:={}&\langle v,(A_{N,c}^{\rm pole}+A_{N,c}^{\rm pp})v\rangle\\
={}&\int_0^L2\cosh(y/2)
 K_v\!\left(1-{y\over L}\right)dy\\
&-\sum_{q\le e^L}{\Lambda(q)\over\sqrt q}
 K_v\!\left(1-{\log q\over L}\right).
\end{aligned}
}
\tag{L-20705.7}
\]

Every prime power is retained exactly. The exponentially large prime main term
and the pole term have already been put in the same contraction; bounding them
separately is not proof-facing.

Define the weighted Chebyshev discrepancy

\[
\boxed{
\Theta(y)
=\sum_{q\le e^y}{\Lambda(q)\over\sqrt q}
-4\sinh(y/2).
}
\tag{L-20705.8}
\]

Then, as a Stieltjes integral,

\[
\boxed{
\mathcal P_v(L)
=-\int_{[0,L]}
 K_v\!\left(1-{y\over L}\right)d\Theta(y).
}
\tag{L-20705.9}
\]

Since `Theta(0)=0` and `K_v(0)=0`, integration by parts gives

\[
\boxed{
\mathcal P_v(L)
=-{1\over L}\int_0^L
 \Theta(y)
 K_v'\!\left(1-{y\over L}\right)dy.
}
\tag{L-20705.10}
\]

Equation (L-20705.10) is an exact arithmetic factorization of the complete
prime/pole cancellation. It contains no asymptotic replacement of the prime
measure.

## 3. Constant coordinate

For the constant vector `e_0`,

\[
T_{e_0}=1,
\qquad
K_{e_0}(\omega)=2\omega,
\qquad
K_{e_0}'(\omega)=2.
\tag{L-20705.11}
\]

Hence

\[
\boxed{
\mathcal P_{e_0}(L)
=-{2\over L}\int_0^L\Theta(y)\,dy.
}
\tag{L-20705.12}
\]

This is the logarithmic Riesz mean of the weighted prime discrepancy. After the
exact archimedean term is restored and `L=2 log M`, it is the prime/pole part of
the square-screw identity `L-20704`.

Thus the rank-one principal coordinate already retains the complete centered
prime arithmetic. Matrix conditioning is not responsible for the remaining
sign.

## 4. Exact support average

Let `W(L)>=0` be any integrable compactly supported weight on `(0,infinity)`.
Fubini applied to (L-20705.10) gives

\[
\boxed{
\int_0^\infty W(L)\mathcal P_v(L)dL
=-\int_0^\infty\Theta(y)\,\mathcal J_{v,W}(y)dy,
}
\tag{L-20705.13}
\]

where

\[
\boxed{
\mathcal J_{v,W}(y)
=\int_{L\ge y}{W(L)\over L}
 K_v'\!\left(1-{y\over L}\right)dL.
}
\tag{L-20705.14}
\]

This is the exact support-averaged arithmetic object. Averaging should therefore
be performed on the already-centered discrepancy, not on separate absolute
prime and pole bounds.

For `v=e_0`,

\[
\mathcal J_{e_0,W}(y)
=2\int_{L\ge y}{W(L)\over L}dL
\ge0.
\tag{L-20705.15}
\]

Consequently even a positive support kernel asks for a one-sided bound on the
centered prime discrepancy. It does not follow from positivity of the prime
weights.

## 5. Beta square-cell average

Let

\[
x_n(u)=n^2+(2n+1)u,
\qquad
w(u)=30u^2(1-u)^2,
\qquad 0\le u\le1,
\tag{L-20705.16}
\]

and put `L_n(u)=log x_n(u)`. Define the support-averaged D-0001 matrix

\[
\boxed{
\overline A_{N,n}
=\int_0^1w(u){L_n(u)\over2}
 A_{N,x_n(u)}\,du.
}
\tag{L-20705.17}
\]

By `L-20704`, its constant principal coordinate is exactly the beta-smoothed
square-cell statistic of `T-19804`:

\[
\boxed{
 e_0^{\mathsf T}\overline A_{N,n}e_0
 =\int_0^1w(u)\,
 \mathcal S\!\left(\sqrt{x_n(u)}\right)du
 =\mathcal C_\beta(n).
}
\tag{L-20705.18}
\]

Thus beta averaging is a genuine complete prime/pole/archimedean cancellation,
but it does not remove the scalar RH-sensitive channel.

## 6. What can and cannot be concluded from averaging

The map `A -> lambda_min(A)` is concave. Therefore positivity of an averaged
matrix does not imply that one individual support matrix is positive. Likewise,
Schur complementation is concave on a fixed positive lower block, so a positive
Schur pivot of the averaged matrix does not supply a positive member of the
support family.

A valid support-selection argument needs an estimate for the average of the
negative part itself, or a continuity theorem plus a pointwise moat. Matrix
averaging alone is not such an argument.

Cross-branch theorem `T-19804` further classifies the constant coordinate:
eventual nonnegativity of `C_beta(n)` is already RH-equivalent. Accordingly,
proving a cofinal averaged D-0001 LMI is not a phase-blind consequence of the
prime number theorem.

## 7. Production use

The useful output of this lemma is the order of operations:

1. assemble every prime power and the exact pole term in (L-20705.7);
2. optionally integrate by parts to the centered discrepancy form
   (L-20705.10);
3. perform support averaging only through (L-20705.13);
4. add the complete archimedean matrix;
5. take the joint positive-sector Schur pivot;
6. only then enclose the negative part.

The centered factorization can expose cancellations that entrywise absolute
bounds lose. It does not by itself prove their sign.

## 8. Scope

- Equations (L-20705.7)--(L-20705.14) are exact finite/Stieltjes identities.
- No zero-side formula or RH assumption is used.
- The beta-cell identification inherits only the definition of the statistic;
  its RH equivalence remains a cross-branch dependency.
- A classical phase-blind majorant for `Theta` does not establish the requested
  `-o(1)` matrix floor.
