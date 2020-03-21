# Allows the playing of Minecraft from a USB thumbdrive at schools where
# running .exe files is disabled, but Python AND Java are installed on C:\
# The script locates Java executable on C:\, creates a temporary location for %APPDATA%
# on the USB drive, then runs Minecraft.jar on the USB drive.
# Either double-click the startMinecraft.py file, or run it from Idle,
# as the CMD prompt will be disabled by the school
# Original code by NotTarts
# Modified by Inksaver
# Pastebin http://pastebin.com/ZNY7Xs7z
# http://www.minecraftforum.net/forums/mapping-and-modding/minecraft-tools/1260547-minecraft-portable-2-7-2-java-portable-minecraft
import os, sys, subprocess, shutil
from datetime import datetime
import time

class mcpLog():
    def __init__(self, filename):
        # Creating the initial log file/erasing old log
        self.logFilename = filename
        self.logObj = open(self.logFilename,'w')
        self.logObj.close()        

    def write(self, content):
        # Appending to the log
        self.logObj = open(self.logFilename,'a')
        self.logObj.write(content)
        self.logObj.close()

class mcpLauncher():
    def __init__(self, filename):
        log.write('Launching Minecraft...\n')
        self.launcherJar = filename

    def findJava(self, directories):
        log.write('- Searching for Java binaries... ')
        # Going through every directory in the list to find javaw.exe

        for directory in directories:
            binFile = findFile('javaw.exe', directory)
            if binFile:
                self.javaBin = binFile
                log.write('done.\n')
                log.write('- Found Java at {}.\n'.format(os.path.realpath(self.javaBin)))
                return
            else: self.javaBin = None

        if not self.javaBin:
            # Java is needed, so if it's not found the app exits
            log.write('\nError: Could not find Java binaries.')
            sys.exit(1)



    def launch(self): #def launch(self, user, config):
        log.write('- Starting...\n')
        log.write('arguments 1 = ' + str([os.path.realpath(self.javaBin)]) + '\n')
        log.write('arguments 2 = ' + str(['-jar', self.launcherJar]) + '\n')
        arguments = [os.path.realpath(self.javaBin)] + ['-jar', self.launcherJar]
        log.write('arguments = ' + str(arguments) + '\n')
        subprocess.call(arguments)

def findFile(filename, directory):
    for root, dirs, files in os.walk(directory):
        for name in files:
            if name == filename:
                return os.path.join(root, name)

def main():
    #Define global variable for logfile object
    global log
    
    currentDir = sys.path[0] #path[0], is the directory containing the script that was used to invoke the Python interpreter eg "F:\Minecraft Portable" 
    dataDir = os.path.join(currentDir, 'mcp_data') #Join one or more path components intelligently. eg "F:\Minecraft Portable" + \ + "mcp_data"
    launcherDir = os.path.join(dataDir, 'launcher') # Place to save the launcher (minecraft.jar) eg "F:\Minecraft Portable\mcp_data" + \ + "launcher"
    # The following code ensures the .minecraft folder in the USB is used NOT in default %APPDATA%
    os.putenv('APPDATA',dataDir) # Changing AppData locally so Minecraft/external applications store it here. VERY IMPORTANT!
    # Store file path + names in variables
    launcherFile = os.path.join(launcherDir, 'Minecraft.jar') # eg "F:\Minecraft Portable\mcp_data\launcher" + \ + "Minecraft.jar"  
    logFile = os.path.join(dataDir, 'mcp_log.log') # "F:\Minecraft Portable\mcp_data" + \ + "mcp_log.log"
    # Create logFile Object
    log = mcpLog(logFile) # "F:\Minecraft Portable\mcp_data\mcp_log.log"
    
    # Write credits, date, etc to log
    log.write('Minecraft Portable 2.7.2\nby NotTarts. Modified by Inksaver\n\nStarted at {}\nData directory: {}\n\n'.format(datetime.now(), os.path.realpath(dataDir)))
    # Create launcher object
    launcher = mcpLauncher(launcherFile)
    
    # Finding the Java binaries, checking both the 32-bit and 64-bit Program Files directories.
    launcher.findJava([os.path.join(str(os.getenv('ProgramW6432')), 'Java'), os.path.join(str(os.getenv('ProgramFiles(x86)')), 'Java')])    
    launcher.launch() # Launch Minecraft!
    log.write('\nProcess finished.')

# Program starts here    
main()





