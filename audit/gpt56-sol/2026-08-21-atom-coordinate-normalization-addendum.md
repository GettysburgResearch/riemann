# Addendum — atom-coordinate normalization in the balanced transition

Date: 2026-08-21  
Status: binding correction

After the main audit was written, one further representation mismatch was
caught in newly added `L-100710`.

If

\[
w(n)=n^{-(m+1)/2}\kappa(\sqrt{n/X}),
\]

then the full Euler activity is already included in `w(np)`. Therefore

```text
endpoint-kernel coordinates: R_p = p^-1/2 U_p - p^-1 U_(p^2);
source-atom coordinates:     (R_p w)(n) = w(np)-w(np^2).
```

`L-100710` multiplied the atom weights by the endpoint activities once more and
is withdrawn. The corrected theorem is `L-100711`:

\[
w(np^2)\le p^{-1}w(np),
\qquad
w(np)-w(np^2)>0.
\]

For every future prime `q`, however, the corrected transition obeys only

\[
\frac{(R_pw)(nq)}{(R_pw)(n)}\le q^{-1}.
\]

Thus the distinguished transition is locally positive but remains at the
prime-harmonic future exponent. This is exactly compatible with the retained
finite completion counterexample and leaves the balanced cross-prime estimate
open.