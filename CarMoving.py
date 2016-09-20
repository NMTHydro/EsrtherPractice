
with open(color.csv, 'r') as data:

a = data[:,0]
b = data[;,1]
approach_traffic_light(a,b)


def approach_traffic_light(a, b):
    if a == 'green':
      continue_moving()
      else:
       if a == 'red':
          stop_moving()
       else:
           if a == 'yellow' and b == 'green':
              still_go()
           else:
               nope_dont()


def continue_moving():
    print "The light is green. GoGoGo!"

def stop_moving():
    print "The light is red. STOOOOOP!"

def still_go():
    print "Decrease the velocity, we can still go."

def nope_dont():
    print "Ready to stop."

