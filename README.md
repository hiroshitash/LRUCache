The goal is to implement a User cache. This module holds active users to 
improve system performance.  The other modules use the following interface 
method to retrieve user objects:
 
public User getUser(String userId)
 
The cache returns an instance of the User object for a given user id. 
 
The cache can hold at most a pre-configured number (cache size) of user objects. The cache size is 
configurable and set at the time of application startup. 
 
The cache is backed by a data store (ignore the specifics of data store for this exercise).
- If the user id is found in the cache, the user object is returned. 
- If not found, the user object is fetched from the user data store. The fetched user 
  object is added to the cache, and the user object is returned. 
- If the cache is full, then a user is evicted from the cache before adding another 
  user object. That is, when the number of cached users reaches the size of cache, then the 
  user that has not been requested for the longest time is evicted.
 
For example, if the cache size is 3, and user ids are requested in the 
following order:
1
2
3
2
1
4
When the user id 4 is requested, user with id 3 is evicted from the cache, 
as it was the not requested for the longest time.
 
The performance of the getUser method is critical, and should be as close 
to O(1) as possible.

