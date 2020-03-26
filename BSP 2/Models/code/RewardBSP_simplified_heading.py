import math

def reward_function(params):

    #Read input parameters
    waypoints = params['waypoints']
    heading = params['heading']
    closest_waypoints = params['closest_waypoints']
    speed = params['speed']
    is_crashed = params['is_crashed']
    is_offtrack = params['is_offtrack']

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
    
    #Speed limit(lower limit in m/s)
    speed_limit = 1

    #Give higher reward if the agent goes faster
    if speed < speed_limit:
        reward = 1e-3
    else:
        reward = 0.1

    #Penalize reward if agent crashed
    if is_crashed == True or is_offtrack == True:
        reward = 1e-3
    
    return float(reward)