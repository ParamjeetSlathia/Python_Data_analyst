import numpy as np
# print(np.__version__)

## creating arrays

# 1D array

# list1 = [1,2,3]
# print(list1)

# arr_list1 = np.array(list1)
# print(arr_list1)

# print(type(arr_list1))




# 2D array

# list1 = [1,2,3]
# list2 = [4,5,6]
# arr_list1_2 = np.array([list1,list2])
# print(arr_list1_2)


# 3D array

# list1 = [1,2,3]
# list2 = [4,5,6]
# list3 = [7,8,9]
# arr_list1_3 = np.array([[list1,list2,list3]])
# print(arr_list1_3)

# print(arr_list1_3.ndim)






# 2. numpy array attributes


# arr1 = np.array([[1,2,3],[4,5,6]])
# print(arr1)

# print("shape", arr1.shape)
# print("size", arr1.size)
# print("dType", arr1.dtype)
# print("n_dim", arr1.ndim)


# create 2 array-1D and 3D, and find it's attributes


# 1d array

# arr1 = np.array([1,2,3,4,5])
# print(arr1)

# print("shape", arr1.shape)
# print("dType", arr1.dtype)
# print("size", arr1.size)
# print("n_dim", arr1.ndim);


# 3d array

# arr1 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

# print(arr1)

# print("shape", arr1.shape)
# print("dType", arr1.dtype)
# print("size", arr1.size)
# print("n_dim", arr1.ndim)






#3. array initializing method

# zero array

# zero_arr = np.zeros((2,3))
# print(zero_arr)

# one array

# one_arr = np.ones((2,3))
# print(one_arr)

#full array

# full_arr = np.full((3,2),7)
# print(full_arr)

#identity matrix

# id_arr = np.eye(3)     #diagonal element
# print(id_arr)


#empty array
# print(np.empty(2))



# evenly spaced array
# print(np.arange(0,10,2))


#specific number of equally (spaced) values between a range
# print(np.linspace(1,10,4))



# random values array - float
# r_arr = np.random.rand(3,2)
# print(r_arr)


# random values array - int

# rint_arr = np.random.randint(1,10,(3,3))
# print(rint_arr)






#4. array indexing and slicing

# a = np.array([1,3,5,7,9])
# print(a) 
# print(a[0])
# print(a[-1])



# slicing  - A feature  that enables accessing parts of the sequence 
# syntax: array_name[start:stop:step]

# a = np.array([1,3,5,7,9])
# print(a) 

#slicing : 
#array[start:stop:step]
# stop -  index,that is not included in output
# print(a[0:3]) # first 3 element
# print(a[-3:])   # last 3 element
# print(a[1:4])     #middle element
# print(a[0::2])   #with step



# arr2 = np.array([[1,2,3],[4,5,6]])
# print(arr2)

# print(arr2[0][1])
# print(arr2[1:])
# print(arr2[:,1])

# print(arr2[:,0])

# 2D: [rows, columns]
# 3D: [layers/height,rows,columns]



# arr3 = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr3)

# print(arr[:,0])  #1st col value
# print(arr3[:,2])   # 3rd col  value


# print(arr3[::,1:2])  #slicing on columns
# print(arr3[1::,1:2])    #slicing on rows and 





# 5 array reshaping and flattening



# arr1 = np.array([1,2,3,4,5,6])
# print(arr1)

# # reshaped = arr1.reshape((6,1))   # 6 rows and 1 column
# # print(reshaped)

# reshaped2 = arr1.reshape((2,3))   # 2 rowa adn 3 column
# print(reshaped2)

# print(reshaped2.flatten())  # 1 row and 6 column mean - flatten kya krta ha multi- dimension array ko one dimension array ma convert krta ha 




# 6 array stacking and splitting
# a = np.array([1,2,3])
# b = np.array([4,5,6])

# print(np.vstack((a,b))) #vertical stacking - row wise
# print(np.hstack((a,b))) #horizontal stacking - column wise

# c = np.array([[1,2,3],[4,5,6]])
# print(c)

# split = (np.hsplit(c,3))

# for s in split:
#   print(s)  



# 7. Mathematical operations on array

# a = np.array([10,20,40,-30])
# print(a)

# print(a+10)  #add
# print(a-30)  #subs
# print(a*2)  # multiply
# print(a/10) # divide

# b = np.array([1,4,9])
# print(b)

# print(np.square(b))
# print(np.sqrt(b))
# print(np.sin(b))



# 8. mathematical operations on multiple arrays

a = np.array([1,2,3])
b = np.array([4,5,6])
print(a)
print(b)

print(np.add(a,b))
print(np.multiply(a,b))
print(np.subtract(a,b))
print(np.divide(a,b))

print(np.dot(a,b))   #dot product multiple a and b then sum
# print(a.T)

# import numpy as np
# t=np.array([[1,2,3],[4,5,6]])
# print(t)
# print(t.T)
