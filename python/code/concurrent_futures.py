from concurrent.futures import ThreadPoolExecutor, as_completed, wait
from concurrent.futures import Future
import time

def get_htm(times):
    time.sleep(times)
    print('times: %s' % times)
    return times

executor = ThreadPoolExecutor(max_workers=2)

urls = [3, 2, 4]
all_tasks = [executor.submit(get_htm, item) for item in urls]
wait(all_tasks, return_when=ALL_C)
print('done')
for future in as_completed(all_tasks):
    data = future.result()
    print('get {data} success'.format(data=data))


# for data in executor.map(get_htm, urls):
#     print('get {data} success'.format(data=data))

# task1 = executor.submit(get_htm, (3))
# task2 = executor.submit(get_htm, (2))
# print(task1.done())
# print(task2.cancel())
# time.sleep(3)
# print(task1.done())