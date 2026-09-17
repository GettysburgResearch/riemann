# Reviewer handoff: calibrated span charge

Status: complete proposed argument for a modest global proportion bound; no
independent acceptance yet. The intended comparison is with the pinned repo
280-block extraction, not the larger 0.673399 preprint claim.

Primary new assertion: PROOF.md Proposition 1, especially E>=q and the optimal
slope statement. The lower-energy phi_m formula is inherited; its conversion
to Delta+(c/q)z>=c is the changed step. Check the sign of the span charge after
averaging all offsets and the endpoint loss p-m+1.

Check the direct Hilbert argument carefully. A=sum m_z v_z v_barz* is Hermitian
but need not be positive. Its trace is total multiplicity because the mixed
inner product is one. Its squared Hilbert--Schmidt norm is the ORDERED sum of
k(z-w)^2, not |k(z-w)|^2. Q's positive index counts at most one per nonreal
conjugate pair; m_z appears in total zero count, not as m_z separate ranks.
These are the points at which an incorrect positivity argument would usually
enter.

The main imported pair-correlation estimate is BGST's unconditional theorem;
classical zero symmetries and Riemann--von Mangoldt are also retained. Confirm the sign in r_T=g-g''/[4(log T)^2]. The two
fixed profiles g and g'' are treated separately before forming r_T, so no
unsupported uniform changing-test estimate is used. Fix each smooth profile
before the large-T limit; only afterward approach the discontinuous limiting
cosine profile. No interval endpoint distribution is used as a smooth function.

The seven-point theorem is a full computer-assisted continuum statement. Its
primitive arithmetic, remainder bounds, range-minimum fallbacks, closed-cell
coverage and Hessian Loewner bound must be reviewed. The old Reviewer A code
was freshly replayed, not reimplemented in this pass. Directed binary64
operations are explicitly part of its trust base. The new constants program
is exact-rational but does not validate that separate pressure computation.

The final inequality is GLOBAL S(T)/N(T), not a fresh dyadic result. A distinct
zero bound is given with its own multiplicity deduction. The decimal constant
is compared using directed rational intervals, not an eigensolver or a sampled
optimizer. Block 322 is sufficient, not asserted globally optimal.

External novelty and record status are deliberately limited: ainta, Reviewer
A, Lamzouri and the original rank--trace work are credited. A stronger public
preprint claim was found and must not be omitted in any publication summary.
No requested review step is an omitted RH-strength inequality.
