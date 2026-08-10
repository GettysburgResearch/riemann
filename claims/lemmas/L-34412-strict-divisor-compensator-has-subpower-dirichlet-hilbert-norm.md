# L-34412 — The strict-divisor compensator has a subpower half-scale Dirichlet-Hilbert norm

Claim ID: `L-34412`  
Title: In the natural critical coefficient norm, the nonunit-divisor lift has operator norm `X^{o(1)}` and uses only strict half-scale inputs  
Status: **PROPOSED COMPLETE ELEMENTARY OPERATOR THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring/review agent: `gpt56-pro`  
Created: 2026-08-10  
Dependencies: `L-34411`; the elementary divisor bound `tau(n)=n^{o(1)}`  
Scope: truncated Dirichlet coefficient Hilbert space. No physical normal-Gram transfer or reflected recurrence is claimed

## 1. Truncated critical coefficient norm

For an arithmetic sequence `f` and endpoint `X>=2`, define

\[
\boxed{
 \|f\|_{\mathscr D(X)}^2
 =\sum_{n\le X}{|f(n)|^2\over n}.
}
\tag{L-34412.1}

This is the diagonal critical-line coefficient norm associated with amplitudes `f(n)/sqrt(n)`.

Let

\[
 \mathcal V f=(\mathbf1-\varepsilon)*f.
\]

Coefficientwise,

\[
\boxed{
 (\mathcal Vf)(n)
 =\sum_{\substack{d\mid n\\d>1}}f(n/d).
}
\tag{L-34412.2}

`L-34411` identifies the compensator as

\[
 \Gamma=\mathcal Vt_{\rm odd}.
\]

## 2. Exact strict-half-scale support

Every term in (L-34412.2) has

\[
 m=n/d\le n/2.
\]

Consequently, when `n<=X`, the operator uses only

\[
 m\le X/2.
\]

Thus

\[
\boxed{
 \mathcal V:\mathscr D(X/2)\longrightarrow\mathscr D(X)
}
\tag{L-34412.3}

has no current-scale input coordinate.

## 3. Divisor-Cauchy estimate

Let

\[
 D(X)=\max_{n\le X}\tau(n),
\]

where `tau(n)` is the number of positive divisors.  For each `n`, Cauchy--Schwarz gives

\[
\begin{aligned}
 |(\mathcal Vf)(n)|^2
 &\le (\tau(n)-1)
  \sum_{\substack{d\mid n\\d>1}}|f(n/d)|^2\\
 &\le D(X)
  \sum_{\substack{d\mid n\\d>1}}|f(n/d)|^2.
\end{aligned}
\tag{L-34412.4}

Multiply by `1/n`, sum over `n<=X`, and write `n=dm`:

\[
\begin{aligned}
 \|\mathcal Vf\|_{\mathscr D(X)}^2
 &\le D(X)
  \sum_{\substack{dm\le X\\d\ge2}}
  {|f(m)|^2\over dm}\\
 &=D(X)
  \sum_{m\le X/2}{|f(m)|^2\over m}
  \sum_{2\le d\le X/m}{1\over d}.
\end{aligned}
\tag{L-34412.5}

The harmonic sum is at most `log X`. Therefore

\[
\boxed{
 \|\mathcal Vf\|_{\mathscr D(X)}^2
 \le D(X)\log X\,
       \|f\|_{\mathscr D(X/2)}^2.
}
\tag{L-34412.6}

This is a complete finite-endpoint inequality.

## 4. Subpower operator norm

The elementary divisor estimate says that for every fixed `epsilon>0`,

\[
 \tau(n)\le C_\epsilon n^\epsilon,
\]

and equivalently

\[
 D(X)=X^{o(1)}.
\]

Hence

\[
\boxed{
 \|\mathcal V\|_{
  \mathscr D(X/2)\to\mathscr D(X)}^2
 \le X^{o(1)}.
}
\tag{L-34412.7}

More explicitly, for every `epsilon>0`,

\[
\boxed{
 \|\mathcal Vf\|_{\mathscr D(X)}^2
 \le C_\epsilon X^\epsilon\log X\,
       \|f\|_{\mathscr D(X/2)}^2.
}
\tag{L-34412.8}

Applying this to the odd second current,

\[
\boxed{
 \|\Gamma\|_{\mathscr D(X)}^2
 \le D(X)\log X\,
       \|t_{\rm odd}\|_{\mathscr D(X/2)}^2.
}
\tag{L-34412.9}

## 5. Direct consequence for the compensated path

`L-34410` proves that `Gamma` is the sole difference between the actual and the all-row positive compensated second jet.  Equation (L-34412.9) shows that this difference is:

```text
strictly lower scale;
source complete;
subpower in the diagonal critical coefficient metric.
```

Thus a proof which transports the `D`-norm to the complete independent-frequency physical Gram with only subpower loss would place the compensator inside the admissible fixed-delay recurrence.

## 6. Firewall: the physical Gram is not the diagonal coefficient norm

The theorem does **not** identify

\[
 \|f\|_{\mathscr D(X)}^2
\]

with a unit physical logarithmic-block energy.  The latter contains off-diagonal pairs of nearby logarithmic frequencies.  Nor does (L-34412.6) permit taking absolute values before the complete source recombination.

A valid continuation must provide one of:

1. an exact annular physical/coefficient isometry for the compensated source;
2. a source-bound Schur estimate controlling the off-diagonal normal Gram;
3. a root-of-unity or other orthogonalization which preserves the proper-divisor labels through the reflected block.

Without such a theorem, the diagonal estimate alone does not prove RH.

## 7. Proof boundary

Closed exactly here, subject to review:

1. strict-half-scale coefficient routing;
2. finite divisor-Cauchy estimate;
3. harmonic factor;
4. `X^{o(1)}` operator norm in `mathscr D`;
5. application to the unique compensator.

Open:

1. transfer to the independent-frequency physical normal Gram;
2. source-complete Schur elimination;
3. coefficient-one reflected recurrence;
4. RH.
