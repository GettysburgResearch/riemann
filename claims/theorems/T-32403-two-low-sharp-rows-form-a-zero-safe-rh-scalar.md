# T-32403 — Two low SHARP rows form one zero-safe RH scalar

Claim ID: `T-32403`  
Title: A fixed positive combination of only the row-two and row-three square-root hinge inverse coefficients has a zero-safe reciprocal-zeta Mellin transform, so its eventual one-sidedness already implies RH  
Status: **PROPOSED COMPLETE CONDITIONAL THEOREM — q=1 NORMALIZATION CORRECTED; ONE-SIDEDNESS OPEN**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Corrected: 2026-08-09  
Dependencies: PR #329 `L-32301/L-32303`; Landau one-sign theorem  
Scope: exact low-row compression and RH implication; no proof of the sign

## 1. The two extreme dual rows

Use the average-carry matrix of PR #329 and the square-root hinge

\[
 h_T(q)=q^{-1/2}-T^{-1/2},
 \qquad2\le q\le T.
\]

Let `c_T(j)` be its triangular inverse and put

\[
\boxed{
 N_j(T)=j(j-1)c_T(j).
}
\tag{T-32403.1}
\]

The exact dual potential corresponding to row `j` is

\[
 F_j(n)=
 \begin{cases}
 0,&n<j,\\
 j(j+1),&n=j,\\
 2n,&n>j.
 \end{cases}
\tag{T-32403.2}
\]

PR #329's adjoint formula gives

\[
 N_j(T)=\sum_{2\le q\le T}b_j(q)h_T(q),
\tag{T-32403.3}
\]

where `b_j` is the unique divisor coefficient sequence of `F_j`.

## 2. Dirichlet symbols for `j=2,3`

Let

\[
 B_j(s)=\sum_{q\ge1}{b_j(q)\over q^s}.
\]

The first increments of `F_2` are

```text
0, 6, 0, 2, 2, 2, ...
```

from nodes `1,2,3,4,...`. Hence

\[
\boxed{
 B_2(s)
 =2+{-2+4\,2^{-s}-2\,3^{-s}\over\zeta(s)}.
}
\tag{T-32403.4}
\]

For `F_3` the increments are

```text
0, 0, 12, -4, 2, 2, 2, ...,
```

so

\[
\boxed{
 B_3(s)
 =2+{-2-2\,2^{-s}+10\,3^{-s}-6\,4^{-s}\over\zeta(s)}.
}
\tag{T-32403.5}
\]

Both identities are initial absolute-convergence identities followed by meromorphic continuation.

## 3. The five-to-one cancellation

Multiply (T-32403.4) by five and add (T-32403.5). The `3^{-s}` terms cancel exactly:

\[
\begin{aligned}
 5B_2(s)+B_3(s)
 &=12
 -6{2-3\,2^{-s}+4^{-s}\over\zeta(s)}\\
 &=12
 -6{(1-2^{-s})(2-2^{-s})\over\zeta(s)}.
\end{aligned}
\tag{T-32403.6}

Define

\[
\boxed{
 \omega=(\varepsilon-\delta_2)*(2\varepsilon-\delta_2)*\mu.
}
\tag{T-32403.7}
\]

Its Dirichlet series is

\[
 \Omega(s)={(1-2^{-s})(2-2^{-s})\over\zeta(s)},
\qquad \omega(1)=2.
\tag{T-32403.8}
\]

The combined coefficient at every carry column `q>=2` is exactly `-6 omega(q)`. Therefore

\[
\boxed{
 5N_2(T)+N_3(T)
 =-6\sum_{2\le q\le T}\omega(q)
 \left(q^{-1/2}-T^{-1/2}\right).
}
\tag{T-32403.9}

Since `N_2=2c_T(2)` and `N_3=6c_T(3)`, equivalently

\[
\boxed{
 5N_2+N_3=2[5c_T(2)+3c_T(3)].
}
\tag{T-32403.10}

Full SHARP implies positivity of this single scalar, but the converse is not required below.

## 4. Three-node divergence form survives the missing unit column

For the complete arithmetic sequence `omega`,

\[
 1*\omega=2\varepsilon-3\delta_2+\delta_4.
\]

Hence its full floor potential is

\[
 H_\omega(1)=2,
 \qquad
 H_\omega(2)=H_\omega(3)=-1,
 \qquad
 H_\omega(n)=0\quad(n\ge4).
\tag{T-32403.11}
\]

The carry system omits `q=1`. Removing the unit coefficient subtracts `2n` from this floor potential. Every exact carry divergence has size zero,

\[
 \sum_n n r_T(n)=0,
\]

so that affine correction pairs to zero. Consequently the finite carry pairing still obeys

\[
\boxed{
 \sum_{q\ge2}\omega(q)h_T(q)
 =2r_T(1)-r_T(2)-r_T(3).
}
\tag{T-32403.12}

Thus

\[
\boxed{
 5N_2(T)+N_3(T)
 =-6[2r_T(1)-r_T(2)-r_T(3)].
}
\tag{T-32403.13}

The three-node statement was therefore correct; only the Mellin normalization below needed the explicit omitted unit term.

## 5. Corrected Mellin transform

Put

\[
 D(T)=\sum_{2\le q\le T}\omega(q)
 \left(q^{-1/2}-T^{-1/2}\right).
\]

For each `q`,

\[
 \int_q^\infty
 \left(q^{-1/2}-T^{-1/2}\right)T^{-z-1}dT
 ={q^{-z-1/2}\over2z(z+1/2)}.
\]

Hence, initially in the absolute-convergence half-plane,

\[
\boxed{
 \int_1^\infty D(T)T^{-z-1}dT
 ={1\over2z(z+1/2)}
 \left[
 { (1-2^{-z-1/2})(2-2^{-z-1/2})
  \over\zeta(z+1/2)}-2
 \right].
}
\tag{T-32403.14}

The `-2` is exactly `-omega(1)`. It was omitted in the first version of this claim. It is entire in the open RH half-plane after multiplication by the elementary denominator and therefore changes none of the off-line pole conclusions.

The finite numerator factors have zeros only on

```text
1-2^(-z-1/2)=0  => Re z=-1/2;
2-2^(-z-1/2)=0  => Re z=-3/2.
```

Thus every zeta zero to the right of the critical line gives a genuine nonreal pole of (T-32403.14).

For positive real `z`, `zeta(z+1/2)` has no zero. Its pole at `z=1/2` makes the reciprocal term vanish, leaving the finite value `-2`. The factors `z` and `z+1/2` have no pole for `z>0`. Hence there is no positive-real singularity.

## 6. One scalar sign implies RH

Assume, for all sufficiently large endpoints `T`,

\[
\boxed{
 5c_T(2)+3c_T(3)\ge0.
}
\tag{T-32403.15}

By (T-32403.9)--(T-32403.10), this says `D(T)<=0` cofinally.

Use the continuous endpoint version of the finite hinge sum, or equivalently interpolate between consecutive integer endpoints; the interpolation correction has Mellin transform holomorphic across every positive-real candidate abscissa.

Then `-D(e^t)` is eventually nonnegative. If an off-line zero existed, (T-32403.14) would have a nonreal pole in `Re z>0`, forcing the nonnegative Laplace transform to have positive abscissa of convergence. Landau's one-sign theorem would then force a singularity at the corresponding positive real boundary point. Section 5 shows that no such positive-real singularity exists.

Therefore no zeta zero has real part greater than one half. Functional-equation symmetry gives

\[
\boxed{
 5c_T(2)+3c_T(3)\ge0\text{ cofinally}
 \Longrightarrow\mathrm{RH}.
}
\tag{T-32403.16}

The reverse eventual sign gives the same conclusion.

## 7. Significance

The full SHARP theorem asks for `T-2` nonnegative coefficients at every endpoint. For the RH consequence this is massively stronger than necessary. A single fixed scalar built only from rows two and three already has a zero-safe reciprocal-zeta symbol.

The elementary frontier may therefore be attacked as

\[
\boxed{
 5c_T(2)+3c_T(3)\ge0
}
\tag{T-32403.17}

rather than full triangular positivity.

## 8. Proof boundary

Closed exactly, subject to review:

- the row-two and row-three Dirichlet symbols;
- the five-to-one zero-safe cancellation;
- the omitted-unit normalization;
- the three-node divergence formula;
- the corrected Mellin transform and zero audit;
- the Landau implication from eventual one-sidedness to RH.

Open:

- proof of (T-32403.15);
- SHARP;
- RH.
