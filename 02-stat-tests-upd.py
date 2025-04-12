import numpy as np
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest

### problem 01 ###

server1 = [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 
           0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
           0, 1, 0, 1, 0, 0, 0, 0, 0, 0]

server2 = [0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 
           0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 
           0, 0, 0, 1, 0, 0, 0, 1, 0, 0,
           0, 1]

s1, s2 = sum(server1), sum(server2)
n1, n2 = len(server1), len(server2)

print("Конверсия 1:", s1 / n1)
print("Конверсия 2:", s2 / n2)

print(proportions_ztest(count = [s1, s2], 
                        nobs = [n1, n2], 
                        alternative = "smaller"))

stat, pvalue = proportions_ztest(count = [s1, s2], 
                                 nobs = [n1, n2], 
                                 alternative = "smaller")

# дополнение
alpha = float(input("Введите уровень значимости: "))
if pvalue > alpha:
    print(f"H0 не отвергается, p-value {pvalue:.3f}")
else:
    print(f"H0 отвергается, p-value {pvalue:.3f}")

### problem 02 ###

poll = np.array([3, 4, 1, 2, 3, 4, 2, 1, 3, 4,
                 1, 2, 4, 3, 1, 2, 3, 4, 3, 4])
print(poll >= 3)

yes = (poll >= 3).sum()
N = poll.size
print(stats.binom_test(x = yes, n = N, p = 0.4))

### problem 03 ###

weight_a = np.array([3, 2.5, 4, 3.5, 4, 4,5, 3.8, 2.7, 1.9, 3.1, 3])
weight_b = np.array([-0.5, 2, 2.5, 3, 4, 4.6, 3.2, 0, 1.5, 1.4, 3.2, 2.2, 0])

print("среднее:", round(weight_a.mean(), 2), 
      "стандартное отклонение:", round(weight_a.std(ddof = 1), 2))

print("среднее:", round(weight_b.mean(), 2), 
      "стандартное отклонение:", round(weight_b.std(ddof = 1), 2))

stats.ttest_ind(weight_a, weight_b, alternative = "greater")

