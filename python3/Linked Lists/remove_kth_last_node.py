from ds import ListNode

"""
Definition of ListNode:
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""
# K =2 means 2nd node from the end. leader is K nodes in front of the trailer when leader reaches the last node.
# we start by advancing the leader poointer thru the linked list for K steps
# when the leader is K nodes ahead of the trailer, we advance both pointers together
# until the leader reaches the last node. 
# edge case: what is head itself is the node we wnat to remove, we cannot do that if there is no node before head
# so we create a dummy node and place it before head and start from there.

def remove_kth_last_node(head: ListNode, k: int) -> ListNode:
    # A dummy node to ensure there's a node before 'head' in case we 
    # need to remove the head node.
    dummy = ListNode(-1)
    dummy.next = head
    trailer = leader = dummy
    # Advance 'leader' k steps ahead.  
    for _ in range(k):
        leader = leader.next
        # If k is larger than the length of the linked list, no node 
        # needs to be removed.
        if not leader:
            return head
    
    # Move 'leader' to the end of the linked list, keeping 'trailer'
    # k nodes behind.
    while leader.next:
        leader = leader.next
        trailer = trailer.next
    
    # Remove the kth node from the end.
    trailer.next = trailer.next.next
    
    return dummy.next
