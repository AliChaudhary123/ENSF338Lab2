1.)
One of the reasons why interpolation search is better than binary search is because of uniformly distributed data. This already assumes that the data in the array is already sorted. In binary search, the array would be split directly in the middle. Interpolation search is more precise in finding the mid point, as a point where the item is most likely to occur.
Another reason is time complexity. The worst case for interpolation search is O(N), and the worst case for binary search is O(log N). Interpolation is much faster

2.)
Yes, the performance will change. As interpolation search follows a uniform distribution, this is what it needs to accurately find the mid-point. If non-uniform distribution was used, then the mid-point's cacluations would be off. 

3.)
The position calculation of the code would need to be changed. The way it is in the code assumes a linear relationship, as it is equally distributed.

4.)
Linear search is preferred to be used when the data is unsorted. Both Binary and Interpolation search requires the data to be sorted, which leaves us with linear search. At this point, linear search requires comparing each value with a key value until a match is found.

5.)
Linear search supports smaller data sets the best. As the complexity is O(n), the linear search is straightforward. With interpolation, estimating the middle point may be less efficient than linear search.

6.)
For binary search, the solution to this problem is that there needs to be a small data set. When the data set gets to a certain small size, linear search can be implemented to find the value quicker. For interpolation searches, calculating inaccurate mid-point values can occur. In that case, linear search can be implemented to ensure that in the case of enequal data distribution, the search can be as efficient as possible. This is to prevent the performance to downgrade from bad calculations. 