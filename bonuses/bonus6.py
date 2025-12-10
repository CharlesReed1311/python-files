contents = ["All carrots are to be sliced longitudinally.",
            "The carrots were reportedly stored.",
            "The slicing process was well presented."]

filenames = ["doc.txt", "report.txt", "present.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"bonuses/files/{filename}", 'w')
    file.write(content)

