# Independent review of the squareclass projection obstruction

Reviewed 18 October 2026 by the theta research agent. This is an internal independent reconstruction, not external referee acceptance.

Source: workspace `QUARTIC_SQUARE_SELECTOR_LATE_DRAFT.md`, intended publication `quartic/SQUARECLASS_PROJECTION_OBSTRUCTION.md`, actual-byte SHA256
`7769a60d2f513c49ae4219199e664eaa7d91ef37d2585d1c317315972d857853`.

I read the entire draft and rebuilt the proof from the unitary common-cover construction and the literal Kubota multiplier in David--Dunn--Hamieh--Lin, arXiv:2306.11875v2, Section 4.3 and its stated quartic reciprocity identities. No unramified representation or pure-tensor interface is needed.

The CRT construction is valid with composite squarefree D: a can be chosen 1 modulo lambda^4 with prescribed nonzero square/nonsquare residues. The u congruences are compatible, and u=1 modulo a guarantees (a,c)=1 for c=D lambda^4 u. No coprimality between u and D is used. The excluded choices u=0 and a-lambda^8bu=0 can be avoided. Choosing d inverse to a modulo c lambda^4 makes the original gamma integral and lambda^4-deep.

For gamma'=n(-t)gamma n(t), t=lambda^4 b/D, the upper-right integrality condition is exactly D dividing a-d-lambda^8bu. The other entries have the required lambda level. Its top-left entry a' is inverse to a modulo D and congruent to a modulo u, and both a,a' are 1 modulo 4 and coprime to c. Quartic reciprocity therefore cancels the u symbols without any squarefree assumption on u or a, and gives the multiplier ratio (a/D)_2=-1. All lambda fourth-power factors and reciprocity signs are paid.

The translated function and original function are eigenvectors of the SAME unitary D_(gamma') with opposite eigenvalues. This proves the exact correlation zero. Reducing a nonzero b modulo squarefree D by its gcd supplies every other nontrivial additive term. The good-prime trace pairing is nondegenerate, so the finite Fourier projections are orthogonal and their quadratic forms have only the b=0 term. This gives exactly uniform residue mass and, by CRT, the stated joint product for arbitrary allowed local subsets.

The squareclass allowed set includes zero and has cardinality (q+1)/2 at every good prime. Hence the exact norm factors are at most 3/5, and the decreasing commuting projections annihilate the original vector strongly. No local-global sufficiency claim is required. The possibility of a nonzero explicitly retained base-cusp Fourier coefficient in a local smooth limit is correctly distinguished from the zero Hilbert limit; it does not contradict the calculation because the fixed-cusp trace is unbounded.

No blocking error was found at this scope. The theorem concerns these explicit quadratic-residue projections of a same-character vector. It does not exclude a descent/kernel construction, prove failure of every square-selector, control a weighted period, or establish a new zero-free region.
