#multiply the two given arrays
import numpy as np

arr1 = [1,2,3,4,5]
arr2 = [6,7,8,9,6]

C= np.multiply(arr1,arr2)

print(C)

#missing data in np array

arr3= [9,4,6,7,np.nan,10,18,np.nan,38]

print(np.isnan(arr3))

#Write a NumPy program to test whether each element of a 1-D array is also present in a second array.

arr4 = [1,2,3,4,5]
arr5 = [1,2,3,4,5]

D= np.array_equal(arr4,arr5)

print(D)

#Write a NumPy program to save a NumPy array to a text file.

arr6 = [1,2,3,4,5]

E=np.savetxt('text,txt',arr6)
print(E)


#Write a NumPy program to Create a 1-D array of 30 evenly spaced elements between 2.5. and 6.5, inclusive.

arr7 =np.linspace(2.5,6.5,30)
print(arr7)


