import pandas as pd
import multiprocessing
from thirdclass import calculate_mean
import time

def parallel_process(obj, df):
    print(obj)
    print(df.mean())

print(multiprocessing.cpu_count())
print(os.cpu_count())
print(len(os.sched_getaffinity(0)))
    
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
num_cores = multiprocessing.cpu_count()
obj = "Proceso empezado "
pool = multiprocessing.Pool(num_cores)
chunk_size = int(df.shape[0] / num_cores)
chunks = [df.iloc[i:i + chunk_size] for i in range(0, df.shape[0], chunk_size)]
data = [(obj, chunk) for chunk in chunks]
pool.starmap(parallel_process, data)
pool.close()
result = pool.join()
print(result)
