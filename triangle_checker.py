import customtkinter

def CheckTriangle(a,b,c):
    side_a = int(a.get())
    side_b = int(b.get())
    side_c = int(c.get())

    assert(side_a > 0 and side_b > 0 and side_c > 0), "Number must be bigger than 0!"
    

    triangle = [side_a,side_b,side_c]
    h = max(triangle)
    triangle.remove(h)

    if h >= sum(triangle):
        result_label.configure(text= "{} >= ({} + {})\n------------\n No, we can't!\n------------".format(h, triangle[0], triangle[1]))
    else:
        result_label.configure(text= "{} <= ({} + {})\n------------\n Yes, we can!\n------------".format(h, triangle[0], triangle[1]))

customtkinter.set_appearance_mode("dark") #dark,light
customtkinter.set_default_color_theme("dark-blue") #blue,green,dark-blue

root = customtkinter.CTk()
root.title("Triangle Checker")
root.resizable(False,False)
root.geometry("400x550")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=30, fill="both")

label = customtkinter.CTkLabel(master=frame, text="Can we create a triangle?", font=('Bahnschrift', 20, 'bold'))
label.pack(pady=12,padx=10)

a = customtkinter.CTkEntry(master=frame,placeholder_text="a (cm)", font=('Bahnschrift', 15, 'bold'))
a.pack(padx = 5, pady= 20)

b = customtkinter.CTkEntry(master=frame, placeholder_text="b (cm)", font=('Bahnschrift', 15, 'bold'))
b.pack(padx = 5,pady = 20)

c = customtkinter.CTkEntry(master=frame, placeholder_text="c (cm)", font=('Bahnschrift', 15, 'bold'))
c.pack(padx = 5, pady = 20)

result = customtkinter.CTkButton(master=frame, text="Show Result!", command=lambda:CheckTriangle(a,b,c), font=('Bahnschrift', 15, 'bold'))
result.pack(padx = 5, pady = 20)

result_label = customtkinter.CTkLabel(master=root, text="", font=("Bahnschrift", 18, "bold"))
result_label.pack(padx = 5, pady = 20, fill = "both")

root.mainloop()
