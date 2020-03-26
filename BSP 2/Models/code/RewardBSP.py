import math

def reward_function(params):
    
    # Read input parameters
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    steering = abs(params['steering_angle']) 
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']
    steps = params['steps']
    progress = params['progress']
    is_crashed = params['is_crashed']
    is_offtrack = params['is_offtrack']
    waypoints = params['waypoints']
    heading = params['heading']
    closest_waypoints = params['closest_waypoints']

    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Give higher reward if the agent is closer to center line
    if distance_from_center <= marker_1:
        reward = 1
    elif distance_from_center <= marker_2:
        reward = 0.5   
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  

    #Speed limit(lower limit in m/s)
    speed_limit = 1

    #Give higher reward if the agent goes faster
    if speed < speed_limit:
        reward = 1e-3
    else:
        reward = 0.1

    #number of steps we want the agent to finish the lap in.
    total_steps = 400

    #Give higher reward the lesser steps the agent uses to complete the track
    #Check every 100 steps if it is lower than the progress of the track and give according reward to the difference
    if (steps % 100) == 0 and progress > (steps / total_steps) * 100:
        reward = int(progress) - int(steps)

    #Gives higher reward if the car is looking towards the next waypoint on the track.
    #Create previous and incomming waypoint
    previous = waypoints[closest_waypoints[0]]
    incomming = waypoints[closest_waypoints[1]]

    #From those waypoints coordinates calculate the the angle of the track the car needs to be headed at(-180,180 from the horizontal line).
    #We use the atan2 and convert it to degrees
    angle_rad = math.atan2(incomming[1] - previous[1], incomming[0] - previous[0])
    angle_deg = math.degrees(angle_rad)

    #calculate the difference between the heading of the car and the angle obtained
    diff = abs(angle_deg - heading)
    
    #Maximum angle we want the car the be able to have before getting lower reward and multiple levels.
    angle_treshold_low = 5
    angle_treshold_mid = 10
    angle_treshold_max = 15

    if diff < angle_treshold_low:
        reward = 10
    elif diff < angle_treshold_mid:
        reward = 5
    elif diff < angle_treshold_max: 
        reward = 1
    elif diff > angle_treshold_max:
        reward = 1e-3

    # Steering penality threshold, change the number based on your action space setting
    ABS_STEERING_THRESHOLD = 15

    # Penalize reward if the agent is steering too much
    if steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8

    #Penalize reward if the agent is off the track
    if all_wheels_on_track == False:
        reward = 1e-3

    #Penalize reward if agent crashed
    if is_crashed == True or is_offtrack == True:
        reward = 1e-3

    return float(reward)

"""

Functionnalities implemented : 

- penalty if zig-zag(steering too much)
- greater reward if closer to the middle
- penalty if not all wheels are on track
- the faster it goes the higher the reward
- the less steps used to complete the track the better reward
- if crash penalize
- the more the track is completed the higher the reward 
- if the car is heading towards closest waypoint better reward

"""