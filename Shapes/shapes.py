import ShapesModule

print("""
1.Circle
2.Rectangle
3.Triangle""")

choice=int(input("Choose an option: "))

if choice==1:
    r=float(input("Enter Radius: "))
    area=ShapesModule.circle(r)
    print(f"Area of circle having radius {r} is: {area}")

elif choice==2:
    l=float(input("Enter Length: "))
    w=float(input("Enter Width: "))
    area=ShapesModule.rectangle(l,w)
    print(f"Area of Rectangle having length {l} and witdth {w} is: {area}")


elif choice==3:
    base=float(input("Enter Base: "))
    height=float(input("Enter Height: "))
    area=ShapesModule.triangle(base,height)
    print(f"Area of Triangle having base {base} and height {height} is: {area}")

else:
    print("Invalid option")