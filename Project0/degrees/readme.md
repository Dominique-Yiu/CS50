## Variables/Functions Definitions
- names(dict) | name -> person_ids {including multiple names}
- people(dict) | person_id -> name, birth, movies(set)
- movies(dict) | movie_id -> title, year, stars(set)

- load_data: loads data from people.csv/stars.csv/movies.csv
- main: print the result of one of the shortest path (if it has), or return None when there exists no shortest path.
- shortest_path: returns the shortest list of (movies, person_id) pairs
- person_id_for_name: returns person_id of the person's name
- neighbor_for_person: returns (movies, person_id) pairs that relates to the given person

## Use breadth-first search to find the shortest path
1. push source
    source
2. push source's neighbors
    source | 1st neighbor | 2nd neighbor | 3rd neighbor ...
3. pop source
    1st neighbor | 2nd neighbor | 3rd neighbor ...
4. push 1st neighbor's neighbors
5. pop 1st neighbor
6. repeat the steps until it finds the target, or return None when the queue is empty


    states -> people

