import json
from ftplib import FTP
import yaml

def update_json(ftp, filepath, data):
    # Convert data to JSON string
    json_data = json.dumps(data, indent=4)

    # Write JSON string to a temporary file
    with open("temp.json", "w") as temp_file:
        temp_file.write(json_data)

    # Upload the temporary file to the FTP server
    with open("temp.json", "rb") as temp_file:
        ftp.storbinary("STOR " + filepath, temp_file)

    print("JSON file updated successfully!")

def list_tools(json_data):
    # Print the names of all tools
    for section, tools in json_data.items():
        for tool in tools:
            print(tool['tool'])

def main():
    # Load FTP credentials from creds.yaml
    with open("creds.yaml", "r") as yaml_file:
        creds = yaml.safe_load(yaml_file)
    server = creds['server']
    username = creds['username']
    password = creds['password']
    filepath = creds['filepath']

    # Connect to FTP server
    ftp = FTP(server)
    ftp.login(user=username, passwd=password)

    # Retrieve lines from the file
    lines = []
    ftp.retrlines('RETR ' + filepath, lines.append)

    # Concatenate lines into a single string
    json_str = '\n'.join(lines)

    # Parse JSON data
    json_data = json.loads(json_str)

    while True:
        # Prompt user for action
        print("\nWhat would you like to do?")
        print("1. Add a new tool")
        print("2. Remove a tool")
        print("3. List names of tools")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        # Perform action based on user choice
        if choice == "1":
            section = input("Enter section name: ")
            name = input("Enter tool name: ")
            url = input("Enter tool URL: ")
            if not url.startswith("http://") and not url.startswith("https://"):
                # Prepend https:// if it's not already included
                url = "https://" + url
            description = input("Enter tool description: ")
            target_blank = input("Open in new tab (true/false) [default=true]: ").lower() or "true"
            new_tool = {
                "tool": name,
                "url": url,
                "description": description,
                "openInNewTab": target_blank == "true"
            }
            if section in json_data:
                json_data[section].append(new_tool)
            else:
                json_data[section] = [new_tool]
            update_json(ftp, filepath, json_data)
        elif choice == "2":
            section = input("Enter section name: ")
            name = input("Enter tool name to remove: ")
            if section in json_data:
                json_data[section] = [tool for tool in json_data[section] if tool['tool'] != name]
                # Check if section becomes empty after removing the tool
                if not json_data[section]:
                    del json_data[section]
                update_json(ftp, filepath, json_data)
            else:
                print(f"Section '{section}' not found.")
        elif choice == "3":
            list_tools(json_data)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please enter a valid option.")

    # Close FTP connection
    ftp.quit()

if __name__ == "__main__":
    main()
