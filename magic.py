class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
        self.family = None
        self.cousins = []

    def __repr__(self):
        fam_name = ''
        if self.family:
            fam_name = f"{self.family.name}"
        return f"{self.name}{fam_name} - {self.age}"

    def __del__(self):
        print(f"{self.name} waves goodbye")

class Family:
    def __init__(self, name):
        self.name = name
        self.members = []
    
    def __repr__(self):
        return "\n".join(str(x) for x in self.members)

    def __add__(self, obj):
        if isinstance(obj, Person):
            setattr(self, obj.name, obj)
            obj.family = self
            self.members.append(obj)

    def __lt__(self, obj):
        if isinstance(obj, Family):
            for my_member in self.members:
                for their_member in obj.members:
                    my_member.cousins.append(their_member)
                    their_member.cousins.append(my_member)
    
    def __contains__(self, obj):
        return obj in self.members

laney = Person(name="Laney", age=19)
tristan = Person(name="Tristan", age=16)
chloe = Person(name="Chloe", age=17)

my_family = Family(name="Staggs")
my_family + laney
my_family + tristan
my_family + chloe

smith = Family(name="Smith")
smith + Person(name="James", age=30)
smith + Person(name="Margo", age=29)

my_family < smith

print("------ My Family ------")
print(my_family)
print("------ Smith ------")
print(smith)
print(f"Chloe's cousins: {chloe.cousins}")
print(f"Jame's cousins: {smith.James.cousins}")
print(f"Tristan in Staggs? {tristan in my_family}")
print(f"Tristan in Smith? { tristan in smith}")

#another_laney = laney
#del laney