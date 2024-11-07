class Stack:
  def __int__(self,size):      
      self.stack=[None]*size
      self.top=-1
      self.size=size
  def is_full(self):
      return self.top==self.size-1
  
  def push(self,element):
      if self.is_full():
          print("stack overflow")
      else:
          self.top+=1
          self.stack[self.top]=element
          print(f'pushed {element} to stack')
          
  def pop(self):
      if self.is_empty():
          print("overflow")
      else:
          popped_element=self.stack[self.top]
          self.stack[self.top]=None
          self.top-=1
          print(f'popped {popped_element} from stack')
          return popped_element 
  def top_item(self):
      if self.is_empty():
          print("stack is empty")
      else:
          print("stack element from top to bottom")
          for i in range(self.top,-1,-1):
              print(self.stack[i])   
  def display(self):
      if self.is_empty():
          print("stack is empty")
      else:
          print("stack element from top to bottom")
          for i in range(self.top,-1,-1):
              print(self.stack[i]) 
def menu():
    print("\n ***stack***")
    print('1.push')
    print('2.pop')
    print('3.top')
    print("4.disply")
    print('5.exit')
def main():
    size=int(input("enter the size"))    
    stack=Stack(size)  
    while True: 
       menu()
       c=int(input("enter your choice"))
       if c==1:           
           element=int(input("enter element to push"))
           stack.push(element)
       elif c==2:           
          stack.pop()
       elif c==3:
          stack.top_item()
       elif c==4:
          stack.display()
       elif c==5:
          print("existing program")
       else:
           
           print("invalid")
           break
if __name__=="__main__":       
     main()
    
    


    
    
    
