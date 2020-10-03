from math import pi, sin, cos
import h5py
from direct.showbase.ShowBase import ShowBase
from direct.task import Task

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.pos = []

        for i in range(150):
            h5 = h5py.File("data/" + str(i + 1) + ".h5", 'r')
            positions = h5.get('positions')[:]
            self.pos.append(positions)
            h5.close()

        self.frame = 0
        self.particle = []

        for i in range(self.pos[0].shape[0]):
            self.particle.append(self.loader.loadModel("models/smiley"))
            self.particle[i].setScale(0.25, 0.25, 0.25)
            self.particle[i].reparentTo(self.render)

        self.exampleTask = self.taskMgr.doMethodLater(2, self.setParticle, 'MyTaskName')
        self.exampleTask.loop()

    def setParticle(self, task):
        for i in range(self.pos[self.frame].shape[0]):
            curPos = self.pos[self.frame][i] * 10
            self.particle[i].setPos(curPos[0], curPos[2], curPos[1])

        self.frame = self.frame + 1
        if self.frame == len(self.pos):
            self.frame = 0
        return task.cont

    # Define a procedure to move the camera.
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont


app = MyApp()
app.run()
