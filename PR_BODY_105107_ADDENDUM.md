## Checkpoint 8 — boundary-optimal Blaschke–Pick selectors

Exact checkpoint base:
7e1cb178cd11202ed1e5877c898d1c2877d22521.

The polynomial CRT selector is no longer the endpoint of the fixed-window
bridge.  Factor every zero forced by the actual-pole manifest into a finite
inner function \(I_0\).  The top-jet congruences become ordinary values

\[
W=I_0H,
\qquad
H(c)=\gamma_c/\beta_c,
\]

and the exact optimal boundary norm is the first \(u\) for which

\[
\left[
\frac{u^2-y_j\overline y_k}{1-c_j\overline c_k}
\right]\succeq0.
\]

The extremal has constant boundary modulus and degree at most \(D-1\) in disk
coordinates.  It preserves the first/second L-105105 moment identities and
transports to rectifiable Jordan windows.

The improvement is strict: at the symmetric
\(\varepsilon=1/5,m=2\) cluster, the reduced polynomial norm is \(676\), while
the optimal inner selector attains the Blaschke lower bound \(625\).  The
intrinsic clustering loss remains.

Exact replay:

    PASS_T105107_BLASCHKE_PICK_JET_SELECTORS
    17/17 focused tests in normal and optimized Python
    digest 82747e320365a97bf9824dd84960f00bbcb77cd738040c2c5214be844dfc738c

Xi manifests, certified rectangle conformal data, cofinal Pick norms,
unweighted quotient edge bounds, RCMV104530, and RH remain open.
