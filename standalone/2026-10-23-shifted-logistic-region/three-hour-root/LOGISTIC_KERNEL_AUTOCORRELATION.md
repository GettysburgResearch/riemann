# A direct autocorrelation proof for the detector kernel

Status: proposed elementary lemma. This reproduces the positivity needed
from the Heath-Brown kernel in BTY Definition 1 without requiring a
numerical root check or a positivity assertion outside its domain.

Let 0<theta<pi/2, k=tan(theta), d=theta/k and S=sec(theta)^2. Define

    g(x)=S[cos(kx)-cos(theta)] for |x|<=d, and g(x)=0 otherwise.

Then g is even, nonnegative, continuous, compactly supported and piecewise
smooth. Its autocorrelation w_e(v)=integral_R g(x)g(x+v)dx is even and
supported on [-2d,2d]. For 0<=v<=2d, direct integration over
[-d,d-v] gives

    w_e(v)=S^2[(d-v/2)cos(kv)+sin(2theta-kv)/(2k)
                  -2cos(theta)(sin(theta)+sin(theta-kv))/k
                  +cos(theta)^2(2d-v)].                         (K1)

Using S/(2k)=csc(2theta) and S cos(theta)/k=csc(theta), (K1) is
precisely the w(v) in BTY Definition 1. Expanding the two shifted sines
gives the equivalent elementary formula used by the scalar certificates.

The consequences follow directly:

* w(v)>=0, because g is nonnegative.
* w(v)<=w(0), by Cauchy--Schwarz and translation invariance of the L2 norm.
* With the Fourier convention ghat(y)=integral g(x)exp(-iyx)dx,
  the transform of w_e is |ghat(y)|^2. Thus
  Re W(iy)=|ghat(y)|^2/2>=0.
* w_e is C2, piecewise C3; w'(0)=0 and w(2d)=w'(2d)=w''(2d)=0.
  For example g is Lipschitz with a bounded piecewise derivative, so the
  second derivative of its correlation is the continuous correlation of
  those L2 derivatives, up to sign. Near the support endpoint each factor
  of g vanishes linearly, giving w(v)=O((2d-v)^3), with the same
  endpoint conclusions also visible by differentiating (K1).

Finally, (K1) at v=0 gives

    w(0)=sec(theta)^2[theta tan(theta)+3theta cot(theta)-3].

For theta=5669/5000 the exact rational constant checker proves w(0)<6
and 2d<1.1, so the positivity, boundedness and Fourier facts assumed in
the master reduction are consequences of this elementary factorization.
The explicit formula, zero-count theorem, finite RH verification and
Littlewood region remain distinct imported analytic inputs.
