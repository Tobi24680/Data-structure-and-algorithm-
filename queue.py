class Q:
    def __init__(self,size):
        self.queue=[None]*size
        self.size=size
        self.front=-1
        self.rear=-1
    def isempty(self):
        return self.front==-1
    def isfull(self):
        return self.rear==self.size-1
    def top(self):
        if self.isempty():
            print("empty")
        else:
            print(f'front item is {self.queue[0]}')
    def eq(self,item):
        if self.isfull():
            print("full")
            return
        if self.front==-1:
            self.front=0
        self.rear+=1
        self.queue[self.rear]=item
        print(f'eq{item}')
    def dq(self):
        if self.isempty():
            print('empty')
            return
        dqitem=self.queue[self.front]
        print(f'dq{dqitem}')
        
        if self.front==self.rear:
            self.front=-1
            self.rear=-1
        else:
            self.front+=1
        return dqitem
    def display(self):
        if self.isempty():
            print("q is empty")
        else:
            print('q',self.queue[self.front:self.rear+1])
def menu():
    print("***queue operation***\n1.enque\n2.dequeue\n3.top\n4.display\n5.exit")
if __name__=="__main__":
    size=int(input("enter"))
    q=Q(size)
    while True:
        menu()
        choice=int(input('enter choice'))
        if choice == 1:
            item=int(input("enter item to enq"))
            q.eq(item)
        elif choice == 2:
            q.dq()
        elif choice==3:
            q.top()
        elif choice ==4:
            q.display()
        elif choice==5:
            print("exit")
            break
        else:
            print("invalid")
        