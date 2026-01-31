#Nested Dictionary from Strings
# Define the function as required
def analyze_strings(string_list):
    #1. Create an empty dictionary (to store the result)
    result = {}
    #2. Loop through each word in the input list
    for word in string_list:
        #Step A: Get the length of the word (use the len() function)
        word_length = len(word)
        #Step B: Check if the length is even or odd
        if word_length % 2 == 0:
            parity_value = "even"
        else:
            parity_value = "odd"
        #Step C: Create an inner dictionary to store word info
        inner_dict = {"length": word_length, "parity": parity_value}
        #Step D: Add the word and its info to the main dictionary (Key = word, Value = inner_dict)
        result[word] = inner_dict
    #3. Return the final dictionary after the loop ends
    return result
#TEST_CODE
#Create a sample list
dessert_list = ["cassata", "panettone", "cannoli", "tiramisu"]

#Call the function and print the result
output = analyze_strings(dessert_list)
print(output)