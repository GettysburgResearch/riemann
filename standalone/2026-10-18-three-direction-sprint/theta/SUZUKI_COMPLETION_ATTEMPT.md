# A source-faithful Suzuki attempt at the 5/6 boundary

**Status: exact arithmetic adapter and an unsuccessful completion attempt.
No improved zero-free region is proved.** The inner-function and eventual
sign criteria are imported classical results of Masatoshi Suzuki, not new
criteria here. The new work below reconstructs the literal ordinary-zeta
kernel, subtracts its exact unit term before any estimate, and identifies
the centered Mobius source which remains to be controlled.

Primary sources actually read: Suzuki,
[A canonical system of differential equations arising from the Riemann
zeta-function, arXiv:1204.1827v2](https://arxiv.org/pdf/1204.1827),
Sections1--2 and Appendix A, especially Proposition1.2 and Theorem A.1;
and [On monotonicity of certain weighted summatory functions associated
with L-functions, arXiv:1204.1823](https://arxiv.org/pdf/1204.1823),
Theorem2.1 and its proof. Normalizations below use
`xi(s)=s(s-1)pi^(-s/2)Gamma(s/2)zeta(s)/2`.

## 1. The actual ordinary-zeta gate

Fix `0<omega<1/2`. Put

    c_omega(n)=n^omega sum_(d|n) mu(d)d^(-2omega)
              =n^omega product_(p|n)(1-p^(-2omega))>0.

For `0<t<1` define

    C=2pi^omega/Gamma(omega),
    I(t)=integral_(t^2)^1 u^(1/2-omega)(1-u)^(omega-1)du,
    g(t)=C[t^(2-omega)(1-t^2)^(omega-1)
                         -omega t^(omega-1)I(t)],
    g1(t)=t^(-1/2)integral_t^1 u^(-1/2)g(u)du.          (1)

Set both kernels to zero above1 and use their continuous value `g1(1)=0`.
The full finite arithmetic sum is

    h1(x)=x^(-1)sum_(n<=x)c_omega(n)g1(n/x), x>=1.     (2)

There is no prime-only, squarefree-row, or truncated-product replacement
in (2). Although `c_omega` is positive, `g1` has a negative part.

Suzuki proves that eventual one-sign behavior of (2) makes

    Theta_omega(z)=xi(1/2-omega-iz)/xi(1/2+omega-iz)

inner in the upper half-plane. A sufficient ordinary-zeta target for
`Re rho<=5/6` is eventual one-sign behavior for **every**
`omega in (1/3,1/2)`. The threshold beyond which the sign holds may depend
on omega. The same statement with omega in every `(omega0,1/2)` gives
the boundary `1/2+omega0`.

The interval quantifier is load bearing. At one fixed omega, a denominator
zero can cancel with a numerator zero separated horizontally by
`2omega`. Fixed-omega innerness alone is not asserted to retain every
zeta zero. Suzuki's proof using all omega, or equivalently choosing an
omega avoiding the finitely many relevant zero separations in a bounded
height rectangle, resolves this common-zero issue.

## 2. Exact unit-centered Mobius source

For `y>=1` write

    f(t)=t^omega g1(t),
    R(y)=sum_(m<=y) f(m/y),
    K(y)=y^(2omega-1)R(y),
    q=omega+1/2,
    K0(y)=y^(omega-1/2)sum_(m<=y)m^(-q),
    L(y)=K(y)-K0(y).                                  (3)

All sums use the ordinary full integer prefix. Then, exactly,

    h1(x)=x^(-1/2)
                 +x^(-omega)sum_(d<=x)mu(d)/d L(x/d). (4)

**Proof.** Expanding the divisor sum in (2), with `n=dm`, gives

    h1(x)=x^(omega-1)sum_(d<=x)mu(d)d^(-2omega)R(x/d)
          =x^(-omega)sum_(d<=x)mu(d)/d K(x/d).

On the other hand,

    sum_(d<=x)mu(d)/d K0(x/d)
      =x^(omega-1/2)sum_(dm<=x)mu(d)(dm)^(-q)
      =x^(omega-1/2),

because the divisor sum of mu is the unit mass at1. This proves (4).
In particular the positive unit term was obtained by finite algebra,
not by assigning a value to a divergent reciprocal Dirichlet series.

## 3. The archimedean cancellation and the exact tail constant

The main continuous Riemann-sum term is zero:

    integral_0^1 f(t)dt=0.                              (5)

Indeed direct differentiation in (1) gives

    t^omega g(t)=-(C/2)d[t^(2omega)I(t)]/dt.

Its integral vanishes at both endpoints. Fubini in the definition of
g1 then gives `integral f=(omega+1/2)^(-1)integral t^omega g(t)dt=0`.
Absolute integrability holds: the worst small-t power in f is
`t^(2omega-1)`, with exponent greater than-1.

There is nevertheless a nonzero discrete tail. Let

    p=(3-2omega)/2,  r=(5-2omega)/4,
    D=4omega pi^omega/[(2omega-1)Gamma(omega)],
    a=D Beta(p,omega),
    b=-D(2omega+1)/(4omega) Beta(r,omega).

Elementary integration of (1) gives

    f(t)=D[t^(2omega-1)Beta_(t^2,1)(p,omega)
       -(2omega+1)/(4omega)t^(omega-1/2)
                                      Beta_(t^2,1)(r,omega)].

Consequently

    f(t)=a t^(2omega-1)+b t^(omega-1/2)+O(t^2)          (6)

at0. After these two singular powers are subtracted, the remainder is
of bounded variation on[0,1]. At1, g1 is O((1-t)^omega), and its
derivative is integrable. For `-1<alpha<0`, ordinary Euler summation gives

    sum_(m<=y)(m/y)^alpha
        =y/(alpha+1)+zeta(-alpha)y^(-alpha)+O(1).

For the bounded-variation remainder the Riemann-sum error is O(1).
Combining this with (5)--(6), uniformly for real `y>=1`, gives

    K(y)=a zeta(1-2omega)
           +b zeta(1/2-omega)y^(omega-1/2)
           +O(y^(2omega-1)).                           (7)

Gamma recurrence and the zeta functional equation simplify BOTH constants:

    a zeta(1-2omega)=4xi(2omega)/(1-2omega),
    b zeta(1/2-omega)=zeta(1/2+omega).                  (8)

Also Euler summation applied to K0 gives

    K0(y)=1/(1/2-omega)
             +zeta(1/2+omega)y^(omega-1/2)+O(y^(-1)).

Thus the slow second term in (7) cancels exactly in the unit-centered
kernel:

    L(y)=d_omega+O(y^(2omega-1)),
    d_omega=4[xi(2omega)-1/2]/(1-2omega)<0.             (9)

The strict sign uses the actual positive even theta density. Its
bilateral Laplace transform is xi, is symmetric about1/2, and is strictly
increasing with `|s-1/2|` on real s. Therefore
`xi(2omega)<xi(0)=1/2` for `0<2omega<1`.
For orientation, an ordinary double-precision evaluation at omega=1/3
gives approximately `d_omega=-0.030720861`; this decimal is not used in
any proof or certificate.

The small constant in (9) is an actual modular/theta cancellation. It
does not change the power of an uncontrolled Mobius fluctuation. Also L
is not smooth across the integer points: K is continuous there, whereas
K0 has an upward jump of exactly1/y at an integer y. Estimates involving
the absolute variation of L must retain these jumps.

## 4. Exact Mellin multiplier and the retained zero obstruction

Put

    A_omega(v)=[(v-omega)(v-omega-1)
                     /((v+omega)(v+omega-1))]
               pi^omega Gamma((v-omega)/2)/Gamma((v+omega)/2).

Beta integration, first in its absolute half-plane, yields

    integral_0^1 g(t)t^(v-1)dt=A_omega(v),
    integral_0^1 g1(t)t^(v-1)dt=A_omega(v)/(v-1/2).

Summing over m, initially `Re s>2omega`, and then continuing to
`Re s>0` using (7), gives

    integral_1^infty L(y)y^(-s)dy/y
       =zeta(s+1)/(s+1/2-omega)
          [xi(s+1-2omega)/xi(s+1)-1].                 (10)

For Re s>0 this is an ordinary absolutely convergent integral. The
apparent zeta-zero denominator on the right cancels against its outside
zeta factor; L itself is an explicit plain-integer archimedean kernel.
Its constant tail (9) corresponds to the pole `d_omega/s` at0.

Convolving L with the **actual** mu(d)/d in (4) removes that outside
zeta factor. The resulting multiplier is

    [xi(s+1-2omega)/xi(s+1)-1]/(s+1/2-omega).          (11)

Thus a hypothetical zero rho of xi still gives a pole at `s=rho-1`,
unless the numerator has the matching zero `rho-2omega`. The family
quantifier in Section1 prevents treating these possible cancellations
as a zero detector valid at one fixed omega.

Formula (10) also explains a tempting but invalid completion. On
`Re s=omega-1/2`, the xi quotient in (11) has modulus1 by the functional
equation, wherever it is defined. This boundary modulus is automatic.
It does not prove that the causal arithmetic kernel obtained from the
high absolute line belongs to the corresponding Hardy/L2 class:
moving the contour can cross precisely the poles under investigation.
Suzuki's Theorem A.1 distinguishes actual kernel membership from this
formal boundary calculation.

## 5. What the completion attempt did and did not achieve

The actual all-order task can now be stated without a general number
field, a general coefficient vector, or a finite-moment surrogate:

    1+x^(1/2-omega)sum_(d<=x)mu(d)/d L_omega(x/d)

must eventually have one sign, for every omega in(1/3,1/2). The displayed
quantity is exactly sqrt(x)h1(x), not a model of it.

The beta smoothing removes the continuous main term, and the exact unit
centering removes its slow fractional tail. Neither step deletes the
centered Mobius source or its possible xi poles. Taking absolute values
of the divisor expansion loses the sign needed for this gate. Likewise
the negativity and small size of d_omega alone do not bound the whole
weighted fluctuation in (4).

No eventual sign, Hardy membership, or improved centered-Mobius power
estimate is proved here. This attempt therefore does not provide5/6 or
an improvement of the working ordinary-zeta boundary. Its useful output
is the literal finite source (4), the exact modular constants (8)--(9),
and the full multiplier (10)--(11), which identify the cancellation a
successful principal-only argument still has to establish.
