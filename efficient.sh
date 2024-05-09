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
python3 efficient_3.py "$input_file" "$output_file"