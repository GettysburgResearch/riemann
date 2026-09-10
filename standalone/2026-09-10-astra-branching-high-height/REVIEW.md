# Independent-review handoff

Status: PROPOSED component mathematics, not an RH submission with a hidden gap.
Primary freeze: PR #857, 3f1984867d23b588d09c88a892882411724b174b.

## Load-bearing analytic checks

1. Equation (11) differentiates each independent child d times. Verify the
   b^-d(1-b)^-d factors and the beta change from a to p=a-d>1. Check that the
   normalized measure includes EVERY off-diagonal atom pair and density term.
2. Verify the beta-density maximum/variation bound, inverse-beta moment,
   scaled-density BV norm, and the explicit G,W bounds in (13). All BV norms
   concern zero extensions, including boundary jumps.
3. Equations (14)–(18): retain the common uniform scale, both endpoints t/4,t,
   the factor TWO in the chosen normalization, the continuous term and its
   variation. The signed recurrence is not a probability-weight recursion.
4. Verify the normalization of (22), including derivative order 2^n-1 and
   knot weights 4^(j d_n). Then check the factor-four coefficient growth and
   the elementary Enestrom–Kakeya proof, including n=0.
5. Equation (27) tests against x^(p+2d) on the complete positive support.
   Confirm the falling/rising factorial, the even derivative sign and that
   all mixed terms remain in the integral R_n. Do not identify P_n with M_n.
6. Check logarithmic-coordinate BV variation for both R_n and R_n', all
   factors of two between p=s/2 and s, the reciprocal-gamma factors, and
   the nonzero guard BEFORE dividing in (33).
7. The threshold uses rational majorants, then only pi>3 and log2>2/3. Verify
   (35)–(36) uniformly in 0<=Re(s)<=1. Simplicity uses a nonzero raw M_n and
   strictly increasing line phase, not an assumption of simple xi zeros.
8. The unwrapped leading-polynomial phase in (37) is -n t log2. Check its
   bounded residual argument; the count is for each fixed finite depth.

## Dependency and quantifier boundaries

The elementary finite-depth factorization is rederived. The locally uniform
entire convergence to xi is imported from the proposed parent proof only for
the conditional RH discussion. It is not needed for eventual confinement of
the explicitly defined finite iterates. Neither the parent's phase certificate
nor any external zero census is a computational input here.

The new theorem says forall n exists T_n with control above T_n. It does NOT
say there exists one T that works for all n, or that control below T_n grows
with n. No all-depth elimination of the finite exceptions is supplied.
Independent review should accept or reject the supplied proof, not provide
that absent source-specific confinement theorem.

## Finite tests to inspect

The checker independently obtains derivative atoms via scaling/normalization,
and compares uniform beta-pair moments with a full signed derivative measure.
The scale test includes both atoms and the continuous term. These are useful
sign/normalization controls, not a formal proof for arbitrary BV densities.
The same author wrote the derivation and checker; no second referee or
independently implemented interval backend is asserted.

The tests mutate primitive formulas as well as result data, resealing hashes
before selected rejections. This shows that specified corruptions are caught.
It is not protection against replacing the complete proof/checker/manifest
with an arbitrary internally consistent malicious package.
