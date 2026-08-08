# T-32403 — Two low SHARP rows form one zero-safe RH scalar

Claim ID: `T-32403`  
Title: A fixed positive combination of only the row-two and row-three square-root hinge inverse coefficients has a zero-safe reciprocal-zeta Mellin transform, so its eventual one-sidedness already implies RH  
Status: **PROPOSED COMPLETE CONDITIONAL THEOREM — ONE-SIDEDNESS OPEN**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
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

Indeed its normalized cumulative average makes one unit jump at row `j`, and PR #329's adjoint formula gives exactly

\[
 N_j(T)=\sum_{q\le T}b_j(q)h_T(q),
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

The constant coefficient `2` sits at Dirichlet index one and therefore does not contribute to (T-32403.3), whose target begins at `q=2`.

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

Thus if

\[
\boxed{
 \omega=(\varepsilon-\delta_2)*(2\varepsilon-\delta_2)*\mu,
}
\tag{T-32403.7}
\]

then, because the index-one term again does not pair with the hinge,

\[
\boxed{
 5N_2(T)+N_3(T)
 =-6\sum_{q\le T}\omega(q)
 \left(q^{-1/2}-T^{-1/2}\right).
}
\tag{T-32403.8}

Since `N_2=2c_T(2)` and `N_3=6c_T(3)`, equivalently

\[
\boxed{
 5N_2+N_3=2[5c_T(2)+3c_T(3)].
}
\tag{T-32403.9}

Full SHARP implies positivity of this single scalar, but the converse is not required below.

## 4. Three-node divergence form

Because

\[
 1*\omega=2\varepsilon-3\delta_2+\delta_4,
\]

the floor potential of `omega` is

\[
 H_\omega(1)=2,
 \qquad
 H_\omega(2)=H_\omega(3)=-1,
 \qquad
 H_\omega(n)=0\ (n\ge4).
\tag{T-32403.10}

Therefore for the exact hinge divergence `r_T`,

\[
\boxed{
 \sum_q\omega(q)h_T(q)
 =2r_T(1)-r_T(2)-r_T(3).
}
\tag{T-32403.11}

The zero-safe low-row scalar is thus only one three-node boundary charge:

\[
\boxed{
 5N_2(T)+N_3(T)
 =-6[2r_T(1)-r_T(2)-r_T(3)].
}
\tag{T-32403.12}

## 5. Mellin transform

For

\[
 D(T)=\sum_{q\le T}\omega(q)
 \left(q^{-1/2}-T^{-1/2}\right),
\]

a direct finite Fubini calculation gives, initially in the absolute-convergence half-plane,

\[
\begin{aligned}
 \int_1^\infty D(T)T^{-z-1}dT
 &={1\over2z(z+1/2)}
   \sum_q{\omega(q)\over q^{z+1/2}}\\
 &=\boxed{
 { (1-2^{-z-1/2})(2-2^{-z-1/2})
  \over
  2z(z+1/2)\zeta(z+1/2)}.}
\end{aligned}
\tag{T-32403.13}

The numerator is zero-free throughout `Re z>0`:

```text
1-2^(-z-1/2)=0  => Re z=-1/2;
2-2^(-z-1/2)=0  => Re z=-3/2.
```

Thus every zeta zero to the right of the critical line gives a genuine nonreal pole.

On the positive real axis, `zeta(z+1/2)` has no zero; its pole at `z=1/2` makes the reciprocal vanish. The elementary factors `z` and `z+1/2` give no positive-real singularity.

## 6. One scalar sign implies RH

Assume, for all sufficiently large integer endpoints `T`,

\[
\boxed{
 5c_T(2)+3c_T(3)\ge0.
}
\tag{T-32403.14}

By (T-32403.8)--(T-32403.9), this says `D(T)<=0` cofinally.

Use the standard piecewise-linear interpolation of the finite Riesz hinge scalar between consecutive integer endpoints. Its interpolation correction is compact/local at each knot and has a Mellin transform holomorphic across every positive-real candidate abscissa; equivalently one may formulate (T-32403.14) directly for the continuous endpoint version of the same finite sum.

Then `-D(e^t)` is eventually nonnegative. If an off-line zero existed, (T-32403.13) would have a nonreal pole in `Re z>0`, so the nonnegative Laplace transform would have positive abscissa of convergence. Landau's one-sign theorem forces a singularity at the corresponding positive real point, contradicting the positive-real audit above.

Therefore no zeta zero has real part greater than one half. Functional-equation symmetry gives

\[
\boxed{
 5c_T(2)+3c_T(3)\ge0\text{ cofinally}
 \Longrightarrow\mathrm{RH}.
}
\tag{T-32403.15}

The reverse eventual sign gives the same conclusion.

## 7. Significance

The full SHARP theorem asks for `T-2` nonnegative coefficients at every endpoint. For the RH consequence this is massively stronger than necessary. A single fixed scalar built only from rows two and three already has a zero-safe reciprocal-zeta symbol.

The new elementary frontier may therefore be attacked as

\[
\boxed{
 5c_T(2)+3c_T(3)\ge0
}
\tag{T-32403.16}

rather than full triangular positivity.

The finite numerator was not guessed from a zeta transform: it arose from an exact positive combination of the first two average-carry dual extreme rays.

## 8. Proof boundary

Closed exactly, subject to review:

- the row-two and row-three Dirichlet symbols;
- the five-to-one zero-safe cancellation;
- the three-node divergence formula;
- the Mellin transform and zero audit;
- the Landau implication from eventual one-sidedness to RH.

Open:

- proof of (T-32403.14);
- SHARP;
- RH.
