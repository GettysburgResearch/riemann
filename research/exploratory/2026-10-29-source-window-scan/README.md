# Intermediate density sources in the return: guarded point scan

**Status:** Exact-rational scalar scan of the pinned source and return formulas, not a Lean certificate or a new zero-free theorem. The physical source envelope below is a proposed finite-source extension of the current one-source schedule; the existing schedule does not itself prove it. See [scan.py](scan.py), which asserts the SHA-256 of the exact PR94 `ChainF50/Chain.lean` it reads.

At θ=8738694/10⁷, h=80599/10⁵, δ=223/500 and p=1/2, the script reads all 130 source faces (boot and steps 1–129). For each it evaluates, in exact rational arithmetic, the uncapped and one particular capped count branch and the 15 scalar `admissionGuard` expressions transcribed from the pinned `Return/Formulas.lean`. The capped test uses a branch cap slightly below that face's source cap. This is one point, not a neighborhood certificate, and it is not an optimization over all weaker B values, larger λ values or alternate branch caps. All 130 uncapped point branches pass these scalar inequalities. Their smallest count exponent is step 129:

    R_129=137478360780643/225606975000000
         =0.609371056815… .

The old counting branch at this θ has exponent 0.612763447532…. The capped branches at the particular caps just described do not pass all 15 point guards. In particular this does not rule out a capped branch with a different cap or a different admitted window.

For a fixed physical numerator cap `s=619/10000`, the same script keeps sources satisfying the scalar fields `2≤λ≤9/2`, `0<B≤1`, `s≤sourceCap`, and `0≤1−B/2−(9/2−λ/2)s`. Exactly 115 of the 130 listed faces pass: boot and steps 1–114. For a source (B,λ), the physical width on the new-conductor interval is

    C_(B,λ)(d)=min{s d, [2y−(2−B)d]/λ}.

At the geometry above, and `19/25≤d≤h+10^−10`, exact rational pairwise crossings give the following pointwise upper envelope (decimal endpoints rounded; the script retains exact rationals):

    cap s d       0.760000000000 ≤ d ≤ 0.803719939976
    source 70     0.803719939976 ≤ d ≤ 0.803791137938
    source 69     0.803791137938 ≤ d ≤ 0.804412178552
    source 68     0.804412178552 ≤ d ≤ 0.805035577484
    source 67     0.805035577484 ≤ d ≤ 0.805664474747
    source 66     0.805664474747 ≤ d ≤ 0.805990000100.

At the top endpoint the step-66 capacity is approximately 0.0487177670242. The fixed step-64 capacity is approximately 0.0487163293. Both are below the cap there. More strongly, the uncapped step-66 line exceeds the uncapped step-64 line throughout the entire interval: the script checks exact positive endpoint differences `8038773107/75701058750000` and `43535683687605953/30280423500000000000000`. Their difference is affine, and applying the same min with s d preserves the inequality. Thus one may investigate a **single** step-66 physical source, with no interval-dependent physical face. Step 64 can still supply its separately defined capP count windows, but the concrete current constants couple those two uses and an amended certificate must separate them. The improvement is small; these point and edge comparisons do not prove the full δ,p row inequalities or a new endpoint.

## What the interfaces permit

`CountScheme` stores a finite list of `AdmittedWindow` values, and each window has its own B, λ, source cap and source face. Thus different intermediate source faces can in principle back different count windows; the 15 point guards must still be certified on each whole proposed window, with the literal cutoff, inverse, plain, natural-tail, width and antitonicity conditions. In `PhysicalDirect/ChosenSource.lean`, the actual premise asks for one positive mesh valid for all windows. For a finite list, the source's `UnitFaceSource.mono_mesh` permits taking the positive minimum of the individually supplied meshes. Choosing a face after a bin is known must still respect the source's stated quantifier order and the finite presentation/height losses.

By contrast `ReturnD/Schedule.lean`'s current `PhysicalSchedule` has one fixed `physicalB` and `physicalLambda`, and its `new_rows` and `PhysicalDirect/ChosenSource` use that one physical face. A pointwise max over several sources is **not** an instance of that structure. To use the envelope one needs a new theorem that partitions the physical conductor parameter into finitely many intervals, applies a valid global source on each, and reunites the resulting bounds with one compatible mesh, common source data and cumulative height budget. The crossings above are candidate interval boundaries for such a theorem, not evidence it is already implemented. In addition, the existing physical schedule demands 2≤λ≤9/2, so steps 115–129 cannot simply be used as physical faces even though the corresponding count-window admissibility only needs λ>1.

The scan transcribes the point guards and verifies the source-file hash. It does not prove the Lean source theorems independently, verify all interval guards, compile an amended schedule, or assume any new selected-norm estimate. The exact pinned theorem for each source is conditional on the source chain's imported dependencies.
