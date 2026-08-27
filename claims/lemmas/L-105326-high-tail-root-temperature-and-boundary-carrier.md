# L-105326 — The high-Xi-tail local carrier leakage has a universal nonzero main term

Claim ID: `L-105326`  
Status: **PROPOSED ANALYTIC COROLLARY — INDEPENDENT HOSTILE REVIEW REQUIRED**  
Created: 2026-08-23  
Depends on: `L-105321--L-105322`; `L-105324--L-105325`  
RH status: **not assumed**

## 1. Setup

Fix constants

\[
0<c_2<c_1<c_0,
\qquad H>0,
\]

where `c_0` is the moving-saddle constant. Let `M->infinity`, let `m>=M`, and
choose a regular height `X=X_M` satisfying

\[
X\to\infty,
\qquad
X\le c_2{M\over\log M},
\qquad
w_mX\to\infty.
\tag{L-105326.1}
\]

Put

\[
F_m=\Xi^{(m)}.
\]

By `L-105322`, every zero of `F_m` and `F_m'` in the larger rectangle is real
and simple.

Let

\[
N_m(X)=\#\{x\in[-X,X]:F_m(x)=0\},
\]

\[
S_{2,m}(X)=\sum_{F_m(x)=0,\ |x|<X}x^2,
\]

and define the local root temperature

\[
\mathcal T_m(X)
={S_{2,m}(X)\over N_m(X)(N_m(X)-1)}.
\tag{L-105326.2}
\]

The first real critical-residue moment is

\[
\mathcal M_{1,m}(X)
=-\sum_{F_m'(c)=0,\ |c|<X}
{F_m(c)\over F_m''(c)}.
\tag{L-105326.3}
\]

## 2. Root count and second spatial moment

The exact phase count gives

\[
N_m(X)
={\Theta_m(X)-\Theta_m(-X)\over\pi}+O(1).
\]

Since

\[
\Theta_m'(x)=w_m+O(c_1)+o(1),
\]

uniformly,

\[
\boxed{
N_m(X)
={2w_mX\over\pi}(1+o(1)).
}
\tag{L-105326.4}
\]

The phase-cell discrepancy in every initial interval is `O(1)`. Stieltjes
summation with the weight `x^2` therefore gives

\[
\begin{aligned}
S_{2,m}(X)
&={1\over\pi}
\int_{-X}^{X}x^2\Theta_m'(x)\,dx+O(X^2)\\
&={2w_mX^3\over3\pi}(1+o(1)).
\end{aligned}
\tag{L-105326.5}
\]

The error is uniform because `w_mX->infinity`. Combining
(L-105326.4)--(L-105326.5),

\[
\boxed{
\mathcal T_m(X)
={\pi X\over6w_m}(1+o(1)).
}
\tag{L-105326.6}
\]

## 3. Critical-residue carrier

Every zero `c` of `F_m'` in the buffered box satisfies

\[
{F_m(c)\over F_m''(c)}
=-w_m^{-2}(1+o(1))
\]

uniformly. The critical-point count is

\[
N_{m+1}(X)
={2w_mX\over\pi}(1+o(1)),
\]

because adjacent saddle frequencies have ratio `1+o(1)`. Hence

\[
\boxed{
\mathcal M_{1,m}(X)
={2X\over\pi w_m}(1+o(1)).
}
\tag{L-105326.7}

In particular,

\[
\boxed{
{\mathcal M_{1,m}(X)\over\mathcal T_m(X)}
={12\over\pi^2}(1+o(1)).
}
\tag{L-105326.8}

The ratio is not one.

## 4. Explicit carrier leakage

Let `B_(1,F_m)` and `mathcal E_(Omega)(F_m)` be the first residue flux and
carrier-leakage functional of `L-105324`. There is no nonreal-critical
correction in the present box, so

\[
-B_{1,F_m}=\mathcal M_{1,m}.
\]

Since `N_m/(N_m-1)=1+o(1)`, equations
(L-105326.6)--(L-105326.7) give

\[
\boxed{
\mathcal E_{\Omega_{X,H}}(F_m)
=
{12-\pi^2\over6\pi}
{X\over w_m}(1+o(1)).
}
\tag{L-105326.9}
\]

The constant is strictly positive because `pi^2<12`.

Thus local root temperature and first critical-residue mass each have a
power-sized carrier, and their difference also has a power-sized universal
main term.

## 5. Binding consequence

Any proposed low-order argument of the form

```text
bound local root temperature absolutely;
bound first residue flux absolutely;
bound carrier leakage by o(X/w_m);
```

is false already in the unconditional high derivative model. The correct
object must preserve the exact recombination

\[
\mathcal M_{1,m}
={N_m-1\over N_m}
(\mathcal T_m+\mathcal E_m)
\]

before taking absolute values or negative parts.

The universal high-tail calibration is

\[
\boxed{
\mathcal M_{1,m}
\sim {12\over\pi^2}\mathcal T_m.
}
\tag{L-105326.10}
\]

This factor should replace the complete-polynomial factor one in any
height-localized asymptotic model.

## 6. Scope

The theorem is conditional on independent verification of the moving-saddle
and phase-cell theorems. It concerns the high derivative tail and does not
supply the low-order carrier recombination, a sign for the centered weighted
flux, or RH. Its role is a binding asymptotic firewall: boundary carrier
leakage is structural and must not be estimated away.
