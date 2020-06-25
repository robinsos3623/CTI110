#CTI-110
#P3HW1 - Color Mixer
#Sinclair Robinson
#06-22-2020



color1 = input("Choose your first color. (red,blue,yellow):")
color2 = input("Choose your second color. (red,blue,yellow):")
red= "red"
yellow="yellow"
blue="blue"

if (color1 == "red" and color2 == "blue") or (color1 == "blue" and color2 =="red"):
               print("Your result is purple")

               if (color1 == "red" and color2 == "yellow") or (color1 == "yellow" and color2 == "red"):
                   print("Your result is orange")
                   
               if (color1 == "blue" and color2 == "yellow") or (color1 == "yellow" and color2 == "blue"):
                   print("Your result is green")
               else:
                   print("Error occured")
