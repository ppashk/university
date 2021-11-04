P = -21:.1:21;
T = cos(P+0.05*4)+0.04;


plot(P,T,'*r', 'MarkerSize',4,'LineWidth',2)
hold on 
grid on

net = newrb(P,T);
V = sim(net,P);
%plot(P,V,'ob','MarkerSize',5, 'LineWidth',2,P,T,'ob','MarkerSize',5,'LineWidth',2)
plot(P,V,P,T)
legend('V', 'T')
xlabel('P')
ylabel('V, T')

p = -3:.5:2;
t = cos(p+0.05*4)+0.04;
v = sim(net,p);
plot(p,v,p,t)
