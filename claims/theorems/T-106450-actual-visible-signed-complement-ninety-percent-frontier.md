# T-106450 — Actual-visible × signed-complement frontier for ninety percent

Claim ID: `T-106450`  
Status: **UNCONDITIONAL EXACT REDUCTION; QUOTIENTVIS106450 AND SIGNED COMPLEMENT ESTIMATES OPEN**  
Created: 2026-08-25  
Depends on: `L-105290`, `L-106400`, `L-106431--L-106442`, `R-106432`, `L-106432--L-106435`; pinned fixed-order input \(R_2/N>599/625-o(1)\)  
RH status: **unproved**

## 1. Binding correction to T-106430/T-106440

`L-106431` and `L-106440` prove exact signed decompositions. In particular,
for the hard band \(P_{H_T}\) and a finite source \(P_T\le P_{H_T}\),

\[
\mathcal D_{P_T}(U_T)
=
\Delta_T^{\rm out}+\Delta_T^{\rm hole}.
\]

What is not proved is the inherited visible assertion

\[
\|H_{U_T}P_T\|_{\mathcal S_2}^2
<
\left(\frac1{600}+o(1)\right)N(T,2T).
\]

The cited four-channel theorem controls diagonal source densities before the
physical quotient. `R-106432` gives a finite counterfamily and `L-106434`
exhibits the omitted denominator inverse:

\[
H_{N_T/D_T}P_T
=
H_{1/D_T}T_{N_T-D_T}P_T.
\]

Therefore the `851/15000` OUT+HOLE allowance of `T-106440` is conditional on
a separate actual-visible theorem.

## 2. Exact conclusion-facing quantities

Let \(P_{H_T}\) be the literal hard-band projection in the scalar endpoint
Hardy space and define

\[
\mathcal E_T^-
=
\|H_{U_T}P_{H_T}\|_{\mathcal S_2}^2
=
\int_0^\infty
\min(H_T,r)|\widehat U_T(-r)|^2\,dr.
\tag{T-106450.1}
\]

For a finite source \(P_T\le P_{H_T}\), put
\(R_T=P_{H_T}-P_T\), and retain the exact quantities

\[
\Delta_T^{\rm out}
=
\|H_{U_T}P_{H_T}^\perp\|_{\mathcal S_2}^2
-
\|H_{\overline U_T}P_{H_T}^\perp\|_{\mathcal S_2}^2,
\tag{T-106450.2}
\]

\[
\Delta_T^{\rm hole}
=
\|H_{U_T}R_T\|_{\mathcal S_2}^2
-
\|H_{\overline U_T}R_T\|_{\mathcal S_2}^2.
\tag{T-106450.3}
\]

Then

\[
\boxed{
R_0(T,2T)
\ge
R_2(T,2T)
-
\mathcal E_T^-
-
\bigl(\Delta_T^{\rm out}+\Delta_T^{\rm hole}\bigr)_+
-o(N).
}
\tag{T-106450.4}
\]

This uses the complete hard band for the one-sided visible payment. A sharper
finite-source version may replace \(\mathcal E_T^-\) by
\(\|H_{U_T}P_T\|_{\mathcal S_2}^2\) only after that projection is typed in the
same scalar Hardy space.

## 3. Exact ninety-percent gate

The unconditional second-derivative input leaves the total allowance

\[
\frac{599}{625}-\frac9{10}
=
\frac{73}{1250}.
\]

Define

```text
ACTUALSPECTRAL106450:

limsup
  [ Eminus_T
    + (Delta_T^out + Delta_T^hole)_+ ]
  / N(T,2T)
< 73/1250.
```

Then

\[
\boxed{
\mathrm{ACTUALSPECTRAL}_{106450}
\Longrightarrow
\liminf_{T\to\infty}
\frac{N_0(T,2T)}{N(T,2T)}
>0.9.
}
\tag{T-106450.5}
\]

More flexibly, define

```text
QUOTIENTVIS106450(q):
  limsup Eminus_T/N < q.
```

If \(a,b,q\ge0\) and

\[
\boxed{q+a+b<\frac{73}{1250},}
\tag{T-106450.6}
\]

then

```text
QUOTIENTVIS106450(q)
and OUTASYM106440(a)
and INHOLE106440(b)
```

imply more than ninety percent.

At \(q=1/600\), the residual allowance is

\[
\frac{73}{1250}-\frac1{600}
=
\frac{851}{15000},
\]

so the numerical constants of `T-106430/T-106440` are retained as a
conditional corollary.

## 4. Divisor coordinates and the genuine bridge

`L-106433` writes the actual visible energy and outer tail as positive
Cauchy--exponential quadratic forms at the upper companion poles; applying it
to \(U_T^{-1}\) supplies the favorable upper-zero form. Confluent blocks are
literal derivatives of the same kernel.

`L-106441` remains binding: safe vertical-shift innerness from PR #729 does
not imply finite-alpha derivative-companion innerness. `L-106442` now closes
one important part of the bridge: if a source-exact factorization

\[
U_T=V_TW_T
\]

is proved with \(V_T\) inner, then \(V_T\) cannot worsen the **outer** signed
hard-band tail. No unspecified product commutator remains in that sector.

The in-band hole is different. A general finite source projection need not be
invariant under the causal isometry \(T_{V_T}\). The remaining bridge is
therefore:

```text
a source-exact safe/unsafe factorization of the derivative companion;
and source invariance, a causal-prefix enlargement, or a literal signed
finite-hole cocycle for the same factorization.
```

`L-106435` gives a sharp commutator modulus on the authenticated causal
vertical-shift factor. It becomes endpoint information only after the exact
factorization is proved.

## 5. Boundary

```text
signed source/complement identity                  PROVED EXACT
outer-tail / in-band-hole split                    PROVED EXACT
hard-band visible spectral formula                 PROVED EXACT
rational pole/zero Cauchy matrices                 PROVED EXACT
four-channel source-density ratio <1/600           PROVED EXACT AT SOURCE SCOPE
source ratio -> actual visible H_U energy           OPEN / REFUTED SOURCE-BLINDLY
vertical-shift -> derivative-companion shortcut     REFUTED
inner left factor cannot worsen outer tail           PROVED EXACT
finite-source hole invariance/cocycle                 OPEN
QUOTIENTVIS106450                                  OPEN / RECORD-BEARING
OUTASYM106440 / INHOLE106440                        OPEN / RECORD-BEARING
ACTUALSPECTRAL106450                               OPEN
ninety percent / density one / RH                   UNPROVED
```

