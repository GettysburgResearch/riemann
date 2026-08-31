# Independent audit: positive-source real-zero firewall

Verdict: PASS for frozen science dd498bdc20bdd658d34d0a56d7d22f3c5182b569.
No scientific or metadata repair is required. The acceptance is for a
synthetic positive-source countercontrol, not the actual modular theta
source, an RH/GRH counterexample, or a new automorphic object.

Parent SC: b0e3b18e690accdee6d77b3b3c4c68850f6cb671.
Pre-computation design: 67f88c148bb5914897cc13b6cbce61960a277cd1.
This non-author audit was performed in a separate worktree based on the
exact science SHA. There was no proof-acceptance coordination with the
author, no frozen-source modification, and no push.

## Read and authenticated scope

The complete ZF proof, producer, tests, fixture and manifest were read.
The complete frozen SC note, including its corrected local-integrability
boundary and the completed-observation formula SC9, and the complete
preregistration were read. All six direct source bindings, including the
other four SC artifacts, were authenticated as literal Git blobs and
LF-normalized SHA256 identities. The auxiliary SC finite matrix suite
is not silently counted as independently rerun here.

The source actually needed by ZF is the bounded scalar source class and
SC9, not tensor closure of arbitrary locally L1 fields. The scalar Mellin
formula below was also independently derived, so the acceptance does not
hide an unpaid tensor or averaging premise. Sections1--3 of the frozen
ZF design are retained exactly after the final header change.

## 1. Literal source, completion and real-zero count

For t<1 the vacuum excess is (t^-1-1)/2 and the reflected upper
compact excess is t^-1 C_A(1/t). Direct integration therefore gives

    integral_0^1 (t^-1-1)t^(s-1)/2 dt = 1/[2s(s-1)],

and substituting u=1/t in the other term produces the upper-side
integral with weights t^(s-1)+t^-s. This independently pays the factor2,
the signs, the fixed vacuum1, and residues -1/2,+1/2 at0,1.

Multiplication by s(s-1) gives exactly

    Z_A(s)=1/2+A[1+(s-1)e^(bs)-s e^(b(1-s))].

The endpoints are1/2, reflection is s->1-s, and the apparent exponential
quotient singularities are removable. All interior zeros under discussion
are genuine zeros of L_A because s(s-1) is nonzero there. Positive-source
Gram positivity applies to L_A(z+conjugate(w)) for Re z,Re w>1/2:
its quadratic sum is the positive integral of
|sum_j c_j t^(conjugate(z_j))|^2 against C_A(t)dt/t.
This is not a Herglotz assertion about continuation into the critical strip.

The proof's ZF1--ZF3, at frozen lines117--127, are valid throughout
0<b<=sqrt8. For real0<z<1/2, the probability weight proportional to
e^(x/2)cosh(zx) on[0,b] gives

    J'(z)/J(z) = average[x tanh(zx)] < z b^2.
    Phi'(z) < z J(z)[-2+b^2(1/4-z^2)] < 0.

Strictness holds on a positive-measure subset, not just at an endpoint.
At b^2=8 the final bracket is -8z^2<0; this endpoint is not lost.
The central and endpoint values then give exactly the stated two/zero
real-zero alternatives. For |z|>1/2, J(z)>0 and Phi(z)<0, hence Z_A>1/2.
The derivative is nonzero at either supercritical zero, proving simplicity.

## 2. Threshold and local complex pair

The quadratic coefficient requires its own check; the preceding
monotonicity upper bound alone does not decide central multiplicity.
Independent triangular integration of P'+P/2=x^2 gives

    J2=e^(b/2)(2b^2-8b+16)-16,
    c_b=2J0-J2/4 = b(4-b)e^(b/2)/2.

This agrees with ZF4 and is strictly positive for the entire stated range,
including b=sqrt8. Direct expansion of the exponential polynomial gives
the same z^2 coefficient A c_b; all odd coefficients vanish.
Consequently the threshold zero is exactly double, not higher order.

The series defining J_tilde(u) is entire: its coefficients are bounded
by J0 b^(2n)/(2n)!. At (A_c,0), F_u=A_c c_b is nonzero and F_A=-J0/2.
Thus the analytic implicit-function theorem has its hypotheses paid.
Its slope independently simplifies to

    u'(A_c)=J0^2/(2c_b)
            =4(e^(b/2)-1)^2/[b(4-b)e^(b/2)] > 0.

At b=1 this is the published4(E-1)^2/(3E), with c_b=3E/2.
The analytic nonvanishing factor after division by u-u(A) establishes
the local multiplicity statement. Reality and uniqueness make u(A) real
for real A. Therefore below threshold the nearby simple pair is vertical
through1/2; above threshold it is the real off-central pair. This does not
enumerate other complex zeros or enlarge the permitted b range.

## 3. Globally smooth strict source and persistence

The construction at frozen lines185--244 pays the global source conditions.
Both cutoffs can be chosen even and flat where they become constant.
The absolute value therefore causes no nonsmoothness at0. For x>=0,

    1 <= v_epsilon(x)/e^(x/2) <= e^(epsilon/2),

with a difference supported on[0,2epsilon]. The transition near b lies
in[b-epsilon,b+epsilon], disjoint from that origin region because
epsilon<b/4. The strictly positive e^(-2cosh x) summand makes
h_epsilon>e^(|x|/2) everywhere. Evenness pays the exact reciprocity;
multiplication by t^-1/2 then gives H_epsilon>1 for every finite t>0.
The upper tail of C_epsilon is exactly the stated
epsilon t^-1/2 exp[-(t+t^-1)]/2, with the same vacuum1.

Here is an independent quantitative decomposition of ZF10. On the upper
side, the origin change has height at most
(1+2A)(e^(epsilon/2)-1)/2 on a log-interval of length2epsilon, so its
weighted integral is O(epsilon^2). The edge change has height at most A
on a log-interval of length2epsilon, so contributes O(epsilon).
The additional smooth tail contributes at most

    epsilon/2 * integral_1^infinity
       (t^(M-1/2)+t^(-M-1/2))e^(-t) dt,

which is finite for every fixed M>0. All compact-region Jacobians and
weights are bounded by constants depending only on the fixed A,b,M.
Thus the required weighted L1 convergence is genuinely O(epsilon),
not an inference from pointwise convergence.

For any fixed compact s-set, choose M>1+max|Re s|. The two Mellin weights
and the bounded factor s(s-1) are dominated by this weighted norm.
The common vacuum terms cancel, yielding uniform convergence of the
entire pole-cleared functions. Choose equal-radius reflected disks about
the original simple real pair, small enough to be disjoint and off the
central line, containing no other zero and having zero-free boundaries.
The positive boundary minimum then pays the strict Rouché inequality.
Exactly one zero counting multiplicity in each conjugation-invariant
disk forces that zero to be real and simple. Reflection pairs the two.

[Rouché's theorem in DLMF1.10(iv)](https://dlmf.nist.gov/1.10#iv) was checked
directly; its analytic-domain and strict-boundary hypotheses are met.
The smooth conclusion is existence and persistence of this pair only.
No complete real/complex zero census or effective epsilon threshold is
smuggled into the claim.

## 4. Independent finite reconstruction and adversarial replay

The adjacent independent script reads the exact frozen fixture and uses
a reverse Horner Taylor polynomial, not the producer's forward recurrence.
A separate triangular antiderivative elimination and a direct exponential
z-expansion check the central constants independently.

- All six rational exponential enclosures, all nine sign enclosures,
  the threshold interval, and all nine margins match exactly.
- The sign rows are +++,+--,---. The A=1 candidate succeeds; the A=2
  candidate fails exactly as preregistered. No panel is moved or dropped.
- 512 additional exact Horner/factorial and higher-tail comparisons use
  orders1--32 and x=j/16,1<=j<=16. They are bounded auxiliary controls,
  not substitutes for the analytic continuum proof.
- 32 fresh, unmocked, fully payload-resealed fixture mutations are rejected
  in both modes. Each rejection runs the producer's real source/primitive
  reconstruction. Twenty additional primitive type/cap guards also reject.

The producer's complete canonical fresh comparison at lines471--478
retains bool/int distinction and rejects semantic changes even after
resealing. Bounds on order, integer bits, polynomial sizes, work, JSON
bytes/nodes/depth/container/string lengths remain explicit under -O.
The finite controls do not evaluate any smooth-source integral or prove
the implicit/Rouché theorem by numerical sampling.

## 5. Validation and frozen identities

The original28 tests pass normally in9.159s and under -O in8.932s.
Both producer checks pass; both fixture and source-manifest emits are
LF-byte-exact in each mode (four comparisons). Original-source Ruff
lint/format and full SC-base-to-science whitespace checks pass.

Six source Git/LF identities and four artifact identities independently
match, and the fixture payload seal recomputes exactly:

    science fixture LF SHA256:
    3987133d0fd7e71fcf17d05675ce9a10d3edfb0a906714eb6e13c997cc3e0dfc
    science payload SHA256:
    7acae9c2697842a4dbfd4e5bb229ecec3f7ddaff9fbb8825f277614a5faa7007

The independent review report is replayed with:

    python -B research/l-families/atlas/generalized/theta_positive_source_independent_audit_dd498bdc.py --check
    python -B -O research/l-families/atlas/generalized/theta_positive_source_independent_audit_dd498bdc.py --check

The review branch adds only this audit, its independent script, and report.
It does not alter the five scientific files. The acceptance closes this
synthetic positive-source firewall, not native MP zero placement, RH,
a new arithmetic realization, or any global complex-zero classification.
