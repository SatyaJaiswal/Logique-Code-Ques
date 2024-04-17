# Q. Write a Python function that takes a text file as input and returns a dictionary containing the frequency of each word in the file.

def word_frequency(file_path):
        text = {}
        with open(file_path, 'r') as file:
            for line in file:
            # Split the line into words
                words = line.split()
            # Iterate through each word in the line
            for word in words:
                # Remove any punctuation and convert the word to lowercase
                word = word.strip('.,?!;:').lower()
                # Increment the frequency count of the word in the dictionary
                text[word] = text.get(word, 0) + 1

        return text

# Example usage:
file_path = 'text-file.txt'  
text_dict = word_frequency(file_path)
print(text_dict)

