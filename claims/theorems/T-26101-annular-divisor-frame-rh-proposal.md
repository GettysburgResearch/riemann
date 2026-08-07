# T-26101 — Full elementary RH proposal by annular divisor-gradient projection

Claim ID: `T-26101`  
Title: The parabolic carry seed, the annular dual frame, and the square-screw transfer imply the Riemann Hypothesis  
Status: **FULL ELEMENTARY PROPOSAL — `ADF` OPEN; RH UNPROVED**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Issue: #261  
Base: PR #254 at `be8405e543957ae64ddd10965e9d709e38beb5ff`  
Depends on: PR #248 `L-24501/L-24502/T-24501`; PR #254 `R-25301/L-25301`; `L-26101`--`L-26108`

## 1. Exact finite front door

For prime powers `q=p^a<=X`, let

\[
 w_X(q)=q^{-1/2}\log(X/q)
\]

and consider the exact divisor-gradient LP

\[
\begin{aligned}
 \text{maximize }&J_X(b)=\sum_{m=2}^{X}b_m\log\frac m{m-1},\\
 \text{subject to }&b_m\ge0,\\
 &v_q(b)=\sum_{kq\le X}(b_{kq}-b_{kq+1})\le w_X(q).
\end{aligned}
\tag{T-26101.1}
\]

The von-Mangoldt vector is an exact dual solution, and every feasible `b` gives

\[
\boxed{
 \sum_{q=p^a\le X}
 \frac{\Lambda(q)}{\sqrt q}\log\frac Xq
 \ge J_X(b).
}
\tag{T-26101.2}
\]

No prime asymptotic is used in this finite implication.

## 2. Sharp explicit seed and closed source budget

Use the parabolic seed

\[
 b_X^{(0)}(m)
 =2\sqrt m\left[
  \log(X/m)-2(1-\sqrt{m/X})
 \right].
 \tag{T-26101.3}
\]

PR #248 proves

\[
 b_X^{(0)}(m)\ge0
\]

and

\[
\boxed{
 J_X(b_X^{(0)})
 \ge4\sqrt X-O(\log X).
}
\tag{T-26101.4}
\]

PR #254 proves that the seed is not close to feasible after positive parts are separated: its positive and negative von-Mangoldt weighted constraint masses are both of order at least `sqrt(X)`. The monotone cover therefore loses a fixed square-root amount and is rejected.

`L-26104` proves

\[
\boxed{
 \|(r_X)_+\|_2\ll\log^{3/2}(2X).
}
\tag{T-26101.5}
\]

Thus the initial source budget is closed by elementary calculus.

## 3. Canonical annular repair radius

Use the enlarged canonical annulus from `L-26108`:

\[
 I_X=
 \left[\left\lceil\frac X5\right\rceil,
       \left\lfloor\frac{4X}{5}\right\rfloor\right].
 \tag{T-26101.6}
\]

For prime powers `q<=X` and `j in I_X`, put

\[
 A_X(q,j)
 =2\mathbf1_{q\mid j}
 -\mathbf1_{q\mid j-1}
 -\mathbf1_{q\mid j+1}.
 \tag{T-26101.7}
\]

Let

\[
 r_X(q)=v_q(b_X^{(0)})-w_X(q).
\]

The minimum annular repair norm is

\[
 \mathcal R_X
 =\inf\{\|F\|_2:A_XF\ge r_X\}.
 \tag{T-26101.8}
\]

`L-26105` proves the exact Hilbert--Farkas formula

\[
\boxed{
 \mathcal R_X
 =\sup_{\substack{\lambda\ge0\\A_X^*\lambda\ne0}}
 \frac{\langle\lambda,r_X\rangle_+}
      {\|A_X^*\lambda\|_2}.
}
\tag{T-26101.9}
\]

Thus the sole finite arithmetic theorem can be stated without an existence gap.

## 4. Annular Dual Frame theorem (`ADF`)

For every nonnegative prime-power vector `lambda`, prove

\[
\boxed{
 \left(
  \sum_{q=p^a\le X}\lambda_qr_X(q)
 \right)_+
 \le X^{o(1)}
 \left[
  \sum_{j\in I_X}
  \left(
   2\sum_{q\mid j}\lambda_q
   -\sum_{q\mid j-1}\lambda_q
   -\sum_{q\mid j+1}\lambda_q
  \right)^2
 \right]^{1/2}.
}
\tag{ADF}
\]

By (T-26101.9), `ADF` is exactly equivalent to

\[
\boxed{
 \mathcal R_X=X^{o(1)}.
}
\tag{T-26101.10}
\]

The projected-dual recursion of `L-26106` is a globally monotone primal producer for this optimum. The older per-half-step positive-residual contraction has been withdrawn and is not part of the theorem.

## 5. Additive-rigidity decomposition of the hinge

For

\[
 L_\lambda(n)=\sum_{p^a\mid n}\lambda_{p^a},
\]

one has

\[
 (A_X^*\lambda)_j
 =2L_\lambda(j)-L_\lambda(j-1)-L_\lambda(j+1).
 \tag{T-26101.11}
\]

Thus the denominator is the second-difference energy of an additive arithmetic function.

`L-26107` proves exact dyadic and triadic gap identities and the quantitative estimate

\[
 \sum_{m\in I_X}
 |L_\lambda(m)-L_\lambda(m-1)|^2
 \ll X^2\|A_X^*\lambda\|_2^2.
 \tag{T-26101.12}
\]

The classical Erdős--Kátai--Wirsing logarithm-rigidity theory, and its quantitative modern descendants, suggest the proof decomposition

\[
 \lambda=c\Lambda+\lambda^\perp.
 \tag{T-26101.13}
\]

The transverse component should be controlled by annular curvature, while the scalar logarithmic component is handled by the signed factor-two recurrence inherited from PR #254. Establishing these two estimates would prove `ADF`.

## 6. Feasible sharp carry vector

Assume `ADF`, and choose a flow `F_X` with

\[
 A_XF_X\ge r_X,
 \qquad
 \|F_X\|_2=X^{o(1)}.
 \tag{T-26101.14}
\]

Define

\[
 b_X(m)=b_X^{(0)}(m)+F_X(m-1)-F_X(m).
 \tag{T-26101.15}
\]

By `L-26102/L-26108`, for all sufficiently large `X`,

\[
 b_X(m)\ge0
\]

and every prime-power constraint is feasible. Moreover,

\[
\boxed{
 J_X(b_X)
 \ge4\sqrt X-X^{o(1)}.
}
\tag{T-26101.16}
\]

The objective correction is actually `X^{-3/2+o(1)}`.

## 7. Sharp prime-ramp lower bound

Combining (T-26101.2) and (T-26101.16),

\[
\boxed{
 \sum_{q=p^a\le X}
 \frac{\Lambda(q)}{\sqrt q}\log\frac Xq
 \ge4\sqrt X-X^{o(1)}.
}
\tag{T-26101.17}
\]

This is the complete prime-power ramp, with all exponents and no omitted endpoint.

## 8. Square-screw transfer

At `X=N^2`, use the exact square-screw identity frozen in the carry/square-screw stack:

\[
 \Psi(2\log N)
 =4(N+N^{-1}-2)
 -\sum_{q=p^a\le N^2}
  \frac{\Lambda(q)}{\sqrt q}
  \log\frac{N^2}{q}
 +O(\log N).
 \tag{T-26101.18}
\]

Equation (T-26101.17) gives

\[
\boxed{
 \Psi(2\log N)\le N^{o(1)}.
}
\tag{T-26101.19}
\]

The unconditional derivative budget propagates this estimate between adjacent square samples. The upper-envelope Landau one-sign theorem excludes every pole corresponding to a zeta zero with real part greater than `1/2`. Functional-equation symmetry gives

\[
\boxed{\mathrm{RH}.}
\tag{T-26101.20}
\]

The square-screw normalization, interpolation, and Landau orientation remain inherited dependencies and must be reviewed at their frozen commits.

## 9. Mandatory logarithmic near-null firewall

For

\[
 \lambda_q=\Lambda(q),
\]

one has exactly

\[
 (A_X^*\Lambda)_j
 =\log\frac{j^2}{j^2-1}
\]

and

\[
 \langle\Lambda,r_X\rangle
 =J_X(b_X^{(0)})
 -\sum_{q=p^a\le X}
  \frac{\Lambda(q)}{\sqrt q}\log\frac Xq.
\]

Thus the von-Mangoldt vector is an arithmetic near-null direction whose numerator is the sharp prime-ramp deficit itself. `ADF` cannot follow from a generic frame lower bound or entrywise absolute estimate. A proof must preserve this signed scalar mode.

## 10. Full proposed spine

```text
average binomial carries
-> exact second-difference divisor-gradient LP
-> parabolic seed with 4 sqrt(X)-O(log X) objective
-> exact positive/negative constraint dipole
-> polylog initial positive-residual norm
-> exact annular Hilbert-Farkas duality
-> dyadic/triadic additive-gap rigidity
-> transverse additive rigidity + logarithmic scalar recurrence
-> Annular Dual Frame inequality
-> subpower-norm feasible flow
-> sharp prime-ramp lower bound
-> square-screw upper envelope
-> Landau pole exclusion
-> RH.
```

## 11. Exact proof boundary

```text
finite carry/divisor-gradient algebra       inherited / proposed exact
parabolic seed and sharp objective          inherited / proposed complete
monotone positive cover                     refuted
constraint dipole                           inherited / proposed complete
initial residual L2 budget                  proposed complete
annular slack/cost and enlargement          proposed complete
Hilbert-Farkas primal/dual equivalence       proposed complete
projected-dual monotone potential            proposed complete
dyadic/triadic gap rigidity                 proposed complete
transverse coefficient rigidity             OPEN
logarithmic factor-two recurrence            OPEN
Annular Dual Frame inequality               OPEN / RH-BEARING
ADF -> sharp prime ramp                      proposed complete
sharp prime ramp -> RH                       inherited conditional transfer
Riemann Hypothesis                           UNPROVED
```

This is a full elementary proposal with one exact source-specific inequality and a concrete two-part proof plan. It is not a claim that `ADF` or RH has already been proved.