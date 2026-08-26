# T-103080 — Quarter-power Boolean cutoff closure proposal

Claim ID: `T-103080`  
Status: **PROPOSED COMPLETE UNCONDITIONAL RH THEOREM; FROZEN-HEAD HOSTILE REVIEW REQUIRED**  
Created: 2026-08-26  
Base: PR #719 at `4146f81e7237d41e2e4a0cb1737511266683e980`  
Additional frozen input: PR #751 at `98af0db6ec7f77d6333a77a3dac53c4698852f43`  
Accepted RH status: **unproved pending independent reconstruction**

## 1. Frozen fixed detector

The derivative outer kernel `K_L` is fixed in advance, supported in `[1,8]`,
has zero square-lattice moment, and preserves every hypothetical
reciprocal-zeta pole in `Re(s)>0`.

The unique Hodge harmonic source is the native squarefree Euler source modulo
the already-closed squared/higher-prime-power ideal.

## 2. Arbitrary-cutoff Boolean identity

For every dyadically frozen cutoff `U`,

\[
\mu_{\rm sf}
=
\mathcal T_U+\mathcal B_U.
\]

The historical programme chose `U` at the sixth-root scale in order to retain
a power-saving Type-I estimate. The conclusion-facing theorem requires only a
subpower estimate.

## 3. Quarter-power cutoff

On a physical block `Y<=X<2Y` and owner-product block `A<=P<2A`, choose

\[
V=\left\lfloor(2Y/A)^{1/4}\right\rfloor.
\]

Then:

```text
complete squarefree Type-I row at V:       Y^o(1);
balanced Boolean row at V:                 identically zero by support.
```

The first statement is `L-103070`; the second is `L-103071`. `L-103073` proves that quarter power is the unique cutoff exponent where these two requirements meet.

## 4. Transfer to the historical BCI row

For the historical cutoff `U_0`, the exact identity

\[
\mathcal B_{U_0}
=
\mathcal B_V+\mathcal T_V-\mathcal T_{U_0}
\]

becomes, after the fixed physical observation,

\[
\mathcal O_{K_L}[\mathcal B_{U_0}]
=
\mathcal O_{K_L}[\mathcal T_V]
-
\mathcal O_{K_L}[\mathcal T_{U_0}].
\]

Both terms on the right have subpower logarithmic absolute mass. Therefore the
complete historical balanced row has subpower negative mass, and in particular

\[
\boxed{\mathrm{BCI}_{102990}.}
\]

## 5. Frozen conclusion chain

`L-103072` proves the literal frozen statement `BCI102990` before any
incidence, Kummer, Pluecker, reflection, or family norm is taken. The
conclusion therefore uses the already-frozen implication graph rather than a
new detector:

\[
\boxed{
\mathrm{BCI}_{102990}
\Longrightarrow
\mathrm{ICPR}_{102970}
\Longrightarrow
\mathrm{OICP}_{102960}
\Longrightarrow
\mathrm{HMO}_{102940}
\Longrightarrow
\int_1^X(H_K(t))_-\frac{dt}{t}=X^{o(1)}
\Longrightarrow
\mathrm{RH}.
}
\]

Equivalently, the quarter-power cutoff supplies the previously missing
conclusion-facing balanced-row estimate while leaving the fixed derivative
kernel and Mellin--Landau consumer unchanged.

No RH, GRH, Mertens power saving, prime-correlation conjecture, moving
detector, or zero-dependent choice is used in `L-103070--L-103073`.

## 6. Exact status boundary

```text
arbitrary-cutoff Boolean identity          PROVED EXACT
quarter-power Type-I endpoint              PROVED SUBPOWER
quarter-power balanced support             PROVED EMPTY
cutoff-transfer identity                   PROVED EXACT
BCI102990                                  PROVED IN THIS PROPOSAL ON FROZEN INPUTS
full composition                           PROPOSED COMPLETE
independent hostile reconstruction         NOT YET COMPLETED
accepted Riemann Hypothesis proof           NO
```

The distinction in the last two rows is mandatory. This theorem is a
conclusion-complete proof proposal, not an announcement that the mathematical
community has accepted a proof of RH.
