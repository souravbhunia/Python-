try:
    fileptr=open("file7.txt","w")
    print("success")
    fileptr.write("Sourav Bhunia")
    content=fileptr.read()
    print(content)
    
  
except Exception as e:
    print("error")

finally:
    print("cool it's just okk")


