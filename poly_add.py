class polynomial:
    def __init__(self,coeffs):
        self.coeffs=coeffs
    def evaluate(self,x):
        result=0
        for exp,coeff in self.coeffs.items():
            result+=coeff*(x**exp)
        return result
    def __add__(self,other):
        result_coeff={}
        for exp,coeff in self.coeffs.items():
            result_coeff[exp]=coeff
        for exp,coeff in other.coeffs.items():
            result_coeff[exp]=result_coeff.get(exp,0)+coeff
        return polynomial(result_coeff)
    def __str__(self):
        terms=[]
        for exp,coeff in self.coeffs.items():
            if exp==0:
                term=str(coeff)
            elif exp==1:
                term=f"{coeff}x"
            else:
                term=f"{coeff}x^{exp}"
            terms.append(term)
        return "+".join(terms)
poly1=polynomial({2:3,1:2,0:5})
poly2=polynomial({2:2,1:-1,0:3})
sum_poly=poly1+poly2
print("poly1 is",poly1)
print("poly2 is",poly2)
print("sum poly is",sum_poly)
x=2
print("poly1 at {x}",poly1.evaluate(x))
print("poly2 at {x}",poly2.evaluate(x))
print("sum poly at {x}",sum_poly.evaluate(x))



