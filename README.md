# Load Balancing Ant Colony Optimization:-
This algorithm uses the behaviour of ants and somehow mimics it to find the shortest path in a graph. This implementaion of LBACO is used to allocate incoming tasks to virtual machines withh simulation in Cloudsim.

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
