# L-100600 — Largest-prime ownership and finite cofactor squaring form one exact two-sort source

Claim ID: `L-100600`  
Status: **PROVED EXACT SOURCE IDENTITY; OPERATOR-TYPE REPAIRED**  
RH status: **not assumed**

Let `K_0` be the ratio-eight ordinary-Möbius wavelet kernel of PR #674, and write every squarefree nonunit source integer uniquely as

\[
n=pm,\qquad p=P^+(n),\qquad P^+(m)<p.
\]

Then, for `X>8`,

\[
G_\mu(X)
=-\sum_p p^{-1/2}
  \sum_{\substack{X/(8p)\le m\le X/p\\P^+(m)<p}}
  \mu(m)m^{-1/2}K_0(X/(pm)).
\tag{L-100600.1}
\]

## 1. Correct cofactor shift space

Fix an owner prime `p`.  For each prime `q<p`, let `V_q` be the unrestricted multiplicative shift on the cofactor exponent monoid,

\[
V_q e_m=e_{qm}.
\]

The shift is zero only when a later physical support condition excludes the resulting cofactor; it is **not** killed merely because `q` already divides `m`.  This distinction is essential: the completed source must contain the `q^2` state.

The native squarefree cofactor source is nevertheless

\[
\prod_{q<p}(I-q^{-1/2}V_q)e_1,
\tag{L-100600.2}
\]

because every local native Euler factor has degree one.  Its support is squarefree automatically; squarefreeness is a property of the native polynomial, not a truncation rule imposed on `V_q`.

For a cutoff `Z`, apply only on cofactor coordinates

\[
\mathscr C_{Z,p}^{(m)}
=
\prod_{\substack{q\le Z\\q<p}}(I+q^{-1/2}V_q).
\tag{L-100600.3}
\]

Since the unrestricted shifts commute,

\[
\boxed{
\mathscr C_{Z,p}^{(m)}
\prod_{q<p}(I-q^{-1/2}V_q)
=
\prod_{\substack{q\le Z\\q<p}}(I-q^{-1}V_q^2)
\prod_{Z<q<p}(I-q^{-1/2}V_q).
}
\tag{L-100600.4}
\]

Here `V_q^2=V_{q^2}`.  Thus finite cofactor squaring is source-faithful before physical summation:

- the terminal largest-prime owner `p` is untouched and remains unique;
- every cofactor prime `q<=Z` is replaced by one `q^2` state;
- every cofactor prime `Z<q<p` remains an ordinary state;
- no inverse operator is used;
- zero extension is applied only after the exact source polynomial is formed.

The earlier wording that made `V_q` vanish on repeated `q`-divisibility was incompatible with (L-100600.4) and is withdrawn by this repair.

## 2. Conditional level estimate

For a positive physical kernel satisfying the one-label scaling inequalities used in finite Euler squaring, the completed cofactor level masses admit the owner budget

\[
\Sigma_{p,Z}
\le \sum_{q\le Z}q^{-2}+\sum_{Z<q<p}q^{-1},
\tag{L-100600.5}
\]

with the sums restricted further by physical activation.  Whenever the relevant budget is below one, adjacent-level pairing signs that **completed** fixed-owner packet.

## 3. Exact boundary

Equation (L-100600.4) is a forward completion identity.  It does not provide a positive map from the completed packet back to the original unsquared packet.  In particular, a completion shift is not the same object as a divisor restriction; that separate mismatch is recorded in the corrected `L-100603` and `L-100604`.
