#include <quadmath.h>
#include <algorithm>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iomanip>
#include <string>
#include <vector>

struct Kahan {
    long double sum = 0;
    long double correction = 0;
    void add(long double value) {
        long double y = value - correction;
        long double t = sum + y;
        correction = (t - sum) - y;
        sum = t;
    }
};

int main(int argc, char **argv) {
    uint64_t cutoff = 100000000ULL;
    int cells = 1024;
    std::string carrier_text = "4709203636353.65";
    std::string output = "phase-coefficients.json";
    if (argc > 1) cutoff = std::strtoull(argv[1], nullptr, 10);
    if (argc > 2) cells = std::atoi(argv[2]);
    if (argc > 3) carrier_text = argv[3];
    if (argc > 4) output = argv[4];
    if (cutoff < 2 || cells < 1) return 2;

    std::vector<uint8_t> is_prime(cutoff + 1, 1);
    is_prime[0] = is_prime[1] = 0;
    for (uint64_t p = 2; p * p <= cutoff; ++p)
        if (is_prime[p])
            for (uint64_t k = p * p; k <= cutoff; k += p) is_prime[k] = 0;
    std::vector<uint32_t> primes;
    for (uint64_t p = 2; p <= cutoff; ++p)
        if (is_prime[p]) primes.push_back(static_cast<uint32_t>(p));

    std::vector<Kahan> lr(cells), li(cells), qr(cells), qi(cells);
    const long double pi = acosl(-1.0L), two_pi = 2 * pi;
    const long double L = logl(static_cast<long double>(cutoff));
    const long double T = strtold(carrier_text.c_str(), nullptr);
    const __float128 piq = acosq(-1), two_piq = 2 * piq;
    const __float128 Lq = logq(static_cast<__float128>(cutoff));
    const __float128 Tq = strtoflt128(carrier_text.c_str(), nullptr);
    uint64_t prime_power_count = 0;

    for (uint32_t p : primes) {
        uint64_t q = p;
        while (q <= cutoff) {
            ++prime_power_count;
            const long double lp = logl(static_cast<long double>(p));
            const long double lq = q == p ? lp : logl(static_cast<long double>(q));
            const long double scaled = cells * lq / L;
            const uint64_t lag = static_cast<uint64_t>(floorl(scaled));
            const long double fraction = scaled - lag;
            const long double amplitude = lp / (pi * sqrtl(static_cast<long double>(q)));
            const long double phase_l = remainderl(T * lq, two_pi);
            const long double real_l = amplitude * cosl(phase_l);
            const long double imag_l = -amplitude * sinl(phase_l);

            const __float128 lpq = logq(static_cast<__float128>(p));
            const __float128 lqq = q == p ? lpq : logq(static_cast<__float128>(q));
            const __float128 scaledq = static_cast<__float128>(cells) * lqq / Lq;
            const uint64_t lagq = static_cast<uint64_t>(floorq(scaledq));
            const __float128 fractionq = scaledq - lagq;
            if (lag != lagq) return 3;
            const __float128 amplitudeq = lpq / (piq * sqrtq(static_cast<__float128>(q)));
            const __float128 phaseq = remainderq(Tq * lqq, two_piq);
            const long double reducedq = static_cast<long double>(phaseq);
            const long double real_q = static_cast<long double>(amplitudeq) * cosl(reducedq);
            const long double imag_q = -static_cast<long double>(amplitudeq) * sinl(reducedq);

            auto deposit = [&](uint64_t d, long double wl, long double wq) {
                if (d < static_cast<uint64_t>(cells)) {
                    lr[d].add(wl * real_l);
                    li[d].add(wl * imag_l);
                    qr[d].add(wq * real_q);
                    qi[d].add(wq * imag_q);
                }
            };
            deposit(lag, 1 - fraction, static_cast<long double>(1 - fractionq));
            deposit(lag + 1, fraction, static_cast<long double>(fractionq));
            if (q > cutoff / p) break;
            q *= p;
        }
    }

    long double maximum_difference = 0, coefficient_l1_difference = 0;
    for (int i = 0; i < cells; ++i) {
        long double difference = hypotl(
            lr[i].sum - qr[i].sum,
            li[i].sum - qi[i].sum
        );
        maximum_difference = std::max(maximum_difference, difference);
        coefficient_l1_difference += difference;
    }

    std::ofstream out(output);
    out << std::setprecision(21);
    out << "{\n\"cutoff\":" << cutoff << ",\"K\":" << cells
        << ",\"T\":\"" << carrier_text << "\",\"prime_count\":"
        << primes.size() << ",\"prime_power_count\":" << prime_power_count
        << ",\"maximum_coefficient_difference\":"
        << static_cast<double>(maximum_difference)
        << ",\"coefficient_l1_difference\":"
        << static_cast<double>(coefficient_l1_difference) << ",\n";
    auto write_array = [&](const char *name, const std::vector<Kahan> &values, bool comma) {
        out << "\"" << name << "\":[";
        for (int i = 0; i < cells; ++i) {
            if (i) out << ',';
            out << static_cast<double>(values[i].sum);
        }
        out << "]" << (comma ? ",\n" : "\n");
    };
    write_array("long_real", lr, true);
    write_array("long_imag", li, true);
    write_array("quad_real", qr, true);
    write_array("quad_imag", qi, false);
    out << "}\n";
}
