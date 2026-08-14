# L-91682 — Complete arithmetic causal profiles and factor-61 Lorenz cutoffs

Claim ID: `L-91682`  
Status: **PROVED EXACT / DIRECTED**  
Created: 2026-08-14  
Frozen parent: PR #462 at `8642e062b6c6f5a4c7d443a1ee5a6e9ecf3e4706`  
Depends on: `L-91112`, `L-91341`, `L-91348`, `L-91357`, `L-91359`  
Replay: `X-91682-post-hall-complete-profile`  
RH status: **unproved**

## 1. Statement

Let

\[
P_{61}=\prod_{q\le 61}q,
\qquad p\ge 67,
\qquad 1\le y<67,
\qquad x=py,
\qquad r=p^{-1/2}.
\]

For a square-free divisor `d|P_61`, put `z=y/d` and define the causal row atom

\[
K_R^{(j)}(d)
=\frac1{\sqrt d}
\left[Q_{pz}(j)-rQ_z(j)\right],
\qquad 2\le j\le 66,
\]

with `Q_Y(j)=0` for `Y<j`.  Define the target and score atoms

\[
K_T(d)=\frac1{\sqrt d}
\left[(4\sqrt{pz}-3)-r(4\sqrt z-3)\right],
\]

\[
K_S(d)=\frac1{\sqrt d}
\left[(5\sqrt{pz}-3)-r(5\sqrt z-3)\right].
\]

Then on the actual arithmetic source set,

\[
\boxed{
 d_1<d_2
 \Longrightarrow
 \frac{K_R^{(j)}(d_1)}{K_S(d_1)}
 \ge
 \frac{K_R^{(j)}(d_2)}{K_S(d_2)}
}
\tag{L-91682.1}
\]

and

\[
\boxed{
 d_1<d_2
 \Longrightarrow
 \frac{K_R^{(j)}(d_1)}{K_T(d_1)}
 \ge
 \frac{K_R^{(j)}(d_2)}{K_T(d_2)}.
}
\tag{L-91682.2}
\]

The earlier rough cutoff `p>=500000` is unnecessary.  Both arithmetic orders hold for every real `p>=67`.

Moreover the leftmost score-Lorenz and target-Lorenz cutoffs are uniformly below `2000`:

\[
\boxed{c_S<2000,
\qquad c_T<2000.}
\tag{L-91682.3}
\]

## 2. Global target-normalized one-endpoint profile

Put

\[
\Psi_j(Y)=\frac{Q_Y(j)}{4\sqrt Y-3}.
\]

On an activation cell `N<=Y<N+1`, write

\[
Q_Y(j)=C_{j,N}\log Y-D_{j,N}.
\]

The logarithmic derivative numerator is

\[
M_{4,j}(Y)
=4\sqrt Y\,[2C_{j,N}-Q_Y(j)]-6C_{j,N},
\]

and

\[
\frac{d}{d\log Y}\Psi_j(Y)
=\frac{M_{4,j}(Y)}{2(4\sqrt Y-3)^2}.
\tag{L-91682.4}
\]

Retain

\[
c_j=\frac2{j(j-1)},
\quad
\eta_j=c_j(1+H_{j-1})-a_j+b_j,
\]

\[
K_j=-4c_j+c_jL_{j-1}-a_j\log j+b_j\log(j+1)
\]

from `L-91359`.  The same elementary lattice-ramp bound gives

\[
Q_Y(j)\le 4c_j\sqrt Y-\eta_j\log Y+K_j.
\]

At the right endpoint of a cell, the directed coefficient bounds give

\[
\boxed{
M_{4,j}(Y)
\ge
\sqrt Y\,[4\eta_j\log Y-20c_j-8\eta_j-4K_j]
+6\eta_j.
}
\tag{L-91682.5}
\]

The bracket is increasing.  The replay proves all 65 gates at `Y=83`; the smallest lower gate is

\[
0.0214944300464049\ldots
\]

at `j=66`.  The frozen finite-window theorem covers `j<=Y<83`.  Hence

\[
\boxed{
\Psi_j(Y)\text{ is strictly increasing on }Y\ge j.
}
\tag{L-91682.6}
\]

The same argument with coefficient at least `4` also covers the child-row-inactive causal denominator.

## 3. Inner causal derivative

For `a in {4,5}` put

\[
S_a(Y)=a\sqrt Y-3,
\qquad
\Phi_{a,j}(Y)=\frac{Q_Y(j)}{S_a(Y)},
\]

and

\[
\mathcal R_{a,p,j}(z)
=
\frac{Q_{pz}(j)-rQ_z(j)}
{S_a(pz)-rS_a(z)}.
\]

With `P=pz`,

\[
\mathcal R_{a,p,j}(z)
=
\Phi_{a,j}(P)
+	heta_{a,p}(z)
[\Phi_{a,j}(P)-\Phi_{a,j}(z)],
\]

where `theta>=0` and `d theta/d log z>=0`.  Consequently it is enough to prove

\[
\boxed{
\frac{M_{a,j}(P)}{S_a(P)}
\ge
r\frac{M_{a,j}(z)}{S_a(z)},
}
\tag{L-91682.7}
\]

where

\[
M_{a,j}(Y)=a\sqrt Y[2C_{j,N}-Q_Y(j)]-6C_{j,N}.
\]

Two distinct child-row-active divisors satisfy

\[
d_2\le y/j<67/j.
\]

Since `d_2>=2`, this forces

\[
\boxed{j\le33.}
\tag{L-91682.8}
\]

Thus the continuous counterexample at row `66` lies outside every nontrivial arithmetic inner comparison.

For `2<=j<=33` and child cell `j<=N<=66`, the two-term lattice majorant gives an explicit parent lower function

\[
L_{a,j}(P)
=
\frac{
\sqrt P\,[a\eta_j^{(2)}\log P-D_{a,j}^{(2)}]
+6\eta_j^{(2)}
}{a\sqrt P-3},
\]

with

\[
D_{a,j}^{(2)}=2a\lambda_j^{(2)}+aK_j^{(2)}+12c_j.
\]

The replay proves:

1. `L_{a,j}` is increasing from `P=67j` onward;
2. `M_{a,j}(z)/S_a(z)` decreases inside each child activation cell;
3. every one of the `1584` endpoint gates

\[
L_{a,j}(67N)
>
67^{-1/2}
\frac{M_{a,j}(N)}{S_a(N)}
\]

is strict.

The minimum directed gaps are

\[
0.00256430147432384\ldots
\]

for the score profile and

\[
0.00161505502251516\ldots
\]

for the target profile, both at `(j,N)=(33,33)`.

This proves the inner sector.  The global one-endpoint profiles and continuity at the child-row activation boundary prove the cross-boundary and child-inactive sectors.  Equations (L-91682.1)--(L-91682.2) follow.

## 4. Uniform cutoffs below 2000

Let `C=2000` and define

\[
A_C=
\sum_{\substack{d|P_{61}\\\mu(d)=1,\ d\le C}}\frac1d
-
\sum_{\substack{d|P_{61}\\\mu(d)=-1}}\frac1d,
\]

\[
B_C=
\sum_{\substack{d|P_{61}\\\mu(d)=1,\ d\le C}}\frac1{\sqrt d}
-
\sum_{\substack{d|P_{61}\\\mu(d)=-1,\ d\le C}}\frac1{\sqrt d}.
\]

Exact divisor enumeration gives

\[
\boxed{
A_C=
\frac{852772323997294585715}
{23457676271881394196654}>0.
}
\tag{L-91682.9}
\]

Directed square-root enclosures prove

\[
5\sqrt C A_C-3B_C-\frac{335}{\sqrt C}>0.28728,
\]

\[
4\sqrt C A_C-3B_C-\frac{268}{\sqrt C}>0.15966.
\tag{L-91682.10}
\]

For `x>=C`, the parent even prefix below `C` minus all odd demand is bounded below by the corresponding first two terms.  Since `y<67`, the complete child subtraction is at most `335/sqrt(x)` in score and `268/sqrt(x)` in target.  Both lower bounds increase with `x`, so (L-91682.10) proves (L-91682.3).  If `x<C`, every active source is already below the cutoff.

Only `185` even cutoff nodes remain.

## 5. Verification boundary

The replay proves all displayed finite gates.  It does not prove the remaining even/odd target-Lorenz row determinant and does not prove RH.
