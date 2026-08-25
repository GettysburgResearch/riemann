# T-106440 — Spectral-asymmetry × in-band-hole frontier for ninety percent

Claim ID: `T-106440`  
Status: **UNCONDITIONAL EXACT DECOMPOSITION; TWO FIXED-CONSTANT ESTIMATES OPEN**  
Created: 2026-08-25  
Depends on: `L-106400--L-106441`; `T-106430`; pinned input `R_2/N>599/625-o(1)`  
RH status: **unproved**

## 1. The literal endpoint quantities

Let `U_T` be the reduced endpoint all-pass symbol of `L-106400`.  Let

\[
H_T=\log T
\]

and let `P_T<=P_(H_T)` be the predeclared four-channel endpoint source
projection of `L-106413`.  Put

\[
R_T=P_{H_T}-P_T.
\]

With the convolution-normalized Fourier coefficient `mathfrak u_T` of
`L-106440`, define

\[
\boxed{
\Delta_T^{\rm out}
 =\int_{H_T}^\infty(\xi-H_T)
 \left(|\mathfrak u_T(-\xi)|^2-|\mathfrak u_T(\xi)|^2\right)d\xi,
}
\tag{T-106440.1}
\]

and

\[
\boxed{
\Delta_T^{\rm hole}
 =\|H_{U_T}R_T\|_{\mathcal S_2}^2
  -\|H_{\overline{U_T}}R_T\|_{\mathcal S_2}^2.
}
\tag{T-106440.2}
\]

The exact orthogonal split `L-106440.8` gives

\[
\boxed{
\Delta_T
 =\Delta_T^{\rm out}+\Delta_T^{\rm hole},
}
\tag{T-106440.3}
\]

where `Delta_T` is the signed complement of `T-106430`.

Thus the previous single opaque tail separates into:

```text
OUT:   positive-versus-negative Fourier asymmetry beyond log T;
HOLE:  signed charge of directions omitted inside the physical band.
```

Neither quantity contains the visible four-channel source cost.

## 2. Exact conclusion

The visible source theorem gives

\[
\|H_{U_T}P_T\|_{\mathcal S_2}^2
 <\left({1\over600}+o(1)\right)N(T,2T).
\]

Consequently `L-106431` and (T-106440.3) yield

\[
\boxed{
R_0(T,2T)
\ge R_2(T,2T)
 -{1\over600}N(T,2T)
 -\bigl(\Delta_T^{\rm out}+\Delta_T^{\rm hole}\bigr)_+
 -o(N).
}
\tag{T-106440.4}

Let `a,b>=0` satisfy

\[
\boxed{a+b<{851\over15000}.}
\tag{T-106440.5}

Define

```text
OUTASYM106440(a):
  limsup (Delta_T^out)_+/N < a;

INHOLE106440(b):
  limsup (Delta_T^hole)_+/N < b.
```

Since `(x+y)_+<=x_++y_+`,

\[
\boxed{
\mathrm{OUTASYM}_{106440}(a)
\wedge
\mathrm{INHOLE}_{106440}(b)
\Longrightarrow
\liminf_{T\to\infty}{N_0(T,2T)\over N(T,2T)}>0.9.
}
\tag{T-106440.6}

A convenient symmetric target is

\[
a=b={851\over30000}-\varepsilon.
\]

This is a genuine AND-gate: the outer spectral asymmetry and the finite-frame
hole can be attacked by different mechanisms.

## 3. What already closes each sector

### Outer sector

`L-106440.11` proves exponential decay after all endpoint companion zeros and
poles within a strip of width `sigma_T` are extracted.  In particular, if the
weighted strip-boundary energies are `O(N)` and

\[
\sigma_TH_T\longrightarrow\infty,
\]

the analytic outer remainder is `o(N)`.  Thus `OUTASYM106440` is a
near-boundary divisor problem, not a remote Fourier-tail problem.

### In-band sector

The confluent matrix of `L-106415` gives exact coordinates for `R_T`; the
positive and negative Hankel energies must be retained with their signs.
`PWSAMP106420` would force this hole to be absolutely small, but is much
stronger than `INHOLE106440`.

### Safe inner sector

For a literal inner all-pass block, both positive quantities vanish:

\[
(\Delta^{\rm out})_+=(\Delta^{\rm hole})_+=0.
\]

PR #729 supplies this sign for the actual vertical-shift Xi-prime all-pass in
its safe region. `L-106441` proves that a source-exact factor/homotopy is still
needed before that result can be consumed by the finite-alpha endpoint
companion.

## 4. Exact remaining interface

The strongest current attack is therefore:

```text
SAFEHOM106441:
  factor or homotope the finite-alpha endpoint companion into the authenticated
  safe inner vertical-shift phase plus one literal unsafe residual, with the
  signed Toeplitz product cocycle retained;

OUTASYM106440:
  bound the near-boundary residual Fourier asymmetry;

INHOLE106440:
  bound the signed in-band omission trace.
```

Only the last two estimates enter (T-106440.6); `SAFEHOM106441` is a proposed
way of proving substantial portions of both.

## 5. Boundary

```text
hard-band signed coarea                         PROVED EXACT
outer-tail / in-band-hole split                 PROVED EXACT
analytic strip localization                     PROVED
safe inner blocks have no adverse contribution  PROVED EXACT
vertical-shift -> derivative-companion shortcut REFUTED
OUTASYM106440                                    OPEN
INHOLE106440                                     OPEN
ninety percent for zeta                         UNPROVED
density one / RH                                UNPROVED
```