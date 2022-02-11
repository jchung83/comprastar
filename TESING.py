def show_excitement(str,n):
    if(n==0):
        return str
    else:
        show_excitement(str,n-1)

str="I am super excited for this course!"
print show_excitement(str,5)