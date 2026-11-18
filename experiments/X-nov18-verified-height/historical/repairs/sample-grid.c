/* Insert after Platt's Gaussian removal, before its original Turing call.
 * Print a sign on the subdivided time grid. Arb enclosure must exclude zero.
 */
{
  arb_t grid_point, sample;
  arb_init(grid_point);
  arb_init(sample);
  printf("Grid signs /8:");
  for (int64_t tick = 0; tick <= 8 * int_step; ++tick) {
    int64_t base = N/2 - int_step/2 + tick/8;
    if (tick % 8 == 0)
      arb_set(sample, acb_realref(f_vec[base]));
    else {
      arb_set_si(grid_point, 8 * base + (tick % 8));
      arb_mul_2exp_si(grid_point, grid_point, -3);
      arb_inter_t(sample, NULL, f_vec, grid_point, prec);
    }
    putchar(arb_is_positive(sample) ? '+' : arb_is_negative(sample) ? '-' : '?');
  }
  putchar('\n');
  arb_clear(grid_point);
  arb_clear(sample);
}
