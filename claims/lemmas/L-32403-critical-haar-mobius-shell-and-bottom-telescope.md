# L-32403 — Critical Haar Möbius shell and bottom telescope

Claim ID: `L-32403`  
Title: The half-power normalized dyadic Möbius difference has constant positive interior carry charge and an exact three-coordinate central-cascade telescope  
Status: **PROPOSED COMPLETE EXACT FINITE/ANALYTIC LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-s`  
Created: 2026-08-08  
Dependencies: PR #280 central first-difference residual identity; elementary Dirichlet convolution and Mellin transform  
Scope: exact source/carry reduction and RH-sensitive scalar criterion; no sign or subpower estimate is claimed

## 1. Critical Haar source

Define

\[
\boxed{
 \nu_2
 =\mu-\sqrt2\,\delta_2*\mu.
}
\tag{L-32403.1}

Its Dirichlet series is

\[
\boxed{
 \sum_{n\ge1}{\nu_2(n)\over n^s}
 ={1-2^{1/2-s}\over\zeta(s)}.
}
\tag{L-32403.2}

The coefficient `sqrt(2)` is forced by critical half-power normalization. For the Möbius Riesz mean

\[
 \mathcal R_\mu(X)
 =\sum_{n\le X}{\mu(n)\over\sqrt n}\log{X\over n},
 \qquad X\ge1,
\tag{L-32403.3}

one has the exact dyadic Haar identity

\[
\boxed{
 \mathcal H_2(X)
 :=\mathcal R_\mu(X)-\mathcal R_\mu(X/2)
 =\sum_{n\le X}{\nu_2(n)\over\sqrt n}\log{X\over n}.
}
\tag{L-32403.4}

The value at a noninteger `X/2` is interpreted with the usual real cutoff.

## 2. Complete divisor prefix

Since

\[
 \mathbf1*\mu=\varepsilon,
\]

one has

\[
\boxed{
 \mathbf1*\nu_2
 =\varepsilon-\sqrt2\,\delta_2.
}
\tag{L-32403.5}

Therefore the divisor prefix

\[
 D_\nu(x)
 =\sum_{q\le x}\nu_2(q)\left\lfloor{x\over q}\right\rfloor
\tag{L-32403.6}

is exactly

\[
\boxed{
 D_\nu(0)=0,
 \qquad
 D_\nu(1)=1,
 \qquad
 D_\nu(x)=1-\sqrt2\quad(x\ge2).
}
\tag{L-32403.7}

No Möbius sum remains in this carry coordinate.

## 3. Constant positive charge on every interior split

For an integer split `n=j+(n-j)`, define the source carry charge

\[
 Y_\nu(n,j)
 =D_\nu(n)-D_\nu(j)-D_\nu(n-j).
\tag{L-32403.8}

Equations (L-32403.7) give the complete table:

\[
\boxed{
Y_\nu(2,1)=-1-\sqrt2,
}
\tag{L-32403.9}

\[
\boxed{
Y_\nu(n,1)=Y_\nu(n,n-1)=-1
\qquad(n\ge3),
}
\tag{L-32403.10}

and, whenever both children are at least two,

\[
\boxed{
Y_\nu(n,j)=\sqrt2-1>0.
}
\tag{L-32403.11}

Hence every `1/4`-balanced split with parent `n>=5` has exactly the same strictly positive source charge `sqrt(2)-1`.

This is a stronger geometric simplification than the integer-coefficient dyadic source: the complete interior is not merely nonnegative; it is a constant-charge cone.

## 4. Central first-difference telescope

Let `r(q)` be any finitely supported real sequence on integers `q>=2`, with zero extension above its support. Put

\[
 d_n=r(n)-r(n+1).
\tag{L-32403.12}

Assign `d_n` to the central split

\[
[n,\lfloor n/2\rfloor].
\]

PR #280's exact central residual identity says the resulting carry load is

\[
 r-\mathcal T r,
\tag{L-32403.13}

where

\[
 (\mathcal T r)(q)
 =\sum_{k\ge1}
 [r(2kq-1)-r((2k+1)q)].
\tag{L-32403.14}

Pairing (L-32403.13) with `nu_2` and using the charge table gives

\[
\begin{aligned}
 \langle\nu_2,r-\mathcal T r\rangle
 ={}&(-1-\sqrt2)(r_2-r_3)\\
 &-(r_3-r_4)
 +(\sqrt2-1)\sum_{n\ge4}(r_n-r_{n+1}).
\end{aligned}
\]

The tail telescopes, so

\[
\boxed{
 \langle\nu_2,r-\mathcal T r\rangle
 =-(1+\sqrt2)r(2)
  +\sqrt2\,r(3)
  +\sqrt2\,r(4).
}
\tag{L-32403.15}

This identity holds with no sign assumption on the central coefficients `d_n`.

## 5. Finite bottom-coordinate representation of the Riesz shell

Let

\[
 w_X(q)=q^{-1/2}\log(X/q)\mathbf1_{q\le X}
\tag{L-32403.16}

and define the exact finite central cascade

\[
 r_0=w_X,
 \qquad
 r_{a+1}=\mathcal T r_a.
\tag{L-32403.17}

Support decreases by at least a factor two, so `r_a=0` after `O(log X)` stages.

The carry target begins at `q=2`, whereas the full Riesz shell contains the unit term `nu_2(1)w_X(1)=log X`. Summing (L-32403.15) through the finite cascade therefore gives

\[
\boxed{
\begin{aligned}
 \mathcal H_2(X)
 =\log X
 +\sum_{a\ge0}\Bigl[
  -(1+\sqrt2)r_a(2)
  +\sqrt2\,r_a(3)
  +\sqrt2\,r_a(4)
 \Bigr].
\end{aligned}}
\tag{L-32403.18}

The sum is finite.

Thus the full critical dyadic Möbius Riesz shell is exactly a bottom-coordinate observable of the elementary central carry cascade. No Möbius coefficients remain after the initial source pairing.

## 6. Mellin criterion

Initially for `Re z>1/2`, direct integration gives

\[
\boxed{
 \int_1^\infty
 \mathcal H_2(X)X^{-z-1}\,dX
 ={1-2^{-z}\over z^2\zeta(z+1/2)}.
}
\tag{L-32403.19}

If

\[
\boxed{
 \mathcal H_2(X)=O_\varepsilon(X^\varepsilon)
 \quad\text{for every }\varepsilon>0,
}
\tag{HDS}

then the left side converges normally for every `Re z>0` and analytically continues the right side there, apart from the explicit removable/zero-frequency behavior at `z=0`.

If `rho` is a zeta zero with `Re rho>1/2`, then `z=rho-1/2` lies in `Re z>0`, and

\[
1-2^{-z}\ne0
\]

because `|2^{-z}|<1`. The right side would have a genuine pole, contradiction. Functional-equation symmetry then gives RH.

Hence

\[
\boxed{
\text{HDS}\Longrightarrow\mathrm{RH}.
}
\tag{L-32403.20}

The converse subpower bound follows from the usual RH Riesz estimates, but it is not needed for the proposed attack.

## 7. New proof interface

Equation (L-32403.18) replaces a global Möbius shell estimate by the following concrete finite target:

> Bound the cancellation between the explicit unit term `log X` and the `O(log X)` central-cascade bottom coordinates in (L-32403.18) by `X^o(1)`.

This interface is independent of the coupled interior Selberg matrix and of the full boundary-state norm. It permits the analytic `6/7` bank, first-entrance recombination, Mersenne localization, or direct bottom-coordinate recurrences to be applied only to the three coordinates which actually survive the critical Haar source.

## 8. Proof boundary

Established exactly, subject to review:

1. the half-power dyadic Haar source and its Dirichlet series;
2. the exact dyadic Riesz-shell identity;
3. the compact divisor prefix `epsilon-sqrt(2)delta_2`;
4. constant positive carry charge on every interior split;
5. the exact three-coordinate central-cascade telescope;
6. the Mellin implication `HDS -> RH`.

Not established:

1. HDS;
2. a sign theorem for `H_2`;
3. a subpower bound for the bottom-coordinate telescope;
4. RH.
