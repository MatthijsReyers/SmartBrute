# SmartBrute changelog

### 25/07/2019 - Adding: RemoveDoubles()
After working on the documentation some more I realized that the GetFirstN() function can output lists with duplicates when N is of a sufficiently small size, in order to account for this and any future functions that have this problem I have choosen to create the RemoveDoubles() function.
I have also deprecated the GetAllCombForEach() function after realizing that it does exactly the same thing as the AddForEach() function.