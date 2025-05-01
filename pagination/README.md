# Pagination Project

This project implements various pagination techniques in Python, focusing on handling large datasets efficiently and providing a good user experience when navigating through data.

## Learning Objectives

By completing this project, you will understand:

1. **Simple Pagination**
   - How to implement basic pagination using page and page_size parameters
   - How to calculate start and end indices for data slicing
   - How to handle edge cases in pagination

2. **Hypermedia Pagination**
   - How to enhance pagination with metadata
   - How to provide navigation information (next page, previous page, total pages)
   - How to implement a more user-friendly pagination system

3. **Deletion-Resilient Pagination**
   - How to handle data deletions between pagination requests
   - How to maintain data consistency when items are removed
   - How to implement robust pagination that doesn't miss items

## Project Structure

The project consists of four Python files:

1. `0-simple_helper_function.py`
   - Contains the `index_range` function that calculates start and end indices for pagination
   - Provides the foundation for all pagination implementations

2. `1-simple_pagination.py`
   - Implements basic pagination using the `Server` class
   - Provides a `get_page` method to retrieve paginated data

3. `2-hypermedia_pagination.py`
   - Extends the basic pagination with hypermedia metadata
   - Implements the `get_hyper` method for enhanced pagination

4. `3-hypermedia_del_pagination.py`
   - Implements deletion-resilient pagination
   - Uses an indexed dataset to handle data deletions

## Requirements

- Python 3.9
- Ubuntu 20.04 LTS
- pycodestyle (version 2.5.*)

## Code Style

- All files must end with a new line
- The first line of all files must be `#!/usr/bin/env python3`
- All code must follow pycodestyle guidelines
- All modules, classes, and functions must have proper documentation
- All functions must be type-annotated

## Documentation Requirements

- Module documentation must explain the purpose of the module
- Function documentation must explain the purpose of the function
- Documentation must be meaningful sentences, not just single words
- Documentation can be verified using:
  ```python
  python3 -c 'print(__import__("my_module").__doc__)'
  python3 -c 'print(__import__("my_module").my_function.__doc__)'
  ```

## Usage

The project uses a CSV file containing popular baby names as the dataset. The pagination implementations can be used to navigate through this data efficiently.

Example usage:
```python
from 1-simple_pagination import Server

server = Server()
page = server.get_page(1, 10)  # Get first 10 items
```

## Testing

The project includes test files for each implementation:
- `0-main.py`
- `1-main.py`
- `2-main.py`
- `3-main.py`

These test files demonstrate the functionality of each pagination implementation and verify that they work as expected. 