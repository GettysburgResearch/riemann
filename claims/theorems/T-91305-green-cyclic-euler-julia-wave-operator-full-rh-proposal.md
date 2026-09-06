# T-91305 — Green-Cyclic Euler–Julia Wave Operator: the preferred constructive completion after local source closure

Claim ID: `T-91305`  
Status: **FULL UNCONDITIONAL RH PROPOSAL — NOT A PROOF; ONE RENORMALIZED CYCLIC WAVE OPERATOR OPEN**  
Created: 2026-08-12  
Depends on: `L-91323/L-91324`; corrected `T-91303/T-91304`; PRs #400–#402  
RH status: **unproved**

## 1. What the new local theorem closes

For every safe line \(\sigma>1\), every prime Euler factor of the positive
Jordan source now has an explicit lossless two-output Julia node. Cascading
over all primes gives an explicit isometric source multiplier

\[
\mathcal J_{a,\sigma}
:
H^2
\longrightarrow
H^2\oplus\bigoplus_pH^2
\tag{T-91305.1}
\]

with scalar transfer

\[
\frac{Q_a(\sigma+it)}{Q_a(\sigma)}
\]

and fully polarized prime-power details.

The coefficient-one dyadic scale cocycle is likewise an explicit two-section
Julia cascade at every prime.

No existential Fock square, local Euler-factor positivity, or finite-prime
state remains open on the safe side.

## 2. Why the direct boundary limit is impossible

`L-91324` proves that the prime detail number diverges at

\[
\sigma=\frac12-a.
\]

Hence the completed critical representation cannot be obtained as a strong
limit of the unrenormalized safe Euler–Julia cascades in the same Fock vacuum.

The conclusion-producing construction must act only after either Green
regularization or an equivalent global theta/canonical renormalization.

## 3. The cyclic source vector

Let \(e_a^{\rm Green}\) be the explicit finite-norm completed safe vector from
the one-Green/Jordan construction, including

```text
rational pole channel;
beta/Gamma channel;
all-generation prime innovation vector;
theta ground-state channel;
local p=2 boundary port.
```

Its norm is computed entirely from absolutely convergent safe Euler and gamma
data. Let

\[
f_a(t)
=
e^{-t/2}
\left(\int_1^{e^t}h_a(y)\,dy\right)
\mathbf1_{t\ge0}.
\tag{T-91305.2}
\]

Then

\[
\widehat f_a(z)
=
\frac{\Theta_a(z)}{\frac12-iz}.
\tag{T-91305.3}
\]

## 4. Green-Cyclic Euler–Julia Wave Operator

> **`GEJWO_a`.**  
> Construct a source-ordered partial isometry
> \[
> \boxed{
> W_a:
> \overline{\operatorname{span}}
> \{\text{dyadic descendants and logarithmic jets of }e_a^{\rm Green}\}
> \longrightarrow
> L^2(0,\infty)\oplus\mathcal E_a
> }
> \tag{T-91305.4}
> \]
> satisfying:
>
> 1. **Visible vector**
>    \[
>    W_ae_a^{\rm Green}=f_a\oplus q_a.
>    \]
> 2. **Explicit auxiliary coordinates**
>    \[
>    q_a=q_{\theta,a}\oplus q_{\beta,S\Delta,a}
>        \oplus q_{{\rm Pois},a}\oplus q_{2,a}.
>    \]
> 3. **Safe-source compatibility.** On every finite prime cutoff and safe
>    vertical line, \(W_a\) intertwines the explicit Euler–Julia columns of
>    `L-91323/L-91324`.
> 4. **Dyadic compatibility.** It intertwines the local two-section Julia
>    rectangle with the completed horizontal Xi cocycle.
> 5. **Renormalized limit.** The prime cutoff and critical-boundary limits are
>    taken only after the Green/theta transform, and converge in the output
>    Hilbert norm.
> 6. **Positive metric.** No Pontryagin metric, omitted detail, or same-scale
>    signed remainder is permitted.
> 7. **Minimality.** The finite value/jet couplings agree with `L-91322`, and
>    the infinite tail is controlled in the graph norm of \(W_a\).

The norm identity is

\[
\boxed{
\|e_a^{\rm Green}\|^2
=
\|f_a\|_2^2+\|q_a\|^2.
}
\tag{T-91305.5}
\]

## 5. Why `GEJWO_a` proves the hard renewal estimate

The source norm in (T-91305.5) is finite unconditionally. Therefore

\[
f_a\in L^2(0,\infty).
\]

Since \(1/(\frac12-iz)\) is outer and the boundary modulus of \(\Theta_a\) is
one, PR #402 gives

\[
\Theta_a\ \text{meromorphic inner}.
\tag{T-91305.6}
\]

Equivalently, the factor-four renewal energy is finite.

For a predetermined sequence \(a_j\downarrow0\), `GEJWO_(a_j)` excludes every
off-line zero and proves RH.

## 6. Relation to the three requested routes

### Suzuki–de Branges

The graph closure of \(W_a\) supplies the compatible integrated Marchenko
systems. The canonical Hamiltonian is recovered after the global
renormalization, not from the divergent unintegrated kernel.

### Lévy–Fock–Hardy

The safe source side is now an explicit Euler–Julia/Fock cascade. \(W_a\) is
the renormalized scattering wave operator into the causal/anti-causal Hardy
and auxiliary outputs.

### Theta/Brownian DtN

The graph norm of \(W_a\) is the form norm of the coupled theta,
sum–difference Beta, Poisson, and local \(p=2\) bulk. Its boundary trace is the
Xi impedance.

Thus the three routes remain three realizations of the same one-vector wave
operator.

## 7. Exact boundary

```text
local prime Julia nodes                         EXACT
infinite safe Euler–Julia cascade               EXACT
safe dyadic two-section detail lattice          EXACT
naive critical Fock limit                       REFUTED
Green-cyclic source vector                      EXPLICIT / REVIEW
GEJWO_a renormalized wave operator               OPEN / RH-BEARING
GEJWO on a_j -> renewal L2 -> innerness -> RH    PROPOSED COMPLETE
Riemann Hypothesis                              UNPROVED
```
