import argparse
import os

def parse():
    # Parse command-line arguments for source and destination paths
    parser = argparse.ArgumentParser(description="Make your python script one lined.")
    parser.add_argument('-p', '--path', required=True, help='Source path')
    parser.add_argument('-d', '--destination', required=True, help='Destination path')
    args = parser.parse_args()
    path = args.path
    destination = args.destination
    return path, destination

def main():
    # Get source and destination paths from arguments
    path, destination = parse()
    # Get the code from the specified file
    code = get_code(path)
    # Format the code to be one line
    formatted_code = f'exec("""{format_code(code)}""")'
    #Format the destination
    destination = os.path.join(destination, "onelined-" + os.path.basename(path))
    # Write the formatted code to the destination file
    write_code(destination, formatted_code)

def format_code(code):
    # Replace all newlines in code for one-lining
    finalcode = ""
    for i in range(len(code)):
        if code[i] == '\n':
            finalcode += '\\n'
        elif code[i] == 'n' and code[i-1] == '\\':
            finalcode += '\n'
        else:
            finalcode += code[i]
    return finalcode
            
def get_code(path):
    result = ""
    with open(path, 'r', encoding="utf-8") as f:
        for line in f:
            if line.endswith('\n'):
                line = line[:-1]
            result += format_code(line) + "\n"
        return result
    
def write_code(destination, code):
    with open(destination, 'w', encoding="utf-8") as f:
        f.write(code)

if __name__ == "__main__":          
    main()