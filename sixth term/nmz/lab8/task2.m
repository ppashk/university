P = [0.2 1 1.8 2.6 3.4 4.2 5 5.8 6.6 7.4 8.2];
T = [1.18006 0.74030 -0.02720 -0.65688 -0.76679 -0.29026 0.483662185 1.085519 1.15023 0.63854 -0.13915];
plot(P,T,'*r', 'MarkerSize',4,'LineWidth',2)
hold on 
grid on

net = newrbe(P,T);
disp(net.layers.size)

V = sim(net,P);
plot(P,V,'ob','MarkerSize',5, 'LineWidth',2)

p = [0.6 1.6 2.3 4.0 6.5];
v = sim(net,p);
plot(p,v,'+k','MarkerSize',10, 'LineWidth',2)
grid on