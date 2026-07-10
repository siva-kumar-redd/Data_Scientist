class Citizen:
    @staticmethod
    def is_eligible(age):
        if age>=18:
            print("eligible")
        else:
            print("not eligible")


c1 = Citizen()

c1.is_eligible(18)