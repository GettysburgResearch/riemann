# R-105113 — An incomplete buffer manifest changes the selected charge

Claim ID: R-105113

Status: **PROPOSED EXACT REFUTATION**

Created: 2026-08-23

Depends on: L-105105; L-105106; L-105113

RH status: **unproved**

## Refuted inference

The following implication is false:

> A selector constructed from the pole manifest of a fixed inner core may
> be reused unchanged on larger intermediate rectangles, while retaining
> the same selected core charge, without authenticating and canceling the
> events in the buffer.

## Exact cubic counterexample

Let

\[
F(z)=\frac{z^3}{3}-z^2+1.
\tag{R-105113.1}
\]

Then

\[
F'(z)=z(z-2),
\qquad
F''(z)=2(z-1),
\qquad
F'''(z)=2.
\tag{R-105113.2}
\]

Use the programme convention

\[
\Omega_{T,\eta}
=\{z:|\Re z|<T,\ |\Im z|<\eta\}.
\tag{R-105113.3}
\]

Fix any \(\eta>0\).  Choose a core width \(0<T_0<1\) and an outer width
\(T_1>2\).  The sole eligible core target is \(0\), with

\[
\rho_0=\frac{F(0)}{F''(0)}=-\frac12,
\qquad
\rho_0^2=\frac14.
\tag{R-105113.4}
\]

The core-only first and second manifests each contain only this simple
target, so their reduced selectors are both the constant \(1\).

For

\[
P=\frac F{F'},
\qquad
Q=\frac{F^2}{F'F''},
\tag{R-105113.5}
\]

the buffer contains an \(F''\)-only pole at \(1\) and another simple
\(F'\)-pole at \(2\).  Their exact additional residues are

\[
\operatorname{Res}_{z=1}Q
=\frac{F(1)^2}{F'(1)F'''(1)}
=-\frac1{18},
\tag{R-105113.6}
\]

\[
\operatorname{Res}_{z=2}P
=\frac{F(2)}{F''(2)}
=-\frac16,
\tag{R-105113.7}
\]

and

\[
\operatorname{Res}_{z=2}Q
=\left(\frac{F(2)}{F''(2)}\right)^2
=\frac1{36}.
\tag{R-105113.8}
\]

Therefore the unbuffered first charge jumps when the event at \(2\) enters:

\[
\boxed{
\frac1{2\pi i}\oint_{\partial\Omega_{T,\eta}}P(z)\,dz
=
\begin{cases}
-1/2,&0<T<2,\\
-2/3,&T>2.
\end{cases}
}
\tag{R-105113.9}
\]

The unbuffered second charge changes at both buffer events:

\[
\boxed{
\frac1{2\pi i}\oint_{\partial\Omega_{T,\eta}}Q(z)\,dz
=
\begin{cases}
1/4,&0<T<1,\\
7/36,&1<T<2,\\
2/9,&T>2.
\end{cases}
}
\tag{R-105113.10}
\]

The transition values \(T=1,2\) are raw-irregular and are excluded.

## Complete-buffer selectors restore invariance

Using the complete outer manifests while retaining only \(0\) as the target
gives

\[
W_1(z)=1-\frac z2,
\qquad
W_2(z)=\frac{(z-1)(z-2)}2.
\tag{R-105113.11}
\]

They satisfy the exact reductions

\[
\boxed{
W_1P=-\frac{F}{2z},
\qquad
W_2Q=\frac{F^2}{4z}.
}
\tag{R-105113.12}
\]

Consequently, for every raw-regular intermediate width
\(T_0<T<T_1\),

\[
\boxed{
\frac1{2\pi i}\oint W_1P\,dz=-\frac12,
\qquad
\frac1{2\pi i}\oint W_2Q\,dz=\frac14.
}
\tag{R-105113.13}
\]

This is exactly the fixed-core charge required by L-105113.

## What is and is not refuted

The example proves that a finite core manifest alone cannot justify contour
enlargement in general: an uncanceled actual buffer pole can change the
selected charge.  Full-order cancellation of every outer nontarget is the
sufficient mechanism used by L-105113 to make the buffered carriers
holomorphic and their absolute shell budgets well defined.  It is not
logically necessary merely for signed charge invariance.  For example, an
uncanceled higher-order pole can have zero residue, and a separately
authenticated residue-neutrality certificate could prevent a charge jump
without removing the pole.

It does not refute L-105113, which explicitly requires the complete outer
manifest.  It does not show that complete Xi manifests or weighted shell
bounds are impossible.  Conversely, it supplies neither of them: the
example is a cubic polynomial, not Xi, and all its event data are known
exactly.

Even after the complete manifest is supplied, selector conditioning remains
load bearing.  The buffered selectors in (R-105113.11) are benign only
because this fixture has three separated simple events.  No cofinal Xi
selector bound, RCMV104530, or RH conclusion follows.
