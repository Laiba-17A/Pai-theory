
print("Name: Laiba Javed")
print("ID: 24K-0014")
print("============================= Question 3 =========================")
print(" ")

class Package:
    def __init__(self, pid, wgt):
        self.pId = pid
        self.wgt = wgt


class Drone:
    def __init__(self, droneId, maxload):
        self.droneId = droneId
        self.maxload = maxload
        self.__status = 'idle'
        self.currP = None

    def getStatus(self):
        return self.__status

    def setStatus(self, newS):
        if newS in ['idle', 'delivering', 'charging']:
            self.__status = newS

    def assignPackage(self, p):
        if self.__status == 'idle' and p.wgt <= self.maxload:
            self.currP = p
            self.setStatus('delivering')
            return True
        return False


class FleetManager:
    def __init__(self):
        self.drones = {}
        self.pendingP = []

    def addDrone(self, drone):
        self.drones[drone.droneId] = drone

    def addPackage(self, package):
        self.pendingP.append(package)

    def dispatchJobs(self):
        for drone in self.drones.values():
            if drone.getStatus() == 'idle' and self.pendingP:
                pack = self.pendingP.pop(0)
                assigned = drone.assignPackage(pack)
                if not assigned:
                    self.pendingPackages.insert(0, pack)

    def simulationTick(self):
        for drone in self.drones.values():
            if drone.getStatus() == 'delivering':
                drone.setStatus('charging')
            elif drone.getStatus() == 'charging':
                drone.setStatus('idle')


mang = FleetManager()
d1 = Drone('D1', 5)
d2 = Drone('D2', 10)
mang.addDrone(d1)
mang.addDrone(d2)

p1 = Package('P1', 4)
p2 = Package('P2', 7)
p3 = Package('P3', 12)

mang.addPackage(p1)
mang.addPackage(p2)
mang.addPackage(p3)

mang.dispatchJobs()
mang.simulationTick()
mang.simulationTick()

for d in mang.drones.values():
    print(d.droneId, d.getStatus())
