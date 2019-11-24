"""Simulate Stopwatch Program
a. Desc -> Write a Stopwatch Program for measuring the time that elapses between
the start and end clicks
b. I/P -> Start the Stopwatch and End the Stopwatch
c. Logic -> Measure the elapsed time between start and end
d. O/P -> Print the elapsed time."""
import time
class StopWatch:
   def startstopwatch(self):
      try:
         start=int(input("Please enter 1 so start Stopwatch: "))
         start_time = time.time()
         while start==1:
            n=int(input("Please enter 0 to stop: "))
            if n==0:
               break
         elapsed_time_secs = time.time() - start_time
         print(f"{round(elapsed_time_secs,4)} sec")
      except ValueError:
         print("please read carefully whatever instruction has given to you")

st=StopWatch()
st.startstopwatch()
