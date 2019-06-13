## (sensori-neuro-actuator)-(mechano-enviro) systems (SNA-ME)

SNA forms a sensorimotor loop

```python

class SNA_loop():
    '''Construct a sensorimotor loop
    Abstract Nodal Network Loop Object 
    '''
    def __init__(self, tau):
        self.tau_description = '''a single number quantifying loop time
                                  for a point in loop it is the time-delay
                                  IMPORTANT: carefully consider reference before defining time-delay
                                  
                                  Loops are directed as DAGS, Where nodes are at
                                  Steady State with stochastic functionality
                                  
                                  '''
        



```

I am interested in **sensori-neuro-actuator** (SNA) systems that include:

+ purely biological SNA systems
  + e.g. neurosensory and neuromuscular biomechanical systems
+ purely non-biological SNA Systems 
  + e.g. silicon computing systems, robotic systems
+ hybridization of biological-non-biological SNA systems (BNB hybrdization)

From Delp to Susskind:

modular SNA nodes have time-index flux through defined **2D boundary**

### sensori:

listens for informative inputs encoded in a finite alphabet

### neuro-, nodal-; neurons and nodes; both types of vertex

a computing system that internally comprises well-defined computing **modules**.

#### modules: a vertex within a vertex

defined as a set of physical states
contained by a **spatiotemporal boundary B**

**inputs and outputs (I/O)**: discrete signal time-indexed threads
fluxing through **B**

graph edge: relation type: {connection, communication} (between modules)

### actuator:

To actuate is to influence, to change the physical state of. 

communication is a transmitter-actuation on a receiver

hybridizing computational and actuative systems is what robotics is all about.

Understanding this hybridization in neuromuscular systems and
how synthetic materials, both computational, actuative, sensorial,
and bulk-mechanical type 



