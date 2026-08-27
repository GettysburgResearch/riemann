# L-105360 — Nested symmetric windows transport the boundary Stieltjes measure by explicit critical-residue atoms

Claim ID: `L-105360`  
Status: **PROVED EXACT FINITE-WINDOW TRANSPORT IDENTITY — XI SIGN OPEN**  
Created: 2026-08-23  
Depends on: `L-105217`, `L-105351`; the simple noncommon stratum of `L-105328`  
RH status: **not assumed**

## 1. Symmetric nested windows

Let `F` be entire, real on the real axis, and of definite parity. Let

\[
\Omega_1\Subset\Omega_2
\]

be bounded regular domains invariant under conjugation and under `z -> -z`,
with zero in their common real interior. Define

\[
H_j(z)
={1\over2\pi i}\int_{\partial\Omega_j}
 {F(\zeta)/F'(\zeta)\over\zeta-z}\,d\zeta,
\qquad j=1,2.
\tag{L-105360.1}
\]

Assume that every critical point of `F` in the closed annulus
`Omega_2 \ Omega_1` is simple, noncommon with `F`, and real. By parity the
annular critical points occur in pairs `+-c`, `c>0`, and

\[
\rho_c={F(c)\over F''(c)}={F(-c)\over F''(-c)}.
\tag{L-105360.2}
\]

Put

\[
s_c={1\over c^2},
\qquad
w_c={-2\rho_c\over c^2}.
\tag{L-105360.3}
\]

## 2. Exact boundary-function transport

The nested-window identity `L-105217` gives

\[
H_1(z)
=H_2(z)
+\sum_{c>0\ {m in\ the\ annulus}}
\rho_c\left({1\over z-c}+{1\over z+c}\right).
\]

Pairing `+-c` yields the exact Stieltjes-coordinate update

\[
\boxed{
H_1(z)
=H_2(z)
+z\sum_{c>0\ {m in\ the\ annulus}}
 {w_c\over1-s_cz^2}.
}
\tag{L-105360.4}
\]

No limiting argument, asymptotic estimate, or root matching is used.

## 3. Exact origin-moment update

Let

\[
\beta_n(\Omega_j)
={H_j^{(2n+1)}(0)\over(2n+1)!}
={1\over2\pi i}\int_{\partial\Omega_j}
 {F(\zeta)/F'(\zeta)\over\zeta^{2n+2}}\,d\zeta.
\]

Expanding (L-105360.4) at zero gives, for every `n>=0`,

\[
\boxed{
\beta_n(\Omega_1)
=
\beta_n(\Omega_2)
+
\sum_{c>0\ {m in\ the\ annulus}}w_cs_c^n.
}
\tag{L-105360.5}
\]

Thus the complete origin Hankel hierarchy is transported by a finite atomic
moment sequence.

## 4. Positivity under the sharp residue sign

If every annular critical residue is nonpositive,

\[
\rho_c\le0,
\]

then `w_c>=0`. Suppose the outer boundary function has a positive Stieltjes
representation

\[
H_2(z)=z\int_0^\infty{d\nu_2(s)\over1-sz^2}
\]

with finite compactly supported `nu_2>=0`. Then (L-105360.4) gives

\[
\boxed{
H_1(z)=z\int_0^\infty{d\nu_1(s)\over1-sz^2},
\qquad
\nu_1
=
u_2+
\sum_{c>0\ {m in\ the\ annulus}}w_c\delta_{s_c}.
}
\tag{L-105360.6}
\]

Consequently

\[
\boxed{
\mathrm{OASH}(F;\Omega_2)
\ \wedge\
\bigl(\rho_c\le0\text{ for every crossed pair}\bigr)
\Longrightarrow
\mathrm{OASH}(F;\Omega_1).
}
\tag{L-105360.7}
\]

The conclusion is exact at every finite stage.

## 5. Finite exhaustion

For a nested symmetric exhaustion

\[
\Omega_1\Subset\Omega_2\Subset\cdots\Subset\Omega_N,
\]

iteration gives

\[
\boxed{
H_1(z)
=H_N(z)
+z\sum_{c>0\ {m in}\ \Omega_N\setminus\Omega_1}
 {-2\rho_c/c^2\over1-z^2/c^2}.
}
\tag{L-105360.8}
\]

If `H_N` is Stieltjes and every crossed residue is nonpositive, then every
inner boundary function is Stieltjes. Hence one need not prove the boundary
Loewner gate separately at every intermediate window: one terminal positive
measure plus the sharp critical-residue sign transports the complete
all-order hierarchy inward.

## 6. Exact relation to the two sharp gates

On the simple noncommon real-critical stratum,

```text
CRVH105330   supplies rho_c <= 0 for every crossed critical pair;
OASH105350   is the complete boundary Stieltjes/Hankel hierarchy.
```

Therefore (L-105360.7) is the exact compatibility law between the two sharp
last-defect coordinates. The critical hierarchy does not merely coexist with
the boundary hierarchy: it moves positive atomic mass from the outer boundary
measure into the explicit interior residue ledger.

## 7. Firewalls and scope

- A nonreal conjugate critical pair does not produce one positive atom on
  `[0,infinity)`; it requires the full real rank-two correction.
- A positive real residue produces a **negative** atomic weight and can destroy
  the Stieltjes property.
- Common zeros and multiple critical points require the confluent jet ledger;
  they are not included silently.
- This theorem supplies no terminal positive boundary measure for fixed
  low-order Xi and proves neither `CRVH105330`, `OASH105350`, nor RH.
