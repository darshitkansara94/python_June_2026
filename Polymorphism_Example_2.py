class sound():
    def animalSound(self,sound):
        print(f"animal make sound {sound}")

class dog(sound):
    def dogSound(self):
        self.animalSound("Dog barks")

class cat(sound):
    def catSound(self):
        self.animalSound("cat meow")        

c1 = [dog(), cat()]
c1[0].dogSound()
c1[1].catSound()