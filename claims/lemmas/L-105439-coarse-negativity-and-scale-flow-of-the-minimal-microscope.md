# L-105439 — Coarse negativity and exact scale flow of the minimal Xi microscope

Claim ID: `L-105439`  
Status: **PROVED UNCONDITIONAL COARSE ASYMPTOTIC + EXACT FOURIER SCALE IDENTITY**  
Created: 2026-08-24  
Depends on: `L-105430`, `L-105438`  
RH status: **not assumed**

Use the minimal field

\[
\mathcal Q_r(a,h)
=-{4\over3}\Im m_r(a+ih)
+{2\over3}\Im m_r(a+2ih).
\]

## 1. Unconditional coarse negativity

For

\[
s_j={1\over2}+jh-ia,
\qquad
L_j={\xi'\over\xi}(s_j),
\qquad j=1,2,
\]

`L-105430` gives

\[
\Im m_r(a+jih)
=\Re {1\over L_j}+O_r(|L_j|^{-3}).
\tag{L-105439.1}

Uniformly for all real `a` as `h->infinity`,

\[
L_j=\Lambda+O(1),
\qquad
\Lambda={1\over2}\Log {s_1\over2\pi},
\]

with

\[
\Re(1/\Lambda)\gg1/|\Lambda|>0.
\]

Since

\[
-{4\over3}+{2\over3}=-{2\over3},
\]

one obtains

\[
\boxed{
\mathcal Q_r(a,h)
=-{2\over3}\Re {1\over\Lambda}
+O_r(|\Lambda|^{-2})<0
}
\tag{L-105439.2}

for all `a` once `h>=H_r^(2)` is sufficiently large. Quantitatively,

\[
\boxed{
\mathcal Q_r(a,h)
\le
-{c_r\over\log(3+\sqrt{a^2+h^2})}.
}
\tag{L-105439.3}

## 2. Exact Fourier multiplier

Let

\[
Q(\cdot,h)=K_h*\mu,
\]

where `K_h` is the positive kernel of `L-105438`. With

\[
T_h=e^{-h|D|},
\]

one has

\[
\boxed{
K_h*
={2\pi\over3}T_h(2I-T_h).
}
\tag{L-105439.4}

For one frequency put `t=e^(-h|xi|)`. The multiplier is

\[
k(t)={2\pi\over3}t(2-t).
\]

Differentiating gives

\[
\boxed{
\partial_h\widehat Q(\xi,h)
=-2|\xi|{1-t\over2-t}\widehat Q(\xi,h).
}
\tag{L-105439.5}

Equivalently,

\[
\boxed{
\partial_hQ
=-2|D|{I-T_h\over2I-T_h}Q.
}
\tag{L-105439.6}

The scalar symbol `2(1-t)/(2-t)` lies in `[0,1]` for `0<=t<=1`.

The multiplier is a combination of only two exponentials, so

\[
\boxed{
(\partial_h+|D|)(\partial_h+2|D|)Q=0.
}
\tag{L-105439.7}

## 3. Fine-scale limit

In distributions,

\[
K_h\longrightarrow {2\pi\over3}\delta_0.
\]

At an atom the sharper limit is

\[
\boxed{hQ(c,h)\longrightarrow\rho_c.}
\tag{L-105439.8}

Thus the minimal field runs from an unconditional negative coarse endpoint to
the literal residue measure at fine scale.

## 4. Why the remaining direction is hard

Increasing `h` is dissipative. The desired implication runs backward from
coarse to fine and is anti-diffusive. The simpler two-height multiplier does
not remove this structural directionality.

The gain is that the missing theorem now concerns the unique minimal field and
a second-order, rather than third-order, scale equation.

## 5. Scope

The theorem does not prevent a pole or positive contact during backward scale
flow. That is the remaining Xi-specific problem.
