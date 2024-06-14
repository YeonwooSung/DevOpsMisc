--
-- Refernce: <https://rachbelaid.com/postgres-full-text-search-is-good-enough/>
--

CREATE TABLE author(
   id SERIAL PRIMARY KEY,
   name TEXT NOT NULL
);

CREATE TABLE post(
   id SERIAL PRIMARY KEY,
   title TEXT NOT NULL,
   content TEXT NOT NULL,
   author_id INT NOT NULL references author(id) 
);

CREATE TABLE tag(
   id SERIAL PRIMARY KEY,
   name TEXT NOT NULL 
);

CREATE TABLE posts_tags(
   post_id INT NOT NULL references post(id),
   tag_id INT NOT NULL references tag(id)
 );

INSERT INTO author (id, name) 
VALUES (1, 'Pete Graham'), 
       (2, 'Rachid Belaid'), 
       (3, 'Robert Berry');

INSERT INTO tag (id, name) 
VALUES (1, 'scifi'), 
       (2, 'politics'), 
       (3, 'science');

INSERT INTO post (id, title, content, author_id) 
VALUES (1, 'Endangered species', 
        'Pandas are an endangered species', 1 ), 
       (2, 'Freedom of Speech', 
        'Freedom of speech is a necessary right', 2), 
       (3, 'Star Wars vs Star Trek', 
        'Few words from a big fan', 3);


INSERT INTO posts_tags (post_id, tag_id) 
VALUES (1, 3), 
       (2, 2), 
       (3, 1);


-- For each post, we want to concatenate the title, content, author name, and tags into a single document.
-- We will use this document to perform full-text search.
-- 
-- As we are grouping by post and author, we are using string_agg() as the aggregate function because
-- multiple tag can be associated to a post.
-- Even if author is a foreign key and a post cannot have more than one author, 
-- it is required to add an aggregate function for author or to add author to the GROUP BY.
--
-- We also used coalesce().
-- When a value can be NULL then it's good practice to use the coalesce() function, 
-- otherwise the concatenation will result in a NULL value too.
SELECT
    post.title || ' ' || 
    post.content || ' ' ||
    author.name || ' ' ||
    coalesce((string_agg(tag.name, ' ')), '') as document
FROM post
JOIN author ON author.id = post.author_id
JOIN posts_tags ON posts_tags.post_id = posts_tags.tag_id
JOIN tag ON tag.id = posts_tags.tag_id
GROUP BY post.id, author.id;


-- We can use the to_tsvector() function to convert the document into a tsvector.
-- By using the || operator, we can concatenate the tsvector of each column.
-- Again, we use coalesce() to handle NULL values that could be presented due to the LEFT JOIN.
SELECT to_tsvector(post.title) || 
       to_tsvector(post.content) ||
       to_tsvector(author.name) ||
       to_tsvector(coalesce((string_agg(tag.name, ' ')), '')) as document
FROM post
JOIN author ON author.id = post.author_id
JOIN posts_tags ON posts_tags.post_id = posts_tags.tag_id
JOIN tag ON tag.id = posts_tags.tag_id
GROUP BY post.id, author.id;


--
-- Create a search configuration for the French language.
-- Build a new text search config with support for unaccented characters.
--
-- By configuring the mapping for hword, hword_part, and word to use the unaccent and french_stem dictionaries,
-- we can perform full-text search queries in French.
-- This makes the postgres to apply unaccent first and building the tsvector from the result.
--
CREATE TEXT SEARCH CONFIGURATION fr ( COPY = french );
ALTER TEXT SEARCH CONFIGURATION fr ALTER MAPPING
FOR hword, hword_part, word WITH unaccent, french_stem;
