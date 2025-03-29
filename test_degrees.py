import pytest
from degrees import load_data, neighbors_for_person
import os


@pytest.fixture
def setup_data():
    """Load the small dataset for testing"""
    # Save current directory to return to it later
    original_dir = os.getcwd()

    # Change to the directory containing this file
    if os.path.exists("small"):
        load_data("small")
        yield "small"
    else:
        pytest.skip("small dataset directory not found")

    # Return to the original directory
    os.chdir(original_dir)


def test_load_data(setup_data):
    """Test that data loading works correctly"""
    from degrees import people, movies

    # Check that data was loaded
    assert len(people) > 0, "People data should be loaded"
    assert len(movies) > 0, "Movie data should be loaded"

    # Check specific entries from the small dataset
    assert "102" in people, "Kevin Bacon (ID 102) should be in the dataset"
    assert "158" in people, "Tom Hanks (ID 158) should be in the dataset"

    # Check that movies are loaded correctly
    assert "112384" in movies, "Apollo 13 (ID 112384) should be in the dataset"


def test_neighbors_for_person(setup_data):
    """Test that neighbors_for_person returns correct data"""
    # Kevin Bacon's ID in the small dataset is 102
    neighbors = neighbors_for_person("102")

    # Check that neighbors is a set
    assert isinstance(neighbors, set), "neighbors_for_person should return a set"

    # Check that we have at least one neighbor
    assert len(neighbors) > 0, "Kevin Bacon should have neighbors"

    # Neighbors should be tuples of (movie_id, person_id)
    for neighbor in neighbors:
        assert isinstance(neighbor, tuple), "Each neighbor should be a tuple"
        assert (
            len(neighbor) == 2
        ), "Each neighbor should be a (movie_id, person_id) pair"
