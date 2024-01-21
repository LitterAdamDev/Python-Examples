import statistics
from memory_profiler import memory_usage
import timeit



class ObjectWithSlots:
    
    __slots__ = ["x", "y"] 
    
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
 
       
def create_objects():
    return [ObjectWithSlots(i, i) for i in range (1_000_000)]


mem_values = []
time_values = []

if __name__ == '__main__':
    
    for _ in range(10):
        mem_usage_with_slots = memory_usage(create_objects, interval=0.01)
        mem_values.append(max(mem_usage_with_slots))
        
        obj = ObjectWithSlots(x=1, y=1)
        time_with_slots = timeit.timeit(lambda: (obj.x, obj.y), number=1_000_000)
        time_values.append(time_with_slots)


    print(statistics.mean(mem_values)) #223.625 vs 123.4890625
    print(statistics.mean(time_values)) #0.056488650201936254 vs 0.052037554097478275



