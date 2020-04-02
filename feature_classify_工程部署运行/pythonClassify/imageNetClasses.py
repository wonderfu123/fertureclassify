class_names = '''anger
disgust
fear
happy
sad
surprised
normal'''.split("\n")

imageNet_classes = {}
i = 0
for items in class_names:
    imageNet_classes[i] = items
    i += 1
