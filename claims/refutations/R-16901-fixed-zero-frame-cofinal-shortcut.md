# R-16901 — A fixed certified-zero frame cannot close the cofinal visible gate

Claim ID: `R-16901`  
Title: An off-line zero is exponentially amplified by boundary packets while every fixed real-zero frame remains bounded  
Status: `PROPOSED REFUTATION / SCOPE THEOREM`  
Authoring agent: `gpt56-03-k`  
Created: 2026-07-31  
Dependencies: the zero-side Weil pairing; elementary Paley--Wiener translation; zeta-zero symmetries  
Scope: prevents a false completion of `L-15307` from finitely many certified zeros alone

## 1. Purpose

`L-15307` reduces the visible Schur gate to

\[
 \sigma_L^2-\omega_L-\omega_L^2/h_L>0,
 \tag{R-16901.1}
\]

where `sigma_L^2` is a positive certified-zero frame floor and `omega_L` is one
relative radius for the complete omitted-zero/symbol/cross residual.  It is
tempting to keep one fixed proof-grade critical-line zero set, note that its
Gram is positive, and treat the residual as a routine tail.

That shortcut is false.  If one off-line zero exists, compact packets translated
toward the support boundary amplify its contribution exponentially in the
support length, while their evaluations at every fixed finite collection of
real ordinates stay uniformly bounded.

Thus a fixed finite zero frame cannot by itself yield a cofinal residual margin.
A genuine proof needs either a source-bound complete residual theorem, a growing
zero certificate with a matching analytic tail, or a different scalar
complement mechanism.

## 2. Fourier convention and zero quartet

Use the additive transform

\[
 \widehat f(z)=\int_{\mathbb R}f(t)e^{-izt}\,dt.
 \tag{R-16901.2}
\]

For a real even compactly supported function,

\[
 \widehat f(-z)=\widehat f(z),
 \qquad
 \widehat f(\overline z)=\overline{\widehat f(z)}.
 \tag{R-16901.3}
\]

In the centered zero-side convention, one zero parameter

\[
 z_0=\gamma+i\eta,
 \qquad \gamma>0,
 \qquad \eta\ne0,
 \tag{R-16901.4}
\]

comes with the quartet

\[
 z_0,\ -z_0,\ \overline z_0,\ -\overline z_0.
 \tag{R-16901.5}
\]

For a real even `f`, the quartet contribution to the Hermitian Weil quadratic
form is, up to the common positive multiplicity convention,

\[
 \boxed{
 4\,\operatorname{Re}\bigl(\widehat f(z_0)^2\bigr).}
 \tag{R-16901.6}
\]

Unlike a critical-line zero, this contribution is not a modulus square and can
have either sign.

## 3. Boundary-translated packets

Choose a nonzero real even bump

\[
 \phi\in C_c^\infty((-a,a))
 \tag{R-16901.7}
\]

with

\[
 \widehat\phi(z_0)\ne0.
 \tag{R-16901.8}
\]

For `L>a`, define the real even two-boundary packet

\[
 f_L(t)=\phi(t-L)+\phi(t+L).
 \tag{R-16901.9}
\]

Its support lies in `[-L-a,L+a]`, its `L2` norm is constant for all sufficiently
large `L`, and

\[
 \boxed{
 \widehat f_L(z)=2\cos(Lz)\widehat\phi(z).}
 \tag{R-16901.10}
\]

Assume for definiteness that `eta>0`; replacing `z_0` by its conjugate handles
the other sign.  Then

\[
 2\cos(Lz_0)
 =e^{i\gamma L-\eta L}+e^{-i\gamma L+\eta L}
 =e^{-i\gamma L+\eta L}\bigl(1+O(e^{-2\eta L})\bigr).
 \tag{R-16901.11}
\]

Consequently

\[
 \widehat f_L(z_0)^2
 =e^{2\eta L-2i\gamma L}\widehat\phi(z_0)^2
  \bigl(1+O(e^{-2\eta L})\bigr).
 \tag{R-16901.12}
\]

Choose an unbounded sequence `L_n` for which

\[
 \operatorname{Re}\left(
 e^{-2i\gamma L_n}\widehat\phi(z_0)^2
 \right)
 \le-\frac12|\widehat\phi(z_0)|^2.
 \tag{R-16901.13}
\]

Such a sequence exists because the phase `2 gamma L` traverses the circle.
Equations (R-16901.6) and (R-16901.12) then give the strict exponential upper
bound

\[
 \boxed{
 Q_{\{z_0\text{ quartet}\}}(f_{L_n},f_{L_n})
 \le-c_\phi e^{2|\eta|L_n}}
 \tag{R-16901.14}
\]

for one `c_phi>0` and all sufficiently large `n`.

## 4. Every fixed real-zero frame stays bounded

Let

\[
 Z=\{\gamma_1,\ldots,\gamma_m\}\subset\mathbb R
 \tag{R-16901.15}
\]

be any fixed finite collection of certified critical-line ordinates.  From
(R-16901.10),

\[
 |\widehat f_L(\gamma_j)|
 \le2|\widehat\phi(\gamma_j)|,
 \tag{R-16901.16}
\]

uniformly in `L`.  Hence its complete positive frame contribution satisfies

\[
 \boxed{
 \sum_{j=1}^m m_j|\widehat f_L(\gamma_j)|^2
 \le C_{\phi,Z}}
 \tag{R-16901.17}
\]

with a constant independent of the support length.

More generally, if a growing certified real-zero set contains `M_L` ordinates
and every listed multiplicity is bounded by the declared count convention, the
same construction gives the coarse upper bound `O(M_L)` for its positive frame.
To dominate (R-16901.14) by counting alone would require an exponentially large
source-bound frame or a residual theorem that already excludes the off-line
quartet.

## 5. Consequence for the visible Schur program

Suppose a proposed cofinal proof uses only:

1. one fixed finite positive critical-line zero frame;
2. a residual radius bounded independently of `L`, or by any subexponential
   function of `L`;
3. no separate theorem excluding off-line zero amplification on the chosen
   visible/ambient packet.

Then the packets `f_(L_n)` contradict the claimed residual domination whenever
an off-line zero exists.  Therefore that architecture cannot prove
(R-16901.1).

The valid alternatives are:

- a **complete residual-block estimate** in the exact metric of `L-15307`;
- a growing certified-zero block and an analytic omitted-zero budget whose
  combined source dependence is explicit;
- a weighted-deficit/complement theorem that removes these boundary directions
  from the visible sector;
- a boundary-profile/local-Weyl theorem that treats the whole zero quartet and
  its cross map before taking absolute values.

## 6. Why this is not a disproof of the positive route

The theorem does not say that the visible Schur margin is false.  It says that
the margin contains the actual global difficulty: a finite positive frame cannot
be separated from its omitted-zero residual by a support-independent estimate.

If RH is true, every zero term is a positive modulus square and the obstruction
disappears.  If RH is false, the boundary packets above are precisely the kind
of directions that a complete cofinal low packet must detect.  Thus proving the
source-bound residual margin is a substantive RH theorem, not bookkeeping.

## 7. Proof boundary

- The translation calculation and exponential separation are elementary and
  exact.
- Applying the packet as a production localized-Weil vector requires the same
  form-domain or zero-side absolute-convergence gate used elsewhere in the
  repository; smooth compact support satisfies the standard test domain.
- The theorem refutes only the **fixed-frame/subexponential-residual shortcut**.
  It does not refute growing zero frames, weighted-deficit saturation, or a
  complete local-Weyl residual theorem.
- No assertion about the existence of an off-line zeta zero is made.