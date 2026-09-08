import subprocess

# Start Solara (Recruiter Dashboard) on port 8765
solara_cmd = ["solara", "run", "app.py", "--port", "8765"]

# Start FastAPI (Candidate Scheduling) on port 8000
fastapi_cmd = ["uvicorn", "src.candidate_schedule:app", "--reload", "--port", "8000"]

# Launch both processes
solara_proc = subprocess.Popen(solara_cmd)
fastapi_proc = subprocess.Popen(fastapi_cmd)

# Wait for both to finish (keeps script alive)
solara_proc.wait()
fastapi_proc.wait()
