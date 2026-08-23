# L-105216 — The low-order Bezoutian is an exact chord average of polarized Laguerre defects

Claim ID: `L-105216`  
Status: **PROVED UNCONDITIONALLY**  
Created: 2026-08-23  
Depends on: `L-105207--L-105208`, `L-105213--L-105214`  
RH status: **not assumed**

Let `F` be a real `C^2` function and define

\[
\mathscr B_F(x,y)
={F(x)F'(y)-F'(x)F(y)\over x-y},
\]

with diagonal `F'^2-FF''`. Define the polarized Laguerre form

\[
\boxed{
\Gamma_F(u,v)
=F'(u)F'(v)
-{1\over2}
\left[F''(u)F(v)+F(u)F''(v)\right].
}
\tag{L-105216.1}

## 1. Exact chord identity

For real `x,y`, put

\[
\alpha_t=(1-t)x+ty,
\qquad
\beta_t=tx+(1-t)y.
\]

Then

\[
\boxed{
\mathscr B_F(x,y)
=\int_0^1
\Gamma_F(\alpha_t,\beta_t)\,dt.
}
\tag{L-105216.2}

Indeed, if

\[
Q(t)=F(\alpha_t)F'(\beta_t)
-F'(\alpha_t)F(\beta_t),
\]

then

\[
Q'(t)=2(y-x)\Gamma_F(\alpha_t,\beta_t),
\]

while `Q(1)=-Q(0)`. Integrating proves (L-105216.2).

Thus the full two-point Pick/Bezoutian kernel is not an unrelated object: it
is the average of the real phase numerator along the chord exchanging its two
endpoints. The diagonal case reduces to the ordinary Laguerre defect.

## 2. Translation average for the actual Xi source

Use the two-sided positive Fourier representation

\[
\Xi(t)=\int_{\mathbb R}\varphi(u)e^{itu}\,du,
\qquad
\varphi(u)=\Phi(|u|)>0,
\]

and put

\[
F=\Xi^{(k)}.
\]

Plancherel gives, for every real `d`,

\[
\boxed{
\int_{\mathbb R}
\Gamma_F(m+d,m-d)\,dm
=4\pi\int_{\mathbb R}
 u^{2k+2}\varphi(u)^2\cos(2du)\,du.
}
\tag{L-105216.3
}

Consequently, for a chord of length `h`,

\[
\boxed{
\begin{aligned}
&\int_{\mathbb R}
\mathscr B_F(m+h/2,m-h/2)\,dm\\
&\qquad=4\pi\int_{\mathbb R}
 u^{2k+2}\varphi(u)^2
{\sin(hu)\over hu}\,du,
\end{aligned}
}
\tag{L-105216.4
}

with the continuous value one at `hu=0`.

## 3. An unconditional short-chord mean-positive region

Since

\[
{\sin x\over x}\ge1-{x^2\over6}
\qquad(x\in\mathbb R),
\]

put

\[
A_k=\int_{\mathbb R}u^{2k+2}\varphi(u)^2du,
\qquad
B_k=\int_{\mathbb R}u^{2k+4}\varphi(u)^2du.
\]

Equation (L-105216.4) gives

\[
\boxed{
\int_{\mathbb R}
\mathscr B_F(m+h/2,m-h/2)\,dm
\ge4\pi\left(A_k-{h^2\over6}B_k\right).
}
\tag{L-105216.5
}

Therefore

\[
\boxed{
|h|<\sqrt{6A_k/B_k}
\quad\Longrightarrow\quad
\int_{\mathbb R}
\mathscr B_F(m+h/2,m-h/2)\,dm>0.
}
\tag{L-105216.6
}

This is a genuine fixed-low-order theorem. It proves that short-chord
Bezoutian negativity cannot dominate after translation averaging.

## 4. Binding localization firewall

The sinc multiplier in (L-105216.4) changes sign for long chords, and a
positive translation average does not imply positivity at one specified
ordinate. Thus the theorem does not prove the Pick kernel positive and does
not establish RH.

Its conclusion is nevertheless sharper than an undifferentiated mean-phase
statement:

```text
real phase numerator                 diagonal of the Bezoutian;
full Pick kernel                     chord average of polarized numerators;
short-chord center average           explicitly positive;
remaining obstruction                fixed-center/long-chord fluctuation.
```

Together with `L-105214`, this identifies the actual Levinson problem as the
negative-square localization of one boundary Cauchy–Loewner kernel, not a
failure of source-level mean orientation.