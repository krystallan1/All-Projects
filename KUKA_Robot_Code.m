% Code written by Krystal Lan
% September 3, 2022

% Code to translate ".dat" file to a table with 6 columns with column
% headers X, Y, Z, A, B, C

% MUST SPECIFY 2 VARIABLES: NUMBER OF DATA POINTS AND FILE NAME (see below)

% **Specify number of data points to be read**
num_data_points = 17;

% **Specify file to be read**
fid = fopen("new_handeye.dat");


% ----------------**The code below need not be changed**-----------------------


% detect if the current line specifies a data point
s = 'DECL E6POS';

% get the first line of the file
line = fgetl(fid);

% create a cell array to store all of the data points
C = cell(num_data_points, 6);
C{num_data_points, 6} = [];

% keep track of the number of data points parsed
count = 1;

while count <= num_data_points
    if length(line)>11 % if the current line is not longer than "DECL E6POS", do not compare anything
        sub = extractBefore(line, 11); 
        if strcmp(sub, s) % check if the current line also starts with "DECL E6POS"
            % extract all the data values we want into one cell
            line = extractAfter(line, '{');
            line = extractBefore(line, 'S');
            C{count, 1} = line;
            count = count + 1;
        end 
    end
    line = fgetl(fid);
end

% extract the individual data values into their corresponding cells
for i=1:num_data_points
    str = C{i, 1};
    tokens = split(str);

    for j=2:7
        tok = extractBefore(tokens(j), ",");
        num = str2double(tok);
        C{i, j-1} = num;
    end
end

% all_values is the final table of double values with the corresponding column names
all_values = cell2table(C, 'VariableNames', {'X' 'Y' 'Z' 'A' 'B' 'C'});

fclose(fid);

