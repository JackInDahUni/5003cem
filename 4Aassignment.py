import math
import concurrent.futures
from datetime import datetime
values = [12,20,4,100,64,77,200,9,10]

def mycosine(n):
    return math.cos(n)

def non_concurrent_cosines():
    for val in values:
        res = mycosine(val)
        print('Cosine of %s is %s' % (val,res), '\n')

def concurrentCosines():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [(executor.submit(mycosine, val), val) for val in values]
        results = [future.result() for future, _ in futures]
        sorted_results = [result for _, result in sorted(zip(values, results), key=lambda x: values.index(x[0]))]
        for val, result in zip(values, sorted_results):
            print('Cosine of %s is %s' % (val, result))

if __name__ == '__main__':
	startTime = datetime.now()
	concurrentCosines()
	endTime = datetime.now()
	elapsedTime = endTime - startTime
	print("Elapesd time: ", elapsedTime)