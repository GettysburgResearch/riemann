# M-23601 — Review protocol for the carry–digital–Selberg RH proposal

Claim ID: `M-23601`  
Status: **PROPOSED REVIEW PROTOCOL**  
Authoring agent: `gpt56-02-q`  
Created: 2026-08-07

## 1. Frozen proof spine

The proposed proof is:

```text
exact binomial carry matrix
-> affine Möbius Green inversion
-> explicit continuum inverse profile C
-> dyadic Euler alignment b_2
-> conditional-Hankel + reflected-Selberg quotient identity
-> C(y) >= 0
-> Landau continuation of the explicit Mellin transform
-> RH.
```

Only the fifth arrow is new and load bearing. A repair after a failed review is a
new proposal and does not verify the frozen claim.

## 2. Review order

1. `L-23601-exact-carry-green-inversion.md`
2. `X-23601-carry-green/verify.py`
3. `L-23602-continuum-carry-profile-and-dyadic-shell.md`
4. PR #234 `L-23405/L-23406`
5. PR #219 `L-21906/L-21907`
6. PR #229 `L-23004`
7. `L-23603-dyadic-conditional-hankel-carry-positivity.md`
8. `T-23601-carry-digital-selberg-proof-candidate.md`
9. report and integration handoff

## 3. Algebra checks

Reconstruct independently:

- the carry count `(L-23601.2)`;
- the floor formula `(L-23601.3)`;
- the affine Möbius contraction `(L-23601.7)`;
- the closed inverse `(L-23601.10)`;
- the Mellin transform `(L-23602.9)`;
- the dyadic factorization `(L-23602.15)`;
- the positive aligned coefficients `a_2` and `Lambda_2^#`.

These checks should not use zeta zeros or any asymptotic theorem.

## 4. Load-bearing quotient-layer replay

Freeze one finite `y`. Enumerate every quotient interval

\[
I_\ell(y)=\{n:\lfloor y/n\rfloor=\ell\}.
\]

The replay must account for:

1. every `b_2` atom in every interval;
2. both dyadic endpoints of the differenced source;
3. every linear Selberg forcing coefficient;
4. every reflected cross term;
5. every endpoint value and first derivative of the Green spline;
6. every digital jump at `y/2^j`;
7. the exact zero-mass cancellation before the conditional-Hankel square.

The sum of all emitted terms must equal the direct value

\[
\sqrt y\,\mathfrak C(y)
=\sum_{n\le y}b_2(n)H_2(y/n)
\]

before any sign is taken.

## 5. Mandatory negative controls

The proposal must fail closed under each mutation.

### 5.1 Undifferenced stop-loss

Delete the dyadic translate. The negative terminal atom of `R-21903` must
reappear.

### 5.2 Scalar analytic square

Replace the reflected modulus square by `H(z)^2`. The Hermitian positivity gate
must fail.

### 5.3 Missing noncoprime chains

At `q=v=5,r=5`, all three primitive residue chains must be emitted. A single
`(q,v)` step is rejected.

### 5.4 First-cell Mertens projection

The coherent first critical cell must remain visible. Any implementation which
annihilates it is incomplete.

### 5.5 Digit endpoint

Replace the signed dyadic endpoint sum by termwise absolute values. The sharp
binary digit identity and the carry constant must be lost.

## 6. Landau review

After `mathfrak C>=0` is accepted, verify only:

1. trivial convergence for `Re z>1/2`;
2. removability at `z=1/2`;
3. absence of real zeta zeros in `(1/2,1)` via eta;
4. Landau's singularity theorem for a nonnegative Mellin density;
5. noncancellation of a hypothetical off-line zero in `(T-23601.3)`;
6. functional-equation symmetry.

No square-screw normalization is needed for the logical proof. The carry and
square-screw replays are independent consistency checks.

## 7. Classification rules

```text
L-23601 finite algebra                      VERIFY / REJECT independently
L-23602 transform and dyadic bridge         VERIFY / REJECT independently
L-23603 quotient identity                   decisive proof hinge
T-23601 deduction from L-23603              conditional composition
X-23601                                    finite regression only
RH                                          not accepted before full review
```

An omitted quotient face, sign-indefinite endpoint measure, or unreflected cross
term classifies `L-23603` as `REJECTED`, not `VERIFIED WITH FIXES`.
