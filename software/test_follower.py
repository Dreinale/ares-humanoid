"""
Test du bras follower SO-101 — env ares (lerobot 0.6.2)
Fait bouger chaque joint séquentiellement pour valider le bras.
"""
import time
from lerobot.robots.so_follower.so_follower import SOFollower
from lerobot.robots.so_follower.config_so_follower import SOFollowerRobotConfig

robot = SOFollower(SOFollowerRobotConfig(port="COM3", id="enzo_follower_arm", cameras={}))
robot.connect()
print("Connecté. Positions initiales:")
obs = robot.get_observation()
for k, v in obs.items():
    print(f"  {k}: {v:.1f}")

joints = ["shoulder_pan", "shoulder_lift", "elbow_flex", "wrist_flex", "wrist_roll", "gripper"]
neutral = {f"{j}.pos": 0.0 for j in joints}

print("\nRetour position neutre...")
robot.send_action(neutral)
time.sleep(2)

for joint in joints:
    print(f"\nTest {joint}...")
    action = dict(neutral)
    action[f"{joint}.pos"] = 30.0
    robot.send_action(action)
    time.sleep(1.5)
    action[f"{joint}.pos"] = -30.0
    robot.send_action(action)
    time.sleep(1.5)
    robot.send_action(neutral)
    time.sleep(1)

print("\nTest gripper ouvert/fermé...")
robot.send_action({**neutral, "gripper.pos": 100.0})
time.sleep(1.5)
robot.send_action({**neutral, "gripper.pos": 0.0})
time.sleep(1.5)
robot.send_action(neutral)

robot.disconnect()
print("\nTest terminé — bras OK.")
