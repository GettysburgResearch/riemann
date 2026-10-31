# Independent review of the complete local Bessel gate

Reviewer: Bessel/local-sign swarm lane, October 31, 2026.

Verdict: **the local analytic consumer, exact coefficient enclosures, full complex-disk pole count, residue tests, and whole-semicircle sign proof check at the scopes claimed**. The two finite actual-source results therefore support the stated all-real-zero conclusion inside `|z|<=20*sqrt(5)`. Neither result establishes an unbounded family or a new zero-free region for zeta.

## Frozen source identities

| File | SHA-256 |
|---|---|
| `LOCAL_WINDOW_CERTIFICATE.md` | `22d7dff1fea511238c036c967bd74d799ffb59dfe4a317185e04715e36de81bc` |
| `certify_bessel_window.py` | `ab83d07bb742ccf2ed3af90168d943b4f3544b33f1433c284b0f220644ae6306` |
| `verify_local_gate_controls.py` | `b88ee0876a6ac64bb270226d4d91964881e7606964c3c798b443d7b88687db84` |
| `LOCAL_CERTIFICATE_10_50_500.json` | `d143656f550fae5822cd9efcbf750b4bbfde11a405452c0f8030d9e040d5ec04` |
| `LOCAL_CERTIFICATE_20_100_500.json` | `1c0323a10287804ef39b5a39f6a0b60acd8e5bedd515c5311b097270f4eb4953` |
| `LOCAL_GATE_CONTROLS.json` | `e72b76cb41de30cec4708408b18e81875931b1548cc011a6bb2bdae8c2b9a125` |
| Prior `verify_polya_obstruction.py` dependency | `cb4f9cb91d4595295974aae955e7782ac9aa8d1fa83c9a4f80f39ae1e7e30989` |

The final note, checker, controls, and source dependency were read in full. I independently reran the order-50 source certificate and both rejection controls using isolated standard-library Python. Both outputs are byte-identical to the saved receipts. The order-100 receipt was inspected and is bound above; I did not rerun that more expensive case. Its acceptance logic is the same reviewed checker.

## Analytic consumer and full-disk coverage

The complex zero count and real brackets have distinct roles. A strict complex count of k, together with k disjoint strict real sign changes, exhausts all zeros counting multiplicity. Thus each located zero is simple and there are no extra complex or multiple zeros. The interval numerator and derivative tests exclude cancellation and give positive residues at all poles inside the disk.

With this coverage established, the maximum-principle argument is valid. A simple real pole with residue gamma>0 contributes `-gamma*y/|E-lambda|²` to the imaginary part. Its holomorphic real-coefficient remainder contributes O(y), so sufficiently small upper puncture semicircles have negative imaginary part uniformly, including arbitrarily close to their real endpoints. The rest of the real boundary has zero imaginary part and the outer semicircle has a strict negative sign. The harmonic maximum principle and its strict version therefore apply. No nonreal interior pole is crossed or ignored.

The decaying Bessel Weyl function has the opposite strict sign, with the correct radial convention `y'(0)=a K'(a)`. Its denominator cannot vanish at a nonreal energy by the usual self-adjoint Dirichlet problem. Hence a nonreal transform zero cannot occur at a regular point or at a denominator zero. Positive source coefficients make the Fourier transform strictly positive on the imaginary z axis, excluding negative real energy. Finally `|E|=|z|²/4`, so R=500 gives precisely the claimed z disk. The strict outer semicircle condition also handles its nonreal boundary points.

This proves a statement about every transform zero in that disk. It does not identify the transform-zero count with the six/eight denominator poles, and the note does not make that error.

## Rational primitive source and scaling

I inspected the inherited interval arithmetic: each operation encloses the exact operation on its input intervals, division rejects zero-containing denominators, and the exponential routine retains its complete rational Taylor tail before scaling and squaring. Changing the loaded namespace's grid to 10^(-130) does not remove that remainder or modify the source file. The 130-term Machin reconstruction encloses pi independently of a floating constant.

For x=n/a>=0, the argument Y=x+sqrt(1+x²) is at least one. Integer square/fourth-root floors with a one-grid-unit upper enlargement enclose the roots. The literal theta terms are positive. For k>=8 the bound `40 k^4 Y^(9/4) exp(-3k²Y)` follows from pi>3 and pi²<10; its ratio is below one half. The displayed first-tail bound therefore contains every omitted term. The Bessel I series has a decreasing positive remainder ratio after index 180, and the full geometric remainder is included. Every actual source weight is enclosed and checked positive.

The order recurrence uses v=nu/a, so substituting its even powers into the scaled energy variable E/R introduces exactly `(R/a²)^j`. The common positive normalization changes neither impedance nor zeros. The exact normalized c0 is one; using interval quotients for the other coefficients is a safe outward enclosure even though those quotients share c0.

The derivative used in the residue test is with respect to the scaled variable z=E/R. Thus the factor R in `-R*A/Bp` is necessary and correct.

## Polynomial certificate implementation

I independently checked `p_even(z)²-z*p_odd(z)²=p(sqrt(z))*p(-sqrt(z))`. It squares the roots with multiplicity and preserves the count inside the unit circle. Positive scalar normalizations at each step do not affect that count. The strict coefficient-dominance test uses a lower absolute bound for the selected coefficient and upper absolute bounds for every other coefficient, so Rouché applies to the actual polynomial throughout the interval enclosure.

The subsequent real scan is used to obtain brackets, not as a complex completeness argument. The root count supplies completeness. Ordinary bisection preserves each bracket. When a midpoint sign is unresolved, the interval mean-value enclosure `mid-B(mid)/B'(interval)` still contains the already established root; the code rejects an unresolved derivative or inadequate contraction. The final entire-interval numerator/derivative enclosure gives the residue sign, rather than evaluating at an approximate root.

For the curved boundary I expanded `Im(A(e^(i theta))*conjugate(B(e^(i theta))))` independently. Pairing coefficient differences at separation d gives the stated Chebyshev U_(d-1) polynomial after division by sin theta, and the sign in `Im(-A/B)` is negative. The change x=2t-1, the power-to-Bernstein coefficient formula, and the de Casteljau left/right subdivision are correct. Every accepted leaf covers its whole subinterval; both children of every unresolved cell are retained. Thus positive lower Bernstein coefficients prove the entire interval, including endpoints, without an angular grid.

The saved results are consistent with the code: order 50 uses three Graeffe rounds, six poles, and one degree-24 Bernstein cell; order 100 uses five rounds, eight poles, and five degree-49 cells with maximum depth four.

## Rejection controls and review limit

Both controls test mathematical omissions. For `-z³/(z²+1/4)`, the exact outer sign polynomial is `x²+3/4>0`, but the full count finds two interior zeros and the real brackets cannot cover them. For `-z-(1/100)/(z-1/3)`, the outer sign is also negative, but the genuine residue is negative and is rejected. The independent replay reproduced both rejections exactly.

The review shares the author's interval backend and does not claim a second transcendental-arithmetic implementation. It is an independent mathematical/source review and replay by another AI agent. The unbounded cofinal local sign theorem, formal proof-assistant verification, and external human refereeing remain outside this evidence.
