test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class MinHeap:
    def __init__(self):
        self.heap = []
    
    def _parent_index(self, index):
        if index <= 0 or index >= len(self.heap):
            return None
        return (index - 1) // 2
    
    def _left_child_index(self, index):
        left = 2 * index + 1
        return left if 0 <= index < len(self.heap) and left < len(self.heap) else None
    
    def _right_child_index(self, index):
        right = 2 * index + 2
        return right if 0 <= index < len(self.heap) and right < len(self.heap) else None
    
    def _has_left_child(self, index):
        return self._left_child_index(index) is not None
    
    def _has_right_child(self, index):
        return self._right_child_index(index) is not None

def test_1_2():
    heap = MinHeap()
    heap.heap = [1, 3, 2, 7, 4, 5, 8]  # Sample heap for testing
    
    # 1.2.1 Parent calculation
    record_test("1.2.1 Parent calculation",
                heap._parent_index(4) == 1)
    
    # 1.2.2 Children calculation
    left_correct  = heap._left_child_index(1)  == 3
    right_correct = heap._right_child_index(1) == 4
    record_test("1.2.2 Children calculation",
                left_correct and right_correct)
    
    # 1.2.3 Root node edge case
    p0 = heap._parent_index(0)
    record_test("1.2.3 Root node edge case",
                p0 is None)
    
    # 1.2.4 Boundary validation
    has_children = heap._has_left_child(1) and heap._has_right_child(1)
    record_test("1.2.4 Boundary validation", has_children)
    
    # 1.2.5 Invalid index handling
    no_children = not heap._has_left_child(6) and not heap._has_right_child(6)
    record_test("1.2.5 Invalid index handling", no_children)

if __name__ == "__main__":
    test_1_2()
    for r in test_results:
        print(r)
