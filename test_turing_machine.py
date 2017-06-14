"""
Contains unit tests for the Turing Machine implemented here
"""
import unittest
from turing_machine import TuringMachine, EndOfTapeException


class TestTuringMachine(unittest.TestCase):
    """
    Base class for unit tests of a Turing machine
    """
    def setUp(self):
        """
        Initialize the parameters required to instantiate a Turing machine,
        then instantiated it. The Turing machine created here will serve as
        our test fixture.
        """
        self.machine_length = 4
        self.initial_tape_index = 0

        self.machine = TuringMachine(
                self.machine_length, 
                self.initial_tape_index
        )


class TestConstructor(TestTuringMachine):
    """
    Tests that the machine was successfully instantiated
    """
    def setUp(self):
        """
        Override the setUp method in the superclass to not construct the
        Turing machine.
        """
        self.machine_length = 4
        self.initial_tape_index = 0

    def test_instantiation(self):
        """
        Tests that the Turing machine is created correctly
        """
        machine = TuringMachine(self.machine_length, self.initial_tape_index)

        self.assertEqual(self.machine_length, len(machine.memory))
        self.assertEqual(self.initial_tape_index, machine.index)


class TestLength(TestTuringMachine):
    """
    Tests that calling ``len`` on the turing machine returns the length of the
    machine's tape. 

    .. note::
        Since we're using the same setUp routine here as in our base class,
        we don't need to redefine it here. This is related to the idea of 
        object inheritance, which we will discuss later in the course.
    """
    def test_length(self):
        self.assertEqual(self.machine_length, len(self.machine))


class TestMoveLeft(TestTuringMachine):
    """
    Contains unit tests for :meth:`TuringMachine.move_left`
    """

    def test_move_left_allowed(self):
        """
        Tests that the machine successfully moves left if it the machine is
        not at the left end of its tape.
        """
        expected_final_tape_index = 0
        self.machine.index = 1

        self.machine.move_left()

        self.assertEqual(expected_final_tape_index, self.machine.index)

    def test_move_left_exception_thrown(self):
        """
        Tests that when I try moving to the left at the left end of the Turing
        Machine's tape, that a :class:`EndOfTapeException` is thrown.

        .. note::
            Notice the use of the ``with`` statement. This is called a context
            guard. It is a generalization of the ``try`` and ``except``
            statements that are used to handle exceptions in Python. Special
            methods are called when both entering and leaving a context guard.
            Context guards will be discussed in more detail later in the
            course.
        """
        self.machine.index = 0

        with self.assertRaises(EndOfTapeException):
            self.machine.move_left()


class TestMoveRight(TestTuringMachine):
    """
    Tests that moving right on the Turing machine behaves as expected
    """

    def test_move_right_allowed(self):
        expected_final_tape_index = 2
        self.machine.index = 1

        self.machine.move_right()

        self.assertEqual(expected_final_tape_index, self.machine.index)

    def test_move_right_exception_thrown(self):
        self.machine.index = len(self.machine) - 1

        with self.assertRaises(EndOfTapeException):
            self.machine.move_right()


class TestRead(TestTuringMachine):
    """
    Tests :meth:`TestTuringMachine.value`, which should read what the Turing
    machine has

    .. note::
        Note the use of operator overloading. When I read from the Turing
        Machine, it calls the method that I decorated with the ``@property``
        decorator.
    """
    def setUp(self):
        """
        Set up some dummy data for us to read. Notice that I am doing
        something similar in this test case as I did in
        :class:`TestConstructor`, but in this case, I am calling the
        ``setUp`` method of the superclass of this class. This means that
        everything in the ``setUp`` method of the superclass will get
        executed prior to my code below it.
        """
        TestTuringMachine.setUp(self)

        self.expected_read_value = 1

        self.machine.memory[self.machine.index] = self.expected_read_value

    def test_read(self):
        """
        Tests that the read method works as expected. Notice that even though
        the read method is a function, I don't need to call it to get the
        value of the machine. This is because I used ``@property`` to let the
        Python interpreter know that my method is a getter.
        """
        self.assertEqual(self.expected_read_value, self.machine.value)

class TestWrite(TestTuringMachine):
    """
    Tests that writing to the Turing Machine works as expected
    """
    def setUp(self):
        """
        Perform a similar ``setUp`` as the read test, except define some data
        to write.
        """
        TestTuringMachine.setUp(self)

        self.data_to_write = 2

    def test_write(self):
        """
        Write the data to the machine, and ensure that the data has been
        correctly written.

        .. note::
            Note the use of operator overloading in the write method. By
            flagging my method with ``@value.setter``, I have told the Python
            interpeter that the decorated method is a setter for this method.
            In doing so, I have overloaded the assignment operator for objects
            of type :class:`TuringMachine`, ensuring that the writing method
            that I defined executes when I assign a value to the Turing 
            machine.
        """
        self.machine.value = self.data_to_write

        self.assertEqual(
                self.data_to_write, 
                self.machine.memory[self.machine.index]
        )
