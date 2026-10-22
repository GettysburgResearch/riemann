## Checkpoint 15 - normalized finite Cartan collar transfer

Exact checkpoint base:
f8102c6648829f72a6faaad06141c25b043c3f05.

The finite analytic collar input is now explicit. For \(f(a)\ne0\), zeros
in \(D(a,r_2)\), and

\[
A_f=\log\frac{\max_{|z-a|=r_3}|f(z)|}{|f(a)|},
\qquad \beta=\log(r_3/r_2),
\]

Jensen and a normalized finite Blaschke factor give

\[
n\le A_f/\beta,
\qquad
S_f\le\varepsilon r_2A_f/\beta,
\]

\[
\log|f(z)/f(a)|
\ge-
\left[
\frac{2r_1}{r_2-r_1}
+\frac{\log(2/\varepsilon)}{\beta}
\right]A_f
\]

outside the equal zero disks. Finite families add their radius loads, and
the sharp gate \(2S<\min(\Delta_T,\Delta_\eta)\) supplies one common
disk-safe rectangle.

The raw quotient route is cheaper than the log-derivative route: it needs
exceptional disks for \(F'\) and \(F''\), but not for \(F\). A constant
function exactly refutes the amplitude-unnormalized form sometimes printed
for Cartan lower bounds, so the checkpoint normalizes before every use.

The Xi variable is locked to
\(\Xi_t(z)=\xi(1/2+iz)\). The origin cannot be a common anchor for three
consecutive derivatives because \(\Xi_t\) is even. Authenticating an
off-center anchor, cofinal growth, complete manifests, and absorption of
the resulting permitted \(\exp(O_k(R\log^2 R))\) generic loss remain open.
RCMV104530 and RH are not proved.

Exact replay:

    PASS_T105114_ANCHORED_EQUAL_DISK_COLLAR
    16 focused tests in normal and optimized Python
    digest 15ff7ba8056a9beb5e942945c9f92dcce566f7d737bc04f8f2db6895109c3284
