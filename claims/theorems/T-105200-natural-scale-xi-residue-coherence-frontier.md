# T-105200 — Natural-scale Xi residue coherence and the cumulative defect frontier

Claim ID: `T-105200`  
Status: **MAJOR PROPOSED UNCONDITIONAL ADVANCE; FINAL LOW-ORDER BUDGET OPEN**  
Created: 2026-08-23  
Updated: 2026-08-23  
Base: PR #723 live checkpoint `fd3ef43a6964e502f00ad906482eae5b3c544fba`  
Depends on: `L-105200--L-105205`; PRs #716, #720, #723  
RH status: **unproved**

## 1. Unconditional high-derivative theorem

For every fixed `C,H>0`, put

\[
T_M=C\sqrt{M\over\log M}.
\]

The positive Xi Fourier saddle has a uniform complex Gaussian limit on the
complete natural box. Consequently, for all sufficiently large `M`:

1. every zero of every `Xi^(m)`, `m>=M`, in
   `|Re z|<=T_M`, `|Im z|<=H` is real and simple;
2. the zero count is
   \[
   N_m(T_M)={2w_mT_M\over\pi}+O_C(1);
   \]
3. every derivative-ratio residue at a real zero of `Xi^(m+1)` in a buffered
   inner box satisfies
   \[
   {\Xi^{(m)}(c)\over\Xi^{(m+2)}(c)}
   =-w_m^{-2}(1+o(1));
   \]
4. the associated residue coherence is `1-o(1)`, uniformly over `m>=M`.

Thus the open mean-value condition `RCMV104530` is not merely compatible with
the Xi Fourier source: it holds with asymptotically optimal margin throughout
the full high derivative tail.

Equivalently, a rectangle of original height `T` is unconditionally cleared by
all derivative orders

\[
\boxed{m\ge K T^2\log(2+T)}
\]

for every fixed `K>0`, once `T` is sufficiently large (with the threshold
depending on `K,H`).

## 2. Exact first and second contour fluxes

PR #723 supplies the exact second-moment window flux

\[
B_{2,F}
={1\over2\pi i}
\int_{\partial\Omega}{F(z)^2\over F'(z)F''(z)}\,dz.
\]

`L-105204` supplies its first-moment companion

\[
B_{1,F}
={1\over2\pi i}
\int_{\partial\Omega}{F(z)\over F'(z)}\,dz.
\]

Together they give the exact finite-window coherence formula

\[
\mathfrak C_F
=
{(-B_{1,F}+C_{1,F})_+^2
\over
R_F(B_{2,F}-C_{2,F}-D_F)},
\tag{T-105200.1}
\]

where the two `C` terms are the nonreal critical corrections and `D_F` is the
adjacent-derivative residue debt.

For `F=Xi^(m)` in the natural high derivative tail, choose a regular vertical
edge in one model cell. Then `L-105205` proves

\[
C_{1,F}=C_{2,F}=0,
\qquad
D_F=o(R_F/w_m^4),
\]

and

\[
\boxed{
B_{1,F}=-{R_F\over w_m^2}(1+o(1)),
\qquad
B_{2,F}={R_F\over w_m^4}(1+o(1)).
}
\tag{T-105200.2}

Thus

\[
{B_{1,F}^2\over R_FB_{2,F}}=1-o(1).
\]

The high-tail residue theorem is therefore also an unconditional evaluation of
the exact oriented window fluxes, not only a local-zero computation.

## 3. Exact low-order descent ledger

Let `Omega_T` be a regular critical-strip rectangle in the Xi `t`-plane and
choose

\[
r(T)=\left\lceil K T^2\log(2+T)\right\rceil
\]

large enough that `Xi^(r(T))` has no off-real zero in `Omega_T`. For
`0<=j<r(T)`, let

```text
R_j(T)          real zeros of Xi^(j+1) on the real slice;
C_j(T)          residue coherence of Xi^j at those zeros;
B_j(T)          the two endpoint defects;
W_j(T)          the exact boundary winding difference.
```

`L-105203` gives

\[
O_{\Omega_T}(\Xi)
\le
2\sum_{j<r(T)}R_j(T)(1-\mathfrak C_j(T))
+
\sum_{j<r(T)}(B_j(T)+W_j(T)-1).
\tag{T-105200.3}
\]

The high derivative off-real term is absent. The right side contains no
unspecified `O(1)` and no global percentage hypothesis.

Define the **coherence-residue defect budget** `CRDB105200` by

\[
\boxed{
2\sum_{j<r(T)}R_j(T)(1-\mathfrak C_j(T))
+
\sum_{j<r(T)}(B_j(T)+W_j(T)-1)
<2
}
\tag{CRDB105200}
\]

for every sufficiently large regular `T`, with finite low-height verification
handled separately.

Since the off-real zero count is an even nonnegative integer,

\[
\boxed{
\mathrm{CRDB105200}\Longrightarrow\mathrm{RH}.
}
\tag{T-105200.4}
\]

The implication is exact. `CRDB105200` remains open.

## 4. What remains after the new unconditional tail theorem

The new work proves that both moment fluxes, the adjacent debt and residue
coherence have the desired asymptotic throughout the complete derivative tail.
Accordingly, the next analytic task is not another high-derivative percentage
or a second global polynomial identity. It is one of the following equivalent
low-order advances:

1. localize and bound (T-105200.1) uniformly for the finite ladder
   `j<r(T)`;
2. prove directly that the weighted coherence loss
   \[
   \sum_{j<r(T)}R_j(T)(1-\mathfrak C_j(T))
   \]
   is subunit;
3. combine the first/second contour fluxes with the explicit
   Hermite--Biehler/Levinson boundary transport so that their total budget is
   below two.

## 5. Exact boundary

```text
natural-scale complex Gaussian saddle       PROPOSED COMPLETE
half-infinite derivative-tail real-rooting  PROPOSED COMPLETE
natural order T^2 log T high entry           PROPOSED COMPLETE
critical residues = -w_m^-2(1+o(1))         PROPOSED COMPLETE
high-tail residue coherence -> 1             PROPOSED COMPLETE
exact first window flux                      PROVED EXACT
high-tail second-residue debt lower order    PROPOSED COMPLETE
high-tail two-flux coherence                  PROPOSED COMPLETE
finite coherence-defect budget               PROVED EXACT
Xi rectangle budget                          PROVED CONDITIONAL ON EXISTING FLUX IDENTITY
CRDB105200                                    OPEN / RH-BEARING
Riemann Hypothesis                            UNPROVED
```

This draft PR is intended to remain the dedicated continuation workspace for
subsequent attacks on `CRDB105200`; later passes should update this branch
rather than open a new proposal for each refinement.
