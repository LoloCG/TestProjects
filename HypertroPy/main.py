from tabulate import tabulate
import test_exercises as TestExer

def main():
    ex1_attr = TestExer.get_ex1_attr()
    ex1_workout_performed = TestExer.get_ex1_workout_performed()

    ex1 = Exer_Session(ex1_attr, ex1_workout_performed)

    ex2_attr = TestExer.get_ex2_attr()
    ex2_workout_performed = TestExer.get_ex2_workout_performed()
    ex2 = Exer_Session(ex2_attr, ex2_workout_performed)

    exer_session_list = [ex1, ex2]

    session_num = 1
    session1 = Session(exer_session_list, session_num=session_num)
    session1.display_session_exercises()
    
class Exer_Cons_Attr:
    def __init__(self, exer_attr_dict):
        """
        Requires a dictionary of the base exercise attributes with the following format
            'exercise_name': (str),
            'exercise_muscle_group': (str),
            'exercise_rep_range': (list[int] of 2 values),
            'min_weight_increment': (float),
            'rest_time_mins': (float)

        From there, it obtains the following attributes:
            self.exercise_name
            self.exercise_muscle_group
            self.max_rep_range
            self.min_rep_range
            self.min_weight_increment
            self.rest_time_mins
            self.exercise_rir_first_microcycle
        """ 
        for itemName, item in exer_attr_dict.items():
            #print(f"Adding attribute {itemName} ({item}) to exercise")
            if itemName == "exercise_rep_range":  # Separate the rep range into min_rep and max_rep
                self.max_rep_range = item[0]
                self.min_rep_range = item[1]
            else:
                setattr(self, itemName, item)

        if self.max_rep_range <= 10:
            self.exercise_rir_first_microcycle = 4
        else:
            self.exercise_rir_first_microcycle = 3

class Exer_Session(Exer_Cons_Attr):
    def __init__(self, exer_attr_dict, exer_workout_performed):
        super().__init__(exer_attr_dict)
        for itemName, item in exer_workout_performed.items():
            setattr(self, itemName, item)
            #print(f"DEBUG: itemname = {itemName}, item = {item}")
        self.exer_workout_sets_performed = len(self.exer_workout_reps_performed)
        print(f"In {self.exercise_name}, performed {self.exer_workout_sets_performed} sets of {self.exer_workout_weight_performed} Kg")
    
        self.reps_startAndEnd = [self.min_rep_range, self.max_rep_range]
    
    def get_dict_exer_session(self):
        #rep_range_str = ', '.join(map(str, self.rep_range)) if isinstance(self.rep_range, (list, tuple)) else self.rep_range
        
        return {
            'Exercise':             self.exercise_name,
            'Sets':                 self.exer_workout_sets_performed, 
            'Weight':               self.exer_workout_weight_performed, 
            'First Set Rep-range':  self.reps_startAndEnd, 
            'RIR':                  self.exercise_rir_first_microcycle, 
            'Rest time':            self.rest_time_mins
        }

class Session:
    def __init__(self, exer_performed_list, session_num):
        self.exer_performed = exer_performed_list
        self.microcycle_session_num = session_num # TODO: make dynamic in the future when scaling.

    def display_session_exercises(self):
        if not self.exer_performed:
            print("No exercises to display.")
            return

        headers = ['Exercise', 'Sets', 'Weight', 'First Set Rep-range', 'RIR', 'Rest time']

        table_data = []
        for exercise in self.exer_performed:
            values = list(exercise.get_dict_exer_session().values())

            for i, value in enumerate(values):
                #print(f"DEBUG: for exercise {exercise.exercise_name}, i={i},value={value}")
                if isinstance(value, (list, tuple)):
                    values[i] = ' - '.join(map(str, value))  # Convert list/tuple to a comma-separated string

            table_data.append(values)

        alignment = ["center"] * len(headers)  # Center align all columns

        print(f"\nWorkout Session {self.microcycle_session_num}:")
        print(tabulate(table_data, headers=headers, tablefmt="fancy_grid", colalign=alignment))


main()
