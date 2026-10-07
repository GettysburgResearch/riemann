# Exponent model for the 7/8 paper (exploratory reconstruction)

Status: EMPIRICAL / PROPOSED reconstruction. This is not a statement of the paper.

`model2.py` re-implements the high-side exponent bookkeeping of the Sept 30 paper, Part II, from its stated formulas:
* row-bin exponent, ll. 15726–15735;
* adaptive row count, ll. 15963–15966 and Prop. `detector-counts`, ll. 15185–15220;
* low-side exponent $l_x/2+b/12$, l. 8570;
* dual-length loss.

It also implements variants:
* `optLS`: optimal capacities;
* `DH`: density hypothesis for rows;
* `msMob`: an optimal mean square replacing amplification.

Check: at the paper geometry `(l_x,b,ell)=(17/48,1/8,1/6)`, `sigma_low` returns `0.875`. The worst high-side margin at $\beta_*=7/8^+$ is $\approx-1.9\times10^{-4}$, at $\delta\approx0.3875$, $x=1/2$. The paper's certificate is $-49/440640$ plus a $\Delta$ term (ll. 16000, 16096–16104).

* `opt5.py <mode> <seed> <seconds> <step>`: random local search over the geometry.
* `dhopt.py`: grid optimum under the density hypothesis for rows ($13/15$).

Run with `python3 -I`, from this directory.
