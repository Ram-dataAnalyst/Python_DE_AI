import sys
import subprocess
from pathlib import Path

BASE=Path(sys.argv[1])
print(BASE)

#Create all required folders
folders = ["script", "landing", "data/processing", "data/archive", "data/error", "data/output"]
for folder in folders:
    try:
        (BASE / folder).mkdir(parents=True, exist_ok=True)
        print(f"Created folder {folder}")
    except:
        print(f"Failed to create folders")


#Create requirements.txt (skip if it already exists)
req_file=BASE / "requirements.txt"
try:
    if not  req_file.exists():
        req_file.write_text("pandas\nopenpyxl\npython-dotenv\ngoogle-genai\n")
        print("Created requirements file on ", req_file)
except:
    print("Failed to create requirements file")
finally:
    print("Requirements files Created")

#Create .env placeholder (skip if already configured)
env_file = BASE / ".env"
try:
    if not env_file.exists():
        env_file.write_text("GEMINI_API_KEY=PASTE_YOUR_GEMINI_API_KEY_HERE\n")
except:
    print("Failed to create requirements file")
finally:
    print("Requirements files Created")

# 4. Create initial script placeholder (skip if already exists)
script_file = BASE / "script" / "data_profiler.py"
if not script_file.exists():
    script_file.write_text('import sys\nprint("Running profile on with empty script, ensure to replace with the actual script content:", sys.argv[1] if len(sys.argv) > 1 else "No file")\n')

# 5. Install packages into the current Python environment
print("Installing requirements...")
subprocess.run([sys.executable, "-m", "pip", "install", "-r", str(req_file)])

print("\nSetup completed successfully!")