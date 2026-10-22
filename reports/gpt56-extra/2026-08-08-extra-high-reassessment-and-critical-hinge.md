# Extra-high reassessment: five-adic scope correction and critical square-root hinge attack

Date: 2026-08-08
Status: research report; RH unproved

## 1. Correction of the two preceding passes

The preceding five-adic continuation moved too quickly from the valid scaling

```text
w_X(5q)=5^(-1/2) w_(X/5)(q)
```

to an unsupported claim that the remaining carry state was a five-dimensional
residue automaton.  The actual nonmultiple carry columns depend on complete
floor/quotient data and the legal adjacent-tree repair has binary/Mersenne
ancestry.  PR #322 now contains `R-30107` and its front door has been corrected.

The earlier response also referred to supporting five-adic lemmas which had not
actually been committed.  That provenance claim is withdrawn.

## 2. New cross-route observation

PR #295 decomposes the complete critical target into positive square-root
hinges

```text
h_T(q)=(q^(-1/2)-T^(-1/2))_+.
```

The carry inverse of each hinge is substantially simpler than the complete
logarithmic target.  This motivates a new elementary front:

```text
Critical Hinge Saturation (CHS)
    -> exact Carry Saturation
    -> sharp entropy prime-ramp lower bound
    -> square-screw/Landau
    -> RH.
```

The proposal is `T-32201`.

## 3. New exact theorem: the complete top half is positive

`L-32201` proves for every nonnegative decreasing target, not just a hinge,
that every inverse coefficient with `2n>T` is nonnegative.  In the top half the
carry matrix is the affine kernel

```text
beta_(nq)=(2q-n-1)/(n+1).
```

After setting `d_n=c_n/(n+1)` and `S_q=sum_(n>=q)d_n`, the inversion is

```text
q(q-1)S_q=sum_(m=q)^T m[h(m)-h(m+1)],
```

and

```text
d_q=[h(q)-h(q+1)]/(q-1)
    +2V_(q+1)/(q(q^2-1)) >=0.
```

This is unconditional finite progress on CHS.

## 4. Exact firewall: the inner half is Mertens-sensitive

`L-32202` proves

```text
h_T=sum_(N<T) delta_N e_N,
delta_N=N^(-1/2)-(N+1)^(-1/2),
```

and hence

```text
c_T(j)=sum_(N=j)^(T-1) delta_N s_N(j),
```

where the inverse of the constant step has the exact Mertens formula displayed
there.  The continuum hinge inverse has Mellin multiplier

```text
p/[2(p-2)(p-3/2) zeta(p-1)].
```

Thus the extraordinary finite positivity of square-root hinges is a legitimate
RH-sensitive phenomenon.  A large finite scan is discovery only.

## 5. Exact continuum equality firewall

`L-32203` proves that every nonnegative continuum carry packing has first mass
at most eight, and attaining eight forces exact saturation almost everywhere.
So a smooth positive minorant cannot recover the sharp constant while leaving a
hidden residual.  Near-sharp mass and small source residual are quantitatively
the same issue.

## 6. Reconnaissance, explicitly not proof

Independent local experiments during this pass found no negative hinge
coefficient through endpoints in the millions.  They also show that simple
endpoint-to-endpoint monotonicity is false: the step-inverse update has signed
Mertens contributions.  No finite endpoint horizon is promoted to CHS.

The committed exact checker `X-32201` verifies only:

```text
6392 top-half rational inversion rows;
3916 exact step/Mertens inverse rows;
```

with digest

```text
af9d38edad3476f824f0884e9b413771c221b2ffa31ca10bc584ff4183969048
```

## 7. Current research judgment

The extra-high re-run does **not** produce an unconditional proof of RH.
It does, however, replace the unsupported five-state narrative by a much cleaner
finite theorem:

```text
CHS is sufficient;
CHS is proved on the entire top half;
the unresolved inner half is exactly a critical Mertens-smoothed step inverse;
there is no continuum minorant shortcut around it.
```

A future claimed completion must prove the complete signed sum in `L-32202.7`
or construct a genuinely weaker near-sharp packing.  Reviewers are not being
asked to invent that proof.
