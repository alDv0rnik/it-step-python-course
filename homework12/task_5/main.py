from figures import circle_area, circle_perimeter
from figures import triangle_area, triangle_perimeter
from figures import square_area, square_perimeter

i = int(input("Change figure: triangle-1, square-2, circle-3: "))
j = int(input("Change action: perimeter-1, area-2: "))
if __name__ == "__main__":
    if i == 1:
        if j == 1:
            print(triangle_perimeter(int(input("Enter side a: ")), int(input("Enter side b: ")),
                                     int(input("Enter side c: "))))
        elif j == 2:
            print(triangle_area(int(input("Enter side a: ")), int(input("Enter side b: ")),
                                int(input("Enter side c: "))))
        else:
            print("Try again")
    elif i == 2:
        if j == 1:
            print(square_perimeter(int(input("Enter side length: "))))
        elif j == 2:
            print(square_area(int(input("Enter side length: "))))
        else:
            print("Try again")
    elif i == 3:
        if j == 1:
            print(circle_perimeter(int(input("Enter radius: "))))
        elif j == 2:
            print(circle_area(int(input("Enter radius: "))))
        else:
            print("Try again")
    else:
        print("Try again")
