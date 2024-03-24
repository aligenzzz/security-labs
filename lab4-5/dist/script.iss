; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{B8C5F168-D3BD-4B33-BBB5-001A88F96918}
AppName=App
AppVersion=1.0
;AppVerName=App 1.0
AppPublisher=My Company, Inc.
AppPublisherURL=https://www.example.com/
AppSupportURL=https://www.example.com/
AppUpdatesURL=https://www.example.com/
DefaultDirName={autopf}\App
DefaultGroupName=App
AllowNoIcons=yes
; Uncomment the following line to run in non administrative install mode (install for current user only.)
;PrivilegesRequired=lowest
OutputDir=D:\Repositories\security-labs\lab4-5\App
OutputBaseFilename=setup
Password=alina
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "D:\Repositories\security-labs\lab4-5\dist\main.exe"; DestDir: "{app}"; Flags: ignoreversion
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{group}\App"; Filename: "{app}\main.exe"
Name: "{group}\{cm:ProgramOnTheWeb,App}"; Filename: "https://www.example.com/"
Name: "{group}\{cm:UninstallProgram,App}"; Filename: "{uninstallexe}"
Name: "{autodesktop}\App"; Filename: "{app}\main.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\main.exe"; Description: "{cm:LaunchProgram,App}"; Flags: nowait postinstall skipifsilent

[Code]
procedure CurStepChanged(CurStep: TSetupStep);
var
  FilePath: String;
  ExpectedHash: String;
  FileHash: String;
begin
  if (CurStep = ssPostInstall) then
  begin
    FilePath := ExpandConstant('{app}\main.exe');
    ExpectedHash := '01f4abdf3d12b1daf66ea0a77b75fab62c2148f0';

    FileHash := GetSHA1OfFile(FilePath);

    Log('FileHash: ' + FileHash);
    Log('ExpectedHash: ' + ExpectedHash);


    if (FileHash <> ExpectedHash) then
    begin
      MsgBox('Invalid file!', mbError, MB_OK);
      Abort;
    end;
  end;
end;