# What a genuine short extension of the raw inverse range would buy

20 October 2026. Status: conditional scalar deduction and research target.
**The improved inverse estimate assumed here has not been proved. No new
numerical zero-free boundary is asserted.**

The source is Liu, [arXiv:2610.26835v1](https://arxiv.org/html/2610.26835v1),
the short/long count intersection (13.16), the endpoint (14.8), and the
critical and tangent family in Lemmas 14.9--14.10. Their analytic and
continuous-certificate dependencies are retained. This note identifies
the gain required from the signed interface in
[CENTERED_INVERSE_INTERFACE.md](CENTERED_INVERSE_INTERFACE.md).

## 1. The missing analytic premise

Suppose the raw unselected inverse mean, with the same full row support,
punctures, coefficient class, and smoothing uniformity as the source,
were bounded at row scale whenever

\[
                         H\ge D^{1-\eta},\qquad \eta>0.
\tag{1}
\]

Suppose also that the original sixth-power amplification and buffered
detector argument apply to this estimate. In the amplified branch they
would give

\[
 I(U,U^r)\ll U^{1/6+(5/6)(1-\eta)r+\epsilon}.
\tag{2}
\]

Only a neighborhood of the critical long-detector length below is
needed for the scalar improvement; the old estimates can be retained
everywhere else. Neither the exact cancellation of a formal diagonal
nor a centered estimate for an isolated positive child proves (1).

## 2. Exact change in the detector count

Use the source definitions

\[
 c_\kappa=(3\kappa)^{-1},\quad
 D_\kappa(x)=3-(1+2c_\kappa)x,\quad
 P_\kappa(x)=(2-2c_\kappa x)(1-x).
\]

To avoid confusing the column length with this scalar polynomial, put

\[
 q=\frac{\delta P_\kappa(x)}{D_\kappa(x)},\qquad
 L=\frac56-\delta,\qquad \nu=\frac56\eta.
\]

The short count is unchanged. The new long count and their intersection
are exactly

\[
 \begin{split}
 R_{\rm short}(t)&=1-\delta+q(3/2-t),\\
 R_{{\rm long},\eta}(t)&=1/6+(L-\nu)t,\\
 t_\eta&=\frac{L+3q/2}{L+q-\nu},\\
 R_\eta&=1-\delta+q(3/2-t_\eta).
 \end{split}
\tag{3}
\]

These formulas apply locally where the denominator is positive and the
intersection remains in the licensed short/long range. At the inherited
critical class both conditions are strict. The full inverse envelope
also has a flat row-scale part with exponent one for
\(r\le1/(1-\eta)\). For sufficiently small eta the intersection
\(t_\eta\) remains strictly above that cutoff, and
\(R_\eta>1-\delta\), so this flat part does not replace the displayed
long branch near the critical point. In particular,

\[
 \left.\partial_\eta R_\eta\right|_{\eta=0}
              =-\frac{5q t_0}{6(L+q)}<0.
\tag{4}
\]

Using (3) only on a small neighborhood of that class, and the old count
elsewhere, is sufficient. Thus no change of the high-delta detector floor
or a negative long-count slope is being licensed by this calculation.

## 3. The resulting local scalar improvement

Write the source endpoint, now with (3), as

\[
 E_\eta=C_0+\delta/2+
 \delta x\{\ell+c_\kappa(h/4-l_y/2)\}
                    -\frac{3h}{4}(1-R_\eta),
\tag{5}
\]

where

\[
 C_0=-1/4+b/6+5\ell/4,\quad
 h=(1+b+3\ell)/2,\quad l_y=(1+b-\ell)/2.
\]

At the source critical point let
\(\kappa_0=2B_\flat-1\), \(\delta_0=\delta_c(\kappa_0)\),
\(\ell_0=\ell^*(\kappa_0)\), \(b_0=b^*(\kappa_0)\), and
\(x_0=1/2\). Partial derivatives of E below hold the other independent
variables fixed. The source proves

\[
 E=E_\delta=E_b=0,\quad E_{\delta\delta}<0,\quad
 E_{b\delta}\ne0,\quad E_x>0,
\tag{6}
\]

at this point. The first two strict derivative signs follow from the
completed-square certificate and its positive first discriminant
coefficient; the nonzero mixed derivative is the critical-class
transversality in Lemma 14.10. Also put
\(\lambda=E_\ell>0\). Differentiation along the source critical
family gives

\[
 E_\kappa=-\lambda\,\frac{d\ell^*}{d\kappa},\qquad
 \lambda-E_\kappa/2
       =\lambda\left(1+\tfrac12\frac{d\ell^*}{d\kappa}\right)>0.
\tag{7}
\]

The final positivity is part of Lemma 14.9's derivative bounds.

Impose the self-consistent relation
\(\kappa=5/6-\ell/2\), equivalently
\((1+\kappa)/2=11/12-\ell/4\). The Jacobian of
\((E_\eta,\partial_\delta E_\eta,\partial_b E_\eta)\) in
\((\ell,\delta,b)\) at eta zero is nonsingular: its determinant is
\(- (\lambda-E_\kappa/2)E_{b\delta}^2\).
The implicit function theorem therefore supplies a nearby critical
triple for all sufficiently small eta. The negative second delta
derivative and positive x derivative retain a unique local maximum at
the boundary x=1/2. Away from this neighborhood the original endpoint
has a strict compact margin, so the same small perturbation preserves
its sign. All other source scalar admissibility inequalities are strict
and remain valid.

Consequently, **if** the analytic premise (1)--(2) is supplied with the
stated scope, the source comparison has a locally improved limiting
endpoint

\[
 B(\eta)=B_\flat-\rho\eta+O(\eta^2),\qquad
 \rho=\frac{5h_0q_0t_0}
 {32(L_0+q_0)(\lambda-E_\kappa/2)}>0.
\tag{8}
\]

To obtain strict comparison at the limiting triple one decreases ell
slightly, just as in the source tangent-family argument. This is a
conditional scalar implication, not a substitute for the missing raw
inverse estimate.

For orientation only, ordinary high-precision evaluation gives

\[
 \delta_0\approx0.469344859,\quad t_0\approx1.163953577,
 \quad h_0\approx0.793947597,\quad \rho\approx0.043609724.
\]

These decimals are not directed or certified and are not used in the
proof of positivity. They explain the relevant scale: a genuine small
raw-range gain matters near detector length U raised to 1.164, rather
than only in a much longer column range. No value eta greater than zero
has been established in this packet, so (8) is not an achieved boundary.
