# An order-four extension notch isolates the elliptic three-place channel

Status: **exact all-extension inverse-designed Tate notch, exact elliptic
rank-four recurrence, and exact trace recovery for the three-place
quadratic-family cumulant defect; no new point count, sheaf construction,
zero theorem, RH, or GRH result**

Bounded replay:
[quadratic_family_three_place_tate_notch_spectroscopy.py](quadratic_family_three_place_tate_notch_spectroscopy.py).
Canonical summary:
[quadratic_family_three_place_tate_notch_spectroscopy.json](quadratic_family_three_place_tate_notch_spectroscopy.json).

Frozen source: commit
`4a9dc1bcc3fe57a2d6c883cdf4bb6079faa25db8`, theorem blob
`c3855545837643d63416b07e78e2f931b006a226`, and producer blob
`31018f73bf0afb91550f8240bfbc91e84e1c83d8`.

## 0. Outcome

Fix an odd prime \(p\) and three distinct points
\(a,b,c\in\mathbf F_p\).  Let

\[
 E:y^2=(a-z)(b-z)(c-z)
\tag{0.1}
\]

have Frobenius trace \(t=t_1\) over \(\mathbf F_p\), and write

\[
 1-tu+pu^2=(1-\alpha u)(1-\beta u).
\tag{0.2}
\]

Thus \(\alpha\beta=p\) and the extension traces are

\[
 t_n=\alpha^n+\beta^n.
\tag{0.3}
\]

Let \(\Delta_n\) be the frozen three-place third-cumulant defect over
\(\mathbf F_{p^n}\), and clear its family denominator:

\[
 R_n=A(p^n)\Delta_n,
 \qquad
 A(q)=q^4(q-1).
\tag{0.4}
\]

The frozen theorem decomposes this sequence exactly as

\[
\boxed{
 R_n=3(1+\epsilon^n)(2p^n-3)S_n
      +18(p^n-2)t_n,}
\tag{0.5}
\]

where

\[
 \epsilon=\chi_p(-1),\qquad
 S_n=\delta_1^n+\delta_2^n+\delta_3^n,\qquad
 \delta_i\in\{\pm1\}
\tag{0.6}
\]

and the \(\delta_i\) are the three oriented pair-difference squareclasses.

Let \(\mathsf E\) denote extension-degree shift,
\((\mathsf Ef)_n=f_{n+1}\), and define the orientation-universal signed-Tate
notch

\[
\boxed{
 \mathcal N_p(\mathsf E)
 = (\mathsf E^2-1)(\mathsf E^2-p^2).}
\tag{0.7}
\]

The first term in (0.5) is a linear combination of
\((\pm1)^n\) and \((\pm p)^n\), so the notch annihilates it identically:

\[
\boxed{
 H_n:=\mathcal N_p(\mathsf E)R_n
 =\mathcal N_p(\mathsf E)\bigl(18(p^n-2)t_n\bigr).}
\tag{0.8}
\]

This is an exact inverse-designed detector.  It removes every Tate and
orientation channel before any recurrence is fitted.

The surviving roots are precisely

\[
 \alpha,\quad\beta,\quad p\alpha,\quad p\beta.
\tag{0.9}
\]

All four have nonzero amplitudes after notching.  Hence \(H_n\) has the
exact minimal characteristic polynomial

\[
\boxed{
 \mathcal P_{E,p}(T)
 =(T^2-tT+p)(T^2-ptT+p^3).}
\tag{0.10}
\]

Equivalently,

\[
\boxed{
\begin{aligned}
 \mathcal P_{E,p}(T)
 ={}&T^4-(p+1)tT^3+(p^3+p+pt^2)T^2\\
    &-p^2(p+1)tT+p^4.
\end{aligned}}
\tag{0.11}
\]

The recurrence itself recovers the elliptic trace:

\[
\boxed{t=-{[T^3]\mathcal P_{E,p}(T)\over p+1}.}
\tag{0.12}
\]

Thus the low-rank recurrence moonshot which fails for the raw two-place
higher cumulants succeeds after inverse design at three places: a universal
order-four nuisance notch leaves exactly one elliptic Frobenius packet.

## 1. Exact extension adapter

For a base-field element \(x\in\mathbf F_p^*\),

\[
 \chi_{p^n}(x)=\chi_p(x)^n.
\tag{1.1}
\]

Apply this to \(-1\) and to the three pair differences.  The frozen formula

\[
 A(q)\Delta^{(3)}_3
 =3(1+\chi_q(-1))(2q-3)
   \sum_{i=1}^3\chi_q(d_i)
  +18(q-2)t_q
\tag{1.2}
\]

then becomes (0.5) at \(q=p^n\).  The trace \(t_q=t_n\) is (0.3) because
the curve (0.1) is the base change of one fixed elliptic curve over
\(\mathbf F_p\).

This fixed-base-tower requirement is essential.  Choosing unrelated triples
over each \(\mathbf F_{p^n}\) would not define one Frobenius recurrence.

## 2. The nuisance spectrum and the universal notch

Expand one orientation summand:

\[
 3(1+\epsilon^n)(2p^n-3)\delta^n
 =6(\delta p)^n-9\delta^n
  +6(\epsilon\delta p)^n-9(\epsilon\delta)^n.
\tag{2.1}
\]

Every nuisance root is therefore in \(\{1,-1,p,-p\}\).  Equation (0.7)
is the monic polynomial with exactly those four roots, proving (0.8).

It is also degree-minimal among scalar shift filters which work for every
formal orientation profile: any such polynomial must vanish at all four
possible roots.  For one fixed triple, accidental sign absences can permit a
smaller filter; the theorem concerns the member-blind orientation-universal
notch.

In explicit finite-difference form,

\[
 H_n=R_{n+4}-(1+p^2)R_{n+2}+p^2R_n.
\tag{2.2}
\]

Only three tower rows separated by two extension degrees are needed to
evaluate the notch at one \(n\).

## 3. The elliptic spectrum survives

The geometric part of (0.5) is

\[
 G_n=18(p^n-2)t_n
 =18\bigl((p\alpha)^n+(p\beta)^n\bigr)
  -36\bigl(\alpha^n+\beta^n\bigr).
\tag{3.1}
\]

Applying \(\mathcal N_p\) multiplies the amplitude of a root \(\lambda\)
by

\[
 (\lambda^2-1)(\lambda^2-p^2).
\tag{3.2}
\]

The four roots in (0.9) have absolute values \(p^{1/2}\) and
\(p^{3/2}\), so none is a notch root of absolute value \(1\) or \(p\).
They are distinct: \(\alpha\ne\beta\) because an odd prime cannot satisfy
\(t^2=4p\), and a cross-equality such as \(\alpha=p\beta\) would force a
Frobenius root to have absolute value one.  Thus all four amplitudes are
nonzero and distinct-root Vandermonde minimality applies.

The roots \(\alpha,\beta\) have polynomial \(T^2-tT+p\).  Scaling both by
\(p\) gives \(T^2-ptT+p^3\).  Their product is (0.10), proving the exact
rank-four recurrence and (0.11)--(0.12).

## 4. Detector-design interpretation

The two-place extension spectroscopy finds only signed-Tate modes, with
minimal ranks rising to seven, fourteen, and sixteen.  The present packet
uses that diagnosis constructively:

~~~text
clear the exact family denominator
  -> list every universal nuisance eigenvalue
  -> build its primitive shift-polynomial notch
  -> apply the notch before fitting
  -> recover one named elliptic Frobenius recurrence
~~~

This is a concrete instance of inverse-designed cohomological spectroscopy.
It does not infer an elliptic curve from a numerical fit: the geometric
adapter is frozen first, and the recurrence is derived from its exact
\(L\)-polynomial.

The result suggests a falsifiable template for more complicated detectors.
After all explicitly known signed-Tate roots are notched, any surviving
minimal recurrence root not of the form \(\pm p^j\) must come from a
different channel.  Naming that channel still requires an exact geometric
adapter and normalization; recurrence matching alone is not enough.

No number-field transfer, family estimate, principal-member amplifier,
individualization theorem, zero theorem, RH implication, or GRH implication
is supplied.

## 5. Claim ledger

| statement | grade |
|---|---|
| fixed-base extension adapter (0.5) | **PROVED FROM THE FROZEN ALL-\(q\) FORMULA** |
| nuisance signed-Tate support | **PROVED EXACT** |
| universal primitive notch (0.7) | **PROVED EXACT AND DEGREE-MINIMAL IN ITS DECLARED CATEGORY** |
| exact elliptic isolation (0.8) | **PROVED EXACT** |
| rank-four characteristic polynomial (0.10) | **PROVED EXACT AND MINIMAL** |
| trace recovery (0.12) | **PROVED EXACT** |
| sheaf construction or new cohomology theorem | **NOT CLAIMED** |
| RH or GRH | **NOT PROVED** |

## 6. Bounded replay

The replay uses the two base-prime controls already present in the frozen
packet: \((p,t)=(3,0)\) and \((5,-2)\).  It tests all formal orientation
sign profiles, actual extension degrees through twenty-eight, exact nuisance
annihilation, direct-versus-spectral notch values, the order-four recurrence,
minimal root counts starting at extension degree one, and trace recovery.  It
enumerates no finite-field
element, polynomial, curve, point, prime, or zero and performs no
floating-point fit.

~~~text
python -B research/l-families/atlas/function_field/quadratic_family_three_place_tate_notch_spectroscopy.py --check
python -B -O research/l-families/atlas/function_field/quadratic_family_three_place_tate_notch_spectroscopy.py --check
python -B -m unittest tests.test_quadratic_family_three_place_tate_notch_spectroscopy
python -B -O -m unittest tests.test_quadratic_family_three_place_tate_notch_spectroscopy
python -B -m ruff check research/l-families/atlas/function_field/quadratic_family_three_place_tate_notch_spectroscopy.py tests/test_quadratic_family_three_place_tate_notch_spectroscopy.py
python -B -m ruff format --check research/l-families/atlas/function_field/quadratic_family_three_place_tate_notch_spectroscopy.py tests/test_quadratic_family_three_place_tate_notch_spectroscopy.py
~~~
