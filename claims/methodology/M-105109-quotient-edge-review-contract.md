# M-105109 — Review contract for quotient-edge margins

Claim ID: M-105109

Status: **HOSTILE REVIEW CONTRACT**

Created: 2026-08-23

Depends on: L-105105; L-105106; R-105106; L-105107; L-105109

RH status: **unproved**

## Denominator ledger

- Use \(\mathscr L=F'/F\) and
  \(\mathscr A=\mathscr L^2+\mathscr L'=F''/F\).
- The second quotient is \(1/(\mathscr L\mathscr A)\), not
  \(1/\mathscr A\), \(1/(\mathscr L^2+\mathscr A)\), or a product of
  independently attained minima.
- The exact second margin is
  \(m_{12}=\inf|\mathscr L\mathscr A|\).  The product
  \(m_1m_2\) gives only a sufficient lower bound.
- An upper bound for a logarithmic derivative does not imply the required
  lower margin.
- Since an extremal selector has constant boundary modulus,
  \(\|W_*h\|_E=\tau\|h\|_E\).  It does not attenuate a bad edge in
  supremum norm.

## Gauge firewall

- The gauge polynomial has depths \(M_a\in\mathbb Z_{\ge1}\) and
  \(P(\zeta)\ne0\).
- For the first gauge, \(Q_1'(\zeta)=P(\zeta)\).
- For the second gauge, \(Q_2'(\zeta)=0\) and
  \(Q_2''(\zeta)=2P(\zeta)\); the cross terms vanish at \(\zeta\).
- Multiplication by \(e^g\) preserves zeros exactly and the specified
  finite jets, but need not preserve derivative zeros or the complete
  actual-pole manifest.
- The gauge result refutes finite-jet control of a boundary margin.  It is
  not a same-manifest theorem.

## Explicit-family checks

- \(F_s=\exp(z^2/2-z^4/(4s))\) is entire, zero-free, real, and even.
- The allowed range is
  \(1<s<(5+\sqrt{17})/4\); both endpoints are excluded.
- \(F_s'\) has zeros \(0,\pm\sqrt s\), so only zero is interior.
- The polynomial
  \(P_s(x)=x^3-2sx^2+(s^2-3s)x+s^2\) has exactly one simple root in
  each of \((-\infty,-1)\), \((0,1)\), and \((s,\infty)\).
- The second manifest is target zero plus nontargets
  \(\pm\sqrt{\alpha(s)}\), all simple and noncommon.
- Check \(\mathscr A_s(0)=1\) and
  \(\mathscr A_s(\pm\sqrt s)=-2\); no quotient pole is removed by a
  common \(F',F''\) zero.
- Both target principal coefficients equal one.
- The second target normalization is \(\beta_0=-\alpha\), hence
  \(y_0=-1/\alpha\); omitting the sign must fail \(W_2(0)=1\).
- The selector norms tend to \(1\) and \((3+\sqrt5)/2\), while the two
  quotient values at one diverge.

## Scope firewall

- The result proves divergence of the unweighted and optimally weighted
  **boundary supremum envelopes**.  It does not prove divergence of any
  oriented contour integral.
- Indeed the full weighted contour integrals stay equal to the fixed target
  residue one; cancellation remains available.
- Interior-manifest completeness does not authenticate an exterior collar.
- The second nontarget locations move with \(s\); only topology, orders, and
  bounded conditioning are stable.
- The family is zero-free of order four and is not an Xi-class model.
- No Xi boundary lower margin, collar exclusion, edge cancellation,
  cofinal weighted decay, strict coherence, RCMV104530, or RH conclusion
  follows.
