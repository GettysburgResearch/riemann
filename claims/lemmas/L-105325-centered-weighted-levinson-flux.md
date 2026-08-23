# L-105325 — Local temperature leakage is one centered weighted Levinson flux

Claim ID: `L-105325`  
Status: **PROPOSED EXACT ENTIRE-FUNCTION IDENTITY — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-23  
Depends on: `L-105324`; the parity-symmetric rectangle conventions of the Xi reverse-Rolle programme  
RH status: **not assumed**

## 1. Symmetric setup

Let `F` be entire, real on the real axis, and of definite parity. Let

\[
\Omega_{T,\eta}
=\{z:|\Re z|<T,\ |\Im z|<\eta\}
\]

be regular for `F` and `F'`. Use the notation of `L-105324`:

\[
N=N_F,
\qquad
\delta=\Delta_0(F;\Omega),
\qquad
M=N+\delta=N_{F'},
\]

and assume `N,M>=2`.

Parity gives

\[
S_1(F;\Omega)=0,
\qquad
\Delta_1(F;\Omega)=0.
\]

Put

\[
\mathcal T=\mathcal T_\Omega(F)
={S_2(F;\Omega)\over N(N-1)}.
\tag{L-105325.1}
\]

## 2. One centered flux, not two separate moments

The symmetric transport formula of `L-105324` is

\[
\mathcal T_\Omega(F')-\mathcal T_\Omega(F)
={S_2+\Delta_2\over M(M-1)}
-{S_2\over N(N-1)}.
\]

Since

\[
M(M-1)-N(N-1)
=\delta(2N+\delta-1),
\]

this becomes

\[
\boxed{
\mathcal T_\Omega(F')-\mathcal T_\Omega(F)
={\Gamma_2(F;\Omega)\over M(M-1)},
}
\tag{L-105325.2}
\]

where

\[
\boxed{
\Gamma_2(F;\Omega)
=
\Delta_2(F;\Omega)
-
\mathcal T_\Omega(F)\,
\Delta_0(F;\Omega)
\bigl(2N_F+\Delta_0(F;\Omega)-1\bigr).
}
\tag{L-105325.3}
\]

Thus the zeroth and second winding moments do not need two unrelated bounds.
They occur in one exact centered combination.

## 3. Logarithmic-derivative representation

Let

\[
L_F={F'\over F},
\qquad
J_F={L_F'\over L_F}
={F''\over F'}-{F'\over F}.
\tag{L-105325.4}
\]

Define the real centering parameter

\[
\lambda_F
=
\mathcal T_\Omega(F)
\bigl(2N_F+\Delta_0(F;\Omega)-1\bigr).
\tag{L-105325.5}
\]

The root multiset in a parity- and conjugation-symmetric rectangle makes
`mathcal T` real. Equations (L-105324.5) and (L-105325.3) give

\[
\boxed{
\Gamma_2(F;\Omega)
={1\over2\pi i}
\int_{\partial\Omega}
(z^2-\lambda_F)J_F(z)\,dz.
}
\tag{L-105325.6}
\]

This is a single centered second-moment winding of `F'/F`.

## 4. Exact four-edge formula

Because `F` has definite parity, `L_F` and `J_F` are odd. Schwarz reflection
gives

\[
J_F(\bar z)=\overline{J_F(z)}.
\]

For every real even polynomial weight `W`, direct pairing of the top/bottom and
left/right edges gives

\[
\boxed{
{1\over2\pi i}
\int_{\partial\Omega_{T,\eta}}W(z)J_F(z)\,dz
={2\over\pi}
\left[
\int_0^\eta
\Re\!\bigl(W(T+iy)J_F(T+iy)\bigr)\,dy
-
\int_0^T
\Im\!\bigl(W(x+i\eta)J_F(x+i\eta)\bigr)\,dx
\right].
}
\tag{L-105325.7}
\]

Apply this with

\[
W_F(z)=z^2-\lambda_F.
\]

Then

\[
\boxed{
\begin{aligned}
\Gamma_2(F;T,\eta)
={2\over\pi}\Bigg[&
\int_0^\eta
\Re\!\left(
((T+iy)^2-\lambda_F)J_F(T+iy)
\right)dy\\
&-
\int_0^T
\Im\!\left(
((x+i\eta)^2-\lambda_F)J_F(x+i\eta)
\right)dx
\Bigg].
\end{aligned}
}
\tag{L-105325.8}
\]

The first integral is the centered vertical edge flux; the second is the
centered Levinson horizontal argument flux.

## 5. Global polynomial cancellation

Let `F=p` be a polynomial and let the rectangle contain every zero of `p` and
`p'`. Then `delta=-1` and `mathcal T(p')=mathcal T(p)` by `L-105323`. Hence

\[
\boxed{
\Gamma_2(p;\Omega)=0.
}
\tag{L-105325.9}
\]

In other words, the complete polynomial derivative ladder has exact centered
zeroth/second winding cancellation. Nonzero `Gamma_2` in an entire finite
window is purely boundary leakage.

## 6. Xi derivative ladder

For

\[
F=\Xi^{(j)},
\]

`Gamma_2` uses the same meromorphic logarithmic-derivative current as the
ordinary reverse-Rolle winding charge, but with the one exact centering weight
`z^2-lambda_F`.

The low-order temperature transport telescopes:

\[
\boxed{
\mathcal T_\Omega(\Xi^{(r)})
-
\mathcal T_\Omega(\Xi)
=
\sum_{j=0}^{r-1}
{\Gamma_2(\Xi^{(j)};\Omega)
 \over N_{j+1}(N_{j+1}-1)}.
}
\tag{L-105325.10}
\]

Here `N_(j+1)` is the complete zero count of `Xi^(j+1)` in the regular
rectangle. No unweighted derivative level is inserted.

This supplies the exact boundary coordinate missing from the conserved finite
carrier theorem. A conclusion-facing sufficient statement is

```text
CWLF105325:
  the telescoped centered weighted flux in (L-105325.10), together with the
  explicitly separated nonreal-critical correction, is small enough to keep
  the local residue temperature positive and the cumulative reverse-Rolle
  budget below two.
```

`CWLF105325` remains open.

## 7. Scope

The identity supplies no sign for either edge integral. The centering parameter
`lambda_F` depends on the literal root moments in the same fixed rectangle; it
may not be replaced by an asymptotic selected after seeing a zero. Regular
height limits, canonical-product passage, and the cumulative Xi estimate
remain open. RH is not proved.
