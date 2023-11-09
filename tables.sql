CREATE TABLE USERS (
    "id" SERIAL PRIMARY KEY,
    "user" VARCHAR(50) NOT NULL,
    "password" VARCHAR(50) NOT NULL
);

CREATE TABLE OFERTA (
    "id" SERIAL PRIMARY KEY,
    "id_produs" VARCHAR(255),
    "titlu" VARCHAR(255),
    "descriere" VARCHAR(1023),
    "pret" VARCHAR(255),
    "photo_urls" VARCHAR(255)[],
    "magazin" VARCHAR(255),
    "parent_url" VARCHAR(255)
)