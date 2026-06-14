class TimeMap:

    def __init__(self):
        self.hashMap = {}

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # it can store multiple values for the same key at different time stamps.
        # does that mean my "key" should be a tuple of key and timstamp?

        # {key : [(timestamp, value), ...]}

        if key in self.hashMap:
            self.hashMap[key].append((timestamp, value))
        else:
            self.hashMap[key] = [(timestamp, value)]


        

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.hashMap:
            return ""
        
        # i want to find the timestamp that is exactly match or closest less than value

        values = self.hashMap[key]

        left = 0
        right = len(values) - 1

        best_match = ""

        while left <= right:
            mid = (left + right) // 2

            if values[mid][0] <= timestamp:
                
                best_match = values[mid][1]

                left = mid + 1
            else:
                right = mid - 1
        
        return best_match



        

        
        
