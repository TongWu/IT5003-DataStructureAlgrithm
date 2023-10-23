# Student ID: A0255954R
# Full Name: Wu Tong
# Lab Group: B5
# TA: Steven Halim
import sys

# Create a DLL class
class Node:
    def __init__(self, name, partner=None):
        self.name = name
        self.partner = partner
        self.next = None
        self.prev = None


def conga(n, q, couples, instructions):
    head = None
    tail = None

    # Create double linked node
    for couple in couples:
        # Create node with name and its partner
        cp1 = Node(name=couple[0])
        cp2 = Node(name=couple[1], partner=cp1)
        cp1.partner = cp2

        # Update prev and next
        # If the node list is empty
        if head is None:
            # Add head and tail
            head = cp1
            tail = cp2
            cp1.next = cp2
            cp2.prev = cp1
        else:
            # Extend the node list
            tail.next = cp1
            cp1.prev = tail
            cp1.next = cp2
            cp2.prev = cp1
            tail = cp2

    # Set microphone holder, default at the front
    mic_holder = head
    yelled_names = []

    # Process the instructions
    for inst in instructions:
        if inst == 'F':
            # The mic holder will pass the mic to the person in front of them
            mic_holder = mic_holder.prev
            pass
        elif inst == 'B':
            # The mic holder will pass the mic to the person behind them.
            mic_holder = mic_holder.next
            pass
        elif inst == 'R':
            # Pass mic to the person behind them, if mic holder is the tail, pass to the head
            next_mic_holder = mic_holder.next if mic_holder.next else head

            if mic_holder != tail:
                # Move to the back of the line
                if mic_holder.prev:
                    mic_holder.prev.next = mic_holder.next
                else:
                    head = mic_holder.next
                mic_holder.next.prev = mic_holder.prev
                tail.next = mic_holder
                mic_holder.prev = tail
                mic_holder.next = None
                tail = mic_holder
            mic_holder = next_mic_holder
            pass
        elif inst == 'C':
            # Pass the mic to the person behind them.
            # Then, they will move to behind where their partner is
            # If mic holder is at the back of the line, mic will be passed to the front of the line
            next_mic_holder = mic_holder.next if mic_holder.next else head
            if mic_holder != tail:
                if mic_holder.prev:
                    mic_holder.prev.next = mic_holder.next
                else:
                    head = mic_holder.next
                if mic_holder.next:
                    mic_holder.next.prev = mic_holder.prev

                partner = mic_holder.partner
                mic_holder.next = partner.next
                mic_holder.prev = partner
                if partner != tail:
                    partner.next.prev = mic_holder
                else:
                    tail = mic_holder
                partner.next = mic_holder
            mic_holder = next_mic_holder
            pass
        elif inst == 'P':
            # Yell their partner's name into the mic
            yelled_names.append(mic_holder.partner.name)
            pass

    # Print out results
    for name in yelled_names:
        print(name)
    print()
    print_people = head
    while print_people:
        print(print_people.name)
        print_people = print_people.next
    pass


def solution():
    n, q = map(int, input().strip().split())
    couples = [sys.stdin.readline().strip().split() for _ in range(n)]
    inst = input().strip()
    conga(n, q, couples, inst)


solution()