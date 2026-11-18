"""Arb enclosure of the radial Li loss at 100 times the squared verified height."""
from flint import arb, ctx


def main():
    ctx.prec = 112
    T = arb(3000175332800)
    M = 100 * T**2
    pi = arb.pi()

    # KLN Table 1. The first column is 1000*sigma, the second bounds 100*A.
    rows = [(600,218),(650,297),(700,399),(750,528),(800,692),
            (850,898),(860,945),(870,993),(880,1044),(890,1096),
            (900,1150),(910,1207),(920,1265),(930,1326),(940,1388),
            (950,1452),(960,1518),(970,1586),(980,1655),(990,1726)]
    top = 1 - 1/(arb("5.57")*(2*T).log())
    assert arb("0.993") < top < arb("0.994")

    def main_count(x):
        return x/(2*pi)*((x/(2*pi)).log()-1)

    total = arb(0)
    steps = 200
    # Reverse height order permits a cumulative-count Abel bound.
    next_weight = [arb(0)]*494
    for j in reversed(range(steps)):
        lo = T*(steps+j)/steps
        hi = T*(steps+j+1)/steps
        hlog = hi.log()
        all_right = (main_count(hi)-main_count(T)+10*(hlog+T.log()))/2
        cap = all_right
        table_caps = {}
        for index, coefficient in rows:
            sigma = arb(index)/1000
            table_caps[index] = (arb(coefficient)/100*hlog**(5-2*sigma)
                                 *hi**(8*(1-sigma)/3) + 6*hlog**2)
        scale = M/lo**2
        prev_cos = arb(1)
        for i in range(500,994):
            sigma = arb(i)/1000
            upper = (arb(i+1)/1000).min(top)
            if i in table_caps:
                cap = cap.min(table_caps[i])
            if i >= 980:
                # Johnston--Yang, Table 3, at the indicated exact sigma.
                cap = cap.min(arb("17.5") * hlog**(5-2*sigma)
                              *hi**(8*(1-sigma)/3) + arb("2.3")*hlog**2)
            new_cos = (scale*(upper-arb(1)/2)).cosh()
            weight = new_cos-prev_cos
            diff = weight-next_weight[i-500]
            assert diff > 0
            total += 4*diff*cap
            next_weight[i-500] = weight
            prev_cos = new_cos

    tail = 2*(2*T)**4*(2*((2*T/(2*pi)).log()+arb(1)/3)/(3*pi*(2*T)**3))
    tail *= (M/(8*T**2)).cosh()-1
    loss = (total+tail)/M
    print("M",100*3000175332800**2)
    print("radial loss per index",loss)
    assert loss < arb("28.2")


if __name__ == "__main__":
    main()
