const fs = require('fs');
const { execSync } = require('child_process');

const ps = `Add-Type -AssemblyName System.IO.Compression.FileSystem; $zip = [System.IO.Compression.ZipFile]::OpenRead('WHY SIT HERE AND DIE.docx'); $entry = $zip.Entries | Where-Object { $_.FullName -eq 'word/document.xml' }; $stream = $entry.Open(); $reader = New-Object System.IO.StreamReader($stream); $content = $reader.ReadToEnd(); $reader.Close(); $zip.Dispose(); $content | Out-File -FilePath 'document.xml' -Encoding UTF8`;

fs.writeFileSync('extract.ps1', ps, 'utf8');
execSync('powershell.exe -ExecutionPolicy Bypass -File extract.ps1', {stdio:'inherit'});
console.log('Done');
