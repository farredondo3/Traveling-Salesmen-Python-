# Hash Map
import csv
import datetime
#from datetime import datetime


class Package:

    def __init__(self,id,address, city, state, zip, deadline, weight, note):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.note = note
        self.deliveredTime = None
        self.status = "At hub"

    def __str__(self):
        return "%s %s %s %s %s %s %s %s %s %s" \
               %(self.id,self.address,self.city,self.state,self.zip,self.deadline,self.weight,self.note, self.status, str(self.deliveredTime))


class Truck:
    def __init__(self, truck_num, dateTimeObj):
        self.truck_num = truck_num
        self.time_departure = dateTimeObj
        self.truckList = []
        self.index = 0

    def __str__(self):
        return f'truckId %s time_left %s count %i' %(self.truck_num, self.time_departure, len(self.truckList))

    def insertPackage(self, pkgId):

        if self.index < 16:
            self.truckList.insert(self.index, pkgId)
            self.index = self.index + 1


#data member called mileage current location, last location


def minimumDistanceFromAddress(address, packages):

    minNum = 1000
    nextAddress = ""
    nextID = 0

    for pkg in packages:
        pack = myList.get(pkg)
        address2 = pack.address
        distance = distanceLookup(address,address2)
        if distance < minNum:
            minNum = distance
            nextAddress = address2
            nextID = pkg

    return nextAddress,nextID, minNum

def deliverPackage(truck):
    miles = 0
    startTime = truck.time_departure
    currentLocation = "4001 South 700 East"
    while len(truck.truckList) > 0:
        addressVisited, iddelivered,distanceTraveled = minimumDistanceFromAddress(currentLocation, truck.truckList)
        miles += distanceTraveled
        temp = distanceTraveled/18 * 60 * 60
        dts = datetime.timedelta(seconds= temp)
        pack = myList.get(iddelivered)
        pack.status = 'delivered'
        timeObj = truck.time_departure + dts
        truck.time_departure = timeObj
        pack.deliveredTime = timeObj
        truck.truckList.remove(iddelivered)
        currentLocation = addressVisited
        #print(dts)
        #print(timeObj)
        #print(iddelivered)

    return miles

class HashMap:
    def __init__(self):# method that initializes the itself a constructor.
        self.size = 40  # what size should I make it.
        self.map = [None] * self.size # sets hashmap to empty in all slots and sets them to all indexes

    def _get_hash(self, key): # method that gets hash
        hash = 0 # idk why hash is set to 0
        for char in str(key): # for loop that calculates from key to index and returns index
            hash += ord(char)
        return hash % self.size

    def add(self, key, value): # gets cell and inserts the key and value into the cell
        key_hash = self._get_hash(key)
        key_value = [key, value] #constructing a list with the key and value we want to insert

        if self.map[key_hash] is None:#Checks if cell is empty
            self.map[key_hash] = list([key_value]) #if true insert the key and value into the new list within the index
            return True
        else:
            for pair in self.map[key_hash]: # if not empty we check to see if key exists already, if so update the value
                if pair[0] == key: #if the key doesn't exists append to list. idk what that means. If keys doesn't exist add a new key/value pair
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True

    def get(self, key):#get the hash given the key locate the cell if not none iterate through the pairs within the cell and find a value that matches key and return value
        key_hash = self._get_hash(key)# no key found return none
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key): #passed in key and now find key in order to find key_hash(index)
        key_hash = self._get_hash(key)#check if key cell is none if so return false. Key value doesnt exist

        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):# need index in order to remove from list
            if self.map[key_hash][i][0] == key:#when Item is found, use pop to remove the item.
                self.map[key_hash].pop(i)
                return True
        return False

    def keys(self):#prints out every non empty cell
        arr = []
        for i in range(0, len(self.map)):
            if self.map[i]:
                arr.append(self.map[i][0])
        return arr

    def print(self):
        print('-------')
        for item in self.map:
            if item is not None:
                print(str(item))

def loadPackages(fileName):
    with open(fileName) as PackageFile:
        packages = csv.reader(PackageFile, delimiter = ",")
        for package in packages:
            id = int(package[0])
            address = package[1]# address city state zip
            city = package[2]
            state = package[3]
            zip = package[4]
            deadline = package[5]
            weight = package[6]
            note = package[7]

            p = Package(id,address,city,state,zip,deadline,weight,note)
            myList.add(id,p)


def printHashMap(myList):
    for i in range(len(myList.map)):
        print("package: {}".format(myList.get(i+1)))

#print(myList.keys())
#printHashMap(myList)
#def distanceLookup(sourceAddress,deliveryAddress)
#address and distance 27 package 40


def loadDistanceData(filename):
    with open(filename) as fileReader:
        distances = csv.reader(fileReader, delimiter = ",")
        for distance in distances:
            distanceData.append(distance)


def loadAddressData(filename):
    with open(filename) as fileReader:
        addresses = csv.reader(fileReader, delimiter = ",")
        for address in addresses:
            addressData.append(address[0])

def printDistances(distanceData):
    for i in range(len(distanceData)):
        print("distances: {}".format(distanceData[i]))

def printAddresses(addressData):
    for i in range(len(addressData)):
        print("addresses: {}".format(addressData[i]))


def distanceLookup(sourceAddress,deliveryAddress):
    vreturn = 0
    h = addressData.index(sourceAddress)
    j = addressData.index(deliveryAddress)
    distance = distanceData[h][j]
    #print(distance)

    if distanceData[h][j] == "":
        distance = distanceData[j][h]
        #print(distance)
    return float(distance)

#printDistances(distanceData)
#printAddresses(addressData)

myList = HashMap()
distanceData = []
addressData = []

def mainModule():


    #distance = distanceLookup("380 W 2880 S", "5100 South 2700 West")
    #print(distance)

    loadDistanceData("Only numbers distance C950.csv")
    loadAddressData("addressC950.csv")

    loadPackages("newC950_Package.csv")
    #package = myList.get(15)
    #print(package)

    nowTime = " 08:00:00"
    h, m, s = nowTime.split(":")
    # print(h, m, s)
    timeObj = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    #print(timeObj)

    truck1 = Truck(1, timeObj)

    truck1.insertPackage(1)
    truck1.insertPackage(13)
    truck1.insertPackage(14)
    truck1.insertPackage(15)
    truck1.insertPackage(16)
    truck1.insertPackage(19)
    truck1.insertPackage(20)
    truck1.insertPackage(29)
    truck1.insertPackage(30)
    truck1.insertPackage(31)
    truck1.insertPackage(34)
    truck1.insertPackage(37)
    truck1.insertPackage(40)
    truck1.insertPackage(2)
    truck1.insertPackage(4)
    truck1.insertPackage(25)

    #print(truck1)

    #for i in range(len(truck1.truckList)):
        #print(truck1.truckList[i])

    nowTime = " 09:05:00"
    h, m, s = nowTime.split(":")
    timeObj = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

    truck2 = Truck(2, timeObj)

    truck2.insertPackage(3)
    truck2.insertPackage(6)
    truck2.insertPackage(18)
    truck2.insertPackage(5)
    truck2.insertPackage(28)
    truck2.insertPackage(32)
    truck2.insertPackage(36)
    truck2.insertPackage(38)
    truck2.insertPackage(7)
    truck2.insertPackage(8)
    truck2.insertPackage(10)
    truck2.insertPackage(11)
    truck2.insertPackage(12)
    truck2.insertPackage(17)
    truck2.insertPackage(21)
    truck2.insertPackage(22)

    #print(truck2)

    #for i in range(len(truck2.truckList)):
        #print(truck2.truckList[i])

    nowTime = " 10:20:00"
    h, m, s = nowTime.split(":")
    timeObj = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

    truck3 = Truck(3, timeObj)

    truck3.insertPackage(9)
    truck3.insertPackage(23)
    truck3.insertPackage(24)
    truck3.insertPackage(26)
    truck3.insertPackage(27)
    truck3.insertPackage(33)
    truck3.insertPackage(35)
    truck3.insertPackage(39)

    #print(truck3)

    #for i in range(len(truck3.truckList)):
        #print(truck3.truckList[i])


    truck1Miles = deliverPackage(truck1)
    #print(truck1Miles)

    truck2Miles = deliverPackage(truck2)
    #print(truck2Miles)

    truck3Miles = deliverPackage(truck3)
    #print(truck3Miles)

    print(truck1.time_departure)
    print(truck2.time_departure)
    print(truck3.time_departure)

    printHashMap(myList)

    truckMilesTotal = truck1Miles + truck2Miles + truck3Miles
    print(truckMilesTotal)
if __name__ == '__main__':
    mainModule()