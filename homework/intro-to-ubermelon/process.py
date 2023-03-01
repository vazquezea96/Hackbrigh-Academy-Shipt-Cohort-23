log_file = open("um-server-01.txt") # declaring variable log_file to open the "um-server-01" txt file


def generate_sales_reports(log_file): # function with log_file as the parameter
    for line in log_file: # reading each line in the log_file
        line = line.rstrip() # removing trailing characters at end of each line
        day = line[0:3] # splicing the string from index 0 to index 3 to grab a specific char
        if day == "Mon": # result of splicing - looking for day - changed "Tues" to "Mon"
            print(line) # print lines that match the splicing


generate_sales_reports(log_file) # function call with the corresponding argument
