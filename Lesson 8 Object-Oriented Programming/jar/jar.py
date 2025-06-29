class Jar:
    def __init__(self, capacity=12):
        # Check if capacity is an int and non-negative
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        self._capacity = capacity
        self._size = 0  # Start with zero cookies

    def __str__(self):
        # Return a string with as many cookie emojis as the current size
        return "🍪" * self._size

    def deposit(self, n):
        # Add n cookies; raise error if it exceeds capacity
        if self._size + n > self._capacity:
            raise ValueError("Exceeds jar capacity")
        if n < 0:
            raise ValueError("Cannot deposit negative cookies")
        self._size += n

    def withdraw(self, n):
        # Remove n cookies; raise error if not enough cookies
        if n > self._size:
            raise ValueError("Not enough cookies to withdraw")
        if n < 0:
            raise ValueError("Cannot withdraw negative cookies")
        self._size -= n

    @property
    def capacity(self):
        # Return the capacity (read-only property)
        return self._capacity

    @property
    def size(self):
        # Return the current number of cookies in the jar (read-only)
        return self._size
