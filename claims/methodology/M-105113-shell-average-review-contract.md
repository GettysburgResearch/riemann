# M-105113 — Shell-average review contract

Claim ID: M-105113

Status: **PROPOSED REVIEW CONTRACT**

Created: 2026-08-23

Depends on: L-105113; T-105113; R-105113

RH status: **unproved**

## Purpose

This contract governs review of the buffered-selector shell-average packet.
It separates the exact finite identity from the manifest, selector-growth,
shell-estimate, and Xi cofinal debts.

## 1. Coordinate and orientation obligations

1. The rectangle convention must be

   \[
   \Omega_{T,\eta}
   =\{z:|\Re z|<T,\ |\Im z|<\eta\}.
   \]

2. The vertical shell must be

   \[
   T_0<|\Re z|<T_1,
   \qquad
   |\Im z|<\eta_1,
   \]

   and the horizontal shell must be

   \[
   |\Re z|<T_1,
   \qquad
   \eta_0<|\Im z|<\eta_1.
   \]

3. The vertical shell is divided by
   \(\Delta_T=T_1-T_0\); the horizontal shell is divided by
   \(\Delta_\eta=\eta_1-\eta_0\).  Interchanging these factors is a
   blocking error.

4. Every \(q_H\) must be typed as the unnormalized integral

   \[
   q_H=\oint_{\partial\Omega_{T,\eta}}H(z)\,dz.
   \]

   Thus \(q_1=-2\pi iA_0\) and \(q_2=2\pi iB_0\).  Dropping \(2\pi\), or
   silently redefining \(q_H\) as a normalized charge, is a blocking error.

5. The signed area identity must retain \(+i\operatorname{sgn}(x)\) on the
   vertical shell and \(-\operatorname{sgn}(y)\) on the horizontal shell.

## 2. Manifest and selector obligations

1. The manifest is the complete **actual-pole** manifest on the outer
   rectangle, after all numerator cancellations and common events are
   resolved.

2. The target set is the fixed eligible real core
   \(|c|<T_0\).  Every other actual outer pole is a nontarget and must
   receive the zero congruence to its full actual order.

3. The target congruences must use the L-105105 coefficients:

   \[
   (z-c)^{r_c-1}
   \quad\hbox{for }F/F',
   \qquad
   r_c(z-c)^{2r_c-2}
   \quad\hbox{for }F^2/(F'F'').
   \]

4. Review must verify that the weighted carriers have only simple poles at
   the fixed core targets and are holomorphic throughout the buffer.

5. The outer boundary must be raw-event regular.  The simultaneous good
   rectangle must be chosen outside the null set of intermediate pairs on
   which \(F'F''\) has a boundary zero.

6. Abstract finiteness of the outer event set is not an authenticated Xi
   manifest.  Any constructive or certified Xi use must exhibit the event
   locations, actual orders, and common-event decisions.

## 3. Tonelli and shell-budget obligations

1. The triangular weights must be derived as parameter-measure weights:

   \[
   \omega_\eta(y)
   =|\{\eta\in(\eta_0,\eta_1):\eta>|y|\}|,
   \]

   \[
   \omega_T(x)
   =|\{T\in(T_0,T_1):T>|x|\}|.
   \]

2. The exact Tonelli mean must be proved before invoking existence of a
   good rectangle.

3. For every prescribed nonnegative pair
   \((\lambda_1,\lambda_2)\), simultaneous selection for both carriers
   must use one aggregate nonnegative cost

   \[
   K=\lambda_1|H_1|+\lambda_2|H_2|,
   \]

   not two independently selected rectangles.  The resulting common
   rectangle may depend on the prescribed weight pair; no universal
   rectangle for all pairs may be claimed.

4. The shell budget is for

   \[
   H_1=W_1F/F',
   \qquad
   H_2=W_2F^2/(F'F''),
   \]

   themselves.  Selector degree, coefficient size, conditioning, and local
   cancellations remain inside this product.

5. Factoring out a selector norm is permitted only after a separate valid
   bound is supplied.  Such a factorization must not erase a cancellation
   needed to make a multiple raw pole locally integrable.

6. Qualitative finiteness of every finite shell is not a cofinal estimate.
   The budget must be normalized by both buffer widths and compared with an
   explicit target scale.

## 4. Cofinal and Xi firewalls

The finite identity does not establish any of the following:

- a complete cofinal sequence of authenticated Xi manifests;
- uniform selector degree, coefficient, Pick-norm, or collision control;
- a bound for the weighted shell budget at scale \(R_n\);
- the positive signed first-moment estimate \(A_n\ge\mu R_n\);
- multiplicity-defect control or a complete zero-count comparison;
- strict Xi jet coherence, RCMV104530, or RH.

The conditional coherence corollary is correctly typed only when
\(R_n\to\infty\), \(\mu,\nu>0\), and

\[
A_n\ge\mu R_n(1+o(1)),
\qquad
\mathcal E(H_{2,n})\le2\pi\nu R_n(1+o(1)),
\]

so that

\[
B_n\le\nu R_n(1+o(1)),
\qquad
\liminf\frac{A_n^2}{R_nB_n}\ge\frac{\mu^2}{\nu}.
\]

The strict threshold requires \(\mu^2/\nu>1/2\), with any claimed margin
written explicitly.

## 5. Exact fixture obligations

For

\[
F=z^3/3-z^2+1,
\]

review must check all of the following by exact rational arithmetic:

1. \(F'=z(z-2)\), \(F''=2(z-1)\), and \(F'''=2\);
2. the core residue is \(-1/2\) and its square is \(1/4\);
3. the buffer residues are \(-1/18\) at the \(F''\)-event \(1\), and
   \(-1/6,1/36\) at the \(F'\)-event \(2\);
4. the core-only raw charges jump as \(T\) crosses \(1\) and \(2\);
5. \(W_1=1-z/2\) and \(W_2=(z-1)(z-2)/2\) satisfy every outer congruence;
6. the weighted carriers reduce exactly to
   \(-F/(2z)\) and \(F^2/(4z)\);
7. their normalized charges remain \(-1/2\) and \(1/4\) on every
   raw-regular intermediate rectangle.

## 6. Verdict rule

The packet may be classified **PROPOSED EXACT FINITE IDENTITY** only if the
coordinate, orientation, manifest-completeness, selector, \(2\pi\), Tonelli,
and cubic-fixture obligations all pass.

Any assertion of an Xi shell bound, a constructive cofinal manifest, a
signed Xi moment estimate, RCMV104530, or RH must be rejected unless it is
supported by a separate theorem and certificate.  Passing this contract
authenticates the finite shell ledger only.
