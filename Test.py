UserInput = input("月利润")
money = int(UserInput)
print(type(money))
def work(request):
    if request<=100000:
        print(request*0.1)
    if 100000<request>200000:
        print((request-100000)*0.075+10000)
    if 200000<request>400000:
        print((request-200000)*0.05+17500)
    if 400000<request>600000:
        print((request-400000)*0.03+27500)
    if 600000<request>1000000:
        print((request-600000)*0.015+33500)
    if request>1000000:
        print((request-1000000)*0.001+39500)
work(money)
