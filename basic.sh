#datapoints/in1.txt

# #!/bin/bash

# # Check if the correct number of arguments are provided
# if [ "$#" -ne 2 ]; then
#     echo "Usage: $0 <input_file> <output_file>"
#     exit 1
# fi

# # Assign input and output file names to variables
# input_file="$1"
# output_file="$2"

# # Check if the input file exists
# if [ ! -f "$input_file" ]; then
#     echo "Error: Input file '$input_file' not found."
#     exit 1
# fi

# # Run the Python script with the provided arguments
# python3 basic_3.py "$input_file" "$output_file"

#!/bin/bash    

# Check if exactly two arguments are provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 input_file output_file"
    exit 1
fi

# Assign arguments to variables
input_file="$1"
output_file="$2"

# Run the Python script with input and output file paths
python basic_3.py "$input_file" "$output_file"