x=linspace(0,3);
y=94.*power(cos(x), 3) - 24.*cos(x) + 177.*power(sin(x), 2) - 108.*power(sin(x), 4) - 72.*power(cos(x), 3).*power(sin(x), 2) - 65;
grid on;
hold on;
plot(x,y)