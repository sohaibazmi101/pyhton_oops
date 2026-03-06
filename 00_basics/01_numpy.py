import numpy as np

class NumPyBasics:
    def __init__(self):
        pass

    def create_array(self):
        a = np.array([1,2,3,4,5])
        print(a)
        print(type(a))
        b = np.array([[1,2,3],
                      [4,5,6]])
        print("b: ", b)
        print(type(b))

        # Useful Creators

        print(np.zeros((3,3)))    # This creates 3x3 array matrix with float as a datatypes with values all 0.
        print(np.zeros((3,3), dtype=int)) # This creates 3x3 array Matrix with datatype int with all values as 0
        print(np.ones((3,4))) # This creates array matrix of 3x4 with all values 1. and data types is float.
        print(np.ones((3,4)).dtype) # This must return float64 or floatxx.
        print(np.ones((3,4), dtype=int)) # This creates with data type int
        print(np.ones((3,4), dtype=int).dtype) # Return int64
        print("np.eye(3): \n",np.eye(3)) # This creates identity matrix of 3x3 with datatypes float
        print("np.eye(3, dtypes=int): \n", np.eye(3, dtype=int))
        print(np.arange(0,10,2)) # This creates an array starting from 0 upto 10 (not included) with step 2
        print(np.arange(0,10,2).dtype) # Return int64
        print(np.linspace(10,20,5)) # This creates 5 values in an array with equal spaced between 10 and 20 (included both)
        print("\nRandom.rand(3,3): \n",np.random.rand(3,3)) # This creates a 3x3 matrix with all values between 0 and 1.
        print("\nnp.random.randint(1,10(2,2)): \n", np.random.randint(1,10,(2,2)))
        # This creates matrix of size 2x2 of all values between 1,10

        # Array Properties

        print("Array Properties")

        a = np.array([[1,2,3,4],[3,4,5,6]])
        print(a)
        print(a.shape) # Return (2,4)
        print(a.ndim) # Return number of rows
        print(a.size) # Return size of array (elements)
        print(a.dtype) # Return datatypes

        b = np.array([1,2,3,4,5,6,7])
        print(b[0])
        print(b[2])
        print(b[-1]) # Return lsat element of the array
        print(b[1:3])
        print("Mean: ",np.mean(a))

        # Vectorization

        c = [1,2,3,4,5]
        result = []
        for i in c:
            result.append(i * 2)
        print(result)

        d = np.array([1,2,3,4,5])
        res = d * 2
        print(res)

        a = np.array([1,2,3,4,5])
        b = np.array([5,6,7,8,9])
        print("Array Ops: \n")
        print(a + b)
        print(a - b)
        print(a * b)
        print(a / c)
        print(a % b)

        print("Mathematical Formulae: ")
        print(np.sqrt(a))
        print(np.log(a))
        print(np.exp(a))
        print(np.sin(a))
        print(np.std(a))


    def menu(self):
        while True:
            print("__________________MENU_ITEMS________________")
            print("1. Create Array")
            choice = input("Enter Your Choice: ")
            if choice == "0":
                exit()
            elif choice == "1":
                self.create_array()

if __name__ == "__main__":
    npb = NumPyBasics()
    npb.menu()