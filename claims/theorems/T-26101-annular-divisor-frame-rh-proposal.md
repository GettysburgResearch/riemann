# T-26101 — Full elementary RH proposal by annular divisor-gradient projection

Claim ID: `T-26101`  
Title: The parabolic carry seed, the annular dual frame, and the square-screw transfer imply the Riemann Hypothesis  
Status: **FULL ELEMENTARY PROPOSAL — `ADF` OPEN; RH UNPROVED**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Issue: #261  
Base: PR #254 at `be8405e543957ae64ddd10965e9d709e38beb5ff`  
Depends on: PR #248 `L-24501/L-24502/T-24501`; PR #254 `R-25301/L-25301`; `L-26101`--`L-26105`

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

`L-26104` proves the pointwise source estimate and its Euclidean consequence

\[
\boxed{
 \|(r_X)_+\|_2\ll\log^{3/2}(2X).
}
\tag{T-26101.5}
\]

Thus the initial source budget is closed unconditionally.

## 3. Exact annular repair radius

Fix

\[
 I_X=[\lceil9X/20\rceil,\lfloor4X/5\rfloor]
\]

and

\[
 A_X(q,j)
 =2\mathbf1_{q\mid j}
 -\mathbf1_{q\mid j-1}
 -\mathbf1_{q\mid j+1}.
 \tag{T-26101.6}
\]

Let

\[
 r_X(q)=v_q(b_X^{(0)})-w_X(q).
\]

The minimum annular repair norm is

\[
 \mathcal R_X
 =\inf\{\|F\|_2:A_XF\ge r_X\}.
 \tag{T-26101.7}

`L-26105` proves the exact dual formula

\[
\boxed{
 \mathcal R_X
 =\sup_{\substack{\lambda\ge0\\A_X^*\lambda\ne0}}
 \frac{\langle\lambda,r_X\rangle_+}
      {\|A_X^*\lambda\|_2}.
}
\tag{T-26101.8}

Thus the sole finite arithmetic theorem may be stated without an existence gap.

## 4. Annular Dual Frame theorem (`ADF`)

Prove, for every nonnegative prime-power vector `lambda`,

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

By (T-26101.8), `ADF` is equivalent to

\[
\boxed{
 \mathcal R_X=X^{o(1)}.
}
\tag{T-26101.9}

The source-specific active projection and `SAF2/SAF3` of `L-26103` are a proposed constructive proof of `ADF`; they are not additional hypotheses once `ADF` is established.

## 5. Feasible sharp carry vector

Assume `ADF`, and choose an annular flow `F_X` with

\[
 A_XF_X\ge r_X,
 \qquad
 \|F_X\|_2=X^{o(1)}.
 \tag{T-26101.10}

Define

\[
 b_X(m)=b_X^{(0)}(m)+F_X(m-1)-F_X(m).
 \tag{T-26101.11}

By `L-26102`, for all sufficiently large `X`,

\[
 b_X(m)\ge0
\]

and every prime-power constraint is feasible. Moreover,

\[
\boxed{
 J_X(b_X)
 \ge4\sqrt X-X^{o(1)}.
}
\tag{T-26101.12}

The objective correction is actually `X^{-3/2+o(1)}`.

## 6. Sharp prime-ramp lower bound

Combining (T-26101.2) and (T-26101.12),

\[
\boxed{
 \sum_{q=p^a\le X}
 \frac{\Lambda(q)}{\sqrt q}\log\frac Xq
 \ge4\sqrt X-X^{o(1)}.
}
\tag{T-26101.13}

This is the complete prime-power ramp, with all exponents and no omitted endpoint.

## 7. Square-screw transfer

At `X=N^2`, use the exact square-screw identity frozen in the carry/square-screw stack:

\[
 \Psi(2\log N)
 =4(N+N^{-1}-2)
 -\sum_{q=p^a\le N^2}
  \frac{\Lambda(q)}{\sqrt q}
  \log\frac{N^2}{q}
 +O(\log N).
 \tag{T-26101.14}

Equation (T-26101.13) gives

\[
\boxed{
 \Psi(2\log N)\le N^{o(1)}.
}
\tag{T-26101.15}

The unconditional derivative budget propagates this estimate between adjacent square samples. The upper-envelope Landau one-sign theorem excludes every pole corresponding to a zeta zero with real part greater than `1/2`. Functional-equation symmetry gives

\[
\boxed{\mathrm{RH}.}
\tag{T-26101.16}

The square-screw normalization, interpolation, and Landau orientation remain inherited dependencies and must be reviewed at their frozen commits.

## 8. Mandatory near-null firewall

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

Thus the von-Mangoldt vector is an arithmetic near-null direction whose numerator is the sharp prime-ramp deficit itself. `ADF` cannot follow from a generic frame lower bound or entrywise absolute estimate. A proof must use the source sign and show that every other nonnegative near-null vector is controlled by the same negative-slack mechanism.

## 9. Full proposed spine

```text
average binomial carries
-> exact second-difference divisor-gradient LP
-> parabolic seed with 4 sqrt(X)-O(log X) objective
-> exact positive/negative constraint dipole
-> polylog initial positive-residual norm
-> exact annular Hilbert-Farkas duality
-> Annular Dual Frame inequality
-> subpower-norm feasible flow
-> sharp prime-ramp lower bound
-> square-screw upper envelope
-> Landau pole exclusion
-> RH.
```

## 10. Exact proof boundary

```text
finite carry/divisor-gradient algebra       inherited / proposed exact
parabolic seed and sharp objective          inherited / proposed complete
monotone positive cover                     refuted
constraint dipole                           inherited / proposed complete
initial residual L2 budget                  proposed complete
annular slack/cost transfer                  proposed complete
Hilbert-Farkas primal/dual equivalence       proposed complete
Annular Dual Frame inequality               OPEN / RH-BEARING
SAF2/SAF3 constructive route to ADF          OPEN
ADF -> sharp prime ramp                      proposed complete
sharp prime ramp -> RH                       inherited conditional transfer
Riemann Hypothesis                           UNPROVED
```

This is a full elementary proposal with one exact source-specific inequality. It is not a claim that `ADF` or RH has already been proved.