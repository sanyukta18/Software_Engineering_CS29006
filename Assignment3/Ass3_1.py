#!/usr/bin/env python
# coding: utf-8

# In[102]:


# In this python file, only the definations for the magic functions and the basic operations
# for the question segments are provided. There may be the need to add new functions or overload 
# existing ones as per the question requirements.

def Cloning(li1): 
    li_copy = li1[:] 
    return li_copy 

class Vector:
     
    def __init__(self, *args): 
        self._coords=[] 
        self._l = 0
        if(len(args)!=0):
                lst=args[0]
    #         print("lst: ",lst)
    #        print(type(lst))
                if isinstance(lst, list): 
    #              print(lst[2])
                    l = len(lst)
                    self._l = l
    #             print("length is :",end = " ")
    #             print(l,end = " ")
                    i = 0
    #           i print(lst[2])= 0
            # if arg is an int(dimension)
                    while(True):
                        self._coords.append(lst[i])
                        i+=1
    #                 print("i is: ",end = " ")
    #                 print(i)
                        if i == int(l):
                            return 

                if isinstance(lst,int):
                    self._l = 1
                    self._coords.append(lst)
                    return
            
#     def get_coords(self):
#         return self.

    def __len__(self):
        # return the dimension of the vector
        return len(self._coords)

    def __getitem__(self, j):
        # return the jth coordinate of the vector
        return self._coords[j]

    def __setitem__(self, j, val):
        # set the jth coordinate of vector to val
        self._coords[j]=val

    def __add__(self, other):
        # u + v
        r1 = [] 
#         s1 = len(self._coords)
#         s2 = len(other._coords)
        i = 0 
        if self._l == other._l:
             while i < self._l: 
                r = self._coords[i]+other._coords[i]
                r1.append(r)
                i = i+1
                
        return r1
        
    def __eq__(self, other):
        # return True if vector has same coordinates as other
#         s1 = len(self._coords)
#         s2 = len(other._coords)
#         i = 0
#         if(s1!=s2):
#             return False 
#         else:
            i=0
            while i<len(self._coords):
                if(self._coords[i]!=other._coords[i]):
                    return False
                i = i+1
            return True 
        
        
    def __ne__(self, other):
        # return True if vector differs from other
#         s1 = len(self._coords)
#         s2 = len(other._coords)
        i = 0
        if(self._l != other._l):
            return True 
        else: 
            while i<self._l:
                if(self._coords[i]!=other._coords[i]):
                    return True
                i = i+1
            return False
    
    def __str__(self):
        # return the string representation of a vector within <>
#         print("in")
        s1  = "<"
        l = self._l
        i = 0
        while i<l:
#             print("in2")
            k = "% s" % self._coords[i]
            s1 = s1+k
            if i != l-1 :
                s1 = s1 + ","
            i = i+1
        s1 = s1 + ">"
#         print("exit")
#         print(s1)
        return s1

    def __sub__(self, other):
        # Soln for Qs. 2
        r1 = Vector() 
        s1 = len(self._coords)
        s2 = len(other._coords)
        i = 0 
        if s1 == s2:
            while i < s1: 
                r = self._coords[i]-other._coords[i]
                r1._coords.append(r)
                i = i+1
            
        return r1
    
    def __neg__(self):
        # Soln for Qs. 3
        r1 = Vector()
        l = len(self._coords)
        i = 0
        while i<l:
            j = self._coords[i]*(-1)
            r1._coords.append(j)
            i = i+1
            
        return r1 
    
    def __mul__(self, value):
        
        if isinstance(value,int):
            r1 = Vector()
            l = len(self._coords)
            i = 0
            while i<l:
                j = self._coords[i]*(value)
                r1._coords.append(j)
                i = i+1

            return (r1) 
        
        else:
            i = 0
            r = -1
#             print("DDDDDD")
    #         l1 = len(self._coords)
    #         l2 = len(other._coords)
            if self._l == value._l:
                r = 0
#                 print("self_l is ",end = " ")
#                 print(self._l)
                while i<self._l:
                    r = r+(self._coords[i])*(value._coords[i])
                    i = i+1
#                     print("r is : ",end = " ")
#                     print(r)
                    
            return r
    
    def __rmul__(self,value):
        r1 = Vector()
        l = self._l
        i = 0
        while i<l:
            j = self._coords[i]*(value)
            r1._coords.append(j)
            i = i+1
            
        return (r1) 
    
#     def __mul__(self, other):
#         # Soln for Qs. 4, 5 and 6
#         i = 0
#         r = -1
# #         l1 = len(self._coords)
# #         l2 = len(other._coords)
#         if self._l == other._l:
#             r = 0
#             while i<self._l:
#                 r = r+(self._coords[i])*(other._coords[i])
#                 i = i+1
#                 self._coords
#         return r

def print_v(a):
        i = 0
        while i< len(a._coords):
#             print("Hii")
            
            if i!=(len(a._coords)-1):
                print(a[i])
                print(",",end = " ")
            else:
                print(a[i])
            i = i+1
#         print("Byee")  
#         print(" ")     
def main():
    print("Making v1")
    v1 = Vector(5)
    print("Making v2")
    v2 = Vector (7)
    print("Making v3")
    v3 = Vector([1,2,3,4,5])

    # Add suitable print statements to display the results
    # of the different question segments
    
    #print length
    print("length of vector v1 is: ")
    print(len(v1))
#     print("\n")
    
    #returning coordinate at j
    j = input("Give value of co-ordinate to return in v3\n")
    print(v3[int(j)])
#     print("\n")
    
    #setting item at co-ordinate j
    k = input("Give value of co-ordinate to assign to in v3\n")
    val = input("Give value to be assigned to co-ordinate\n")
    v3[int(j)] = int(val)
    print("New value of v3 at index j is: ")
    print(v3[int(j)])
#     print("\n")
    
    #adding v1 and v2
    print("Sum of v1 = 5 and v2 = 7 is: ") 
    r1 = Cloning(v1+v2)
    Sum = Vector (*r1) 
    print_v(Sum)
#     print("\n")
    
    #equating two vectors 
    print("Vectors v1 and v2 ",end = " ")
    if(v1 == v2):
        print("are equal")
    else:
        print("are not equal")
#     print("\n")
    
    #non-equating magic function
    print("Vectors v1 and v2 ",end = " ")
    if(v1 != v2):
        print("are not equal")
    else:
        print("are equal")
#     print("\n")
    
    #making string of vector and printing it
    print("Vector v3 as string is: ")
    print(str(v3))
    
#     print("\n")
    
    #Subtracting two vectors and printing the output
    print("Subtracting v2 and v1 gives: ")
    print_v(v2-v1)
#     print("\n")
    
    #negating a vector
    print("negating v1 gives: ")
    print_v(-v1)
#     print("\n")
    
    #multiplying a vector and a value
    print("Multiplying v1 with 3,(v1*3) i.e 5*3 = ")
    print_v(v1*3)
#     print("\n")
    print("Multiplying v1 with 3,(3*v1) i.e 3*5 = ")
    print_v(3*v1)
#     print("\n")
    
    #Scalar multiplication of v1 and v2
    print("Scalar multiplication of v1 and v2 i.e 5*7 = ")
    print(v1*v2)
#     print("\n")
    
    

if __name__ == '__main__':
    main()


# In[ ]:




kk=[1,2,3,4]
print(type(kk))
print(kk[2])


# In[ ]:




