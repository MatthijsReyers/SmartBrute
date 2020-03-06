# SmartBrute changelog

### 06/03/2020 - Lazy evaluation and type hinting.
Today work has started on refactoring the SmartBrute codebase to make all password/key generators lazily evaluated. Additionally I am also working on adding type hinting to all functions and variables.

### 12/08/2019 - GetAllComb() optimalization and new features
The GetAllComb() function now no longer generates a list with all possible combinations but instead returns an object that will generate the required string when asked for or itterated over (similarly to how python's build-in range() function works). This means that python no longer needs to store giant amounts of data in RAM when working with multiple nested GetAllComb() functions or when the GetAllComb() function is given a large list.
I have also added the `minKeys` & `maxKeys` arguments which allow the user to choose how many keys to combine, which was previously not possible.
The previous GetAllComb() function has now been renamed to GetAllCombNoDoubles() and the GetAllTrueComb() function has been depricated because the same thing can now be doen with the new GetAllComb() function.

### 12/06/2019 - Dutch password list example
The example folder now contains a script for generating passwords based on the names of popular dutch footbal/soccer clubs.

### 25/07/2019 - Adding the RemoveDoubles() function
After working on the documentation some more I realized that the GetFirstN() function can output lists with duplicates when N is of a sufficiently small size, in order to account for this and any future functions that have this problem I have choosen to create the RemoveDoubles() function.
I have also deprecated the GetAllCombForEach() function after realizing that it does exactly the same thing as the AddForEach() function.

### 24/07/2019 - New options in the settings dict
It is now possible to filter the generated passwords for certain characters, and you can also disable the previewing of generated passwords in the console, because it significatnly slows down the program.



# Upcomming/requested/suggested features
- Proper docstrings for all functions.
- Proper type hinting for all functions and variables.
- All Key generators will be made lazy.
- GetAllCombNoDoubles() will be replaced with the more general filterDoubles().
- Filtering generated passwords with regex/regular expressions.
- The ability to load in a password list from a file for manipulation in with SmartBrute.
