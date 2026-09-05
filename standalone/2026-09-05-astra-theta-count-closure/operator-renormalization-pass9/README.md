# All-rank arithmetic tail control in the original metric

**RH and the full arithmetic sign remain UNPROVED.** Complete proposed
component proofs are supplied in PROOF.md. Independent review is required.
Base: PR #790 at c64a0ae131d60cce48bc0dcc73358f7a1a857a89.
All additions are confined to operator-renormalization-pass9/.

## What the completion attempt achieved

The preceding endpoint defect is handled at the OPERATOR level. Let

    K_l(s,t)=sqrt(pi/(s+t)) exp(-(s+t)/4-l^2/(4(s+t))),
    Delta_X=sum_(n<=X) Lambda(n)n^-1/2 K_(log n)
                       -int_1^X x^-1/2 K_(log x)dx.

The continuous term is subtracted exactly. In the ORIGINAL L2 metric,
Delta_X converges in trace norm to Delta, with

    ||Delta-Delta_X||_1 <= B_X ->0,
    B_X=16sqrt(log X)|E(X)|/X
        +100 int_(log X)^infinity sqrt(v)|E(exp v)|exp(-v)dv,
    E(x)=sum_(n<=x)Lambda(n)-x+1, X>=3.

The proof uses the classical quantitative PNT. It does not prove a new
PNT rate, and its imported constants are not numerically certified here.
The same B_X bounds every signed finite matrix, with NO rank or order
factor. The Gaussian contour estimate, including its trace-norm derivative,
is proved rather than inferred from a scalar bound.

An exact continuum tail has kernel

    C_>X(s,t)=pi erfc((log X-s-t)/(2sqrt(s+t))).

For compact integrable tests, the difference between the complete prime
tail and this continuum tail extends to a trace-class operator of norm at
most B_X. The continuum tail itself is unbounded on L2: its endpoint mode
must not be silently discarded.

## Arbitrary simultaneous limits now work AFTER correction

Define the trace-class arithmetic base

    B(s,t)=(1/(4pi))int_R [Omega(x)+1/(x^2+1/4)]
                                  exp(-(x^2+1/4)(s+t))dx

and Gamma_X^bal=B-Delta_X/(2pi). The complete unconditional explicit
formula identifies its trace-norm limit with the original Gamma_0.
Every finite source matrix is compiled from

    h_X(u)=[1/s+(1-X^(1-s))/(s-1)-log(pi)/2+psi(s/2)/2
                         -sum_(n<=X)Lambda(n)n^-s]/(2s-1),
    s=1/2+sqrt(u+1/4).

The s=1 quotient is removable; its value is log X. All prime powers are
retained. The compiler uses finite prime data and exact gamma data, with
the full tail paid by B_X, not set to zero.

For the parent's square-width projections Pi_r and ANY X_r->infinity,

    Pi_r Gamma_(X_r)^bal Pi_r -> P_(1/2) Gamma_0 P_(1/2)

in trace norm. There is no coupling condition between X_r and r.
The limit retains Gamma_1 and every hypothetical negative direction.
This is an approximation theorem, not positivity of those matrices.

## The final positivity shortcut fails on actual arithmetic

Already at X=2,

    Tr Gamma_2^bal=(2-gamma_E-log(2pi))/4 <0,

and the single test f(t)=exp(-2t) has the exact value

    <f,Gamma_2^bal f>
      =[17/4-gamma_E-log(4pi)-pi^2/8-3(log2)^2/4]/27
      < -13/3240.

The source uses the real prime 2 with its literal log weight. No synthetic
zero set or floating-point acceptance is used. The same cutoff has a
negative spectral-density interval and infinitely many negative directions,
even after a fixed thermal shift. This does not refute the full source
or rule out a different/cofinal positive approximation.

The remaining estimate is still an arithmetic lower bound for the balanced
finite form at arbitrary rank. Norm convergence, the positive limiting
trace, and exact endpoint subtraction do not establish that lower bound.
This pass closes the rank-uniform ARITHMETIC ERROR problem on the
nonescaping schedule, not the RH-bearing sign problem.

## Execution and review

Run `python verify.py --check result.json`, then the same with `python -O`.
Run `python test_rejections.py`, then the same with `python -O`.
Finally run `sha256sum -c SHA256SUMS`.

The checker tests finite rational algebra and constant certificates. It does
not machine-prove PNT, contour convergence, infinite trace bounds or RH.
See VALIDATION.md for executed counts and SOURCE_LOCK.json for references.
Priority review: the differentiated nuclear contour; Stieltjes boundary
sign; unbounded endpoint versus bounded remainder; continuum factors;
original-metric all-rank inequality; and the exact X=2 test.
