from pipeline.steps.ingest import load_code
from pipeline.steps.diff import compute_diff
from pipeline.steps.generate import generate_tests

def run_pipeline(repo_url, commit_id):
    old_code, new_code = load_code(repo_url, commit_id)
    
    diff = compute_diff(old_code, new_code)
    
    tests = generate_tests(diff)
    
    return tests