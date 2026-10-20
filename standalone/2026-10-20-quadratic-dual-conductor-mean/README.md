# A conductor average from a quadratic dual family

20 October 2026. **Proposed analytic component theorems with explicit
external inputs. No improved zeta or Hecke zero-free boundary is claimed.**

This continuation of PR #1010 replaces summation of its individual
conductor bounds by an actual conductor average. The key is not a cheaper
local Gauss bound: a varying sextic character becomes a quadratic
character on the dual side of the cubic theta functional equation.
An asymmetric two-piece decomposition can therefore use different large
sieves on its two sides.

## Results

Write p=(2 beta+1)/6, with 5/6<=beta<1, and assume a common zero-free
half-plane Re(s)>beta for the finite-order Hecke completion characters.
Liu's imported preprint supplies beta=B_flat; beta=7/8 is a weaker usable
input. No proposed infinite-order Hecke theorem is used.

For K,C>=1 define

    H_p(K,C)=max(
        K^(1-3p/2) C^(2-7p/4),
        K^(1-12p/11) C^(2-20p/11),
        K^(1-p) C^(2-2p)).

The [proof](PROOF.md) establishes a completed-series second moment with
this bound, without any zero-free input. Removing the completion gives

    sum_(c squarefree, Nc~C) |S_(f,c)(X)|^2
       << (XFC)^epsilon X^(2p) H_p(K,C),

where S uses the actual normalized cubic Gauss coefficients and the
character psi_f (./c)_6; f is a squarefree fixed-within-the-average
modulus, F=Nf, and K=F0 F1^2 is its exact matching/nonmatching level.
The estimate is uniform in f, not an unspecified fixed-conductor constant.

All sixth-power-free rows can also be retained. With their explicit
possible residues subtracted,

    sum_(Nu~U, u sixth-power-free) |S_u(X)-P_u(X)|^2
       << (XU)^epsilon X^(2p) U^(2-7p/4).

Only rows u=r^4 can have a main term. They are centered explicitly,
not discarded. For a bounded coherent short-divisor mark, including a
Mobius mark, the complete centered mean is bounded by

    (ABU)^epsilon A^(2p) B^2 H_p(B,U).

These sums are defined precisely in PROOF.md and ALL_ROWS_AND_MARKS.md.
The angular degree is zero; common radial smooth profiles and fixed
bad-prime/ray conventions are retained. Arbitrary angular parameters or
arbitrary rowwise arithmetic coefficient arrays are not claimed.

## Numerical meaning

At beta=7/8, p=11/24 and the unmarked conductor exponent is

    2-7p/4 = 115/96 = 6/5-1/480.

At the more precise B_flat it is approximately 1.197982789226688.
This exponent belongs to the stated Gauss-weighted mean, NOT to the
original inverse/plain moment in PR #1006. The numerical coincidence
with its 6/5 target does not prove its hypothesis.

For total scale Y, short length B=Y^(1/4), long length A=Y^(3/4), and
row scale U=Y^(3/10), the new centered root-mean-square bound is
Y^(109/160+epsilon) using beta=7/8. The comparable Euler-only averaged
baseline is Y^(153/220+epsilon). Neither number is a zero-free boundary.

[SCOPE_AND_AUDIT.md](SCOPE_AND_AUDIT.md) records the actual remaining
transfer, the old-proof audit, an unsuccessful direct consumer test,
and limits on review and numerical evidence.

## Verification and provenance

    python -I -S -B verify.py
    python -I -S -B -O verify.py

The checker proves the scalar inequalities over their continuous parameter
ranges by exact affine/bilinear identities, checks the local quadratic
character transition, and tests the complete row-exponent bookkeeping.
It is not a proof assistant for the analytic estimates.
[SOURCES.json](SOURCES.json) pins the imported papers and repository
commits. [VALIDATION.md](VALIDATION.md) records executed checks.
No independent human or separate-agent review, remote CI, or integration
approval is asserted. Main and the prior research files are unchanged.
