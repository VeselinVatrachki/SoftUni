from string import punctuation


with open("text.txt", "r") as file, open("output.txt", "w") as output:
    result = []
    for row, line in enumerate(file):
        count_letters = 0
        count_punc_marks = 0
        for char in line:
            if char.isalpha():
                count_letters += 1
            elif char in punctuation:
                count_punc_marks += 1
        result.append(f"Line {row + 1}: {line.strip()} ({count_letters})({count_punc_marks})")

    output.write("\n".join(result))