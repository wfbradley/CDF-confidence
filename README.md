CDF-confidence
==============

These python tools allow users to compute and/or plot (empirical) CDFs with confidence intervals.

Currently, the code uses an analytic technique equivalent to bootstrap resampling.  We should extend this
to include:
  (1) Confidence bands versus pointwise confidence intervals
  (2) Include an option to use the Dvoretzky-Kiefer-Wolfowitz inequality
  (3) Include an option for the error from the (inverse of the) Kolmovorov-Smirnov test

It seems that the Komlós–Major–Tusnády approximation offers a pretty good quantitive
bound (see also the Donsker theorem), although it's not clear that the constants are explicit.

