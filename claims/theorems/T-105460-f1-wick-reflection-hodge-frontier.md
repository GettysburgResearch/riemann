# T-105460 — Corrected F1 Boolean–Wick configuration and reflection-Hodge frontier

Claim ID: `T-105460`

Status: **MAJOR F1 SOURCE COMPRESSION; REFLECTION IS A STRONGER SUFFICIENT ROUTE**

Corrected: 2026-08-26

The finite F1 conclusions remain exact:

```text
prime-box Chow multiplication = Boolean/Wick convolution;
canonical Beta pair owner = pure-Lefschetz incidence Green;
deterministic pair star/primitive debt = source-gauge debt;
canonical source = Beta average of one owner-core half-source square;
ordinary multiplication = Wick multiplication + repeated-label contractions.
```

For the ordinary completion \(J_U\), the reflection decomposition gives

\[
\mathcal D_{\rm out}J_U
=
-2\mathcal D_{\rm out}\mathcal O_U.
\tag{T-105460.1}
\]

The measure \(\mathcal D_{\rm out}\mathcal O_U\) has total mass zero and four
exact exponential moments. Consequently

\[
\mathrm{F1VAR}_{105460}
\Longleftrightarrow
\mathrm{REFSIG}_{106150}
\Longleftrightarrow
\mathrm{SFSC}_{106150}.
\tag{T-105460.2}
\]

## Binding correction

The bounded derivative-outer current \(H_K\) is not
\(\mathcal D_{\rm out}J_U\). The exact bridge is

\[
(5D+\tfrac32)(I-\sqrt2\,\mathsf S)H_K
=
4\mathcal D_{\rm out}J_U+H_{\rm closed}.
\tag{T-105460.3}
\]

Both inverse factors are stable on logarithmic \(L^1\). Hence

\[
\boxed{
\mathrm{F1VAR}_{105460}
\Longrightarrow
\mathrm{F1HARDY}_{105470}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-105460.4}
\]

No converse from `F1HARDY105470` to `F1VAR105460` is asserted.

The `TP2`-but-not-`TP3` firewall remains exact. The canonical owner still has
no star or primitive-cycle debt. The only correction is the observation
multiplier between the reflection distribution and the bounded detector.

```text
F1 source/Chow geometry                         PROVED EXACT
canonical owner pure Lefschetz                  PROVED EXACT
reflection signature of J_U                     PROVED EXACT
zero-mass total-variation coordinate            PROVED EXACT
direct reflection = bounded K_L identity        WITHDRAWN
stable reflection -> bounded-current transfer   PROVED
F1VAR105460 / REFSIG106150                      OPEN / RH-BEARING
F1HARDY105470 / BCI102990                       OPEN / RH-BEARING
Riemann Hypothesis                              UNPROVED
```

The full correction and positive bounded-current spectral coordinate are
`T-105490`.
