string = str(input("File name: ")).strip().lower()

if string.endswith(".gif"):
    print("image/gif")
elif string.endswith(".jpg") or string.endswith(".jpeg"):
    print("image/jpeg")
elif string.endswith(".png"):
    print("image/png")
elif string.endswith(".pdf"):
    print("application/pdf")
elif string.endswith(".txt"):
     print("text/plain")
elif string.endswith(".zip"):
     print("application/zip")
else: print("application/octet-stream")
