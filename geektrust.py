# Our problem is set in the traffic snarls of planet Lengaburu. After the recent Falicornian war, victorious King
# Shan of Lengaburu wishes to tour his kingdom. But the traffic in Lengaburu is killing. You should see how Silk
# Dorb gets jammed in the evening!
# Write code to help King Shan navigate Lengaburu's traffic.

# import dependencies
import sys

# define a function which will update the crater basesd on creater_changed_by parameter
# for sunny we will reduce it by 10%
# for rainy we will increase it by 20%
# for windy no chnage in crater
# it will return the updated the orbit crater
def update_crater(orbit_opt, weather_lower, crater_changed_by):

    if weather_lower == 'sunny' or weather_lower == 'rainy':
        orb_1 = int(orbit_opt['orbit_1'][1] + ((orbit_opt['orbit_1'][1] * crater_changed_by)/100))
        orb_2 = int(orbit_opt['orbit_2'][1] + ((orbit_opt['orbit_2'][1] * crater_changed_by)/100))
        return orb_1, orb_2
    else:
        return orbit_opt['orbit_1'][1], orbit_opt['orbit_2'][1]


# define a function which will find the perfect matched vehicle and orbit
# Steps:
#   1. calculate the time for a vehicle for both orbit
#   2. based on min time taken find the best orbit
#   3. repeat step 1 and 3 for all the vehicle
#   4. return the best vehicle based on orbit
def find_veh_orbit(orbit_opt, vehicle_opt, weather, weather_lower, crater_changed_by, veh_opts, orbit_1_speed, orbit_2_speed):
    # define a variable for time_taken
    time_taken = 0
    # define a variable to store the selected vehicle
    vehicle_selected = ''
    # define a variable to store the selected orbit
    orbit_selected = ''

    # update the orbit crater
    orbit_1_crater, orbit_2_crater = update_crater(orbit_opt, weather_lower, crater_changed_by)
    # print(orbit_1_crater, orbit_2_crater)

    # get the orbit distance
    orbit_1_dis = orbit_opt['orbit_1'][0]
    orbit_2_dis = orbit_opt['orbit_2'][0]

    # loop through the vehicles
    for vehicle in veh_opts:
        # get the vehicle_speed, time taken to cross one crater from vehicle_opt dict
        vs = vehicle_opt[vehicle][0]
        tt = vehicle_opt[vehicle][1]

        # check the vehicle speed(vs) with orbit_1_speed for orbit 1 and orbit_2_speed for orbit 2
        # claculate time taken to cross the orbit distance
        if vs >= orbit_1_speed:
            temp_speed = orbit_1_speed
            tt_distance_1 = (orbit_1_dis/temp_speed) * 60
        else:
            tt_distance_1 = (orbit_1_dis/vs) * 60
        if vs >= orbit_2_speed:
            tt_distance_2 = (orbit_2_dis/orbit_2_speed) * 60
        else:
            tt_distance_2 = (orbit_2_dis/vs) * 60

        # claculate time taken to cross the orbit crater
        tt_crater_1 = (tt * orbit_1_crater)
        tt_crater_2 = (tt * orbit_2_crater)

        # sum the total time taken to cover the distance and crater
        total_time_1 = tt_distance_1 + tt_crater_1
        total_time_2 = tt_distance_2 + tt_crater_2

        # compare the time taken and will select the orbit which takes less time
        if total_time_1 < total_time_2:
            if time_taken == 0:
                time_taken = total_time_1
                vehicle_selected = vehicle
                orbit_selected = 'ORBIT1'
            else:
                if total_time_1 < time_taken:
                    time_taken = total_time_1
                    vehicle_selected = vehicle
                    orbit_selected = 'ORBIT1'
                else:
                    pass
        else:
            if time_taken == 0:
                time_taken = total_time_2
                vehicle_selected = vehicle
                orbit_selected = 'ORBIT2'
            else:
                if total_time_2 < time_taken:
                    time_taken = total_time_2
                    vehicle_selected = vehicle
                    orbit_selected = 'ORBIT2'
                else:
                    pass
    return vehicle_selected.upper(), orbit_selected


# define a function which will select the crater reduced by and vehicles optio based on weather condition
# this function will then call find_veh_orbit() to find the best vehicle and orbit
# print the best vehicle and orbit to the console
def crater_veh_option(orbit_opt, vehicle_opt, weather, in_weather, orbit_1_speed, orbit_2_speed):
    # covert the weather into lower case
    weather_lower = in_weather.lower()
    # check the weather
    if weather_lower == 'sunny':
        # select the crater reduced by and vehicle option from weather dictionary
        crater_changed_by = -weather[weather_lower][0]
        veh_opts = weather[weather_lower][1]

        # call the below function will find the vehicle and orbit
        # print(find_veh_orbit(orbit_opt, vehicle_opt, weather,weather_lower, crater_changed_by, veh_opts, orbit_1_speed, orbit_2_speed))
        res_vehicle, res_orbit = find_veh_orbit(orbit_opt, vehicle_opt, weather,weather_lower, crater_changed_by, veh_opts, orbit_1_speed, orbit_2_speed)
        print(res_vehicle, res_orbit)

    elif weather_lower == 'rainy':
        # select the crater reduced by and vehicle option from weather dictionary
        crater_changed_by = weather[weather_lower][0]
        veh_opts = weather[weather_lower][1]

        # call the below function will find the vehicle and orbit
        #print(find_veh_orbit(orbit_opt, vehicle_opt, weather, weather_lower, crater_changed_by, veh_opts, orbit_1_speed, orbit_2_speed))
        res_vehicle, res_orbit = find_veh_orbit(orbit_opt, vehicle_opt, weather,weather_lower, crater_changed_by, veh_opts, orbit_1_speed, orbit_2_speed)
        print(res_vehicle, res_orbit)

    elif weather_lower == 'windy':
        # select the crater reduced by and vehicle option from weather dictionary
        crater_changed_by = 0
        veh_opts = weather[weather_lower][1]

        # call the below function will find the vehicle and orbit
        #print(find_veh_orbit(orbit_opt, vehicle_opt, weather, weather_lower, crater_changed_by, veh_opts, orbit_1_speed, orbit_2_speed))
        res_vehicle, res_orbit = find_veh_orbit(orbit_opt, vehicle_opt, weather,weather_lower, crater_changed_by, veh_opts, orbit_1_speed, orbit_2_speed)
        print(res_vehicle, res_orbit)

    else:
        print("wrong weather")



def main():
    #input_file = sys.argv[1]

    # define orbit option
    # I will use a list to store distance(mega miles) and craters to cross
    # [distnace, crater_to_cross]
    orbit_opt = {
    'orbit_1': [18,20],
    'orbit_2': [20,10]
    }


    # define the vechicle options
    # I will use a list to store speed and time taken to cross 1 crater
    # [speed, time_taken ]
    vehicle_opt = {
    'bike': [10, 2],
    'tuktuk': [12, 1],
    'car': [20,3]
    }

    # define weather conditions
    # I will use a list or store craters reduced by integer percentage and vehicle options used
    # [reduced_by, vehicle_option ]
    # reduced_by 0 means no change

    weather = {
    'sunny': [10, ['car', 'bike', 'tuktuk']],
    'rainy': [20, ['car', 'tuktuk']],
    'windy': [0, ['car', 'bike']]
    }

    # get the input from file
    # Rainy 40 25
    input_file = sys.argv[1]
    f = open(input_file, "r")

    f1 = f.readline()
    input_vals = f1.rstrip().split(' ')

    # separate the input weather, ORBIT_1_TRAFFIC_SPEED  and ORBIT_2_TRAFFIC_SPEED
    in_weather = input_vals[0]
    orbit_1_speed = int(input_vals[1])
    orbit_2_speed = int(input_vals[2])
    #print(in_weather, orbit_1_speed, orbit_2_speed)


    crater_veh_option(orbit_opt, vehicle_opt, weather, in_weather, orbit_1_speed, orbit_2_speed)

if __name__ == "__main__":

    main()
