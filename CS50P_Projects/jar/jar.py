class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer or > 0.")
        self._capacity = capacity
        self._cookies = 0

    def __str__(self):
        return "🍪" * self._cookies

    def deposit(self, n):
        if n < 0:
            raise ValueError("Cannot deposit a negative number of cookies.")
        if self._cookies + n > self._capacity:
            raise ValueError("Not enough capacity to deposit that many cookies.")
        self._cookies += n

    def withdraw(self, n):
        if n < 0:
            raise ValueError("Cannot withdraw a negative number of cookies.")
        if self._cookies < n:
            raise ValueError("Not enough cookies to withdraw that many.")
        self._cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._cookies

def main():
    jar = Jar()
    print(f"Initial capacity: {jar.capacity}")
    print(f"Initial cookie count: {jar.size}")

    jar.deposit(5)
    print(f"Cookies added. Current cookie count: {jar.size}")

    print(f"Jar content: {str(jar)}")
    jar.withdraw(2)
    print(f"Cookies withdrawn. Current cookie count: {jar.size}")

    jar.withdraw(jar.size)
    print(f"Cookies withdrawn. Current cookie count: {jar.size}")

if __name__ == "__main__":
    main()
