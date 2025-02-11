1. I would use a linear search algorithm that would increment through the all of the room rumbers until there was a match with EY128. SO we would begin incrementally searching using linear search for room "EY128" from the left of the sign.

2. In this case, a step would be a comparison of the room number to the desired room number value "EY128". Since we have no knowledge of the floor plan, we would begin our search from the left of the signn where "EY100-EY130". This means we would have to make 15 comparisons until we reached "EY128"; It takes 15 steps to find room "EY128".

3. Yes there is a best and worst case scenario, this is dependent on the room number that we are searching for. A room number that would be the first in the set being searched would yield the best case scenario, whereas a room that is last in the set, or outside of the given set would yield a worst case scenario

4. A worst case scenario would be if we were looking for room "EY130" which is the last room number in the sign of "EY100-EY130", or rooms that aren't the floor that we are currently on, because we could search the entire array/set and still not find anything

   A best case scenario would be if we were looking for room "EY100" as it would be the very first room we encounter, meaning the algorithm only made one comparison, meaning there was only one step. The case complexity here would be O(1).

5. Now that we have memorized the layout of the floor, we would now know to begin our linear search from the right of the sign, the end of the array/set as we know that the room "EY128" is closer to that end of the array/set of rooms on this floor.
