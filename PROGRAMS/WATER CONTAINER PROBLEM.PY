''' you are given an integer array of height of length n.There are n vertical lines drawn such that the two endpoints
 of the i th line are i,0 and i,height[i].
find the two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of the water a conatiner can store.
Note : YOU MAY NOT STANT THE CONTAINER.
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.'''

li=eval(input("Enter the height: "))
s=0
e=len(li)-1
maxi=0
ar=0
while(s!=e):
    if(li[s]<li[e]):
        ar=li[s]*(e-s)
        s=s+1
    else:
        ar=li[e]*(e-s)
        e=e-1
    if(ar>maxi):
        maxi=ar
print("THE MAXIMUM CAPACITY OF THE CONTAINER: ",maxi)
