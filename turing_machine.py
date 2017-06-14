"""
Contains an implementation of a Turing Machine
"""

class EndOfTapeException(IndexError):
    """
    Thrown if a Turing machine reaches an index of 0 and tries to move left,
    or if the machine reaches the right end of its tape and wants to move
    further to the right
    """
    pass

class TuringMachine(object):
    """
    Implements a Turing machine, and shows how basic operations on the machine
    are performed.

    .. note::
        Although this implementation has a finite-length tape, this is not
        required. It's just kind of hard to make an infinite-size tape in a
        finite amount of memory :) .
    """
    def __init__(self, tape_size, initial_tape_index):
        """
        Create an instance of a Turing machine

        :param int tape_size: The number of cells in the tape
        :param int initial_tape_index: The index of the cell where the head
            will start
        """
        self.memory = [0 for _ in range(0, tape_size)]
        self.index = initial_tape_index

    def __len__(self):
        """
        Returns the length of tape
        """
        return len(self.memory)

    def move_left(self):
        """
        Move the head to the left. If there is no more memory for the tape to
        move left, then raise an error
        """
        if self.index == 0:
            raise EndOfTapeException(
                    "Unable to move left, index is at 0"
                )
        self.index -= 1

    def move_right(self):
        """
        Move the head to the right. If this can't be done, raise an error.
        """
        if self.index == len(self) - 1:
            raise EndOfTapeException(
                    "Unable to move right, reached end of the tape"
                )
        self.index += 1

    @property
    def value(self):
        """
        Returns the value at the current head position
        """
        return self.memory[self.index]

    @value.setter
    def value(self, value_to_set):
        """
        Set the value at the current head position.

        :param value_to_set: The value that is to be set at that position in
        the tape
        """
        self.memory[self.index] = value_to_set

