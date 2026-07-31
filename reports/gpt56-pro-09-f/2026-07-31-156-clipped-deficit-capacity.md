# Full-trace capacity audit and clipped-deficit replacement

Agent: `gpt56-pro-09-f`  
Date: 2026-07-31  
Issue: #156  
Stack: draft PR #163

## Requested target

The requested scalar condition was

\[
 \operatorname{Tr}D_j-d_j(G_j-\alpha_j)
 \le G_j-\Gamma_j.
\]

It is a valid sufficient condition through `L-15612`, but a load-bearing audit
shows that it is not the sharp saturation theorem. It charges arbitrarily many
shallow deficit eigenvalues below `G_j-Gamma_j`, even though those modes cannot
cross the target complement floor.

## Exact finite separation

The rational model

```text
G=2, alpha=0, Gamma=1,
D=diag(2,2,3/5,3/5),
A=2I-D,
L=span(e1,e2)
```

has exact complement floor `7/5>1`. Nevertheless

```text
Tr D-2(G-alpha)=6/5>1=G-Gamma,
```

so the requested full-trace inequality fails.

Clipping at the exact danger threshold gives

```text
theta=G-Gamma=1,
Tr(D-theta I)_+=2=2(Gamma-alpha),
```

which captures precisely the two dangerous modes. `X-15605` verifies this with
exact Fractions; seven adversarial tests pass. Proof-object SHA-256:

```text
d246fe0a776f5baa01d21b3befb91dab4fbf1d21d528553c2a5a9e9eb1c43202
```

## New exact theorem: L-15618

For `A>=GI-D`, `A|L<=alpha I`, `dim L=d`, and

```text
D_theta=(D-theta I)_+,
0<=theta<G-alpha,
```

scalar Jensen and trace cyclicity give

```text
Tr(P_L D_theta P_L)>=d(G-alpha-theta),

A|L_perp >=
G-theta-[Tr D_theta-d(G-alpha-theta)].
```

At `theta=G-Gamma`, the exact sharp scalar gate is

\[
 \boxed{
 \operatorname{Tr}(D-(G-\Gamma)I)_+
 \le d(\Gamma-\alpha).}
\]

This proves `A|L_perp>=Gamma` and forces the complete dangerous part of `D` into
the low packet.

## New exact symbol theorem: L-15620

For a localization deficit

```text
D_G=P_I F^-1 (G-s)_+ F P_I,
```

Jensen on each eigenfunction and completeness of the time-limited Fourier basis
give the Berezin trace inequality

\[
 \operatorname{Tr}\Phi(D_w)
 \le {|I|\over2\pi}\int\Phi(w(\xi))d\xi
\]

for every nonnegative convex `Phi` with `Phi(0)=0`.

Taking `Phi(x)=(x-(G-Gamma))_+` yields the exact cancellation

\[
 \operatorname{Tr}
 (D_G-(G-\Gamma)I)_+
 \le {|I|\over2\pi}
 \int(\Gamma-s(\xi))_+d\xi.
\]

Therefore the proof-facing arithmetic target is

\[
 \boxed{
 {|I_j|\over2\pi}
 \int(\Gamma_j-s_j(\xi))_+d\xi
 \le d_j(\Gamma_j-\alpha_j).}
\]

On the scaled Suzuki interval, the prefactor is `1/pi`. The auxiliary level
`G_j` disappears completely.

## Near-quadratic exact-radical capacity: L-15619

Using a fixed compact Gevrey zero-mean atom with Fourier decay

```text
exp(-c |xi|^beta),
```

and spatial scale

```text
ell_lambda=(log lambda)^p/lambda,
p>1,
```

gives an exact source packet of rank

\[
 d_\lambda
 \gg_p{\lambda^2\over(\log\lambda)^p}
\]

with arithmetic Gram floor `1/2` and complete normalized exterior tail smaller
than every inverse power of `lambda`. The uniform Weil compression and cross
residual inherit the same rapid decay from `L-15617`.

Thus the source-capacity/rate side is within an arbitrarily small
polylogarithmic loss of the natural phase-space scale.

## Honest remaining theorem

The original full-trace inequality has not been proved for the complete Suzuki
symbol and is not necessary for saturation. The exact remaining arithmetic
statement is the strictly sharper directed sublevel integral

\[
 \boxed{
 {1\over\pi}
 \int_\mathbb R(\Gamma_j-s_j(\xi))_+d\xi
 \le d_j(\Gamma_j-\alpha_j),}
\]

or a Schatten/layer-cake majorant sufficient for it.

This is still RH-bearing. Existing mean-square/PNT shell estimates lose the
phase-sensitive terminal-prime cancellation and do not establish the cofinal
bound. No proof of RH is claimed.
