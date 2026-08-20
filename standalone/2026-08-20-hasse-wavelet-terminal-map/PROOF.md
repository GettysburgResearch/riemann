# T100210 — Signed Hasse divergence and the minimal-wavelet terminal map

**Scientific status:** exact terminal map; `MWOC99910` and RH remain unproved.

## 1. Flow-independent Hasse divergence

Let `B={1,...,k}` be labelled vertices with activities `0<a_i<1`. Put

\[
w(A)=\prod_{i\in A}a_i,\qquad \Delta_B=\prod_i(1-a_i).
\]

Suppose `J` is any nonnegative Hasse flow from odd vertices to even vertices such that every odd vertex exports exactly `w(A)`, every nonempty even vertex receives exactly `w(A)`, and the empty even vertex receives `1-Delta_B`.

For a complex potential `Phi` on the cube define

\[
\mathcal B_J(\Phi)=\sum_{A\text{ odd}}\sum_{E\text{ even},A\sim E}J(A,E)[\Phi(A)-\Phi(E)].
\]

Summing the divergence at every vertex gives

\[
\boxed{
\mathcal B_J(\Phi)=\Delta_B\Phi(\varnothing)-\sum_{A\subseteq B}(-1)^{|A|}w(A)\Phi(A).
}
\tag{1}
\]

Thus the signed boundary is independent of the priority order and of the particular feasible flow.

For the exponential product potential

\[
\Phi_\gamma(A)=P_A^{i\gamma},\qquad P_A=\prod_{i\in A}p_i,
\]

finite Euler expansion gives

\[
\boxed{
\mathcal B_J(\Phi_\gamma)=\Delta_B-\prod_i(1-a_ip_i^{i\gamma}).
}
\tag{2}
\]

At the neutral phase,

\[
\boxed{\mathcal B_J(\Phi_0)=0.}
\tag{3}
\]

The edgewise factors `1-p_i^{i gamma}` are the local differential form of this global product identity.

## 2. Exact dictionary to the minimal ordinary-Möbius wavelet

Let `K_0` be PR #674's compact kernel supported on `[1,8]`, and put

\[
\phi(y)=\frac{K_0(y)}{\sqrt y}.
\]

The minimal ordinary-Möbius wavelet is

\[
G_\mu(X)=\sum_{n\ge1}\frac{\mu(n)}{\sqrt n}K_0(X/n).
\]

After division by `sqrt(X)`,

\[
\boxed{
\frac{G_\mu(X)}{\sqrt X}=\sum_{n\ge1}\frac{\mu(n)}n\phi(X/n).
}
\tag{4}
\]

Fix `X` and take one label for each prime `p<=X`, with native normalized activity

\[
a_p=\frac1p.
\]

For a labelled subset `A`, set

\[
\Phi_X(A)=\phi(X/P_A).
\]

The potential vanishes unless `X/8<=P_A<=X`, so the finite cube contains the complete physical packet, and

\[
\sum_A(-1)^{|A|}w(A)\Phi_X(A)=\frac{G_\mu(X)}{\sqrt X}.
\]

Applying (1),

\[
\boxed{
\frac{G_\mu(X)}{\sqrt X}=\Delta_X\phi(X)-\mathcal B_{J_X}(\Phi_X),
}
\tag{5}
\]

where

\[
\Delta_X=\prod_{p\le X}(1-p^{-1}).
\]

For `X>8`, `phi(X)=0`, hence

\[
\boxed{
\frac{G_\mu(X)}{\sqrt X}=-\mathcal B_{J_X}(\Phi_X).
}
\tag{6}
\]

The compact ordinary-Möbius scalar is therefore exactly the signed Hasse divergence under the correct native `1/p` activities.

## 3. Positive variation is not controlled by neutral cancellation

For a real potential write

\[
U_+=\sum J(A,E)[\Phi(A)-\Phi(E)]_+,
\]

\[
U_-=\sum J(A,E)[\Phi(E)-\Phi(A)]_+,
\]

and `V=U_++U_-`. Then

\[
\boxed{
\mathcal B_J(\Phi)=U_+-U_-,\qquad U_+=\frac{V+\mathcal B_J(\Phi)}2.
}
\tag{7}
\]

The signed product controls only `U_+-U_-`; it gives no upper bound for `V`.

An exact two-edge fixture has two edges of mass `1/2` and drops `+1` and `-1`. Then

\[
\mathcal B_J(\Phi)=0,\qquad V=1.
\]

Repeating the fixture leaves the signed boundary zero while making positive variation arbitrarily large. PR #673 proves the corresponding actual priority positive flux is power-sized for every ordering, so averaging orders cannot repair the shortcut.

Thus the inference

```text
neutral phase annihilation
    -> subpower positive Hasse variation
    -> RH
```

is false. Any valid phase-Hasse proof must preserve cancellation between different edges through the compact wavelet observation.

## 4. Terminal route map

The phase-Hasse route now has a complete disposition:

1. every exact cube flow has the same signed divergence (1);
2. its phase symbol is the closed Euler product (2), with neutral phase zero;
3. under the native normalized activities `1/p`, the physical signed divergence is exactly the minimal ordinary-Möbius wavelet (6);
4. PR #674 gives the unique minimal ratio-eight kernel and positive desmoothing resolvents;
5. PR #675 proves that the critical cumulative Hardy energy and `MWOC99910` are equivalent to RH;
6. the positive-variation shortcut is refuted by (7) and PR #673.

Therefore the only viable continuation is a signed nonzero-phase packing estimate preserving inter-edge cancellation through the wavelet observation. Under the exact dictionary above, it is precisely the ordinary-Möbius cross-core theorem `MWOC99910`:

\[
\boxed{
\text{signed phase-Hasse packing}\longrightarrow MWOC99910\longleftrightarrow RH.
}
\tag{8}
\]

The conclusion-facing arithmetic arrow remains open.

## 5. Exact status

```text
flow-independent signed divergence          proved
closed Euler-product phase symbol           proved
neutral phase annihilation                  proved
minimal-wavelet source dictionary           proved
positive variation shortcut                 refuted
signed nonzero-phase packing / MWOC          open / RH-equivalent
Riemann Hypothesis                          unproved
```
