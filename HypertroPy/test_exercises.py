def create_microcycle_structure():
    '''
    '''

    print(f"Microcycle structure consist on:")
def microcycle_values():
    # maybe define the exercise distribution in 0-6 representing days of the week monday to sunday? 
    ex1_obj_week_distr = [0,2,4] # mon, wed, fri
    
# ======================== High Bar Squats ========================
def HighBarSquat_attr():
    exercise_name = 'High bar squats'
    exercise_muscle_group = 'Quadriceps'
    exercise_rep_range = [10,5]
    min_weight_increment = 5
    rest_time_mins = 3

    basicExerciseAttr_dict = {
        'exercise_name': exercise_name,
        'exercise_muscle_group': exercise_muscle_group,
        'exercise_rep_range': exercise_rep_range,
        'min_weight_increment': min_weight_increment,
        'rest_time_mins': rest_time_mins
    }
    
    return basicExerciseAttr_dict

def HighBarSquat_performance():
    microcycle_info = {
        'exer_workout_reps_performed': [10,9,8],
        'exer_workout_weight_performed': 100
    }
    return microcycle_info

# ======================== Bench Press ========================
def BenchPress_attr():
    exercise_name = 'Bench Press'
    exercise_muscle_group = 'Chest'
    exercise_rep_range = [15,8]
    min_weight_increment = 2.5
    rest_time_mins = 2

    basicExerciseAttr_dict = {
        'exercise_name': exercise_name,
        'exercise_muscle_group': exercise_muscle_group,
        'exercise_rep_range': exercise_rep_range,
        'min_weight_increment': min_weight_increment,
        'rest_time_mins': rest_time_mins
    }
    
    return basicExerciseAttr_dict

def BenchPress_performance():
    microcycle_info = {
        'exer_workout_reps_performed': [14,12,11],
        'exer_workout_weight_performed': 60
    }
    return microcycle_info

# ======================== Dumbbell Lateral Raises ========================
def DumbbelLateralRaises_attr():
    exercise_name = 'Dumbbell Lateral Raises'
    exercise_muscle_group = 'Deltoids'
    exercise_rep_range = [20,15]
    min_weight_increment = 2.5
    rest_time_mins = 2

    basicExerciseAttr_dict = {
        'exercise_name': exercise_name,
        'exercise_muscle_group': exercise_muscle_group,
        'exercise_rep_range': exercise_rep_range,
        'min_weight_increment': min_weight_increment,
        'rest_time_mins': rest_time_mins
    }
    
    return basicExerciseAttr_dict

def DumbbelLateralRaises_performance():
    exer_performance_info = {
        'exer_workout_reps_performed': [19,17,16],
        'exer_workout_weight_performed': 15
    }
    return exer_performance_info
