#include <algorithm>
#include <cmath>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <vector>

struct PrimePower {
    std::uint64_t n;
    long double lambda;
};

struct Event {
    std::uint64_t t;
    long double delta;
    bool operator<(const Event &other) const {
        return t < other.t || (t == other.t && delta < other.delta);
    }
};

static long double inv_integral(long double left, long double right) {
    if (!(right > left)) return 0.0L;
    return 1.0L / left - 1.0L / right;
}

static std::vector<PrimePower> build_prime_powers(int limit) {
    std::vector<bool> prime(limit + 1, true);
    prime[0] = prime[1] = false;
    for (int p = 2; 1LL * p * p <= limit; ++p) {
        if (!prime[p]) continue;
        for (long long n = 1LL * p * p; n <= limit; n += p) {
            prime[static_cast<std::size_t>(n)] = false;
        }
    }

    std::vector<PrimePower> rows;
    rows.reserve(700000);
    for (int p = 2; p <= limit; ++p) {
        if (!prime[p]) continue;
        const long double logp = logl(static_cast<long double>(p));
        std::uint64_t n = static_cast<std::uint64_t>(p);
        while (n <= static_cast<std::uint64_t>(limit)) {
            rows.push_back({n, logp});
            if (n > static_cast<std::uint64_t>(limit) /
                        static_cast<std::uint64_t>(p)) {
                break;
            }
            n *= static_cast<std::uint64_t>(p);
        }
    }
    std::sort(
        rows.begin(), rows.end(),
        [](const PrimePower &left, const PrimePower &right) {
            return left.n < right.n;
        });
    return rows;
}

struct ScaleResult {
    int scale;
    std::vector<long double> energy;
    std::vector<long double> diagonal;
};

static ScaleResult run_scale(
    const std::vector<PrimePower> &rows,
    int scale,
    int first_block,
    int last_block) {

    const long double max_t = expl(static_cast<long double>(last_block + 1));
    std::vector<Event> events;
    events.reserve(rows.size() * 2);

    for (const auto &row : rows) {
        if (static_cast<long double>(row.n) <= max_t) {
            events.push_back({row.n, row.lambda});
        }
        if (row.n <= UINT64_MAX / static_cast<std::uint64_t>(scale)) {
            const std::uint64_t shifted =
                row.n * static_cast<std::uint64_t>(scale);
            if (static_cast<long double>(shifted) <= max_t) {
                events.push_back(
                    {shifted, -static_cast<long double>(scale) * row.lambda});
            }
        }
    }
    std::sort(events.begin(), events.end());

    std::vector<long double> energy(last_block + 1, 0.0L);
    long double value = 0.0L;
    std::size_t index = 0;
    long double cursor = expl(static_cast<long double>(first_block));

    while (index < events.size() &&
           static_cast<long double>(events[index].t) <= cursor) {
        const std::uint64_t t = events[index].t;
        long double delta = 0.0L;
        while (index < events.size() && events[index].t == t) {
            delta += events[index].delta;
            ++index;
        }
        value += delta;
    }

    for (int block = first_block; block <= last_block; ++block) {
        const long double right =
            expl(static_cast<long double>(block + 1));
        while (index < events.size() &&
               static_cast<long double>(events[index].t) < right) {
            const std::uint64_t event_integer = events[index].t;
            const long double event =
                static_cast<long double>(event_integer);
            energy[block] +=
                value * value * inv_integral(cursor, event);
            cursor = event;

            long double delta = 0.0L;
            while (index < events.size() &&
                   events[index].t == event_integer) {
                delta += events[index].delta;
                ++index;
            }
            value += delta;
        }

        energy[block] += value * value * inv_integral(cursor, right);
        cursor = right;

        while (index < events.size() &&
               static_cast<long double>(events[index].t) <= cursor) {
            const std::uint64_t t = events[index].t;
            long double delta = 0.0L;
            while (index < events.size() && events[index].t == t) {
                delta += events[index].delta;
                ++index;
            }
            value += delta;
        }
    }

    std::vector<long double> diagonal(last_block + 1, 0.0L);
    for (const auto &row : rows) {
        const long double n = static_cast<long double>(row.n);
        const long double scaled_n = static_cast<long double>(scale) * n;
        const long double weight_squared = row.lambda * row.lambda;

        for (int block = first_block; block <= last_block; ++block) {
            const long double left = expl(static_cast<long double>(block));
            const long double right =
                expl(static_cast<long double>(block + 1));

            const long double first_left = std::max(left, n);
            const long double first_right = std::min(right, scaled_n);
            if (first_right > first_left) {
                diagonal[block] += weight_squared *
                    inv_integral(first_left, first_right);
            }

            const long double tail_left = std::max(left, scaled_n);
            if (right > tail_left) {
                const long double coefficient =
                    1.0L - static_cast<long double>(scale);
                diagonal[block] +=
                    weight_squared * coefficient * coefficient *
                    inv_integral(tail_left, right);
            }
        }
    }

    return {scale, energy, diagonal};
}

int main() {
    constexpr int limit = 10000000;
    constexpr int first_block = 2;
    constexpr int last_block = 15;
    const std::vector<int> scales = {2, 3, 4, 5, 8, 16};

    const auto rows = build_prime_powers(limit);
    std::vector<ScaleResult> results;
    for (int scale : scales) {
        results.push_back(
            run_scale(rows, scale, first_block, last_block));
    }

    std::cout << std::setprecision(18);
    std::cout << "{\n";
    std::cout << "  \"classification\": "
              << "\"LONG_DOUBLE_RECONNAISSANCE\",\n";
    std::cout << "  \"prime_limit\": " << limit << ",\n";
    std::cout << "  \"prime_power_count\": " << rows.size() << ",\n";
    std::cout << "  \"complete_blocks\": ["
              << first_block << ", " << last_block << "],\n";
    std::cout << "  \"scale4_rows\": [\n";

    const auto &scale_four = results[2];
    for (int block = first_block; block <= last_block; ++block) {
        const long double off_diagonal =
            scale_four.energy[block] - scale_four.diagonal[block];
        std::cout << "    {\"j\": " << block
                  << ", \"total\": "
                  << static_cast<double>(scale_four.energy[block])
                  << ", \"diagonal\": "
                  << static_cast<double>(scale_four.diagonal[block])
                  << ", \"off_diagonal\": "
                  << static_cast<double>(off_diagonal)
                  << ", \"total_over_diagonal\": "
                  << static_cast<double>(
                         scale_four.energy[block] /
                         scale_four.diagonal[block])
                  << "}";
        std::cout << (block == last_block ? "\n" : ",\n");
    }

    std::cout << "  ],\n";
    std::cout << "  \"scale_summary_j5_j15\": [\n";
    for (std::size_t index = 0; index < results.size(); ++index) {
        const auto &result = results[index];
        long double total_sum = 0.0L;
        long double ratio_sum = 0.0L;
        int count = 0;
        for (int block = 5; block <= last_block; ++block) {
            total_sum += result.energy[block];
            ratio_sum += result.energy[block] / result.diagonal[block];
            ++count;
        }

        std::cout << "    {\"scale\": " << result.scale
                  << ", \"mean_total\": "
                  << static_cast<double>(total_sum / count)
                  << ", \"mean_total_over_diagonal\": "
                  << static_cast<double>(ratio_sum / count)
                  << ", \"last_total\": "
                  << static_cast<double>(result.energy[last_block])
                  << ", \"last_diagonal\": "
                  << static_cast<double>(result.diagonal[last_block])
                  << ", \"last_ratio\": "
                  << static_cast<double>(
                         result.energy[last_block] /
                         result.diagonal[last_block])
                  << "}";
        std::cout << (index + 1 == results.size() ? "\n" : ",\n");
    }

    std::cout << "  ],\n";
    std::cout << "  \"proof_boundary\": "
              << "\"Complete prime-power enumeration through 1e7; "
              << "integer event sweep and long-double exact-cell "
              << "antiderivatives. Discovery only: no outward rounding "
              << "or independent compiler replay. Blocks j=2,...,15 are "
              << "complete.\"\n";
    std::cout << "}\n";
}
