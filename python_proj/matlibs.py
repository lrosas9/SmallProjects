with open("C:\\git\\SmallProjects\\python_proj\\story.txt", "r") as f:
    story = f.read()

words = set()
start_of_word = -1

target_start = "<"
target_end = ">"

for i, thing in enumerate(story):
    if thing == target_start:
        start_of_word = i

    if thing == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1
print(words)

answers = {}

for word in words:
    answer = input("Enter the word for " + word + ": ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])
print(story)