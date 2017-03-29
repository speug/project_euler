l = range(1,101)
ssq = sum(l)*sum(l)
sqs = sum(map(lambda x: x*x,l))
print((ssq-sqs))
