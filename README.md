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

For implementaion code see - [here](/implementaion/)

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
## Plots
![Plot1](/png1/3.png)
As we increase the number of ants, The variance increases,
![Plot2](/png1/1.png) ![Plot3](/png1/2.png)

As we change values of alpha, beta, gamma:-

[Plot4](/png1/7.png)
[Plot5](/png/10.png) 
[Plot6](/png1/8.png) 
[Plot7](/png1/11.png) 
[Plot8](/png1/6.png) 
[Plot9](/png1/14.png)

## Some observations:
Plots show that:
1. Value of alpha should be low.
2. Value of beta should be lower than alpha.
3. Value of gamma should be high.
4. Number of ants(m) must be kept b/w `vms` and `2*vms` where vms -- Number of VMs used.

## References used:
[Dynamic Task Scheduling Algorithm based
on Ant Colony Scheme](https://www.google.co.in/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwi0p5vnj6LYAhUGPY8KHUTbA0oQFggsMAA&url=https%3A%2F%2Fpdfs.semanticscholar.org%2F082c%2F6b5926f23b9df35ee5c1629528e85bfc7b2a.pdf&usg=AOvVaw2N6UL_dVoTWFgqFOdMl2H5)
Kamolov Nizomiddin Baxodirjonovich , Tae-Young Choe
Department of IT Convergence Engineering,
Kumoh National Institute of Technology,
Daehak-ro, Gumi, Gyeongbuk, South Korea
