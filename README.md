# Robocopy GUI  

A simple Python-based GUI for **Robocopy**, allowing users to easily select source and destination folders, view drive information, and execute file copying operations with predefined parameters.  

## Features  
- **Easy-to-use GUI** powered by **Tkinter**  
- **Select source and destination folders** through a file browser  
- **Display drive information** (total size and free space)  
- **Execute Robocopy commands** with standard options  
- **Error handling and success messages**  

## Requirements  
Ensure you have **Python 3.x** installed and that **Robocopy** is available on your Windows system.  

### Install Dependencies  
```sh
pip install tk
```

## Usage  
1. **Clone the repository**  
   ```sh
   git clone https://github.com/hsuehyt/Robocopy.git  
   cd Robocopy  
   ```
2. **Run the script**  
   ```sh
   python Robocopy.py  
   ```  
3. **Select source and destination folders**  
4. **Click "Start Robocopy"** to begin copying  

## Robocopy Parameters Used  
The script executes **Robocopy** with the following options:  
- `/E` - Copy all subdirectories, including empty ones  
- `/XC`, `/XN`, `/XO` - Exclude changed, newer, and older files  
- `/XD` - Exclude system directories (`$RECYCLE.BIN`, `System Volume Information`, etc.)  

## License  
This project is open-source and available under the **MIT License**.  

## Contribution  
Feel free to open issues or submit pull requests for improvements!