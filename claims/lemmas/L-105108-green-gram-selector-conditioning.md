# L-105108 — Green–Gram conditioning ledger for optimal selectors

Claim ID: L-105108

Status: **PROPOSED EXACT FINITE-WINDOW THEOREM**

Created: 2026-08-23

Depends on: L-105103; L-105105; L-105107

RH status: **unproved**

## 1. Positive Green convention and local loads

Let \(\Omega\) be a bounded simply connected Jordan domain.  Retain the
complete actual-pole manifest \((S,d)\), target set \(\mathcal T\), and
top-primary data \(\gamma_c\ne0\) from L-105107.  Assume
\(\mathcal T\ne\varnothing\).  For the empty target set, L-105107 already
gives \(W_*=0\) and \(\tau=0\); the target-indexed ledgers below are then
vacuous.  Define the forced orders

\[
n_a=
\begin{cases}
d_a,&a\notin\mathcal T,\\
d_a-1,&a\in\mathcal T,
\end{cases}
\tag{L-105108.1}
\]

For a Riemann map \(\phi:\Omega\to\mathbb D\), define

\[
r_\Omega(c)=\frac{1-|\phi(c)|^2}{|\phi'(c)|},
\qquad
\rho_\Omega(c,a)=
\left|
\frac{\phi(c)-\phi(a)}
{1-\overline{\phi(a)}\phi(c)}
\right|,
\tag{L-105108.2}
\]

and use the positive Dirichlet Green convention

\[
\boxed{
g_\Omega(c,a)=-\log\rho_\Omega(c,a).
}
\tag{L-105108.3}
\]

Thus \(g_{\mathbb D}(z,a)=\log|(1-\overline a z)/(z-a)|\).
This normalization has no factor two.

The ordinary Pick value \(y_c=\gamma_c/\beta_c^\Omega\) in L-105107 has
the exact magnitude

\[
\boxed{
\mathcal L_c:=|y_c|
=|\gamma_c|\,r_\Omega(c)^{d_c-1}
\exp\!\left(
\sum_{\substack{a\in S\\a\ne c}}n_a g_\Omega(c,a)
\right).
}
\tag{L-105108.4}
\]

Indeed,

\[
|\beta_c^\Omega|
=r_\Omega(c)^{-(d_c-1)}
\prod_{a\ne c}\rho_\Omega(c,a)^{n_a}.
\tag{L-105108.5}
\]

For one target, every other event is a nontarget, so L-105107 gives the
exact potential identity

\[
\boxed{
\log\tau
=\log|\gamma_c|+(d_c-1)\log r_\Omega(c)
+\sum_{a\ne c}d_a g_\Omega(c,a).
}
\tag{L-105108.6}
\]

For several targets, (L-105108.4) is a targetwise necessary load, not the
full optimum.  Other targets occur there with exponent \(d_a-1\), and the
phases of the complex values \(y_c\) remain load-bearing.

## 2. Exact normalized-Gram representation

Enumerate the target images \(\alpha_j=\phi(c_j)\).  Normalize the Szegő
kernel matrix from L-105107 to

\[
G_{jk}=
\frac{
\sqrt{(1-|\alpha_j|^2)(1-|\alpha_k|^2)}
}{1-\alpha_j\overline{\alpha_k}},
\qquad
D_y=\operatorname{diag}(y_{c_1},\ldots,y_{c_t}).
\tag{L-105108.7}
\]

The matrix \(G\) is positive definite, \(G_{jj}=1\), and

\[
|G_{jk}|^2=1-\rho_\Omega(c_j,c_k)^2.
\tag{L-105108.8}
\]

Positive diagonal congruence of the L-105107 Pick matrix gives the exact
operator formula

\[
\boxed{
\tau
=\left\|G^{-1/2}D_yG^{1/2}\right\|_2.
}
\tag{L-105108.9}
\]

A different Riemann map changes the normalized kernels by compatible
unimodular diagonal factors.  Hence (L-105108.9), the spectrum of \(G\),
and all bounds below are conformally intrinsic.

Put

\[
Y=\max_c|y_c|,
\qquad
\kappa=\kappa_2(G).
\tag{L-105108.10}
\]

Then

\[
\boxed{
Y\le\tau\le Y\sqrt\kappa.
}
\tag{L-105108.11}
\]

The lower bound is the diagonal Pick condition.  The upper bound follows
from submultiplicativity in (L-105108.9).  For \(Y>0\), equality
\(\tau=Y\) holds exactly when all prescribed values \(y_c\) are the same
constant: if an interpolant of norm \(Y\) attains modulus \(Y\) at an
interior target, the maximum-modulus principle makes it constant.

Separating the constant part of the data gives the sharper phase-sensitive
bound

\[
\boxed{
\tau\le
\inf_{\eta\in\mathbb C}
\left(
|\eta|+\sqrt\kappa\max_c|y_c-\eta|
\right).
}
\tag{L-105108.12}
\]

The exact Hilbert–Schmidt ledger

\[
\mathcal E=
\operatorname{tr}(G^{-1}D_yGD_y^*)
\tag{L-105108.13}
\]

also yields

\[
\sqrt{\mathcal E/t}\le\tau\le\sqrt{\mathcal E}.
\tag{L-105108.14}
\]

Neither \(\kappa(G)\) nor \(\mathcal E\) alone is the optimum; the joint
operator in (L-105108.9) is exact.

## 3. Target separation and a potential-only envelope

For each target define its target-only product separation

\[
\delta_c=
\prod_{\substack{b\in\mathcal T\\b\ne c}}
\rho_\Omega(c,b),
\qquad
\delta_c=1\quad(t=1).
\tag{L-105108.15}
\]

In disk coordinates put

\[
B_c(z)=
\prod_{\substack{b\in\mathcal T\\b\ne c}}
b_{\alpha_b}(z),
\qquad
L_c(z)=\frac{B_c(z)}{B_c(\alpha_c)}.
\tag{L-105108.16}
\]

Then \(L_c(\alpha_b)=\mathbf1_{b=c}\) and
\(\|L_c\|_\infty=\delta_c^{-1}\).  For every \(\eta\in\mathbb C\),

\[
H_\eta(z)=
\eta+
\sum_{c\in\mathcal T}(y_c-\eta)L_c(z)
\tag{L-105108.17}
\]

is an admissible Pick interpolant.  Therefore

\[
\boxed{
\tau\le
\inf_{\eta\in\mathbb C}
\left(
|\eta|+
\sum_{c\in\mathcal T}\frac{|y_c-\eta|}{\delta_c}
\right).
}
\tag{L-105108.18}
\]

Taking \(\eta=0\), and observing that division by \(\delta_c\) raises the
exponent of every *other target* from \(d_a-1\) to \(d_a\), gives the
conformally intrinsic Green–Gram sandwich

\[
\boxed{
\max_{c\in\mathcal T}
\left\{
|\gamma_c|r_\Omega(c)^{d_c-1}
e^{\sum_{a\ne c}n_ag_\Omega(c,a)}
\right\}
\le\tau
\le
\sum_{c\in\mathcal T}
|\gamma_c|r_\Omega(c)^{d_c-1}
e^{\sum_{a\ne c}d_ag_\Omega(c,a)}.
}
\tag{L-105108.19}
\]

The lower and upper exponents in (L-105108.19) are deliberately different
at other targets.  Replacing either ledger by the other is invalid.

There is also an exact Gram/product identity

\[
\boxed{
(G^{-1})_{cc}=\delta_c^{-2}.
}
\tag{L-105108.20}
\]

To see it, identify \(G\) as the Gram matrix of normalized Szegő kernels.
The distance of the \(c\)-kernel from the span of the other kernels is the
norm of its projection onto \(B_cH^2\), namely \(|B_c(\alpha_c)|=\delta_c\).
The standard inverse-Gram distance formula gives (L-105108.20).  Hence

\[
\lambda_{\min}(G)
\ge\left(\sum_c\delta_c^{-2}\right)^{-1},
\qquad
\kappa(G)\le t\sum_c\delta_c^{-2},
\tag{L-105108.21}
\]

and, with \(\delta_*=\min_c\delta_c\),

\[
\tau\le
Y\sqrt{t\sum_c\delta_c^{-2}}
\le\frac{tY}{\delta_*}.
\tag{L-105108.22}
\]

Alternatively, if

\[
\mu=\max_j\sum_{k\ne j}|G_{jk}|<1,
\tag{L-105108.23}
\]

Gershgorin's theorem gives

\[
\tau\le
Y\sqrt{\frac{1+\mu}{1-\mu}}.
\tag{L-105108.24}
\]

Conditions (L-105108.21)--(L-105108.24) are finite sufficient envelopes,
not authenticated Xi separation laws.

## 4. Exact two-target thresholds

For two distinct targets \(c_j,c_k\), write

\[
\rho_{jk}=\rho_\Omega(c_j,c_k),
\quad
p_{jk}=y_j\overline{y_k},
\quad
A_{jk}=2\operatorname{Re}p_{jk}
+\frac{|y_j-y_k|^2}{\rho_{jk}^2}.
\tag{L-105108.25}
\]

The Schwarz–Pick condition for an interpolant of squared norm \(s\) is

\[
s|y_j-y_k|^2
\le
\rho_{jk}^2|s-y_j\overline{y_k}|^2.
\tag{L-105108.26}
\]

Thus the exact two-target squared optimum is

\[
\boxed{
s_{jk}=
\max\left\{
|y_j|^2,
|y_k|^2,
\frac{A_{jk}+\sqrt{A_{jk}^2-4|p_{jk}|^2}}2
\right\}.
}
\tag{L-105108.27}
\]

Every multipoint optimum obeys

\[
\tau\ge\max_{j<k}\sqrt{s_{jk}},
\tag{L-105108.28}
\]

with equality when there are exactly two targets.  For three or more
targets, even all two-by-two conditions can miss a collective obstruction;
the full Pick matrix remains necessary.

## 5. Domain comparison and Euclidean collision bounds

If \(\Omega_1\subseteq\Omega_2\) carry the same finite manifest and the
same ambient-coordinate jet data, restriction of admissible selectors gives

\[
\tau_{\Omega_1}\le\tau_{\Omega_2}.
\tag{L-105108.29}
\]

This statement does not compare problems after new events or targets are
added.  For one fixed target it has the exact ratio

\[
\boxed{
\frac{\tau_{\Omega_2}}{\tau_{\Omega_1}}
=
\left(
\frac{r_{\Omega_2}(c)}{r_{\Omega_1}(c)}
\right)^{d_c-1}
\prod_{a\ne c}
\left(
\frac{\rho_{\Omega_1}(c,a)}
{\rho_{\Omega_2}(c,a)}
\right)^{d_a}
\ge1.
}
\tag{L-105108.30}
\]

For a proper inclusion the inequality is strict whenever the forced order
\(N_0=(d_c-1)+\sum_{a\ne c}d_a\) is positive.  This is the strict Schwarz
lemma applied to the normalized inclusion map.  The sole equality exception
is the constant value-interpolation problem \(d_c=1\) with no nontarget.

Suppose now that

\[
B(c,\delta)\subseteq\Omega\subseteq B(c,R)
\tag{L-105108.31}
\]

and every nontarget lies in \(B(c,\delta)\).  Schwarz–Pick and domain
monotonicity give

\[
\delta\le r_\Omega(c)\le R,
\qquad
\frac{|a-c|}{R}
\le\rho_\Omega(c,a)
\le\frac{|a-c|}{\delta}.
\tag{L-105108.32}
\]

For the one-target problem, \(N_0=D-1\), so

\[
\boxed{
|\gamma_c|
\frac{\delta^{D-1}}
{\prod_{a\ne c}|a-c|^{d_a}}
\le\tau\le
|\gamma_c|
\frac{R^{D-1}}
{\prod_{a\ne c}|a-c|^{d_a}}.
}
\tag{L-105108.33}
\]

For any subset \(A\) of nontargets in the inball, dropping the remaining
factors gives the conformal-map-free lower bound

\[
\boxed{
\tau\ge
|\gamma_c|\delta^{d_c-1}
\prod_{a\in A}
\left(\frac{\delta}{|a-c|}\right)^{d_a}.
}
\tag{L-105108.34}
\]

Finally,
\(\rho_\Omega(c,a)=|a-c|/r_\Omega(c)+o(|a-c|)\) as \(a\to c\).
Hence a colliding nontarget cluster of total order \(M\) has the sharp local
growth \(\prod|a-c|^{-d_a}\); in a common scale \(\varepsilon\), the
collision exponent is exactly \(M\).

## 6. Residue edge consequence

On a rectifiable Jordan boundary, the L-105107 residue identity remains
unchanged.  Combining its edge estimate with (L-105108.19) gives

\[
\left|
\frac1{2\pi i}\int_EW_*h\,dz
\right|
\le
\frac{\operatorname{len}(E)}{2\pi}\|h\|_E
\sum_{c\in\mathcal T}
|\gamma_c|r_\Omega(c)^{d_c-1}
e^{\sum_{a\ne c}d_ag_\Omega(c,a)}.
\tag{L-105108.35}
\]

This is an exact finite-window sufficient envelope.  It supplies neither
the manifest nor decay of \(h\), and its positive Green charges may grow.

## 7. Sharp finite fixtures

1. In \(\mathbb D\), with \(\gamma=1\), target \(c=1/3\) of order two
   and nontarget \(-1/2\) of order one have
   \(r=8/9\), \(\rho=5/7\), and \(\tau=(8/9)(7/5)=56/45\).

2. At target nodes \(\pm1/2\), the same magnitudes \((2,2)\) give
   \(\tau=2\) for values \((2,2)\), but \(\tau=4\) for values
   \((-2,2)\).  Here
   \(G=\left[\begin{smallmatrix}1&3/5\\3/5&1\end{smallmatrix}\right]\),
   \(\kappa(G)=4\), and the upper bound in (L-105108.11) is attained by
   the opposite-phase data.

3. With targets \(\pm\varepsilon\), equal target data one, and a simple
   nontarget at zero, \(I_0(z)=z\),
   \(y_{-\varepsilon}=-\varepsilon^{-1}\),
   \(y_\varepsilon=\varepsilon^{-1}\), and
   \(W_*(z)=z^2/\varepsilon^2\).  At \(\varepsilon=1/5\),
   \(Y=5\), \(\kappa(G)=25\), \(\tau=25\), while the uncentred
   cardinal envelope is \(26\).  One factor five is the nontarget Green
   load and the other is target interaction.

4. For nodes \((-1/2,0,1/2)\) and values \((-1,1,-1)\), every two-target
   optimum is at most \(2+\sqrt3\), but

   \[
   \det(sK-D_yKD_y^*)
   =\frac{16}{225}(s-1)(s^2-62s+1),
   \tag{L-105108.36}
   \]

   so the full optimum is \(\tau=4+\sqrt{15}\).

5. In the disk \(B(0,R)\), with \(R>1/2\) and \(\gamma=1\), target zero
   of order two and nontarget \(1/2\) of order two give
   \(\tau_R=4R^3\): enlarging from \(R=1\)
   to \(R=2\) raises the norm from \(4\) to \(32\).

6. In the fixed unit disk, with \(\gamma=1\) and integers \(n\ge2\),
   \(m\ge1\), target zero of order one and nontarget \(1/n\) of order
   \(m\) give \(\tau=n^m\).  Smooth boundary, fixed conformal
   radius, fixed target data, and fixed total multiplicity therefore do not
   provide a separation-free selector bound.

## 8. Boundary of the result

This theorem closes a finite Green–Gram conditioning ledger.  It does not
supply:

- an actual Xi event manifest or multiplicity labels;
- certified conformal coordinates on changing Xi rectangles;
- any cofinal bound for the Green loads, product separations, normalized
  Gram condition, or joint data operator;
- unweighted quotient estimates for \(F/F'\) or \(F^2/(F'F'')\);
- weighted-edge decay, multiplicity-defect control, or strict jet coherence;
- RCMV104530 or RH.

No historical Green claim or accepted actual-Xi Pick claim is used as a
dependency; L-105107 is the explicit finite-selector dependency.  Historical
annular Green work uses a different factor-two convention and is unintegrated.
Accepted low-order actual-Xi Pick matrices use a different kernel.  The
historical colliding L-91014 and quarantined L-92302 remain outside the
dependency chain.  No novelty is claimed for classical Green functions,
Szegő Gram matrices, finite Blaschke interpolation, or Schwarz–Pick.  The
new contribution is their exact conditioning ledger for the L-105107
top-jet residue selector and the resulting finite/cofinal frontier.
