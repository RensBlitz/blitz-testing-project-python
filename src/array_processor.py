class ArrayProcessor:
    def sum_array(self, arr):
        """Return the sum of all elements in the array."""
        return sum(arr)

    def find_max(self, arr):
        """Return the maximum value in the array."""
        if not arr:
            raise ValueError("Array cannot be empty")
        return max(arr)

    def find_min(self, arr):
        """Return the minimum value in the array."""
        if not arr:
            raise ValueError("Array cannot be empty")
        return min(arr)

    def filter_even(self, arr):
        """Return a new array containing only even numbers."""
        return [x for x in arr if x % 2 == 0]

    def filter_odd(self, arr):
        """Return a new array containing only odd numbers."""
        return [x for x in arr if x % 2 != 0]

    def reverse_array(self, arr):
        """Return a reversed copy of the array."""
        return arr[::-1]

    def remove_duplicates(self, arr):
        """Return a new array with duplicates removed, preserving order."""
        seen = set()
        result = []
        for item in arr:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result