import pytest
import os
from ramile import *

# Get the absolute path to the directory containing this file
TEST_DIR = os.path.dirname(os.path.abspath(__file__))

def test_csharp_app():
    """ Test with csharp app project.
    """
    data_dir = os.path.join(TEST_DIR, 'data/csharp-app')
    output_file = os.path.join(data_dir, 'test-output.txt')
    
    # Ensure clean state
    if os.path.exists(output_file):
        os.remove(output_file)
        
    project = Project(data_dir, 3000, output_file)
    project.run()
    
    # Clean up
    if os.path.exists(output_file):
        os.remove(output_file)

    assert project.info.lines_extracted == 11
    assert project.info.lines_skipped_blank == 1
    assert project.info.lines_skipped_comments == 6
    return
