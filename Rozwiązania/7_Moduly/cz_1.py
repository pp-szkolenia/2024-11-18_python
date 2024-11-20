import time
from functions import modulo


start = time.perf_counter()
result = modulo(12, 5)
end = time.perf_counter()

print("Czas wykonywania: ", end-start)
