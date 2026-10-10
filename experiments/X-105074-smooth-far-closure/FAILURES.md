# A2 FAILURES — dead ends and refuted routes (mandatory ledger)

F-A2-1. POINTWISE FORM (a) FOR THE SMOOTH FAR FIELD IS FALSE AS STATED (if any far pinch
exists). Prop G's target "|Z| + |Z'| <= M_far on Omega^+" cannot be proved unconditionally:
at a hypothetical simple far pinch s', the DERIVATIVE genuinely blows up like (s-s')^{-1/2}
(A2.md 3.2, K2) — this is intrinsic, not an artifact of the method. What IS true: Z itself
stays bounded at simple pinches (K1), and the D_half window h-mass vanishes. The correct
unconditional target is the L2/sequence form of Theorem A2, and P2.7 provably accepts it.
Any successor claiming pointwise (a) for the smooth field without excluding pinches has a
counterexample-shaped hole.

F-A2-2. RESIDUE-EXTRACTION ROUTES ARE DEAD, PERMANENTLY. Every attempt to write the pinch
contribution as (coefficient) x (s-s')^{+-1/2} extracts Res 1/zeta at rho = 1/zeta'(rho):
no unconditional lower bound on |zeta'(rho)| exists (its absence is Prop G's hypothesis (ii)).
First-draft near-pinch estimate here did exactly this and was scrapped. The repair — the
whole lane's load-bearing move — is on-contour evaluation only: |1/zeta(w)| <=
|w - rho|^{-1} e^{CL(T)} needs zeta' of nothing; and the numerator zeta^{1/2}(2a - w)
VANISHES like d^{1/2} at the branch point (it is a ZERO of zeta, unlike the v=1 POLE that
drives the main pinch), cancelling the pole's d^{-1}. Route marker: any future far-field
work should treat "does 1/zeta' appear?" as the first triage question.

F-A2-3. EPSILON-SMALLNESS OF THE SMOOTH FAR CONTRIBUTION IS UNACHIEVABLE with explicit
constants: the band [60, T_x] (verified height to Gevrey/Borel-Caratheodory crossover,
T_x ~ 1e3-1e5 for realistic (c_delta, C)) contributes bounds of size 1e9-1e80 (gevrey_num.py,
machine-verified finite). A route needing "smooth part < eps |c_P|^2" dies here. SURVIVES
because the architecture only needs FINITENESS: bounded pieces have window h-mass O(h) -> 0
(P2.7 step (5)-(6) kill them; smallness is needed only for pieces carrying their own 1/h
mass). Recorded so nobody re-attempts the smallness version.

F-A2-4. UNIFORM-IN-h STATEMENTS FAIL FOR ZERO CLUSTERS (m >= 2 zeros colliding with one
branch point): Z itself can blow up like (s-s')^{3/2-m}, whose window L2 mass diverges as
h -> Re s'. Cannot be excluded unconditionally (that WOULD be an anti-conspiracy hypothesis
— exactly what we must not assume). Repair: the explicit exclusion set H_ex (widths
kappa_j^{1/(2 m_j)}, super-summable), limsup along H_good. NOT a loss for the architecture:
P2.7's contradiction extracts h -> 0 along a sequence (checked, A2.md 5.3). A route that
insists on all-h uniformity is dead unconditionally.

F-A2-5. THE STRAIGHT-LINE (NO-THREAD) FAR CONTOUR IS DEAD (recorded for completeness,
inherited from P2.8(b)): on Re z = 1/16 the factor 1/zeta(a - z) is evaluated at
Re = 11/16 + (3/2)h at unbounded heights; hypothetical zeros there make it non-locally-
integrable; no fixed line works since h sweeps (0, 5/24]. Threading is forced; the w-plane
(t-independent base) is the right chart because the poles are the s-independent objects.

F-A2-6. z-PLANE s-INDEPENDENT CONTOUR (the brief's first suggestion, taken literally) is
IMPOSSIBLE: in the z-plane the poles a - rho sweep rectangles of width 3/8 x height 3 r_0
as s sweeps the window; an s-independent contour would need a zero-free corridor of that
width at every height — a zero-repulsion hypothesis. The salvage is the w = a - z chart,
where the BASE LINE is t-independent (only bulges near branch points move with s): the
brief's "where possible" realized precisely.

F-A2-7. Numeric dead end: none. Both scripts ran clean; pairs_num confirms the vacuousness
of the pinch set below height 163; gevrey_num confirms finiteness (values astronomical, as
F-A2-3 records) and measured Gevrey constant c ~ 1.5-2 at delta = 1/4.
