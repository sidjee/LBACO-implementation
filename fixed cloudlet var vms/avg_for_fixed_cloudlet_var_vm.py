import os, subprocess
import time, sys

#command1 = 'javac Try2.java && java org.cloudbus.cloudsim.examples.Try2'
#output = subprocess.check_output(command1, shell=True)
#print output[len(output)-33:-28]
# Conclusion Example 4 is best and used

if len(sys.argv) != 3 :
	print "Usage python avg.py <file_name> <no_of_times>"
	exit()

n = int(sys.argv[2])
file = sys.argv[1]
start_time = time.time()
#total_time_for_2 = 0
#print "Descriptions of Example 2"
#print "`1 Datacenter, Fixed VMs properties, variable number of VMs, Variable number of cloudlets, Variable lenght of each Cloudlet, Host RAM and BandWidth adjusted accordingly, Variable MIPS of Host, Fixed number of CPU's : 1`"
#start2_time = time.time()
#print "[" + str(start2_time - start_time)[:4] + "s] Starting simulation of Example 2"
#for i in range(10) :
#	command2 = 'javac Try2.java && java org.cloudbus.cloudsim.examples.Try2'
#	output = subprocess.check_output(command2, shell=True)
#	total_time_for_2 += float(output[len(output)-33:-28])
#end2_time = time.time()
#print "[" + str(end2_time - start_time)[:4] + "s] Simulation of Example 2 completed"
#print "Total time for ex2 executing 10 times " + str(total_time_for_2) + "s\n"

total_time_for_4 = 0
#print "Descriptions of Example 4"
#print "`1 Datacenter, Fixed VMs properties, variable number of VMs, Variable number of cloudlets, Variable lenght of each Cloudlet, Host RAM and BandWidth adjusted accordingly, Fixed MIPS of Host, Number of CPU's equal number of VMs`"
start4_time = time.time()
print "[" + str(start4_time - start_time)[:4] + "s] Starting simulation of Example 4\n"
for i in range(n) :
	command4 = 'javac ' + file + ' && java CloudComputing.' + file[:-5]
	output = subprocess.check_output(command4, shell=True)
	total_time_for_4 += float(output[len(output)-33:-28])
	this_simulation_time = float(output[len(output)-33:-28])
	print "Total time in " + str(i+1) + " simulation is " + str(this_simulation_time) + "s"
end4_time = time.time()
print "\n[" + str(end4_time - start_time)[:4] + "s] Simulation of Example 4 completed\n"
print "Total time for executing Example4 " + str(n) +" times " + str(total_time_for_4) + "s"
print "Average time per simulation is " + str(total_time_for_4/n) + "s\n"
end_time = time.time()
print "[" + str(end_time - start_time)[:4] + "s] Exiting the program....."
