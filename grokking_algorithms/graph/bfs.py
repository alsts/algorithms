from collections import deque

graph = {
    "you": ["alice", "bob", "claire"],
    "bob": ["anuj", "peggy"],
    "alice": ["peggy"],
    "claire": ["thom", "jonny"],
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jonny": []
}


def person_is_seller(person):
    return person[-1] == 'm'


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []

    while len(search_queue) > 0:
        person = search_queue.popleft()

        if not (person in searched):
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                person_neighbours = graph[person]
                search_queue += person_neighbours
                searched.append(person)
    return False


search("you")
