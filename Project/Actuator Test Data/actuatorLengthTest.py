import numpy as np
import matplotlib.pyplot as plt

#Actuator elongation due to internal volume increase using a 10 ml syringe
airVolume = np.array([0,2,4,6,8,10])  #from 0 to 10ml
actuatorLength=np.array([[0,3,8,13,19,24],[0,3,8,11,17,22],[0,3,8,12,17,21],[0,3,7,13,17,21],[0,3,7,11,17,21],[0,3,7,12,17,21],[0,3,7,12,16,21],[0,3,7,12,17,21],[0,3,7,13,18,23],[0,2,7,12,17,24],[0,2,7,12,17,23],[0,2,5,10,15,20],[0,1,5,10,15,20]])   #results from 13 tests

averageData=actuatorLength.mean(axis=0)
errorData=actuatorLength.std(axis=0)

plt.errorbar(airVolume,averageData,yerr=errorData,fmt='o')
plt.plot(airVolume,averageData,'-')
plt.ylabel('Actuator Stretch [cm]',fontsize=30)
plt.xlabel('Air volume [ml]',fontsize=30)
plt.show()

#Actuator elongation, measuring excerted force with Instrom machine.
test1=np.genfromtxt("Specimen_RawData_1.csv",delimiter=",",skip_header=2)
test2=np.genfromtxt("Specimen_RawData_2.csv",delimiter=",",skip_header=2)
test3=np.genfromtxt("Specimen_RawData_3.csv",delimiter=",",skip_header=2)
test4=np.genfromtxt("Specimen_RawData_4.csv",delimiter=",",skip_header=2)
test5=np.genfromtxt("Specimen_RawData_5.csv",delimiter=",",skip_header=2)
test6=np.genfromtxt("Specimen_RawData_6.csv",delimiter=",",skip_header=2)
test7=np.genfromtxt("Specimen_RawData_7.csv",delimiter=",",skip_header=2)
test8=np.genfromtxt("Specimen_RawData_8.csv",delimiter=",",skip_header=2)
test9=np.genfromtxt("Specimen_RawData_9.csv",delimiter=",",skip_header=2)
test10=np.genfromtxt("Specimen_RawData_10.csv",delimiter=",",skip_header=2)
test11=np.genfromtxt("Specimen_RawData_11.csv",delimiter=",",skip_header=2)
test12=np.genfromtxt("Specimen_RawData_12.csv",delimiter=",",skip_header=2)
test13=np.genfromtxt("Specimen_RawData_13.csv",delimiter=",",skip_header=2)
test14=np.genfromtxt("Specimen_RawData_14.csv",delimiter=",",skip_header=2)
test15=np.genfromtxt("Specimen_RawData_15.csv",delimiter=",",skip_header=2)
test16=np.genfromtxt("Specimen_RawData_16.csv",delimiter=",",skip_header=2)
test17=np.genfromtxt("Specimen_RawData_17.csv",delimiter=",",skip_header=2)
syringeLength=57   #internal length from 0 to 10 ml, 57 mm

plt.plot(test1[:,1],test1[:,2],label='Test 1')
plt.plot(test2[:,1],test2[:,2],label='Test 2')
plt.plot(test3[:,1],test3[:,2],label='Test 3')
plt.plot(test4[:,1],test4[:,2],label='Test 4')
plt.plot(test5[:,1],test5[:,2],label='Test 5')
plt.plot(test6[:,1],test6[:,2],label='Test 6')
plt.plot(test7[:,1],test7[:,2],label='Test 7')
plt.plot(test8[:,1],test8[:,2],label='Test 8')
plt.plot(test9[:,1],test9[:,2],label='Test 9')
plt.plot(test10[:,1],test10[:,2],label='Test 10')
plt.plot(test11[:,1],test11[:,2],label='Test 11')
plt.plot(test12[:,1],test12[:,2],label='Test 12')
plt.plot(test13[:,1],test13[:,2],label='Test 13')
plt.plot(test14[:,1],test14[:,2],label='Test 14')
plt.plot(test15[:,1],test15[:,2],label='Test 15')
plt.plot(test16[:,1],test16[:,2],label='Test 16')
plt.plot(test17[:,1],test17[:,2],label='Test 17')
plt.legend()
plt.ylabel('Force [N]')
plt.xlabel('Distance [mm]')
plt.show()

test4=np.delete(test4,[582,583],axis=0)
test14=np.delete(test14,[582],axis=0)

load=test3[:,2]
load=np.vstack((load,test4[:,2]))
load=np.vstack((load,test5[:,2]))
load=np.vstack((load,test6[:,2]))
load=np.vstack((load,test7[:,2]))
load=np.vstack((load,test8[:,2]))
load=np.vstack((load,test9[:,2]))
load=np.vstack((load,test10[:,2]))
load=np.vstack((load,test11[:,2]))
load=np.vstack((load,test12[:,2]))
load=np.vstack((load,test13[:,2]))
load=np.vstack((load,test14[:,2]))
load=np.vstack((load,test15[:,2]))
load=np.vstack((load,test16[:,2]))
load=np.vstack((load,test17[:,2]))
averageLoad=load.mean(axis=0)
errorLoad=load.std(axis=0)

for i in range(len(test3)):
	if test3[i,1]>syringeLength:
		limit=i
		break

plt.errorbar(test3[0:limit,1],averageLoad[0:limit],yerr=errorLoad[0:limit],fmt='o',label='Average')
plt.legend()
plt.ylabel('Force [N]',fontsize=30)
plt.xlabel('Distance [mm]',fontsize=30)
plt.show()

#Linear regression model for stretch vs. distance
m, b = np.polyfit(distance,averageData,1)

stretch=test3[0:limit,1]*m+b

#Force vs. Stretch
plt.errorbar(stretch,averageLoad[0:limit],yerr=errorLoad[0:limit],fmt='o',label='Average')
plt.plot(stretch,averageLoad[0:limit])
plt.ylabel('Force [N]',fontsize=30)
plt.xlabel('Stretch [mm]',fontsize=30)
plt.show()
