#insert p tags between paragraph breaks

#get paragraphs that will be wrapped in p tags from user
initial_string = input("Input paragraphs:")

#split grafs at each return
grafs = initial_string.split("\n")

#get rid of any extra newlines
[grafs.remove(graf) for graf in grafs if not graf]

#initiate p tag string that will contain wrapped grafs
p_tag_grafs = "<p>"

#insert p tags between each paragraph
for index, graf in enumerate(grafs):
    p_tag_grafs += "\n\t" + graf + "\n</p>"
    if index != len(grafs) - 1:
        p_tag_grafs += "\n<p>"
        
print(p_tag_grafs)

#input desired csv file name for final output
file_name = "your-file-name.txt"

#write p tag grafs to a file ready for copying
with open(file_name, 'w') as file:
    file.write(p_tag_grafs)
