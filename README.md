# Degrees

This is a Python program that determines how many “degrees of separation” apart two actors are.

## Usage

To run the program, use the following command:

```bash
$ python degrees.py [directory]
```

Where `[directory]` is the name of the directory containing the dataset (either "large" or "small").

## Example

```bash
$ python degrees.py large
Loading data...
Data loaded.
Name: Emma Watson
Name: Jennifer Lawrence
3 degrees of separation.
1: Emma Watson and Brendan Gleeson starred in Harry Potter and the Order of the Phoenix
2: Brendan Gleeson and Michael Fassbender starred in Trespass Against Us
3: Michael Fassbender and Jennifer Lawrence starred in X-Men: First Class
```

## Data

The data consists of three CSV files:

- `people.csv`: Contains information about actors, including their unique ID, name, and birth year.
- `movies.csv`: Contains information about movies, including their unique ID, title, and release year.
- `stars.csv`: Establishes the relationship between actors and the movies they have starred in.

## Implementation

The `shortest_path` function in `degrees.py` needs to be completed to find the shortest path between two actors using breadth-first search.
