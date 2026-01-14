def run_code(code):
    """
    Executes Python code safely and returns the output.
    """
    import sys
    import io

    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()

    try:
        exec(code, {})
        output = redirected_output.getvalue()
    except Exception as e:
        output = f"Error: {e}"
    finally:
        sys.stdout = old_stdout

    return output

