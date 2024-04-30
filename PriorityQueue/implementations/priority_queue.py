import PriorityQueue.classes.linked_list as linked_list
import patients


priority_queue = linked_list.LinkedList()
priority_queue.add_patient(priority_queue.head, patients.patient1), priority_queue.add_patient(priority_queue.head, patients.patient2),
priority_queue.add_patient(priority_queue.head, patients.patient3), priority_queue.add_patient(priority_queue.head, patients.patient4),
priority_queue.add_patient(priority_queue.head, patients.patient5), priority_queue.add_patient(priority_queue.head, patients.patient6),
priority_queue.add_patient(priority_queue.head, patients.patient7), priority_queue.add_patient(priority_queue.head, patients.patient8),
priority_queue.add_patient(priority_queue.head, patients.patient9), priority_queue.add_patient(priority_queue.head, patients.patient10),
priority_queue.add_patient(priority_queue.head, patients.patient11)

priority_queue.update_group_priority(priority_queue.head)
priority_queue.traverse()
