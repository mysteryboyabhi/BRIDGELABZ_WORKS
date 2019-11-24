from sys import argv
def m_payment(P,Y,R):
    if Y==0 or R==0:
        return "Sorry year and rate can't be zero"
    n = 12*Y
    r = R/(12*100)
    payment=P*r/(1-(1+r)**(-n))
    return round(payment, 4)

P,Y,R=map(float,input("Enter value of P,Y and R: ").split())
print(m_payment(P,Y,R))