addpath(genpath('.'));

sdirectory = './data/StanfordSimpleDogWalking';
jpgffiles = dir([sdirectory '/*.jpg']);

filepw = fopen('Stanford_data_Seg_1_leash.txt','w');

for k = 1:length(jpgffiles)
filename = [sdirectory '/' jpgffiles(k).name];

image = imread(filename);
[nrows, ncols] = size(image);
heightRatio = double(315./nrows);
widthRatio = double(315./ncols);

%image = imresize(image, [315,315]);

%para = makeDefaultParameters;

%t = tic;
%smap = drfiGetSaliencyMap( image, para );
%time_cost = toc(t);
%fprintf( 'time cost for saliency computation using DRFI approach: %.3f\n', time_cost );

image_resize_name =  regexprep(jpgffiles(k).name,'.jpg','-saliencyMap.jpg');
cd 'data/stanford_salient_images/'
%imwrite(smap,image_resize_name);
cd '../../'

sdirectoryLabl = '.';
sdirectorySalient = './data/stanford_salient_images/';

object_name = 'leash'; %change the object name 

[path, name, ext] = fileparts(filename);

lablfilename = [sdirectory '/' name '.labl' ];

file_ID = fopen(lablfilename); 
string_line = fgetl(file_ID);
fclose(file_ID);

num_part = textscan(string_line, '%f', 'Delimiter', '|');
number_length = length(num_part{1});

input_file = textscan(string_line, '%s', 'Delimiter', '|');
labl_file = input_file{1};

% convert cell array to ordinary number array
number_array = zeros(1, number_length - 3);
for number_index = 4 : number_length
    number_array(number_index - 3) = str2double(labl_file{number_index});
end

% convert cell array to ordinary string array
string_array = cell(1, (length(labl_file) - number_length));
count_index = 1;
for string_index = (number_length + 1) : length(labl_file)
    string_array{count_index} = labl_file{string_index};
    count_index = count_index + 1;
end

% record object's position
data_index = 1;
for search_index = 1 : length(string_array)
    
    % get a line from string array
    temp_cell = textscan(string_array{search_index}, '%s', 'Delimiter', ' ');
    
    % convert cell string to string
    temp_cell_string = temp_cell{1}(1);
    temp_string = temp_cell_string{1};
    
    % if the object is leash
    if (strcmp(object_name,'leash'))
        temp_string = temp_string(1:length(temp_string) - 2);
    end
    % compare object name with the label name in label file
    if (strcmp(temp_string, object_name))
        % record dog-walker index
        dog_walker_index = search_index;
        
        % get start index and end index for a specific sentence
        start_index = (4 * (dog_walker_index - 1) ) + 1;
        end_index = 4 * (dog_walker_index);
        
        % record the position information
        object_position(data_index,:) = number_array(start_index:end_index);
        
        data_index = data_index + 1;
    end
    
end
cd 'data/stanford_salient_images/'
grayImage = imread(image_resize_name);

objectsigma = 0;
imagesigma = sum(grayImage(:));

x = floor(object_position(1) * widthRatio);
w = floor(object_position(3) * widthRatio);
y = floor(object_position(2) * heightRatio);
h = floor(object_position(4) * heightRatio);

width = x+w;
height = y+h;


if x < 1
    x = 1;
end

if y < 1 
    y = 1;
end 
    

for p=x:width
    for q=y:height
        objectsigma = objectsigma + double(grayImage(p,q));
    end 
end

probabilityWeight = objectsigma./imagesigma;
fprintf(filepw,'%f\n',probabilityWeight);
cd ../..
end

fclose(filepw);



