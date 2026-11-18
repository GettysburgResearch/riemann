# Brief independent check of the tree-Holder integrability step

Reviewer: semantic_skeptic. Date:17 November2026. This independently checks the general step indexed as SG309 in `proposals/independent_campaigns/sine_gram_moment_existence_round4.md`; it creates no duplicate theorem or full alternative development.

The step is valid. A cyclic trace word identifies vertices but retains labeled edge occurrences. Removing loops leaves, for at least two vertices, a connected Eulerian multigraph. Every vertex degree remains even; therefore no edge is a bridge. Parallel edges must remain separate occurrences: in a doubled two-vertex graph each has spanning-tree inclusion probability1/2, not1.

For uniform weights over the finite collection of spanning trees, every nonloop edge has inclusion probability r_e>0 because it belongs to some tree. Bridgelessness gives r_e<1 because deleting that edge leaves a connected graph and hence a tree omitting it. For each tree define F_T=product_(e in T)|k_e|^(1/r_e). The identity product_T F_T^(w_T)=product_e|k_e| and weighted Holder give

integral product_e|k_e|<=product_T(integral F_T)^(w_T)
 =product_e||k||_(1/r_e).

The last equality is correct, including the exponents: tree edge differences form a unimodular coordinate map, and the exponent contributed for edge e is(1/r_e)sum_(T contains e)w_T=1. Every norm is finite since1/r_e>1. The one-vertex graph is handled separately by its empty product/integral1.

The nonbridge condition is material. A single bridge edge would have r_e=1 and demand the divergent L1 norm of sinc; this proof does not cover such a graph. Cyclic trace-word quotient graphs cannot have that defect. For a triangle and a four-cycle the bound specializes to the familiar L^(3/2) and L^(4/3) convolution bounds, respectively.

Combined with0<=rho_l<=1, the ordered Campbell partition expansion and the exact root-window factor0<=w_R<=1 tending to1, this supplies dominated convergence for every fixed expected moment. The moment order is fixed; no uniform growing-order estimate follows from these graph constants alone. The separately established factorial bound supplies uniform integrability and Hamburger determinacy/full expected-law convergence. None of these steps proves ergodicity, almost-sure IDS convergence or arithmetic moment matching.
