# L-98011 — A zero-marginal target sandwich collapses the complete Lorenz dual to the scalar slice

Claim ID: `L-98011`  
Status: **PROVED EXACT FINITE-DIMENSIONAL THEOREM**  
Created: 2026-08-18  
Depends on: the oriented Lorenz slack of PR #591 / `L-97700`  
RH status: **not assumed**

Let a finite paired source have even atoms `E` and odd atoms `O`, with capacities `a_i>=0`, target coordinates `t_i>0`, and scalar coordinates `r_i>=0`. Put

\[
T_E=\sum_{i\in E}a_it_i,
\qquad
T_O=\sum_{i\in O}a_it_i,
\]

and let

\[
E_+=\{i\in E:r_i>0\},
\qquad
T_E^+=\sum_{i\in E_+}a_it_i.
\]

The forward Lorenz dual slack is

\[
D^+(\lambda)
=\lambda T_O+
\sum_{i\in E}a_i(r_i-\lambda t_i)_+
-R_O.
\tag{L-98011.1}
\]

Then `D^+` is convex and piecewise affine. Its one-sided derivatives at zero are

\[
\boxed{
\partial_-D^+(0)=T_O-T_E,
\qquad
\partial_+D^+(0)=T_O-T_E^+.
}
\tag{L-98011.2}
\]

Consequently the following are equivalent:

1. `lambda=0` is a global minimizer of `D^+`;
2. the **zero-marginal target sandwich** holds,
   \[
   \boxed{T_E^+\le T_O\le T_E;}
   \tag{L-98011.3}
   \]
3. for every real `lambda`,
   \[
   D^+(\lambda)\ge D^+(0).
   \tag{L-98011.4}
   \]

Under this sandwich, completed-parity scalar Lorenz feasibility reduces exactly to the zero hinge:

\[
\boxed{
D^+(\lambda)\ge0\ \text{for every real }\lambda
\iff
D^+(0)=R_E-R_O\ge0.
}
\tag{L-98011.5}
\]

## Proof

For `lambda<0`, every hinge is active because `r_i>=0` and `t_i>0`. Hence

\[
D^+(\lambda)
=R_E-R_O+\lambda(T_O-T_E),
\]

which gives the left derivative in (L-98011.2). For `lambda>0` sufficiently small, exactly the even atoms with positive scalar remain active, giving the right derivative.

A convex function has a global minimum at zero if and only if its left derivative is nonpositive and its right derivative is nonnegative. These two inequalities are precisely

\[
T_O-T_E\le0,
\qquad
T_O-T_E^+\ge0,
\]

which is (L-98011.3). The remaining assertions follow immediately.

## Specialization to the canonical `5:3` source

For the canonical atoms at endpoint `X`,

\[
r_X(k)=k^{-1/2}Q_*(X/k),
\qquad
t_X(k)=k^{-1/2}T(X/k).
\]

By the positive dictionary,

\[
r_X(k)>0\iff X/k>2\iff k<X/2.
\]

Thus the sandwich becomes the pair of explicit source inequalities

\[
\boxed{
\sum_{\substack{\mu(k)=+1\\k<X/2}}t_X(k)
\le
\sum_{\substack{\mu(k)=-1\\k\le X}}t_X(k)
\le
\sum_{\substack{\mu(k)=+1\\k\le X}}t_X(k).
}
\tag{L-98011.6}
\]

Equivalently, if

\[
\mathcal T_X=\sum_{k\le X}\mu(k)t_X(k)
\]

is the signed target and

\[
\mathcal Z_X=\sum_{\substack{\mu(k)=+1\\X/2\le k\le X}}t_X(k)
\]

is the even zero-scalar target band, then

\[
\boxed{0\le\mathcal T_X\le\mathcal Z_X.}
\tag{L-98011.7}
\]

This theorem does not assert (L-98011.7) for the arithmetic source. It proves that this target-only sandwich is the exact additional condition under which all nonzero Lorenz hinges cost nothing beyond the native scalar. A finite failure of the sandwich is an exact target separator; a proof of the sandwich plus scalar nonnegativity collapses `CPSL67` to the root zero hinge.
