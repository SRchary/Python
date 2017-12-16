import time
import threading as th

start_time = time.time()

def squar(param):

    for i in param:
        time.sleep(0.2)
        print "square start"
        print i*i

def cube(param):
    
    for i in param:
        time.sleep(0.2)
        print "cube start"
        print i*i*i

lst =[ i for i in range(100)]

t1 = th.Thread(target = squar ,args =( lst ,) )
t2 = th.Thread(target = cube ,args =( lst ,) )

t1.start()
t2.start()
t1.join()
t2.join()


#squar(lst)
#cube(lst)
print time.time()-start_time


        
