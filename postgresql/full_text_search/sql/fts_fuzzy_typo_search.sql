
-- The similarity funciton is based on the pg_trgm extension.
-- So, we need to create the extension first.
CREATE EXTENSION pg_trgm;

-- similarity(text, text) → float
-- The similarity function returns a number that indicates how similar two strings are.
-- The number is between 0 and 1, where 1 means the strings are identical.
-- This function is based on the pg_trgm extension, which provides functions and operators for determining the similarity of text values based on trigram matching.
SELECT to_tsquery('balloon |' || string_agg(word, ' | ') )
FROM data_words
WHERE similarity(word, 'balloon') > 0.4;


-- The levenstein distance is a measure of the similarity between two strings.
-- To use the levenshtein distance, we need to create the fuzzystrmatch extension.
CREATE EXTENSION fuzzystrmatch;
-- Use levenshtein distance to find similar words
select levenshtein('abc', 'abd');
