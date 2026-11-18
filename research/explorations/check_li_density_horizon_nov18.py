"""Arb certificate for the radial Li loss at 107 times the squared verified height."""

from flint import arb, ctx

from check_robin_density_nov18 import INGHAM, KADIRI


def main():
    ctx.prec = 128
    height = arb(3000175332800)
    degree = 107 * height**2
    pi = arb.pi()
    top = 1 - 1 / (arb("5.57") * (2 * height).log())
    assert arb("0.993") < top < arb("0.994")

    # Closed real-part intervals in Chourasiya--Simonic Tables 1 and 4.
    # Compute the exponents just once. Height dependence is evaluated below.
    rows = []
    for i in range(500, 994):
        s = arb(i) / 1000
        a, b, c = map(arb, INGHAM[(32 * (i - 500)) // 1000])
        ingham = (a, 3 * (1 - s) / (2 - s), (7 - 5*s) / (2 - s), b, c)
        valid = [row for row in KADIRI if row[0] * 1000 <= i * 6400]
        kadiri = None
        if valid:
            _, a, b = valid[-1]
            kadiri = (arb(a), 8*(1-s)/3, 2*(3-2*s), arb(b))
        rows.append((s, (s + arb(1)/1000).min(top), ingham, kadiri))

    def main_count(t):
        return t / (2*pi) * ((t/(2*pi)).log() - 1)

    next_weights = [arb(0) for _ in rows]
    total = arb(0)
    steps = 200
    for j in reversed(range(steps)):
        lower = height * (steps + j) / steps
        upper = height * (steps + j + 1) / steps
        log_h = upper.log()
        log_log_h = log_h.log()
        count_cap = (main_count(upper)-main_count(height)+10*(log_h+height.log()))/2
        scale = degree / lower**2
        prev = arb(1)
        for index, (_, right, ingham, kadiri) in enumerate(rows):
            a, power, logpower, b, c = ingham
            cap = count_cap.min(a * (power*log_h + logpower*log_log_h).exp()
                                + b*log_h**2 + c*log_h)
            if kadiri is not None:
                a, power, logpower, b = kadiri
                cap = cap.min(a * (power*log_h + logpower*log_log_h).exp() + b*log_h**2)
            this = (scale * (right - arb(1)/2)).cosh()
            weight = this - prev
            difference = weight - next_weights[index]
            assert difference > 0
            total += 4 * difference * cap
            next_weights[index] = weight
            prev = this

    tail = (2 * (2*height)**4 * 2*((2*height/(2*pi)).log()+arb(1)/3)
            / (3*pi*(2*height)**3) * ((degree/(8*height**2)).cosh()-1))
    ratio = (total + tail) / degree
    print("Index horizon", 107 * 3000175332800**2)
    print("Radial loss per index", ratio)
    assert ratio < 24


if __name__ == "__main__":
    main()
