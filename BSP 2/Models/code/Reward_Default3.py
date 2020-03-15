def reward_function(params):
    '''
    zig-zag, distance from middle, wheels on track
    '''
    
    # Read input parameters
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    steering = abs(params['steering_angle']) # Only need the absolute steering angle
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']


    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Give higher reward if the agent is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 1
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  


    #Give higher reward if the agent goes faster
    if speed 

    # Steering penality threshold, change the number based on your action space setting
    ABS_STEERING_THRESHOLD = 15

    # Penalize reward if the agent is steering too much
    if steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8

    #Penalize reward if the agent is off the track
    if all_wheels_on_track == False:
        reward = 1e-3

    return float(reward)

"""
- the more the track is completed the higher the reward 
- the faster it goes the higher the reward
- if the car is heading towards closest waypoint better reward
- if crash penalize
- the less steps used to complete the track the better reward
"""