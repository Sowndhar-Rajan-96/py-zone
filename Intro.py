class SelfIntroduction:
    def __init__(self, name, age, job_title):
        self.name = name
        self.age = age
        self.job_title = job_title

    def introduce(self):
        print(f"Hello! My name is {self.name}.")
        print(f"I am {self.age} years old.")
        print(f"I work as a {self.job_title}.")

# Create an instance of the class
person = SelfIntroduction(name="Sowndhar", age=28, job_title="Senior Software Engineer")

# Call the introduce method
person.introduce()
