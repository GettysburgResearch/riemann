# L-100400 — Activation-zero upper envelope, atom-free future identity, and correct cell coarea

Claim ID: `L-100400`  
Status: **PROVED EXACT REDUCTION; GLOBAL ENVELOPE SIGN OPEN**  
Created: 2026-08-20  
Depends on: PR #673 `L-99971`; PR #668 scalar Mellin/Landau consumer  
RH status: **unproved**

Put

\[
\beta(n)=\mu(n)-\mathbf 1_{67\mid n}\mu(n/67)
\]

and use the activation-zero carrier

\[
U(y)=4(\sqrt y-1)\mathbf 1_{y\ge1}.
\]

Define

\[
Q_-(X)=\sum_{n\ge1}\frac{\beta(n)}{\sqrt n}U(X/n)^2,
\]

\[
C_2=16\frac{1-67^{-3/2}}{\zeta(3/2)},
\qquad
\mathcal E_-(X)=C_2X-Q_-(X).
\]

PR #673 proves \(Q_-(X)\ge0\) for every \(X\ge1\).

## 1. Exact all-integer kernel

Completing the absolutely convergent leading Euler product gives

\[
\boxed{
\mathcal E_-(X)
=
\sum_{n\ge1}\frac{\beta(n)}{\sqrt n}R_-(X/n),
}
\]

where

\[
R_-(y)=
\begin{cases}
16y,&0<y<1,\\
32\sqrt y-16,&y\ge1.
\end{cases}
\]

Indeed, for \(n\le X\),

\[
16(X/n)-16(\sqrt{X/n}-1)^2=32\sqrt{X/n}-16.
\]

## 2. Mellin transform

For \(\Re s>1\),

\[
\int_1^\infty U(y)^2y^{-s-1}\,dy
=
\frac{16}{s(s-1)(2s-1)}.
\]

Hence

\[
\boxed{
\mathcal M\mathcal E_-(s)
=
\frac{C_2}{s-1}
-
\frac{16(1-67^{-(s+1/2)})}
{s(s-1)(2s-1)\zeta(s+1/2)}.
}
\]

The apparent poles at \(s=1\) and \(s=1/2\) cancel.  Every hypothetical zero
\(\rho\) with \(\Re\rho>1/2\) survives at \(s=\rho-1/2\).  Therefore

\[
\boxed{
\int_1^X(\mathcal E_-(t))_-\frac{dt}{t}=X^{o(1)}
\Longrightarrow RH.
}
\tag{ACAD100400}
\]

The estimate `ACAD100400` is not proved here.

## 3. Atom-free future identity

Let

\[
L_-(X)
=
\sum_{n\le X}\frac{\beta(n)}{\sqrt n}
4(\sqrt{X/n}-1).
\]

Because \(U(1)=0\), differentiating the normalized quadratic transform produces
no activation atoms.  One obtains

\[
\boxed{
\mathcal E_-(X)
=
4X\int_X^\infty L_-(t)\frac{dt}{t^2}.
}
\]

This removes the atomic tail present in the unshifted quadratic envelope.

## 4. Exact cell spline

For an integer \(N\le X<N+1\), put

\[
T_N=\sum_{n>N}\frac{\beta(n)}{n^{3/2}},
\qquad
A_N=\sum_{n\le N}\frac{\beta(n)}n,
\qquad
B_N=\sum_{n\le N}\frac{\beta(n)}{\sqrt n}.
\]

With \(t=\sqrt X\),

\[
\boxed{
\mathcal E_-(t^2)
=
P_N(t)
=
16T_Nt^2+32A_Nt-16B_N.
}
\]

At an activation \(d=N+1\),

\[
T_{N+1}=T_N-\frac{\beta(d)}{d^{3/2}},
\quad
A_{N+1}=A_N+\frac{\beta(d)}d,
\quad
B_{N+1}=B_N+\frac{\beta(d)}{\sqrt d}.
\]

Substitution gives

\[
\boxed{
P_{N+1}(\sqrt d)=P_N(\sqrt d),
\qquad
P_{N+1}'(\sqrt d)=P_N'(\sqrt d).
}
\]

Thus \(\mathcal E_-\) is a global \(C^1\) quadratic spline in \(\sqrt X\).

## 5. Correct cell negative-mass formula

For \(P_N(t)=At^2+Bt+C\),

\[
\boxed{
\int_{\alpha^2}^{\beta^2}[-\mathcal E_-(X)]_+\frac{dX}{X}
=
\int_\alpha^\beta[-P_N(t)]_+\frac{2\,dt}{t}.
}
\]

On a negative interval this has primitive

\[
\boxed{
-At^2-2Bt-2C\log t.
}
\]

In the only possible double-negative regime

\[
A_N=-u<0,\qquad B_N=-v<0,\qquad T_N>0,
\]

the two roots are

\[
\boxed{
t_\pm=\frac{u\pm\sqrt{u^2-T_Nv}}{T_N},
}
\]

and the cell is negative exactly when \(u^2>T_Nv\).

This is the corrected finite arithmetic frontier.  It is not replaced by the
normalized-cell formula refuted in `R-100400`.
