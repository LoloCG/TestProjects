def get_ex1_attr():
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

def get_ex1_workout_performed():
    microcycle_info = {
        'exer_workout_reps_performed': [10,9,8],
        'exer_workout_weight_performed': 100
    }
    return microcycle_info

def get_ex2_attr():
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

def get_ex2_workout_performed():
    microcycle_info = {
        'exer_workout_reps_performed': [14,12,11],
        'exer_workout_weight_performed': 60
    }
    return microcycle_info