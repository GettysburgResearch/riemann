#include <quadmath.h>

#include <algorithm>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <vector>

namespace {

__float128 quad_pi() { return acosq(static_cast<__float128>(-1)); }

void kahan_add(long double value, long double& sum, long double& correction) {
    const long double adjusted = value - correction;
    const long double updated = sum + adjusted;
    correction = (updated - sum) - adjusted;
    sum = updated;
}

}  // namespace

int main(int argc, char** argv) {
    if (argc < 4) {
        std::fprintf(stderr, "usage: %s c first_index count\n", argv[0]);
        return 2;
    }
    const std::uint64_t cutoff = std::strtoull(argv[1], nullptr, 10);
    const std::uint64_t first_index = std::strtoull(argv[2], nullptr, 10);
    const int count = std::atoi(argv[3]);
    if (cutoff < 2 || count < 1) {
        std::fprintf(stderr, "c must be at least 2 and count positive\n");
        return 2;
    }

    std::vector<std::uint8_t> is_prime(cutoff + 1, 1);
    is_prime[0] = is_prime[1] = 0;
    for (std::uint64_t p = 2; p * p <= cutoff; ++p) {
        if (is_prime[p]) {
            for (std::uint64_t k = p * p; k <= cutoff; k += p) {
                is_prime[k] = 0;
            }
        }
    }
    std::vector<std::uint32_t> primes;
    primes.reserve(static_cast<std::size_t>(cutoff / std::log(static_cast<long double>(cutoff)) * 1.1L));
    for (std::uint64_t p = 2; p <= cutoff; ++p) {
        if (is_prime[p]) {
            primes.push_back(static_cast<std::uint32_t>(p));
        }
    }

    const __float128 pi = quad_pi();
    const __float128 two_pi = 2 * pi;
    const __float128 L_quad = logq(static_cast<__float128>(cutoff));
    const long double L = static_cast<long double>(L_quad);
    std::vector<long double> p_s(count, 0), p_d(count, 0);
    std::vector<long double> c_s(count, 0), c_d(count, 0);
    std::uint64_t prime_power_count = 0;

    for (const std::uint32_t p : primes) {
        const __float128 log_p = logq(static_cast<__float128>(p));
        std::uint64_t q = p;
        while (q <= cutoff) {
            ++prime_power_count;
            const __float128 log_q = logq(static_cast<__float128>(q));
            const long double y = static_cast<long double>(log_q);
            const long double weight = static_cast<long double>(log_p / sqrtq(static_cast<__float128>(q)));
            const long double alpha = 1 - y / L;
            const __float128 theta_quad = two_pi * log_q / L_quad;
            const long double theta = static_cast<long double>(theta_quad);
            const __float128 reduced = remainderq(theta_quad * static_cast<__float128>(first_index), two_pi);
            long double sine = sinl(static_cast<long double>(reduced));
            long double cosine = cosl(static_cast<long double>(reduced));
            const long double step_sine = sinl(theta);
            const long double step_cosine = cosl(theta);

            for (int j = 0; j < count; ++j) {
                kahan_add(weight * sine, p_s[j], c_s[j]);
                kahan_add(2 * weight * alpha * cosine, p_d[j], c_d[j]);
                const long double next_sine = sine * step_cosine + cosine * step_sine;
                const long double next_cosine = cosine * step_cosine - sine * step_sine;
                sine = next_sine;
                cosine = next_cosine;
                if ((j & 15) == 15) {
                    const long double norm = hypotl(sine, cosine);
                    sine /= norm;
                    cosine /= norm;
                }
            }
            if (q > cutoff / p) {
                break;
            }
            q *= p;
        }
    }

    std::printf(
        "{\n  \"c\": %llu,\n  \"n0\": %llu,\n  \"count\": %d,\n"
        "  \"prime_count\": %zu,\n  \"prime_power_count\": %llu,\n"
        "  \"L\": \"%.40Lg\",\n  \"PS\": [",
        static_cast<unsigned long long>(cutoff),
        static_cast<unsigned long long>(first_index),
        count,
        primes.size(),
        static_cast<unsigned long long>(prime_power_count),
        L);
    for (int j = 0; j < count; ++j) {
        std::printf("%s\"%.40Lg\"", j ? ", " : "", p_s[j]);
    }
    std::printf("],\n  \"PD\": [");
    for (int j = 0; j < count; ++j) {
        std::printf("%s\"%.40Lg\"", j ? ", " : "", p_d[j]);
    }
    std::printf("]\n}\n");
    return 0;
}
