# T-106090 — Least-discrepancy rough-tail L-family frontier

Claim ID: `T-106090`  
Programme aliases: `LFAM1.LEAST_DISCREPANCY_REPAIR`, `LFAM2.ROUGH_TAIL_FAMILY_FRONTIER`, `STRESS.BOOLEAN_CORE_TRIANGULAR_MOMENT`  
Status: **MAJOR UNCONDITIONAL REPAIR AND EXACT AMPLIFIED L-FAMILY NORMAL FORM; HYBRID MOMENT OPEN**  
Created: 2026-08-25  
Depends on: `L-106090--L-106094`, `R-106090`; parent PR #719 at `ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc`, especially `L-102951--L-102963`, `T-102990`  
Programme issues: #743, #736, #737  
RH status: **unproved**

This theorem resynchronizes PR #751 with the latest Hodge--Boolean parent and
replaces the stale minimum-owner positive-moment frontier by a source-exact
normal form for the canonical equal-pair obstruction `BCI102990`.

## 1. Inherited repairs now binding on this branch

At the locked parent head:

```text
squarefree Boolean Type-I global transport        PROVED by L-102953;
equal and one-sided reduced cores                  CLOSED by L-102955;
exceptional balanced owner sector                  EMPTY by L-102957;
both opposite owner products paid by cores         PROVED by L-102958;
literal-product phase packing with masks           PROVED by L-102956/L-102959;
minimum-owner total positive moment                OVERSTRONG by L-102960;
canonical equal-pair owner gauge                   LEGAL by L-102962;
owner and phase gauges                             DECOUPLED by L-102963.
```

Accordingly:

```text
BSFTI106081                         CLOSED;
MOBOSM-EX106081                    FINITE TERMINAL;
MOBOSM106081                       optional stronger route;
BCI102990                          clean live arithmetic frontier.
```

## 2. Exact least-discrepancy triangularization

After common-core extraction, the live pair is

\[
N=P g^2c^2,\qquad M=Q g^2d^2,
\qquad
c,d>1,\quad(c,d)=1.
\]

`L-106090` assigns it uniquely to the smaller of
\(P^-(c)\) and \(P^-(d)\).  If

\[
\ell=P^-(c)<P^-(d),
\]

then

\[
\ell\mid N,\qquad \ell\nmid M,\qquad P^-(d)>\ell,
\]

and

\[
1=-\sum_{h=1}^{\ell-1}e_\ell(-hM).
\]

Thus the complete coprime two-sided core is an exact triangular sum of
anchor/rough-tail interactions:

\[
\boxed{
\mathcal C_{\rm 2s}
=
-\,2\operatorname{Re}
\sum_\alpha\sum_{h=1}^{\ell_\alpha-1}
\langle A_\alpha,R_{\alpha,h}\rangle .
}
\tag{T-106090.1}
\]

The anchor index \(\alpha\) retains the common core, left reduced core,
canonical equal-pair owner coordinate, shell, carrier, Boolean representation,
marked prime and every renewal label.

Define

```text
LDART106090:
  the logarithmic adverse part of the exact triangular bilinear current
  (T-106090.1) is X^o(1), with each source occurrence and incidence weight
  used exactly once.
```

Then, by the coefficient-exact partition,

\[
\boxed{
\mathrm{LDART}_{106090}
\Longrightarrow
\mathrm{BCI}_{102990}.
}
\tag{T-106090.2}
\]

## 3. Every local rough-tail family is closed

For one frozen anchor and opposite owner fibre, `L-106091` gives the exact
even-character frame

\[
\sum_{h=1}^{\ell-1}\|R_{\alpha,h}\|^2
=
\frac{\ell+1}{\ell-1}\|R_{\alpha,1}\|^2
+
\frac{2\ell}{\ell-1}
\sum_{\substack{\eta(-1)=1\\\eta\ne1}}
\|R_{\alpha,\eta}\|^2.
\tag{T-106090.3}
\]

The principal term is the literal untwisted \(\ell\)-rough tail.  The
nonprincipal terms are genuine even Dirichlet-L channels with the
anchor-coprimality and roughness Euler factors retained.

Since \(P^-(d)>\ell\), `L-106092` proves that every fixed fibre is
automatically long-core and costs only

\[
\frac{X^{o(1)}}{g^2Q}.
\]

No local conductor, ramification, core-length or character-family-size
obstruction survives.

## 4. The anchor must be amplified before the family square

A fixed-anchor Cauchy estimate would count the same opposite tail for every
compatible anchor.  `R-106090` shows that this source-blind passage can lose
the full anchor dimension.

`L-106093` instead applies Mellin polarization first.  For each conductor
\(\ell\), common core \(g\), opposite owner product \(Q\), quadratic class
\(\sigma\), phase \(h\), and Mellin frequency \(t\), it defines

\[
Z_{g,\ell,Q,\sigma,h}(t)
=
\sum_{\substack{\alpha\\g_\alpha=g,\ \ell_\alpha=\ell}}
\overline{A_\alpha(t)}
B_{\alpha;g,Q,\sigma,h}(t).
\tag{T-106090.4}
\]

The complete anchor amplifier is therefore inside the scalar family member
before its norm is squared.

The exact family identity is

\[
\boxed{
\sum_{h=1}^{\ell-1}|Z_{g,\ell,Q,\sigma,h}(t)|^2
=
\frac{\ell+1}{\ell-1}|Z_{g,\ell,Q,\sigma,1}(t)|^2
+
\frac{2\ell}{\ell-1}
\sum_{\substack{\eta(-1)=1\\\eta\ne1}}
|Z_{g,\ell,Q,\sigma,\eta}(t)|^2.
}
\tag{T-106090.5}
\]

Here \(Z_{g,\ell,Q,\sigma,1}=Z_{g,\ell,Q,\sigma,0}\) is the principal
unphased amplitude.

## 5. Exact controlling moment

Let \(\mathfrak M_{\rm LDRT}(Y)\) be the natural source-dual
Mellin--Gauss moment of `L-106093.9`:

\[
\begin{aligned}
\mathfrak M_{\rm LDRT}(Y)
={1\over2\pi}
\sum_{g,\ell,Q}g^2\ell Q
\sum_{\sigma=\pm1}
\int |\widehat\kappa(t)|^2
\Bigg[
&{\ell+1\over\ell-1}|Z_{g,\ell,Q,\sigma,1}(t)|^2\\
&+{2\ell\over\ell-1}
\sum_{\substack{\eta(-1)=1\\\eta\ne1}}
|Z_{g,\ell,Q,\sigma,\eta}(t)|^2
\Bigg]dt.
\end{aligned}
\tag{T-106090.6}
\]

The weight \(g^2\ell Q\) is dual to the literal common-core,
selected-core-prime and opposite-owner weights; it is not a freely inserted
amplifier weight.

Define

```text
LDRTM106090:
  after the complete Hodge, Boolean, common-core, equal-pair, shell,
  marked-67 and renewal recombinations, the moment M_LDRT(Y) is Y^o(1).
```

The principal embedding, source-dual Cauchy and Mellin--Plancherel give

\[
\boxed{
\mathrm{LDRTM}_{106090}
\Longrightarrow
\mathrm{LDART}_{106090}
\Longrightarrow
\mathrm{BCI}_{102990}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-106090.7}
\]

This implication is exact.

Because the moment is positive, it has two scientifically distinct gates:

```text
LDRPCM106090:
  its anchor-amplified principal rough-tail part is Y^o(1);

LDRNEM106090:
  its anchor-amplified nonprincipal even-character part is Y^o(1).
```

Therefore

\[
\boxed{
\mathrm{LDRPCM}_{106090}
\wedge
\mathrm{LDRNEM}_{106090}
\Longrightarrow
\mathrm{LDRTM}_{106090}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-106090.8}
\]

The conjunction is genuine.  A nonprincipal family theorem does not
individualize the native principal member, while a principal estimate does
not supply the new-family moment.

## 6. The diagonal is already paid

`L-106094` expands (T-106090.6) in the left-anchor index and proves

\[
\boxed{
\mathfrak M_{\rm LDRT}^{\rm anchor\ diagonal}(Y)=Y^{o(1)}.
}
\tag{T-106090.9}
\]

The payment uses exactly the natural moment weight \(g^2\ell Q\), the
fixed-fibre phase estimate, and

\[
\ell=P^-(c)\le c,
\qquad
\sum_g g^{-2}<\infty,
\qquad
\sum_c c^{-1}\ll\log Y,
\qquad
\sum_{P=pq}P^{-1}\ll(\log\log Y)^2.
\]

Define the strictly narrower live gates

```text
LDRPCX106090:
  the distinct-anchor part of the principal amplified moment is Y^o(1);

LDRNEX106090:
  the distinct-anchor part of the nonprincipal even-family moment is Y^o(1).
```

Then

\[
\boxed{
\mathrm{LDRPCX}_{106090}
\wedge
\mathrm{LDRNEX}_{106090}
\Longrightarrow
\mathrm{LDRTM}_{106090}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-106090.10}
\]

Only coherent correlations between **different** anchors remain.

## 7. Function-field target

Define

```text
FFLDRT106090:
  over F_q[T], prove the anchor-amplified moment of the least-discrepancy
  Artin--Schreier/Kummer rough-tail family, classify every geometrically
  constant or resonant constituent, and identify the exact number-field
  trace/exponential-sum theorem suggested by the proof.
```

Known function-field RH is not itself the transfer.  The desired output is
the geometric mechanism that bounds the nonprincipal moment and its principal
individualization analogue.

## 8. Correct scientific boundary

```text
critical Hodge = squarefree Boolean source          INHERITED PROVED
Boolean Type-I global transport                     INHERITED PROVED
exceptional / equal / one-sided sectors             INHERITED CLOSED
equal-pair owner and phase-gauge decoupling          INHERITED PROVED
least-discrepancy incidence partition                PROVED EXACT
opposite core strictly rough                         PROVED EXACT
rough-tail even-character family                     PROVED EXACT
fixed-fibre family moment                            PROVED LONG-CORE
anchor-amplified Mellin--Gauss normal form           PROVED EXACT
anchor diagonal in the hybrid moment                 PROVED SUBPOWER
source-blind fixed-fibre summation                   REFUTED
LDRPCX106090 / LDRNEX106090                          OPEN
LDRTM106090 / LDART106090                            OPEN / RH-BEARING
BCI102990                                            OPEN / RH-BEARING
Riemann Hypothesis                                   UNPROVED
```

The remaining theorem is no longer a conductor/core, phase-mask, diagonal or
fixed-fibre problem.  It is the distinct-anchor hybrid moment of a completely
explicit rough-tail family.
