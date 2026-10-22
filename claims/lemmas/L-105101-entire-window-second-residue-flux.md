# L-105101 — Entire-window second critical-residue flux

Claim ID: L-105101

Status: **PROPOSED EXACT ENTIRE-FUNCTION IDENTITY; review pending**

Created: 2026-08-23

Depends on: residue theorem; L-105100 for the global polynomial comparison;
PR #720 L-104523.3 only as exact-head, post-freeze prior-art context

RH status: **not assumed**

## 1. Regular rectangle

Let \(F\) be an entire function with \(F''\not\equiv0\), satisfying

\[
F(\bar z)=\overline{F(z)}.
\tag{L-105101.1}
\]

Fix \(T,\eta>0\) and orient the rectangle

\[
\Omega_{T,\eta}
=\{z:|\Re z|<T,\ |\Im z|<\eta\}
\tag{L-105101.2}
\]

counterclockwise. Assume:

1. every zero of \(F'\) in \(\overline\Omega_{T,\eta}\) is simple;
2. every zero of \(F''\) in \(\overline\Omega_{T,\eta}\) is simple;
3. \(F'F''\) has no zero on \(\partial\Omega_{T,\eta}\).

Put

\[
Q_F(z)=\frac{F(z)^2}{F'(z)F''(z)}.
\tag{L-105101.3}
\]

For a zero c of \(F'\), define

\[
\rho_c=\frac{F(c)}{F''(c)}.
\tag{L-105101.4}
\]

For a zero d of \(F''\), define

\[
\tau_d=\frac{F(d)^2}{F'(d)F'''(d)}.
\tag{L-105101.5}
\]

Simplicity of the \(F'\)-zeros ensures \(F''(c)\ne0\) and also excludes a
common zero of \(F'\) and \(F''\). Simplicity of the \(F''\)-zeros ensures
\(F'''(d)\ne0\).

## 2. Local residue identity

At a zero c of \(F'\),

\[
\operatorname{Res}_{z=c}Q_F=\rho_c^2.
\tag{L-105101.6}
\]

At a zero d of \(F''\),

\[
\operatorname{Res}_{z=d}Q_F=\tau_d.
\tag{L-105101.7}
\]

If the numerator also vanishes, the apparent singularity may be removable;
the displayed residue is then zero. These are the only possible poles in the
rectangle. Therefore

\[
\boxed{
B_F(T,\eta)
:=\frac1{2\pi i}\int_{\partial\Omega_{T,\eta}}Q_F(z)\,dz
=
\sum_{\substack{F'(c)=0\\c\in\Omega_{T,\eta}}}\rho_c^2
+
\sum_{\substack{F''(d)=0\\d\in\Omega_{T,\eta}}}\tau_d.
}
\tag{L-105101.8}
\]

No polynomial truncation or limiting argument is used.

## 3. Exact real/nonreal/debt split

Define the height-truncated real moment

\[
M_{2,F}(T)
=
\sum_{\substack{-T<c<T\\c\in\mathbb R,\ F'(c)=0}}
\left|\frac{F(c)}{F''(c)}\right|^2.
\tag{L-105101.9}
\]

Because F is real on the real axis, every summand in (L-105101.9) is the
algebraic square \(\rho_c^2\). Put

\[
C_F(T,\eta)
=
\sum_{\substack{F'(c)=0,\ c\in\Omega_{T,\eta}\\c\notin\mathbb R}}
\rho_c^2,
\tag{L-105101.10}
\]

and

\[
D_F(T,\eta)
=
\sum_{\substack{F''(d)=0\\d\in\Omega_{T,\eta}}}
\tau_d.
\tag{L-105101.11}
\]

Conjugate pairing makes C and D real, although neither has a fixed sign.
Splitting (L-105101.8) gives

\[
\boxed{
M_{2,F}(T)
=B_F(T,\eta)-C_F(T,\eta)-D_F(T,\eta).
}
\tag{L-105101.12}
\]

Call \(T\) **regular** when every real zero of \(F'\) or \(F''\) in
\([-T,T]\) is simple and

\[
F'(\pm T)F''(\pm T)\ne0.
\tag{L-105101.13}
\]

For any fixed regular \(T\), discreteness of the two zero sets permits a
sufficiently small positive eta for which all rectangle hypotheses hold and
the rectangle contains no nonreal zero of \(F'\). In that case \(C_F=0\).
This choice is pointwise in \(T\) and supplies no uniform lower bound for eta
as \(T\to\infty\).

## 4. Four-edge flux

The counterclockwise boundary is traversed as:

\[
-T-i\eta\to T-i\eta\to T+i\eta\to -T+i\eta\to -T-i\eta.
\]

Thus

\[
\begin{aligned}
\int_{\partial\Omega}Q_F\,dz
={}&
\int_{-T}^{T}Q_F(x-i\eta)\,dx
-\int_{-T}^{T}Q_F(x+i\eta)\,dx\\
&+i\int_{-\eta}^{\eta}
\left[Q_F(T+iy)-Q_F(-T+iy)\right]\,dy.
\end{aligned}
\tag{L-105101.14}
\]

Schwarz reflection gives
\(Q_F(x-i\eta)=\overline{Q_F(x+i\eta)}\). Hence

\[
\boxed{
\begin{aligned}
B_F(T,\eta)
={}&-\frac1\pi\int_{-T}^{T}
\Im Q_F(x+i\eta)\,dx\\
&+\frac1{2\pi}\int_{-\eta}^{\eta}
\left[Q_F(T+iy)-Q_F(-T+iy)\right]\,dy.
\end{aligned}
}
\tag{L-105101.15}
\]

The symmetric vertical integrals are real.

If F has definite parity, \(F(-z)=\varepsilon F(z)\) with
\(\varepsilon\in\{-1,1\}\), then

\[
Q_F(-z)=-Q_F(z).
\tag{L-105101.16}
\]

Consequently

\[
\boxed{
B_F(T,\eta)
=-\frac1\pi\int_{-T}^{T}
\Im Q_F(x+i\eta)\,dx
+\frac1\pi\int_{-\eta}^{\eta}Q_F(T+iy)\,dy.
}
\tag{L-105101.17}
\]

The final integral is real by Schwarz pairing.

Equivalently, the symmetry may be made explicit on the half-rectangle:

\[
\boxed{
B_F(T,\eta)
=\frac2\pi\left[
\int_0^\eta \Re Q_F(T+iy)\,dy
-\int_0^T \Im Q_F(x+i\eta)\,dx
\right].
}
\tag{L-105101.18}
\]

## 5. Xi derivative specialization

For an integer \(k\ge1\), take

\[
F=\Xi^{(k-1)}.
\]

Then

\[
Q_k(z)
=\frac{\Xi^{(k-1)}(z)^2}
{\Xi^{(k)}(z)\Xi^{(k+1)}(z)},
\tag{L-105101.19}
\]

and (L-105101.9) is exactly

\[
M_{2,k}(T)
=
\sum_{\substack{|c|<T,\ c\in\mathbb R\\\Xi^{(k)}(c)=0}}
\left|
\frac{\Xi^{(k-1)}(c)}{\Xi^{(k+1)}(c)}
\right|^2
\tag{L-105101.20}
\]

at simple zeros. Conditional on the regular-rectangle hypotheses in Section
1, every Xi derivative has definite parity, so the boundary term has the
reduced forms (L-105101.17)--(L-105101.18). The adjacent-derivative debt is

\[
D_k(T,\eta)
=
\sum_{\substack{\Xi^{(k+1)}(d)=0\\d\in\Omega_{T,\eta}}}
\frac{\Xi^{(k-1)}(d)^2}
{\Xi^{(k)}(d)\Xi^{(k+2)}(d)}.
\tag{L-105101.21}
\]

The nonreal correction C is the algebraic squared-residue sum over nonreal
zeros of \(\Xi^{(k)}\) inside the same rectangle.

The fixed-window identity itself permits a common zero of
\(\Xi^{(k-1)}\) and \(\Xi^{(k)}\): its displayed residue is zero and the
singularity is removable under the stated simplicity hypothesis. Direct use
in the PR #720 L-104522 transfer additionally requires the common-zero
exclusion imposed there, or a separate multiplicity ledger. Simplicity of all
relevant Xi-derivative zeros, and the required common-zero exclusion, are not
known globally and are not asserted here.

## 6. Relation to the global root ledger

For a real polynomial p satisfying L-105100, take an outer rectangle
containing every zero of \(p'p''\). Then

\[
B_p(\text{outer})=\mathcal K_4(p).
\]

For an inner rectangle,

\[
\boxed{
\mathcal K_4(p)-B_p(T,\eta)
=
\sum_{\substack{p'(c)=0\\c\notin\Omega_{T,\eta}}}\rho_c^2
+
\sum_{\substack{p''(d)=0\\d\notin\Omega_{T,\eta}}}\tau_d.
}
\tag{L-105101.22}
\]

Thus the missing height localization in T-105100 is exactly an exterior
residue/edge-flux problem, not a formal consequence of centered root moments.

The local circle computation at an \(F'\)-zero is already present in draft
PR #720 L-104523.3, which also warns that a large contour encloses \(F''\)
zeros. The new content here is the complete finite-rectangle ledger, its
orientation signs, its real/nonreal/debt split, and its fixed-window Xi
specialization. It is not a claim of novelty for the residue theorem or for
boundary-flux arguments in general.

At fixed \((T,\eta)\), the direct entire-function identity bypasses polynomial
exhaustion but trades the explicit \(V_2,V_4\) ledger for the unevaluated
boundary charge \(B_F\). It neither transports the global root ledger nor
closes CPASS105100. Moreover, \(B_F\) is a contour charge, not an
argument-principle index: pole-free edges need not have zero integral.

## 7. Scope

This theorem is exact at one regular finite window. It does not:

- handle multiple derivative zeros without confluent residues;
- bound B, C, or D;
- choose eta uniformly in T;
- justify a \(T\to\infty\) passage;
- establish the Xi simplicity or common-zero hypotheses;
- close the canonical-product route to the global L-105100 root ledger;
- prove RCMV104530, a positive transfer constant, or RH.
