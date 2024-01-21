import statistics
from memory_profiler import memory_usage
import timeit



class ObjectWithoutSlots:
    
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
 
       
def create_objects():
    return [ObjectWithoutSlots(i, i) for i in range (1_000_000)]


mem_values = []
time_values = []

if __name__ == '__main__':
    
    for _ in range(10):
        mem_usage_without_slots = memory_usage(create_objects, interval=0.01)
        mem_values.append(max(mem_usage_without_slots))
        
        obj = ObjectWithoutSlots(x=1, y=1)
        time_without_slots = timeit.timeit(lambda: (obj.x, obj.y), number=1_000_000)
        time_values.append(time_without_slots)


    print(statistics.mean(mem_values)) #223.625
    print(statistics.mean(time_values)) #0.056488650201936254



