# Sharp ceiling for the prescribed quartic polynomial-moment objective

Proposer: semantic_skeptic. Date: 17 November 2026. Status: exact derivation independently checked by li_advocate; director adjudication pending. This is a finite moment/certificate observation, not a bound on the true proportion of simple critical zeros, not a limitation on all quartic certificates, and not a historical-novelty claim.

Keep the specific polynomial

p(x)=1-7x/4+2x²/3, q(x)=1-p(x)².

For any probability measure mu with finite fourth moment, Jensen/Cauchy–Schwarz gives the exact inequality

integral q dmu
 =1-integral p² dmu
 <=1-[integral p dmu]².

Consequently, whenever m1(mu_T)->1 and m2(mu_T)->4/3,

limsup integral q dmu_T<=1-(5/36)²=1271/1296.

Using the exact identity

integral q dmu_T=(D_T-85)/36+o(1),

D_T=84m3(mu_T)-16m4(mu_T),

this sharpens the simple consistency bound D<=121 to

limsup D_T<=4331/36.

These statements apply to Hermitian empirical measures as well: (Tr p(F))²<=d Tr p(F)². No positive-semidefinite matrix hypothesis is required.

## Sharpness under these first two moments

Let r_minus<r_plus be the two roots of

24x²-63x+31=0.

Their sum is21/8 and product31/24, so both are positive. Also(r_minus-1)(r_plus-1)=-1/3, hence r_minus<1<r_plus. Give them positive weights

w_minus=(r_plus-1)/(r_plus-r_minus),

w_plus=(1-r_minus)/(r_plus-r_minus).

This is a probability law with mean1. Its support satisfies x²=(21/8)x-31/24, giving second moment4/3. On both support points,

p(x)=5/36.

Jensen is therefore an equality. The law attains objective1271/1296 and D=4331/36. Its next moments are53/24 and2347/576, which independently reproduce that D value. Approximating its weights by empirical eigenvalue multiplicities shows sharpness for asymptotic finite-matrix moment sequences with these limiting first two moments.

## What the ceiling means

In the exact count transfer with d/N->1 and normalized HS error->0, this particular certificate yields the lower-bound expression2 integral q-1. That expression can never exceed

2*(1271/1296)-1=623/648

under the stated first two moments. This is a ceiling on **what this one prescribed lower-bound certificate can certify**, not an upper bound on the actual simple-critical proportion. The sharpness law itself has entirely positive support, illustrating the distinction.

This ceiling does NOT apply to the clipped objective integral h with h=max(q,-1), which is generally larger than integral q. The final moment-only relaxation in the transfer replaces h by q, and it is that relaxed polynomial expression alone which is bounded here. Rare large outliers can keep the first two moments fixed while integral h tends to1 and integral q tends to minus infinity; the explicit construction is in `audits/adversarial_reviews/quartic_ceiling_independent_round3.md`. No cap on that clipped objective is asserted.

Other quartic or higher-degree certificates can behave differently. No obstruction to a moment ladder, a different polynomial, or density1 is asserted. The useful conclusion is to keep the arithmetic target D and the eventual choice of certificate explicit when optimizing a finite-prefix method.

Independent source-free algebra/sharpness and scope review: `audits/adversarial_reviews/quartic_ceiling_independent_round3.md`.
