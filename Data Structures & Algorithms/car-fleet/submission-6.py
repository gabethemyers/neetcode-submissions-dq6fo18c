class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_points = sorted(zip(position, speed), reverse=True)
        car_times = []
        

        for (pos, spd) in car_points:
            time = (target - pos) / spd
            if not car_times or time > car_times[-1]:
                car_times.append(time)
        return len(car_times)

            



