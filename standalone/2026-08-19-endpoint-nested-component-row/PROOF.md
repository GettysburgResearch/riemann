# Endpoint-nested common-parent component-row proof candidate

For each fixed component row define

\[
 c_X(j)=\sum_{n\le X/j}\frac{\mu(n)}{\sqrt n}Q_{X/n}(j).
\]

The canonical packet containing target, component row and response coordinates
is coordinatewise nondecreasing with endpoint. Hence it is one positive
vector-valued Stieltjes source. The compact Hall flow is implemented by
partitioning positive source intervals: matched mass produces a nonnegative
target-null row difference; residual mass alone recurses. On the residual
endpoint source, disjoint random-key cylinders of widths `alpha_i` over the
smaller endpoint intervals recover the exact rough-prime children. The
complement recovers the exact causal current. Repetition terminates because
endpoints descend by factor 67.

Under the frozen exact endpoint-frame identity, direct integration of these
nonnegative observations is the full row `c_X`, so `c_X(j)>=0` for all `X,j`.

For fixed `j`,

\[
 \int_1^\infty c_X(j)X^{-s-1}dX
 =\frac{C_j}{s^2}
  +\frac{P_j(s+1/2)}{s^2\zeta(s+1/2)}.
\]

The continuation is analytic at every positive real `s`. Landau's theorem and
row nonnegativity force the defining transform to be holomorphic in
`Re(s)>0`. Every hypothetical zeta zero `rho` with `Re(rho)>1/2` survives in
some fixed row because

\[
 P_j(\rho)
 =-\frac{\rho(\rho+1)}{1-\rho}j^{-\rho-1}
  +O_\rho(j^{-\Re\rho-2}).
\]

It would create a pole of the defining Mellin integral in `Re(s)>0`, a
contradiction. Functional-equation symmetry gives the proposed RH conclusion.

The exact finite score audit is instead

\[
 \mathcal H(c_X)=P_\Lambda(X),
\]

so no `4sqrt(X)` score shortcut is used.

Status: complete proof candidate, not accepted proof. The endpoint-frame
identity and compact Hall/source interfaces require independent reconstruction;
publication does not establish RH.
