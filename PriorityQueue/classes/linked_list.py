import PriorityQueue.classes.node as node
import PriorityQueue.classes.patient as patient


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def traverse(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value.__str__() + "/n")
            current_node = current_node.next

    def __delete_at_index(self, node_to_delete: node.Node):
        node_to_delete.prev.next = node_to_delete.next
        node_to_delete.next.prev = node_to_delete.prev
        node_to_delete.next = None
        node_to_delete.prev = None
        self.size -= 1

    def update_priority(self, name: str, new_priority: int, cur_node: node.Node):
        pt = cur_node.value
        if cur_node is None:
            return None
        elif pt.name == name:
            pt.priority = new_priority
            self.__delete_at_index(cur_node)
            self.add_patient(self.head, cur_node)
            return pt.__str__()
        self.update_priority(name, new_priority, cur_node.next)

    def add_patient(self, cur_patient: node.Node, patient_to_add: patient):
        new_patient = node.Node(patient_to_add)

        if self.head is None:
            self.head = new_patient
            self.tail = new_patient
            self.size += 1
            return None

        elif cur_patient is None:
            self.tail.next = new_patient
            new_patient.prev = self.tail
            self.tail = new_patient
            return

        elif cur_patient.value.priority > patient_to_add.priority:
            if cur_patient is self.head:
                self.head.prev = new_patient
                new_patient.next = self.head
                self.head = new_patient
                return None
            cur_patient.prev.next = new_patient
            cur_patient.prev = new_patient
            new_patient.next = cur_patient
            new_patient.prev = cur_patient.prev
            if new_patient.next is None:
                self.tail = new_patient
            self.size += 1
            return None
        self.add_patient(cur_patient.next, patient_to_add)

    def attend_patient(self):
        if self.head is None:
            return None
        patient_to_attend = self.head.value
        print(patient_to_attend.__str__())
        self.head = self.head.next
        self.head.prev = None
        self.size -= 1
