'''input=20
output=AABBC(shortest num)
A=1
B=2(A)+A
C=3(B)+B
upto Z'''




num=1
num1=2
alpha1=[]
for i in range(26):
    alpha1.append(num)
    num=num1*num+num
    num1+=1
alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
weight=75
max=0
res=[]
result=dict(zip(alpha1,alpha))
# for i in range(len(alpha1)):
while(weight>0):
    for i in range(len(alpha1)):
        
        if(alpha1[i]>=weight):
            if(alpha1[i]==weight):
                max=alpha1[i]
            elif(alpha1[i-1]<=weight):
                max=alpha1[i-1]
                res.append(result[max])
                weight=weight-max

        
res.reverse()
for i in res:
    print(i,end="")
