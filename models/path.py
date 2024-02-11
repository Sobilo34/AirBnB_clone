#!/usr/bin/env python3

import sys

# Iterate over sys.path and modify the elements
sys.path = [path.replace('/models', '') if path.startswith('/AirBnB_clone/models') else path for path in sys.path]

# Print the modified sys.path
print(sys.path)
