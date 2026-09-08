# Higher-prime-power continuation of PR #792

Status: **PROPOSED complete analytic proof drafts; independent review required.
The requested all-epsilon inequality and RH are NOT proved.**
Scope: the actual prime-power source at the parent's fixed scale v=2, all degrees.
Exact parent: `a895f734fc4243dbe81e1a0c5a17cf978a744962`.
What was run: 1,192 exact finite controls in each interpreter mode, parent replays,
and ten corruption refusals; details in VALIDATION.md and REPLAY_LOG.json.
Smallest remaining gap: subexponential growth of the prime-only Pcal_N below.

## Main proved-in-draft result

For the actual higher-prime-power sum

    Q_N = sum_p sum_(r>=2) (log p)/p^(2r) L_N^(-1)(3r log p),

PROOF.md gives a complete argument that

    Q_N = (2/3)(-1)^N + q_N,       q in l^2(N>=1),
    ||q||_2 <= K+C3,
    K^2 = 6 integral_1^infinity |theta(x)-x|^2 dx/x^3 < infinity,
    C3 = sum_p (log p)p^(-3/2)/(1-p^(-1/2)) < 20.

Thus the ENTIRE infinite higher-power contribution is uniformly bounded and
has the indicated alternating main term with o(1) error. No decay rate or
numerical value for K is claimed. The square part uses the classical PNT;
cubes and above are controlled without a prime-distribution theorem.

The reusable atom identity is

    <x^(-s(w)), y^(-s(w))>_(H^2) = min(x,y)/max(x,y)^2,
    s(w)=(2-w)/(1+w).

Removing the constant coefficient yields an exact positive integral kernel
and a cross-term-preserving finite-source norm formula. The proof does not
use zeta zeros to build these atoms or their Hilbert space.

## Exact return and the failed extension

With

    Pcal_N = (-1)^N sum_p (log p)/p^2 L_N^(-1)(3 log p)
                 -3*2^(N-1)+2/3,

all higher powers and all archimedean coefficients are paid in the identity

    d_N = -(3/8)Pcal_N + r_N,          r in l^2.

The parent's original c_N(2) is obtained from d_j, j<=N, at cost at most
(8/9)sqrt(2N+1). The remaining bound on Pcal_N is OPEN and RH-equivalent.

The attempted stronger extension to l^2 is FALSE: actual critical-line zeros
force both d and Pcal to have infinite squared coefficient sum. Even the
square-bias-corrected source has

    integral_1^infinity |theta(x)-x+sqrt(x)|^2 dx/x^2 = infinity.

These obstructions are compatible with bounded coefficients under RH. They
identify the wrong proof norm, not a failure of the original conjecture.

Do not independently replace every power by its continuum integral starting
at one: those continuum moments have a divergent sum over exponents. The
proof subtracts only the square main term, keeping the other powers intact.

## Reading, replay, and scope

Read PROOF.md Sections 2 and 3 for the main theorem, Section 5 for the exact
return, and Section 6 for the full-source H^2 obstruction.

From this directory:

    python verify_exact.py --check result.json
    python -O verify_exact.py --check result.json
    sha256sum -c SHA256SUMS

The checker authenticates four pinned parent blobs and verifies finite
Laguerre, source-integral, kernel, norm, sign, endpoint and pole-residue
algebra. Rational-weight and continuous-source controls are NOT actual prime
data. The checker does not certify PNT, infinite norms, analytic boundary
behavior, or the open prime cancellation.

No main, predecessor, canonical or formal file is changed. The twelve files
of the predecessor remain unchanged. No independent referee, Lean build,
actual prime sweep, zero verification, or remote CI success is claimed.
The repository was resolved by its stable ID 1309150028 after transfer from
`gfreund123/riemann` to `GettysburgResearch/riemann`; historical source URLs
and frozen predecessor bytes are left intact.
