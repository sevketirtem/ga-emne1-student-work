def calculate_area(width, height):
    area = width * height
    return area

total_area = 0
for width in range (2,5):
    area = calculate_area(width,2)
    print(f"Area is: {area}")
    total_area += area

print(f"Total area is: {total_area}")







#total_area1= calculate_area(2,5)
#total_area2= calculate_area(3,4)


#print(f"Area is: {total_area1}")
#print(f"Area is: {total_area2}")


