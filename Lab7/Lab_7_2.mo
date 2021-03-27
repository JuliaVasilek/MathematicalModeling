model Lab_7_2

parameter Real al_1 = 0.000018;
parameter Real al_2 = 0.377;

parameter Integer N = 3030;

Real n(start=24);

equation

der(n) = (al_1 + al_2 * n) * (N - n);

end Lab_7_2;
