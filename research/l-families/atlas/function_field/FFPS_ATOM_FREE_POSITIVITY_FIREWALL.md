# Atom-free positivity is impossible for a nonzero quadratic amplifier

Status: **exact finite-dimensional no-go theorem; no global FFPS estimate,
RH, or GRH claim**

Exact replay:
[`ffps_atom_free_positivity_firewall.py`](ffps_atom_free_positivity_firewall.py).

## 0. Outcome

The two most attractive features of a family amplifier cannot coexist in one
ordinary quadratic kernel:

\[
 \boxed{
 \text{nonzero positive-semidefinite principal domination}
 \quad+\quad
 \text{exact literal-atom deletion}
 \quad\text{is impossible}.}
\tag{0.1}
\]

This is not an asymptotic limitation.  It is a two-line matrix theorem.

If a Hermitian matrix `K` is positive semidefinite, then every `2 x 2`
principal minor gives

\[
 |K_{ij}|^2\le K_{ii}K_{jj}.
\tag{0.2}
\]

Therefore `K_ii=0` for every atom forces every matrix entry to vanish:

\[
 \boxed{K\succeq0\text{ and }\operatorname{diag}K=0
 \quad\Longrightarrow\quad K=0.}
\tag{0.3}
\]

There is a sharper domination version.  If `v` is a principal observation
and

\[
 K\succeq c,vv^*,
\]

then testing a coordinate vector gives

\[
 \boxed{K_{ii}\ge c|v_i|^2.}
\tag{0.4}
\]

For the native principal sum, `v_i=1`.  Any positive quadratic form that
dominates `c|P|^2` must therefore retain at least `c` units of Wick diagonal
at **every** source atom.  Hard masking changes which atoms exist and can
improve the inverse Gram, but it does not evade (0.4) on the retained source.

The block-coset interferometer escapes (0.3) in exactly one way: it is
indefinite.  Its negative quotient spectrum is not a defect that can be
dropped; it is the algebraic price of exact atom deletion.

## 1. Complete signature of the balanced quotient kernel

Let `h` quotient cosets each contain `n` source atoms, so `N=hn`.  The
off-coset interferometer has atom kernel

\[
 A_{xy}=
 \begin{cases}
 0,&\Phi(x)=\Phi(y),\\
 h/(h-1),&\Phi(x)\ne\Phi(y).
 \end{cases}
\tag{1.1}
\]

It has the exact spectrum

\[
 \boxed{
 \operatorname{Spec}(A)=
 \left\{
 N^{(1)},
 \left(-{N\over h-1}\right)^{(h-1)},
 0^{(N-h)}
 \right\}.}
\tag{1.2}
\]

Indeed:

- the global constant vector has eigenvalue
  `(h/(h-1))*n*(h-1)=N`;
- a vector constant on each coset with quotient sum zero has eigenvalue
  `-hn/(h-1)=-N/(h-1)`;
- a vector summing to zero inside every coset lies in the kernel.

The replay writes an explicit basis of these three spaces over the rationals
and checks (1.2) entry by entry.  Hence the sharp scalar diagonal repair is

\[
 \boxed{\delta_{\rm PSD}={N\over h-1}.}
\tag{1.3}
\]

Adding less than this multiple of the literal atomic norm leaves a negative
quotient direction.  Adding it restores positivity but spends a diagonal
budget that grows with coset size.

This repair is **not** the same object as either the phase-Gram repair or the
unit Wick coefficient of the selected average.  Those live in different
quadratic spaces and normalizations.

## 2. Why the exact principal identity remains signed

The quotient Fourier decomposition says

\[
 |P|^2
 =\mathcal I+{1\over h-1}
  \sum_{\chi\ne1}|H_\chi|^2.
\tag{2.1}
\]

The second term supplies exactly the negative quotient channels missing from
`I` and restores the rank-one positive principal kernel.  Its atomic diagonal
also restores the unit principal diagonal.  This is a structured spectral
repair, not a triangle-inequality estimate.

Taking absolute values term by term destroys both cancellations.  The exact
Artin--Schreier/Kummer countermodel in the companion weight-barrier packet has
`|P|^2=1` while the two terms on the right of (2.1) are separately of full
quadratic size.

Thus a conventional route of the form

\[
 |P|^2\le \text{positive atom-free family energy}
\tag{2.2}
\]

cannot exist at this kernel level.  A viable route must use at least one of:

1. a signed estimate preserving the cancellation in (2.1);
2. an allowed positive diagonal budget controlled by a separate theorem;
3. an auxiliary-variable or nonlinear amplifier outside a single quadratic
   atom kernel;
4. rigidity converting one principal anomaly into many family anomalies
   without a PSD majorant.

This narrows the average-to-principal problem.  It does not solve it.

## 3. Relation to hard-mask leverage

The restricted inverse-Gram theorem is still useful.  It minimizes the phase
energy needed to represent the principal functional on a **changed support**.
The present theorem concerns a different question: whether one can then turn
the resulting source square into a positive, atom-free principal majorant.

The two conclusions coexist:

\[
 \begin{array}{c|c}
 \text{hard correlated support} &
 \text{can improve sharp principal leverage}\\
 \hline
 \text{exact Wick deletion} &
 \text{forces the surviving nonzero quadratic form to be signed}
 \end{array}
\tag{3.1}
\]

The true RH-facing target is therefore not “find a better positive mask.”
It is “find a source-faithful signed theorem whose negative quotient channels
are controlled jointly with the principal channel.”

## 4. Proof ledger and scope

Proved exactly:

- the zero-diagonal PSD theorem (0.3);
- the coordinatewise domination cost (0.4);
- the complete balanced-coset signature (1.2);
- the sharp scalar diagonal repair (1.3).

Imported exactly from the block-coset packet:

- the quotient kernel (1.1);
- the signed identity (2.1).

Not proved:

- a native FFPS realization of multiple block masks;
- any signed varying-conductor estimate;
- that every possible nonlinear or auxiliary amplifier obeys this no-go;
- principal-member individualization, RH, or GRH.

The theorem applies to one Hermitian quadratic kernel on a fixed finite atom
space.  That boundary is essential: higher moments, randomized identities,
and geometric rigidity are not silently ruled out.

## 5. Bounded replay

Run:

```text
python -B research/l-families/atlas/function_field/ffps_atom_free_positivity_firewall.py --check
python -B -O research/l-families/atlas/function_field/ffps_atom_free_positivity_firewall.py --check
python -B -m unittest tests.test_ffps_atom_free_positivity_firewall
python -B -O -m unittest tests.test_ffps_atom_free_positivity_firewall
```

The largest rational matrix is `40 x 40`.  No point count or floating-point
operation is performed.  The general proof is symbolic; the matrices are
only refusal tests for normalization and multiplicity errors.
