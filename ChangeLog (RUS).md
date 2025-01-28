## Console Version

### Version 0.0.1

- Added functionality for automatic email sending:
    - Support for working with a pre-prepared list of email addresses.
    - Ability to attach a preset file to emails.

### Version 0.0.2

- Added the ability to attach a database in XLSX format to emails.

### Version 0.0.3

- Added the ability to choose the database file format: XLSX or XLS.
- Implemented the ability to manually enter the name of the database file (XLSX).
- Added the ability to manually enter the name of the PDF file for attachment.

### Version 0.0.4

- Added support for files in XLS format.

### Version 0.0.5

- Added support for sending emails via the Mail.ru SMTP server.

## Interface Version

### Version 0.0.1

- Released a test version of the program with an interface based on PySide6.

### Version 0.0.2

- Separated the interface rendering and program logic into separate files to improve code readability and maintainability.
- Added a graphical interface for selecting the database file (XLSX/XLS).
- Implemented a graphical interface for selecting the attachment file (PDF).
- Added the ability to use a configuration file in "Key: Value" format for convenient storage and management of program settings.

### Version 0.0.3

- Implemented multithreading for updating the ProgressBar object, preventing the interface from freezing during task execution.
- Changed the logic for processing the configuration file to prevent errors related to incorrect values.
- Added the ability to compile the program into an executable file (EXE) for easier distribution and use.

### Version 0.0.4

- Button labels have been changed to more understandable and user-friendly ones.
- Improved interface readability.
- Added developer contact information to the program interface.

### Version 0.0.5

- Migrated from PySide6 to PySide2 to improve compatibility with different system architectures.

### Version 0.0.6

- Added a settings button (work in progress, WIP) for future program configuration improvements.
- Added a notification label indicating the start of email sending.

### Version 0.0.7

- Added the ability to use files located outside the application folder.
- Improved flexibility in working with file paths.

### Version 0.0.8

- Added full program settings with extended capabilities:
    - Ability to select a configuration file via the file manager.
    - Ability to save the configuration file in the application folder.
    - Implemented the ability to modify the email text in the settings.
    - Added the ability to change the signature text in the email (if present).

### Version 0.0.9

- Added a "Hide/Show Password" button for improved convenience and security.
- All interface interactions are now handled through signals.
- Added a function for automatically selecting the SMTP server based on the sender's email domain.