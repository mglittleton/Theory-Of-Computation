import re # module for processing regular expressions https://docs.python.org/3/library/re.html
import sys
import codecs
import csv
if __name__ == '__main__':
  # Exit if command line args entered incorrectly
  if len(sys.argv) != 2:
    print("usage: extract_links.py [input_file]")
    sys.exit(0)

# Filename is 2nd command line arg
filename = sys.argv[1]

# TODO Read HTML file
text = open('stackoverflow.html', errors='ignore').read()

# TODO Set up regex
match_list = re.findall(r'https?://[^."\']+\.[^"?\']+', text)

# TODO Find links using regex, save in list called 'matches'
list_file = open('matches.txt', 'w')
for i in match_list:
  list_file.write(i + '\n')

list_file.close()


# Check matches, print results
# TODO Read in links from answers.txt (hint...this is a CSV file),
# save in list called 'answer_data'


# Compare answers with matches found using regex, print out any mismatches
# UNCOMMENT BELOW WHEN READY TO CHECK IF YOUR REGEX IS FINDING ALL THE LINKS
# result = "All links matched!"
# if len( matches ) != len( answer_data ):
#   result = "Your regex found %i matches. There should be %i matches" %(len( matches ), len( answer_data ) )
# else:
#   for i in range( len(answer_data) ):
#     if( matches[i] != answer_data[i] ):
#       result = "Mismatched link. Got %s but expected %s" % ( matches[i], answer_data[i] )
#       break
# print( result )