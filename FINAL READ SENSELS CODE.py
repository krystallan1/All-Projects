import csv
import numpy as np

def read_csv_from_row(file_path, start_row, keyword):
    data = []
    found_keyword = False
    current_row = start_row
    
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for _ in range(start_row):  # Skip rows until the desired start_row
            next(reader, None)
        
        for row in reader:
            if not row:  # Check for a blank line
                if found_keyword:
                    break  # Exit the loop if we found the keyword and reached a blank line
            else:
                if found_keyword:
                    data.append(row)
                if row[0] == keyword:
                    found_keyword = True
            current_row += 1

    return data, current_row

def flatten_list(list_of_lists):
    return [item for sublist in list_of_lists for item in sublist]

def read_sensels(file_path, keyword, num_frames, num_sensels):
    current_row = 1
    row_to_read = current_row

    # Create empty 3D arrays for each section
    total_sensels_left = np.zeros((num_frames, num_sensels))
    total_sensels_right = np.zeros((num_frames, num_sensels))

    heel_left = np.zeros((num_frames, 36))
    heel_right = np.zeros((num_frames, 24))

    midfoot_left = np.zeros((num_frames, 70))
    midfoot_right = np.zeros((num_frames, 50))

    metatarsal_left = np.zeros((num_frames, 67))
    metatarsal_right = np.zeros((num_frames, 60))

    toe_left = np.zeros((num_frames, 43))
    toe_right = np.zeros((num_frames, 41))

    for frame in range(num_frames):
        print("frame number: ", frame)
        for i in range(1, 11):
            result, row_to_read = read_csv_from_row(file_path, row_to_read, keyword)

            # Flatten the list of lists and convert to a 1-dimensional NumPy array
            flattened_result = flatten_list(result)
            numpy_array = np.array(flattened_result)

            if (i%2) == 1: # Left side
                if i == 1:
                    total_sensels_left[frame, :] = numpy_array
                if i == 3:
                    heel_left[frame, :] = numpy_array
                if i == 5:
                    midfoot_left[frame, :] = numpy_array
                if i == 7:
                    metatarsal_left[frame, :] = numpy_array
                if i == 9:
                    toe_left[frame, :] = numpy_array
            else: # Right side
                if i == 2:
                    total_sensels_right[frame, :] = numpy_array
                if i == 4:
                    heel_right[frame, :] = numpy_array
                if i == 6:
                    midfoot_right[frame, :] = numpy_array
                if i == 8:
                    metatarsal_right[frame, :] = numpy_array
                if i == 10:
                    toe_right[frame, :] = numpy_array
    return total_sensels_left, total_sensels_right, heel_left, heel_right, midfoot_left, midfoot_right, metatarsal_left, metatarsal_right, toe_left, toe_right

#! these are inputs into the big function
file_path = 'left crossover start.csv'
keyword = 'SENSELS'
num_frames = 217
num_sensels = 279

total_sensels_left, total_sensels_right, heel_left, heel_right, midfoot_left, midfoot_right, metatarsal_left, metatarsal_right, toe_left, toe_right = read_sensels(file_path, keyword, num_frames, num_sensels)


