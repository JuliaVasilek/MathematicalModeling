model Lab_7_3

parameter Real al_1 = 0.1;
parameter Real al_2 = 0.4;

parameter Integer N = 3030;

Real n(start=24);

equation

der(n) = (al_1 * time + al_2 * cos(time) * n) * (N - n);

end Lab_7_3;
