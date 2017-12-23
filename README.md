# Load Balancing Ant Colony Optimization:-
This algorithm uses the behaviour of ants and somehow mimics it to find the shortest path in a graph. This implementaion of LBACO is used to allocate incoming tasks to virtual machines with simulation in Cloudsim.

## Testing configurations:-
### VMs 
```
size = 10000 ------- image size (MB)

ram = 512 ------- vm memory (MB)

mips = random (500 to 1000)

bw = 1000 (can be kept random) -------- Bandwidth

pesNumber = 1 (can be kept random) -------- number of cpus

vmm = "Xen" -------- VMM name
```
### Cloudlets (Tasks in Cloudsim)
```
length = Random (100 to 1000) -------- no of instructions

fileSize = 300 (can be kept random) ----------- Input file size

outputSize = 300 

pesNumber = 1 (can be kept random) --------- No of processing elements to be used
```
## Experiment:
We created 20 Virtual machines (giving each VM a full Space shared processing element) and kpet their mips random (b/w 500 to 1000). Similarly, we created different number of cloudlets randomly allocating their lengths(no of instructions) to them. Then the DatacenterBroker was given different algorithms to use in order to allocate these tasks to VMs. The following plots were made to show the performance of the datacenter when using these different optimization techniques.

### The following are the meaning of symbols used:-
```
Q -------- multiplier for pheromone update

m --------- No of ants used

vms ---------- No of VMs used

alpha ----------- Exponent of pheromones

beta ----------- Exponent of computing capacity

gamma ------------ Exponent of Load balancing factor

rho = 0.05 (kept constant) ----------- vapourization constant for pheromone trail
```
