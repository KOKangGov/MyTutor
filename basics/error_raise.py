# error_raise.py

class Bird:
    def fly(self):
        raise NotImplementedError
    
# class Eagle(Bird):
#    pass

#eagle = Eagle()
#eagle.fly()

class Eagle(Bird):
    def fly(self):
        print("Very fast")
eagle = Eagle()
eagle.fly()
