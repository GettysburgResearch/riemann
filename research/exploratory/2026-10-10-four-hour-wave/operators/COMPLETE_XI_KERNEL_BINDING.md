# Bind the literal arithmetic kernel to the complete Xi zero source

Status: new exact source-adapter derivation, submitted for independent
review. This proves an identity and an all-window equivalence; it does not
prove the required all-window sign. The full L=1 continuum lower run remains
pending, and no coefficient-trace criterion is inferred here.

The kernel is exactly O1.1 of the inherited
[OPERATOR_AUDIT.md](../../../../reviews/C/pass4-math-completion/proofs/OPERATOR_AUDIT.md).
Set b=3/2, c=1/2, lambda_j=2j+1/2 and

    C_b=(1-gamma_E-log(2*pi))/3,
    q_n=Lambda(n)/sqrt(n),
    P_2=sum_(n>=2) Lambda(n)/n^2=-zeta'(2)/zeta(2).

Thus, on the entire real line,

    W(x)=exp(c|x|)/2+C_b exp(-b|x|)
         +sum_(j>=1) exp(-lambda_j|x|)/(lambda_j^2-b^2)
         -(1/(2b))sum_(n>=2)q_n[exp(-b|x-log n|)+exp(-b|x+log n|)]. (X1)

Imported classical inputs are the completed-xi normalization
xi(s)=s(s-1)*pi^(-s/2)*Gamma(s/2)*zeta(s)/2, its functional symmetry,
entire order one and complete zero strip, Hadamard factorization after
passing from the even function to its squared variable, the digamma series
and special values, the Dirichlet logarithmic derivative in Re s>1, and
uniqueness of the Laplace transform for continuous functions of exponential
order. No zero location on the critical line is assumed.

## X2. Exact identity

Let rho range over **all** nontrivial zeta zeros with analytic multiplicity,
and write a_rho=rho-1/2. Then

    W(x)=sum_rho exp(a_rho*x)/(b^2-a_rho^2),  x in R.      (X2)

The sum is complete and converges absolutely and locally uniformly. It
is real and even by conjugation and the functional reflection. In particular
no pole factor or reflected member is omitted.

To prove this, define F(s)=xi(1/2+s), an even entire function of order one,
and L(s)=F'(s)/F(s). Its complete paired product has only a constant
exponential and gives

    L(s)=sum_{ {a,-a} } 2m_a*s/(s^2-a^2).                (X3)

There is no center zero: eta(1/2)>0 by grouping consecutive terms of
its alternating series, while 1-2^(1-1/2)<0; hence zeta(1/2)<0 and
F(0)>0. Passing from F(s) to its squared variable gives entire order
1/2, proving the stated constant-exponential genus-zero factorization.

The inverse-square zero sum is finite. Since |Re a|<1/2,

    Re(b^2-a^2)=b^2-(Re a)^2+(Im a)^2>2+(Im a)^2.

Consequently the sum in X2 is absolutely and locally uniformly convergent
and is bounded by a fixed constant times exp(|x|/2). Denote its sum by Z(x).
For real s>b, termwise Laplace integration and paired partial fractions give

    integral_0^infinity exp(-sx) Z(x) dx
       = [(s/b)L(b)-L(s)]/(s^2-b^2).                    (X4)

Indeed a complete opposite pair has integral
2m_a*s/[(s^2-a^2)(b^2-a^2)], which is exactly the same pair's contribution
to X4. The factor at s=b is removable.

## X3. The literal source has exactly that Laplace transform

All terms in X1 can be integrated absolutely at real s>b. For the prime
part, if d=log n, direct splitting at x=d gives

    integral_0^infinity exp(-sx)[exp(-b|x-d|)+exp(-b|x+d|)] dx
       =2[s exp(-bd)-b exp(-sd)]/(s^2-b^2).

Thus its complete transform is

    [-zeta'(s+1/2)/zeta(s+1/2)-(s/b)P_2]/(s^2-b^2).     (X5)

For the gamma part write A(s)=sum_(j>=1)
1/[(lambda_j^2-b^2)(s+lambda_j)]. Partial fractions in lambda_j use

    1/[(lambda^2-b^2)(lambda+s)]
      = 1/[2b(s+b)(lambda-b)]
        -1/[2b(s-b)(lambda+b)]
        +1/[(s^2-b^2)(lambda+s)].

The three coefficients sum to zero, so the digamma series applies without
an unspecified subtraction constant. Using
psi(1/2)=-gamma_E-2log2 and psi(2)=1-gamma_E gives

    A(s)=[-psi(5/4+s/2)/2
          +(1+2log2)s/6+1/4-gamma_E/2-log2/2]/(s^2-b^2).

Apply psi(5/4+s/2)=psi(1/4+s/2)+2/(s+1/2), and add the growing and C_b
terms. Exact algebra gives their complete numerator

    (s/b)[3/2-(log pi+gamma_E)/2]
      -1/(s-1/2)-1/(s+1/2)
      +(log pi)/2-psi(1/4+s/2)/2.                       (X6)

On the initial half-line s>b, the literal completed-xi logarithmic
derivative is

    L(s)=1/(s-1/2)+1/(s+1/2)
         -(log pi)/2+psi(1/4+s/2)/2
         +zeta'(s+1/2)/zeta(s+1/2),
    L(b)=3/2-(log pi+gamma_E)/2-P_2.                    (X7)

Equations X5--X7 show that the Laplace transform of W is exactly X4.
For uniqueness, W is continuous by the complete local source sums and
has at most exponential order b: the prime pair is bounded termwise by
2 exp(bx)n^(-b) for x>=0, whose q_n-weighted sum is 2 exp(bx)P_2; the
remaining terms have that growth bound as well. Laplace uniqueness gives
W=Z for x>=0, and evenness gives X2 on the full line.

## X4. Native quadratic form and the precise remaining all-window gate

For every fixed L>0 and native complex h in L2(0,L), X2 gives exactly

    q_L(h,h)
      =b sum_rho [ integral_0^L conjugate(h(t))*exp(a_rho*t) dt ]
                   [ integral_0^L h(u)*exp(-a_rho*u) du ]
                   /(b^2-a_rho^2).                    (X8)

Local absolute uniform convergence and L2 contained in L1 on the fixed
interval justify the exchange. This is the complete actual-xi source,
with its actual complex denominators and reflected members. Away from RH
these summands cannot be replaced by positive absolute squares.

If RH holds, a_rho=i*Im rho, and (X8) becomes a sum of nonnegative squared
Fourier moments divided by b^2+(Im rho)^2. Thus q_L is nonnegative for
every L>0.

Conversely suppose q_L is nonnegative for every native complex L2 test
and every L>0. Smooth approximate point masses, shifted together into an
interval (0,L), show that all finite matrices [W(t_i-t_j)] are positive
semidefinite. Continuity of W justifies the limit. Their two-point minors
give |W(x)|<=W(0), so W is bounded on R. Its one-sided Laplace transform
is then holomorphic on Re s>0. Equation X4 agrees there, by meromorphic
continuation, with that holomorphic function. A zero a of F with Re a>0
would give L(s) a simple pole of residue m_a, hence X4 a pole of nonzero
residue -m_a/(a^2-b^2). Neither a=b nor a=-b can be a zero by the complete
classical strip. Such a pole contradicts holomorphy. Functional symmetry
would reflect any zero with Re a<0 to one with Re a>0. Hence every a is
purely imaginary and RH follows.

Therefore the exact native criterion is

    RH iff q_L(h,h)>=0 for every L>0 and every h in L2(0,L). (X9)

A certificate for every 0<L<=1 is a proper bounded-window subset of this
criterion. It does not establish the all-window hypothesis of X9. This
binding also does not authenticate any separate global trace or
coefficient criterion from the predecessor corpus.
