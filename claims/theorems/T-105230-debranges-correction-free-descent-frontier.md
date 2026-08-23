# T-105230 — De Branges correction-free descent frontier

Claim ID: `T-105230`  
Status: **PROPOSED EXACT FINITE FACTORIZATION; entire Xi angle estimate open**  
Created: 2026-08-23  
Depends on: `L-105224`; `L-105222`; PRs #724 and #726  
RH status: **unproved**

## 1. The correction ledger can be bypassed during downward induction

At a reverse–Rolle descent step, suppose the derivative

\[
G=\Xi^{(k)}
\]

has already been shown real-rooted. For finite canonical-product truncations,
`L-105224` constructs two source-owned de Branges vectors `u_a,v_a` with

\[
\pi N_a=\|u_a\|^2,
\qquad
-\pi A_a=\langle v_a,u_a\rangle,
\qquad
\pi B_a=\|v_a\|^2.
\]

Hence the **actual** real residue defect is

\[
\boxed{
\pi^2(N_aB_a-A_a^2)=\|u_a\wedge v_a\|^2.
}
\tag{T-105230.1}
\]

This is not the raw safe-line defect of `L-105221`. It already contains the
complete correction needed to pass from boundary carriers to real critical
moments, but encodes it positively as one wedge norm.

## 2. Exact local extinction port

Combining `L-105222` with (T-105230.1), no wrong extremum occurs in
`[a-1,a+1]` whenever

\[
\boxed{
\frac{\|u_a\|^2}{\pi}
\frac{
\operatorname{dist}(v_a,\mathbb R u_a)^2
}{
\|v_a\|^2
}
<
\frac9{25}.
}
\tag{T-105230.2}
\]

Call the uniform large-centre version

\[
\boxed{\mathrm{DBAE105230}}
\]

for **de Branges angle extinction**.

This is exactly the integrality scale needed to remove the last wrong
extremum; a statement merely saying that the angle tends to zero without its
rate is insufficient.

## 3. Interface with the exterior-square programme

Equation (T-105230.1) is itself an exterior-square norm. PR #724 constructs an
independent unconditional exterior-square Fourier Gram for the Xi Laguerre
defects and a positive near-collision energy for residue dispersion.

The two objects now have matching type:

```text
PR #724:
  exterior-square Fourier/translation Gram;

T-105230:
  exterior-square de Branges/spectral Gram.
```

A source-faithful intertwiner between these two exterior powers, with loss
`o(1/N_a)`, would prove `DBAE105230`. This is more specific than separately
bounding the four correction terms in `MCRC105220`.

## 4. Entire-function gate

For the actual Xi derivative, define `DBEX105230` to mean:

1. symmetric real-zero canonical-product truncations of `G` produce
   `u_(a,N),v_(a,N)` as in `L-105224`;
2. these vectors converge in the de Branges space of `G+iG'`;
3. their three Gram entries converge to the actual weighted real moments;
4. the convergence is uniform on the large-centre schedule used in the
   reverse–Rolle cascade.

Then

\[
\boxed{
\mathrm{DBEX105230}
\wedge
\mathrm{DBAE105230}
\Longrightarrow
\text{no high-ordinate wrong extremum at that descent step}.
}
\tag{T-105230.3}
\]

PR #726 already supplies a summable high-derivative coherence tail. Therefore
only a finite low-order prefix requires this entire-space angle control.

## 5. Exact boundary

```text
finite derivative-real-rooted Gram          PROPOSED EXACT
safe-point count vector                     PROPOSED EXACT
debt/nonreal-free actual moment factor       PROPOSED EXACT
weighted wedge extinction port               PROPOSED EXACT
DBEX105230 entire de Branges exhaustion       OPEN
DBAE105230 angle estimate                     OPEN / RH-BEARING
finite-height endpoint/winding ledger         OPEN / RH-BEARING
Riemann Hypothesis                            UNPROVED
```
