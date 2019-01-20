class Employe:

    def __init__(self ,first_name ,last_name ,email):
        self.first_name = first_name
        self.last_name  = last_name
        self.email      = email

    def user_name(self):
        return self.first_name+"."+self.last_name

ep1 = Employe("RAVI" ,"S" ,"sr27631@gmail.com")


##clling class attributes using   class instance


## Calling class attributes  using Class name
print(Employe.user_name(ep1))
