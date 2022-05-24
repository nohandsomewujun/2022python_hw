import recognize
import sys
import time

start_time = time.time()

if sys.argv[1] == '-sort_k':
    recognize.sort_by_known(sys.argv[2], sys.argv[3])
elif sys.argv[1] == '-auto_sort':
    recognize.auto_sort(sys.argv[2], sys.argv[3])


end_time = time.time()
print("Tatal time {:.2f}s".format(end_time - start_time))
