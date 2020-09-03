class Dog:
    doginfo = "dog is funny"
    def bark(self):
        print("bbbbb   bbbb")
    def shout(self, str):
        print("bbbbb   bbbb" + str)
    def sleep(self):
        print("dog is sleeping")

mydog = Dog()
mycat = Dog()

mycat.sleep()
mydog.bark()
mydog.shout(" fdsgfdsgf")
print(Dog.doginfo)
