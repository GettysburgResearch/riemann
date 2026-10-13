import numpy as np
a0, d0, alpha = 51/100, 1/50, 5/6
def Rstar(delta, x=0.5):
    Dx = 3 - 17*x/9; Px = (2 - 8*x/9)*(1 - x); J = (alpha-delta)*Dx + delta*Px
    return 1 - delta + (alpha-delta)*delta*Px/(2*J)
for (b,l) in [(1/8,1/6)]:
    lx, ly, h = (1-b-l)/2, (1+b-l)/2, (1+b+3*l)/2
    print(f"(b,l)=({b},{l}): h={h:.4f}, 1/h={1/h:.4f}")
    for name, R in [("paper", Rstar), ("ideal", lambda d: 1-d)]:
        eps=1e-6; s = (R(d0+eps)-R(d0))/eps
        c = -(h*(s + 1/4)) + (1-ly)/2            # per unit (delta-delta0); eta' = (delta-delta0)/2
        print(f"  {name} counts: dR/ddelta|floor = {s:+.3f}; near-floor row with zero at a0+eta' costs Z^(eta - {2*c:.3f} eta') relative to trivial")
        print(f"      => eta' > {1/(2*c):.3f} eta;  truncation r h (eta-eta') > eta  =>  r > 1/(h(1-{1/(2*c):.3f})) = {1/(h*(1-1/(2*c))):.2f}")
        # far class at delta=5/6 with that r: extra over paper's bin bound
        r = 1/(h*(1-1/(2*c)))
        slope = h*r/2 - (1-ly)/2 - h/4
        extra = (alpha-d0)*slope
        slack_ideal = 1/48 + alpha/16
        print(f"      far class delta=5/6 at r={r:.2f}: extra over bin bound = {extra:.3f} - eta*({r*h-1:.2f});  ideal slack there = {slack_ideal:.3f}  => needs eta >= {(extra-slack_ideal)/(r*h-1):.3f}; then main needs f >= eta/h = {(extra-slack_ideal)/(r*h-1)/h:.3f}")
