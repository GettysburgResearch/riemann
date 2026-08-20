# T100500 — Minimal ordinary-Möbius wavelet route

**Scientific status: exact route reduction and new theorems; the Riemann Hypothesis remains unproved.**

# L-100500 — Exact Abel–Mertens frame for the minimal ratio-eight wavelet

Claim ID: `L-100500`
Status: **PROVED EXACT REAL-VARIABLE THEOREM**
Created: 2026-08-20
Frozen parent: PR #675 at `7b28224ba1b072d4ccd5b93ad37c0a64e7939740`
RH status: **not assumed**

Retain PR #674's ordinary-Möbius wavelet

\[
G_\mu(X)
=
\sum_{X/8\le n\le X}
\frac{\mu(n)}{\sqrt n}K_0(X/n),
\]

where

\[
K_0(y)=
\begin{cases}
8\sqrt y-8-3\log y,&1\le y<2,\\
-8\sqrt2\sqrt y+8(1+\sqrt2)+3(1+\sqrt2)\log y
-3(2+\sqrt2)\log2,&2\le y<4,\\
4\sqrt y-8\sqrt2+9\sqrt2\log2-3\sqrt2\log y,&4\le y<8,\\
0,&\text{otherwise}.
\end{cases}
\]

Direct substitution gives

\[
K_0(1)=K_0(8)=0,
\]

and continuity at \(2\) and \(4\).

Let

\[
M(x)=\sum_{n\le x}\mu(n).
\]

Define

\[
V(y)
=
y^{-1/2}\left(\frac12K_0(y)+yK_0'(y)\right).
\]

Then

\[
V(y)=
\begin{cases}
8-\dfrac{7+\frac32\log y}{\sqrt y},&1<y<2,\\[2mm]
-8\sqrt2+
\dfrac{
7(1+\sqrt2)+\frac32(1+\sqrt2)\log y
-\frac32(2+\sqrt2)\log2
}{\sqrt y},
&2<y<4,\\[3mm]
4+
\dfrac{
-7\sqrt2+\frac92\sqrt2\log2
-\frac32\sqrt2\log y
}{\sqrt y},
&4<y<8.
\end{cases}
\tag{L-100500.1}
\]

For

\[
w_X(t)=t^{-1/2}K_0(X/t),
\]

the endpoint terms in Abel summation vanish. Therefore

\[
\begin{aligned}
G_\mu(X)
&=
-\int_{X/8}^{X}M(t)w_X'(t)\,dt\\
&=
\boxed{
X^{-1/2}\int_1^8M(X/y)V(y)\,dy.
}
\tag{L-100500.2}
\end{aligned}
\]

This is an exact compact Mertens frame: no source completion, factor-67
registry, Hall flow, owner label, or positive collapse is present.

## Quantitative Littlewood dictionary

If for some \(\theta\ge0\)

\[
M(x)=O_\varepsilon(x^{1/2+\theta+\varepsilon}),
\]

then (L-100500.2) gives

\[
\boxed{
G_\mu(X)=O_\varepsilon(X^{\theta+\varepsilon}).
}
\tag{L-100500.3}
\]

Conversely, the Mellin transform

\[
\int_1^\infty G_\mu(X)X^{-s-1}\,dX
=
\frac{
(s+\frac32)(1-\sqrt2\,2^{-s})(1-2^{-s})^2
}{
s^2(s-\frac12)\zeta(s+\frac12)
}
\tag{L-100500.4}
\]

has no multiplier zero at \(s=\rho-\frac12\) when
\(\frac12<\Re\rho<1\). Hence

\[
G_\mu(X)=O_\varepsilon(X^{\theta+\varepsilon})
\quad(\forall\varepsilon>0)
\]

implies

\[
\Re\rho\le\frac12+\theta
\]

for every nontrivial zero. In particular,

\[
\boxed{
G_\mu(X)=X^{o(1)}
\quad\Longleftrightarrow\quad
\mathrm{RH}.
}
\tag{L-100500.5}
\]

The same exponent dictionary holds for PR #675's cumulative Hardy energy.


---

# L-100501 — The critical dyadic inverse has square-root cost

Claim ID: `L-100501`
Status: **PROVED EXACT INTERFACE FIREWALL**
Created: 2026-08-20
Depends on: PR #674's minimal annihilator
RH status: **unproved**

The minimal filter is

\[
\mathscr D
=
(I-\sqrt2S_2)(I-S_2)^2.
\]

The two neutral factors have polynomial inverse coefficients,

\[
(I-S_2)^{-2}
=
\sum_{j\ge0}(j+1)S_{2^j}.
\]

The half-order factor has the exact positive inverse

\[
\boxed{
(I-\sqrt2S_2)^{-1}
=
\sum_{j\ge0}2^{j/2}S_{2^j}.
}
\tag{L-100501.1}
\]

At scale \(X\), the active coefficient mass in (L-100501.1) is comparable to

\[
\sum_{j\le\log_2X}2^{j/2}\asymp\sqrt X.
\]

Thus a source-blind reconstruction of the unfiltered critical state from one
minimal wavelet necessarily pays the full square-root scale. The critical
factor is the homogeneity \(X^{1/2}\), not an artifact of the chosen proof.

A finite-dimensional version is equally sharp. Let \(e_1,\dots,e_N\) be
orthonormal labels and let the physical collapse send every \(e_j\) to one.
Then

\[
\left\|\mathcal C\right\|=\sqrt N.
\]

Choosing equal coefficients on any subinterval on which \(K_0\) has one sign
gives labelled diagonal energy one and physical wavelet magnitude
\(\asymp\sqrt N\).

Therefore none of the following alone proves the wavelet criterion:

```text
the coefficient diagonal;
the free labelled square function;
a source-blind inverse of the dyadic annihilator;
Cauchy--Schwarz after label collapse.
```

The remaining estimate must use the actual Möbius tails in
`L-100500.2` before absolute values.


---

# T-100500 — Minimal ordinary-Möbius wavelet route to closure

Claim ID: `T-100500`
Status: **COMPLETE ROUTE REDUCTION — FINAL ARITHMETIC ESTIMATE RH-EQUIVALENT**
Created: 2026-08-20
Base: PR #675 at `7b28224ba1b072d4ccd5b93ad37c0a64e7939740`

The route is

\[
M(x)
\longrightarrow
G_\mu(X)
\longrightarrow
\text{compact Hardy energy}
\longrightarrow
\text{Mellin pole exclusion}.
\]

Every interface is exact:

1. `L-100500` gives the compact Abel–Mertens formula.
2. PR #674 gives the unique minimal ratio-eight kernel and positive
   factor-67 desmoothing.
3. PR #675 gives the exact \(L^2\) spectral abscissa.
4. `L-100501` proves that a source-blind inverse necessarily pays
   \(\sqrt X\).

The final conclusion-producing theorem may be written in any of the equivalent
forms

\[
G_\mu(X)=X^{o(1)},
\]

\[
\int_1^Y Q_X\,\frac{dX}{X^3}=Y^{o(1)},
\]

or

\[
M(X)=X^{1/2+o(1)}.
\]

Each is equivalent to RH. The wavelet route is nevertheless attractive because
it is:

```text
ordinary-Mobius;
fixed support ratio eight;
three explicit activation bands;
free of factor-67 source ownership;
free of Hall, Volterra, score, and capacity interfaces.
```

The first unsupported statement is the actual ordinary-Möbius compact
cross-core cancellation. It is not proved here.

```text
minimal wavelet and multiplier       PROVED
compact Mertens frame                PROVED
quantitative exponent dictionary     PROVED
source-blind inverse shortcut        REFUTED
MWOC100500                            OPEN / RH-EQUIVALENT
Riemann Hypothesis                   UNPROVED
```


---

# M-100500 — Hostile review protocol for the minimal-wavelet route

1. Recompute all three formulas for \(K_0\).
2. Check \(K_0(1)=K_0(8)=0\) and continuity at \(2,4\).
3. Perform Abel summation with both endpoint terms present before cancelling.
4. Verify every coefficient in \(V(y)\).
5. Rebuild the Mellin multiplier and its zero lines.
6. Keep the half-order inverse factor \(2^{j/2}\); do not replace it by a
   polynomial-cost inverse.
7. Reject any diagonal or free-labelled estimate promoted to physical
   cancellation.
8. Treat `MWOC100500` and RH as open.

Immediate falsifiers:

```text
a nonzero Abel endpoint;
a missing activation-band derivative;
a multiplier zero in the translated open strip;
a sub-square-root source-blind inverse;
MWOC or RH marked proved by the replay.
```


---

# Research report — route A: minimal wavelet

The minimal ratio-eight wavelet is the cleanest conclusion-facing object in the
repository. The new Abel formula identifies it directly as a compact average
of the ordinary Mertens function, with a completely explicit three-band
kernel. This removes the last appearance that the wavelet route might contain
an extra source or owner theorem.

The same calculation also exposes the critical inverse. Its half-order factor
has coefficients \(2^{j/2}\), so source-blind desmoothing costs exactly the
square-root scale one is trying to beat. The remaining compact cross-core
estimate is therefore the Littlewood criterion in wavelet coordinates.

RH remains unproved.
