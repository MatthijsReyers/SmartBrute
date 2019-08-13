# SmartBrute changelog

### 12/08/2019 - GetAllComb() optimalization and new features
The GetAllComb() function now no longer generates a list with all possible combinations but instead returns an object that will generate the required string when asked for or itterated over (similarly to how python's build-in range function works). This means that python no longer needs to store giant amounts of data in RAM when working with multiple nested GetAllComb() functions or when the GetAllComb() function is given a large list.
I have also added the ```minKeys``` & ```maxKeys``` arguments which allow the user to choose how many keys to combine, which was previously not possible.

### 12/06/2019 - Dutch password list examples
I wanted to 

### 25/07/2019 - Adding the RemoveDoubles() function
After working on the documentation some more I realized that the GetFirstN() function can output lists with duplicates when N is of a sufficiently small size, in order to account for this and any future functions that have this problem I have choosen to create the RemoveDoubles() function.
I have also deprecated the GetAllCombForEach() function after realizing that it does exactly the same thing as the AddForEach() function.

### 24/07/2019 - New options in the settings dict
It is now possible to filter the generated passwords for certain characters, and you can also disable the previewing of generated passwords in the console, because it significatnly slows down the program.



# Upcomming/requested/suggested features

- Filtering generated passwords with regex/regular expressions.
- The ability to load in a password list from a file for manipulation in with SmartBrute.