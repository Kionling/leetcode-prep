# Week 1-2  

## 📌 Week 1: Arrays & Hashing Study Plan  

**Goal:** Build strong fundamentals in arrays and hashmaps while improving problem-solving skills.  

### ✅ Key Techniques to Learn:  
- Iterating over arrays (`for`, `while`, `enumerate`)  
- Using HashMaps (`dict`) for fast lookups  
- Using HashSets (`set()`) for uniqueness  
- Sorting & Two Pointers  
- Frequency Counting with `Counter()`  

---

## 📌 Day 1: Arrays & Iteration  

### **Concepts to Learn**  
- Basic array operations (indexing, slicing)  
- Iterating over arrays using loops  
- Using `enumerate()` for index-value pairs  
- Sorting & Two Pointers technique  

### **📝 Problems**  
1️⃣ **Two Sum**  
🔗 [LeetCode: Two Sum](https://leetcode.com/problems/two-sum/)  
✅ Use HashMap to find pairs in O(n) time.  

2️⃣ **Best Time to Buy and Sell Stock**  
🔗 [LeetCode: Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)  
✅ Track min price while iterating.  

3️⃣ **Contains Duplicate**  
🔗 [LeetCode: Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)  
✅ Use HashSet for O(n) time complexity.  

---

## 📌 Day 2: HashMaps & Frequency Counting  

### **Concepts to Learn**  
- Using HashMap (`dict`) for fast lookups  
- Tracking counts with `Counter()`  
- When to use `defaultdict`  

### **📝 Problems**  
4️⃣ **Valid Anagram**  
🔗 [LeetCode: Valid Anagram](https://leetcode.com/problems/valid-anagram/)  
✅ Use HashMap to count character frequencies.  

5️⃣ **Group Anagrams**  
🔗 [LeetCode: Group Anagrams](https://leetcode.com/problems/group-anagrams/)  
✅ Use HashMap with sorted keys.  

6️⃣ **Top K Frequent Elements**  
🔗 [LeetCode: Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)  
✅ Use HashMap + Heap (`heapq.nlargest`).  

---

## 📌 Day 3: HashSet & Unique Elements  

### **Concepts to Learn**  
- Using `set()` to track unique elements  
- Checking for duplicates in O(1)  
- Using HashSet for fast lookups  

### **📝 Problems**  
7️⃣ **Longest Consecutive Sequence**  
🔗 [LeetCode: Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)  
✅ Use HashSet to check sequence efficiently.  

8️⃣ **Intersection of Two Arrays**  
🔗 [LeetCode: Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/)  
✅ Use HashSet for O(n) time complexity.  

9️⃣ **Happy Number**  
🔗 [LeetCode: Happy Number](https://leetcode.com/problems/happy-number/)  
✅ Use HashSet to track seen numbers in cycles.  

---

## 📌 Day 4: Sorting & Two Pointers  

### **Concepts to Learn**  
- Sorting an array (`nums.sort()`)  
- Two-pointer technique for pairs/triplets  
- Handling duplicate values efficiently  

### **📝 Problems**  
🔟 **3Sum**  
🔗 [LeetCode: 3Sum](https://leetcode.com/problems/3sum/)  
✅ Use Sorting + Two Pointers to reduce O(n³) → O(n²).  

1️⃣1️⃣ **Valid Palindrome**  
🔗 [LeetCode: Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)  
✅ Use Two Pointers for in-place checking.  

1️⃣2️⃣ **Remove Duplicates from Sorted Array**  
🔗 [LeetCode: Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)  
✅ Use Two Pointers to modify array in O(n).  

---

## 📌 Day 5: Prefix Sum & Running Sum  

### **Concepts to Learn**  
- Using prefix sum for range calculations  
- Handling subarray problems efficiently  

### **📝 Problems**  
1️⃣3️⃣ **Find Pivot Index**  
🔗 [LeetCode: Find Pivot Index](https://leetcode.com/problems/find-pivot-index/)  
✅ Use prefix sum to check balance point.  

1️⃣4️⃣ **Running Sum of 1D Array**  
🔗 [LeetCode: Running Sum](https://leetcode.com/problems/running-sum-of-1d-array/)  
✅ Use prefix sum for O(n).  

1️⃣5️⃣ **Subarray Sum Equals K**  
🔗 [LeetCode: Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)  
✅ Use HashMap (`dict`) to track prefix sums.  

---

## 📌 Day 6: Sliding Window  

### **Concepts to Learn**  
- Expanding & contracting window size  
- Handling substring & subarray problems  

### **📝 Problems**  
1️⃣6️⃣ **Longest Substring Without Repeating Characters**  
🔗 [LeetCode: Longest Substring](https://leetcode.com/problems/longest-substring-without-repeating-characters/)  
✅ Use HashSet + Two Pointers.  

1️⃣7️⃣ **Maximum Sum Subarray of Size K**  
🔗 [LeetCode: Maximum Sum Subarray](https://leetcode.com/problems/maximum-subarray/)  
✅ Use Sliding Window for O(n).  

1️⃣8️⃣ **Minimum Window Substring**  
🔗 [LeetCode: Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)  
✅ Use HashMap for character frequencies.  

---

## 📌 Day 7: Mock Interview & Review  

### **Tasks:**  
✔ Redo 3 problems that you struggled with.  
✔ Try solving 1-2 problems under 30-40 min (simulate an interview).  
✔ Write down patterns you noticed.  
✔ Review all key concepts learned.  

---

## 📌 Summary of Week 1  

| Day  | Topic                  | Key Concept                           | Example Problems |
|------|-------------------------|--------------------------------------|-----------------|
| Day 1 | Arrays & Iteration      | Iterating, Sorting, Two Pointers     | Two Sum, Stock Buy/Sell, Contains Duplicate |
| Day 2 | HashMaps               | Frequency Count, Grouping            | Valid Anagram, Group Anagrams, Top K Elements |
| Day 3 | HashSet                | Unique Elements, Cycles              | Longest Consecutive Sequence, Happy Number |
| Day 4 | Sorting & Two Pointers | Pair/Triplet Search                  | 3Sum, Palindrome, Remove Duplicates |
| Day 5 | Prefix Sum             | Efficient Range Queries              | Pivot Index, Running Sum, Subarray Sum K |
| Day 6 | Sliding Window         | Expanding/Contracting Windows        | Longest Substring, Max Subarray, Min Window |
| Day 7 | Mock Interview         | Review & Debugging                   | Reattempt hard problems |

---

## 📌 Next Steps  

✅ Start solving at least **2 problems per day**.  
✅ Time yourself (**30-40 min per problem**).  
✅ Track mistakes & learn patterns.  


# Notes

![enumerate and range](/images/enumerate%20and%20range.png)

**Enumerate Example**
```
arr = [10, 20, 30, 40, 50]

for index, value in enumerate(arr):
    print(f"Index {index}, Value {value}")
```


# Range for loop tips
![range](/images//range%20notes.png)

**Out of bounds accounted. Checking for one element beyond current index**
```
arr = [3, 5, 7, 9, 10]

for i in range(len(arr) - 1):  # Stops at second-to-last element
    if arr[i] > arr[i + 1]:  # Compare current and next element
        print("Array is not sorted")
        break
else:
    print("Array is sorted")  # ✅ Output: Array is sorted
```


# While loop

```
num = int(input("Enter a positive number: "))

while num <= 0:  # Keep asking if input is negative or zero
    print("Invalid input! Try again.")
    num = int(input("Enter a positive number: "))

print(f"You entered: {num}")  # ✅ Correct input
```

**Input Validation**
```
while True:
    command = input("Enter command (type 'exit' to stop): ")
    if command.lower() == "exit":  
        break  # Stops the loop
    print(f"You entered: {command}")
```
**While loop finding the max value**
```
def find_max(arr):
    if not arr:
        return None
    max_value = arr[0]
    i = 1

    while i < len(arr):
        if arr[i] > max_value:
            max_value = arr[i]
        i += 1
    return max_value
```

# Regular For Loop
Checks for even numbers
```
def count_evens(arr):
    count = 0
    for num in arr:
        if num % 2 == 0:
            count += 1
    return count
```
Finds occurrances of target
```
def count_occur(arr, target):
    count = 0
    for num in arr:
        if num == target:
            count += 1
    return count
```
---

# 🗺️ Hashmap notes

## When to use
✅ Fast Lookups (O(1))
✅ Fast Insertions & Deletions (O(1))
✅ Counting Frequencies
✅ Mapping Keys to Values



**Creating a dictionary**
```
my_dict = {"name": "Alice", "age": 25, "city": "NYC"}
```
**Accessing Values**
```
print(my_dict.get("age"))  # 25
```

**Adding and updating values**
```
my_dict["country"] = "USA"  # Add new key-value pair
my_dict["age"] = 26  # Update existing key
print(my_dict)
```

**Removing**
my_dict.pop("city")  # Removes 'city'

**Looping**
```
for key in my_dict:
    print(key, my_dict[key])
```

**looping through key-value pairs**
```
for key, value in my_dict.items():
    print(f"{key}: {value}")
```
**Looping through values**
```
for value in my_dict.values():
    print(value)
```

**Dictionary Comprehension**
```
squares = {num: num**2 for num in range(1, 6)}
```

## Examples
Counts the number of word occurrences
```
def word_count(words):
    count_dict = {}
    for word in words:
        if word in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1
    return count_dict
```
**Other method Using Counter**
```
def word_count(words):
    return dict(Counter(words))
```


# Two Pointers Technique & Sorting
**The algorithm**
Two Pointers in opposite directions
```
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1  # Two Pointers

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return (arr[left], arr[right])  # Found the pair!
        elif current_sum < target:
            left += 1  # Move left pointer forward
        else:
            right -= 1  # Move right pointer backward

    return None  # No pair found

print(two_sum_sorted([1, 2, 3, 4, 6], 6))  # Output: (2, 4)
```

**Two pointers same direction**
```
def merge_sorted_lists(arr1, arr2):
    i, j = 0, 0
    merged = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    merged.extend(arr1[i:])
    merged.extend(arr2[j:])
    
    return merged

print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  
# Output: [1, 2, 3, 4, 5, 6]
```
----
```
arr = [3, 1, 4, 1, 5, 9]
sorted_arr = sorted(arr)  # Default: Ascending order
print(sorted_arr)  # [1, 1, 3, 4, 5, 9]
```
* This uses the Sort() method to sort a unsorted array. 
# Two Pointers Three Sum
```
def three_sum(nums):
    """
    Given an integer array nums, return all unique triplets [nums[i], nums[j], nums[k]]
    such that i != j, i != k, j != k, and nums[i] + nums[j] + nums[k] == 0.

    Input: nums = [-1, 0, 1, 2, -1, -4]
    Output: [[-1, -1, 2], [-1, 0, 1]]
    """
    # TODO: Implement using the two pointers approach
    nums.sort()
    result = []
    
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])

                left += 1
                right -= 1
                
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1 
                    
            elif total < 0:
                left += 1 
            else:
                right -= 1
       
    return result
    
print(three_sum([-1, 0, 1, 2, -1, -4]))
```

# Two pointers 4sum
```
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left, right = j + 1, len(nums) - 1

                while left < right:
                    four_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if four_sum == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif four_sum < target:
                        left += 1
                    else: 
                        right -= 1
        return result
```


**Sorting in descending order**
```
sorted_desc = sorted(arr, reverse=True)
print(sorted_desc)  # [9, 5, 4, 3, 1, 1]
```
-----
# HashSets 

* Does not store duplicates
* Fast lookups

## When to use a Hash Set
✅ Fast Lookups (O(1))
✅ Removing Duplicates
✅ Membership Testing (if x in set)
✅ Finding Common Elements


```
#Creating a set 
my_set = {1, 2, 3, 4}

#Creating an empty set 
my_set = set()


print(my_set)
print(empty_set)
```
* An empty set initializes: {}

## Adding 

```
my_set.add(5)
print(my_set)  # {1, 2, 3, 4, 5}
```

## Removing

```
val = my_set.pop()  # Removes a random element
print(val, my_set)
```

## Checking for elements

```
if 3 in my_set:
    print("3 is in the set!")
```

## Set operations
Sets support union, intersection, and difference
Returns a new set containing all unique elements
```
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1 | set2)  # {1, 2, 3, 4, 5}
print(set1.union(set2))  # Same output
```
## Intersection
Returns common elements between two sets
```
print(set1 & set2)  # {3}
print(set1.intersection(set2))  # Same output
```

## Difference
Returns elements that are only in the first set
```
print(set1 - set2)  # {1, 2}
print(set1.difference(set2))  # Same output
```
## Symmetric difference
Retunrs elements that are in either set, but not both
```
print(set1 ^ set2)  # {1, 2, 4, 5}
print(set1.symmetric_difference(set2))  # Same output
```
## Example use
Converting between sets and lists
```
nums = [1, 2, 2, 3, 3, 4]
unique_nums = set(nums)
print(unique_nums)  # {1, 2, 3, 4}

#Convert back to list
unique_list = list(unique_nums)
print(unique_list)  #[1, 2, 3, 4]
```

## Looping through a set
```
for num in my_set:
print(num)
```

## Set comprehension 
```
squared_set = {x**2 for x in range(5)}
print(squared_set)  # {0, 1, 4, 9, 16}
```

## Problems 
Finding duplications with a Hash Set
```
def find_duplicates(nums):
    seen = set()
    duplicates = set()

    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return duplicates

print(find_duplicates([1, 2, 3, 4, 2, 5, 6, 3]))  
# Expected: {2, 3}
```

Finding common elements
```
def common_elements(list1, list2):
    # Convert both lists to sets and find the intersection
    return set(list1) & set(list2)

# Test case
print(common_elements([1, 2, 3], [2, 3, 4]))  
# Expected output: {2, 3}
```
* Use the set intersection (&) operator to find elements that exist in both sets.
* Return the intersection set, which contains only the common elements.
 **Time complexity:**
* Converting lists to sets: O(n) + O(m)
* Finding the intersection: O(min(n, m))
* Overall complexity: O(n + m) (much faster than nested loops O(n*m)).

Removing duplicates
```
def remove_duplicates(arr):
    return set(arr)
print(remove_duplicates([1, 1, 2, 2, 3, 4, 4, 5]))  
# Expected: [1, 2, 3, 4, 5]
```

# Sliding window
✅ Use When:
* You're working with contiguous chunks of data (substrings, subarrays).

* You need to find the maximum/minimum/longest/shortest subsequence or window that meets some dynamic constraint.

* You need to track state within a moving section of a list (e.g., sum, distinct characters, frequency).
## The Algorithm
```
# Longest substring without repeating characters
s = "abcabcbb"
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        sett = set()
        max_len = 0 

        for right in range(len(s)):
            while s[right] in sett:
                sett.remove(s[left])
                left += 1 
            window = (right - left) + 1
            max_len = max(max_len, window)
            sett.add(s[right])
        return max_len
```
Finding the max average with a fixed window size 

```
 def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        curr_sum = 0
        left = 0
        right = len(nums)

        for i in range(k):
            curr_sum += nums[i]
        max_avg = curr_sum / k 

        for i in range(k , right):
            curr_sum += nums[i]
            curr_sum -= nums[i-k]
            avg = curr_sum / k 
            max_avg = max(max_avg, avg)
        return max_avg 
```

# Hash Maps & Sets

## Contains duplicates
```
def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
```

## Happy Number 
```
def isHappy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d)**2 for d in str(n))
    return n == 1
```

# Binary Search

## Iterative

```
def binary_search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid  # Found!
        elif nums[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half

    return -1  # Not found
```
## Recursive 
```
def binary_search_recursive(nums, target, left, right):
    if left > right:
        return -1  # Base case: not found

    mid = (left + right) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binary_search_recursive(nums, target, mid + 1, right)
    else:
        return binary_search_recursive(nums, target, left, mid - 1)
```

## First Bad Version
```
def firstBadVersion(n: int) -> int:
    left, right = 1, n

    while left < right:
        mid = (left + right) // 2

        if isBadVersion(mid):
            right = mid  # potential answer, search left
        else:
            left = mid + 1  # must be after mid

    return left  # left == right, first bad version
```

## Search Insert Position
```
def searchInsert(self, nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left
```


# Stacks and Queues
Implements a Last In First Out (LIFO) principle
## Basic Stack Implementation
```
stack = []

# Push
stack.append('A')
stack.append('B')
stack.append('C')
print("Stack: ", stack)

# Pop
element = stack.pop()
print("Pop: ", element)

# Peek
topElement = stack[-1]
print("Peek: ", topElement)

# isEmpty
isEmpty = not bool(stack)
print("isEmpty: ", isEmpty)

# Size
print("Size: ",len(stack))
```


## Valid Parentheses (Stack)
```
def is_valid_parentheses(s: str) -> bool:
    # Dictionary to map closing brackets to corresponding opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []
    
    for char in s:
        if char in bracket_map.values():
            # If it is an opening bracket, push onto the stack
            stack.append(char)
        elif char in bracket_map:
            # If it's a closing bracket, check if the stack is not empty and matches the top element
            if not stack or stack.pop() != bracket_map[char]:
                return False
        else:
            # If the character is not a bracket (optional handling based on the problem statement)
            continue
    
    # If the stack is empty, all opening brackets have been matched
    return len(stack) == 0

# Test cases
print(is_valid_parentheses("({[]})"))  # Expected output: True
print(is_valid_parentheses("({[)]}"))  # Expected output: False
print(is_valid_parentheses(""))        # Expected output: True
```

## Min Stack
```
class MinStack:
    def __init__(self):
        """
        Initialize two stacks:
        - self.stack: to store the actual values.
        - self.min_stack: to store the minimum value at each push.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        # Push the new element onto the min_stack if it's the first element
        # or if it's smaller than the current minimum.
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
        else:
            # Else, push the current minimum again.
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        # Pop from both stacks.
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()

    def top(self) -> int:
        # Return the top element of the main stack.
        if self.stack:
            return self.stack[-1]
        raise IndexError("Stack is empty")

    def getMin(self) -> int:
        # Return the top element of the min stack which is the current minimum.
        if self.min_stack:
            return self.min_stack[-1]
        raise IndexError("Stack is empty")

# Example usage:
if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print("Current Min:", minStack.getMin())   # Expected output: -3
    minStack.pop()
    print("Top:", minStack.top())              # Expected output: 0
    print("Current Min:", minStack.getMin())   # Expected output: -2

```

# Queues 
Implements a First In First Out Principle (FIFO)
* Primary Operations:

* Enqueue: Add an element to the back of the queue.

* Dequeue: Remove an element from the front of the queue.

* Peek/Front: Look at the element at the front without removing it.

* isEmpty: Check if the queue is empty.

* sSize: Optionally, track the number of elements in the queue.


## Basic Implementation 
```
from collections import deque

# Create a queue
queue = deque()

# Enqueue elements
queue.append('A')
queue.append('B')
queue.append('C')

print("Initial queue:", list(queue))

# Dequeue elements
first = queue.popleft()  # 'A' is removed
print("Dequeued element:", first)
print("Queue after dequeue:", list(queue))

# Peek at the front element without removing it
if queue:
    front = queue[0]
    print("Front element:", front)
```

# Implementing a queue using stacks
```
class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        return self.s1.pop()

    def peek(self) -> int:
        return self.s1[-1]
        

    def empty(self) -> bool:
        return not self.s1
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
```

## Time needed to buy tickets:
```
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque()

        # Initialize the queue with ticket indices
        for i in range(len(tickets)):
            queue.append(i)

        time = 0

        # Loop until the queue is empty
        while queue:
            # Increment the time counter for each iteration
            time += 1

            # Get the front element of the queue
            front = queue.popleft()

            # Buy a ticket for the front person
            tickets[front] -= 1

            # If person k bought all their tickets, return time
            if k == front and tickets[front] == 0:
                return time

            # Re-add the current index to the queue for the next iteration
            if tickets[front] != 0:
                queue.append(front)

        return time
```

# Linked List

## Reversing Linked List 

```
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # Initialize previous pointer to None and current pointer to head
        # Example:
        #   List: head -> [1] -> [2] -> [3] -> None
        #   prev = None, curr = [1]
        prev = None
        curr = head
        
        # Iterate until curr becomes None (end of list)
        while curr:
            # Save the next node
            # For curr = [1] -> [2] -> [3] -> None, next_temp = [2] -> [3] -> None
            next_temp = curr.next
            
            # Reverse the current node's pointer:
            # Change curr.next from pointing to [2] to pointing to prev (initially None)
            # Now [1] -> None
            curr.next = prev
            
            # Move the prev pointer forward:
            # prev now becomes the current node ([1])
            prev = curr
            
            # Move the current pointer to the next node in original list:
            # curr becomes next_temp, i.e., [2] -> [3] -> None
            curr = next_temp
            
            # Visual after first iteration:
            #   Reversed part: None <- [1]
            #   Remaining part: [2] -> [3] -> None
            #
            # Second iteration:
            #   prev = [1] -> None, curr = [2] -> [3] -> None
            #   Save next_temp = [3] -> None
            #   Reverse pointer: [2].next now points to [1] (prev)
            #   List becomes: None <- [1] <- [2]
            #   And so on...
        
        # When curr is None, the entire list has been reversed.
        # prev points to the new head of the reversed list.
        return prev
```

## Reverse A Linked List
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        cur = prev.next
        for _ in range(right - left):
            temp = cur.next
            cur.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next
```
