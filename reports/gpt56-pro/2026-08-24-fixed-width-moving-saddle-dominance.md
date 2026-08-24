# Fixed-width moving-saddle dominance from the explicit Xi kernel

The earlier moving-saddle proposal had the right local saddle but lacked a global comparison along the translated contour. The missing comparison becomes tractable after using the correct horizontal ray through the saddle.

For large real part, the first theta orbit dominates the Xi kernel with all fixed derivatives. Its logarithmic second derivative is

```text
(log phi_1)''=-2x-12x/(x-3)^2,
x=2pi exp(2u).
```

On a sufficiently narrow complex strip this has negative real part of size `exp(2 Re u)`. Adding the `m log u` term gives

```text
Re S_m''(t+delta)
 <= -c[m/t^2+exp(2t)].
```

Because the exact saddle equation makes the real derivative vanish at parameter `t=w_m`, the real action is strictly concave and globally maximized there. This proves the shifted-ray dominance requested by the prior audit. A complex Gaussian expansion then gives a relative saddle asymptotic, and the exact reflected phase gives the fixed-width real-rooted high derivative tail.

The proof is marked proposed complete pending independent hostile review. It does not address the low-order Levinson/residue descent and does not prove RH.
