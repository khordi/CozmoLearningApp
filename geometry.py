import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps

def angle(self: cozmo.robot.Robot):
    self.say_text("An angle is two rays that share the same vertex. Intersecting lines can also form angles.",voice_pitch=0,duration_scalar=0.6,in_parallel=False).wait_for_completed
    self.drive_straight(distance_mm(150),speed_mmps(50),in_parallel=True)
    self.say_text("As an example, if i drive from A to B and then turn 20 degrees to the right and then move B to C. The angle between ABC  ",voice_pitch=0,duration_scalar=0.6,in_parallel=True).wait_for_completed

    return
