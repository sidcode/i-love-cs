#Lexical Analyzer for 'Introductory Language for Computer Science (ILCS)'
#Written by - Siddhant and Apoorva

import re
import sys

#Validate input
if (len(sys.argv) != 2) :
        print('Usage: python lexer.py <dslFile.txt>')
        exit()

inp = sys.argv[1]

#open code file in the domain-specific language
dsl_file = open(inp,'r')
data = dsl_file.read()

#create a file for line-by-line analysis for input to future compilation stages
lexout = open('Lexer_output.txt','w')

print("\n\t\t\tLexical analysis for ILCS begins\n")
print("-------------------------------------------------------------------\n\n")

#express the Regular Expression for the ILCS Visualization language
#The RegEx groups similar patterns together
#Group 1,2: Comments
#Group 3: String Literals
#Group 4: Keywords
#Group 5: Operators
#Group 6: Numeric Literals
#Group 7: Separators
#Group 8: Identifiers
#Group 9: Whitespaces
#Group 10: Lexical Errors

pattern = re.compile(r"(#@[\s\S]*?@#)|(#.*)|('.*')|(insert\b|\+|add\b|delete\b|-|remove\b|find\b|search\b|sort\b|check\b|visualize\b|merge\b|convert\b|has\b|is\b|of\b|to\b|if\b|and\b|not\b|in\b|all\b)|(data\b|list\b|matrix\b|tree\b|bTree\b|heap\b|trie\b|table\b|graph\b|avl\b|binary\b|binSearch\b|adjacency\b|directed\b|if\b|multi\b|check\b|show\b|insert\b|to\b|right\b|left\b|delete\b|sort\b|traverse\b|type\b|start\b|done\b|dfs\b|bfs\b|heapify\b|find\b|min\b|max\b|size\b|merge\b|convert\b|is\b|of\b|descendent\b|search\b|has\b|goto\b|loop\b|till\b|empty\b|to\b|take\b|sibling\b|parent\b|child\b|degree\b|path\b|level\b|height\b|root\b|element\b|neighbour\b|connect\b|next\b|back\b|also\b|and\b|not\b|in\b|all\b)|(\d+)|({|}|-|,)|([a-zA-Z_]\w*)|(\s|\n)|([^\\1\\2\\3\\4\\5\\6\\7\\8\\9])")

#evaluate the regex over the ILCS code and get grouped patterns
scan = pattern.scanner(data)

#line stores line variable for ILCS
line = 1

#define lists for the different tokens
keywords = []
identifiers = []
operators = []
literals = []
separators = []
comments =[]
errors = []

flag = 0

print("\t\t\tLexical Analysis Complete\n\n\tLine-by-line analysis stored in Lexical_Output.txt file")
print("\n")

print("-------------------------------",file=lexout)
print("Line number ",line,file=lexout)
print("-------------------------------",file=lexout)

#Begin processing groups and outputting to file Lexical_output.txt

while 1:
    m = scan.match()
    
    #Reached Last token
    if m is None:
        print("End of lexing",file=lexout)
        break
    
    else:
        
        #Handles Line Numbers
        if '\n' in m.group(m.lastindex):
            ct = (m.group(m.lastindex)).count('\n')
            line = line+ct

            if(ct is 1):
                print("\n----------------\nLine number ",line,"\n-----------------",file=lexout)

        #Group-wise processing
        if m.lastindex is 1:
            print("\nMulti-Line Comment\t\t",m.group(1),"\n",file=lexout)
            comments.append((line,m.group(1)))


        elif m.lastindex is 2:
            print("Single-Line Comment\t\t",m.group(2),"\n",file=lexout)
            comments.append((line,m.group(2)))

        elif m.lastindex is 3:
            print("String Literal\t\t",m.group(3),file=lexout)
            literals.append((line,m.group(3)))

        elif m.lastindex is 4:
            print("Operator\t\t",m.group(4),file=lexout)
            operators.append((line,m.group(4)))
        
        elif m.lastindex is 5:
            print("Keyword\t\t",m.group(5),file=lexout)
            keywords.append((line,m.group(5)))

        elif m.lastindex is 6:
            print("Numeric Literal\t\t",m.group(6),file=lexout)
            literals.append((line,m.group(6)))
    
        elif m.lastindex is 7:
            print("Separator\t\t",m.group(7),file=lexout)
            separators.append((line,m.group(7)))

        elif m.lastindex is 8:
            print("Identifier\t\t",m.group(8),file=lexout)
            identifiers.append((line,m.group(8)))

        elif m.lastindex is 9:
            continue
        
        #handles lexical errors
        else:
            print("Lexical error\n",file=lexout)
            print("Lexical error at line ",line)
            print(m.group(m.lastindex))
            
            errors.append((line,m.group(m.lastindex)))
            
#close the file Lexical_output.txt
lexout.close()


#Print Category-wise list of tokens
print("\n\t\tCategory wise list of tokens\n\t\t---------------------------\n")
print("\t\tLine No. \t\t 'token name'\n")

print("\nKeywords\n")
print("-------------\n")
for (i,j) in keywords:
    print("Line ",i,"\t\t ",j)


print("\n-------------")
print("Operators")
print("-------------\n")
for (i,j) in operators:
    print("Line ",i,"\t\t ",j)

print("\n-------------")
print("Identifiers")
print("-------------\n")
for (i,j) in identifiers:
    print("Line ",i,"\t\t ",j)

print("\n-------------")
print("Literals")
print("-------------\n")
for (i,j) in literals:
    print("Line ",i,"\t\t ",j)

print("\n-------------")
print("Separators")
print("-------------\n")
for (i,j) in separators:
    print("Line ",i,"\t\t ",j)

print("\n-------------")
print("Comments")
print("-------------\n")
for (i,j) in comments:
    print("Line ",i,"\t\t ",j)

print("\n-------------")
print("Lexical Errors")
print("-------------\n")
for (i,j) in errors:
    print("Error in Line ",i,"\t\t ",j)
print("\nEnd of Lexing\nHave a look at Lexical_output.txt for line-by-line token analysis!\n")

#End of prgram for ILCS Lexical Analyzer
