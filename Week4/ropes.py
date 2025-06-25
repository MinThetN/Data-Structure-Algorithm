from Heap import heap
import sys

class RopeCutter:
    
    def __init__(self):
        self.priority_queue = None
        self.accumulated_expense = 0
        self.operation_count = 0
    
    def initialize_rope_data(self, rope_lengths):
        """Initialize the heap with rope lengths"""
        if not rope_lengths or len(rope_lengths) < 2:
            return False
        
        # Create a copy to avoid modifying original data
        rope_data = [length for length in rope_lengths if length > 0]
        self.priority_queue = heap(items=rope_data)
        self.accumulated_expense = 0
        self.operation_count = 0
        return True
    
    def perform_single_merge(self):
        """Merge two smallest ropes and return the cost"""
        if self.priority_queue.heapsize < 2:
            return 0
        
        # Extract the two shortest ropes
        first_rope = self.priority_queue.extract()
        second_rope = self.priority_queue.extract()
        
        # Calculate merge cost
        merge_cost = first_rope + second_rope
        self.accumulated_expense += merge_cost
        self.operation_count += 1
        
        # Insert the merged rope back
        self.priority_queue.insert(merge_cost)
        
        return merge_cost
    
    def calculate_minimum_cost(self, rope_lengths):
        """Calculate the minimum cost to connect all ropes"""
        if not self.initialize_rope_data(rope_lengths):
            return 0
        
        # Continue merging until only one rope remains
        while self.priority_queue.heapsize > 1:
            self.perform_single_merge()
        
        return self.accumulated_expense
    
    def get_statistics(self):
        """Return operation statistics"""
        return {
            'total_cost': self.accumulated_expense,
            'operations': self.operation_count,
            'remaining_ropes': self.priority_queue.heapsize if self.priority_queue else 0
        }

def read_input_data():
    """Read and parse input data from stdin"""
    try:
        user_input = input().strip()
        if not user_input:
            return []
        
        # Parse space-separated integers
        rope_measurements = []
        for value in user_input.split():
            try:
                length = int(value)
                if length > 0:  # Only include positive lengths
                    rope_measurements.append(length)
            except ValueError:
                continue  # Skip invalid values
        
        return rope_measurements
    except EOFError:
        return []

def process_rope_cutting_problem():
    """Main function to process the rope cutting problem"""
    # Read input data
    rope_data = read_input_data()
    
    # Handle edge cases
    if len(rope_data) <= 1:
        return 0
    
    # Create rope cutter instance
    cutter = RopeCutter()
    
    # Calculate minimum cost
    minimum_expense = cutter.calculate_minimum_cost(rope_data)
    
    return minimum_expense

def validate_and_solve():
    """Validate input and solve the problem with error handling"""
    try:
        result = process_rope_cutting_problem()
        return result
    except Exception as error:
        return 0

def functional_rope_solver():
    """Functional approach to solve rope cutting problem"""
    def merge_ropes(rope_heap):
        """Recursively merge ropes until one remains"""
        if rope_heap.heapsize <= 1:
            return 0
        
        # Extract two minimum ropes
        min1 = rope_heap.extract()
        min2 = rope_heap.extract()
        
        # Calculate current merge cost
        current_cost = min1 + min2
        
        # Insert merged rope back
        rope_heap.insert(current_cost)
        
        # Recursively calculate remaining cost
        return current_cost + merge_ropes(rope_heap)
    
    # Read and process input
    input_line = input().strip()
    if not input_line:
        return 0
    
    rope_lengths = list(map(int, input_line.split()))
    
    if len(rope_lengths) <= 1:
        return 0
    
    # Create heap and solve
    rope_heap = heap(items=rope_lengths[:])
    return merge_ropes(rope_heap)


if __name__ == "__main__":
    SOLVING_METHOD = "object_oriented" 
    
    if SOLVING_METHOD == "functional":
        final_result = functional_rope_solver()
    else:
        final_result = validate_and_solve()
    
    print(final_result)

def compact_rope_solution():
    """Compact version of the rope cutting solution"""
    data = input().strip()
    if not data:
        print(0)
        return
    
    lengths = list(map(int, data.split()))
    if len(lengths) < 2:
        print(0)
        return
    
    rope_heap = heap(items=lengths[:])
    total_expense = 0
    
    while rope_heap.heapsize > 1:
        a, b = rope_heap.extract(), rope_heap.extract()
        cost = a + b
        total_expense += cost
        rope_heap.insert(cost)
    
    print(total_expense)
 