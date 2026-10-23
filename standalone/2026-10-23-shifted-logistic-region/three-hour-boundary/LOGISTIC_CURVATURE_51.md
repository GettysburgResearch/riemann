# A sharp elementary curvature bound for the logistic kernel

2026-10-21. Independent check of the parent's autocorrelation identity
`../three-hour-root/LOGISTIC_KERNEL_AUTOCORRELATION.md`, SHA256
`26dca6795b0fc64f4030f0c271f3f8fdec43c5a796bdae12647e3afdac26ca43`.
The identity and its stated positivity consequences pass review.

Put k=tan(theta), d=theta/k, S=sec(theta)^2, and

    g(x)=S(cos(kx)-cos(theta))  if |x|<=d, and 0 otherwise.

This even continuous function is Lipschitz; its weak derivative is
-S*k*sin(kx) on (-d,d) and zero outside. In particular g' belongs to
L2 and has no endpoint delta terms. For w(v)=integral g(x)g(x+v)dx,
weak differentiation followed by integration by parts gives

    w''(v)=-integral g'(x)g'(x+v)dx.

The right side is continuous, by translation continuity in L2. Thus it
is the ordinary second derivative of the globally C2 correlation, also
outside its compact support. Cauchy--Schwarz proves the global bound

    ||w''||_infinity <= ||g'||_2^2
       = S^2*k*[theta-sin(2theta)/2].                  (C1)

The equality comes from integrating sin^2(kx) over [-d,d]. The bound
is attained in absolute value at v=0, so no mesh or extremum search
is involved. With theta=5669/5000, the companion exact Fraction
checker proves

    50 < S^2*k*[theta-sin(2theta)/2] < 51.              (C2)

It reuses the frozen rational sine/cosine enclosures from the
independently reviewed baseline scalar checker. All acceptance is
exact integer/Fraction arithmetic; the decimal 50.06970149... is only
an informational rendering.

Consequently, for every v>=0 including beyond the support,

    |w(v)-w(0)| <= (51/2)v^2.                          (C3)

Here w'(0)=0 by evenness and differentiability. In the three-transform
logistic lower reduction, each former error 1000 eta^3/b^3 can be
replaced by 51 eta^3/b^3. The integral of u^2 exp(-bu) is 2/b^3,
which cancels the factor 1/2 in (C3). In prime-power Taylor bounds,
the former coefficient 175 can similarly be replaced by 51/2.

This is an elementary bound on the same kernel. It changes no
explicit-formula, zero-count or prime-distribution premise. The old
certificates remain valid; any improved zero-free constant needs its
own full parameter certificate.
