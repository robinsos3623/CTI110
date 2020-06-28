#CTI-110
#P3LAB - Debugging
#Sinclair Robinson
#06-22-2020

# Named constants to represent the grade thresholds
A_SCORE = 90- 100
B_SCORE = 80-89
C_SCORE = 70-79
D_SCORE = 60-69
F_SCORE = 59 

# Get a test score from the user.
score = int(input('Enter your test score: '))

# Determine the grade.
if score >= 90:
      print('Your grade is A.')
elif score >= 80:
      print('Your grade is B.')
elif score >= 70:
      print('Your grade is C.')
elif score >= 60:
      print('Your grade is D.')
if score < 59:
      print('Your grade is F.')








    

    
