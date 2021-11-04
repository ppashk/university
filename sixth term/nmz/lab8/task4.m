p = -3:0.1:3;
a1 = radbas(p);
a2 = radbas(p-1.5);
a3 = radbas(p+2);
a = a1 + a2*1 + a3*0.5;
plot(p,a1,p,a2,p,a3*0.5,p,a)