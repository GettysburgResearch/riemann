# Direct Möbius attack: exact two-moment completion and a critical-line formula

**PROPOSED COMPONENT PROOFS; independent review required. The sparse count
estimate, unbounded native positivity, and RH remain unproved.**

This continuation attacks the actual annular scalar, using exact integer
Dirichlet convolution rather than another spectral counting criterion.

For every integer Y>=2 the paper constructs a real Dirichlet polynomial p_Y
supported below 4Y such that

    p_Y[n]=mu(n) for n<Y;
    p_Y(1)=0; p_Y'(1)=1;
    |p_Y[n]|<20;
    sum |p_Y[n]|^2/n <130+log Y.

Its correction costs less than 129 beyond the unavoidable Möbius-prefix
coefficient norm. That norm has sharp leading order (log Y)/zeta(2).
All these bounds are unconditional and elementary; no PNT is used here.
The two corrections are distributed over whole paired blocks, rather than
concentrated at one very large endpoint coefficient.

The exact quadratic convolution identity gives a replacement for the native
Mangoldt coefficients through n<2Y^2, with

    L_Y(s)=-2 zeta'(s)p_Y(s)+zeta(s)zeta'(s)p_Y(s)^2.

It has no poles at zeta zeros. Its only pole is at one with residue exactly
one. With Y=ceil(2m), Mellin inversion therefore yields a legal unconditional
critical-line formula for the FULL original D(m). The complete absolute tail
above t=Y is O_epsilon(Y^(-1/2+epsilon)(1+log Y)^2), tending to zero for
0<epsilon<1/2. This is an analytic theorem with non-numerical classical
convexity constants, not a newly evaluated contour integral.

The integral on 0<=t<=Y is still signed and unestimated at RH strength.
An explicit homogeneous two-moment correction preserves the same Möbius
prefix, the same logarithmic coefficient norm order, and the exact native
answer, but forces a large low-frequency absolute majorant for at least
one of two fixed candidate representations. Thus the attempted universal
absolute-norm proof fails even with these exact source constraints.
This is not a counterexample to RH, nor a failure theorem for the distinguished
p_Y itself.

Read PROOF.md for all quantifiers and the exact stopping point. SOURCES.json
credits the classical quadratic Vaughan/Heath-Brown identity, the zeta
approximate functional equation, and the different #805 contour programme.
The finite checker uses rational formal prime-log polynomials and outward
144-bit elementary logarithms. It does NOT evaluate zeta, a contour, or a
failure count at unbounded scale.

Replay with the authenticated sparse-sign-bootstrap/PROOF.md sibling present:

    python -I -S -B verify.py --check result.json
    python -I -S -B -O verify.py --check result.json
    python -I -S -B test_rejections.py
    python -I -S -B -O test_rejections.py

The main, preceding research, review, canonical, formal and workflow sources
are unchanged. No external novelty, independent acceptance, formal proof,
new positive range or end-to-end RH proof is claimed.
