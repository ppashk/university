net=newff([0.5 10],[15 1],{'tansig' 'purelin'});
init(net);
%xtrain = linspace(0.5,10,100);
xtrain = .5:.1:10;

ytrain = (x - 1).cos(3*xtrain - 15);
net.trainParam.epochs = 10;
[net,TR,Y,E]=train(net,xtrain(1:67),ytrain(1:67));

yprediction=sim(net,xtrain);
 
plot(xtrain,ytrain,'o',xtrain,yprediction,'r-');
hold on
xlabel('x');
ylabel('y');
 
%plot(xtrain,yprediction,);
 
hold off

