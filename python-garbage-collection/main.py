import sys
import gc
import dis
import time

#gc.set_debug(True)
#gc.set_threshold(20000, 50, 100)
gc.disable()
class Link:

    def __init__(self, next_link, value) -> None:
        self.next_link = next_link
        self.value = value
        
    def __repr__(self) -> str:
        return self.value


l = Link(None, "Main")
link_list = []

start = time.perf_counter()

for i in range(5_000_000):
    tmp_link = Link(l, "Link")
    link_list.append(tmp_link)

end = time.perf_counter()

print(end - start)


print(gc.get_count())    
gc.collect(2) #delete up-to generation 2 / all 3 generations
print(gc.get_count()) 
# Will return the number of references in the byte code, not the actual code
#print(sys.getrefcount(a)) 
#print(gc.get_referents(a))

# get the byte code to see where the references are
#print(dis.dis(compile("sys.getrefcount(a)", "", "single")))

#print(gc.get_threshold())
print(gc.get_threshold()) #700, 10, 10
# (threshold0) 700 = number_of_alloc - num_of_delloc since the last collection
# (threshold1) 10 = 10 times generation 0 were collected since the last collection of generation 1
# (threshold2) 10 = long_lived_pending / long_lived_total (hardwritten to 25%)
# - We will only collect generation 2 if we hit the counter and the ratio as well