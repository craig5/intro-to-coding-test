#!/usr/bin/env python3


books = {
    "book1": {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "year": 1960
    },
    "book2": {
        "title": "1984",
        "author": "George Orwell",
        "year": 1949
    },
    "book3": {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "year": 1925
    },
    "book4": {
        "title": "One Hundred Years of Solitude",
        "author": "Gabriel García Márquez",
        "year": 1967
    },
    "book5": {
        "title": "Moby Dick",
        "author": "Herman Melville",
        "year": 1851
    },
    "book6": {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "year": 1813
    },
    "book7": {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "year": 1951
    },
    "book8": {
        "title": "To the Lighthouse",
        "author": "Virginia Woolf",
        "year": 1927
    },
    "book9": {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "year": 1937
    },
    "book10": {
        "title": "Brave New World",
        "author": "Aldous Huxley",
        "year": 1932
    },
    "book11": {
        "title": "The Lord of the Rings",
        "author": "J.R.R. Tolkien",
        "year": 1954
    },
    "book12": {
        "title": "Anna Karenina",
        "author": "Leo Tolstoy",
        "year": 1877
    },
    "book13": {
        "title": "Crime and Punishment",
        "author": "Fyodor Dostoevsky",
        "year": 1866
    },
    "book14": {
        "title": "The Brothers Karamazov",
        "author": "Fyodor Dostoevsky",
        "year": 1880
    },
    "book15": {
        "title": "The Picture of Dorian Gray",
        "author": "Oscar Wilde",
        "year": 1890
    },
    "book16": {
        "title": "Don Quixote",
        "author": "Miguel de Cervantes",
        "year": 1605
    },
    "book17": {
        "title": "Jane Eyre",
        "author": "Charlotte Brontë",
        "year": 1847
    },
    "book18": {
        "title": "Wuthering Heights",
        "author": "Emily Brontë",
        "year": 1847
    },
    "book19": {
        "title": "War and Peace",
        "author": "Leo Tolstoy",
        "year": 1869
    },
    "book20": {
        "title": "Frankenstein",
        "author": "Mary Shelley",
        "year": 1818
    },
    "book21": {
        "title": "Gulliver's Travels",
        "author": "Jonathan Swift",
        "year": 1726
    },
    "book22": {
        "title": "The Odyssey",
        "author": "Homer",
        "year": -800
    },
    "book23": {
        "title": "The Adventures of Huckleberry Finn",
        "author": "Mark Twain",
        "year": 1884
    },
    "book24": {
        "title": "The Adventures of Tom Sawyer",
        "author": "Mark Twain",
        "year": 1876
    },
    "book25": {
        "title": "The Divine Comedy",
        "author": "Dante Alighieri",
        "year": 1320
    },
    "book26": {
        "title": "Les Misérables",
        "author": "Victor Hugo",
        "year": 1862
    },
    "book27": {
        "title": "Alice's Adventures in Wonderland",
        "author": "Lewis Carroll",
        "year": 1865
    },
    "book28": {
        "title": "The Iliad",
        "author": "Homer",
        "year": -800
    },
    "book29": {
        "title": "The Count of Monte Cristo",
        "author": "Alexandre Dumas",
        "year": 1844
    },
    "book30": {
        "title": "The War of the Worlds",
        "author": "H.G. Wells",
        "year": 1898
    },
    "book31": {
        "title": "The Sun Also Rises",
        "author": "Ernest Hemingway",
        "year": 1926
    },
    "book32": {
        "title": "The Road",
        "author": "Cormac McCarthy",
        "year": 2006
    },
    "book33": {
        "title": "The Adventures of Sherlock Holmes",
        "author": "Arthur Conan Doyle",
        "year": 1892
    },
    "book34": {
        "title": "The Grapes of Wrath",
        "author": "John Steinbeck",
        "year": 1939
    },
    "book35": {
        "title": "The Wind in the Willows",
        "author": "Kenneth Grahame",
        "year": 1908
    },
    "book36": {
        "title": "The Old Man and the Sea",
        "author": "Ernest Hemingway",
        "year": 1952
    },
    "book37": {
        "title": "Slaughterhouse-Five",
        "author": "Kurt Vonnegut",
        "year": 1969
    },
    "book38": {
        "title": "The Bell Jar",
        "author": "Sylvia Plath",
        "year": 1963
    },
    "book39": {
        "title": "The Canterbury Tales",
        "author": "Geoffrey Chaucer",
        "year": 1400
    },
    "book40": {
        "title": "Middlemarch",
        "author": "George Eliot",
        "year": 1871
    },
    "book41": {
        "title": "Gone with the Wind",
        "author": "Margaret Mitchell",
        "year": 1936
    },
    "book42": {
        "title": "The Secret Garden",
        "author": "Frances Hodgson Burnett",
        "year": 1911
    },
    "book43": {
        "title": "A Tale of Two Cities",
        "author": "Charles Dickens",
        "year": 1859
    },
    "book44": {
        "title": "Dracula",
        "author": "Bram Stoker",
        "year": 1897
    },
    "book45": {
        "title": "The Fountainhead",
        "author": "Ayn Rand",
        "year": 1943
    },
    "book46": {
        "title": "The Scarlet Letter",
        "author": "Nathaniel Hawthorne",
        "year": 1850
    },
    "book47": {
        "title": "Sense and Sensibility",
        "author": "Jane Austen",
        "year": 1811
    },
    "book48": {
        "title": "Emma",
        "author": "Jane Austen",
        "year": 1815
    },
    "book49": {
        "title": "Oliver Twist",
        "author": "Charles Dickens",
        "year": 1837
    },
    "book50": {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "year": 1937
    }
}


year_counts = {}
for book_id, book_info in books.items():
    title = book_info["title"]
    author = book_info["author"]
    year = book_info["year"]
    print(f"{title} -> By {author}  ({year})")
    if year not in year_counts:
        year_counts[year] = 0
    year_counts[year] += 1
