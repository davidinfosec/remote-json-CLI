# Remote JSON Editor

The Remote JSON Editor is a Python script that allows users to remotely edit a JSON file hosted on an FTP server. With this tool, users can add, remove, or list tools within different sections of the JSON file using a command-line interface.

![ShareX_o1sHQIqOfX](https://github.com/davidinfosec/remote-json-CLI/assets/87215831/75879500-6ea2-4252-8b4d-13eb6b5a479b)
![ShareX_MmU6ExHzBl](https://github.com/davidinfosec/remote-json-CLI/assets/87215831/0a39dbec-6e77-48dd-9e58-3a3b166ea3f4)

## Features

- **Add Tool**: Users can add a new tool to the JSON file by specifying the section name, tool name, URL, description, and whether to open the URL in a new tab.
- **Remove Tool**: Users can remove a tool from the JSON file by specifying the section name and the tool name to be removed. If the removal of a tool results in an empty section, that section will be automatically removed from the JSON file.
- **List Tools**: Users can list the names of all tools within the JSON file grouped by their respective sections.
- **User-Friendly Interface**: The script provides a simple and intuitive command-line interface for interacting with the JSON file.

## How to Use

1. Clone the repository to your local machine.
2. Update the FTP server credentials and JSON file path in the `creds.yaml` file to match your setup.
3. Run the script using Python: `python remotejson.py`.
4. Follow the on-screen instructions to add, remove, or list tools within the JSON file.

## Requirements

- Python 3.x
- ftplib (Python FTP library)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
