# Proposed 23/24 Dedekind zero-free refinement

**Status: proposed unconditional theorem, with a complete composition proof;
independent mathematical review is required.** This is not an RH proof or a
new best bound for ordinary Riemann zeta. The claim improves the ALL-NUMBER-FIELD
boundary of Cureton--Thorner v2 from 31/32 to 23/24, using their analytic
construction and de Faveri's new sixth-power-free zero-density estimate.

## The result

For every number field K, the proposed proof gives

    zeta_K(s) != 0 for Re(s)>23/24, s!=1.

The finite-order Hecke corollary follows with the standard principal-pole
exception. No uniform constants across fields or conductors are asserted.
The pre-existing stronger special-case 7/8 result is not improved.

Read **PROOF.md**, particularly Sections 2--3 BEFORE the margin table. The
new ingredient is not merely numerical optimization: all Poisson denominators
must be covered by the density theorem, including their S-unit twists.

## What changed in the argument

The exact family matching identifies each frequency with a sixth-power-free
ideal and one of finitely many fixed unit twists. A coefficient-preserving
adapter supplies the density bound for that full family. At sigma=41/50 the
unrounded exceptional exponent is 2563/4267; it can be enlarged to 601/1000
after paying a small, fixed field-dependent height range.

At the rescaled X=Z^(11/20), Y=Z^(103/200), the complete reflected bound is
still supplied by CT's fixed-M>1 argument. The actual theta average is
O(Z^(123/400+epsilon)). The Poisson reference is C=7/20, and the Gaussian
principal detector must therefore use normalization b=13/20, not 61/100.
All seven error sectors have a saving exceeding 1/24. The least Poisson
saving is 8410759/200000000; it still exceeds 1/24 after a total 1/10000
power-loss allowance. Thus the actual detector satisfies f(Z)<<Z^(37/120),
and 13/20+37/120=23/24 gives the region.

## Sources and unresolved tasks

CT v2, DF Theorem 1.1 and its zero-detector calculation, and the classical
BGL detector are imported unconditional mathematical inputs. They are not
rebuilt in Lean or certified by our finite checks. SOURCES.md names their
versions, exact uses, and the sections actually inspected. The composition
and its fixed-twist/family/scale adapters are new proposed arguments here.
No global literature-priority claim is made.

Independent review should first challenge the fixed unit-twist adapter and
its complete-column central mean, then the arbitrary-fixed-M reflected
estimate, contour domains, and the final Mellin normalization. A defect in
one of these analytic steps would invalidate the asserted improved theorem
even if every rational check passed.

The critical fixed-center native covariance from #955 remains unresolved.
This continuation neither assumes nor proves it. It also does not promote
any of the preceding averaged moments or torus obstructions to an RH theorem.

## Reproduce the finite certificate

    python verify.py
    python -O verify.py
    python -m unittest -v test_verify.py
    python -O -m unittest -v test_verify.py

The checker uses exact rational arithmetic and no assertions disabled by -O.
It covers every term of the specialized density inequality, all 13 contour
vertices (143 strict linear inequalities), reciprocal-disk buffers, all seven
new margins, and the final normalization. Eight tests also reconstruct CT's
original margin table and execute six corrupted parameter files separately.
These are arithmetic checks, NOT a proof assistant or independent referee.

Publication is add-only on a new branch, based on #955 at
6d3d69c7896e3a5d61d1f67e4627125257398ec7. No inherited proof, checker, main,
or integrated-status file is changed. The old local norm-fiber companion
remains at its separately recorded publication status; it is not republished
or credited as an input to this theorem.
