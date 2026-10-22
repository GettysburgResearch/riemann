# M-23813 — Final weighted-shell review boundary

Claim ID: `M-23813`  
Title: Consolidated adversarial protocol after the unweighted prime-tail drift correction  
Status: **REVIEW PROTOCOL — NO RH PROOF CLAIM**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Issue: #238  
Scope: canonical review front door for the live carry/Green arithmetic family

## 1. Consolidation decision

The live carry programme contains several exact finite coordinate systems:

```text
triangular carry inversion;
endpoint-projected Green equality;
Green–Skorokhod clipping;
prime oversupport affine lift;
positive endpoint-scale frame;
ordinary-prime dipole transport;
dyadic two-contact and factor-five source;
weighted shell-tail transport.
```

They do not define independent conclusion-producing theorems.  After the latest
stress tests, the canonical review target is the **weighted dyadic shell tail**
of `L-23823`--`L-23826`.

The unweighted ordinary-prime queue is not the final theorem.  The density-drift
calculation on PR #274 gives a proposed asymptotic of order

\[
\sqrt X/\log^2X
\]

for its full suffix and therefore rules out the required subpower rate.  The
weighted dyadic shell removes that deterministic first-order drift before the
tail maximum is formed.

## 2. Frozen live inputs

The consolidation was made against the following immutable heads:

```text
PR #240  b64c8136c790c76db4d9527f938e809111bab3b8
PR #248  5f2b25f89afbb90a3bc4ca6d40148f530303eb54
PR #265  e0ad1484d70098eb7c8be17655ea08568d5e2cd2
PR #269  51ce086be09be6849c89aa69e22fcff2665b0c03
PR #270  1efc886cc2cd41f01b51c9d8ca789379d174aad9
PR #271  9f5ac31cb975fd95a46eabf5af0b648e7c6bd126
PR #274  c2e1a978a0156944c26132943fa41bcf7c838fec
PR #202  d4c8e59f8f3f992a76fd48ad13bef78505dca7cc
```

No status from a source PR is inherited automatically.

## 3. Canonical theorem stack

The preferred review spine is:

```text
L-23823  normalized continuum tails and fixed-ratio shell moat
L-23827  atomwise endpoint tail majorization
L-23824  exact weighted prime-tail transport
X-23821  exact rational transport replay
L-23825  finite shell profile and Chebyshev remainder
L-23826  in-support weighted shell assembly
T-23811  WSTS implies RH
T-23812  RH implies WSTS; exact equivalence boundary
```

The sole open statement is

\[
\boxed{
\mathrm{WSTS}:
\max_z
\left[
\sum_{z\le p\le X}
(\log p)
\bigl(r_X(p)-\mathbf1_{p\le\lfloor X/2\rfloor}r_{\lfloor X/2\rfloor}(p)
\bigr)
\right]_+
=X^{o(1)}.
}
\tag{M-23813.1}

Equivalently, after retaining the proved negative continuum moat, it is enough
to prove

\[
\boxed{
\sup_z
\left(
X^{-1/2}
\int_{[z,X]}
E_{1/2}(t/X)d[\vartheta(t)-t]
\right)_+
=X^{o(1)}.
}
\tag{M-23813.2}

`T-23812` shows that this theorem is equivalent to RH, not merely sufficient.

## 4. What has been removed from the proof burden

The review should not reopen the following completed reductions unless it finds
an exact error in their stated hypotheses:

```text
parabolic objective constant four;
proper-prime-power tail O(log^2 X);
continuum tail order and quantitative shell moat;
endpoint-atom continuum order;
carry-floor approximation and summable floor error;
finite weighted tail transport and its min-cut charge;
physical positivity / Green / affine geometry;
conditional square-screw and Landau transfer.
```

In particular, the Green and affine branches establish that physical
nonnegativity is not a separate asymptotic obstruction.  The exact zero-tax
ordinary-prime deformation makes the same point from LP duality.  Their
remaining scalar is the same prime-ramp mode represented by `WSTS`.

## 5. Superseded or rejected proof hinges

Do not count any of the following as support for `WSTS`:

```text
unweighted prime-tail queue PTQ/PTC;
nonnegative monotone Divisibility Cover;
generic Green-energy smallness;
universal block-normalized Selberg–Mourre inverse;
bounded endpoint-face or source-rank claims;
one-frequency physical-block identification;
conditional-Hankel positivity;
finite numerical ladders.
```

The exact finite algebra surrounding these routes may remain useful, but their
former conclusion-producing statements are not dependencies.

## 6. Mandatory mutations

A claimed proof of `WSTS` must survive all of the following.

### 6.1 First fixed-ratio Mertens cell

The exact `2/3` Farey/Mertens increment must appear in the weighted shell or be
carried through an explicit causal fixed-ratio filter.  It may not disappear
under an unsigned estimate.

### 6.2 Dyadic source

The source

\[
b_2(n)=\mu(n)-\mathbf1_{2\mid n}\mu(n/2)
\]

and its two-contact/bottom-charge projection must be recoverable from the shell
ledger.  The odd target may not be replaced by the already controlled odd
leakage load.

### 6.3 Density-drift mutation

The proof must explicitly use the weighted shell difference.  Applying its
argument to the unweighted full ordinary-prime suffix must reproduce, rather
than contradict, the proposed positive drift of PR #274.

### 6.4 Complete boundary accounting

Every reciprocal knot, shell cutoff, prime endpoint, floor remainder, and
Stieltjes endpoint convention must be declared before taking a positive part.

### 6.5 Logarithmic ray

The von-Mangoldt/logarithmic dual direction is the prime-ramp discrepancy.  It
may not be projected out as Green-orthogonal or dismissed by a generic frame
bound.

## 7. Automatic rejection conditions

Reject a proposed completion if it:

```text
uses PNT error alone as though it were subpolynomial;
treats fixed-ratio convergence as uniform at a shrinking ratio;
takes absolute values before the dyadic shell subtraction;
uses the unweighted queue as the conclusion-producing scalar;
omits the Chebyshev Stieltjes remainder;
drops a reciprocal-knot or shell-cutoff term;
replaces the two-frequency physical block by H(z)^2;
uses a finite computation as a cofinal theorem;
claims RH while WSTS remains an assumption.
```

## 8. Review classifications requested

Review each component as one of:

```text
VERIFIED
VERIFIED WITH FIXES
GAP/BLOCKED
REJECTED
```

The full proposal can be accepted as an RH proof only if `WSTS` is proved from
unconditional inputs.  Verification of the exact reductions alone leaves the
proposal `GAP/BLOCKED`.

## 9. Exact status

```text
continuum shell geometry                  PROPOSED COMPLETE
endpoint-atom continuum transport         PROPOSED COMPLETE
finite weighted transport                 PROPOSED COMPLETE
finite shell / floor reduction            PROPOSED COMPLETE
WSTS <=> RH                               PROPOSED COMPLETE EQUIVALENCE
unconditional WSTS                        OPEN / RH-BEARING
Riemann Hypothesis                        NOT PROVED
```
