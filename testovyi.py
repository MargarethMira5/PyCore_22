# # .writelines
# with  open("demofile3.txt", "w") as f:
#     f.writelines(['5', '\n5'])
# f.close()

# #open and read the file after the appending:
# f = open("demofile3.txt", "r")
# print(f.read())

# f = open("myfile.txt", "a")
# f.write("Now the file has one more line!")
# f.flush()
# f.write("...and another one!")


# .write
# file.write("See you soon!")

# # truncate()
f = open("demofile2.txt", "a")
f.write("I`m back..In love with Five Hargreeves!")
f.truncate(15)
f.close()

# #open and read the file after the truncate:
# f = open("demofile2.txt", "r")
# print(f.read())

# fileno()
# try:
#     with open('foo.txt', 'r+') as fp:
#         file_id = fp.fileno()
#         print(file_id)
# except FileNotFoundError:
#     print("File not found.")

