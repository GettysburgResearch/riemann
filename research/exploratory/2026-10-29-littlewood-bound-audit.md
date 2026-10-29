# Littlewood bounds from a fixed Dirichlet zero-free half-plane

**Status:** An independent derivation of a classical conditional implication. Assume an external source gives the same fixed `theta<1` with `L(s,chi) != 0` for `Re(s)>theta` for every nonprincipal Dirichlet character. When this premise is instantiated with a tracker or cached dependency, the conclusion inherits that premise's exact theorem scope and verification limitations. Nothing here establishes the zero-free premise or claims priority.

For clarity take `1/2<=theta<1`. For every nonprincipal character modulo q, including complex and imprimitive characters, the premise implies

```text
|L(1,chi)| >= c_theta / loglog(q+3)
```

with a positive constant depending only on theta. In fact the same argument gives the asymptotic statement

```text
liminf_(q -> infinity) min_(chi nonprincipal mod q)
   |L(1,chi)| loglog(q) >= zeta(2) e^(−gamma) (1−theta).       (1)
```

Moduli without a nonprincipal character may be omitted from the minimum. The asymptotic constant is explicit; the argument below does not give an explicit finite-q threshold or a numerical value of `c_theta`.

For each character let `log L(s,chi)` be the unique analytic logarithm on `Re(s)>theta` that agrees with the absolutely convergent Euler logarithm on `Re(s)>1`. This is well-defined because that half-plane is simply connected and L is entire and zero-free there. Nonprincipal imprimitive characters cause no exception: their deleted Euler factors have no zeros on `Re(s)>0` and their L-functions are entire.

Fix `0<eta<1−theta`. Uniform convexity/strip bounds and the polynomial bound for imprimitive Euler factors give `|L(s,chi)| <= (q(3+|Im s|))^C` on each fixed vertical strip inside `Re(s)>theta`. On disks centered at `2+it`, the normalized logarithm at the center is absolutely bounded by the Euler series. Borel–Carathéodory on a slightly larger zero-free disk then gives

```text
|log L(s,chi)| <<_(theta,eta) log(q(3+|Im s|))
```

uniformly in the fixed strip `1−eta<=Re(s)<=2`. Disks retain a fixed positive distance from `Re(s)=theta`, so the implied constant is uniform in q and chi.

Choose a fixed `A>1/(1−theta)` and eta with `1/A<eta<1−theta`, and put `y=(log q)^A`. Shift the inverse-Mellin integral of `Gamma(z) log L(1+z,chi) y^z` from `Re(z)=1` to `Re(z)=−eta`. The logarithm is holomorphic on the intervening strip; the only crossed pole is that of Gamma at z=0, with residue `log L(1,chi)`. Gamma's exponential vertical decay controls the horizontal joins and the new integral. Its size is `O_(theta,eta)(y^(−eta) log(q+3))=o(1)` uniformly in chi. Hence

```text
log L(1,chi) = sum_(p,k>=1) chi(p)^k e^(−p^k/y)/(k p^k) + o(1).
```

By the prime number theorem (indeed standard effective Chebyshev bounds suffice for the smoothing comparison), the smoothed prime logarithm differs from the sharp logarithm `sum_(p<=y) sum_(k>=1) chi(p)^k/(k p^k)` by `o(1)`, uniformly in chi. The k>=2 terms follow from absolute summability. For every p and `|chi(p)|<=1`,

```text
Re [−log(1−chi(p)/p)] >= −log(1+1/p).
```

Taking real parts and using Mertens' product formula gives

```text
|L(1,chi)| >= (zeta(2)e^(−gamma)+o(1))/log y
            = (zeta(2)e^(−gamma)/A+o(1))/loglog q.
```

This holds for every fixed `A>1/(1−theta)`; let A approach that endpoint after taking the liminf to obtain (1). Fixed small q can be covered by shrinking `c_theta`: there are only finitely many characters and the assumed zero-free region includes `s=1`. This finite adjustment does not by itself provide a concrete numeric `c_theta`. The corresponding upper bound follows from `|1−chi(p)/p|>=1−1/p`, giving `|L(1,chi)| <= (e^gamma A+o(1)) loglog q` for each fixed admissible A.

For a negative fundamental discriminant `D<-4`, Dirichlet's class-number formula gives

```text
h(D) = sqrt(|D|) L(1,chi_D)/pi,
liminf_(D -> −infinity) h(D) loglog|D| / sqrt(|D|)
   >= pi e^(−gamma)(1−theta)/6.
```

The finitely many fields `D=−3,−4` have different unit factors and are harmless after a finite adjustment. The bound implies an effective-in-principle discriminant cutoff for any fixed class-number ceiling only if the strip-bound and Mertens constants, finite checks, and the underlying theta premise are made effective; (1) alone supplies no explicit cutoff.

## Prior art and qualification

Under GRH, Littlewood obtained the same logarithmic order and the constant `pi² e^(−gamma)/12` for real primitive characters; see [Montgomery–Vaughan, *Extreme values of Dirichlet L-functions at 1*](https://personal.science.psu.edu/rcv4/personal/Publications/LFNAT1H.pdf), Introduction. Our theta=`1/2` specialization agrees with that constant. A [Prove2Me record](https://prove2.me/theorems/2d1a57d1-6f7a-49e9-ac5b-c96941121ac8) already states the qualitative 7/8-half-plane implication for primitive real characters and reports a separately archived kernel-checked explicit corollary. Its record attributes the underlying source to Daugherty, Ryan and Ward. This note does not independently verify that formalization or its numerical constants. The [teal-sea record](https://zeta-record.vercel.app/read/hunts/README.html) separately describes a conditional, computational explicit class-number bound and a class-number census, with its own stated review status. These sources preclude claiming the qualitative imaginary-quadratic application as new.
