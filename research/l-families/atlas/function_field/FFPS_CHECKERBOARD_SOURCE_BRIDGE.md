# FFPS checkerboard source bridge: quartic orientation and the Wick firewall

Status: **exact fixed-fibre source theorem and exact normalization firewall**.
The global varying-conductor FFPS moments remain open.

## Start here

The Legendre checkerboard of FFPS_CORRELATED_MASK_AMPLIFIER.md is a real
source mechanism, but only after one load-bearing correction.

For a fixed square-phase coefficient \(u\), the local coordinate really is
the unordered pair \(\{c,-c\}\), and \((c|p)\) is well defined when
\(p\equiv1\pmod4\). In live T-106120, however, the owners \(P,Q\) vary
inside fixed quadratic-class sectors and the corrected physical coordinates
are

\[
 X=Pc^2\pmod\rho,
 \qquad
 Y=Qd^2\pmod\ell.
\]

The raw core sign \((c|\rho)\) is not a function of \(X\). Modulo \(5\),

\[
 (P,c)=(1,1),\qquad (P',c')=(4,2)
\]

both give \(Pc^2=P'c'^2=1\), but their core signs are \(+1\) and \(-1\).
This is exactly the owner/core coupling corrected by R-106122.

The repair is canonical up to a harmless sector gauge. For
\(p\equiv1\pmod4\), choose a quartic character \(\xi_p\) with
\(\xi_p^2=\kappa_p\), and choose a representative \(u_{p,\sigma}\) of each
owner quadratic sector. On the physical coset
\(u_{p,\sigma}(\mathbf F_p^\times)^2\), put

\[
 \epsilon_{p,\sigma}(x)
 =\xi_p(x/u_{p,\sigma})\in\{\pm1\}.
\tag{1}
\]

In source variables this is

\[
 \boxed{
 \epsilon_{p,\sigma}(Pc^2)
 =\xi_p(P/u_{p,\sigma})\,\kappa_p(c).}
\tag{2}
\]

Thus every source representation of the same physical coordinate receives
the same sign. In the bilateral fibre, the physical checkerboard is

\[
 \boxed{
 \Pi_\pm(P,Q,c,d)
 ={1\over2}
 \left(1\pm
 \epsilon_{\rho,\tau}(Pc^2)
 \epsilon_{\ell,\sigma}(Qd^2)
 \right).}
\tag{3}
\]

Up to fixed sector scalars, the nonconstant factor in (3) is exactly the
existing L-106120 channel

\[
 \eta=\kappa_\ell,
 \qquad
 \theta=\kappa_\rho,
\]

with quartic roots \(\chi^2=\kappa_\ell\),
\(\psi^2=\kappa_\rho\). The checkerboard is therefore **spectrally already
inside the double-nonprincipal Kummer family**. What is new is the hard
physical projector before the square; a soft character-mode estimate does
not re-invert a restricted Gram matrix.

## 1. Frozen source contract

This packet locks the correlated-mask packet at commit
12f52a2235cdcda5c3c6b43a82bfcadbbb08f73c and the live PR #751 source at
head 98af0db6ec7f77d6333a77a3dac53c4698852f43.

The main live blobs are:

| claim | blob | role |
|---|---|---|
| L-106020 | dffea80b5cd7790779397fda1430d30260e79876 | even-character Gauss--Mellin identity |
| L-106024 | d94787dc2cd1cedd74d33ddc6269daf8de1cc061 | local sign-pair Gram \(pI-J\) |
| L-106120 | a8d829dc10611adb7bfb4853902bdff0ab02a065 | bilateral source variables and root characters |
| T-106121 | 9111983ae4bf199a8315310a9ce090561430c33b | corrected physical coordinates \(Pc^2,Qd^2\) |
| R-106122 | dc51ae3add697ab4cec868ef8439f864ce77d71a | owner-only/core-only collision firewall |
| R-106123 | f89cad68d67444280088d8bea7cbfb7c1eacc90d | varying-conductor firewall |
| L-106126 | b4dbebde403a11696c56a4689b2df8b53326a157 | two/four physical collision lines |
| R-106131 | 8dde14dd382e0c4fc1bb54d5da21de85ea002f41 | complete-family atomic cardinality |
| L-106131 | 37722c3f36ec7d1681f34d4329a3795e5028f7ae | Wick additive/Kummer decomposition |
| T-106140 | d5be8e376c88b63de0be19e0d9e8791624e99ae2 | live WCADD/WCKUM conjunction |

The producer resolves every declared path at that exact commit and rejects
any blob mismatch. It also hash-locks the correlated note and JSON at
12f52a223.

## 2. Why the raw core parity fails physical collapse

Suppose \(P/u=r^2\) in one owner quadratic sector. Replacing
\((P,c)\) by another representation of the same \(X=Pc^2\) can replace \(c\)
by \(r^{-1}c\). Its raw sign changes by \(\kappa_p(r)\). The mod-\(5\)
fixture above realizes precisely this possibility.

Therefore the condition

\[
 (c|\rho)(d|\ell)=+1
\tag{4}
\]

is source-readable, but under varying owners it is not a deletion of a set of
physical \(X,Y\) coordinates. Different source atoms collapsed to one
physical coordinate may land on opposite sides of (4). In that situation
the phase operator still acts on the full physical coordinate set; the hard
restricted-Gram theorem does not apply.

Equation (2) supplies the missing owner orientation. Since \(x/u\) is a
square, the value in (1) can be written without choosing complex roots as

\[
 \epsilon_{p,\sigma}(x)
 =(x/u)^{(p-1)/4}\in\{\pm1\}.
\tag{5}
\]

This also proves two gauge facts.

1. Replacing \(\xi_p\) by the other quartic root
   \(\xi_p\kappa_p\) changes nothing on
   \(x/u\in(\mathbf F_p^\times)^2\).
2. Replacing \(u\) by \(ur^2\) multiplies every sign in that sector by the
   constant \(\kappa_p(r)\). It either preserves the labels \(+/-\) or swaps
   them; the unordered projector pair and every leverage value are unchanged.

So a fourth-power orientation is needed to name the positive half, but no
mathematics depends on that name.

## 3. Bilateral physical checkerboard and CRT

Fix one live bilateral fibre

\[
 \iota=(g,\ell,\rho,\sigma,\tau),
 \qquad \ell,\rho\equiv1\pmod4,
\]

with owner classes
\(\sigma=\kappa_\ell(Q)\), \(\tau=\kappa_\rho(P)\). Normalize \(Y\) and
\(X\) by the corresponding sector representatives. The pair of square
coordinates lies in

\[
 (\mathbf F_\ell^\times)^2
 \times
 (\mathbf F_\rho^\times)^2,
\]

and CRT identifies this product with a subgroup of the units modulo
\(\ell\rho\). The product of the two unique order-two characters on these
square subgroups is the checkerboard sign in (3). Each local sign is
balanced, so each projector has exactly half of the complete physical grid.

This is a legitimate CRT parity on the **two-coordinate normalized physical
tuple**. It is not, in general, an ordinary Jacobi symbol of one integer:
\(X=Pc^2\) and \(Y=Qd^2\) come from opposite source sides. In a one-core
composite-conductor tensor such as L-106040, the analogous product can be a
literal Jacobi character of that one core. Live T-106121 is bilateral and
must retain the two-coordinate wording.

Let \(P_0=\sum_\omega z_\omega\) be the unphased member and put

\[
 H=\sum_\omega
 \epsilon_{\rho,\tau}(X_\omega)
 \epsilon_{\ell,\sigma}(Y_\omega)z_\omega.
\]

The two doubled hard-mask observations are exactly

\[
 \boxed{
 O_+=2\sum_{\Pi_+=1}z_\omega=P_0+H,
 \qquad
 O_-=2\sum_{\Pi_-=1}z_\omega=P_0-H.}
\tag{6}
\]

In L-106120.6, choose

\[
 \eta=\kappa_\ell,
 \quad \theta=\kappa_\rho,
 \quad \chi^2=\eta,
 \quad \psi^2=\theta.
\]

Then

\[
 \chi(Q)\eta(d)\psi(P)\theta(c)
 =\chi(Q)\kappa_\ell(d)\psi(P)\kappa_\rho(c),
\tag{7}
\]

which differs from the coefficient of \(H\) only by the fixed sector scalar
\(\chi(u_{\ell,\sigma})\psi(u_{\rho,\tau})\). This proves the exact
double-nonprincipal identification. The condition \(p\equiv1\pmod4\) is
also exactly what makes \(\kappa_p\) even and hence the square of a quartic
root character.

## 4. What the restricted Gram proves -- and what it does not

On the complete fixed physical grid, put

\[
 G=(\ell I-J)\otimes(\rho I-J).
\]

The hard projector deletes one checkerboard half **before** restricting the
phase form. For either half, the exact result of the correlated-mask packet
is

\[
 \boxed{
 L_{\rm cb}(\ell,\rho)
 ={4\over
 \frac{\ell+1}{\ell-1}\frac{\rho+1}{\rho-1}
 +\frac{2\ell}{\ell-1}\frac{2\rho}{\rho-1}}
 ={4(\ell-1)(\rho-1)\over5\ell\rho+\ell+\rho+1}.}
\tag{8}
\]

The optimal retained weight is uniformly \(2\). At
\((\ell,\rho)=(5,13)\), the support has six of twelve coordinates,

\[
 E_A=258,
 \qquad
 L_{\rm cb}={144\over258}={24\over43}
 <{4\over7},
\]

where \(4/7\) is the complete tensor leverage.

This hard gain is not soft mode control. If the same weight
\(\alpha=\mathbf1+w\) is evaluated in the complete inverse metric, the
constant and top modes are orthogonal, so

\[
 \boxed{
 \alpha^*G^{-1}\alpha
 ={12\over21}+{12\over65}
 ={344\over455}>{4\over7}.}
\tag{9}
\]

Thus an estimate for the \(H\) character channel, or its inclusion in
WCKUM106140, does not change \(G^{-1}\) into \(G_A^{-1}\). Spectral
containment and hard physical deletion are different operations.

## 5. The atomic/Wick obstruction survives the hard gain

Let \(E_\pm\) be the complete nonzero two-phase energy after the physical
projector. Every retained source atom has phase diagonal

\[
 (\ell-1)(\rho-1)|z_\omega|^2,
\]

while its doubled observation \(O_\pm\) has diagonal
\(4|z_\omega|^2\). The positive restricted-frame inequality is

\[
 |O_\pm|^2\le L_{\rm cb}E_\pm.
\tag{10}
\]

After normal ordering it becomes

\[
 O_\pm^\circ
 \le L_{\rm cb}E_\pm^\circ
 +\left(L_{\rm cb}(\ell-1)(\rho-1)-4\right)D_\pm.
\tag{11}
\]

For distinct eligible primes the displayed coefficient is positive; at
\((5,13)\) it is

\[
 {24\over43}\cdot48-4={980\over43}.
\]

So the local leverage does not cancel the complete-family atomic
cardinality identified by R-106131. A positive sum of such conductor
fibres is still blocked by R-106123. Taking absolute values fibre by fibre
is still forbidden by T-106140.

There is, however, an exact atomic-free projector identity. Put

\[
 D=\sum|z_\omega|^2,
 \qquad
 D_\pm=\sum_{\Pi_\pm=1}|z_\omega|^2,
\]

and define

\[
 P_0^\circ=|P_0|^2-D,
 \quad
 H^\circ=|H|^2-D,
 \quad
 O_\pm^\circ=|O_\pm|^2-4D_\pm.
\]

Parallelogram gives

\[
 \boxed{
 P_0^\circ
 ={1\over2}(O_+^\circ+O_-^\circ)-H^\circ.}
\tag{12}
\]

Only one selected quartic--quartic channel occurs in \(H\), so its atomic
Gauss weight is bounded independently of the conductors. The principal
atomic summation used in corrected L-106121 therefore also pays the atomic
part of this one selected channel. Its off-atomic varying-conductor moment
is still open.

## 6. Exact boundary and smallest next gate

Proved here:

- raw core parity fails physical collapse under varying owners;
- quartic-oriented parity (1)--(3) is a function of \(Pc^2,Qd^2\);
- its gauge dependence is only a sectorwise sign/swap;
- the bilateral checkerboard is exactly the
  \((\kappa_\ell,\kappa_\rho)\) double-nonprincipal Kummer mode;
- the hard restricted Gram gives (8), while soft complete-frame weighting
  gives (9);
- the Wick correction (11) retains a positive conductor-dimensional atomic
  term;
- the centered projector identity (12) cancels literal atoms exactly.

Not proved:

- any varying-owner or varying-conductor moment;
- that the \(p\equiv1\pmod4\) fibres dominate or replace the other fibres;
- CBKM106130, WCADD106140, WCKUM106140, BCI102990, RH, or GRH;
- a growing-\(d\) source realization. Live bilateral T-106121 has two
  marked phase primes per fibre, while the dramatic prime-prefix theorem in
  the correlated packet is a formal tensor asymptotic.

The smallest missing **algebraic** ledger item is the physical quartic
projector corollary (1)--(12); this packet supplies it. The smallest honest
**analytic** lift is a globally recombined, Wick-centered estimate for the
two conditioned currents in (12), together with the one selected
quartic--quartic Kummer trace \(H^\circ\), including all owner, core,
roughness, carrier, exceptional and ineligible-conductor ledgers. Equivalently
one may use the stronger existing WCADD106140 and WCKUM106140 gates.
No local restricted-Gram statement alone can replace that signed global
moment.

## 7. Reproduction

The producer uses only tiny exact residue and integer/rational matrix checks
at \(p=5,13\). It enumerates no conductor family, character family,
L-function, finite-field curve, or zero set. Git objects, source bytes,
exact operations, matrix cells and wall time are capped and fail closed.

    python research/l-families/atlas/function_field/ffps_checkerboard_source_bridge.py --check
    python -O research/l-families/atlas/function_field/ffps_checkerboard_source_bridge.py --check
    python -m pytest -q tests/test_ffps_checkerboard_source_bridge.py
    python -O -m pytest -q tests/test_ffps_checkerboard_source_bridge.py
    python -m ruff check research/l-families/atlas/function_field/ffps_checkerboard_source_bridge.py tests/test_ffps_checkerboard_source_bridge.py

Regenerate the canonical JSON by omitting --check from the first command.
