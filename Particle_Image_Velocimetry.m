% Code written by Krystal Lan
% November 2023

% Goal: process data obtained from Particle Image Velocimetry of an airfoil
% and plot velocity vectors after eliminating all outliers

% Clear the MATLAB workspace and close existing figures
clc
clear all
close all

% Ask user to input filename header
filename_prompt = "Enter the filename header: ";
fileNameHeader = input(filename_prompt, 's');
% Ask user to input number of files to analyze
numfiles_prompt = "Enter the number of files to analyze: ";
numFiles = input(numfiles_prompt);
% Ask user to input characteristic length of the model
characteristicLength_prompt = "Enter the characteristic length of the model (mm): ";
characteristicLength = input(characteristicLength_prompt)/1000;

% Create 3D arrays to store data
uData = zeros([29, 39, numFiles]);
vData = zeros([29, 39, numFiles]);

% Load data into 3D arrays
for n = 1:numFiles
    file = sprintf('%s_%04d', fileNameHeader, n);
    load(file)
    uData(:, :, n) = u;
    vData(:, :, n) = v;
end

% Iterate through the entire array and eliminate all outliers
flag = true; % flag to indicate if a value in the array has been changed
while flag == true
    flag = false;
    uMean = mean(uData, 3, "omitnan");
    vMean = mean(vData, 3, "omitnan");
    uStdDev = std(uData, 0, 3, "omitnan");
    vStdDev = std(vData, 0, 3, "omitnan");
    for n = 1:numFiles
        for i = 1:29
            for j = 1:39
                if (uData(i, j, n) - uMean(i,j)) < (-uStdDev(i,j)*2) || (uData(i, j, n) - uMean(i,j)) > (uStdDev(i,j)*2) || (vData(i,j,n) - vMean(i,j)) < (-vStdDev(i,j)*2) || (vData(i,j,n) - vMean(i,j)) > (vStdDev(i,j)*2) 
                    uData(i, j, n) = NaN; 
                    vData(i, j, n) = NaN;
                    flag = true;
                end 
            end
        end
    end
end

uAvg = mean(uData, 3, "omitnan");
vAvg = mean(vData, 3, "omitnan");

% Create the plot
quiver(x, flipud(y), uAvg, -vAvg);
xlabel('X position (m)');
ylabel('Y position (m)');
axis equal;

% Calculations for average velocity and Reynold's number 
vMean = sqrt(uAvg.^2 + vAvg.^2);
maxVelocity = max(vMean(:));
reynoldsNum = (1000*maxVelocity*characteristicLength)/0.001;
maxReynoldsNum = max(reynoldsNum(:));
fprintf('Max Velocity: %f\n', maxVelocity)
fprintf('Re: %f\n', maxReynoldsNum)
