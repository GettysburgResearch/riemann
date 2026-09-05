# Prime diagonal, complete signed energy, and the boundary-norm test

Status: PROPOSED analytic proofs; independent mathematical review required.
Scope: actual prime-only coefficients at the parent's fixed scale; all degrees.
Parent: PR #792, 3b1bb5b81b36f742b6d5840088bf79a8e1519084.
What was run: 1,192 NEW exact finite controls in each interpreter mode, all
three unchanged predecessor checkers, and twelve intended corruption refusals.
Smallest remaining gap: the actual-source polynomial energy comparison below.
**The requested subexponential inequality and RH remain unproved.**

## Main new arithmetic result

For F_n=L_n^(-1), the literal prime diagonal obeys

    Delta_n=sum_p (log p)^2 p^-4 F_n(3log p)^2
           =(2/3)n+O(sqrt(n)log(n+2)).

The proof is uniform in degree and uses only ordinary Laguerre identities
and the classical quantitative PNT. Its core is a low/high variation bound,
not a large-degree numerical extrapolation. The infinite prime sums were
not evaluated by the finite checker.

## Signed energy and the actual missing inequality

Retain the parent's prime-only coefficients

    Pcal_n=(-1)^n sum_p (log p)p^-2 F_n(3log p)-3*2^(n-1)+2/3.

Set E_N=sum_(n<=N) n|Pcal_n|^2 and D_N=sum_(n<=N) n Delta_n. Then

    D_N~(2/9)N^3.

The complete E_N has an exact two-variable Christoffel--Darboux formula
against dtheta-dx+dx/(2sqrt(x)), retaining ALL signed cross terms.
A comparison E_N<=C N^A D_N for any fixed A would prove RH. It is NOT
proved. Under RH, E_N/N^2 has an explicit positive limit retaining squared
multiplicities. These conditional conclusions are not additional RH progress.

The generic arbitrary-coefficient comparison has an exponential dimension
cost on exponentially many prime nodes. More sharply, a positive perturbation
of the weights on the SAME ordinary primes preserves their PNT error class
and the diagonal asymptotic but forces exponential coefficient growth. It is
not actual zeta and does not preserve the original completed Euler data.

## Complete boundary-norm classification

For the actual meromorphic continuation D(w)=d_0/2+(3/8)xi'/xi(s(w)) and
the prime-only continuation, the supremum of radial p-means is finite for
EVERY 0<p<1 and infinite for EVERY p>=1, unconditionally. Thus changing
only this exponent does not solve the problem. In particular finite
meromorphic radial p-means must not be called analytic H^p membership.

A weighted area norm with weight 1-|w|^2 admits genuine boundary poles and
excludes interior poles. Its finiteness is RH-equivalent, with an explicit
local logarithmic divergence coefficient at an off-line zero. This correct
replacement norm is identified, but its arithmetic finiteness is not proved.

## Reading and replay

Read PROOF.md first (PE-1 through PE-4), then BOUNDARY.md (BR-1 and BR-2).
VALIDATION.md separates mathematical arguments from executed finite controls.
The local labels are not canonical theorem registry IDs.

From this directory, with the parent files present:

    python verify_exact.py --check result.json
    python -O verify_exact.py --check result.json
    sha256sum -c SHA256SUMS

No finite prime/zero sweep, actual-zeta derivative computation, Lean build,
independent referee review, or remote CI success is claimed. Classical inputs
are credited and external novelty is not claimed. All twenty predecessor
files are retained unchanged; this is an add-only continuation of the same PR.
