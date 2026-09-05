# Uniform prime asymptotics and the fixed-ray obstruction

**The full signed inequality and RH remain UNPROVED.** This is an add-only
continuation of PR #790. Complete proposed proofs are in PROOF.md; independent
mathematical/code review and external novelty assessment are pending.

Base: 337c222a54a232b89b9f47827b2caeb754145efc.
Repository: GettysburgResearch/riemann (repository ID 1309150028; formerly
gfreund123/riemann). All predecessor files are preserved.

## Positive result: the former fixed-time asymptotic is now uniform

For F_(m,t)(x)=(x^2+1/4)^m exp(-t(x^2+1/4)), I=int F, and r=sqrt(m/t),

    |Fhat(ell)/I-exp(-ell^2/(8t))cos(r ell)|
       <=min(2,4(1+t)/sqrt(m)), every m>=1,t>0,ell real.

The proof is an exact Gamma mixture plus an elementary Gaussian score
estimate; it does not assume the desired heat signs.

For L=(log m)/2+2t, m>=max(4,20t), define

    C_t(r)=sum_(n>=2) Lambda(n)n^(-1/2)
                         exp(-(log n)^2/(8t))cos(r log n).

Then

    4pi D_m(t)/I=log(r/(2pi))-2C_t(r)+E_(m,t),
    |E_(m,t)|<=80(L+2)(1+t)e^t m^(-1/4)
             +10sqrt(t/m)+[1+t(20+2log(m+2)+|log t|)]/m.

For every epsilon in (0,1/4), the error tends to zero uniformly for
0<t<=(1/4-epsilon)log m. This extends the parent PH20 beyond fixed time.
It does NOT prove positivity throughout this interval: the signed prime
term is retained. No finite zero verification is used in the new results.

## Exact continuum subtraction

Write E(x)=sum_(n<=x)Lambda(n)-x+1 and
J=int_1^infinity E(x) d[x^(-1/2)Fhat(log x)]. Then, for m>=1,

    sum Lambda(n)n^(-1/2) Fhat(log n)=-I_(m-1,t)/2-J,
    4pi D_m(t)=int F Omega+I_(m-1,t)+2J.

The continuous prime main term is NEGATIVE exactly; its cancellation is
forced by F(i/2)=0. This is a source identity, not a sign theorem for J.

## What must be controlled to finish: fixed spectral center, increasing resolution

For a fixed u>0, put

    B_m(u)=(e/u)^m D_m(m/u), z_u(A)=(eA/u)e^(-A/u),
    R(u)=max_A |z_u(A)|, A=rho(1-rho).

The exact rate is limsup |B_m(u)|^(1/m)=R(u). If RH is false, some FIXED
positive rational u has R(u)>1 and B_m(u)<=-c R(u)^m on a set of integers
of positive lower density. The proof keeps multiplicities, handles coincident
transformed atoms and uses no independence of phases or zero ordinates.

Quantitatively,

    max(1,sup_(u rational>0) limsup_m (B_m(u)_-)^(1/m))
       =sup_A |A|/Re A.

Thus the one-sided source estimate B_m(u)>=-C_(u,epsilon)e^(epsilon m),
for every positive rational u and every epsilon>0, would prove RH. It is
still RH-equivalent and OPEN, not a weaker established arithmetic theorem.
On these rays t=m/u, the center sqrt(m/t)=sqrt(u) stays fixed and the
real width shrinks like m^(-1/2). The new uniform asymptotic does not cover
this regime. Increasing a finite verification range cannot settle all rays.

## Verification and review

Run:

    python verify.py --check checks.json
    python -O verify.py --check checks.json
    sha256sum -c SHA256SUMS

Executed: 2148 finite exact rational/Gaussian-rational controls in each mode,
identical full JSON, and four deliberately corrupted-result refusals.
These are not machine proofs of the analytic statements or a zero census.
No Lean build, remote CI success, independent referee acceptance, or external
priority is claimed. See REVIEW_AND_SOURCES.md and VALIDATION.md.
