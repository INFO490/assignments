## Week 1 Assignment

### Recording your session

We will use the `script` command tool to record our session. `script` records everything that happens on your terminal session. To use `script`, simply type

        $ script

If no argument is given, it writes to a file named _typescript_. You can later rename this file to _filename.txt_, where _filename_ should be your firstname-lastname. Or you can write to a different file from the beginning by 

        $ script firstname-lastname.txt

When you are done, type

        $ exit

This will end the session and save the file. You should upload the this file to Moodle.

### Part 1. Navigating through your file system.

0. As described above, use `script` to start recording your session. 

1. Use `pwd` to output the path of the current working directory:

2. Use `ls` with `-F` option to list all files in the current directory. Here, the `-F` option classifies the files with different special character for different kinds of files. Note that there other many options that you can use with the `ls` command (and other Unix commands in general). Use `man ls` to see the options available.

3. Use `mkdir` to create a new directory. We will download and store the census data in this directory, so choose an appropriate name (_e.g._ "census" ).

4. Use `cd` to change the working directory to your new directory.

5. Use `ls` with `-a` option to list all the files in the new directory. The -a option shows all the hidden files in the directory. Note that with `-a` option you see '.' (current directory) and '..' (parent directory) even if there is no file in this directory.

6. Use `wget` to download the census data from <http://www2.census.gov/acs2012_1yr/pums/csv_pil.zip>.

 Note: This file is the 2012 1-year American Community Survey (ACS) Public Use Microdata Sample (PUMS) file for Illinois from the U.S. Census Bureau. It represents about one percent of the Illinois population, and includes detailed response information of each individual, such as relationship, age, sex, educational attainment, income, and employment status.

7. Use `ls` with `-l` option to list all the files in the directory. The `-l` option displays detailed information about files, including sizes.

### Part 2. Working with data file.

1. Since the downloaded file is compressed, we have to extract it. Use `unzip` to extract the census data file you downloaded in the previous problem.

2. Use `ls` to display all the files in the directory, but this time with a combination of all three options, `-l`, `-a`, and `-F`.

 Hint: To show all files including the hidden files _and_ classify them using special characters, one would use a combination of two options `-a` and `-F`, or simply `-aF`.

3. Use `wc` to count the number of lines in the CSV (Comma Separated Values) file. The `-l` option prints the number of lines in a file. The output should be
         
         127209 ss12pil.csv

 That means this data file has 127,209 rows.

4. Obviously, it would be not practical to print all 127,209 lines at once, so we will take a peek at how the first few lines of this file look like. Use `head` to print the first 10 lines of the CSV file.

5. We also want to look at the end of the file, but a line of this file looks quite long. Use `tail` with `-n 5` option (or simply `-5`) to print only the last 5 lines of the file.

### Part 3. Using `awk` and `sed` to manipulate files.

1. You might have noticed there were very many columns when we used `head` and `tail` (286 columns if you count them; that's 127,209 rows times 286 columns). Let's grab only a few useful columns. The seventh column is "PWGTP," the integer weight of each person; the eighth column is "AGEP," the age; the fortieth column is "MARHT," the number of times married; and the seventy-third column is "WKHP," the usual hours worked per week for the past 12 months. Use `awk` to extract column 7, 8, 40, and 73, and output the result to another file.

 Hint 1: We have to tell `awk` that the columns are separated by commas (rather than whitespaces) by using the `-F ","` or simply `-F,` option. 

 Hint 2: After the options comes the _program_ part surrounded by single quotes. In this program part is the _pattern_ followed by the _action_ surrounded by curly brackets. That is, `awk` usage pattern is

         $ awk [options] 'pattern{action}' file

 Note that the _pattern_ part is not necessary to do this problem. Omitting the pattern part is also a valid `awk` usage pattern:

         $ awk [options] '{action}' file

 Hint 3:  I like to prepend the input file with `<` as this seems intuitive. Although one may omit the optional `<` in front of the input file, one _must_ prepend the output file with `>` (because the input file is one of the arguments to `awk` while the output file is separate from the `awk` command). In summary, to read columns 1, 2, and 3 of _file1.csv_ and save the output to a file named _file2.csv_, one would type

         $ awk -F, '{print $1 "," $2 "," $3}' <file1.csv >file2.csv

2. Use `head` to check if your output looks correct.

 The output should be

         PWGTP,AGEP,MARHT,WKHP
         00200,50,1,
         00070,45,1,40
         00212,26,,40
         00015,87,1,
         00071,41,1,25
         00080,13,,
         00095,05,,
         00131,32,1,40
         00147,33,1,37
                  
3. Use `sed` to change the commas in the CSV file to vertical bars.

 Hint: We use the substitute command `s/../../` to convert some pattern to another pattern. To change commas to vertical bars, we would type

         $ sed 's/,/|/' <week1.csv >week1.bsv

 Let's look at what the result looks like.

         $ head week1.bsv
         PWGTP|AGEP,MARHT,WKHP
         00200|50,1,
         00070|45,1,40
         00212|26,,40
         00015|87,1,
         00071|41,1,25
         00080|13,,
         00095|05,,
         00131|32,1,40
         00147|33,1,37     
                    
 Note that only the first occurrences of the commas are changed on every line. This behavior is typical of `sed`; it look at one line at a time and changes only the first occurrence of the search word.

 Here, we want to make changes on every occurrence instead of only the first. The `g` (global) flag at the end tells `sed` to make changes for every occurrence. That is, we have to use the command `s/../../g`.

4. Finally, use `head` to check if the final output of `sed` looks correct.

 The output should be

         PWGTP|AGEP|MARHT|WKHP
         00200|50|1|
         00070|45|1|40
         00212|26||40
         00015|87|1|
         00071|41|1|25
         00080|13||
         00095|05||
         00131|32|1|40
         00147|33|1|37


5. That's it! Don't forget to end the `script` session and upload _firstname-lastname.txt_ to Moodle.
