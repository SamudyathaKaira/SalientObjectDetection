Code :
Salient Object Detection: A Discriminative Regional Feature Integration Approach
https://github.com/playerkk/drfi_matlab

1. This code does not require any tool set
2. Images should be places in the data folder
3. Before testing, you might want to download our pre-trained Random Forest model, 
which is available at http://jianghz.com/drfi/files/drfiModelMatlab.zip. Put it into the model folder.
4. Run the program demo.m by calling 
> demo 
-----------------------------------------

In order to modify the number of segments 
1. Modify the makeDefaultParameters.m 
para.num_segmentation = 15; % This could be adjusted 

-----------------------------------------

Changes were done to demo to resize the image before using it. 
1. eval_demo.m has the experiments performed for this project 
2. Plots.py was used to generate the plots from the raw probability weights data  
