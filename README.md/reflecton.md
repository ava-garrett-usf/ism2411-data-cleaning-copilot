#1 What Copilot generated:
I started prompting Copilot using comments. I created a list of the steps to the data cleaning process. Then when writing the data cleaning code I referenced the number in the list and Copilot generated the comment for each block of code aswell as the code for functions #1-4. I inititlaly wrote the import block for csv file myself but when it ran with the required output pipeline it was incorrect so I used copilot reccomendations to fix it.

#2 What I modified from Copilot:
The code copilot generated worked for the majority of the functions. The initial response of Copilot to the function that removes invalid rows was incorrect because it tried to check strings and ints using >=. Copilot also did not standradize function names with the required output block I imported so I had to go back and match them. I initially wrote a function to print the head of the raw data frame but it interfered with the ouput pipeline because it was called before the output block.

#3 What I learned
I learned how to switch from my computers/vs code terminal to my python terminal in vs code. I had to do this to import pandas. I also learned how to create a virtual enviroment but I didn't keep it in the final project and used the global version of pandas instead. I learned how to generate the next responses from Copilot and how to add subfolders. I also learned how to call data from other files and create new files in my code.
