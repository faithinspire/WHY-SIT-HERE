const fs = require('fs');
const path = require('path');

// docx is a zip — use built-in zlib + manual zip parsing via Buffer
// Simpler: just read the raw XML from the zip using Node's built-in
const { execSync } = require('child_process');

// Extract word/document.xml from the docx (which is a zip file)
const AdmZip = (() => {
  try { return require('adm-zip'); } catch(e) { return null; }
})();

if (!AdmZip) {
  // Fallback: use PowerShell to extract
  const ps = `
    Add-Type -AssemblyName System.IO.Compression.FileSystem
    $zip = [System.IO.Compression.ZipFile]::OpenRead('WHY SIT HERE AND DIE.docx')
    $entry = $zip.Entries | Where-Object { $_.FullName -eq 'word/document.xml' }
    $stream = $entry.Open()
    $reader = New-Object System.IO.StreamReader($stream)
    $content = $reader.ReadToEnd()
    $reader.Close(); $zip.Dispose()
    $content | Out-File -FilePath 'document.xml' -Encoding UTF8
  `;
  fs.writeFileSync('extract.ps1', ps);
  execSync('powershell -ExecutionPolicy Bypass -File extract.ps1');
  console.log('Extracted via PowerShell');
} else {
  const zip = new AdmZip('WHY SIT HERE AND DIE.docx');
  const entry = zip.getEntry('word/document.xml');
  fs.writeFileSync('document.xml', entry.getData().toString('utf8'));
  console.log('Extracted via AdmZip');
}
