-- Create a tmp file to compute lifespan
CREATE TEMPORARY TABLE temp_lifespan AS
SELECT band_name AS band_name, IFNULL(split, 2020) - IFNULL(formed, 0) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%';

-- Rank the bands by longevity
SELECT band_name, lifespan
FROM temp_lifespan
ORDER BY lifespan DESC;
