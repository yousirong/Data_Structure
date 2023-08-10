class Node:
    def __init__(self, element):
        self.data = element
        self.link = None

def insertFront(head, e):
    node = Node(e)
    node.link = head
    head =  node
    return head

def printList(head):
    node = head
    while node != None:
        print(node.data, end = ' ')
        node = node.link
    print()
    
def linkedListPractice1():
    head = Node(10)        #head--> 10 ---> 20 ---> 30
    head.link = Node(20)
    head.link.link = Node(30)
    print(head.data, head.link.data, head.link.link.data)
    #head--> 10 ---> 20 ---> 30

   
    node = Node(50)  # node -> 50 None
    node.link = head
    head = node   #head -> 50 -> 10 -> 20  -> 30  link가 다음 head를 참조하고
    # head는 다음 node를 참조하게 하여 리스트 모델 형식을 만듦듦
    print(head.data, head.link.data, head.link.link.data, head.link.link.link.data)

    #head -> 50 -> 10 -> 20  -> 30
    #       node
    #head -> 50 -> 10 -> 20  -> 30
    #             node

    node = head   # 위 print와 같이 100번째 리스트를 출력하기 위해서는 head.link.link........link.data가
                  # 되어버림 그러므로 다음은 효과적으로 node을 불러오는 방법임
    print(node.data)
    # 50
    node = node.link
    print(node.data)
    # 10
    node = node.link
    print(node.data)
    # 20
    node = node.link
    print(node.data)
    # 30
    print(node.link)
    # None
    # print(node)
    # 위의 문장의 경우 리스트의 노드가 많아 질수록 길어질 수밖에 없음 
    # 밑의 코드처럼 while문을 써서 

    while node != None:
        print(node.data, end = ' ')
        node = node.link
    print()

# 연결리스트를 만드는 쳬계적인 방법
    
    head = None
    head = insertFront(head, 60)   # head -> 60 | None
    head = insertFront(head, 70)   #  head -> 70| link -> 60
    head = insertFront(head, 50)   # head -> 50 | link  -> 70
    head = insertFront(head, 40)   # head -> 40 | link -> 50
    # 40 50 70 70
    node = head
    while node != None:
        print(node.data, end = ' ')
        node = node.link

    print()
        
#    printList(head)

# 클래스를 이용한 연결리스트     
class LinkedList:
    def __init__(self):
        self.head = None
  
        

    def insertFront(self, e):
        node = Node(e)
        node.link = self.head
        self.head =  node

#    def insert(self,pos,e):
        
#    def delete(self,pos):

    def printList(self):
        node = self.head
        while node != None:
            print(node.data, end = ' ')
            node = node.link
        print()
            
def linkedListPractice2():
    L = LinkedList()
    L.insertFront(20)
    L.insertFront(40)
    L.insertFront(30)
    L.printList()


#linkedListPractice1()
linkedListPractice2()
#
30 40 20
    
