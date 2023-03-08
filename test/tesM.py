import pandas as pd
import multiprocessing
from thirdclass import calculate_mean
import time

def parallel_process():
    df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
    num_cores = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(num_cores)
    obj = 'Proceso comenzado'
    chunk_size = int(df.shape[0] / num_cores)
    chunks = [df.iloc[i:i + chunk_size] for i in range(0, df.shape[0], chunk_size)]
    data = [(obj, chunk) for chunk in chunks]
    pool.starmap(calculate_mean, data)
    pool.close()
    pool.join()
    return ('finished')


