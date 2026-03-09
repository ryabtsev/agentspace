with open('index.html', 'r') as f:
    lines = f.readlines()

header_end_idx = -1
agnostic_start_idx = -1
block_start_idx = -1
block_end_idx = -1

for i, line in enumerate(lines):
    if "</header>" in line:
        header_end_idx = i
    elif '<div class="agnostic">' in line:
        agnostic_start_idx = i
    elif '<div class="section">' in line and '<h2>3. Directory Examples (Use Cases)</h2>' in lines[i+1]:
        block_start_idx = i
    elif block_start_idx != -1 and '</div>' in line and i > block_start_idx + 20 and block_end_idx == -1:
        # We know from cat -n that the block ends with 3 </div>s, wait we know it ends at line 125, which is index 124
        pass

# Hardcode based on what we found
block_start = 100 - 1
block_end = 125

block_lines = lines[block_start:block_end]
del lines[block_start:block_end]

# Find header end again since we deleted lines
for i, line in enumerate(lines):
    if "</header>" in line:
        header_end_idx = i
        break

lines = lines[:header_end_idx + 1] + ['\n'] + block_lines + ['\n'] + lines[header_end_idx + 1:]

with open('index.html', 'w') as f:
    f.writelines(lines)
