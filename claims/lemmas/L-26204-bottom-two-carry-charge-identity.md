# L-26204 — The dyadic dipole sees only the bottom two carry coefficients

Claim ID: `L-26204`  
Title: The compact opposite-parity source annihilates every carry row above three and turns the RH-bearing Riesz mean into one fixed bottom-charge functional  
Status: **PROPOSED EXACT FINITE ALGEBRA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-source-specific`  
Created: 2026-08-08  
Dependencies: `L-26201`; PR #269 `L-26201`--`L-26203`; the finite carry matrix of PR #244  
Scope: exact source compression and finite triangular algebra; no sign estimate or RH conclusion

## 1. The two dyadic sources

Retain the Euler-aligned source

\[
 b_2(n)=\mu(n)-\mathbf 1_{2\mid n}\mu(n/2)
\tag{L-26204.1}
\]

and the compact dipole source of `L-26201`

\[
 \omega_2(n)
 =\mu(n)-\frac32\mathbf 1_{2\mid n}\mu(n/2)
 +\frac12\mathbf 1_{4\mid n}\mu(n/4).
\tag{L-26204.2}
\]

They satisfy the exact source filter

\[
 \boxed{
 \omega_2
 =
 b_2-\frac12\,\delta_2*b_2.
 }
\tag{L-26204.3}
\]

Equivalently,

\[
 \sum_{n\ge1}\frac{\omega_2(n)}{n^s}
 =
 \frac{(1-2^{-s})(1-2^{-s-1})}{\zeta(s)}.
\tag{L-26204.4}
\]

Neither Euler factor vanishes at a zeta zero in the open critical strip.

## 2. Compact carry image

For the finite carry matrix

\[
 \beta_{nq}
 =
 \frac{\lfloor n/q\rfloor\,[q-1-(n\bmod q)]}{n+1},
 \qquad 2\le q\le n,
\tag{L-26204.5}
\]

define

\[
 K_{\omega}(n)
 =
 \sum_{q=2}^{n}\omega_2(q)\beta_{nq}.
\tag{L-26204.6}
\]

The compact dipole formula of `L-26201`, specialized to its base scale `m=1`, gives

\[
 \boxed{
 K_{\omega}(n)
 =
 \begin{cases}
 -5/6,&n=2,\\
 -1/2,&n=3,\\
 0,&n\ge4.
 \end{cases}}
\tag{L-26204.7}
\]

Thus the complete infinite inverse-zeta source is invisible to every carry row above three. This is an exact source identity, not a bounded-rank assertion: the high-rank same-sign Möbius families remain present in the coefficient `omega_2`, but their carry image cancels against their actual `2`-adic siblings.

## 3. The exact triangular inverse

For an integer endpoint `X>=3`, put

\[
 w_X(q)=q^{-1/2}\log(X/q),
 \qquad 2\le q\le X.
\tag{L-26204.8}
\]

Because

\[
 \beta_{qq}=\frac{q-1}{q+1}>0,
\]

there is a unique real vector `c_X(2),...,c_X(X)` satisfying

\[
 \boxed{
 w_X(q)=\sum_{n=q}^{X}c_X(n)\beta_{nq}
 \qquad(2\le q\le X).
 }
\tag{L-26204.9}
\]

No sign is assumed. This is the exact Carry Saturation inverse before its positivity question is asked.

Define the compact dyadic Riesz coordinate

\[
 \boxed{
 \mathcal R_{\omega}(X)
 =
 \sum_{q=2}^{X}
 \frac{\omega_2(q)}{\sqrt q}\log(X/q).
 }
\tag{L-26204.10}
\]

Pairing (L-26204.9) with `omega_2(q)`, interchanging the finite sums, and using (L-26204.7) yields

\[
 \boxed{
 \mathcal R_{\omega}(X)
 =
 -\frac56c_X(2)-\frac12c_X(3).
 }
\tag{L-26204.11}
\]

Equivalently,

\[
 \boxed{
 5c_X(2)+3c_X(3)
 =
 -6\mathcal R_{\omega}(X).
 }
\tag{L-26204.12}
\]

Every coefficient `c_X(n)` for `n>=4` disappears from the final functional. Full Carry Saturation is therefore much stronger than what this source needs.

## 4. Exact relation to the two-contact source

Let

\[
 \widetilde{\mathcal R}_{2}(X)
 =
 \sum_{q\le X}\frac{b_2(q)}{\sqrt q}\log(X/q),
\tag{L-26204.13}
\]

including the `q=1` term. Then (L-26204.3) gives the stable dyadic identity

\[
 \boxed{
 \widetilde{\mathcal R}_{\omega}(X)
 =
 \widetilde{\mathcal R}_{2}(X)
 -
 2^{-3/2}\widetilde{\mathcal R}_{2}(X/2).
 }
\tag{L-26204.14}
\]

Thus the compact dipole is the first strict dyadic difference of PR #269's two-contact Riesz source. It retains the same rightmost-zero exponent but has a finite carry image.

In the full-divisor Green coordinate of PR #269,

\[
 \overline G_Xb_2=-3e_2+e_3.
\]

Equation (L-26204.7) is the corresponding averaged-carry statement: after one additional stable dyadic difference, the source is supported on the same fixed bottom boundary.

## 5. Why this is a narrower proof target

Any one of the following implies

\[
 \mathcal R_{\omega}(X)\le0:
\]

1. `c_X(2)>=0` and `c_X(3)>=0`;
2. the weaker single inequality
   \[
   \boxed{5c_X(2)+3c_X(3)\ge0;}
   \tag{L-26204.15}
   \]
3. a source-specific reflected identity whose residual is precisely the left side of (L-26204.15).

The first condition is only the bottom two entries of Carry Saturation. The second permits either entry to be negative and is strictly weaker still.

A proposed proof must not infer (L-26204.15) from finite numerical positivity, from generic Hankel positivity, from bounded source rank, or from a carry flow supported above index three. PR #269 proves that high-index adjacent transport is exactly invisible to the underlying dyadic scalar.

## 6. Exact regression

`X-26202-bottom-charge` verifies with rational and formal arithmetic:

- the filter identity (L-26204.3);
- the compact carry image (L-26204.7);
- the formal triangular inverse through a symbolic endpoint;
- the identity (L-26204.12) coefficient by coefficient;
- mutations deleting or changing a `2`-adic sibling.

The regression proves no sign.

## 7. Proof boundary

Closed exactly:

- the dyadic source filter;
- the compact two-row carry image;
- the unique finite inverse interface;
- the bottom-charge/Riesz identity;
- the stable relation to the PR #269 two-contact source.

Open:

- eventual nonnegativity of `5c_X(2)+3c_X(3)`;
- a source-specific proof of that inequality;
- RH.
