# L-34001 — The entire Q=4 Jordan physical deformation is the exact atomized carry transform

Claim ID: `L-34001`  
Title: Prefix localization of a divisor-summed source equals its atomized carry transform; hence every Q=4 Jordan physical jet is exactly the corresponding carry jet, and the product curvature cancels the inverse-source curvature in the augmented reserve  
Status: **PROPOSED COMPLETE EXACT ALGEBRA / CALCULUS — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro-09-v`  
Created: 2026-08-09  
Parent: PR #339  
Dependencies: PR #339 `L-33802`; PR #337 `L-32711`; elementary finite divisor switching  
Scope: exact real-X physical/carry identification and curvature bookkeeping; no RH-scale current bound or RH conclusion

## 1. A general prefix/carry identity

Let `f` be any finitely supported arithmetic sequence, or any sequence for which the finite sums below are defined, and put

\[
 c=\mathbf 1*f,
 \qquad
 C_c(X)=\sum_{m\le X}c(m)
 \qquad(X\ge0),
\]

where `1(n)=1`. For real `X>=0` and `0<=theta<=1`, define the centered prefix defect

\[
 \mathcal Q_c(X,\theta)
 =C_c(X)-C_c(\theta X)-C_c((1-\theta)X).
\tag{L-34001.1}
\]

Also put

\[
 \mathcal C(x,\theta)
 =\lfloor x\rfloor-\lfloor\theta x\rfloor-\lfloor(1-\theta)x\rfloor
 \in\{0,1\}.
\tag{L-34001.2}
\]

Then

\[
 \boxed{
 \mathcal Q_c(X,\theta)
 =\sum_{d\le X}f(d)\,
   \mathcal C(X/d,\theta).
 }
\tag{L-34001.3}
\]

### Proof

Finite divisor switching gives

\[
 C_c(Y)
 =\sum_{m\le Y}\sum_{d\mid m}f(d)
 =\sum_{d\le Y}f(d)\left\lfloor\frac Yd\right\rfloor.
\]

Apply this at `Y=X,theta X,(1-theta)X` and subtract. The result is exactly (L-34001.3). No limiting argument or source relabeling is involved.

For an integer split `X=n`, `theta=j/n`, equation (L-34001.3) reduces to

\[
 \boxed{
 \mathcal Q_c(n,j/n)
 =\sum_{d\le n}f(d)\chi_{n,d}(j),
 }
\tag{L-34001.4}
\]

where

\[
 \chi_{n,d}(j)
 =\left\lfloor\frac nd\right\rfloor
  -\left\lfloor\frac jd\right\rfloor
  -\left\lfloor\frac{n-j}{d}\right\rfloor.
\]

Thus ordinary prefix localization and atomized carry localization are literally the same operation whenever the physical coefficient is `1*f`.

## 2. Apply the identity to the complete Q=4 Jordan family

Retain the Q=4 Euler--Blaschke system

\[
 B_4=A_4^{-1},
 \qquad
 J_{4,\tau}(s)=\frac{A_4(s-\tau)}{A_4(s)},
 \qquad \tau\ge0,
\]

and define the source-convolved deformation of `L-33802`

\[
 K_{4,\tau}=b_4*J_{4,\tau}.
\tag{L-34001.5}
\]

Because

\[
 \mathbf1*b_4=e_4,
\]

associativity gives the exact identity

\[
 \boxed{
 c_{4,\tau}:=e_4*J_{4,\tau}
 =\mathbf1*K_{4,\tau}.
 }
\tag{L-34001.6}
\]

Let

\[
 G_{4,\tau}(X)=\sum_{m\le X}c_{4,\tau}(m)
\]

and define the full real-X Jordan physical field

\[
 \mathcal Q_{4,\tau}(X,\theta)
 =G_{4,\tau}(X)
  -G_{4,\tau}(\theta X)
  -G_{4,\tau}((1-\theta)X).
\tag{L-34001.7}
\]

Equation (L-34001.3) yields

\[
 \boxed{
 \mathcal Q_{4,\tau}(X,\theta)
 =\sum_{d\le X}K_{4,\tau}(d)
   \mathcal C(X/d,\theta).
 }
\tag{L-34001.8}
\]

This is the exact atomized carry transform of the *same* source-convolved Jordan state. It holds for every real `X`, every carry position `theta`, and every `tau` for which the finite coefficients are evaluated.

Consequently the previously separate objects

```text
physical prefix field;
atomized carry field;
Jordan source deformation
```

are one finite object in different notation.

## 3. All first three physical jets are the carry jets of L-32711

From `L-33802`,

\[
 K_{4,0}=b_4,
 \qquad
 K'_{4,0}=q_4=b_4*\Lambda_4,
 \qquad
 K''_{4,0}=t_4=b_4*C_4.
\tag{L-34001.9}
\]

Differentiate the finite sum (L-34001.8) coefficientwise at `tau=0`. Put

\[
 Y_X(\theta)=\sum_{d\le X}b_4(d)\mathcal C(X/d,\theta),
\]

\[
 Q_X(\theta)=\sum_{d\le X}q_4(d)\mathcal C(X/d,\theta),
\]

\[
 T_X(\theta)=\sum_{d\le X}t_4(d)\mathcal C(X/d,\theta).
\]

Then exactly

\[
 \boxed{
 \mathcal Q_{4,0}=Y_X,
 \qquad
 \partial_\tau\mathcal Q_{4,\tau}|_0=Q_X,
 \qquad
 \partial_\tau^2\mathcal Q_{4,\tau}|_0=T_X.
 }
\tag{L-34001.10}
\]

At an integer split `(n,j)`, these are precisely the carry-row quantities

\[
 Y_e=\mathcal L_e(b_4),
 \qquad
 Q_e=\mathcal L_e(q_4),
 \qquad
 T_e=\mathcal L_e(t_4)
\]

of `L-32711`.

In particular, since `c_4=e_4*Lambda_4=1*q_4`, the corrected true physical current of PR #325 is exactly

\[
 \boxed{
 Q_4^{\rm phys}(n,j)=Q_e.
 }
\tag{L-34001.11}
\]

This removes the last typing distinction between the true prefix current and the augmented-reserve carry current.

## 4. Exact physical Jordan energy is an atomized carry Gram

Fix any carry-position interval `I subset (0,1)` and a real `X`. Define

\[
 \mathscr E_X(\tau)
 =\int_I|\mathcal Q_{4,\tau}(X,\theta)|^2\,d\theta.
\tag{L-34001.12}
\]

Let

\[
 \mathsf G_X(d,e)
 =\int_I
 \mathcal C(X/d,\theta)
 \mathcal C(X/e,\theta)\,d\theta.
\tag{L-34001.13}
\]

Then (L-34001.8) gives the exact finite Gram identity

\[
 \boxed{
 \mathscr E_X(\tau)
 =\sum_{d,e\le X}
 K_{4,\tau}(d)\overline{K_{4,\tau}(e)}
 \mathsf G_X(d,e).
 }
\tag{L-34001.14}
\]

The matrix `G_X` is positive semidefinite because it is literally a Gram matrix of the carry windows. Thus no physical-to-carry transference map remains for the complete Jordan family: the physical energy *is* its carry Gram.

## 5. Exact curvature identity

For real coefficients, or with real parts inserted in the complex case, differentiate (L-34001.12):

\[
 \boxed{
 \frac12\mathscr E_X''(0)
 =\int_I\left(|Q_X(\theta)|^2
 +\operatorname{Re}(\overline{Y_X(\theta)}T_X(\theta))\right)d\theta.
 }
\tag{L-34001.15}

At one integer row `e=(n,j)`, the pointwise version is

\[
 \boxed{
 \frac12\frac{d^2}{d\tau^2}
 |\mathcal Q_{4,\tau}(n,j/n)|^2\Big|_{\tau=0}
 =Q_e^2+Y_eT_e.
 }
\tag{L-34001.16}

This is exactly the product-source curvature of `L-33802`, now in the same row coordinate as the augmented reserve.

## 6. Curvature--reserve cancellation

`L-32711` defines

\[
 \mathcal A_e
 =\mathcal R_e+Q_e^2-Y_eT_e,
 \qquad
 \mathcal R_e=P_e^2-S_e.
\tag{L-34001.17}

Adding (L-34001.16) gives the exact cancellation

\[
 \boxed{
 \mathcal A_e
 +\frac12\frac{d^2}{d\tau^2}
 |\mathcal Q_{4,\tau}(n,j/n)|^2\Big|_{0}
 =\mathcal R_e+2Q_e^2.
 }
\tag{L-34001.18}

The potentially dangerous inverse-source second-current term `Y_eT_e` disappears identically. Thus the product-source Jordan curvature and the source-complete augmented Kummer reserve are complementary pieces of one exact ledger.

After integration over any carry-position interval the same identity holds with the corresponding row/position integrals.

Equation (L-34001.18) is a no-double-spend statement: a future reflected proof must not separately charge `Y T` after combining these two objects, because it has already canceled algebraically.

## 7. What remains after the exact identification

The source-placement problem is closed by (L-34001.8)--(L-34001.14). The second-current/bare-source cross term is closed algebraically by (L-34001.18).

The conclusion-producing quantity which remains is the first-current square

\[
 |Q_X(\theta)|^2,
\]

or its integrated block version. A theorem of the form

\[
 \int_I|Q_X(\theta)|^2d\theta
 \le C\int_I S_4(X,\theta)d\theta
\]

with a scale-independent constant would be RH-strength in this source because the current retains every off-line zeta pole. It is **not** inferred here from the positive Gram or from finite scans.

Accordingly, this lemma does not claim the discovery-only inequality of PR #339.

## 8. Proof boundary

Closed exactly, subject to independent review:

1. general prefix/carry identity for `c=1*f`;
2. entire Q=4 Jordan physical/carry identification for all real `X,theta,tau`;
3. exact identification of the true physical current with `Q_e` from `L-32711`;
4. exact finite Gram representation of the physical Jordan energy;
5. first and second jet identities;
6. exact curvature--augmented-reserve cancellation (L-34001.18).

Still open:

1. an RH-scale estimate for the first-current square;
2. a coefficient-one neutral block recurrence or another conclusion-producing estimate;
3. RH.
