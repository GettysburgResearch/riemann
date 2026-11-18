# Exact Mellin-phase approximation versus a dilation derivative

Let \(H=L^2((0,\infty),dx)\), \(D f=x f'\) in the distributional sense on \((0,\infty)\), and \(\mathrm{Dom}(D)=\{f\in H:xf'\in H\}\). Let \(U\) be a unitary Mellin multiplier with measurable modulus-one symbol \(u(t)\) on \(s=1/2+it\). Set \(g=U\mathbf 1_{(0,1)}\). No regularity of \(u(t)\) is needed.

## Domain and minimization

Set \(F(y)=e^{y/2}f(e^y)\). This is a unitary change of variables to \(L^2(\mathbb R,dy)\), and the distributional operator corresponding to \(D\) is \(\partial_y-1/2\). The identity follows by testing against smooth compactly supported functions or by the distributional change of variables. In particular \(f\in\mathrm{Dom}(D)\) exactly when \(F\in H^1(\mathbb R)\). Take the Mellin transform with kernel \(x^{s-1}\), so on the line it is the Fourier transform of \(F\) with positive sign and Plancherel measure \(dt/(2\pi)\). The symbol of \(D\) is \(-s\), and that of \(D^*D\) is \(q(t)=|s|^2=1/4+t^2\). The domain consists of transforms \(h\) with \(\int q|h|^2\,dt/(2\pi)<\infty\). Since \(U\) multiplies pointwise by \(u(t)\), it preserves this domain and each of the two norms exactly. This argument also covers symbols with jumps or arbitrary measurable phase.

The Mellin transform of \(g\) is \(h_g(t)=u(t)/s\), by direct integration of the indicator followed by multiplication. Its squared norm is 1 and \(g\notin\mathrm{Dom}(D)\), since \(q|h_g|^2=1\) on the whole line. For every \(\tau>0\), completion of the square in the two integrands shows that the unique minimizer of \(\|f-g\|_H^2+\tau\|Df\|_H^2\) has
\[
 h_\tau(t)=\frac{u(t)}{s(1+\tau q(t))}.
\]
This transform is admissible by direct integration. In full detail, subtracting the minimum at \(f_\tau\) from the objective at any admissible \(f\) leaves exactly \(\|f-f_\tau\|_H^2+\tau\|D(f-f_\tau)\|_H^2\), so equality is unique in \(H\).

## Exact cost and Pareto curve

Put \(A=1+\tau/4\). With \(d\nu=dt/(2\pi)\), the rational integrals from \(t=\sqrt{A/\tau}\,v\) are
\[
 J_1=\int (1+\tau q)^{-1}d\nu=\frac{1}{2\sqrt{\tau}\sqrt A},
 \qquad
 J_2=\int(1+\tau q)^{-2}d\nu=\frac{1}{4\sqrt{\tau}A^{3/2}}.
\]
Thus
\[
 B(\tau)^2:=\|Df_\tau\|_H^2=J_2
   =\frac{1}{4\sqrt{\tau}A^{3/2}},
 \qquad
 E(\tau)^2:=\|f_\tau-g\|_H^2=\tau(J_1-J_2)
   =\frac{\sqrt\tau(1+\tau/2)}{4A^{3/2}}.
\]
The latter identity also follows from \(\tau^2\int q(1+\tau q)^{-2}d\nu\).

The pointwise form \(E(\tau)^2=\int |h_g|^2[\tau q/(1+\tau q)]^2\,d\nu\) shows strict increase, continuity and limits 0 and 1 by dominated convergence. Hence each fixed error tolerance \(0<\varepsilon<1\) selects a unique \(\tau\) with \(E(\tau)=\varepsilon\). For an admissible \(f\) with \(\|f-g\|_H\le\varepsilon\), the objective inequality implies \(\tau\|Df\|_H^2\ge\tau B(\tau)^2+\varepsilon^2-\|f-g\|_H^2\). This proves constrained optimality with equality only at \(f_\tau\). For \(\varepsilon\ge1\) the unique minimizer of the derivative norm is zero, since \(q\ge1/4\). At \(\varepsilon=0\) the feasible set is empty. Conversely, \(B(\tau)^2\) decreases continuously from infinity to zero, so the same curve uniquely minimizes the error at every fixed positive derivative budget, by the same objective inequality with the roles of the bounds interchanged.

The exact product on this frontier is
\[
 \varepsilon\,\inf_{\|f-g\|_H\le\varepsilon}\|Df\|_H
     =\frac{\sqrt{1+\tau/2}}{4(1+\tau/4)^{3/2}}
     \ \longrightarrow\ \frac14
       \qquad(\varepsilon\downarrow0).
\]
The exact Pareto curve here uses the derivative cost \(\|Df\|_H\). If the cost is instead the full graph norm \((\|f\|_H^2+\|Df\|_H^2)^{1/2}\), the same sharp limit follows by comparing to the derivative lower bound and evaluating the full norm at \(f_\tau\), where \(\|f_\tau\|_H\le1\). The exact full-graph frontier is obtained separately by replacing \(q\) by \(1+q\) in the pointwise minimizer and selecting its parameter by the error constraint. No assertion about zeros or RH is needed.

## Checks

The companion numerical check integrates the complex residual and derivative of the proposed filter for a discontinuous, oscillatory multiplier. It also evaluates a fixed complex perturbation and checks the full objective difference against the predicted quadratic gap. Quadrature in \(t=\sqrt{A/\tau}\tan v\) keeps the broad and narrow profiles on the same finite interval. These tests check the constants and signs and are independent of the functional-analytic justification above.
