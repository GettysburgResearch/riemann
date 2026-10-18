# A small positive heat threshold does not bound the original strip

Status: an exact counterexample theorem for finite symmetric probability
laws. It is not a statement about the numerical value of the
de Bruijn--Newman constant of the Riemann kernel.

**Theorem.** Fix any variance \(v>0\) and any Fourier band \(B>0\). For
every \(\varepsilon>0\), there is a symmetric, finitely supported
probability law of variance exactly \(v\) whose entire characteristic
function has zeros at distance exactly \(B\) from the real axis, but whose
heat deformation has only real zeros at every time
\(\tau\ge\tau_0\), for some \(0<\tau_0<\varepsilon\).

Here heat deformation means normalizing the measure
\(e^{\tau x^2}\,d\mu(x)\) and taking its Fourier transform. Every such
deformation exists because the support is finite.

## Proof by three spins

Choose a large \(h>0\), put

\[
 a=\cosh(Bh),\qquad
 r=\left(v-\frac{h^2}{1+a}\right)^{1/2}>0.
\]

The square root is positive for all sufficiently large \(h\). Let
\(X\) have masses \(a/(a+1)\) at zero and \(1/[2(a+1)]\) at each of
\(\pm h\), and let \(S\) be an independent fair sign. The law of
\(Y=X+rS\) has variance \(v\) and characteristic function

\[
 f_h(z)=\frac{a+\cos(hz)}{a+1}\cos(rz).                           \tag{1}
\]

The zeros of the first factor are exactly

\[
 \frac{(2k+1)\pi}{h}\ \pm\ iB,\qquad k\in\mathbb Z,             \tag{2}
\]

and those of the second are real. Thus the full zero band is exactly \(B\).

Encode \(Y\) using three signs:

\[
 Y=\frac h2\sigma_1+\frac h2\sigma_2+r\sigma_3.
\]

The zero-field Ising law with initial coupling
\(J_{12}=-\tfrac12\log a\) and \(J_{13}=J_{23}=0\) gives exactly the
law in (1). Tilting by \(e^{\tau Y^2}\) changes the couplings to

\[
 J_{12}(\tau)=\tfrac12(\tau h^2-\log a),\qquad
 J_{13}(\tau)=J_{23}(\tau)=\tau hr.                               \tag{3}
\]

The omitted constant in \(\tau Y^2\) cancels when the law is normalized.
For

\[
 \tau\ge\tau_0:=\frac{\log\cosh(Bh)}{h^2},                      \tag{4}
\]

all three couplings are nonnegative. The multivariate Lee--Yang theorem
then makes the characteristic function zero-free in each of the two open
half-planes: its external fields are \(iz(h/2,h/2,r)\), whose real parts
all have the same strict sign whenever \(\Im z\ne0\). Global spin flip
supplies the half-plane with the opposite sign. All zeros are therefore
real.

Finally \(0<\log\cosh(Bh)<Bh\), so
\(0<\tau_0<B/h\to0\). Taking \(h\) sufficiently large proves the
theorem.

## What this rules out

There is no universal inference of the form

\[
 \text{real zeros after time }\tau_0
       \quad\Longrightarrow\quad
 \text{initial band at most }g_v(\tau_0),
 \qquad g_v(\tau_0)\longrightarrow0,
\]

based only on symmetry, positivity, existence of all heat deformations,
and fixed initial variance. Thus a positive upper bound for a heat
threshold cannot simply be run backwards to obtain a narrower strip for
the original transform.

This family does **not** have a uniform exponential-moment envelope as
\(h\to\infty\); for real \(t>B\), its moment generating functions
grow without bound. A proposed reverse theorem with additional uniform
growth or source-specific hypotheses requires a separate analysis. The
present theorem does not disprove such a theorem, and does not infer any
new bound for the actual theta source.

## Primary source for the single imported theorem

C. M. Newman and W. Wu, *Constants of de Bruijn--Newman type in analytic number theory and statistical physics*,
arXiv:1901.06596v2, Section 2.5, Theorem 11, gives the multivariate
nonvanishing theorem used in (3)--(4):
<https://arxiv.org/pdf/1901.06596>.

The three-spin construction and the fixed-variance normalization are
derived here. No numerical zero search is used.
