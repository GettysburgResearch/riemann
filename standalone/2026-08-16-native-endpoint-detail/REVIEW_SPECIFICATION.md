# Hostile review specification for T-94100

## Freeze

- Verify PR #511 remains at `6ece82279cb03474ebc79914db572f6ff095d238`.
- Verify the successor commit has that SHA as its sole parent.
- Verify every path and checksum in the packet ledgers.

## Exact separator

- Reconstruct `c_X`, `w_X`, `Omega_X` and `J_Lambda(X)`.
- Confirm that exact equality in every component row forces `d_X=c_X`.
- Confirm a negative coordinate is a valid dual-cone Farkas separator.

## Endpoint-detail theorem

- Reconstruct `a_T=d_T-d_(T-1)` and its coefficientwise positivity.
- Verify the carry coefficient `beta_(nq)` by direct block counting.
- Verify the sharp harmonic inequality, including all four residue classes.
- Verify the signed scale-four increment inequality without replacing it by an
  absolute majorant.
- Audit all three endpoint-activation cases in the derivative proof.
- Verify `Delta_T(q)>0` for every `2<=q<T` and triangular vanishing for `q>=T`.

## Greedy compiler

- Check each minimum-ratio coefficient and residual update.
- Confirm one `lambda_T` is used in row, ordinary `q`, ordinary `4q`, detail,
  score, `Y_4` and ownership.
- Form detail only after the common ordinary sums.
- Reconstruct positive radix-four inversion and ordinary feasibility.
- Verify the exact diagonal blocker and final slack identities.

## Endpoint frontier

- Verify the scale-four expansion of `Y_4` and the Chebyshev support price.
- Do not accept finite values of `B_X` as proof of `NEDB`.
- Independently reconstruct the frozen one-sided endpoint consumer before any
  RH promotion.

## Verdict

The finite compiler passes only if all exact items above reconstruct. RH remains
unproved unless the asymptotic blocker theorem and endpoint consumer both pass.
