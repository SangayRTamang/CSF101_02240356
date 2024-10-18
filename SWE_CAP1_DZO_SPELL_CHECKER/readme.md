# code
To process Dzongkha words using this code, first I imported `re` library which is used to do pattern matching along with other string operations.
I created a function `only_dzongkha_word(word)` which will check if the input word is a Dzongkha word or not.
Then I defined the main function `filter_dzongkha_words(input_file,output_file)` that will read the input file, process each line, 
and output the lines that contain only Dzongkha words into the specified output file. 

I have to ensure that the input file name is 'dzo_dict.txt', and output file name is 'only_dzongkha.txt', 
and the input file dzo_dict.txt has Dzongkha words which the code will read and filter out to have only Dzongkha words saved as 'only_dzongkha.txt'.