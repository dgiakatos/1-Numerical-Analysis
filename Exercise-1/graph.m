x=linspace(0,3);
y=14*x.*exp(x-2) - 12.*exp(x-2) - 7*power(x,3) + 20*power(x,2) - 26*x + 12;
grid on;
hold on;
plot(x,y)