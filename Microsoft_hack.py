def simulator(number_of_simulations):

    print("Starting_temperature Target_temperature N Runtime")
    for i in range(number_of_simulations):
        a = [int(x) for x in raw_input().split(',')]
        if a[3] >= 44640:
            raise ValueError('Your runtime value exceeds allowed number 44640.')

        #simulation here
        starting_temp = a[0]
        target_temp = a[1]
        N = a[2]
        runtime = a[3]


        energy_unit_counter = 0

        #runtime --> number of steps
        if runtime != 0:
            if starting_temp <= target_temp - (N-1):
                energy_unit_counter += 5 #loosing to the lowest range
                runtime = runtime-1
                for i in range(N-1):
                    energy_unit_counter += 10
                    runtime = runtime-1
            if starting_temp >= target_temp + N:
                runtime = runtime-1
                starting_temperature = starting_temperature- 1
                #energy counter is the same we are dropping to the minimum extreme
                runtime = runtime-1
                starting_temperature = starting_temperature- 1
                #energy counter is the same we are dropping to the minimum extreme
                runtime = runtime-1
                starting_temperature = starting_temperature- 1
                #energy counter is the same we are dropping to the minimum extreme
                runtime = runtime-1
                starting_temperature = starting_temperature- 1


        print energy_unit_counter


number_of_simulations = input("How many simulations you want to run?  ")
simulator(number_of_simulations)
