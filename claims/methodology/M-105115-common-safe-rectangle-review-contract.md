# M-105115 - Common safe-rectangle review contract

Claim ID: M-105115

Status: **REVIEW CONTRACT**

Created: 2026-08-23

RH status: **unproved**

## Required checks

1. Treat every bad disk as closed and exclude the closed projection
   interval; tangency is not safe.
2. Require nonnegative half-width parameters \(T,\eta\) before using the
   absolute-coordinate identity.
3. Distinguish the exact full-supporting-line certificate from the larger,
   configuration-dependent set of safe finite rectangle boundaries.
4. Merge clipped projection intervals before computing \(|B_T|\) and
   \(|B_\eta|\); \(2S\) is only a relaxation.
5. Keep both strict inequalities \(\Delta_T>2S\) and
   \(\Delta_\eta>2S\) when using only total radius.
6. Normalize restricted Tonelli by the actual positive measure
   \(g_Tg_\eta\), and retain any additional null exceptional set.
7. Before comparing with an unrestricted shell mean, prove full-shell
   integrability or removable continuation across raw events.  Otherwise
   use only the restricted safe-set integral.
8. Require a single prescribed aggregate nonnegative cost before selecting
   the common rectangle.
9. Verify that every candidate boundary lies in the region on which the
   analytic upper and lower bounds hold.
10. Use raw quotients when zeros of \(F\) are allowed; do not divide through
   \(F'/F\) or \(F''/F\) at such zeros.
11. Preserve the L-105112 domain firewall.  An outer optimal selector need
    not have constant modulus on an intermediate edge.
12. Keep fixed outer carriers fixed throughout L-105113 averaging; do not
    rebuild a selector after seeing the selected rectangle.
13. Authenticate actual quotient-pole manifests separately from Cartan
    zero covers.

## Fail-closed scope

The following remain false unless separately proved:

- the supporting-line product exhausts every safe rectangle;
- the non-strict \(2S\) gate suffices for closed disks;
- projection overlap can be ignored without paying the relaxed loss;
- the restricted safe-set average has no normalization loss;
- unsafe raw quotient singularities are automatically full-shell integrable;
- zeros of \(F\) must be charged in the raw quotient route;
- qualitative order-one growth yields a usable cofinal Xi margin;
- a finite geometric transfer proves a signed moment lower bound;
- RCMV104530 or RH follows.
