# R-28001 — Fixed-order Abel positivity does not close the binary–ternary producer

Claim ID: `R-28001`  
Title: The third and fourth cumulative producer kernels have exact negative entries  
Status: **EXACT COUNTEREXAMPLES / STRONGER SOURCE-SPECIFIC SIGN REMAINS OPEN**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Frozen parent: PR #277 at `d5be8262c80a1debcf86922b45a4d00a406803f1`  
Reviewed target: PR #279 `L-27801/T-27801`

## 1. Producer

Retain the equal binary–ternary producer of `L-23811`.  Given a finite target
`w(2),...,w(X)`, put

\[
U(m)=\sum_{k\le X/m}\mu(k)w(mk),
\qquad
r(m)=U(m)-U(m+1),
\]

and solve downward

\[
A(m)=r(m)+\frac12\sum_{M>m}A(M)
\bigl[
\mathbf1_{\lceil M/3\rceil=m}
+\mathbf1_{M-\lceil M/3\rceil=m}
+\mathbf1_{\lfloor M/2\rfloor=m}
+\mathbf1_{M-\lfloor M/2\rfloor=m}
\bigr].
\]

For Abel order `k`, endpoint `Q`, and `q<=Q`, use

\[
w_{Q,k}(q)=\binom{Q-q+k-1}{k-1}.
\tag{R-28001.1}
\]

This is the `k`th cumulative producer kernel evaluated at a node.

## 2. Third-order witness

At

\[
Q=520,
\qquad k=3,
\qquad n=15,
\]

exact rational evaluation gives

\[
\boxed{
A_{w_{520,3}}(15)=-\frac{91}{256}<0.
}
\tag{R-28001.2}
\]

The target is exactly

\[
w(q)=\binom{522-q}{2}\mathbf1_{q\le520}.
\]

The value is independent of any larger ambient endpoint because the target and
its Möbius divergence vanish above `520`.  Consequently this is an interior
counterexample on every sufficiently larger endpoint.  It cannot be moved into
an endpoint collar of fixed or sublinear width.

Therefore the all-scale third-kernel assertion

\[
S_X(n,Q)\ge0
\]

in the form proposed by `TACP-I` is false.

The finite scan through `Q,n<=80` on PR #279 remains a correct finite statement;
it simply stops before the first witness found here.

## 3. Fourth-order witness

The next Abel order also fails.  At

\[
Q=3559,
\qquad k=4,
\qquad n=15,
\]

one obtains exactly

\[
\boxed{
A_{w_{3559,4}}(15)
=-\frac{84,999,795}{2048}<0.
}
\tag{R-28001.3}
\]

Thus increasing from three to four cumulative integrations does not repair the
ambient kernel.

## 4. Scope of the conclusion

These witnesses prove:

```text
raw producer positivity for every positive target        false;
second cumulative producer positivity                     false (PR #279);
third cumulative producer positivity                      false;
fourth cumulative producer positivity                     false.
```

They do **not** prove that every finite Abel order fails, and they do not produce
a negative coefficient for the actual logarithmic target

\[
w_X(q)=q^{-1/2}\log(X/q).
\]

The actual target has remained nonnegative in large floating reconnaissance,
but finite reconnaissance is not a proof.

## 5. Correct strategic consequence

The producer cannot be closed by asserting positivity of an ambient fixed-order
cumulative kernel and then invoking complete monotonicity of the target.  A
valid proof must use one of:

1. the complete source rather than an ambient target cone;
2. an order or kernel adapted to scale and source;
3. the dyadic Euler-aligned bottom charge derived in `L-28001`;
4. a reflected source-image theorem retaining every binary–ternary cross term;
5. another direct proof of the prime-ramp inequality.

The exact counterexamples narrow the method.  They do not show the binary–ternary
producer itself false.

## 6. Reproduction

`X-28001-binary-ternary-source/verify.py` regenerates both witnesses with
`fractions.Fraction` and no numerical library.
