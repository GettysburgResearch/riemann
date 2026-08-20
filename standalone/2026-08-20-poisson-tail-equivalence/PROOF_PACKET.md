# T100140 standalone terminal-equivalence packet

**Scientific status: exact equivalence and mechanism audit; RH remains unproved.**

# L-100140 — Exact Cauchy–Poisson tail-square and signed-square identities

Claim ID: `L-100140`
Status: **PROVED EXACT ANALYTIC IDENTITY**
Created: 2026-08-20
Frozen parent: PR #659 at `83c17b32a99ac9e1aa5aec3168535550eb286636`
RH status: **not assumed**

Let \((c_n)\) be a finite real sequence and let \(\tau>0\). Define

\[
D_\tau(\gamma)=\sum_{n\ge1}c_n n^{\tau-i\gamma},
\qquad
P_\tau(\gamma)=\frac{\tau}{\pi(\tau^2+\gamma^2)}.
\]

Put

\[
Q_\tau(c)=\int_{\mathbb R}|D_\tau(\gamma)|^2P_\tau(\gamma)\,d\gamma.
\]

The Cauchy characteristic function is

\[
\int_{\mathbb R}e^{-i\gamma v}P_\tau(\gamma)\,d\gamma
=e^{-\tau|v|}.
\tag{L-100140.1}
\]

## 1. Positive Poisson norm

Finite expansion gives

\[
\boxed{
Q_\tau(c)=\sum_{m,n}c_mc_n\min(m,n)^{2\tau}.
}
\tag{L-100140.2}
\]

Define

\[
C_c(u)=\sum_{n\ge u}c_n.
\]

Since

\[
\min(m,n)^{2\tau}=2\tau\int_0^{\min(m,n)}u^{2\tau-1}\,du,
\]

finite Tonelli yields

\[
\boxed{
Q_\tau(c)=2\tau\int_0^\infty|C_c(u)|^2u^{2\tau-1}\,du.
}
\tag{L-100140.3}
\]

As all indices satisfy \(n\ge1\), \(C_c(u)=\sum_nc_n\) on \(0<u\le1\). Hence

\[
\boxed{
Q_\tau(c)=\left|\sum_nc_n\right|^2
+2\tau\int_1^\infty|C_c(u)|^2u^{2\tau-1}\,du.
}
\tag{L-100140.4}
\]

The off-diagonal owner packing is exactly the positive square of every
arithmetic coefficient tail. It is not supplied by the coefficient diagonal.

## 2. Signed Poisson square

Without conjugating the second factor,

\[
\boxed{
\int_{\mathbb R}D_\tau(\gamma)^2P_\tau(\gamma)\,d\gamma
=\left(\sum_nc_n\right)^2.
}
\tag{L-100140.5}
\]

For real coefficients, \(D_\tau(-\gamma)=\overline{D_\tau(\gamma)}\), so the
mixed real/imaginary term is odd. Consequently

\[
\boxed{
Q_\tau(c)-\left(\sum_nc_n\right)^2
=2\int_{\mathbb R}|\Im D_\tau(\gamma)|^2P_\tau(\gamma)\,d\gamma.
}
\tag{L-100140.6}
\]

Equations (L-100140.4) and (L-100140.6) identify the same loss in two exact
coordinates:

```text
multiplicative coordinate: weighted square of every coefficient tail;
phase coordinate:          Cauchy-averaged imaginary phase energy.
```

A positive-norm proof must bound this loss. Replacing the signed square by the
positive norm is not a cancellation theorem.


---

# L-100141 — RH implies the complete growing-moment Poisson-owner estimate

Claim ID: `L-100141`
Status: **PROVED CONDITIONAL CONVERSE / RETAINED OVERLAP WITH PR #671**
Created: 2026-08-20
Depends on: PR #659 `L-99802/L-99803`; `L-100140`
RH status: **assumed only in this lemma**

Retain PR #659's compact kernel

\[
\kappa=\mathcal KT,
\qquad
\mathcal K=(I-S_2)(I-2S_4),
\]

and on the block \(2^L\le x<2^{L+1}\) put

\[
M_L=\max\!\left(1,\left\lfloor\frac{L}{(\log(L+e))^3}\right\rfloor\right),
\qquad
\kappa_L=(I-S_2)^{M_L}\kappa.
\]

Then

\[
\operatorname{supp}\kappa_L\subset[1,2^{M_L+3}],
\tag{L-100141.1}
\]

and

\[
\|\kappa_L\|_\infty+
\operatorname{Var}_{d\log y}(\kappa_L)\ll2^{M_L}.
\tag{L-100141.2}
\]

Let

\[
\beta(n)=\mu(n)-\mathbf1_{67\mid n}\mu(n/67),
\]

\[
c_{L,y}(n)=\frac{\beta(n)}{\sqrt n}\kappa_L(y/n),
\qquad
\tau_L=\frac1{\log(L+e)}.
\]

For terminal inverse blocks with `y<1`, extend `c_{L,y}` by zero and put
`Q_L(y)=0`; every estimate below is then trivial on that final half-block.

The sequence is supported on

\[
y2^{-M_L-3}\le n\le y.
\]

## 1. RH prefix estimate

Under RH, for every \(\varepsilon>0\),

\[
M(x)=\sum_{n\le x}\mu(n)=O_\varepsilon(x^{1/2+\varepsilon}).
\tag{L-100141.3}
\]

Therefore

\[
B_\beta(x)=\sum_{n\le x}\beta(n)
=M(x)-M(x/67)
=O_\varepsilon(x^{1/2+\varepsilon}).
\tag{L-100141.4}
\]

## 2. Uniform coefficient-tail estimate

For \(u\ge0\), set

\[
C_{L,y}(u)=\sum_{n\ge u}c_{L,y}(n).
\]

Apply Abel summation separately to every shifted copy of \(\kappa\) in
\(\kappa_L\). On the support of one copy, \(n\) ranges through an interval of
fixed ratio eight. Equations (L-100141.2) and (L-100141.4) give, uniformly in the
truncation point \(u\),

\[
\boxed{
|C_{L,y}(u)|\ll_\varepsilon2^{M_L}(1+y^\varepsilon).
}
\tag{L-100141.5}
\]

## 3. Poisson norm

By `L-100140`,

\[
Q_L(y)=2\tau_L\int_0^\infty|C_{L,y}(u)|^2u^{2\tau_L-1}\,du.
\]

The sequence vanishes above \(u=y\), so

\[
\sqrt{Q_L(y)}
\ll_\varepsilon
2^{M_L}(1+y^\varepsilon)y^{\tau_L}.
\tag{L-100141.6}
\]

Uniformly for \(1\le y\le2^{L+1}\),

\[
2^{M_L}=2^{o(L)},
\qquad
y^{\tau_L}=2^{o(L)}.
\]

In the precise subpower sense—after fixing any target exponent and then taking
\(\varepsilon\) sufficiently small—

\[
\boxed{
\sup_{1\le y\le2^{L+1}}\sqrt{Q_L(y)}=2^{o(L)}.
}
\tag{L-100141.7}
\]

## 4. Positive inverse

The inverse coefficients are

\[
b_{L,k}=\binom{M_L+k-1}{k}.
\]

Their complete active mass is

\[
\sum_{k=0}^{L+1}b_{L,k}
=\binom{M_L+L+1}{M_L}=2^{o(L)}.
\tag{L-100141.8}
\]

Each logarithmic block has length \(\log2\). Combining (L-100141.7) and
(L-100141.8) gives

\[
\boxed{
\sum_{k=0}^{L+1}b_{L,k}
\int_{2^{L-k}}^{2^{L+1-k}}
\sqrt{Q_L(y)}\frac{dy}{y}=2^{o(L)}.
}
\tag{L-100141.9}
\]

Thus RH implies `GPMOC99800`.


---

# L-100142 — GPMOC and OCE are exact RH criteria on their frozen inputs

Claim ID: `L-100142`
Status: **PROVED EXACT LOGICAL EQUIVALENCE / GPMOC DIRECTION ALSO IN PR #671**
Created: 2026-08-20
Depends on: `L-100141`; PR #659 `L-99802/L-99803`; PR #660
`L-99720/L-99721/T-99720`; PR #653's scalar Mellin–Landau theorem
RH status: **equivalent**

## 1. GPMOC

PR #659 proves

\[
\mathrm{GPMOC99800}
\Longrightarrow
\text{subpower logarithmic negative mass of }\mathcal Kh
\Longrightarrow
\mathrm{RH}.
\tag{L-100142.1}
\]

The first arrow uses the positive inverse and the point estimate
\(|f_L(y)|\le\sqrt{Q_L(y)}\). The Mellin multiplier

\[
(1-2^{-s})(1-2\,4^{-s})
\]

has no zero at a translated off-line zeta pole.

`L-100141` proves the reverse implication. Hence

\[
\boxed{
\mathrm{GPMOC99800}\quad\Longleftrightarrow\quad\mathrm{RH}.
}
\tag{L-100142.2}
\]

The growing moment tower, compact support, Cauchy–Poisson gap, and subpower
inverse costs normalize the criterion; they do not reduce the logical strength
of the final off-diagonal estimate.

## 2. Source-specific frozen-orbit OCE

On PR #660's frozen native Littlewood–Paley inputs, the labelled first-owner
energy has polylogarithmic size. Here `OCE67` denotes only that source-specific
frozen-orbit contract; it is not the refuted universal `UOCE67` statement.
It asserts

\[
\int_2^Y[(\mathcal P_Xh)(X)]_-\frac{dX}{X}
\ll_\varepsilon
Y^\varepsilon
\left(1+\int_2^Y\mathcal S_X^2\frac{dX}{X}\right)^{1/2}.
\tag{L-100142.3}
\]

The established energy estimate and PR #653's zero-safe consumer give

\[
\mathrm{OCE67}\Longrightarrow\mathrm{RH}.
\tag{L-100142.4}
\]

Conversely, RH gives subpower logarithmic negative mass for the frozen
zero-safe compact observation. Since the energy factor in (L-100142.3) is at
least one,

\[
\mathrm{RH}\Longrightarrow\mathrm{OCE67}.
\tag{L-100142.5}
\]

Thus, on the stated identification and energy inputs,

\[
\boxed{
\mathrm{OCE67}\quad\Longleftrightarrow\quad\mathrm{RH}.
}
\tag{L-100142.6}
\]

A proof of either final embedding is itself a proof of RH and must be audited at
that level.


---

# R-100140 — Diagonal, local-gap, and free-labelled energies do not control the Poisson tails

Claim ID: `R-100140`
Status: **PROVED EXACT SOURCE-BLIND FIREWALL**
Created: 2026-08-20
Depends on: `L-100140`
RH status: **unproved**

Fix \(N\ge2\) and let

\[
c_n=\begin{cases}N^{-1/2},&N<n\le2N,\\0,&\text{otherwise}.
\end{cases}
\]

For every \(\tau>0\), the coefficient diagonal satisfies

\[
\sum_nc_n^2n^{2\tau}\le(2N)^{2\tau}.
\tag{R-100140.1}
\]

But by `L-100140`, every active pair has \(\min(m,n)>N\), so

\[
\boxed{Q_\tau(c)\ge N^{1+2\tau}.}
\tag{R-100140.2}
\]

Consequently

\[
\frac{Q_\tau(c)}{\sum_nc_n^2n^{2\tau}}
\ge\frac{N}{2^{2\tau}}.
\tag{R-100140.3}
\]

For \(\tau_N=1/\log\log N\), the diagonal is \(N^{o(1)}\), while

\[
Q_{\tau_N}(c)=N^{1+o(1)}.
\]

The same fixture is the physical-collapse vector from PR #660: its free
labelled norm is one and its scalar collapse is \(\sqrt N\).

Therefore none of the following, by itself, proves `GPMOC99800` or `OCE67`:

```text
the coefficient diagonal;
the local Cauchy–Poisson owner gap;
the free labelled Littlewood–Paley energy;
a source-blind Cauchy–Schwarz estimate;
a diagonal large sieve.
```

A valid proof must use the actual \(\beta\)-signs to control the tail sums
before absolute values.


---

# T-100140 — Terminal equivalence audit of the canonical scalar obstruction

Claim ID: `T-100140`
Status: **SUPPLEMENTAL BINDING STATUS THEOREM — RH UNPROVED**
Created: 2026-08-20
Base: PR #659 at `83c17b32a99ac9e1aa5aec3168535550eb286636`
Publication base: PR #671 at `2889071e9ebdc412b94cf2cfe74f1fd5142b2857`

PR #671 now independently preserves the positive-tail equivalence direction.
This supplement retains the signed phase identity and the frozen-orbit OCE
corollary that are absent there.

## 1. Exact result

`L-100140` converts the final positive Poisson norm into

\[
Q_L(y)=|f_L(y)|^2+2\tau_L\int_1^\infty
\left|\sum_{n\ge u}c_{L,y}(n)\right|^2u^{2\tau_L-1}\,du.
\]

Thus the unresolved off-diagonal owner packing is exactly a weighted
square-root-Mertens tail theorem for the complete compact filtered source.

`L-100141` proves that RH supplies all these tail estimates with the full
growing-moment and positive-inverse bookkeeping. Together with PR #659,

\[
\boxed{\mathrm{GPMOC99800}\iff\mathrm{RH}.}
\]

Likewise, on PR #660's proved energy inputs,

\[
\boxed{\mathrm{OCE67}\iff\mathrm{RH}.}
\]

## 2. What is and is not closed

```text
Cauchy–Poisson tail-square identity        PROVED EXACT
signed Poisson square identity             PROVED EXACT
RH => GPMOC                                PROVED
GPMOC => RH                                RETAINED / RECONSTRUCTED
RH <=> GPMOC                               PROVED
RH <=> OCE on native LP inputs             PROVED
diagonal/local-energy shortcut             REFUTED
unconditional GPMOC/OCE                    NOT PROVED
Riemann Hypothesis                         UNPROVED
```

## 3. Consequence for the project

The last estimate is no longer an unspecified technical embedding. It is an
exact equivalent formulation of RH. Renaming it as a Carleson theorem,
off-diagonal packing theorem, or physical-collapse lemma does not lower its
burden.

The strongest honest next attack is the coefficient-tail form

\[
2\tau_L\int_1^\infty
\left|\sum_{n\ge u}\frac{\beta(n)}{\sqrt n}
(\mathcal F_LT)(y/n)\right|^2u^{2\tau_L-1}\,du=2^{o(L)}
\]

after inverse-weighted block integration. It must exploit the actual
squarefree-core signs. Any proof of this display is already a complete RH
proof.


---

# M-100140 — Hostile review protocol

Review in this order:

1. Expand the Cauchy characteristic function and verify the `min(m,n)` kernel.
2. Reconstruct the coefficient-tail integral by finite Tonelli.
3. Check the signed Poisson square without complex conjugation.
4. Verify the logarithmic-variation bound for every shifted compact kernel.
5. Derive the RH Abel-summation tail estimate uniformly in the tail cutoff.
6. Check the subpower costs \(2^{M_L}\), \(y^{\tau_L}\), and the hockey-stick
   inverse mass.
7. Reconstruct the positive inverse and Landau implication from PR #659.
8. Verify the RH converse for OCE only on PR #660's frozen scalar and energy
   inputs.
9. Run the adjacent-block counterexample to every diagonal shortcut.
10. Do not label an RH-equivalent estimate as an independently proved lemma.

Immediate falsifiers:

```text
a missing conjugate in the positive Poisson norm;
a signed square represented as positive;
a coefficient-tail cutoff omitted;
a filter seminorm with power-sized growth;
a non-zero-safe inverse multiplier;
a diagonal estimate substituted for a tail estimate;
GPMOC or OCE marked proved by the finite replay;
RH marked established.
```


---

# Research report — the final Poisson-owner obstruction is exactly RH

The canonical scalar programme had reduced the remaining work to a compact
Cauchy–Poisson owner norm. The new calculation identifies that norm exactly:
it is the physical square plus the weighted square of every coefficient tail.

This permits a converse theorem. Under RH, square-root Mertens bounds and Abel
summation control every filtered coefficient tail. The growing filter, support,
strip, and inverse costs are all subpower, so the full GPMOC estimate follows.
The already-proved forward implication therefore makes GPMOC equivalent to RH.

The same audit applies to the native first-owner Littlewood–Paley contract OCE.
Its free labelled energy is polylogarithmic, but the physical embedding is
equivalent to RH rather than a generic martingale inequality.

A finite adjacent-block fixture shows why diagonal and local coercivity cannot
bridge the gap. The repository has reached an exact terminal criterion, not yet
an unconditional proof.
