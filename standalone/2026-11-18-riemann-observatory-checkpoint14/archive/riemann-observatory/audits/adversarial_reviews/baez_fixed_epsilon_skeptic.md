# Targeted independent check: Báez-Duarte fixed-epsilon majorants

Reviewer: li_advocate. Date:2026-11-17. Source inspected: arXiv:math/0205003v1, pp.3–6, especially Lemmas2.1–2.2 and the p.5 domination passage. This is a targeted passage review, not another whole-work audit. The equivalence agent supplied the suspected exponent restriction and an alternative bound; both were independently checked.

Lemma2.2's unconditional modulus inequality

|ζ(1/2−ε+it)/ζ(1/2+ε+it)|≤C_(ε0)(1+|t|)^ε, 0≤ε≤ε0<1/2,

is correct. Functional equation and conjugation express its modulus as

π^(−ε)|Γ(1/4+ε/2+it/2)/Γ(1/4−ε/2+it/2)|.

The real gamma parameters remain in a compact subset of(0,∞); uniform vertical Stirling and compact-region continuity prove the stated bound. If the denominator vanishes at a fixed ε,t, reflection/conjugation gives the numerator a zero of the same order. The quotient as a function of t at fixed ε has a removable local extension; for L² purposes arbitrary values on the isolated exceptional ordinates also suffice. Joint continuity in both ε,t is neither asserted nor required.

On p.5 the printed bound K_ε(1+|t|)^(−1+2ε) is square integrable only for ε<1/4. It does not by itself justify the following range ε0<1/2. The main theorem only needs sufficiently small positive ε, so restricting to ε0<1/4 repairs that step without altering the argument's goal.

An alternative repairs every fixed0<ε<1/2. In Lemma2.1 the positive error exponent η is free, independently of the shift δ=ε. Under RH, functional equation plus Lindelöf gives

|ζ(1/2−ε+it)|≪_(ε,η)(1+|t|)^(ε+η).

Decomposing the Dirichlet partial sum into1/ζ(1/2+ε+it) plus the Balazard–Saias error, the quotient term divided by1/2−ε+it is O((1+|t|)^(ε−1)), and the error term is O_ε,η((1+|t|)^(ε+2η−1)), uniformly in the truncation n≥2 after discarding n^(−ε/3)≤1. Choose0<η<(1/2−ε)/2. This is an L² majorant for every fixed ε<1/2. Its constant need not be uniform as ε→0; no such uniformity is required for the fixed-epsilon truncation limit.

The final ε↓0 stage is different. Lemma2.2 supplies a genuinely uniform majorant O_ε0((1+|t|)^(ε0−1)), square integrable for ε0<1/2. The quotient tends to1 for almost every t. At a critical-line zero of multiplicity m its horizontal ε-limit can instead be(−1)^m, but this countable set of ordinates has measure zero and does not obstruct dominated L² convergence. It would be incorrect to assert pointwise limit1 at every critical zero.

The phrase 'without the assumption of the Riemann hypothesis' at this last stage concerns the gamma-ratio estimate and its boundary-function convergence. The preceding identification of those functions with Mellin transforms of the constructed H-elements remains conditional on RH; the proof does not establish RH unconditionally.

Classification: the displayed p.5 majorant needs a narrower parameter range than the following sentence suggests; the main theorem is repaired by the already sufficient small-epsilon range or by the free-exponent argument above. No fatal theorem error or new contradiction is claimed, and later versions/corrections were not audited in this targeted review.

## Additional independent algebraic checks of preprint normalization/exponent typos

The equivalence agent requested checks of two further local printed expressions in the same preprint. The extracted primary PDF passages were inspected; the journal version was not compared.

First, the preprint defines K with measure(2π)^(−1/2)dt while defining M without a Fourier prefactor. For χ=1_(0,1], Mχ(t)=1/(1/2+it), so ∫|Mχ|²dt=2π and ||χ||²=1. The printed K measure would give squared norm sqrt(2π), not1. The asserted isometry therefore requires dt/(2π), or a corresponding normalization of M. This is a fixed harmless norm scaling for the closure argument, but the printed isometry constant is inconsistent as written.

Second, definition f_(2ε,n)=∑_(a≤n)μ(a)a^(−2ε){1/(ax)} gives, for x>1,

f_(2ε,n)(x)=(1/x)∑_(a≤n)μ(a)/a^(1+2ε).

Equation(2.9)'s displayed1+ε instead of1+2ε is inconsistent with that definition. Either exponent yields the required fixed-ε bound O_ε(1/x) by absolute convergence, so this does not break the convergence argument.

These are scoped algebraic inconsistencies in the inspected preprint expressions, not a claim that the main theorem is false or that the later journal text retains them. The source-version boundary remains explicit.
