#Q1 Create a threading process such that it sleeps for 5 seconds and then prints out a message.

import threading
from threading import Thread
import time
def display():
    time.sleep(5)
    print("Child Thread:",threading.current_thread().getName())


t=Thread(target=display)
t.setName("My thread........")
t.start()

print("Main thread executing:",threading.current_thread())


import threading


#Q2 Make a thread that prints numbers from 1-10, waits for 1 sec between
from threading import Thread
import time
def show(n):
        for x in range(n):
            time.sleep(1)
            print(threading.current_thread().getName(),x)

n=10
x=Thread(target=show,args=(n,))
x.start()
print("Main thread executing:",threading.current_thread())


#Q3. Make a list that has 5 elements.
# Create a threading process that prints the 5 elements of the list
#  with a delay of multiple of 2 sec between each display.
#Delay goes like 2sec-4sec-6sec-8sec-10sec

import threading
from threading import Thread
import time
def count():
    m=2
    for x in l:
        print(x)
        time.sleep(m)
        m=m+2


l=[5,3,1,8,9,4]
b=Thread(target=count)
b.start()

#Q4 Call factorial function using thread.

import threading
from threading import Thread
def fact():
    x=int(input("enter the number: "))
    fact=1
    for a in range(1,x+1):
         fact=fact*a
    print(fact)

t1=Thread(target=fact)
t1.start()