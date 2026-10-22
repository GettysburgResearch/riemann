# L-105113 — Buffered-selector shell averaging

Claim ID: L-105113

Status: **PROPOSED EXACT FINITE SELECTOR-SHELL IDENTITY**

Created: 2026-08-23

Depends on: L-105101; L-105103; L-105104; L-105105; L-105106

RH status: **unproved**

## 1. An outer manifest with a fixed inner target core

Use the rectangle convention

\[
\Omega_{T,\eta}
=\{z:|\Re z|<T,\ |\Im z|<\eta\}.
\tag{L-105113.1}
\]

Fix

\[
0<T_0<T_1,
\qquad
0<\eta_0<\eta_1,
\tag{L-105113.2}
\]

and let \(F\) be holomorphic on a neighborhood of
\(\overline\Omega_{T_1,\eta_1}\), with \(F',F''\not\equiv0\), and satisfying
\(F(\bar z)=\overline{F(z)}\).  Assume the
outer boundary is raw-event regular:

\[
F'(z)F''(z)\ne0
\qquad(z\in\partial\Omega_{T_1,\eta_1}).
\tag{L-105113.3}
\]

Put

\[
P=\frac F{F'},
\qquad
Q=\frac{F^2}{F'F''}.
\tag{L-105113.4}
\]

Authenticate the complete actual-pole manifests of \(P\) and \(Q\) in the
outer rectangle.  Thus, if locally

\[
F=w^mU,
\qquad
F'=w^rV,
\qquad
F''=w^sW,
\qquad
U(0)V(0)W(0)\ne0,
\]

the actual orders are

\[
d_1=(r-m)_+,
\qquad
d_2=(r+s-2m)_+,
\tag{L-105113.5}
\]

and only points with positive actual order enter the corresponding
manifest.

Let \(\mathcal T_0\) be the complete set of real, noncommon, odd-order
zeros \(c\) of \(F'\) satisfying

\[
|c|<T_0.
\tag{L-105113.6}
\]

Assume that neither endpoint \(\pm T_0\) is such a target.  If
\(r_c=\operatorname{ord}_cF'\), define

\[
\rho_c^{\rm jet}
=\frac{r_c!F(c)}{F^{(r_c+1)}(c)},
\tag{L-105113.7}
\]

and the fixed core charges

\[
A_0=-\sum_{c\in\mathcal T_0}\rho_c^{\rm jet},
\qquad
B_0=\sum_{c\in\mathcal T_0}(\rho_c^{\rm jet})^2\ge0.
\tag{L-105113.8}
\]

Apply the arbitrary-target primary selector of L-105106 to the **outer**
actual manifests, but take only \(\mathcal T_0\) as the target set.  Thus
choose the unique reduced selectors \(W_1,W_2\) with

\[
W_1(z)\equiv(z-c)^{r_c-1}\pmod{(z-c)^{r_c}},
\tag{L-105113.9}
\]

\[
W_2(z)\equiv
r_c(z-c)^{2r_c-2}
\pmod{(z-c)^{2r_c-1}}
\tag{L-105113.10}
\]

at every \(c\in\mathcal T_0\), and the zero congruence modulo the full
actual pole primary at every other point of the corresponding outer
manifest.  In particular,

\[
\deg W_\nu<D_\nu,
\tag{L-105113.11}
\]

where \(D_\nu\) is the total actual-pole order of the entire outer
manifest.  No bound for \(D_\nu\), the coefficients, or the norm of
\(W_\nu\) is asserted.

Define the already-weighted carriers

\[
H_1=W_1P,
\qquad
H_2=W_2Q.
\tag{L-105113.12}
\]

The target congruences leave one simple pole at each core target, with

\[
\operatorname{Res}_cH_1=\rho_c^{\rm jet},
\qquad
\operatorname{Res}_cH_2=(\rho_c^{\rm jet})^2.
\tag{L-105113.13}
\]

Every other actual pole in the outer rectangle is removable for the
corresponding \(H_\nu\).  Thus \(H_1,H_2\) are holomorphic on the buffer
between the fixed core and the outer boundary.  This guaranteed
holomorphic-buffer conclusion uses the complete outer manifest; a
core-only manifest does not suffice for it.

## 2. Contour-independent buffered charges

Every intermediate rectangle with

\[
T_0<T<T_1,
\qquad
\eta_0<\eta<\eta_1
\tag{L-105113.14}
\]

contains all core targets.  Since it contains no other pole of \(H_1\) or
\(H_2\), the residue theorem gives

\[
\boxed{
q_1
:=\oint_{\partial\Omega_{T,\eta}}H_1(z)\,dz
=-2\pi iA_0,
}
\tag{L-105113.15}
\]

and

\[
\boxed{
q_2
:=\oint_{\partial\Omega_{T,\eta}}H_2(z)\,dz
=2\pi iB_0.
}
\tag{L-105113.16}
\]

Here and below \(q_\nu\) denotes the unnormalized contour integral, not
\((2\pi i)^{-1}\) times that integral.  Equations (L-105113.15)--
(L-105113.16) therefore retain the full \(2\pi\) factors.

The weighted carriers extend through canceled buffer events, so the
identities themselves remain meaningful if a raw event lies on an
intermediate edge.  For use with the raw programme quotients, one may and
will select a **raw-event regular** pair satisfying

\[
F'F''\ne0
\quad\hbox{on }\partial\Omega_{T,\eta}.
\tag{L-105113.17}
\]

There are only finitely many raw events in the outer compact rectangle.
Pairs failing (L-105113.17) lie in a finite union of vertical or horizontal
lines in the \((T,\eta)\)-parameter rectangle and hence form a null set.

## 3. Exact signed shell average

Write

\[
\Delta_T=T_1-T_0,
\qquad
\Delta_\eta=\eta_1-\eta_0,
\tag{L-105113.18}
\]

and define the vertical and horizontal slicing shells

\[
\mathscr V
=\{x+iy:T_0<|x|<T_1,\ |y|<\eta_1\},
\tag{L-105113.19}
\]

\[
\mathscr H
=\{x+iy:|x|<T_1,\ \eta_0<|y|<\eta_1\}.
\tag{L-105113.20}
\]

Define the triangular slice weights

\[
\omega_\eta(y)=
\begin{cases}
\Delta_\eta,&|y|\le\eta_0,\\
\eta_1-|y|,&\eta_0<|y|<\eta_1,\\
0,&|y|\ge\eta_1,
\end{cases}
\tag{L-105113.21}
\]

and

\[
\omega_T(x)=
\begin{cases}
\Delta_T,&|x|\le T_0,\\
T_1-|x|,&T_0<|x|<T_1,\\
0,&|x|\ge T_1.
\end{cases}
\tag{L-105113.22}
\]

Let \(H\) be either buffered carrier and set

\[
q_H=\oint_{\partial\Omega_{T,\eta}}H(z)\,dz,
\tag{L-105113.23}
\]

which is independent of the intermediate pair by Section 2.  Averaging the
four counterclockwise oriented edges over
\((T,\eta)\in(T_0,T_1)\times(\eta_0,\eta_1)\), and applying Fubini, gives
the exact two-dimensional identity

\[
\boxed{
q_H=
\frac{1}{\Delta_T\Delta_\eta}
\left{
i\int_{\mathscr V}
\operatorname{sgn}(x)\omega_\eta(y)H(x+iy)\,dA
-\int_{\mathscr H}
\operatorname{sgn}(y)\omega_T(x)H(x+iy)\,dA
\right}.
}
\tag{L-105113.24}
\]

The signs follow from upward orientation on the right vertical edge,
downward orientation on the left edge, rightward orientation on the bottom
edge, and leftward orientation on the top edge.

Define the weighted absolute shell budget

\[
\mathcal E(H)
=\frac{1}{\Delta_T\Delta_\eta}
\left{
\int_{\mathscr V}\omega_\eta(y)|H(x+iy)|\,dA
+\int_{\mathscr H}\omega_T(x)|H(x+iy)|\,dA
\right}.
\tag{L-105113.25}
\]

Then

\[
\boxed{
|q_H|\le\mathcal E(H)
\le
\frac1{\Delta_T}\int_{\mathscr V}|H|\,dA
+\frac1{\Delta_\eta}\int_{\mathscr H}|H|\,dA.
}
\tag{L-105113.26}
\]

The inverse width paired with the vertical shell is
\(1/\Delta_T\), while that paired with the horizontal shell is
\(1/\Delta_\eta\).  This coordinate placement is load bearing.

## 4. Simultaneous good-rectangle selection

For a nonnegative measurable carrier \(K\), put

\[
\mathcal C_K(T,\eta)
=\int_{\partial\Omega_{T,\eta}}K(z)\,|dz|.
\tag{L-105113.27}
\]

Tonelli's theorem gives the exact mean identity

\[
\boxed{
\frac1{\Delta_T\Delta_\eta}
\int_{T_0}^{T_1}\int_{\eta_0}^{\eta_1}
\mathcal C_K(T,\eta)\,d\eta\,dT
=
\frac1{\Delta_T\Delta_\eta}
\left{
\int_{\mathscr V}\omega_\eta K\,dA
+\int_{\mathscr H}\omega_T K\,dA
\right}.
}
\tag{L-105113.28}
\]

For every prescribed nonnegative weight pair
\((\lambda_1,\lambda_2)\), take

\[
K=\lambda_1|H_1|+\lambda_2|H_2|.
\tag{L-105113.29}
\]

For that prescribed pair, there is one common raw-event regular
intermediate rectangle for both carriers for which

\[
\boxed{
\lambda_1\int_{\partial\Omega_{T,\eta}}|H_1|\,|dz|
+\lambda_2\int_{\partial\Omega_{T,\eta}}|H_2|\,|dz|
\le
\lambda_1\mathcal E(H_1)+\lambda_2\mathcal E(H_2).
}
\tag{L-105113.30}
\]

Excluding the null set of raw-irregular pairs does not change the Tonelli
average.  Combining (L-105113.15)--(L-105113.16) with
(L-105113.25) gives the moment envelope

\[
\boxed{
2\pi\bigl(\lambda_1|A_0|+\lambda_2B_0\bigr)
\le
\lambda_1\mathcal E(H_1)+\lambda_2\mathcal E(H_2).
}
\tag{L-105113.31}
\]

This is an integrated absolute-edge alternative to a pointwise denominator
margin.  It pays the complete two-dimensional cost of the **weighted**
carriers \(H_\nu=W_\nu h_\nu\).  Selector degree, coefficient growth,
conditioning, and cancellation are not factored out or discarded.

## 5. A conditional cofinal criterion

Let buffered outer rectangles be indexed by \(n\), with

\[
T_{0,n}\longrightarrow\infty,
\qquad
0<T_{0,n}<T_{1,n},
\qquad
0<\eta_{0,n}<\eta_{1,n}.
\tag{L-105113.32}
\]

At each stage authenticate the complete outer manifests, construct the
fixed-core selectors, write \(A_n,B_n\) for the stage core charges, and let
\(R_n=|\mathcal T_{0,n}|\).  Assume \(R_n\to\infty\).  Every selected
noncommon residue is nonzero, so \(B_n>0\) eventually.  On the simple,
common-zero-free stratum, suppose for some \(\mu,\nu>0\), independently,
that

\[
A_n\ge\mu R_n(1+o(1)),
\tag{L-105113.33}
\]

and that the second weighted shell budget satisfies

\[
\mathcal E(H_{2,n})
\le2\pi\nu R_n(1+o(1)).
\tag{L-105113.34}
\]

Then (L-105113.31) gives

\[
B_n\le\nu R_n(1+o(1)),
\qquad
\liminf_{n\to\infty}
\frac{A_n^2}{R_nB_n}
\ge\frac{\mu^2}{\nu}.
\tag{L-105113.35}
\]

Consequently, if

\[
\mu^2>\frac\nu2,
\tag{L-105113.36}
\]

the strict residue-coherence threshold is obtained along the selected
cofinal sequence.  The same conclusion with a specified margin
\(1/2+\delta\) requires \(\mu^2/\nu>1/2+\delta\).

The shell budget supplies only an upper bound for \(B_n\).  The signed lower
bound (L-105113.33) is separate, although the exact signed area identity
(L-105113.24) provides a possible format in which to attack it.  Multiple
targets and the L-105104 multiplicity defect remain separate from the
simple-stratum statement.

## 6. Exact cubic buffer fixture

Take

\[
F(z)=\frac{z^3}{3}-z^2+1,
\qquad
F'(z)=z(z-2),
\qquad
F''(z)=2(z-1).
\tag{L-105113.37}
\]

Choose \(0<T_0<1\), an outer width \(T_1>2\), and take \(0\) as the
sole core target.  Then

\[
\rho_0=-\frac12,
\qquad
A_0=\frac12,
\qquad
B_0=\frac14.
\tag{L-105113.38}
\]

The complete buffered selectors are

\[
W_1=1-\frac z2,
\qquad
W_2=\frac{(z-1)(z-2)}2.
\tag{L-105113.39}
\]

They give the exact cancellations

\[
\boxed{
H_1=W_1\frac F{F'}=-\frac{F}{2z},
\qquad
H_2=W_2\frac{F^2}{F'F''}=\frac{F^2}{4z}.
}
\tag{L-105113.40}
\]

Thus every intermediate rectangle has normalized charges

\[
\frac{q_1}{2\pi i}=-\frac12,
\qquad
\frac{q_2}{2\pi i}=\frac14,
\tag{L-105113.41}
\]

independently of whether the raw buffer events \(1\) and \(2\) lie inside.

## 7. Sharpness of the shell normalization

The geometric width factors in (L-105113.26) cannot be reduced in the
underlying measurable slicing lemma.  Let

\[
K_{\mathscr V}
=\mathbf1_{\{T_0<|x|<T_1,\ |y|<\eta_0/2\}}.
\tag{L-105113.42}
\]

Every intermediate rectangle has vertical cost \(2\eta_0\) and zero
horizontal cost, while

\[
\frac1{\Delta_T}\int_{\mathscr V}K_{\mathscr V}\,dA=2\eta_0.
\tag{L-105113.43}
\]

Similarly,

\[
K_{\mathscr H}
=\mathbf1_{\{|x|<T_0/2,\ \eta_0<|y|<\eta_1\}}
\tag{L-105113.44}
\]

has horizontal cost \(2T_0\) on every intermediate rectangle and

\[
\frac1{\Delta_\eta}\int_{\mathscr H}K_{\mathscr H}\,dA=2T_0.
\tag{L-105113.45}
\]

Qualitative finite-shell integrability is also insufficient for a cofinal
bound.  The entire carriers \(H_N\equiv N\) have finite cost on every fixed
shell, but every absolute boundary cost grows like
\(4N(T+\eta)\).  Quantitative normalized shell control is load bearing.

## 8. Boundary of the result

For \(F=\Xi^{(k-1)}\), the theorem is an exact finite identity conditional
on a complete actual outer manifest.  It does not provide:

- authentication of Xi pole locations, actual orders, common-event
  cancellations, or core multiplicity labels;
- a root-free or constructive cofinal outer-manifest compiler;
- bounds for \(D_\nu\), selector coefficients, primary condition numbers,
  Pick norms, or target collisions;
- an estimate of \(\mathcal E(W_\nu h_\nu)\) at the required Xi scale;
- permission to replace that weighted budget by an unweighted quotient
  budget without a separate selector estimate;
- a signed first-moment lower bound, multiplicity-defect estimate, or
  zero-count comparison;
- strict Xi jet coherence, RCMV104530, or RH.

The outer manifest exists abstractly at every finite regular stage because
the denominator events are discrete.  That observation is not an
authentication theorem: constructing \(W_\nu\) and proving its shell budget
requires the event locations and orders.  A fresh complete manifest is
needed at every cofinal stage.

No novelty is claimed for the residue theorem, primary CRT, or
Tonelli--Fubini slicing.  The contribution is the fixed-core/outer-buffer
combination: one complete outer selector freezes the desired core charge
across a two-parameter family of contours, after which an exact signed shell
identity and a simultaneous absolute good-rectangle criterion become
available.

The closest programme antecedents are L-105105--L-105106, which construct
finite-window selectors but do not freeze a smaller target core across an
outer buffer; R-105106, which warns that finite completeness gives no
cofinal edge bound; L/T-105110, which use oriented principal-part
cancellation; and L/T-105111, which certify pointwise denominator margins.
No Xi edge estimate or cofinal passage follows here.
