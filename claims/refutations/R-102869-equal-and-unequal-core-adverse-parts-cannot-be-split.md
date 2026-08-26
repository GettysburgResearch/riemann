# R-102869 — Equal-core and unequal-core adverse parts cannot be separated chaos by chaos

Claim ID: `R-102869`  
Status: **PROVED COMPOSITION FIREWALL**  
Created: 2026-08-24  
Depends on: `L-102745`; `L-102886--L-102888`  
RH status: **not assumed**

The exact gcd partition

\[
\mathscr V_{\rm cross}
=
\mathscr P_{\rm eq}
+
\mathscr P_{\rm one}
+
\mathscr P_{\rm two}
\]

is a source identity.  It is not a license to estimate the three negative
parts independently.

The equal-core packet contains the pure semiprime second-chaos carrier.  For
the centered outer kernel, `L-102745` gives

\[
C_2(X)
=
-\kappa_0
\frac{\sqrt X\log\log X}{\log X}
+
O\!\left(\frac{\sqrt X}{\log X}\right),
\qquad
\kappa_0>0.
\]

The next fixed chaos has the opposite power-scale sign, and the signs continue
to alternate.  Therefore the adverse second-chaos carrier is canceled only
after the complete all-chaos core packet is recombined.

In particular,

\[
(\mathscr P_{\rm eq})_-
+
(\mathscr P_{\rm one}+\mathscr P_{\rm two})_-
\]

may be power-sized even when

\[
(\mathscr V_{\rm cross})_-
\]

is subpower.  The inequality

\[
(f+g)_-\le f_-+g_-
\]

is valid but can destroy the conclusion-bearing cancellation.

Only regions with an independent absolute estimate—such as the very-large-gcd
region of `L-102887`—may be removed before final recombination.

Any successor theorem must therefore state one coherent small-gcd scalar
containing the equal-core base and every internally phased unequal-core term.
