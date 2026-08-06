#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <vector>

namespace {
constexpr int LIMIT = 10000000;
constexpr int FIRST_BLOCK = 2;
constexpr int LAST_BLOCK = 16;
constexpr int LAYERS = 5;

struct Event {
    long double x;
    int channel;
    long double delta_slope;
    bool operator<(const Event& other) const {
        if (x != other.x) return x < other.x;
        return channel < other.channel;
    }
};

long double phi(long double t) {
    if (t < 0.0L || t > 2.0L) return 0.0L;
    return t <= 1.0L ? t : 2.0L - t;
}

long double G(long double t) {
    const long double h = logl(4.0L);
    return phi(t - 1.0L) - 2.0L * phi(t - 1.0L - h);
}

long double H(long double t) { return G(t) - G(t - 1.0L); }

int layer_for_exponent(int exponent) {
    if (exponent <= 4) return exponent - 1;
    return 4;
}

void append_piecewise_linear_events(std::vector<Event>& events,
                                    long double logn,
                                    long double weight,
                                    int channel,
                                    bool boundary_difference) {
    const long double h = logl(4.0L);
    const long double locations[6] = {
        logn + 1.0L, logn + 2.0L, logn + 3.0L,
        logn + 1.0L + h, logn + 2.0L + h, logn + 3.0L + h};
    const long double changes[6] = {1, -2, 1, -2, 4, -2};
    for (int k = 0; k < 6; ++k) {
        events.push_back({locations[k], channel, weight * changes[k]});
        if (boundary_difference) {
            events.push_back({locations[k] + 1.0L, channel,
                              -weight * changes[k]});
        }
    }
}

long double pair_integral(long double a, long double da,
                          long double b, long double db,
                          long double dt) {
    return a * b * dt
         + (a * db + b * da) * dt * dt / 2.0L
         + da * db * dt * dt * dt / 3.0L;
}
}  // namespace

int main() {
    std::vector<bool> is_prime(LIMIT + 1, true);
    is_prime[0] = is_prime[1] = false;
    for (int p = 2; 1LL * p * p <= LIMIT; ++p) {
        if (!is_prime[p]) continue;
        for (long long n = 1LL * p * p; n <= LIMIT; n += p) {
            is_prime[static_cast<size_t>(n)] = false;
        }
    }

    std::vector<Event> layer_events;
    std::vector<Event> prime_difference_events;
    layer_events.reserve(4000000);
    prime_difference_events.reserve(2000000);
    long long prime_power_count = 0;

    for (int p = 2; p <= LIMIT; ++p) {
        if (!is_prime[p]) continue;
        const long double logp = logl(static_cast<long double>(p));
        long long n = p;
        int exponent = 1;
        while (n <= LIMIT) {
            const long double logn = logl(static_cast<long double>(n));
            const long double weight = logp / sqrtl(static_cast<long double>(n));
            append_piecewise_linear_events(
                layer_events, logn, weight, layer_for_exponent(exponent), false);
            if (exponent == 1) {
                append_piecewise_linear_events(
                    prime_difference_events, logn, weight, 0, true);
            }
            ++prime_power_count;
            if (n > LIMIT / p) break;
            n *= p;
            ++exponent;
        }
    }

    std::sort(layer_events.begin(), layer_events.end());
    std::sort(prime_difference_events.begin(), prime_difference_events.end());

    std::array<std::array<std::array<long double, LAYERS>, LAYERS>,
               LAST_BLOCK + 1> gram{};
    std::array<long double, LAST_BLOCK + 1> prime_difference_energy{};

    {
        std::array<long double, LAYERS> value{};
        std::array<long double, LAYERS> slope{};
        long double previous = layer_events.front().x;
        size_t index = 0;

        auto integrate_to = [&](long double right) {
            long double cursor = previous;
            while (cursor < right) {
                int block = static_cast<int>(floorl(cursor));
                long double endpoint = std::min(right,
                                                static_cast<long double>(block + 1));
                long double dt = endpoint - cursor;
                if (block >= FIRST_BLOCK && block <= LAST_BLOCK) {
                    for (int a = 0; a < LAYERS; ++a) {
                        for (int b = 0; b < LAYERS; ++b) {
                            gram[block][a][b] += pair_integral(
                                value[a], slope[a], value[b], slope[b], dt);
                        }
                    }
                }
                for (int a = 0; a < LAYERS; ++a) value[a] += slope[a] * dt;
                cursor = endpoint;
            }
            previous = right;
        };

        while (index < layer_events.size()) {
            long double location = layer_events[index].x;
            if (location > LAST_BLOCK + 1.0L) break;
            integrate_to(location);
            while (index < layer_events.size()
                   && fabsl(layer_events[index].x - location) < 1e-18L) {
                slope[layer_events[index].channel] +=
                    layer_events[index].delta_slope;
                ++index;
            }
        }
        integrate_to(static_cast<long double>(LAST_BLOCK + 1));
    }

    {
        long double value = 0.0L;
        long double slope = 0.0L;
        long double previous = prime_difference_events.front().x;
        size_t index = 0;

        auto integrate_to = [&](long double right) {
            long double cursor = previous;
            while (cursor < right) {
                int block = static_cast<int>(floorl(cursor));
                long double endpoint = std::min(right,
                                                static_cast<long double>(block + 1));
                long double dt = endpoint - cursor;
                if (block >= FIRST_BLOCK && block <= LAST_BLOCK) {
                    prime_difference_energy[block] +=
                        pair_integral(value, slope, value, slope, dt);
                }
                value += slope * dt;
                cursor = endpoint;
            }
            previous = right;
        };

        while (index < prime_difference_events.size()) {
            long double location = prime_difference_events[index].x;
            if (location > LAST_BLOCK + 1.0L) break;
            integrate_to(location);
            long double change = 0.0L;
            while (index < prime_difference_events.size()
                   && fabsl(prime_difference_events[index].x - location) < 1e-18L) {
                change += prime_difference_events[index].delta_slope;
                ++index;
            }
            slope += change;
        }
        integrate_to(static_cast<long double>(LAST_BLOCK + 1));
    }

    std::cout << std::setprecision(18);
    std::cout << "{\n  \"classification\": \"LONG_DOUBLE_RECONNAISSANCE\",\n";
    std::cout << "  \"prime_limit\": " << LIMIT << ",\n";
    std::cout << "  \"prime_power_count\": " << prime_power_count << ",\n";
    std::cout << "  \"blocks\": [\n";
    for (int j = FIRST_BLOCK; j <= LAST_BLOCK; ++j) {
        long double total = 0.0L;
        for (int a = 0; a < LAYERS; ++a)
            for (int b = 0; b < LAYERS; ++b) total += gram[j][a][b];
        std::cout << "    {\"j\": " << j
                  << ", \"total\": " << static_cast<double>(total)
                  << ", \"prime_energy\": "
                  << static_cast<double>(gram[j][0][0])
                  << ", \"square_energy\": "
                  << static_cast<double>(gram[j][1][1])
                  << ", \"twice_prime_square\": "
                  << static_cast<double>(2 * gram[j][0][1])
                  << ", \"prime_boundary_difference_energy\": "
                  << static_cast<double>(prime_difference_energy[j]) << "}";
        std::cout << (j == LAST_BLOCK ? "\n" : ",\n");
    }
    std::cout << "  ],\n";
    std::cout << "  \"proof_boundary\": \"Complete 1e7 manifest and deterministic long-double event integration; discovery only, not directed.\"\n}\n";
    return 0;
}
