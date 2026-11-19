CREATE TABLE IF NOT EXISTS photos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT NOT NULL,
    taken_date TEXT,
    location TEXT,
    description TEXT,
    deleted BOOLEAN NOT NULL DEFAULT 0
);