from tabulate import tabulate
import test_exercises as TestExer
import db_handler as db

weekday = ['mon','tues','wed','thurs','fri','sat','sun'] # TODO: convertir en enum para reemplazar numero de ejercicio

def main():
    exer_list = create_exercise_object_list()

    microcycleObj = Microcycle()
    microcycle_exer_session_obj_dict = microcycleObj.create_exer_sessions_obj(exer_list)
    microcycle_sessions_obj_dict = microcycleObj.create_microcycle_sessions(microcycle_exer_session_obj_dict)
    
    for session_name, session_obj in microcycle_sessions_obj_dict.items():
        session_obj.display_session_exercises()

def create_exercise_object_list():
    ex1_attr = TestExer.HighBarSquat_attr()
    ex1_obj_week_distr = [0,2,4]
    ex1 = Exer_Cons_Attr(ex1_attr,distribution=ex1_obj_week_distr)

    ex2_attr = TestExer.BenchPress_attr()
    ex2_obj_week_distr = [0,4]
    ex2 = Exer_Cons_Attr(ex2_attr,distribution=ex2_obj_week_distr)

    ex3_attr = TestExer.DumbbelLateralRaises_attr()
    ex3_obj_week_distr = [2]
    ex3 = Exer_Cons_Attr(ex3_attr,distribution=ex3_obj_week_distr)

    exer_obj_list = [ex1, ex2, ex3]

    return exer_obj_list

class Exer_Cons_Attr:
    def __init__(self, exer_attr_dict, distribution):
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

        self.exer_distr = distribution

        if self.max_rep_range <= 10:
            self.exercise_rir_first_microcycle = 4
        else:
            self.exercise_rir_first_microcycle = 3

class Exer_Session:
    def __init__(self, exer_sess_attrDict):
        for itemName, item in exer_sess_attrDict.items():
            setattr(self, itemName, item)

class Session:
    def __init__(self, session_exer_list, session_name):
        self.session_name = session_name
        #print(f"DEBUG: In session of key {session_name}")
        self.session_exercise_dict = {}
        for exer in session_exer_list:
            self.session_exercise_dict[exer.exercise_name] = exer

    def display_session_exercises(self):
        headers = ['Exercise', 'Sets', 'Weight', 'First Set Rep-range', 'RIR', 'Rest time']

        table_data = []
        for exer_name, exercise in self.session_exercise_dict.items():
            values = list(exercise.__dict__.values())
            for i, value in enumerate(values):
                #print(f"DEBUG: for exercise {exercise.exercise_name}, i={i},value={value}")
                if isinstance(value, (list, tuple)): # Convert list/tuple to a comma-separated string
                    values[i] = ' - '.join(map(str, value))  

            table_data.append(values)

        alignment = ["center"] * len(headers)  # Center align all columns

        print(f"\nWorkout Session {self.session_name}:")
        print(tabulate(table_data, headers=headers, tablefmt="fancy_grid", colalign=alignment))
    
class Microcycle:
    def __init__(self): 
        '''
        MVP:
            - Required attr to save and manipulate:
                microcycle_num
                microcycle_exercises_name_list
                other: date_period, 
            - Obtain a list of the exercise_cons_attr objects and from there separate to as many as 
                the frequency distribution requires, into different exer_session object.
            - Create as many Session objects that includes each exer_session objects.
        '''
        self.microcycle_num = None
        self.microcycle_exercises_name_list = []
    
    def create_microcycle_sessions(self, microcycle_exer_session_obj_dict):
        '''
        Separates and joins the exercise of each session in a dictionary, then for each session
            it generates a dictionary of "session" objectes, where it creates the sessions giving each 
            its exercise objects
        '''
        sessions = {} 
        for exer_name, exer_obj in microcycle_exer_session_obj_dict.items():     
            parts = exer_name.split('_')
            day = parts[len(parts)-2]
            session_num = parts[len(parts)-1]

            session_key = f"{day}_{session_num}"
            #print(f"DEBUG: adding {exer_name} to key {session_key}")

            if session_key not in sessions:
                sessions[session_key] = []
                #print(f"DEBUG: new session found: {session_key}")

            sessions[session_key].append(exer_obj)
        
        microcycle_sessions_obj_dict = {}

        for session_key, exercises in sessions.items():
            session_name = 'session_'+ session_key

            microcycle_sessions_obj_dict[session_name] = Session(session_exer_list=exercises, session_name=session_name)

        return microcycle_sessions_obj_dict

    def create_exer_sessions_obj(self, exer_cons_obj_list):    
        '''
        Generates a dictionary where key = exercise name identifier, item = session exercise object
        ''' 
        if self.microcycle_num is None: self.microcycle_num = 1
        else: 
            print(f"ERROR in create_exer_sessions_obj_name method of Microcycle class.\nThe microcycle_num was {self.microcycle_num}, not None")
            return
        
        microcycle_exer_session_obj_dict = {}
        object_counter = {}
        for exercise in exer_cons_obj_list:
            for num in exercise.exer_distr:
                base_name = exercise.exercise_name.replace(" ", "_") + '_' + str(num)

                if base_name not in object_counter:   # TODO: in the future, reemplace with enums lib...
                    object_counter[base_name] = 0
                else:
                    object_counter[base_name] += 1
                
                exer_session_obj_name = f"{base_name}_{object_counter[base_name]}"
                self.microcycle_exercises_name_list.append(exer_session_obj_name) # to save the exercises of the microcycle in this class...
                
                exerciseDict_obj = self.create_exer_Session_attr_dict(exercise)

                microcycle_exer_session_obj_dict[exer_session_obj_name] = Exer_Session(exerciseDict_obj) 
                
        #self.create_microcycle_sessions(microcycle_exer_session_obj_dict) # this should be uncommented if creating sessions is automated.
        return microcycle_exer_session_obj_dict

    def create_exer_Session_attr_dict(self,exercise):
        exerciseDict = {
            'exercise_name':                    exercise.exercise_name,
            'exercise_muscle_group':            exercise.exercise_muscle_group,
            'max_rep_range':                    exercise.max_rep_range,
            'min_rep_range':                    exercise.min_rep_range,
            'min_weight_increment':             exercise.min_weight_increment,
            'rest_time_mins':                   exercise.rest_time_mins,
            'exercise_rir_first_microcycle':    exercise.exercise_rir_first_microcycle
            }
        
        return exerciseDict

main()
