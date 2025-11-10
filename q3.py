
print("Name: Laiba Javed")
print("ID: 24K-0014")
print("============================= Question 3 =========================")
print(" ")

class Package:
    def __init__(self, packageId, weightInKg):
        self.packageId = packageId
        self.weightInKg = weightInKg


class Drone:
    def __init__(self, droneId, maxLoadInKg):
        self.droneId = droneId
        self.maxLoadInKg = maxLoadInKg
        self.__status = 'idle'
        self.currentPackage = None

    def getStatus(self):
        return self.__status

    def setStatus(self, newStatus):
        if newStatus in ['idle', 'delivering', 'charging']:
            self.__status = newStatus

    def assignPackage(self, packageObj):
        if self.__status == 'idle' and packageObj.weightInKg <= self.maxLoadInKg:
            self.currentPackage = packageObj
            self.setStatus('delivering')
            return True
        return False


class FleetManager:
    def __init__(self):
        self.drones = {}
        self.pendingPackages = []

    def addDrone(self, drone):
        self.drones[drone.droneId] = drone

    def addPackage(self, package):
        self.pendingPackages.append(package)

    def dispatchJobs(self):
        for drone in self.drones.values():
            if drone.getStatus() == 'idle' and self.pendingPackages:
                pkg = self.pendingPackages.pop(0)
                assigned = drone.assignPackage(pkg)
                if not assigned:
                    self.pendingPackages.insert(0, pkg)

    def simulationTick(self):
        for drone in self.drones.values():
            if drone.getStatus() == 'delivering':
                drone.setStatus('charging')
            elif drone.getStatus() == 'charging':
                drone.setStatus('idle')


manager = FleetManager()
d1 = Drone('D1', 5)
d2 = Drone('D2', 10)
manager.addDrone(d1)
manager.addDrone(d2)

p1 = Package('P1', 4)
p2 = Package('P2', 7)
p3 = Package('P3', 12)

manager.addPackage(p1)
manager.addPackage(p2)
manager.addPackage(p3)

manager.dispatchJobs()
manager.simulationTick()
manager.simulationTick()

for d in manager.drones.values():
    print(d.droneId, d.getStatus())
