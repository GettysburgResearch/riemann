# R2 VERDICT: the reductio-side L2 refinement through D_half
VERDICT: R2 does NOT close independently. Its "one log short" gap is real and exactly
quantified (F2: pointwise/Minkowski routes give h int_WIN |D_half Z_far|^2 <= C log(1/h),
target O(1)); the proposed L2-multiplier repair EXISTS and is proved here (F3: D_half is
exactly the sqrt(x)-multiplier on the x-side; F4: its commutator with the frequency window
is bounded, norm <= (1/2) int |v w(v)| dv, uniformly in h; the weighted-operator norm of
sqrt(x) on e^{-hx}-weighted L2 is (2eh)^{-1/2}, which is where the naive route loses).
But the repair converts R2's endpoint into precisely the inequality (FAR-WIN) — the same
residual that R1 reaches — so R2 is structurally blocked as an INDEPENDENT route: it has no
input about WHERE in frequency the far field's log(1/h) line mass lives, and that location
is the entire question.

Reason, in two paragraphs. (1) What the reductio supplies is a line-L2 budget: the unweighted
far field has int_R |Ztil_far(h+it)|^2 dt <= C log(1/h) (F1). D_half must upgrade this to a
window bound after multiplication by sqrt(x) ~ (1/h)^{1/2} on the effective support. Any
route that treats the window as a subset of the line pays the full multiplier norm
(2eh)^{-1/2} on the full budget: h * (1/h) * log(1/h) = log(1/h) — one log over, and this is
SHARP for the method: the pinch term itself saturates the line budget's log(1/h) with a
1/x-density that the sqrt(x)-weight turns into exactly 1/h, so no norm inequality that
forgets frequency location can do better. (2) The only additional structure available is
frequency localization, and F3/F4 show the localization commutes with the multiplier at O(1)
cost; after commuting, the needed statement is that the frequency-localized far field's
x-density is o(1/x) — or 1/x with small constant — relative to the pinch's. That is a
statement about the arithmetic field at the single frequency gamma_1/3 ((FAR-WIN)), not about
the reductio: the negation hypothesis is frequency-blind and cannot supply it (F5 shows the
reductio's own J-bound gives the window mass only up to a vacuous self-referential factor
27.5). Conclusion: R2's multiplier refinement is the correct FORM of the missing step and is
proved as a reduction (FAR.md Sec 3); its closing content is (FAR-WIN), which R2 cannot
produce. Timeboxed verdict: structurally blocked as an independent closer; merged into the
single residual inequality.
