import node
import patient


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def traverse(self):
        node = self.head
        while(node is not None):
            print(node.value)
            node = node.next

    def append(self, value, node):
        if self.head is None:
            self.head = node.Node(value)
            self.size += 1
            return
        if node.next is None:
            new_node = node.Node(value)
            node.next = new_node
            self.size += 1
            return
        self.append(value, node.next)

    def prepend(self, value):
        new_node = node.Node(value)
        self.head = new_node
        new_node.next = self.head
        self.size += 1

    def delete_at_index(self, del_index, node, pos=0):
        if del_index >= self.size: return
        elif del_index == 0:
            self.head = self.head.next
            return
        elif pos == del_index - 1:
            next_next = node.next.next
            node.next.next = None
            node.next = next_next
            return
        self.delete_at_index(del_index, node.next, pos+1)

    def add_patient(self, cur_patient: node.Node, patient_to_add: patient):
        new_patient = node.Node(patient_to_add)

        if self.head is None:
            pass
        
        if cur_patient.value.priority > patient_to_add.priority:    
            cur_patient.prev.next = new_patient
            cur_patient.prev = new_patient
            #cur_patient.prev.prev.next = new_patient
            return 