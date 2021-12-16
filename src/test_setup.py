import sys, os

# Hack to help fix imports in pytest.
# from https://stackoverflow.com/a/47188103
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
