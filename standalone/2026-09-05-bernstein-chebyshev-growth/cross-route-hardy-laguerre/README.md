# Cross-route continuation: an arithmetic operator and linear-size trace recovery

Status: **PROPOSED complete analytic proofs; independent review required. RH and the unrestricted positivity/cancellation inequality remain UNPROVED.**
Scope: actual xi, fixed a=3/4 and b=3/2, all degrees; one separately certified four-dimensional section; exact synthetic controls.
Parent: PR #792 at `875e8dd47186e924445533513a1ad405af09d7a7`.
External repository source: PR #793 at `f22b67db113d1aa4f986fe35a2fc0321fdff7d47`.
What ran: 2,188 exact finite controls per mode, including a rational outward actual-source certificate. See VALIDATION.md.
Smallest remaining gap: positivity of the literal gamma-plus-prime operator, or a genuinely new signed estimate implying the original bound.

Read **REVIEW.md** for the comparison of other agents' work, **BRIDGE.md** for the proofs, then **VALIDATION.md** and the two JSON records. Labels HL-1 through HL-6 are local to this folder.

## Main results

The #793 Hardy operator and the original #792 coefficients have an exact common realization. The new arithmetic kernel is an absolutely trace-norm-convergent gamma-plus-prime series with `||T||_1<30`, and explicit tails. Every finite matrix in one fixed Laguerre basis is constructed from derivatives of `xi'/xi` at the safe point `s=2`; no zero data is input.

For the fixed unilateral shift `S`, let `A=I-2S`. Then

```text
A* T A = T,
d_n = (9/8) Tr(T A^n).
```

These identities do not assert `T>=0`. That missing positivity would make all `|d_n|<=d_0`, hence prove the original subexponential inequality and RH.

The additional all-degree transfer is not a generic trace-norm estimate. Put

```text
J_(M,n)=Tr(P_M T A^n P_M), M>=n.
```

It uses only the leading `(M+n)`-dimensional source matrix, and

```text
|d_n-(9/8)J_(M,n)| <= 1080 log(e sqrt M)/sqrt M.
```

Thus `M=n` uses **2n source coordinates**, with error tending to zero. The actual paired spectral geometry avoids the generic `||A^n||=3^n` truncation loss. Independent-entry rounding still suffers binomial amplification; no stable high-degree numerical algorithm or boundedness of `J_(M,n)` is claimed.

Predetermined matrix sections also converge in trace norm with a stated rate and eventually capture every negative direction. Their required dimension depends on the negative gap. A negative exact section already witnesses full negativity; the tail guarantee is not needed for that implication.

## Actual source and necessary distinctions

The leading 4-by-4 actual matrix is positive definite, certified through rational Euler--Maclaurin and gamma source enclosures at `s=2`. Its smallest LDL pivot is about `8.04115e-12`; only the exact interval endpoints are used for acceptance.

A strip-confined six-zero polynomial control has positive heat, satisfies the conserved-form and trace identities, and has a positive leading 4-by-4 section, but its fifth pivot is negative. This is not actual xi.

The arithmetic prime atom has summable trace norm `O(Lambda(n)n^(-5/4))`, while its sharp relative quadratic-form cost is `Lambda(n)/(b sqrt n)`, whose sum diverges. Trace-class construction is therefore not a proof of arithmetic positivity.

## Replay

```sh
python verify_bridge.py --check result.json
python -O verify_bridge.py --check result.json
sha256sum -c SHA256SUMS
```

The checker is standard-library-only and self-contained in this directory. Earlier files and suites are unchanged, not implicitly rerun. Analytic arguments, global signs, and RH are not machine-certified. No external priority or canonical integration is claimed.
