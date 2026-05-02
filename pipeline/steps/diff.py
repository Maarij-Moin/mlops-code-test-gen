import difflib

def compute_diff(old_code, new_code):
    diff = difflib.unified_diff(
        old_code.splitlines(),
        new_code.splitlines()
    )
    return "\n".join(diff)