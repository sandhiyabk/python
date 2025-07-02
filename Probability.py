import random
import matplotlib.pyplot as plt
def toss():
    return random.choice(['Heads','Tails'])
results=[toss() for _ in range(1000)]
head_prob=results.count("Heads")/len(results)
tail_prob=results.count("Tails")/len(results)
#print(results)
print(" P(Heads) :",head_prob)
print(" P(Tails) :",tail_prob)
labels =['Heads','Tails']
values=[head_prob,tail_prob]
plt.bar(labels,values,color=['pink','green'])
plt.title("Coin Toss Probability")
plt.ylabel('Probabilty')
plt.show()
