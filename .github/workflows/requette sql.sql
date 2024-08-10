CREATE TABLE Livres (
    BookID INTEGER PRIMARY KEY,
    Titre TEXT NOT NULL,
    Auteur TEXT NOT NULL,
    AnnéePublication INTEGER NOT NULL,
    Genre TEXT NOT NULL
);

INSERT INTO Livres (Titre, Auteur, AnnéePublication, Genre) VALUES
('1984', 'George Orwell', 1949, 'Fiction'),
('To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction'),
('Sapiens', 'Yuval Noah Harari', 2011, 'Non-fiction'),
('The Da Vinci Code', 'Dan Brown', 2003, 'Mystery'),
('The Catcher in the Rye', 'J.D. Salinger', 1951, 'Fiction');

SELECT * FROM Livres;

SELECT * FROM Livres WHERE AnnéePublication > 2000;

SELECT * FROM Livres WHERE Genre = 'Fiction';


UPDATE Livres
SET AnnéePublication = 2024
WHERE Titre = '1984';

DELETE FROM Livres
WHERE Titre = 'The Da Vinci Code';

