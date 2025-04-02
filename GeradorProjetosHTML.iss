[Setup]
AppName=GeradorProjetosHTML
AppVersion=2.0
DefaultDirName={pf}\GeradorProjetosHTML
OutputDir=.
OutputBaseFilename=Setup_GeradorProjetosHTML
SetupIconFile="C:\Users\Prof. Wellington\Downloads\professor.ico"

[Files]
Source: "C:\Projetos\Projetos Python\geradorHTML\dist\geradorHTML.exe"; DestDir: "{app}"

[Icons]
Name: "{commondesktop}\GeradorProjetosHTML"; Filename: "{app}\geradorHTML.exe"; IconFilename: "{app}\geradorHTML.exe"

[Run]
Filename: "{app}\geradorHTML.exe"; Description: "Executar Gerador de Projetos HTML"; Flags: nowait postinstall skipifsilent
