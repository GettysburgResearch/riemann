# Source polarization and the ambient-operator domain firewall

Status: PROPOSED proof-only companion. No additional computation.
Scope: the stated Fourier normalization and the literal completed-xi
logarithmic derivative. This note does not prove RH or replace E4.

## 1. Sign and factor in the source polarization

Let Phi be real, even and sufficiently rapidly decreasing that its bilateral
Fourier transform X(z)=integral_R Phi(a)exp(iza)da is entire and all following
integrals and integrations by parts converge locally uniformly. The actual
theta representation of centered xi has this property. Define

    B_X(z,w)=[X(z)X'(bar w)-X'(z)X(bar w)]/(z-bar w),
    A_Phi(a,b)=(1/2)integral_(|a+b|)^infinity
        xi Phi((xi-a+b)/2)Phi((xi+a-b)/2) dxi.

Here xi inside the last integral is a real integration variable, not the
Riemann xi function. The singularity of B on z=bar w is removable and its
value there is X'(z)^2-X(z)X''(z).

Put s=a+b,d=a-b. The product of the two Phi factors is even in xi, so
integrating xi times that product from s to infinity gives the same value
as integrating from |s|. Differentiation consequently gives

    (partial_a+partial_b)A_Phi=-(a+b)Phi(a)Phi(b).

Integrate this identity by parts against exp(iza-i bar w b). Directly
expanding the numerator of B using the Fourier integrals then proves

    B_X(z,w)=integral_R2 A_Phi(a,b)exp(iza-i bar w b) da db.

There is no missing factor2 or extra minus sign with these conventions.
If Y(x)=X(ix) and F=Y'/Y, with X even and real entire, substitution yields

    B_X(ix,iy)=Y(x)Y(y)[F(x)+F(y)]/(x+y).

Pointwise positivity of A_Phi, when Phi>=0, is not positive definiteness
as an integral kernel. It supplies positive entries on the safe imaginary
axis, not the sign of arbitrary signed packet quadratic forms.

## 2. The algebraic exponential operator is dense

Now set Y(x)=xi(1/2+x) and F=Y'/Y, and use the complex Hilbert space
L2(0,infinity). Let D be the linear span of e_x(t)=exp(-xt) for real x>1/2.
Distinct exponentials are linearly independent, so

    T e_x=F(x)e_x

defines a linear operator on D. Euler nonvanishing makes F(x) finite and
real on this axis. D is dense: if h is orthogonal to every e_x, its Laplace
transform, holomorphic on Re z>0, vanishes on the interval x>1/2; the identity
theorem and Fourier uniqueness on any vertical line give h=0.

For g=sum c_i e_(x_i),

    2 Re<Tg,g>=sum_(i,j)c_i conjugate(c_j)
                    [F(x_i)+F(x_j)]/(x_i+x_j).

The finite-dimensional construction in E4 is therefore valid without any
assumption about the closure of T on the ambient Hilbert space.

## 3. A forbidden zero obstructs closability itself

Suppose Y has a zero a with Re a>0. Its logarithmic derivative F has a
simple pole at a with nonzero residue, regardless of the zero multiplicity.
For h in Dom(T*), there is k in L2 such that <T e_x,h>=<e_x,k> for all
real x>1/2. Since F is real there, conjugating the inner-product identity gives

    F(x) Lh(x)=Lk(x).

Both Laplace transforms are holomorphic in Re z>0. Meromorphic continuation
and the identity theorem give F(z)Lh(z)=Lk(z) throughout that half-plane.
At the pole a this forces Lh(a)=0. Evaluation h->Lh(a) is a nonzero bounded
linear functional, of norm(2Re a)^(-1/2). Therefore

    Dom(T*) subset ker[h->Lh(a)]

is not dense. The standard graph criterion for densely defined operators
then implies that T is not closable.

Because Y is even and real entire, an off-imaginary zero supplies a zero in
Re a>0. Consequently closability of this algebraic T already implies RH.
Assuming a closed functional-calculus realization F(-d/dt) at the outset
would therefore assume a load-bearing zero-location condition.

## 4. Converse and exact boundary

Under RH, the even genus-one canonical product gives

    F(x)=sum_(gamma>0) 2m_gamma x/(x^2+gamma^2),

where the positive imaginary zeros of Y are i gamma and their multiplicities
are retained. Local convergence follows from sum m_gamma/gamma^2<infinity.
Each summand contributes the positive kernel

    2m_gamma (xy+gamma^2)/[(x^2+gamma^2)(y^2+gamma^2)].

Thus T is accretive on D. Every densely defined accretive linear operator
is closable: if g_j->0 and Tg_j->v, compare accretivity of g_j-epsilon h
with fixed h in D, pass to the limit, and then let real epsilon tend to0
from both signs. Re<v,h>=0; replacing h by ih gives <v,h>=0, hence v=0
by density.

Therefore, for this particular literal algebraic operator,

    RH  iff T is accretive  iff T is closable.

This is an equivalence/domain warning, not a proof of any of these open
properties. In contrast, E4 and its growing-order sequel prove accretivity
on specified finite invariant subspaces without assuming an ambient closure.

The normalization boundary is PR765 at
8f01064df805624c045877655893c324a220975d; the reduced-companion index boundary
is PR783 at9497db89e34669e2167c632c918c491bf6ee73ab. The latter counts distinct
upper-half-plane zero locations for its different companion kernel, not
raw multiplicity. Nothing in this note reverses that cancellation result.

