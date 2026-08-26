# L-102746 — The carrier-quotiented Wick tail has a canonical equal-pair owner

Claim ID: `L-102746`  
Status: **PROVED EXACT SECOND-CHAOS OWNER THEOREM**  
Created: 2026-08-23  
Depends on: `L-102741--L-102744`; `T-102800`  
RH status: **not assumed**

Let \(\mathcal L\) be a finite multiset of labelled prime coordinates.  The
two copies of \(67\) remain distinct labels.  Put

\[
 x_\ell=p_\ell^{-1/2}e^{-i\vartheta_\ell}U_\ell,
 \qquad
 L=\sum_{\ell\in\mathcal L}x_\ell.
\]

The carrier-quotiented prime exponential is

\[
 \mathcal Q=e^{-L}-I+L.
\]

## 1. Exact second-order Duhamel formula

The scalar identity

\[
 e^{-z}-1+z
 =z^2\int_0^1(1-t)e^{-tz}\,dt
\]

holds as a formal power series.  Since all labelled shifts commute,

\[
 \boxed{
 \mathcal Q
 =\int_0^1(1-t)L^2e^{-tL}\,dt.
 }
 \tag{L-102746.1}
\]

Equivalently, with

\[
 W_t=Le^{-tL/2},
\]

one has

\[
 \mathcal Q=\int_0^1(1-t)W_t^2\,dt.
\]

## 2. Equal ownership by unordered prime pairs

Let \(S\subseteq\mathcal L\) be squarefree with \(|S|=k\ge2\).  Its
coefficient in \(\mathcal Q\) is

\[
 (-1)^k x_S.
\]

Fix an ordered pair \((i,j)\) of distinct labels in \(S\).  In the
corresponding term of \(L^2\), the remaining \(k-2\) labels come from
\(e^{-tL}\).  The coefficient owned by \((i,j)\) is therefore

\[
 (-1)^{k-2}x_S
 \int_0^1(1-t)t^{k-2}\,dt
 =\frac{(-1)^k}{k(k-1)}x_S.
\]

There are \(k(k-1)\) ordered pairs.  Hence every unordered pair
\(\{i,j\}\subseteq S\) owns exactly

\[
 \boxed{
 \frac{(-1)^k}{\binom{k}{2}}x_S.
 }
 \tag{L-102746.2}
\]

Summing the \(\binom{k}{2}\) pair shares recovers the native coefficient
exactly.

Thus the completion homotopy produces a canonical random two-owner rule:
every squarefree occurrence of depth \(k\) is divided equally among its actual
unordered prime pairs.

## 3. Diagonal pair terms

The diagonal part of \(L^2\) is

\[
 \sum_\ell x_\ell^2.
\]

It consists only of prime-square shifts with activity \(p_\ell^{-1}\).  By
`L-102601`, `L-102743`, and the squared-core theorem of PR #715, these terms
have polylogarithmic physical cost.

Consequently the conclusion-bearing Wick current may be restricted to
**distinct unordered prime pairs** before any physical norm is taken.

## Scope

The theorem resolves pair ownership and repeated-label diagonals.  It does not
bound the physical overlap of two different integer products carrying
different owner pairs.  That remaining restriction is isolated in `T-102820`.
