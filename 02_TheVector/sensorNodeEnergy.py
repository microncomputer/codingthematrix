from vec_draft import Vec

'''
Example 2.9.7: Sensor node energy utilization: Sensor networks are made up of small, cheap
sensor nodes. Each sensor node consists of some hardware components (e.g., radio, temperature
sensor, memory, CPU). Often a sensor node is battery-driven and located in a remote place, so
designers care about each component’s power consumption.
'''

# domain: elements of a sensor node
D = {'radio', 'sensor', 'memory', 'CPU'}

# function vector mapping components to their power consumption
rate = Vec(D, {'memory':0.06, 'radio':0.1, 'sensor':0.004, 'CPU':0.0025})

# function vector mapping components to amount of time on during test period
duration = Vec(D, {'memory':1.0, 'radio':0.2, 'sensor':0.5, 'CPU':1.0})

energyConsumed = rate*duration
print(energyConsumed)


'''

'''