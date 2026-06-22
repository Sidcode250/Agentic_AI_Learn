1. install uv = pip install uv

2. Find uv.exe = Get-ChildItem "$env:APPDATA\Python" -Recurse -Filter uv.exe

3. copy the path it gives and paste it here = $env:Path += ";C:\Users\<username>\AppData\Roaming\Python\Python313\Scripts" + test

4. test(uv --version) and add permanantly = 

[Environment]::SetEnvironmentVariable(
    "Path",
    [Environment]::GetEnvironmentVariable("Path","User") +
    ";C:\Users\<username>\AppData\Roaming\Python\Python313\Scripts",
    "User"
)

5. also if path not choosen add it from ctrl+shift+p = D:\Agentic_AI_Learn\RAG_FCC\.venv\Scripts\python.exe