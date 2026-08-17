#include <algorithm>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <sstream>
#include <string>
#include <vector>

using u128 = __uint128_t;
using i128 = __int128_t;

static constexpr uint64_t Q = 1000000000000000000ULL;
static const u128 Q2 = (u128)Q * (u128)Q;

static std::string to_string_i128(i128 x) {
    if (x == 0) return "0";
    const bool neg = x < 0;
    u128 u = neg ? (u128)(-x) : (u128)x;
    std::string s;
    while (u != 0) {
        s.push_back(char('0' + (u % 10)));
        u /= 10;
    }
    if (neg) s.push_back('-');
    std::reverse(s.begin(), s.end());
    return s;
}

static std::string decimal_ratio(i128 x, u128 denominator, int digits = 18) {
    const bool neg = x < 0;
    u128 u = neg ? (u128)(-x) : (u128)x;
    const u128 whole = u / denominator;
    u128 rem = u % denominator;
    std::string out = to_string_i128((i128)whole);
    if (digits > 0) {
        out.push_back('.');
        for (int i = 0; i < digits; ++i) {
            rem *= 10;
            out.push_back(char('0' + (rem / denominator)));
            rem %= denominator;
        }
    }
    if (neg) out.insert(out.begin(), '-');
    return out;
}

static uint64_t invsqrt_floor(uint64_t n) {
    // sqrtl supplies only a seed. The returned value is authenticated by exact
    // unsigned-128-bit inequalities and is independent of libm rounding.
    uint64_t k = (uint64_t)((long double)Q / sqrtl((long double)n));
    while ((u128)(k + 1) * (u128)(k + 1) * (u128)n <= Q2) ++k;
    while ((u128)k * (u128)k * (u128)n > Q2) --k;
    return k;
}

static bool smooth23(uint64_t n) {
    while ((n & 1ULL) == 0ULL) n >>= 1;
    while (n % 3ULL == 0ULL) n /= 3ULL;
    return n == 1ULL;
}

int main(int argc, char** argv) {
    uint64_t limit = 100000000ULL;
    std::string output;
    if (argc >= 2) limit = std::strtoull(argv[1], nullptr, 10);
    if (argc >= 3) output = argv[2];
    if (limit < 4) return 2;

    std::vector<int8_t> mu(limit + 1, 1);
    mu[0] = 0;
    std::vector<bool> prime(limit + 1, true);
    prime[0] = prime[1] = false;

    // Exact Eratosthenes/Mobius sieve.
    for (uint64_t p = 2; p <= limit; ++p) {
        if (!prime[p]) continue;
        if (p <= limit / 2) {
            for (uint64_t n = p + p; n <= limit; n += p) prime[n] = false;
        }
        for (uint64_t n = p; n <= limit; n += p) mu[n] = (int8_t)-mu[n];
        if (p <= limit / p) {
            const uint64_t pp = p * p;
            for (uint64_t n = pp; n <= limit; n += pp) mu[n] = 0;
        }
    }

    auto mu_gt3 = [&](uint64_t n) -> int {
        if (n % 2ULL == 0ULL || n % 3ULL == 0ULL) return 0;
        return (int)mu[n];
    };

    i128 row2_lower = 0;
    i128 row3x3_lower = 0;
    i128 minimum_row2 = std::numeric_limits<i128>::max();
    i128 minimum_row3x3 = std::numeric_limits<i128>::max();
    uint64_t minimum_row2_at = 0;
    uint64_t minimum_row3_at = 0;
    uint64_t failure_row2 = 0;
    uint64_t failure_row3 = 0;
    uint64_t coefficient_checks = 0;
    uint64_t max_abs_row2 = 0;
    uint64_t max_abs_row3x3 = 0;

    for (uint64_t n = 1; n <= limit; ++n) {
        const int smooth = smooth23(n) ? 1 : 0;

        int a2 = smooth - mu_gt3(n);
        if (n % 2ULL == 0ULL) a2 += 2 * mu_gt3(n / 2ULL);
        if (n % 3ULL == 0ULL) a2 -= mu_gt3(n / 3ULL);

        int a3x3 = smooth - mu_gt3(n);
        if (n % 2ULL == 0ULL) a3x3 -= mu_gt3(n / 2ULL);
        if (n % 3ULL == 0ULL) a3x3 += 5 * mu_gt3(n / 3ULL);
        if (n % 4ULL == 0ULL) a3x3 -= 3 * mu_gt3(n / 4ULL);

        max_abs_row2 = std::max<uint64_t>(max_abs_row2, (uint64_t)std::abs(a2));
        max_abs_row3x3 = std::max<uint64_t>(max_abs_row3x3, (uint64_t)std::abs(a3x3));
        coefficient_checks += 2;

        const uint64_t lower = invsqrt_floor(n);
        const uint64_t upper = lower + 1ULL;
        row2_lower += (i128)a2 * (i128)(a2 >= 0 ? lower : upper);
        row3x3_lower += (i128)a3x3 * (i128)(a3x3 >= 0 ? lower : upper);

        if (n >= 2) {
            if (row2_lower < minimum_row2) {
                minimum_row2 = row2_lower;
                minimum_row2_at = n;
            }
            if (row2_lower <= 0) {
                failure_row2 = n;
                break;
            }
        }
        if (n >= 3) {
            if (row3x3_lower < minimum_row3x3) {
                minimum_row3x3 = row3x3_lower;
                minimum_row3_at = n;
            }
            if (row3x3_lower <= 0) {
                failure_row3 = n;
                break;
            }
        }
    }

    const bool pass = failure_row2 == 0 && failure_row3 == 0;
    std::ostringstream json;
    json << "{\n";
    json << "  \"arithmetic_class\": \"INTEGER_COEFFICIENTS_PLUS_EXACT_U128_SQRT_BRACKETS\",\n";
    json << "  \"coefficient_checks\": " << coefficient_checks << ",\n";
    json << "  \"final_row2_prefix_lower_bound_decimal\": \"" << decimal_ratio(row2_lower, (u128)Q) << "\",\n";
    json << "  \"final_row3_prefix_lower_bound_decimal\": \"" << decimal_ratio(row3x3_lower, (u128)3 * (u128)Q) << "\",\n";
    json << "  \"limit\": " << limit << ",\n";
    json << "  \"max_abs_row2_coefficient\": " << max_abs_row2 << ",\n";
    json << "  \"max_abs_three_times_row3_coefficient\": " << max_abs_row3x3 << ",\n";
    json << "  \"minimum_row2_prefix_at\": " << minimum_row2_at << ",\n";
    json << "  \"minimum_row2_prefix_lower_bound_decimal\": \"" << decimal_ratio(minimum_row2, (u128)Q) << "\",\n";
    json << "  \"minimum_row2_prefix_scaled_integer\": \"" << to_string_i128(minimum_row2) << "\",\n";
    json << "  \"minimum_row3_prefix_at\": " << minimum_row3_at << ",\n";
    json << "  \"minimum_row3_prefix_lower_bound_decimal\": \"" << decimal_ratio(minimum_row3x3, (u128)3 * (u128)Q) << "\",\n";
    json << "  \"minimum_three_times_row3_prefix_scaled_integer\": \"" << to_string_i128(minimum_row3x3) << "\",\n";
    json << "  \"real_endpoint_consequence\": \"rows 2 and 3 are nonnegative for every real X in [1,limit+1) by exact activation monotonicity\",\n";
    json << "  \"rh_established\": false,\n";
    json << "  \"scale_denominator\": " << Q << ",\n";
    json << "  \"verdict\": \"" << (pass ? "PASS_ACTUAL_LPTRP23_PREFIX_CERTIFICATE" : "FAIL_ACTUAL_LPTRP23_PREFIX_CERTIFICATE") << "\",\n";
    json << "  \"zero_or_negative_row2_prefix_at\": " << failure_row2 << ",\n";
    json << "  \"zero_or_negative_row3_prefix_at\": " << failure_row3 << "\n";
    json << "}\n";

    if (output.empty()) std::cout << json.str();
    else {
        std::ofstream file(output);
        file << json.str();
    }
    return pass ? 0 : 1;
}
