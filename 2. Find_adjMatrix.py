import os
import pandas as pd

# Set working directory
os.chdir(r"D:/Dropbox/nces_distMatrix/2021")

# Make a list of all adj. matrix we want to make
# This list is in miles...
miles = [10, 20]

# Set the "distMatrix" subfolder as the folder to search for data to load.
# This loads all the csv created in "FindDistances_KyleEdit"
search_dir = os.getcwd() + "/distMatrix"

# Loop through all files in that folder to create adj matrix for each state.
for filename in os.listdir(search_dir):
    state = filename[0:2]  # get state substr from filename
    filepath = "distMatrix/" + filename  # get filepath for csv's
    distMatrix = pd.read_csv(filepath)  # load csv's one at a time

    # then loop through miles vector to make one dataset for each mile selection.
    for mile in miles:
        # status update
        print("Computing Adj. Martix for: ", state, "  Miles: ", mile)

        # make temp dataframe so distMatrix does not get overwritten
        temp = pd.DataFrame.copy(distMatrix)

        # Now loop through columns 2 --> len(distMatrix) + 2 (index and python counts at 0 to start) to make conditionals for each column.
        # Column 0 is ncessch ID .. and column 1 is state_abbrev. so skip these...
        for col in range(2, len(temp) + 2):
            colname = temp.columns[col]  # need to get column name for bool comparison to work below.
            temp[colname] = (temp[colname] <= mile).astype(int)  # this line assigns 1 if conditon is true for that col... 0 otherwise

        # Save each unique state/mile combo distance matrix
        flnm = "adjMatrix/" + state + "adj_Matrix" + str(mile) + ".csv"
        temp.to_csv(flnm, index=False)
