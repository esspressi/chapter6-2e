import circle 
import rectangle 

AREA_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_RECTANGLE_CHOICE = 3
PERIMETER_RECTANGLE_CHOICE = 4
QUIT_CHOICE = 5

def main():
  choice = 0

  while choice != QUIT_CHOICE:
    display_menu()
    choice = int(input('Enter your choice: '))

    if choice == AREA_CIRCLE_CHOICE:
      radius = float(input("enter the circle's radius: "))
      print('The area is', circle.area(radius))
    elif choice == CIRCUMFERENCE_CHOICE:
      radius = float(input("enter the circle's radius: "))
      print('the circumference is', \
            circle.circumference(radius))
    elif choice == AREA_RECTANGLE_CHOICE:
      width = float(input("enter the rectangle's width: "))
      length = float(input("enter the rectangle's legnth: "))
      print('The area is', rectangle.area(width, length))
    elif choice == PERIMETER_RECTANGLE_CHOICE:
      width = float(input("enter the rectangle's width: ")) 
      length = float(input("enter the rectangle's legnth: "))
      print('the perimeter is', \
            rectangle.perimeter(width, length))
    elif choice == QUIT_CHOICE:
      print('exiting the program...')
    else:
      print('error: invalid selection')

def display_menu():
  print('        MENU')
  print('1) Area of a circle')
  print('2) Circumference of a circle')
  print('3) Area of a rectangle')
  print('4) Perimeter of a rectangle')
  print('5) Quit'

main()      

      
    
