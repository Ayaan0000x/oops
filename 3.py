class fruits:
    taste="sour"
    def __init__ (self,colour,shape):

        

        fruits.colour=colour

        fruits.shape=shape

    def displays(self):


        print(f"the color pf the fruit is {self.colour} and the shape of the fruit is {self.shape}")


    def displayname(self,name):

        print(f"the name of the fruit is {name} and its taste is {fruits.taste}")



object=fruits("red","sphere")

object.displayname("apple")
object.displays()
