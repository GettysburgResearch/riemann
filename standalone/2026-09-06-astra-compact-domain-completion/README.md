# CD26 — compact inverse construction and the global domain cost

Status: PROPOSED COMPONENT THEOREMS; independent review pending. RH and critical
domain completion remain unproved. Author: Astra. Date: 2026-09-06.
Base: PR804 at 4a88ee5ed8be897ed88c85e69e7650ab7e3ddd01.
This is an add-only sibling; no predecessor, review, canonical or formal file changes.

## Main results

For the actual factorial source d_b of CSM26, we construct the compact function

    v_(b,N)(t)=exp((1-b)t) [sum_(n<=exp(t)) mu(n)/n] 1_[0,log(N+1))(t).

Its output f_(b,N)=d_b*v_(b,N) is in the ORIGINAL source-generated L2 domain
and equals t exp(-bt) exactly on the whole interval [0,log(N+1)]. The input
has no delta derivatives. The endpoint coefficient is derived, not guessed.

A hypothetical zero rho=beta+i gamma with beta>b forces the complete error to obey

    ||f_(b,N)-t exp(-bt)||_2^2 >=
       2(beta-b)(N+1)^(2(beta-b))/|rho|^4.

The proof extends to arbitrary locally exact vectors in that domain and to
all zero multiplicities. Local agreement can force GROWING remote norm; it
cannot justify global completion by itself.

At b=1/2, subpower OUTPUT norm along even one unbounded subsequence would
prove RH. The converse follows from the classical RH-to-Mertens implication.
The subpower estimate is NOT proved here. Uniform INPUT norms for this exact
family are impossible: sum_(k<=N)(sum_(n<=k)mu(n)/n)^2 diverges unconditionally.
In the safe range b>1 the construction does converge with an explicit rate.

## Actual finite certificates

Eight fixed critical-source candidates N=1,2,4,8,16,32,64,128 have directed
full-error certificates. Every cell through x=32768 and the entire infinite
tail are controlled. At N=64 the squared relative error is <1/19000.
The errors strictly increase from 16 to32 and from64 to128. These are
particular candidates, not optimal Toeplitz errors or asymptotic evidence.

Read PROOF.md, ATTEMPT.md, then REVIEW.md and VALIDATION.md.
Run from this directory:

    python checks.py --compare checks.json
    python -O checks.py --compare checks.json
    python certificate.py --compare certificate.json
    python -O certificate.py --compare certificate.json
    python validate.py

The proof is noncomputational except for the stated finite certificates.
No numerical zero, zeta/gamma oracle, Lean build, remote CI, or independent
acceptance is claimed. EXTERNAL_INPUTS.md credits the Nyman--Beurling lineage.
