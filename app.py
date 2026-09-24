import os
import sys

# Route execution to Frontend/app.py
frontend_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Frontend')
os.chdir(frontend_dir)
if frontend_dir not in sys.path:
    sys.path.insert(0, frontend_dir)

app_path = os.path.join(frontend_dir, 'app.py')
with open(app_path, 'r', encoding='utf-8') as f:
    code = compile(f.read(), app_path, 'exec')
    exec(code, globals())
