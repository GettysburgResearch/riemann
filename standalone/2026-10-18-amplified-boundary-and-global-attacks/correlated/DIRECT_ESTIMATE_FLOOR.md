# A 13/15 floor for the unchanged direct estimate

Status: proved as an exact algebraic consequence of a specified exponent
recipe. This is a limit of that sufficient estimate, not a restriction on
the zeros of zeta or on possible stronger analytic estimates.

## Source and normalization

The input is Baiying Liu, [*Improved zero-free half-planes for the
quasi-Riemann hypothesis*, arXiv:2610.12234v2](https://arxiv.org/html/2610.12234v2#S22),
Section 22, Lemma 22.1 and Proposition 22.2, equations (22.1)--(22.4).
Write

\[
 M=l_x+l_y,\qquad b=l_y-l_x,\qquad
 k=\max\left\{0,\frac{1+3\ell-2M}{4},M+\ell-1,
                       \frac{3\ell-1}{2}\right\},
 \qquad a=\max\{0,b/12,b-l_y/2\}.                              \tag{1}
\]

The source's free length assumptions are
\(l_x,l_y>\ell>0\), \(b>0\), and \(h=1-l_x+\ell>0\), with the
lengths in fixed bounded ranges and the inherited coefficient and weight
hypotheses. Its direct and principal exponents are

\[
 L_{\rm low}=l_x/2+a+k/2,
 \qquad C(s)=s-5/6+l_x/3+\ell/6.
\]

Thus the comparison \(L_{\rm low}\le C(B)\) requires

\[
 B\ge B_{\rm low}:=\frac56+\frac{l_x}{6}-\frac\ell6+a+\frac k2.
                                                                    \tag{2}
\]

This uses the variable principal exponent, not the constant from the
original fixed lengths. The normalization in source (17.6) divides the
arithmetic average by \(c_S A_{\mathcal T}(Z)\), where \(c_S>0\) and
\(|A_{\mathcal T}(Z)|\asymp(\log Z)^{-K}\). It changes only the
arbitrarily small exponent loss, not (2). No zero-count, moment parameter,
or nonprincipal comparison is an input to the algebra below.

## Exact global lower bound

**Proposition.** For every real \(l_x,l_y,\ell\), with \(M,b,k,a\)
defined by (1),

\[
 \boxed{B_{\rm low}\ge\frac{13}{15}+\frac{17}{60}k
                         \ge\frac{13}{15}.}                    \tag{3}
\]

Consequently (3) holds throughout the source's free length domain. No
balanced relation between \(M\) and \(\ell\) is assumed.

**Proof.** Define three nonnegative slacks

\[
 d=a-b/12,\qquad
 s_1=4k-1-3\ell+2M,\qquad s_2=k-M-\ell+1.
\]

They are nonnegative directly from the maxima in (1). Substituting
\(l_x=(M-b)/2\) in (2) cancels \(b\) and gives

\[
 B_{\rm low}=\frac56+\frac M{12}-\frac\ell6+\frac k2+d.
\]

The exact identity

\[
 3s_1+s_2=13k+5M-10\ell-2
\]

therefore proves the nonnegative decomposition

\[
 \boxed{B_{\rm low}=\frac{13}{15}+\frac{17k}{60}
                    +d+\frac{3s_1+s_2}{60}.}                  \tag{4}
\]

Since \(k\ge0\), (3) follows. This is an explicit linear-program dual
certificate; no numerical optimization or sampling is involved. \(\square\)

## Sharpness of the relaxed direct recipe

Equality \(B_{\rm low}=13/15\) in (4) forces
\(k=d=s_1=s_2=0\). Solving \(s_1=s_2=0\) gives

\[
 M=\frac45,\qquad\ell=\frac15.
\]

At these values the four entries defining \(k\) are \(0,0,0,-1/5\).
Also \(d=0\) holds exactly when

\[
 0\le b\le\frac{3M}{8}=\frac3{10}.
\]

Indeed \(b/12\) must dominate both \(0\) and
\(b-l_y/2=3b/4-M/4\). Every \(0<b\le3/10\) also satisfies the
source's strict free length inequalities. For example,

\[
 b=\frac1{10},\quad l_x=\frac7{20},\quad l_y=\frac9{20},
 \quad h=\frac{17}{20}
\]

gives \(L_{\rm low}=11/60=C(13/15)\). Thus \(13/15\) is the
exact minimum of the direct scalar recipe even within those free length
inequalities. This example does **not** verify the other analytic
conditions of a complete zero-free argument.

The balanced restriction \(M+\ell=1\) is a separate specialization.
Source (22.5) then states

\[
 B_{\rm low}=\frac{11}{12}-\frac\ell4
       +\frac{(8b+3\ell-3)_+}{12}
       +\frac{(5\ell-1)_+}{8}.
\]

Its minimum is the same \(13/15\); the general proof above does not
need this formula. If an application imposes the additional strict
condition \(\ell<1/5\), the minimum need not be attained, but the same
infimum is approached with fixed \(b=1/10\),
\(M=1-\ell\), and \(\ell\uparrow1/5\), when only these direct
constraints are retained. Additional constraints can increase the
infimum.

## What this requires of a larger improvement

Even eliminating every error from the nonprincipal comparison would
leave the requirement \(B\ge13/15\) if (1)--(2) remain unchanged.
Therefore an improved moment bound on that side alone cannot deliver
\(B=5/6\), much less \(B=1/2\), through this exact recipe.

More quantitatively, suppose a new direct estimate reduces
\(L_{\rm low}\) by \(\Delta_{\rm dir}\), while retaining the same
principal exponent. To obtain a desired boundary \(B_{\rm goal}\),
it is necessary that

\[
 \Delta_{\rm dir}\ge B_{\rm low}-B_{\rm goal}
 \ge\frac{13}{15}-B_{\rm goal}+\frac{17k}{60}.
\]

The optimistic minimum gain is \(1/30\) for \(B_{\rm goal}=5/6\),
and \(11/30\) for \(B_{\rm goal}=1/2\). These are necessary
exponent budgets, not sufficient new estimates. A different arithmetic
observable, a different principal term, or a stronger direct estimate
changes the system. Restricting the target family can help only if it
actually changes a binding estimate or the comparison itself.

This direct-only floor is separate from Liu's sharper optimality theorem
for his full comparison system (Section 34.2), and from the fixed-moment
Xu--Sang endpoint limit in `XU_FIXED_KAPPA_LIMIT.md`. Those statements
retain constraints that were deliberately removed here. No claim is made
that this elementary consequence is new in the literature.
