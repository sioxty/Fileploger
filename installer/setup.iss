[Setup]
AppName=Fileploger
AppVersion=1.0
DefaultDirName={autopf}\Fileploger
DefaultGroupName=Fileploger
SetupIconFile=D:\project\Fileploger\build\exe.win-amd64-3.11\Icon.ico 

[Files]
Source: "D:\project\Fileploger\build\exe.win-amd64-3.11\Fileploger.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\project\Fileploger\build\exe.win-amd64-3.11\frozen_application_license.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\project\Fileploger\build\exe.win-amd64-3.11\Icon.ico"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\project\Fileploger\build\exe.win-amd64-3.11\python311.dll"; DestDir: "{app}"; Flags: ignoreversion

Source: "D:\project\Fileploger\build\exe.win-amd64-3.11\lib\*"; DestDir: "{app}\lib"; Flags: recursesubdirs createallsubdirs
Source: "D:\project\Fileploger\build\exe.win-amd64-3.11\settings\*"; DestDir: "{app}\settings"; Flags: recursesubdirs createallsubdirs
Source: "D:\project\Fileploger\build\exe.win-amd64-3.11\share\*"; DestDir: "{app}\share"; Flags: recursesubdirs createallsubdirs

[Icons]
Name: "{autodesktop}\Fileploger"; Filename: "{app}\Fileploger.exe"; IconFilename: "{app}\Icon.ico"  
Name: "{autoprograms}\Fileploger"; Filename: "{app}\Fileploger.exe"; IconFilename: "{app}\Icon.ico" 
