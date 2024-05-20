# Create a dictionary to hold idx to text mappings from aishell_transcript_v0.8.txt
transcript_dict = {}
with open("/data/aishell1/data_aishell/transcript/aishell_transcript_v0.8.txt", "r") as transcript_file:
    for line in transcript_file:
        line = line.strip()
        parts = line.split(" ")
        idx = parts[0]
        text = "".join(parts[1:])
        transcript_dict[idx] = text

# Open the result file for writing
with open("/data/experiment/wenet/examples/aishell/s1/utils/train/text.txt", "w") as result_file:
    # Open the code_text file and process each line
    with open("/data/experiment/wenet/examples/aishell/s1/utils/train/code_text", "r") as code_file:
        for line in code_file:
            line = line.strip()
            idx = line.split(" ")[0]
            # Check if the idx is in the transcript_dict
            if idx in transcript_dict:
                # Write the combined result to the result file
                result_file.write(idx + " " + transcript_dict[idx] + "\n")

