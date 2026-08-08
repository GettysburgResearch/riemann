# L-27604 — Continuum–discrete commutator boundary

Claim ID: `L-27604`  
Title: The pole-preserving averaged-carry commutator equals a finite factor-five carry scalar plus one explicit dyadic prime-density boundary tending to `3/8`  
Status: **PROPOSED COMPLETE EXACT FINITE/ASYMPTOTIC LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-08`  
Created: 2026-08-08  
Dependencies: `L-27601`--`L-27603`; PR #252 `L-24502`; PR #269 pointwise `omega_2` wavelets; the prime number theorem only for the final `3/8` limit  
Scope: exact scalar physical-to-carry source map; no subpower carry estimate and no RH conclusion

## 1. Continuum and discrete commutators

Fix an integer `X>=5`. Let

\[
 b_X(q)=b(X/q)
\]

be the continuum carry coefficient and let

\[
 \beta_{Xq}
 =\frac{\lfloor X/q\rfloor
 [q-1-(X\bmod q)]}{X+1}
\]

be the discrete average-binomial carry coefficient.

For a completely additive formal logarithm `ell`, define

\[
\boxed{
 \mathcal R_X^{\rm cont}
 =\sum_{q\le X}
  \omega_2(q)[\ell(X)-\ell(q)]b_X(q),
}
\tag{L-27604.1}
\]

and

\[
\boxed{
 \mathcal R_X^{\rm disc}
 =\sum_{q\le X}
  \omega_2(q)[\ell(X)-\ell(q)]\beta_{Xq}.
}
\tag{L-27604.2}
\]

The continuum term is the scaled top-quarter commutator of `L-27602`.

## 2. Exact one-row discretization formula

Write

\[
 X=qk+r,
 \qquad0\le r<q.
\]

The comparison of PR #252 simplifies to

\[
\boxed{
 b_X(q)-\beta_{Xq}
 =\frac{qk(k+1)}{X(X+1)}.
}
\tag{L-27604.3}
\]

Indeed `X+q-r=q(k+1)` in the formula of `L-24502`.

Therefore

\[
\begin{aligned}
 \mathcal R_X^{\rm cont}-\mathcal R_X^{\rm disc}
 =\frac{2}{X(X+1)}
 \sum_{n\le X}n
 \sum_{q\mid n}\omega_2(q)
 [\ell(X)-\ell(q)].
\end{aligned}
\tag{L-27604.4}

## 3. The divisor collapse

Put

\[
 e=\mathbf1*\omega_2
 =\varepsilon-\frac32\delta_2+rac12\delta_4.
\tag{L-27604.5}
\]

Let `Lambda_ell` be the generalized von Mangoldt sequence associated with `ell`:

\[
 \Lambda_\ell(p^a)=\ell(p),
 \qquad
 \Lambda_\ell(n)=0
 \quad\text{otherwise}.
\tag{L-27604.6}
\]

Since

\[
 \ell=\mathbf1*\Lambda_\ell,
\]

one has

\[
\boxed{
 \sum_{q\mid n}\omega_2(q)
 [\ell(X)-\ell(q)]
 =\ell(X/n)e(n)+(e*\Lambda_\ell)(n).
}
\tag{L-27604.7}
\]

The first term is supported only at `n=1,2,4`, and its weighted sum is

\[
 \sum_{n\le X}n\ell(X/n)e(n)=-\ell(2).
\tag{L-27604.8}
\]

Define

\[
 B_\ell(Y)=\sum_{n\le Y}n\Lambda_\ell(n).
\tag{L-27604.9}
\]

The second term gives

\[
 \sum_{n\le X}n(e*\Lambda_\ell)(n)
 =B_\ell(X)-3B_\ell(X/2)+2B_\ell(X/4),
\tag{L-27604.10}
\]

with the floor convention in every endpoint.

Combining the displays proves the exact boundary identity

\[
\boxed{
\begin{aligned}
 \mathcal R_X^{\rm cont}-\mathcal R_X^{\rm disc}
 =\frac{2}{X(X+1)}\Bigl[&
 B_\ell(X)-3B_\ell(X/2)\\
 &+2B_\ell(X/4)-\ell(2)
 \Bigr].
\end{aligned}}
\tag{L-27604.11}
\]

## 4. Natural logarithm and the constant boundary mass

For `ell=log`, `Lambda_ell=Lambda` and the prime number theorem gives

\[
 B_{\log}(X)=\frac{X^2}{2}+o(X^2).
\]

Consequently

\[
\boxed{
 \mathcal R_X^{\rm cont}-\mathcal R_X^{\rm disc}
 =\frac38+o(1).
}
\tag{L-27604.12}
\]

The physical and discrete commutators therefore have the same polynomial growth exponent and the same local subpower criterion. The entire continuum/discretization boundary is an explicit bounded prime-density term; no unknown physical remainder remains at scalar level.

## 5. Exact factor-five carry representation

For `X>=4`, the averaged zeroth source row vanishes:

\[
 \sum_{q\le X}\omega_2(q)\beta_{Xq}=0.
\tag{L-27604.13}
\]

Hence

\[
 \mathcal R_X^{\rm disc}
 =-\sum_{q\le X}\omega_2(q)\ell(q)\beta_{Xq}.
\]

Differentiating the inverse identity

\[
 \omega_2*a_\omega=\varepsilon
\]

gives

\[
 \omega_2\ell=-\Lambda_\omega*\omega_2.
\tag{L-27604.14}
\]

Let

\[
 Z_{X,m}(j)
 =\sum_{k\le X/m}\omega_2(k)\chi_{X,mk}(j)
\]

be the pointwise factor-five wavelet of PR #269. Then

\[
\boxed{
 \mathcal R_X^{\rm disc}
 =\frac1{X+1}
  \sum_{j=0}^{X}
  \sum_{m\le X}\Lambda_\omega(m)Z_{X,m}(j).
}
\tag{L-27604.15}
\]

Every row with `X>=5m` has nonnegative logarithmic-Kummer coupling, while the wavelet itself is supported in the factor-four carry range. Thus the RH-sensitive physical commutator has now been mapped exactly to the declared factor-five carry source plus the explicit boundary (L-27604.11).

Equation (L-27604.15) does not prove a bound for this signed carry average. It identifies the exact scalar which a factor-five transition theorem must estimate.

## 6. Exact replay target

`X-27601` checks (L-27604.11) for every integer `5<=X<=160` with a formal completely additive logarithm. The identity is rejected after each of the three source-coefficient mutations.

## 7. Proof boundary

Closed exactly, subject to review:

- continuum/discrete row comparison;
- finite divisor collapse;
- explicit dyadic prime-density boundary;
- its `3/8` asymptotic under the PNT;
- exact factor-five carry representation of the discrete commutator.

Open:

- a subpower estimate for the discrete signed carry average in (L-27604.15);
- a local-energy recurrence using the carry Schur reserve;
- RH.
