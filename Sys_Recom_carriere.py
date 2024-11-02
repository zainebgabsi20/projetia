import tkinter as tk
from tkinter import messagebox
from experta import Rule, Fact, AND, KnowledgeEngine

class User(Fact):
    pass

class Athletic(Fact):
    jobs = ['Football Player', 'Swimmer', 'Dancer']
    skills = ['teamwork', 'agility', 'physical_fitness', 'endurance', 'swimming_technique', 'breath_control',
              'coordination', 'flexibility', 'creativity']

class Art(Fact):
    jobs = ['Painter', 'Writer', 'Graphic Designer']
    skills = ['creativity', 'imagination', 'attention_to_detail', 'Color Sense', 'Writing Skills', 'Research Skills',
              'Visual Communication', 'Adobe Creative Suite', 'Problem Solving']

class Music(Fact):
    jobs = ['Pianist', 'Singer', 'Sound Engineer']
    skills = ['musicality', 'finger_dexterity', 'music_theory', 'Vocal Technique', 'Stage Presence', 'Interpretation',
              ' Audio Editing', 'Technical Knowledge', 'Acoustics Knowledge']

class Health(Fact):
    jobs = ['Doctor', 'Nurse', 'Medical Researcher']
    skills = ['medical_knowledge', 'compassion', 'communication', 'Problem Solving', 'Critical Thinking', 'Empathy',
              'Analytical Skills', 'Research Skills', 'Attention to Detail']

class Field(Fact):
    pass

class CareerExpert(KnowledgeEngine):
    global success, suggestion
    success = 0
    suggestion = ''

    def start_system(self):
        print("Choose a career field:")
        print("1. Athletic")
        print("2. Art")
        print("3. Music")
        print("4. Health")

        choice = input("Enter the number of your choice: ")
        self.declare(User(field=choice))
        self.ask_job_questions(choice)
        self.run()
        self.suggestion_global()

    def ask_job_questions(self, field):
        field_to_class = {
            '1': Athletic,
            '2': Art,
            '3': Music,
            '4': Health
        }

        chosen_class = field_to_class.get(field)

        if chosen_class:
            print("Answer the following questions with 'yes' or 'no':")
            for skill in chosen_class.skills:
                response = input(f"Are you good in {skill.replace('_', ' ')}? ").lower()
                self.declare(User(skill=skill, interest=response, field=field))
        else:
            print("Invalid choice. Please restart and choose a valid option.")

    @Rule(AND(User(field='1'), AND(User(skill='teamwork', interest='yes'), User(skill='agility', interest='yes'),
                                   User(skill='physical_fitness', interest='yes'))))
    def suggest_Football(self):
        self.suggest_job('Football_player')

    @Rule(AND(User(field='1'), AND(User(skill='endurance', interest='yes'), User(skill='swimming_technique', interest='yes'),
                                   User(skill='breath_control', interest='yes'))))
    def suggest_Swimmer(self):
        self.suggest_job('Swimmer')

    @Rule(AND(User(field='1'), AND(User(skill='coordination', interest='yes'), User(skill='creativity', interest='yes'),
                                   User(skill='flexibility', interest='yes'))))
    def suggest_Dancer(self):
        self.suggest_job('Dancer')

    @Rule(AND(User(field='3'), AND(User(skill='musicality', interest='yes'), User(skill='finger_dexterity', interest='yes'),
                                   User(skill='music_theory', interest='yes'))))
    def suggest_Pianist(self):
        self.suggest_job('Pianist')

    @Rule(AND(User(field='3'), User(skill='vocal_technique', interest='yes'),
          User(skill='interpretation', interest='yes'), User(skill='stage_presence', interest='yes')))
    def suggest_Singer(self):
        self.suggest_job('Singer')

    @Rule(AND(User(field='3'), User(skill='audio_editing', interest='yes'),
          User(skill='acoustics_knowledge', interest='yes'), User(skill='technical_knowledge', interest='yes')))
    def suggest_SoundEngineer(self):
        self.suggest_job('Sound_Engineer')

    @Rule(AND(User(field='2'), User(skill='creativity', interest='yes'),
          User(skill='attention_to_detail', interest='yes'), User(skill='Color Sense', interest='yes')))
    def suggest_Painter(self):
        self.suggest_job('Painter')

    @Rule(AND(User(field='2'), User(skill='imagination', interest='yes'),
          User(skill='Writing Skills', interest='yes'), User(skill='Research Skills', interest='yes')))
    def suggest_Writer(self):
        self.suggest_job('Writer')

    @Rule(AND(User(field='2'), User(skill='Visual Communication', interest='yes'),
          User(skill='Adobe Creative Suite', interest='yes'), User(skill='Problem Solving', interest='yes')))
    def suggest_GraphicDesigner(self):
        self.suggest_job('Graphic_Designer')

    @Rule(AND(User(field='4'), User(skill='medical_knowledge', interest='yes'),
          User(skill='communication', interest='yes'), User(skill='Problem Solving', interest='yes')))
    def suggest_Doctor(self):
        self.suggest_job('Doctor')

    @Rule(AND(User(field='4'), User(skill='compassion', interest='yes'),
          User(skill='Critical Thinking', interest='yes'), User(skill='Empathy', interest='yes')))
    def suggest_Nurse(self):
        self.suggest_job('Nurse')

    @Rule(AND(User(field='4'), User(skill='Analytical Skills', interest='yes'),
          User(skill='Research Skills', interest='yes'), User(skill='attention to detail', interest='yes')))
    def suggest_MedicalResearcher(self):
        self.suggest_job('Medical_Researcher')

    def suggest_job(self, job):
        global success, suggestion
        suggestion = job
        success = 1 + success

    def suggestion_global(self):
        if success == 0:
            messagebox.showinfo('Result', 'The field you chose is not compatible with your skills. Please choose another one')
        else:
            messagebox.showinfo('Result', f'The best fitting job for you is {suggestion}')

class GUI:
    def __init__(self, engine):
        self.root = tk.Tk()
        self.root.title("Career Recommendation System")
        self.root.geometry("400x300")
        self.root.configure(bg='#e6e6e6')

        self.engine = engine
        self.create_gui()

    def create_gui(self):
        self.choice_var = tk.StringVar()
        tk.Label(self.root, text="Choose a career field:", font=("Helvetica", 14), bg='#e6e6e6').pack()

        fields = [("Athletic", "1"), ("Art", "2"), ("Music", "3"), ("Health", "4")]

        for text, value in fields:
            tk.Radiobutton(self.root, text=text, variable=self.choice_var, value=value, font=("Helvetica", 12), bg='#e6e6e6').pack()

        submit_button = tk.Button(self.root, text="Submit", command=self.on_submit, font=("Helvetica", 12), bg='#4caf50', fg='white')
        submit_button.pack(pady=10)

    def ask_job_questions(self, field):
        field_to_class = {
            '1': Athletic,
            '2': Art,
            '3': Music,
            '4': Health
        }

        chosen_class = field_to_class.get(field)

        if chosen_class:
            print("Answer the following questions with 'yes' or 'no':")
            for skill in chosen_class.skills:
                response = messagebox.askyesno("Question", f"Are you good in {skill.replace('_', ' ')}?")
                self.engine.declare(User(skill=skill, interest='yes' if response else 'no', field=field))
        else:
            print("Invalid choice. Please restart and choose a valid option.")

    def on_submit(self):
        self.reset()
        choice = self.choice_var.get()
        self.ask_job_questions(choice)
        engine.run()
        self.suggestion_global()

    def reset(self):
        global success, suggestion
        success = 0
        suggestion = ''

    def suggestion_global(self):
        if success == 0:
            messagebox.showinfo('Result', 'The field you chose is not compatible with your skills. Please choose another one')
        else:
            messagebox.showinfo('Result', f'The best fitting job for you is {suggestion}')

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    engine = CareerExpert()
    gui = GUI(engine)
    gui.run()
